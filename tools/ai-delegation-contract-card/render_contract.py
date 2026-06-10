#!/usr/bin/env python3
import json, sys
from pathlib import Path

def bullets(items):
    return '\n'.join(f'- {x}' for x in items) if items else '- Not specified'

def render(d):
    return f"""# AI Delegation Contract Card: {d.get('title','Untitled')}

**Owner:** {d.get('owner','Unspecified')}  
**Workflow:** {d.get('workflow','Unspecified')}  
**Approval status:** {d.get('approval_status','draft-only')}

## AI may do
{bullets(d.get('ai_may_do', []))}

## AI must not do
{bullets(d.get('ai_must_not_do', []))}

## Human approval required for
{bullets(d.get('human_approval_required_for', []))}

## Evidence required
{bullets(d.get('evidence_required', []))}

## Escalation triggers
{bullets(d.get('escalation_triggers', []))}

## Notes
{d.get('notes','')}
"""

def main(path):
    print(render(json.loads(Path(path).read_text())))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: render_contract.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
