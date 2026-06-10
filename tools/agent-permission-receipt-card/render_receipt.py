#!/usr/bin/env python3
import json, sys
from pathlib import Path

RISKY_ACTIONS = {'spend_money', 'publish_publicly', 'email_external', 'delete_data', 'access_secrets', 'change_dns', 'deploy_production'}

def bullets(items):
    return '\n'.join(f'- {x}' for x in items) if items else '- Not specified'

def risk_flags(d):
    actions = set(d.get('allowed_actions', []))
    flags = sorted(actions & RISKY_ACTIONS)
    if d.get('secrets_access') == 'allowed':
        flags.append('secrets_access_allowed')
    if d.get('public_action') == 'allowed':
        flags.append('public_action_allowed')
    return flags

def render(d):
    flags = risk_flags(d)
    status = 'REVIEW REQUIRED' if flags else 'LOWER-RISK DRAFT RECEIPT'
    return f"""# Agent Permission Receipt: {d.get('agent_name','Unnamed agent')}

**Status:** {status}  
**Owner:** {d.get('owner','Unspecified')}  
**Purpose:** {d.get('purpose','Unspecified')}  
**Identity/auth:** {d.get('identity_auth','Unspecified')}  

## Read scopes
{bullets(d.get('read_scopes', []))}

## Write scopes
{bullets(d.get('write_scopes', []))}

## Allowed actions
{bullets(d.get('allowed_actions', []))}

## Explicitly disallowed actions
{bullets(d.get('disallowed_actions', []))}

## Secrets boundary
{d.get('secrets_boundary','Not specified')}

## Audit / evidence log
{d.get('audit_log','Not specified')}

## Rollback owner
{d.get('rollback_owner','Not specified')}

## Human approval point
{d.get('human_approval_point','Not specified')}

## Escalation triggers
{bullets(d.get('escalation_triggers', []))}

## Risk flags
{bullets(flags)}

## Notes
{d.get('notes','')}
"""

def main(path):
    data = json.loads(Path(path).read_text())
    print(render(data))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: render_receipt.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
