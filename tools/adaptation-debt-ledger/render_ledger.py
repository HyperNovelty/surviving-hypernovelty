#!/usr/bin/env python3
"""Render a local Adaptation Debt Ledger from JSON."""
import json, sys
from pathlib import Path


def bullets(items):
    return "\n".join(f"- {x}" for x in items) if items else "- Not specified"


def table(headers, rows):
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *["| " + " | ".join(str(c).replace("\n", "<br>") for c in row) + " |" for row in rows],
    ])


def render(data):
    debt_rows = [
        [
            item.get("stale_assumption", ""),
            item.get("visible_symptom", ""),
            ", ".join(item.get("carriers", [])),
            item.get("cheap_next_review", ""),
            item.get("owner", ""),
            item.get("priority", ""),
        ]
        for item in data.get("adaptation_debts", [])
    ]
    repair_rows = [
        [item.get("action", ""), item.get("owner", ""), item.get("priority", "")]
        for item in data.get("top_repair_queue", [])
    ]
    flags = data.get("review_flags", [])
    return f"""# Adaptation Debt Ledger: {data.get('title', 'Untitled')}

**Status:** {data.get('status', 'REVIEW AID ONLY')}  
**Owner:** {data.get('owner', 'Unspecified')}  
**Purpose:** {data.get('purpose', 'Unspecified')}  
**Review cadence:** {data.get('review_cadence', 'Unspecified')}

## Debt ledger
{table(['Stale assumption', 'Visible symptom', 'Who carries it', 'Cheap next review', 'Owner', 'Priority'], debt_rows)}

## Top repair queue
{table(['Action', 'Owner', 'Priority'], repair_rows)}

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
