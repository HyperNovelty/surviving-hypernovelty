#!/usr/bin/env python3
import json, sys
from pathlib import Path
REQ=['sheet_name','context','review_owner','review_date','job_to_be_done','why_approved_tools_failed','data_touched','risk_exposure','safer_workaround','policy_or_product_owner','non_punitive_next_step','do_not_claim','boundary_note']
def bullets(xs): return '\n'.join(f'- {x}' for x in xs) if xs else '- None recorded'
def validate(d): return [f'missing required field: {f}' for f in REQ if d.get(f) in (None,'',[])]
def render(d):
    e=validate(d)
    return f"""# Shadow AI Amnesty Triage Sheet: {d.get('sheet_name','Untitled')}

**Review owner:** {d.get('review_owner','')}
**Review date:** {d.get('review_date','')}

## Context
{d.get('context','')}

## Job to be done
{d.get('job_to_be_done','')}

## Why approved tools failed
{bullets(d.get('why_approved_tools_failed',[]))}

## Data touched
{bullets(d.get('data_touched',[]))}

## Risk exposure
{bullets(d.get('risk_exposure',[]))}

## Safer workaround
{bullets(d.get('safer_workaround',[]))}

## Policy/product owner
{d.get('policy_or_product_owner','')}

## Non-punitive next step
{d.get('non_punitive_next_step','')}

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
    if len(sys.argv)!=2: print('usage: render_sheet.py input.json', file=sys.stderr); sys.exit(2)
    raise SystemExit(main(sys.argv[1]))
