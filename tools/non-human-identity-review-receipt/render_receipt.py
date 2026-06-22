#!/usr/bin/env python3
"""Render a local Non-Human Identity Review Receipt from JSON."""
import json
import sys
from pathlib import Path

REVIEW_DECISIONS = {"renew_with_changes", "pause", "revoke", "escalate"}
GATED_VALUES = {"human_approval_required", "allowed_with_controls"}
SENSITIVE_HINTS = {"customer", "student", "patient", "credential", "secret", "confidential", "financial", "payroll", "private", "legal", "health", "crm"}


def bullets(items):
    return "\n".join(f"- {item}" for item in items) if items else "- None recorded"


def table(headers, rows):
    header = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join("---" for _ in headers) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(cell).replace("\n", "<br>") for cell in row) + " |")
    return "\n".join([header, divider] + body)


def receipt_flags(data):
    flags = []
    for review in data.get("identity_reviews", []):
        name = review.get("identity_name", "Unnamed identity")
        if review.get("decision") in REVIEW_DECISIONS:
            flags.append(f"{name}: review decision -> {review.get('decision')}")
        for gate in ("public_action_gate", "spend_gate", "secrets_gate"):
            if review.get(gate) in GATED_VALUES:
                flags.append(f"{name}: {gate.replace('_', ' ')} -> {review.get(gate)}")
        for item in review.get("data_touched", []):
            low = item.lower()
            if any(hint in low for hint in SENSITIVE_HINTS):
                flags.append(f"{name}: sensitive or governance-relevant data touched -> {item}")
        if not review.get("permission_evidence"):
            flags.append(f"{name}: missing permission evidence")
        if not review.get("log_evidence"):
            flags.append(f"{name}: missing log evidence")
        if review.get("unresolved_gaps"):
            flags.append(f"{name}: unresolved gaps present")
        if not review.get("expiry_or_next_review"):
            flags.append(f"{name}: missing expiry/next review")
    return flags


def render(data):
    flags = receipt_flags(data)
    status = "REVIEW ACTION REQUIRED" if flags else "LOWER-RISK RENEWAL RECEIPT"
    summary_rows = []
    for review in data.get("identity_reviews", []):
        summary_rows.append([
            review.get("identity_name", "Unnamed"),
            review.get("business_owner", "Unspecified"),
            review.get("identity_type", "Unspecified"),
            review.get("purpose", "Unspecified"),
            review.get("decision", "Unspecified"),
            review.get("expiry_or_next_review", "Unspecified"),
        ])
    gate_rows = []
    for review in data.get("identity_reviews", []):
        gate_rows.append([
            review.get("identity_name", "Unnamed"),
            review.get("public_action_gate", "Unspecified"),
            review.get("spend_gate", "Unspecified"),
            review.get("secrets_gate", "Unspecified"),
            ", ".join(review.get("data_touched", [])) or "None recorded",
            ", ".join(review.get("current_permissions", [])) or "None recorded",
        ])
    sections = []
    for review in data.get("identity_reviews", []):
        sections.append(f"""### {review.get('identity_name', 'Unnamed identity')}

**Owner:** {review.get('business_owner', 'Unspecified')}  
**Roster link:** {review.get('roster_link', 'Unspecified')}  
**Decision:** {review.get('decision', 'Unspecified')}  
**Next expiry/review:** {review.get('expiry_or_next_review', 'Unspecified')}

**Delta since last review**
{bullets(review.get('delta_since_last_review', []))}

**Permission evidence**
{bullets(review.get('permission_evidence', []))}

**Log evidence**
{bullets(review.get('log_evidence', []))}

**Unresolved gaps**
{bullets(review.get('unresolved_gaps', []))}

**Required next action:** {review.get('required_next_action', 'Unspecified')}

**Notes:** {review.get('notes', '')}
""")
    detail_text = "\n".join(sections)
    return f"""# Non-Human Identity Review Receipt: {data.get('receipt_name', 'Unnamed receipt')}

**Status:** {status}  
**Review owner:** {data.get('review_owner', 'Unspecified')}  
**Review date:** {data.get('review_date', 'Unspecified')}  
**Review cadence:** {data.get('review_cadence', 'Unspecified')}

## Identity review summary
{table(['Identity', 'Owner', 'Identity type', 'Purpose', 'Decision', 'Expiry/next review'], summary_rows)}

## Gates and current scope
{table(['Identity', 'Public action gate', 'Spend gate', 'Secrets gate', 'Data touched', 'Current permissions'], gate_rows)}

## Per-identity evidence
{detail_text}
## Cross-roster questions
{bullets(data.get('cross_roster_questions', []))}

## Receipt flags
{bullets(flags)}

## Boundary note
{data.get('boundary_note', 'Local review receipt only. Not a security certification, IAM system, compliance audit, legal opinion, or permission grant. Do not store secrets here.')}

## Notes
{data.get('notes', '')}
"""


def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    print(render(data))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: render_receipt.py input.json", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
