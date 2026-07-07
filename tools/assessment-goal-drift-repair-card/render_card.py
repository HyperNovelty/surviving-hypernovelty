#!/usr/bin/env python3
import json, sys
from pathlib import Path
REQ=['card_name','context','review_owner','review_date','original_assignment','original_learning_goal','ai_offload_risk','evidence_still_needed','redesigned_proof_artifact','allowed_ai_role','equity_access_check','recourse_path','do_not_claim','boundary_note']
def bullets(xs): return '\n'.join(f'- {x}' for x in xs) if xs else '- None recorded'
def validate(d): return [f'missing required field: {f}' for f in REQ if d.get(f) in (None,'',[])]
def render(d):
    e=validate(d)
    return f"""# Assessment Goal Drift Repair Card: {d.get('card_name','Untitled')}

**Review owner:** {d.get('review_owner','')}
**Review date:** {d.get('review_date','')}

## Context
{d.get('context','')}

## Original assignment
{d.get('original_assignment','')}

## Original learning goal
{d.get('original_learning_goal','')}

## What AI can now offload
{bullets(d.get('ai_offload_risk',[]))}

## Evidence still needed
{bullets(d.get('evidence_still_needed',[]))}

## Redesigned proof artifact
{bullets(d.get('redesigned_proof_artifact',[]))}

## Allowed AI role
{d.get('allowed_ai_role','')}

## Equity/access check
{bullets(d.get('equity_access_check',[]))}

## Recourse path if questioned
{bullets(d.get('recourse_path',[]))}

## Do not claim
{bullets(d.get('do_not_claim',[]))}

## Boundary note
{d.get('boundary_note','')}

## Validation
{'valid' if not e else 'invalid'}
{bullets(e) if e else '- No validation errors'}
"""
def main(p):
    d=json.loads(Path(p).read_text(encoding='utf-8')); print(render(d)); return 1 if validate(d) else 0
if __name__=='__main__':
    if len(sys.argv)!=2: print('usage: render_card.py input.json', file=sys.stderr); sys.exit(2)
    raise SystemExit(main(sys.argv[1]))
