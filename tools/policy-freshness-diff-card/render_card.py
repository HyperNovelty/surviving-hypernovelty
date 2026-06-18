#!/usr/bin/env python3
"""Render a local Policy Freshness Diff Card from JSON."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REVIEW_VERDICTS = {"interim_update_needed", "owner_review_required"}
LOW_EVIDENCE = {"weak"}


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- Not specified"


def freshness_flags(data: dict) -> list[str]:
    flags: list[str] = []
    verdict = data.get("freshness_verdict", "")
    evidence = data.get("evidence_strength", "")
    if verdict in REVIEW_VERDICTS:
        flags.append(f"policy owner review needed: {verdict}")
    if evidence in LOW_EVIDENCE and verdict not in {"still_current", "monitor"}:
        flags.append("evidence is weak; avoid permanent rewrite without stronger local confirmation")
    if not data.get("proposed_diff", {}).get("what_not_to_change_yet"):
        flags.append("missing do-not-change-yet boundary")
    if not data.get("review", {}).get("human_checks"):
        flags.append("missing human checks")
    return flags


def render(data: dict) -> str:
    diff = data.get("proposed_diff", {})
    review = data.get("review", {})
    flags = freshness_flags(data)
    status = "OWNER REVIEW REQUIRED" if flags else "LOWER-RISK MONITORING CARD"
    return f"""# Policy Freshness Diff Card: {data.get('policy_name', 'Unnamed policy')}

**Status:** {status}  
**Policy owner:** {data.get('policy_owner', 'Unspecified')}  
**Evidence strength:** {data.get('evidence_strength', 'Unspecified')}  
**Freshness verdict:** {data.get('freshness_verdict', 'Unspecified')}

## Context
{data.get('context', 'Not specified')}

## Current rule or assumption
{data.get('current_rule', 'Not specified')}

## Change signal
{data.get('change_signal', 'Not specified')}

## Possibly stale assumption
{data.get('stale_assumption', 'Not specified')}

## Affected people
{bullets(data.get('affected_people', []))}

## Proposed diff
**Change type:** {diff.get('change_type', 'Not specified')}  
**Interim language:** {diff.get('interim_language', 'Not specified')}  
**Do not change yet:** {diff.get('what_not_to_change_yet', 'Not specified')}

## Review path
**Decision owner:** {review.get('decision_owner', 'Not specified')}  
**Next review date:** {review.get('next_review_date', 'Not specified')}

### Review triggers
{bullets(review.get('review_triggers', []))}

### Human checks
{bullets(review.get('human_checks', []))}

## Freshness flags
{bullets(flags)}

## Notes
{data.get('notes', '')}

## Boundary
Review aid only. This card does not provide legal, compliance, HR, academic-integrity, medical, security, or risk-management advice.
"""


def main(path: str) -> int:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    print(render(data))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: render_card.py input.json", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
