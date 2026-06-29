#!/usr/bin/env python3
"""Render a local Provenance Breakage Receipt from JSON."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_TOP = [
    "receipt_name",
    "scenario",
    "review_owner",
    "review_date",
    "original_item",
    "chain_steps",
    "alternate_corroboration",
    "confidence_after_review",
    "do_not_claim",
    "next_review_step",
    "boundary_notes",
]
REQUIRED_ORIGINAL = ["description", "source_or_holder", "credential_check", "credential_result"]
REQUIRED_STEP = [
    "step",
    "location_or_tool",
    "transformation",
    "credential_status",
    "what_broke_or_changed",
    "review_note",
]
ALLOWED_STATUS = {
    "present_and_checked",
    "present_not_checked",
    "missing",
    "stripped",
    "transformed",
    "unknown",
    "not_applicable",
}
ALLOWED_CONFIDENCE = {"higher", "medium", "low", "unknown"}


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- Not specified"


def table(headers: list[str], rows: list[list[str]]) -> str:
    return "\n".join(
        [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join("---" for _ in headers) + " |",
            *["| " + " | ".join(str(cell).replace("\n", "<br>") for cell in row) + " |" for row in rows],
        ]
    )


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_TOP:
        if field not in data or data.get(field) in ("", None, []):
            errors.append(f"missing required field: {field}")
    original = data.get("original_item", {})
    if not isinstance(original, dict):
        errors.append("original_item must be an object")
    else:
        for field in REQUIRED_ORIGINAL:
            if original.get(field) in ("", None, []):
                errors.append(f"original_item missing required field: {field}")
        if original.get("credential_result") not in ALLOWED_STATUS:
            errors.append(f"original_item invalid credential_result: {original.get('credential_result')}")
    steps = data.get("chain_steps", [])
    if not isinstance(steps, list):
        errors.append("chain_steps must be a list")
    else:
        for idx, step in enumerate(steps, 1):
            if not isinstance(step, dict):
                errors.append(f"chain step {idx} must be an object")
                continue
            for field in REQUIRED_STEP:
                if step.get(field) in ("", None, []):
                    errors.append(f"chain step {idx} missing required field: {field}")
            if step.get("credential_status") not in ALLOWED_STATUS:
                errors.append(f"chain step {idx} invalid credential_status: {step.get('credential_status')}")
    if data.get("confidence_after_review") not in ALLOWED_CONFIDENCE:
        errors.append(f"invalid confidence_after_review: {data.get('confidence_after_review')}")
    return errors


def render(data: dict) -> str:
    errors = validate(data)
    original = data.get("original_item", {}) if isinstance(data.get("original_item", {}), dict) else {}
    rows = [
        [
            step.get("step", ""),
            step.get("location_or_tool", ""),
            step.get("transformation", ""),
            step.get("credential_status", ""),
            step.get("what_broke_or_changed", ""),
            step.get("review_note", ""),
        ]
        for step in data.get("chain_steps", [])
        if isinstance(step, dict)
    ]
    validation_detail = bullets(errors) if errors else "- No validation errors"
    return f"""# Provenance Breakage Receipt: {data.get('receipt_name', 'Untitled receipt')}

**Scenario:** {data.get('scenario', 'Not specified')}  
**Review owner:** {data.get('review_owner', 'Not specified')}  
**Review date:** {data.get('review_date', 'Not specified')}  
**Confidence after review:** {data.get('confidence_after_review', 'unknown')}

## Original item / first trusted copy
- Description: {original.get('description', 'Not specified')}
- Source or holder: {original.get('source_or_holder', 'Not specified')}
- Credential check: {original.get('credential_check', 'Not specified')}
- Credential result: {original.get('credential_result', 'unknown')}

## Provenance chain
{table(['Step', 'Location/tool', 'Transformation', 'Credential status', 'What broke or changed', 'Review note'], rows) if rows else 'No chain steps supplied.'}

## Alternate corroboration
{bullets(data.get('alternate_corroboration', []))}

## Do not claim from this receipt
{bullets(data.get('do_not_claim', []))}

## Next review step
{data.get('next_review_step', 'Not specified')}

## Boundary notes
{bullets(data.get('boundary_notes', []))}

## Boundary
This receipt is a local chain-of-custody and provenance-survival aid only. Valid credentials do not prove truth, context, fairness, consent, or non-staging. Missing or stripped credentials do not prove fakery. Use domain experts, primary sources, and human editorial/educational review before public, legal, medical, financial, or safety-sensitive action.

## Validation
{'valid' if not errors else 'invalid'}
{validation_detail}
"""


def main(path: str) -> int:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    errors = validate(data)
    print(render(data))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: render_receipt.py input.json", file=sys.stderr)
        sys.exit(2)
    raise SystemExit(main(sys.argv[1]))
