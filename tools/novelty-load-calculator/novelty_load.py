#!/usr/bin/env python3
import json, sys
from pathlib import Path

def score_change(c):
    impact = int(c.get('impact', 3))
    urgency = int(c.get('urgency', 3))
    uncertainty = int(c.get('uncertainty', 3))
    agency = int(c.get('agency', 3))
    return impact + urgency + uncertainty + (6 - agency)

def band(total):
    if total <= 15: return 'low'
    if total <= 30: return 'moderate'
    if total <= 50: return 'high'
    return 'overload'

def main(path):
    data = json.loads(Path(path).read_text())
    rows = []
    for c in data.get('changes', []):
        rows.append({**c, 'load_score': score_change(c)})
    total = sum(r['load_score'] for r in rows)
    top = sorted(rows, key=lambda r: r['load_score'], reverse=True)[:3]
    result = {
        'subject': data.get('subject', 'unspecified'),
        'total_novelty_load': total,
        'band': band(total),
        'top_load_sources': top,
        'recommended_next_step': 'triage the top load sources into act / monitor / delegate / ignore / learn later'
    }
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: novelty_load.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
