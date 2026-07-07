#!/usr/bin/env python3
import json, sys
from pathlib import Path
REQ=['card_name','scenario','review_owner','review_date','credential_signal','what_it_supports','what_it_does_not_prove','context_checks','audience_safe_language','next_review_step','boundary_note']
def bullets(xs): return '\n'.join(f'- {x}' for x in xs) if xs else '- None recorded'
def validate(d):
    e=[f'missing required field: {f}' for f in REQ if d.get(f) in (None,'',[])]
    cs=d.get('credential_signal',{})
    for f in ['present','issuer_or_tool','credential_status']:
        if f not in cs: e.append(f'credential_signal missing field: {f}')
    return e
def render(d):
    e=validate(d); cs=d.get('credential_signal',{})
    return f"""# Provenance Interpretation Label Card: {d.get('card_name','Untitled')}

**Review owner:** {d.get('review_owner','')}
**Review date:** {d.get('review_date','')}

## Scenario
{d.get('scenario','')}

## Credential signal
- Present: {cs.get('present','')}
- Issuer/tool: {cs.get('issuer_or_tool','')}
- Status: {cs.get('credential_status','')}

## What this supports
{bullets(d.get('what_it_supports',[]))}

## What this does not prove
{bullets(d.get('what_it_does_not_prove',[]))}

## Context checks
{bullets(d.get('context_checks',[]))}

## Audience-safe language
{d.get('audience_safe_language','')}

## Next review step
{d.get('next_review_step','')}

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
