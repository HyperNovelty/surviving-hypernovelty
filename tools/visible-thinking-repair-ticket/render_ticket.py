#!/usr/bin/env python3
"""Render a local Visible Thinking Repair Ticket from JSON."""
import json, sys
from pathlib import Path


def bullets(items):
    return "\n".join(f"- {x}" for x in items) if items else "- Not specified"


def render(data):
    missing = [
        f"{item.get('gap', 'Unspecified')} (severity: {item.get('severity', 'unspecified')})"
        for item in data.get("missing_evidence", [])
    ]
    requests = [
        f"{item.get('request', 'Unspecified')} (evidence type: {item.get('evidence_type', 'unspecified')})"
        for item in data.get("repair_requests", [])
    ]
    outcomes = [
        f"{item.get('outcome', 'Unspecified')} -> {item.get('disposition', 'revise')}"
        for item in data.get("acceptable_repair_outcomes", [])
    ]
    flags = data.get("review_flags", [])
    return f"""# Visible Thinking Repair Ticket: {data.get('title', 'Untitled')}

**Status:** {data.get('status', 'REVIEW AID ONLY')}  
**Owner:** {data.get('owner', 'Unspecified')}  
**Purpose:** {data.get('purpose', 'Unspecified')}  
**Review cadence:** {data.get('review_cadence', 'Unspecified')}

## Missing evidence
{bullets(missing)}

## Repair request
{bullets(requests)}

## Acceptable repair outcomes
{bullets(outcomes)}

## Review flags
{bullets(flags)}

## Boundary note
{data.get('boundary_note', 'Review aid only. Human approval required for high-stakes use.')}

## Notes
{data.get('notes', '')}
"""


def main(path):
    print(render(json.loads(Path(path).read_text(encoding="utf-8"))))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: renderer input.json", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
