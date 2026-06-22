(function () {
  "use strict";

  var BOUNDARY_TEXT = "Local review aid only; no legal/compliance/security/academic-integrity authority; no public/account/spend/outreach/deploy actions.";

  function byId(id) {
    return document.getElementById(id);
  }

  function normalizeLines(value) {
    return String(value || "")
      .split(/\r?\n/)
      .map(function (line) { return line.trim(); })
      .filter(Boolean);
  }

  function parseRows(value, columns) {
    return normalizeLines(value).map(function (line) {
      var parts = splitRow(line).map(function (part) { return part.trim(); });
      var row = {};
      columns.forEach(function (column, index) {
        row[column] = parts[index] || "";
      });
      return row;
    });
  }

  function splitRow(line) {
    var parts = [];
    var current = "";
    var escaped = false;
    String(line || "").split("").forEach(function (char) {
      if (escaped) {
        current += char;
        escaped = false;
      } else if (char === "\\") {
        escaped = true;
      } else if (char === "|") {
        parts.push(current);
        current = "";
      } else {
        current += char;
      }
    });
    if (escaped) current += "\\";
    parts.push(current);
    return parts;
  }

  function splitList(value) {
    if (Array.isArray(value)) return value;
    return normalizeLines(value);
  }

  function joinList(value) {
    return splitList(value).join("\n");
  }

  function rowText(rows, columns) {
    return (Array.isArray(rows) ? rows : []).map(function (row) {
      return columns.map(function (column) {
        var value = row && row[column];
        if (Array.isArray(value)) value = value.join(", ");
        if (typeof value === "boolean") value = value ? "yes" : "no";
        return escapeCell(value);
      }).join(" | ");
    }).join("\n");
  }

  function yesNo(value) {
    if (typeof value === "boolean") return value;
    return /^(yes|true|required)$/i.test(String(value || "").trim());
  }

  function escapeCell(value) {
    return String(value == null ? "" : value).replace(/\|/g, "\\|").replace(/\r?\n/g, " ");
  }

  function list(values) {
    return values.length ? values.map(function (item) { return "- " + item; }).join("\n") : "- ";
  }

  function table(headers, rows) {
    return [
      "| " + headers.map(escapeCell).join(" | ") + " |",
      "| " + headers.map(function () { return "---"; }).join(" | ") + " |"
    ].concat(rows.map(function (row) {
      return "| " + row.map(escapeCell).join(" | ") + " |";
    })).join("\n");
  }

  function download(filename, mimeType, content) {
    var blob = new Blob([content], { type: mimeType });
    var url = URL.createObjectURL(blob);
    var link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  function setStatus(text) {
    var status = byId("form-status");
    if (status) status.textContent = text;
  }

  function draftKey(spec) {
    return "surviving-hypernovelty:form-draft:" + spec.slug;
  }

  function readDraft(spec) {
    try {
      var raw = window.localStorage && window.localStorage.getItem(draftKey(spec));
      var parsed = raw ? JSON.parse(raw) : null;
      return parsed && !Array.isArray(parsed) && typeof parsed === "object" ? parsed : null;
    } catch (err) {
      return null;
    }
  }

  function saveDraft(spec, message) {
    try {
      if (!window.localStorage) return;
      window.localStorage.setItem(draftKey(spec), JSON.stringify(collect(spec)));
      setStatus(message || "Local draft saved.");
    } catch (err) {
      setStatus("Local draft could not be saved in this browser.");
    }
  }

  function clearDraft(spec) {
    try {
      if (window.localStorage) window.localStorage.removeItem(draftKey(spec));
    } catch (err) {
      setStatus("Local draft could not be cleared in this browser.");
    }
  }

  function collect(spec) {
    var data = {};
    spec.fields.forEach(function (field) {
      var node = byId(field.id);
      data[field.id] = node ? node.value : "";
    });
    return data;
  }

  function fill(spec, values) {
    spec.fields.forEach(function (field) {
      var node = byId(field.id);
      if (node) node.value = values[field.id] == null ? "" : values[field.id];
    });
  }

  function renderImportPanel() {
    var form = byId("primitive-form");
    var panel = document.createElement("section");
    panel.className = "import-panel";

    var heading = document.createElement("h2");
    heading.textContent = "Import JSON";
    panel.appendChild(heading);

    var label = document.createElement("label");
    label.setAttribute("for", "import-json");
    label.textContent = "Paste JSON exported from this form or matching the linked schema";
    panel.appendChild(label);

    var area = document.createElement("textarea");
    area.id = "import-json";
    area.rows = 8;
    area.spellcheck = false;
    panel.appendChild(area);

    var actions = document.createElement("div");
    actions.className = "actions import-actions";
    var load = document.createElement("button");
    load.type = "button";
    load.id = "load-json";
    load.textContent = "Load JSON into Form";
    actions.appendChild(load);
    panel.appendChild(actions);

    var message = document.createElement("p");
    message.id = "import-status";
    message.className = "status";
    panel.appendChild(message);
    form.appendChild(panel);
  }

  function validateImport(spec, json) {
    var required = spec.requiredFields || [];
    var missing = required.filter(function (field) {
      return json[field] == null || json[field] === "";
    });
    if (missing.length) return "Missing required field(s): " + missing.join(", ");
    return "";
  }

  function importJson() {
    var spec = window.FORM_SPEC;
    var area = byId("import-json");
    var message = byId("import-status");
    var raw = area ? area.value.trim() : "";
    if (!raw) {
      if (message) message.textContent = "Paste JSON before loading.";
      return;
    }
    var parsed;
    try {
      parsed = JSON.parse(raw);
    } catch (err) {
      if (message) message.textContent = "Malformed JSON: " + err.message;
      return;
    }
    if (!parsed || Array.isArray(parsed) || typeof parsed !== "object") {
      if (message) message.textContent = "JSON must be an object.";
      return;
    }
    var validationError = validateImport(spec, parsed);
    if (validationError) {
      if (message) message.textContent = validationError;
      return;
    }
    var values = spec.fromJson ? spec.fromJson(parsed) : parsed;
    fill(spec, values);
    updatePreview();
    saveDraft(spec, "JSON loaded and saved as local draft.");
    if (message) message.textContent = "JSON loaded into form and saved as local draft.";
  }

  function exportJson(spec) {
    return JSON.stringify(spec.toJson(collect(spec)), null, 2) + "\n";
  }

  function renderForm(spec) {
    var form = byId("primitive-form");
    spec.fields.forEach(function (field) {
      var wrap = document.createElement("div");
      wrap.className = "field";
      var label = document.createElement("label");
      label.setAttribute("for", field.id);
      label.textContent = field.label;
      wrap.appendChild(label);

      var input;
      if (field.type === "textarea") {
        input = document.createElement("textarea");
        input.rows = field.rows || 4;
      } else if (field.type === "select") {
        input = document.createElement("select");
        (field.options || []).forEach(function (option) {
          var opt = document.createElement("option");
          opt.value = option;
          opt.textContent = option;
          input.appendChild(opt);
        });
      } else {
        input = document.createElement("input");
        input.type = field.type || "text";
      }
      input.id = field.id;
      input.name = field.id;
      input.addEventListener("input", function () {
        updatePreview();
        saveDraft(window.FORM_SPEC);
      });
      input.addEventListener("change", function () {
        updatePreview();
        saveDraft(window.FORM_SPEC);
      });
      wrap.appendChild(input);

      if (field.hint) {
        var hint = document.createElement("p");
        hint.className = "hint";
        hint.textContent = field.hint;
        wrap.appendChild(hint);
      }
      form.appendChild(wrap);
    });
  }

  function updatePreview() {
    var spec = window.FORM_SPEC;
    var markdown = spec.toMarkdown(collect(spec));
    byId("markdown-preview").textContent = markdown;
    return markdown;
  }

  function fallbackCopy(text) {
    var area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "readonly");
    area.style.position = "fixed";
    area.style.left = "-9999px";
    document.body.appendChild(area);
    area.select();
    var ok = document.execCommand("copy");
    document.body.removeChild(area);
    return ok;
  }

  function init() {
    var spec = window.FORM_SPEC;
    if (!spec) return;

    byId("form-title").textContent = spec.title;
    byId("form-summary").textContent = spec.summary;
    byId("boundary-text").textContent = BOUNDARY_TEXT;

    var links = byId("source-links");
    spec.links.forEach(function (link) {
      var anchor = document.createElement("a");
      anchor.href = link.href;
      anchor.textContent = link.label;
      links.appendChild(anchor);
    });

    renderForm(spec);
    renderImportPanel();
    var draft = readDraft(spec);
    if (draft) {
      fill(spec, draft);
      setStatus("Local draft restored.");
    } else {
      fill(spec, spec.example);
      setStatus("Synthetic example loaded. Edits save locally.");
    }
    updatePreview();

    byId("copy-markdown").addEventListener("click", function () {
      var markdown = updatePreview();
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(markdown).then(function () {
          setStatus("Markdown copied.");
        }, function () {
          setStatus(fallbackCopy(markdown) ? "Markdown copied." : "Copy failed; select the preview text manually.");
        });
      } else {
        setStatus(fallbackCopy(markdown) ? "Markdown copied." : "Copy failed; select the preview text manually.");
      }
    });

    byId("download-markdown").addEventListener("click", function () {
      download(spec.slug + ".md", "text/markdown;charset=utf-8", updatePreview());
      setStatus("Markdown download prepared.");
    });

    byId("download-json").addEventListener("click", function () {
      download(spec.slug + ".json", "application/json;charset=utf-8", exportJson(spec));
      setStatus("JSON download prepared.");
    });

    byId("load-json").addEventListener("click", importJson);

    byId("reset-example").addEventListener("click", function () {
      clearDraft(spec);
      fill(spec, spec.example);
      updatePreview();
      setStatus("Local draft cleared. Reset to synthetic example.");
    });

    byId("clear-draft").addEventListener("click", function () {
      clearDraft(spec);
      fill(spec, spec.example);
      updatePreview();
      setStatus("Local draft cleared. Synthetic example restored.");
    });
  }

  window.FormRuntime = {
    init: init,
    lines: normalizeLines,
    rows: parseRows,
    rowText: rowText,
    joinList: joinList,
    yesNo: yesNo,
    importJson: importJson,
    exportJson: exportJson,
    draftKey: draftKey,
    list: list,
    table: table,
    boundaryText: BOUNDARY_TEXT
  };

  document.addEventListener("DOMContentLoaded", init);
})();
