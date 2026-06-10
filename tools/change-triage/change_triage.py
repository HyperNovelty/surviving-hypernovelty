#!/usr/bin/env python3
import json, sys
from pathlib import Path

def classify(item):
    impact = int(item.get('impact', 3))
    urgency = int(item.get('urgency', 3))
    reversibility = int(item.get('reversibility', 3))
    ownership = item.get('ownership', 'mine')
    if ownership == 'someone_else' and impact < 5:
        return 'delegate'
    if impact >= 4 and urgency >= 4:
        return 'act_now'
    if impact >= 4 and urgency < 4:
        return 'monitor'
    if urgency <= 2 and reversibility >= 4:
        return 'ignore_for_now'
    return 'learn_later'

def main(path):
    data = json.loads(Path(path).read_text())
    out = {k: [] for k in ['act_now','monitor','delegate','ignore_for_now','learn_later']}
    for item in data.get('changes', []):
        out[classify(item)].append(item)
    print(json.dumps({'subject': data.get('subject','unspecified'), 'triage': out}, indent=2))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: change_triage.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
