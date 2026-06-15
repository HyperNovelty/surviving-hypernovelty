#!/usr/bin/env python3
import json, sys
from pathlib import Path

REQUIRED_TOP = [
    'surface_name', 'organization_or_team', 'review_owner', 'last_reviewed',
    'trust_context', 'stakeholders', 'surface_steps', 'human_premium_dimensions',
    'ai_roles', 'protected_human_work', 'human_checkpoints', 'decision', 'boundary_notes'
]
REQUIRED_STEP = ['step', 'current_owner', 'trust_weight', 'ai_posture', 'reason']
ALLOWED_TRUST = {'low', 'medium', 'high'}
ALLOWED_POSTURE = {'remove', 'support', 'protect', 'leave_human'}
ALLOWED_DECISION = {'draft', 'pilot_with_review', 'do_not_automate', 'needs_owner_review'}


def bullets(items):
    return '\n'.join(f'- {x}' for x in items) if items else '- Not specified'


def validate(data):
    errors = []
    for field in REQUIRED_TOP:
        if field not in data or data.get(field) in ('', None, []):
            errors.append(f'missing required field: {field}')
    if data.get('decision') not in ALLOWED_DECISION:
        errors.append(f"decision must be one of {sorted(ALLOWED_DECISION)}")
    for idx, step in enumerate(data.get('surface_steps', []), 1):
        for field in REQUIRED_STEP:
            if field not in step or step.get(field) in ('', None, []):
                errors.append(f'step {idx}: missing {field}')
        if step.get('trust_weight') not in ALLOWED_TRUST:
            errors.append(f"step {idx}: trust_weight must be one of {sorted(ALLOWED_TRUST)}")
        if step.get('ai_posture') not in ALLOWED_POSTURE:
            errors.append(f"step {idx}: ai_posture must be one of {sorted(ALLOWED_POSTURE)}")
    return errors


def posture_summary(steps):
    counts = {key: 0 for key in sorted(ALLOWED_POSTURE)}
    high_trust = 0
    for step in steps:
        posture = step.get('ai_posture')
        if posture in counts:
            counts[posture] += 1
        if step.get('trust_weight') == 'high':
            high_trust += 1
    if counts['leave_human'] or counts['protect']:
        status = 'HUMAN PREMIUM PROTECTED — REVIEW BEFORE CHANGE'
    elif counts['support']:
        status = 'AI SUPPORT CANDIDATE — PILOT WITH CHECKPOINTS'
    else:
        status = 'ADMIN REMOVAL CANDIDATE — VERIFY LOW TRUST LOAD'
    return status, counts, high_trust


def render(data):
    errors = validate(data)
    validation_detail = bullets(errors) if errors else '- No validation errors'
    status, counts, high_trust = posture_summary(data.get('surface_steps', []))
    step_blocks = []
    for idx, step in enumerate(data.get('surface_steps', []), 1):
        step_blocks.append(f"""### Step {idx}: {step.get('step', 'Untitled step')}
- Current owner: {step.get('current_owner', 'Not specified')}
- Trust weight: {step.get('trust_weight', 'Not specified')}
- AI posture: {step.get('ai_posture', 'Not specified')}
- Reason: {step.get('reason', 'Not specified')}
- Risk if automated: {step.get('risk_if_automated', 'Not specified')}""")

    return f"""# Human Premium Trust Surface Card: {data.get('surface_name', 'Untitled surface')}

**Status:** {status}  
**Organization/team:** {data.get('organization_or_team', 'Not specified')}  
**Review owner:** {data.get('review_owner', 'Not specified')}  
**Last reviewed:** {data.get('last_reviewed', 'Not specified')}  
**Decision:** {data.get('decision', 'Not specified')}  

## Trust context
{data.get('trust_context', 'Not specified')}

## Stakeholders
{bullets(data.get('stakeholders', []))}

## Posture counts
- Remove machine-work: {counts['remove']}
- Support human work: {counts['support']}
- Protect from automation pressure: {counts['protect']}
- Leave human: {counts['leave_human']}
- High-trust steps: {high_trust}

## Surface steps
{chr(10).join(step_blocks) if step_blocks else 'No steps supplied.'}

## Human premium dimensions
{bullets(data.get('human_premium_dimensions', []))}

## Approved AI roles
{bullets(data.get('ai_roles', []))}

## Protected human work
{bullets(data.get('protected_human_work', []))}

## Human checkpoints
{bullets(data.get('human_checkpoints', []))}

## Boundary notes
{bullets(data.get('boundary_notes', []))}

## Boundary
This card does not decide policy, staffing, compliance, employment action, medical/legal/financial advice, or customer promises. It is a local review aid only. Domain owners approve actual workflow changes.

## Validation
{'valid' if not errors else 'invalid'}
{validation_detail}
"""


def main(path):
    data = json.loads(Path(path).read_text())
    errors = validate(data)
    print(render(data))
    if errors:
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: render_card.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
