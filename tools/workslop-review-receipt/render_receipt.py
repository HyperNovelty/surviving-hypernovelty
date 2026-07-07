#!/usr/bin/env python3
import json, sys
from pathlib import Path
REQUIRED=['receipt_name','work_context','review_owner','review_date','artifact','intended_use','review_checks','known_weak_spots','human_edits','confidence_after_review','next_reviewer','do_not_claim','boundary_note']
VALID_RESULTS={'passed','needs_work','not_checked','not_applicable'}
VALID_CONF={'high','medium','low','unknown'}
def bullets(xs): return '\n'.join(f'- {x}' for x in xs) if xs else '- None recorded'
def table(rows):
    head='| Check | Result | Evidence |\n| --- | --- | --- |'
    body='\n'.join(f"| {r.get('check','')} | {r.get('result','')} | {str(r.get('evidence','')).replace(chr(10),'<br>')} |" for r in rows)
    return head+'\n'+body
def validate(d):
    e=[]
    for f in REQUIRED:
        if d.get(f) in (None,'',[]): e.append(f'missing required field: {f}')
    art=d.get('artifact',{})
    for f in ['title','source','status_before_review','ai_assistance_disclosed']:
        if f not in art: e.append(f'artifact missing field: {f}')
    for i,c in enumerate(d.get('review_checks',[]),1):
        if c.get('result') not in VALID_RESULTS: e.append(f'review_checks[{i}] invalid result: {c.get("result")}')
    if d.get('confidence_after_review') not in VALID_CONF: e.append('invalid confidence_after_review')
    return e
def render(d):
    e=validate(d); art=d.get('artifact',{})
    status='READY FOR NEXT HUMAN REVIEW' if not e and d.get('confidence_after_review') in {'high','medium'} else 'NEEDS REVIEW BEFORE USE'
    return f"""# Workslop Review Receipt: {d.get('receipt_name','Untitled')}

**Status:** {status}
**Review owner:** {d.get('review_owner','')}
**Review date:** {d.get('review_date','')}
**Confidence after review:** {d.get('confidence_after_review','unknown')}

## Work context
{d.get('work_context','')}

## Artifact
- Title: {art.get('title','')}
- Source: {art.get('source','')}
- Status before review: {art.get('status_before_review','')}
- AI assistance disclosed: {art.get('ai_assistance_disclosed','')}

## Intended use
{d.get('intended_use','')}

## Review checks
{table(d.get('review_checks',[]))}

## Known weak spots
{bullets(d.get('known_weak_spots',[]))}

## Human edits made
{bullets(d.get('human_edits',[]))}

## Next reviewer
{d.get('next_reviewer','')}

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
    if len(sys.argv)!=2: print('usage: render_receipt.py input.json', file=sys.stderr); sys.exit(2)
    raise SystemExit(main(sys.argv[1]))
