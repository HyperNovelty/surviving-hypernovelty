#!/usr/bin/env python3
import json, sys
from pathlib import Path

REQUIRED_TOP = [
    'card_name', 'service_context', 'review_owner', 'last_reviewed', 'ai_role',
    'not_ai_decisions', 'human_review_triggers', 'recourse_path', 'evidence_to_include',
    'repair_commitments', 'response_time_expectation', 'boundary_notes'
]
REQUIRED_TRIGGER = ['trigger', 'human_owner', 'why']
REQUIRED_RECOURSE = ['visible_label', 'contact_route', 'appeal_or_review_step', 'fallback_if_no_response']
ALLOWED_STATUS = {'draft', 'needs_owner_review', 'ready_for_pilot', 'do_not_use_until_reviewed'}


def bullets(items):
    return '\n'.join(f'- {x}' for x in items) if items else '- Not specified'


def validate(data):
    errors = []
    for field in REQUIRED_TOP:
        if field not in data or data.get(field) in ('', None, []):
            errors.append(f'missing required field: {field}')
    status = data.get('status', 'draft')
    if status not in ALLOWED_STATUS:
        errors.append(f"status must be one of {sorted(ALLOWED_STATUS)}")
    if not isinstance(data.get('human_review_triggers', []), list):
        errors.append('human_review_triggers must be a list')
    else:
        for idx, trigger in enumerate(data.get('human_review_triggers', []), 1):
            for field in REQUIRED_TRIGGER:
                if field not in trigger or trigger.get(field) in ('', None, []):
                    errors.append(f'trigger {idx}: missing {field}')
    recourse = data.get('recourse_path', {})
    if not isinstance(recourse, dict):
        errors.append('recourse_path must be an object')
    else:
        for field in REQUIRED_RECOURSE:
            if field not in recourse or recourse.get(field) in ('', None, []):
                errors.append(f'recourse_path missing {field}')
    if not data.get('not_ai_decisions'):
        errors.append('at least one non-AI decision must be named')
    return errors


def risk_status(data):
    triggers = data.get('human_review_triggers', [])
    high_words = ('eligibility', 'denial', 'medical', 'safety', 'discipline', 'employment', 'benefit', 'money', 'rights', 'placement')
    combined = ' '.join([data.get('service_context', ''), data.get('ai_role', '')] + [t.get('trigger', '') for t in triggers]).lower()
    high_count = sum(1 for word in high_words if word in combined)
    if data.get('status') == 'do_not_use_until_reviewed':
        return 'DO NOT USE UNTIL OWNER REVIEW'
    if high_count or len(triggers) >= 3:
        return 'HUMAN RECOURSE REQUIRED — OWNER REVIEW BEFORE LIVE USE'
    return 'RECOURSE PATH DRAFT — PILOT ONLY WITH HUMAN FALLBACK'


def render(data):
    errors = validate(data)
    recourse = data.get('recourse_path', {}) if isinstance(data.get('recourse_path', {}), dict) else {}
    verification = data.get('verification_context', {}) if isinstance(data.get('verification_context', {}), dict) else {}
    verification_section = ''
    if verification:
        verification_section = f"""
## Verification context
- Claimed authority: {verification.get('claimed_authority', 'Not specified')}
- Source of truth: {verification.get('source_of_truth', 'Not specified')}
- Evidence to preserve before action:
{bullets(verification.get('evidence_to_preserve_before_action', []))}
"""
    trigger_blocks = []
    for idx, item in enumerate(data.get('human_review_triggers', []), 1):
        trigger_blocks.append(f"""### Trigger {idx}: {item.get('trigger', 'Untitled trigger')}
- Human owner: {item.get('human_owner', 'Not specified')}
- Why this leaves the AI path: {item.get('why', 'Not specified')}""")
    validation_detail = bullets(errors) if errors else '- No validation errors'
    return f"""# Human Recourse Path Card: {data.get('card_name', 'Untitled card')}

**Status:** {risk_status(data)}  
**Service context:** {data.get('service_context', 'Not specified')}  
**Review owner:** {data.get('review_owner', 'Not specified')}  
**Last reviewed:** {data.get('last_reviewed', 'Not specified')}  
**Card state:** {data.get('status', 'draft')}  

## AI role
{data.get('ai_role', 'Not specified')}
{verification_section}
## The AI/tool does not decide
{bullets(data.get('not_ai_decisions', []))}

## Human-review triggers
{chr(10).join(trigger_blocks) if trigger_blocks else 'No triggers supplied.'}

## Visible recourse path
- Label shown to the person: {recourse.get('visible_label', 'Not specified')}
- Contact route: {recourse.get('contact_route', 'Not specified')}
- Appeal/review step: {recourse.get('appeal_or_review_step', 'Not specified')}
- Fallback if no response: {recourse.get('fallback_if_no_response', 'Not specified')}
- Response-time expectation: {data.get('response_time_expectation', 'Not specified')}

## Evidence to include
{bullets(data.get('evidence_to_include', []))}

## Repair commitments
{bullets(data.get('repair_commitments', []))}

## Boundary notes
{bullets(data.get('boundary_notes', []))}

## Boundary
This card does not create a legal appeals process, rights guarantee, medical/financial/employment/schooling decision, compliance assurance, or promise of outcome. It is a local review aid for making the human path visible. Domain owners approve real timelines, escalation language, and authority.

## Validation
{'valid' if not errors else 'invalid'}
{validation_detail}
"""


def main(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    errors = validate(data)
    print(render(data))
    if errors:
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: render_card.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
