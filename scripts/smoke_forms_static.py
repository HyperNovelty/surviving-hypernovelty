#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

FORMS = {
    "forms/agent-identity-scope-roster.html": {
        "schema": "schemas/agent-identity-scope-roster.schema.json",
        "tokens": [
            "auth_surface",
            "connected_tools",
            "output_destinations",
            "risk_notes",
        ],
    },
    "forms/ai-use-clarity-micro-policy-card.html": {
        "schema": "schemas/ai-use-clarity-micro-policy-card.schema.json",
        "tokens": [
            "policy_context",
            "allowed_uses",
            "requires_disclosure",
            "human_review_triggers",
        ],
    },
    "forms/adaptation-debt-ledger.html": {
        "schema": "schemas/adaptation-debt-ledger.schema.json",
        "tokens": [
            "adaptation_debts",
            "top_repair_queue",
            "cheap_next_review",
        ],
    },
    "forms/visible-thinking-repair-ticket.html": {
        "schema": "schemas/visible-thinking-repair-ticket.schema.json",
        "tokens": [
            "missing_evidence",
            "repair_requests",
            "acceptable_repair_outcomes",
        ],
    },
    "forms/platformized-news-diet-receipt.html": {
        "schema": "schemas/platformized-news-diet-receipt.schema.json",
        "tokens": [
            "source_chain_items",
            "reflection_prompts",
            "original_source_checked",
        ],
    },
}

RUNTIME_TOKENS = [
    "Import JSON",
    "Load JSON into Form",
    "Local draft",
    "localStorage",
    "draftKey",
    "clearDraft",
    "importJson",
    "exportJson",
    "fromJson",
    "Malformed JSON",
    "Missing required field",
]

BLOCKED_PATTERNS = [
    "http://",
    "https://",
    "fetch(",
    "XMLHttpRequest",
    "navigator.sendBeacon",
    "<iframe",
    "form action=",
    "analytics",
    "telemetry",
]


def main():
    errors = []
    runtime = (ROOT / "forms/shared/form_runtime.js").read_text(encoding="utf-8")
    for token in RUNTIME_TOKENS:
        if token not in runtime:
            errors.append(f"forms/shared/form_runtime.js missing runtime token: {token}")

    for rel_path, spec in FORMS.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        schema = json.loads((ROOT / spec["schema"]).read_text(encoding="utf-8"))
        required = schema.get("required", [])
        for token in ["FORM_SPEC", "requiredFields", "toJson", "fromJson", "shared/form_runtime.js"]:
            if token not in text:
                errors.append(f"{rel_path} missing token: {token}")
        for token in ["Clear Draft", 'id="clear-draft"', 'id="reset-example"']:
            if token not in text:
                errors.append(f"{rel_path} missing draft control token: {token}")
        for field in required:
            if field not in text:
                errors.append(f"{rel_path} missing required schema field token: {field}")
        for token in spec["tokens"]:
            if token not in text:
                errors.append(f"{rel_path} missing important schema token: {token}")

    checked_paths = list(FORMS) + [
        "forms/index.html",
        "forms/shared/form_runtime.js",
        "forms/shared/form_styles.css",
    ]
    for rel_path in checked_paths:
        text = (ROOT / rel_path).read_text(encoding="utf-8").lower()
        for pattern in BLOCKED_PATTERNS:
            if pattern.lower() in text:
                errors.append(f"{rel_path} contains blocked local-only pattern: {pattern}")

    if errors:
        print("forms_static_smoke=failed")
        for error in errors:
            print(error)
        return 1

    print("forms_static_smoke=ok")
    print("forms_checked=", len(FORMS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
