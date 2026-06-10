#!/usr/bin/env python3
import json, sys
from pathlib import Path

ALLOWED = {'strong','light','unverified','rejected'}

def main(path):
    data = json.loads(Path(path).read_text())
    errors = []
    for i, claim in enumerate(data.get('claims', []), 1):
        if claim.get('verification_status') not in ALLOWED:
            errors.append(f'claim {i}: invalid verification_status')
        if not claim.get('claim'):
            errors.append(f'claim {i}: missing claim')
        if not claim.get('sources'):
            errors.append(f'claim {i}: missing sources')
    result = {'ledger': data.get('ledger','untitled'), 'claim_count': len(data.get('claims', [])), 'errors': errors, 'valid': not errors}
    print(json.dumps(result, indent=2))
    if errors:
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: source_ledger.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
