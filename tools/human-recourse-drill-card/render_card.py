#!/usr/bin/env python3
import json, sys
from pathlib import Path
REQ=['drill_name','service_context','review_owner','review_date','confusing_ai_supported_answer','human_recourse_path_tested','time_to_human','evidence_preserved','repair_outcome','blocked_step','owner_to_fix','next_drill_date','do_not_claim','boundary_note']
def bullets(xs): return '\n'.join(f'- {x}' for x in xs) if xs else '- None recorded'
def validate(d): return [f'missing required field: {f}' for f in REQ if d.get(f) in (None,'',[])]
def render(d):
    e=validate(d)
    status='DRILL HAS REPAIR OWNER' if d.get('owner_to_fix') and d.get('blocked_step') else 'RECOURSE PATH NEEDS OWNER'
    return f"""# Human Recourse Drill Card: {d.get('drill_name','Untitled')}

**Status:** {status}
**Review owner:** {d.get('review_owner','')}
**Review date:** {d.get('review_date','')}

## Service context
{d.get('service_context','')}

## Confusing AI-supported answer
{d.get('confusing_ai_supported_answer','')}

## Human recourse path tested
{bullets(d.get('human_recourse_path_tested',[]))}

## Time to human
{d.get('time_to_human','')}

## Evidence preserved
{bullets(d.get('evidence_preserved',[]))}

## Repair outcome
{d.get('repair_outcome','')}

## Blocked step
{d.get('blocked_step','')}

## Owner to fix
{d.get('owner_to_fix','')}

## Next drill date
{d.get('next_drill_date','')}

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
