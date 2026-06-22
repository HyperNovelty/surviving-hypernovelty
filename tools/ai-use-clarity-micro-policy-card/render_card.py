#!/usr/bin/env python3
"""Render a local AI Use Clarity Micro-Policy Card from JSON."""
import json, sys
from pathlib import Path


def bullets(items):
    return "\n".join(f"- {x}" for x in items) if items else "- Not specified"


def render(data):
    status = data.get("status", "REVIEW AID ONLY")
    context = data.get("policy_context", {})
    allowed = [
        f"{item.get('use', 'Unspecified')} ({item.get('timing', 'unspecified')}; "
        f"disclosure: {'yes' if item.get('requires_disclosure') else 'no'})"
        for item in data.get("allowed_uses", [])
    ]
    disallowed = [
        f"{item.get('use', 'Unspecified')} - {item.get('reason', 'No reason specified')}"
        for item in data.get("disallowed_uses", [])
    ]
    evidence = [
        f"{item.get('evidence', 'Unspecified')} (when: {item.get('required_when', 'unspecified')})"
        for item in data.get("required_evidence", [])
    ]
    triggers = [
        f"{item.get('trigger', 'Unspecified')} -> {item.get('response', 'clarify')}"
        for item in data.get("human_review_triggers", [])
    ]
    flags = data.get("review_flags", [])
    return f"""# AI Use Clarity Micro-Policy Card: {data.get('title', 'Untitled')}

**Status:** {status}  
**Owner:** {data.get('owner', 'Unspecified')}  
**Purpose:** {data.get('purpose', 'Unspecified')}  
**Review cadence:** {data.get('review_cadence', 'Unspecified')}

## Task context
**Setting:** {context.get('setting', 'Unspecified')}  
**Task:** {context.get('task', 'Unspecified')}  
**Learner-owned work:** {', '.join(context.get('learner_owned_work', [])) or 'Not specified'}

## Allowed uses
{bullets(allowed)}

## Disallowed uses
{bullets(disallowed)}

## Required evidence
{bullets(evidence)}

## Human review triggers
{bullets(triggers)}

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
