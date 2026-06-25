#!/usr/bin/env python3
import json, sys
from pathlib import Path

REQUIRED_TOP = ['receipt_name','scenario','review_owner','last_reviewed','contact_events','verification_route','do_not_do','safe_next_step','boundary_notes']
REQUIRED_EVENT = ['channel','claimed_sender','requested_action','pressure_tactic','risk_if_true','risk_if_fake','source_of_truth']
ALLOWED_STATUS = {'draft','ready_for_personal_use','needs_owner_review','do_not_use_until_reviewed'}

def bullets(items):
    return '\n'.join(f'- {x}' for x in items) if items else '- Not specified'

def validate(data):
    errors=[]
    for field in REQUIRED_TOP:
        if field not in data or data.get(field) in ('', None, []):
            errors.append(f'missing required field: {field}')
    if data.get('status','draft') not in ALLOWED_STATUS:
        errors.append(f"status must be one of {sorted(ALLOWED_STATUS)}")
    if not isinstance(data.get('contact_events',[]), list):
        errors.append('contact_events must be a list')
    else:
        for idx,event in enumerate(data.get('contact_events',[]),1):
            for field in REQUIRED_EVENT:
                if field not in event or event.get(field) in ('', None, []):
                    errors.append(f'contact event {idx}: missing {field}')
    return errors

def urgency_status(data):
    text=' '.join([data.get('scenario',''), data.get('safe_next_step','')] + [e.get('pressure_tactic','')+' '+e.get('requested_action','') for e in data.get('contact_events',[]) if isinstance(e,dict)]).lower()
    if data.get('status') == 'do_not_use_until_reviewed':
        return 'DO NOT USE UNTIL OWNER REVIEW'
    high_words=('code','password','wire','crypto','gift card','bank','login','ssn','social security','payment','urgent','arrest','account locked')
    if any(w in text for w in high_words):
        return 'VERIFY BEFORE ACTION — DO NOT CLICK, PAY, OR SHARE CODES'
    return 'LOWER URGENCY — STILL VERIFY THROUGH KNOWN ROUTES'

def render(data):
    errors=validate(data)
    event_blocks=[]
    for idx,event in enumerate(data.get('contact_events',[]),1):
        event_blocks.append(f"""### Contact {idx}: {event.get('channel','Unknown channel')} from {event.get('claimed_sender','Unknown sender')}
- Requested action: {event.get('requested_action','Not specified')}
- Pressure tactic: {event.get('pressure_tactic','Not specified')}
- Risk if true: {event.get('risk_if_true','Not specified')}
- Risk if fake: {event.get('risk_if_fake','Not specified')}
- Source of truth: {event.get('source_of_truth','Not specified')}
- Notes: {event.get('notes','Not specified')}""")
    validation_detail=bullets(errors) if errors else '- No validation errors'
    return f"""# Scam Attention Receipt: {data.get('receipt_name','Untitled receipt')}

**Status:** {urgency_status(data)}  
**Scenario:** {data.get('scenario','Not specified')}  
**Review owner:** {data.get('review_owner','Not specified')}  
**Last reviewed:** {data.get('last_reviewed','Not specified')}  
**Receipt state:** {data.get('status','draft')}  

## Contact events
{chr(10).join(event_blocks) if event_blocks else 'No contact events supplied.'}

## Verification route
{bullets(data.get('verification_route', []))}

## Do not do until verified
{bullets(data.get('do_not_do', []))}

## Safe next step
{data.get('safe_next_step','Not specified')}

## Boundary notes
{bullets(data.get('boundary_notes', []))}

## Boundary
This receipt does not determine that a contact is safe or fraudulent. It is a local attention-and-verification aid. For real fraud, financial loss, identity exposure, workplace threats, account compromise, legal issues, or emergency claims, use official reporting and domain-owner procedures.

## Validation
{'valid' if not errors else 'invalid'}
{validation_detail}
"""

def main(path):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    errors=validate(data)
    print(render(data))
    if errors:
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: render_receipt.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
