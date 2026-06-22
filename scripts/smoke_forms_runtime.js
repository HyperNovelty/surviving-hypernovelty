#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.resolve(__dirname, "..");
const RUNTIME = fs.readFileSync(path.join(ROOT, "forms/shared/form_runtime.js"), "utf8");
const FORMS = [
  "forms/agent-identity-scope-roster.html",
  "forms/ai-use-clarity-micro-policy-card.html",
  "forms/adaptation-debt-ledger.html",
  "forms/visible-thinking-repair-ticket.html",
  "forms/platformized-news-diet-receipt.html",
];

function makeDocument() {
  const registry = {};

  class Element {
    constructor(tagName) {
      this.tagName = tagName.toUpperCase();
      this.children = [];
      this.listeners = {};
      this.attributes = {};
      this.style = {};
      this.value = "";
      this.textContent = "";
      this.className = "";
    }

    set id(value) {
      this._id = value;
      if (value) registry[value] = this;
    }

    get id() {
      return this._id;
    }

    appendChild(child) {
      this.children.push(child);
      child.parentNode = this;
      return child;
    }

    removeChild(child) {
      this.children = this.children.filter((item) => item !== child);
      return child;
    }

    setAttribute(name, value) {
      this.attributes[name] = value;
      if (name === "id") this.id = value;
    }

    addEventListener(type, handler) {
      if (!this.listeners[type]) this.listeners[type] = [];
      this.listeners[type].push(handler);
    }

    dispatchEvent(type) {
      (this.listeners[type] || []).forEach((handler) => handler({ target: this }));
    }

    click() {
      this.dispatchEvent("click");
    }

    select() {}
  }

  const document = {
    body: new Element("body"),
    domReadyHandlers: [],
    createElement: (tagName) => new Element(tagName),
    getElementById: (id) => registry[id] || null,
    addEventListener: (type, handler) => {
      if (type === "DOMContentLoaded") document.domReadyHandlers.push(handler);
    },
    execCommand: () => true,
  };

  [
    "form-title",
    "form-summary",
    "boundary-text",
    "source-links",
    "primitive-form",
    "copy-markdown",
    "download-markdown",
    "download-json",
    "reset-example",
    "clear-draft",
    "markdown-preview",
    "form-status",
  ].forEach((id) => {
    const element = document.createElement(id === "primitive-form" ? "form" : "div");
    element.id = id;
    document.body.appendChild(element);
  });

  return document;
}

function makeStorage(initial) {
  return {
    data: initial,
    getItem(key) {
      return Object.prototype.hasOwnProperty.call(this.data, key) ? this.data[key] : null;
    },
    setItem(key, value) {
      this.data[key] = String(value);
    },
    removeItem(key) {
      delete this.data[key];
    },
  };
}

function runForm(relPath, storageData) {
  const html = fs.readFileSync(path.join(ROOT, relPath), "utf8");
  const document = makeDocument();
  const context = {
    console,
    document,
    navigator: {},
    localStorage: makeStorage(storageData),
    Blob: function Blob(parts, options) {
      this.parts = parts;
      this.options = options;
    },
    URL: {
      createObjectURL: () => "blob:local-smoke",
      revokeObjectURL: () => {},
    },
  };
  context.window = context;
  vm.createContext(context);

  for (const match of html.matchAll(/<script>([\s\S]*?)<\/script>/g)) {
    vm.runInContext(match[1], context, { filename: relPath });
  }
  vm.runInContext(RUNTIME, context, { filename: "forms/shared/form_runtime.js" });
  document.domReadyHandlers.forEach((handler) => handler());
  return context;
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

for (const relPath of FORMS) {
  const storage = {};
  const firstRun = runForm(relPath, storage);
  const spec = firstRun.FORM_SPEC;
  const key = firstRun.FormRuntime.draftKey(spec);
  const firstField = spec.fields[0].id;
  const firstInput = firstRun.document.getElementById(firstField);
  const draftValue = "Runtime draft smoke: " + spec.slug;

  firstInput.value = draftValue;
  firstInput.dispatchEvent("input");
  assert(storage[key], `${relPath} did not save an edited draft`);

  const secondRun = runForm(relPath, storage);
  assert(
    secondRun.document.getElementById(firstField).value === draftValue,
    `${relPath} did not restore saved draft`
  );
  assert(
    /restored/i.test(secondRun.document.getElementById("form-status").textContent),
    `${relPath} did not report restored draft`
  );

  secondRun.document.getElementById("clear-draft").click();
  assert(!storage[key], `${relPath} did not clear saved draft`);
  assert(
    secondRun.document.getElementById(firstField).value === spec.example[firstField],
    `${relPath} did not reset to example after clear draft`
  );

  const importJson = JSON.stringify(spec.toJson(spec.example));
  secondRun.document.getElementById("import-json").value = importJson;
  secondRun.document.getElementById("load-json").click();
  assert(storage[key], `${relPath} did not save imported JSON as draft`);
  assert(
    /saved as local draft/i.test(secondRun.document.getElementById("import-status").textContent),
    `${relPath} did not report imported draft save`
  );
}

console.log("forms_runtime_smoke=ok");
console.log("forms_checked=", FORMS.length);
