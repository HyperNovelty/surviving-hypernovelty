#!/usr/bin/env python3
"""Render a local Agent Toolchain Exposure Map from JSON."""
import json
import sys
from pathlib import Path

REVIEW_ACTIONS = {
    "spend_money",
    "publish_publicly",
    "email_external",
    "message_external",
    "delete_data",
    "access_secrets",
    "deploy_production",
    "change_permissions",
    "trigger_workflow",
}
SENSITIVE_DATA_HINTS = {"customer", "student", "patient", "credential", "secret", "financial", "payroll", "private"}


def bullets(items):
    return "\n".join(f"- {item}" for item in items) if items else "- Not specified"


def table(headers, rows):
    header = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join("---" for _ in headers) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(cell).replace("\n", "<br>") for cell in row) + " |")
    return "\n".join([header, divider] + body)


def exposure_flags(data):
    flags = []
    for agent in data.get("agents", []):
        name = agent.get("name", "Unnamed agent")
        actions = set(agent.get("actions", []))
        risky = sorted(actions & REVIEW_ACTIONS)
        if risky:
            flags.append(f"{name}: review actions -> {', '.join(risky)}")
        if agent.get("secrets_access") in {"review_required", "allowed"}:
            flags.append(f"{name}: secrets access -> {agent.get('secrets_access')}")
        for touched in agent.get("data_touched", []):
            low = touched.lower()
            if any(hint in low for hint in SENSITIVE_DATA_HINTS):
                flags.append(f"{name}: sensitive data touched -> {touched}")
    for handoff in data.get("handoffs", []):
        if not handoff.get("human_checkpoint"):
            flags.append(
                f"handoff {handoff.get('from','?')} -> {handoff.get('to','?')}: missing human checkpoint"
            )
    return flags


def render(data):
    flags = exposure_flags(data)
    status = "REVIEW REQUIRED" if flags else "LOWER-RISK DRAFT MAP"
    agent_rows = []
    for agent in data.get("agents", []):
        agent_rows.append([
            agent.get("name", "Unnamed"),
            agent.get("owner", "Unspecified"),
            agent.get("identity", "Unspecified"),
            ", ".join(agent.get("tools", [])) or "Not specified",
            ", ".join(agent.get("data_touched", [])) or "Not specified",
            ", ".join(agent.get("actions", [])) or "Not specified",
            ", ".join(agent.get("outputs_to", [])) or "Not specified",
            agent.get("human_checkpoint", "Not specified"),
        ])
    handoff_rows = []
    for handoff in data.get("handoffs", []):
        handoff_rows.append([
            handoff.get("from", "?"),
            handoff.get("to", "?"),
            handoff.get("payload", "Unspecified"),
            handoff.get("trigger", "Unspecified"),
            handoff.get("human_checkpoint", ""),
        ])
    return f"""# Agent Toolchain Exposure Map: {data.get('workflow_name', 'Unnamed workflow')}

**Status:** {status}  
**Owner:** {data.get('workflow_owner', 'Unspecified')}  
**Purpose:** {data.get('purpose', 'Unspecified')}  
**Review cadence:** {data.get('review_cadence', 'Unspecified')}

## Agent/tool exposure table
{table(['Agent', 'Owner', 'Identity', 'Tools', 'Data touched', 'Actions', 'Outputs to', 'Human checkpoint'], agent_rows)}

## Handoffs
{table(['From', 'To', 'Payload', 'Trigger', 'Human checkpoint'], handoff_rows) if handoff_rows else 'No handoffs listed.'}

## Shared boundaries
**Secrets boundary:** {data.get('shared_boundaries', {}).get('secrets_boundary', 'Not specified')}  
**Public/action boundary:** {data.get('shared_boundaries', {}).get('public_action_boundary', 'Not specified')}  
**Audit evidence:** {data.get('shared_boundaries', {}).get('audit_evidence', 'Not specified')}  
**Rollback owner:** {data.get('shared_boundaries', {}).get('rollback_owner', 'Not specified')}

## Review triggers
{bullets(data.get('review_triggers', []))}

## Exposure flags
{bullets(flags)}

## Notes
{data.get('notes', '')}
"""


def main(path):
    data = json.loads(Path(path).read_text())
    print(render(data))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: render_map.py input.json", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
