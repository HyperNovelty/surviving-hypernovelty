#!/usr/bin/env python3
"""Render a local Agent Revocation Reality Check from JSON."""
import json
import sys
from pathlib import Path

WEAK_SYSTEM_STATUSES = {"partly_verified", "not_verified", "unknown"}
WEAK_STEP_STATUSES = {"needs_work", "blocked", "unknown"}
HIGH_RISK_HINTS = {"write", "schedule", "public", "spend", "secret", "token", "crm", "customer", "patient", "student", "financial", "email", "deploy"}


def bullets(items):
    return "\n".join(f"- {item}" for item in items) if items else "- None recorded"


def table(headers, rows):
    header = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join("---" for _ in headers) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(cell).replace("\n", "<br>") for cell in row) + " |")
    return "\n".join([header, divider] + body)


def check_flags(data):
    flags = []
    for system in data.get("connected_systems", []):
        name = system.get("system_name", "Unnamed system")
        if system.get("verified_status") in WEAK_SYSTEM_STATUSES:
            flags.append(f"{name}: revocation status -> {system.get('verified_status')}")
        access = " ".join([system.get("access_type", ""), system.get("revocation_method", "")]).lower()
        if any(hint in access for hint in HIGH_RISK_HINTS) and system.get("verified_status") != "verified":
            flags.append(f"{name}: high-impact access or control needs stronger verification")
    for step in data.get("revocation_steps", []):
        if step.get("status") in WEAK_STEP_STATUSES:
            flags.append(f"Step needs work: {step.get('step', 'Unnamed step')} -> {step.get('status')}")
    if not data.get("dependent_workflows"):
        flags.append("No dependent workflows recorded; downstream breakage may be hidden")
    if not data.get("evidence_to_preserve"):
        flags.append("No evidence preservation list recorded")
    if not data.get("restart_criteria"):
        flags.append("No restart criteria recorded")
    for gap in data.get("open_gaps", []):
        flags.append(f"Open gap: {gap}")
    return flags


def render(data):
    flags = check_flags(data)
    status = "REVOCATION PATH NEEDS WORK" if flags else "REVOCATION PATH READY FOR DRILL"
    system_rows = []
    for system in data.get("connected_systems", []):
        system_rows.append([
            system.get("system_name", "Unnamed system"),
            system.get("access_type", "Unspecified"),
            system.get("revocation_method", "Unspecified"),
            system.get("revocation_owner", "Unspecified"),
            system.get("verified_status", "unknown"),
            system.get("notes", ""),
        ])
    step_rows = []
    for idx, step in enumerate(data.get("revocation_steps", []), 1):
        step_rows.append([
            idx,
            step.get("step", "Unspecified"),
            step.get("owner", "Unspecified"),
            step.get("status", "unknown"),
            step.get("evidence", "Unspecified"),
        ])
    return f"""# Agent Revocation Reality Check: {data.get('check_name', 'Unnamed check')}

**Status:** {status}  
**Review owner:** {data.get('review_owner', 'Unspecified')}  
**Review date:** {data.get('review_date', 'Unspecified')}  
**Agent identity:** {data.get('agent_identity', 'Unspecified')}  
**Roster link:** {data.get('roster_link', 'Unspecified')}

## Scenario
{data.get('scenario', 'No scenario recorded.')}

## Connected systems and revocation methods
{table(['System', 'Access type', 'Revocation method', 'Owner', 'Verified status', 'Notes'], system_rows)}

## Permissions to revoke
{bullets(data.get('permissions_to_revoke', []))}

## Pause trigger and owner
**Pause owner:** {data.get('pause_owner', 'Unspecified')}  
**Pause trigger:** {data.get('pause_trigger', 'Unspecified')}

## Revocation steps
{table(['#', 'Step', 'Owner', 'Status', 'Evidence to check/preserve'], step_rows)}

## Dependent workflows affected
{bullets(data.get('dependent_workflows', []))}

## Evidence to preserve
{bullets(data.get('evidence_to_preserve', []))}

## Restart criteria
{bullets(data.get('restart_criteria', []))}

## Open gaps
{bullets(data.get('open_gaps', []))}

## Decision
**Decision:** {data.get('decision', 'Unspecified')}  
**Required next action:** {data.get('required_next_action', 'Unspecified')}

## Reality-check flags
{bullets(flags)}

## Boundary note
{data.get('boundary_note', 'Local review aid only. Not an IAM system, security control, incident-response plan, compliance audit, legal opinion, vendor certification, or guarantee that revocation works. Do not store secrets here.')}

## Notes
{data.get('notes', '')}
"""


def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    print(render(data))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: render_check.py input.json", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
