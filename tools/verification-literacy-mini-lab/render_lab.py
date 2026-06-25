#!/usr/bin/env python3
import json, sys
from pathlib import Path

REQUIRED_TOP=['lab_name','scenario','audience','facilitator','last_reviewed','learning_goal','claims_or_messages','verification_steps','reflection_prompts','safe_use_boundary']
REQUIRED_MSG=['message','surface_cues','possible_source_of_truth','safe_action','confidence_before','confidence_after']
ALLOWED_STATUS={'draft','ready_for_classroom_or_workshop_review','needs_facilitator_review','do_not_use_until_reviewed'}

def bullets(items):
    return '\n'.join(f'- {x}' for x in items) if items else '- Not specified'

def validate(data):
    errors=[]
    for field in REQUIRED_TOP:
        if field not in data or data.get(field) in ('', None, []):
            errors.append(f'missing required field: {field}')
    if data.get('status','draft') not in ALLOWED_STATUS:
        errors.append(f"status must be one of {sorted(ALLOWED_STATUS)}")
    msgs=data.get('claims_or_messages',[])
    if not isinstance(msgs,list):
        errors.append('claims_or_messages must be a list')
    else:
        for idx,msg in enumerate(msgs,1):
            for field in REQUIRED_MSG:
                if field not in msg or msg.get(field) in ('', None, []):
                    errors.append(f'message {idx}: missing {field}')
    return errors

def render(data):
    errors=validate(data)
    msg_blocks=[]
    for idx,msg in enumerate(data.get('claims_or_messages',[]),1):
        msg_blocks.append(f"""### Message {idx}
> {msg.get('message','Not specified')}

- Surface cues to notice:
{bullets(msg.get('surface_cues', []))}
- Possible source of truth: {msg.get('possible_source_of_truth','Not specified')}
- Safe action: {msg.get('safe_action','Not specified')}
- Confidence before verification: {msg.get('confidence_before','Not specified')}
- Confidence after verification: {msg.get('confidence_after','Not specified')}""")
    validation_detail=bullets(errors) if errors else '- No validation errors'
    return f"""# Verification Literacy Mini-Lab: {data.get('lab_name','Untitled lab')}

**Status:** {data.get('status','draft')}  
**Scenario:** {data.get('scenario','Not specified')}  
**Audience:** {data.get('audience','Not specified')}  
**Facilitator:** {data.get('facilitator','Not specified')}  
**Last reviewed:** {data.get('last_reviewed','Not specified')}  
**Duration:** {data.get('duration_minutes','20–30 minutes')}  

## Learning goal
{data.get('learning_goal','Not specified')}

## Synthetic messages
{chr(10).join(msg_blocks) if msg_blocks else 'No messages supplied.'}

## Verification steps
{bullets(data.get('verification_steps', []))}

## Reflection prompts
{bullets(data.get('reflection_prompts', []))}

## Boundary notes / safe-use boundary
{bullets(data.get('safe_use_boundary', []))}

## Boundary
This mini-lab labels confidence and safer verification routes. It does not certify truth, investigate live fraud, provide legal/financial/cybersecurity advice, or replace official reporting and recovery procedures.

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
    if len(sys.argv)!=2:
        print('usage: render_lab.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
