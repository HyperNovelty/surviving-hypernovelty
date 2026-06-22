#!/usr/bin/env python3
"""Render a local Agent Identity & Scope Roster from JSON."""
import json
import sys
from pathlib import Path

REVIEW_VALUES = {"review_required", "allowed"}
SENSITIVE_HINTS = {"customer", "student", "patient", "credential", "secret", "financial", "payroll", "private", "legal", "health"}
RISKY_ACTIONS = {"publish", "post", "email", "message", "spend", "buy", "deploy", "delete", "change_permissions", "submit", "upload", "external"}


def bullets(items):
    return "\n".join(f"- {item}" for item in items) if items else "- Not specified"


def table(headers, rows):
    header = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join("---" for _ in headers) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(cell).replace("\n", "<br>") for cell in row) + " |")
    return "\n".join([header, divider] + body)


def roster_flags(data):
    flags = []
    for agent in data.get("agents", []):
        name = agent.get("agent_name", "Unnamed agent")
        for field in ("secrets_access", "public_action", "spend_authority"):
            if agent.get(field) in REVIEW_VALUES:
                flags.append(f"{name}: {field.replace('_', ' ')} -> {agent.get(field)}")
        for data_class in agent.get("data_classes", []):
            low = data_class.lower()
            if any(hint in low for hint in SENSITIVE_HINTS):
                flags.append(f"{name}: sensitive data class -> {data_class}")
        for action in agent.get("allowed_actions", []):
            low = action.lower()
            if any(hint in low for hint in RISKY_ACTIONS):
                flags.append(f"{name}: risky allowed action -> {action}")
        if not agent.get("log_location"):
            flags.append(f"{name}: missing log location")
        if not agent.get("expiry_review_date"):
            flags.append(f"{name}: missing expiry/review date")
        if agent.get("approval_state") != "approved_local_only":
            flags.append(f"{name}: approval state -> {agent.get('approval_state', 'missing')}")
    return flags


def render(data):
    flags = roster_flags(data)
    status = "REVIEW REQUIRED" if flags else "LOWER-RISK LOCAL ROSTER"
    rows = []
    for agent in data.get("agents", []):
        rows.append([
            agent.get("agent_name", "Unnamed"), agent.get("owner", "Unspecified"), agent.get("purpose", "Unspecified"), agent.get("identity_type", "Unspecified"), agent.get("auth_surface", "Unspecified"), ", ".join(agent.get("data_classes", [])) or "Not specified", ", ".join(agent.get("read_scopes", [])) or "Not specified", ", ".join(agent.get("write_scopes", [])) or "Not specified", agent.get("approval_state", "Unspecified"), agent.get("expiry_review_date", "Unspecified")
        ])
    control_rows = []
    for agent in data.get("agents", []):
        control_rows.append([
            agent.get("agent_name", "Unnamed"), agent.get("secrets_access", "Unspecified"), agent.get("public_action", "Unspecified"), agent.get("spend_authority", "Unspecified"), ", ".join(agent.get("allowed_actions", [])) or "Not specified", ", ".join(agent.get("blocked_actions", [])) or "Not specified", agent.get("log_location", "Unspecified")
        ])
    return f"""# Agent Identity & Scope Roster: {data.get('roster_name', 'Unnamed roster')}

**Status:** {status}  
**Roster owner:** {data.get('roster_owner', 'Unspecified')}  
**Purpose:** {data.get('purpose', 'Unspecified')}  
**Data boundary:** {data.get('data_boundary', 'Unspecified')}  
**Review cadence:** {data.get('review_cadence', 'Unspecified')}

## Identity scope table
{table(['Agent', 'Owner', 'Purpose', 'Identity type', 'Auth surface', 'Data classes', 'Read scopes', 'Write scopes', 'Approval state', 'Expiry/review date'], rows)}

## Permissions and controls
{table(['Agent', 'Secrets access', 'Public action', 'Spend authority', 'Allowed actions', 'Blocked actions', 'Log location'], control_rows)}

## Escalation triggers
{bullets(data.get('escalation_triggers', []))}

## Roster flags
{bullets(flags)}

## Boundary note
{data.get('boundary_note', 'Visibility and review aid only. Do not store secrets in this roster.')}

## Notes
{data.get('notes', '')}
"""


def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    print(render(data))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: render_roster.py input.json", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
