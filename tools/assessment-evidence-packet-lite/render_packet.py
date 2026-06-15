#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def bullet(items):
    return "\n".join(f"- {item}" for item in items) if items else "- None recorded"


def render(data):
    allowed = data["allowed_help"]
    evidence = data["evidence"]
    review = data["human_review"]
    return f"""# {data['packet_title']}

Learner: {data['learner']}  
Date: {data.get('date', 'not recorded')}  
Assignment: {data['assignment']}

## Learning target

{data['learning_target']}

## Allowed help / AI use rules

AI allowed: {allowed['ai_allowed']}  
Human help allowed: {allowed['human_help_allowed']}

{bullet(allowed.get('rules', []))}

## Learner claim of understanding

{evidence['learner_claim']}

## Process trace

{bullet(evidence.get('process_trace', []))}

## Revision / misconception log

{bullet(evidence.get('revision_or_misconception_log', []))}

## Transfer check

{evidence['transfer_check']}

## Source or tool notes

{bullet(evidence.get('source_or_tool_notes', []))}

## Human review

Reviewer: {review['reviewer']}  
Review needed: {review['review_needed']}

{bullet(review.get('notes', []))}

Next action: {review['next_action']}

## Boundary

This packet is evidence for review, not proof that AI was or was not used. Do not use it as an AI detector, grading guarantee, or substitute for teacher judgment.
"""


def main():
    if len(sys.argv) != 2:
        print('usage: render_packet.py <packet.json>', file=sys.stderr)
        return 2
    data = json.loads(Path(sys.argv[1]).read_text())
    print(render(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
