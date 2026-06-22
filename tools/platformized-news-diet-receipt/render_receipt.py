#!/usr/bin/env python3
"""Render a local Platformized News Diet Receipt from JSON."""
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
    rows = [
        [
            item.get("item", ""),
            item.get("channel", ""),
            item.get("original_source_checked", ""),
            item.get("intermediary", ""),
            item.get("confidence", ""),
            item.get("missing_context", ""),
        ]
        for item in data.get("source_chain_items", [])
    ]
    flags = data.get("review_flags", [])
    return f"""# Platformized News Diet Receipt: {data.get('title', 'Untitled')}

**Status:** {data.get('status', 'REVIEW AID ONLY')}  
**Owner:** {data.get('owner', 'Unspecified')}  
**Purpose:** {data.get('purpose', 'Unspecified')}  
**Review cadence:** {data.get('review_cadence', 'Unspecified')}

## Source-chain receipt
{table(['Item', 'Channel', 'Original source checked?', 'Intermediary', 'Confidence', 'Missing context'], rows)}

## Reflection prompts
{bullets(data.get('reflection_prompts', []))}

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
