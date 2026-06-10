#!/usr/bin/env python3
import json, sys
from pathlib import Path

REQUIRED_TOP = [
    'page_title', 'page_url_or_slug', 'author_or_owner', 'last_reviewed',
    'claim_list', 'source_ledger_ref', 'uncertainty_notes', 'update_policy'
]
REQUIRED_CLAIM = ['claim', 'evidence_type', 'source_refs', 'confidence', 'citation_ready']
ALLOWED_READY = {'yes', 'needs_review', 'no'}


def bullets(items):
    return '\n'.join(f'- {x}' for x in items) if items else '- Not specified'


def validate(data):
    errors = []
    for field in REQUIRED_TOP:
        if field not in data or data.get(field) in ('', None, []):
            errors.append(f'missing required field: {field}')
    for idx, claim in enumerate(data.get('claim_list', []), 1):
        for field in REQUIRED_CLAIM:
            if field not in claim or claim.get(field) in ('', None, []):
                errors.append(f'claim {idx}: missing {field}')
        if claim.get('citation_ready') not in ALLOWED_READY:
            errors.append(f"claim {idx}: citation_ready must be one of {sorted(ALLOWED_READY)}")
    return errors


def readiness_summary(claims):
    counts = {'yes': 0, 'needs_review': 0, 'no': 0}
    for claim in claims:
        if claim.get('citation_ready') in counts:
            counts[claim['citation_ready']] += 1
    if counts['no'] or counts['needs_review']:
        status = 'REVIEW BEFORE PUBLICATION OR ANSWER-LAYER USE'
    else:
        status = 'CITATION HYGIENE READY DRAFT'
    return status, counts


def render(data):
    errors = validate(data)
    validation_detail = bullets(errors) if errors else '- No validation errors'
    status, counts = readiness_summary(data.get('claim_list', []))
    claim_blocks = []
    for idx, claim in enumerate(data.get('claim_list', []), 1):
        claim_blocks.append(f"""### Claim {idx}: {claim.get('claim', 'Untitled claim')}
- Evidence type: {claim.get('evidence_type', 'Not specified')}
- Source refs: {', '.join(claim.get('source_refs', [])) if claim.get('source_refs') else 'Not specified'}
- Confidence: {claim.get('confidence', 'Not specified')}
- Citation ready: {claim.get('citation_ready', 'Not specified')}
- Freshness / review note: {claim.get('freshness_note', 'Not specified')}""")

    return f"""# Answer-Layer Citation Readiness Card: {data.get('page_title', 'Untitled page')}

**Status:** {status}  
**Page URL/slug:** {data.get('page_url_or_slug', 'Not specified')}  
**Author/owner:** {data.get('author_or_owner', 'Not specified')}  
**Last reviewed:** {data.get('last_reviewed', 'Not specified')}  
**Source ledger ref:** {data.get('source_ledger_ref', 'Not specified')}  

## Readiness counts
- Yes: {counts['yes']}
- Needs review: {counts['needs_review']}
- No: {counts['no']}

## Claims
{chr(10).join(claim_blocks) if claim_blocks else 'No claims supplied.'}

## Changed since publication
{bullets(data.get('changed_since_publication', []))}

## Uncertainty notes
{bullets(data.get('uncertainty_notes', []))}

## Update policy
{data.get('update_policy', 'Not specified')}

## Boundary
This card does not guarantee search ranking, AI citation, answer-engine visibility, or factual correctness. It is a local evidence-hygiene and review aid.

## Validation
{'valid' if not errors else 'invalid'}
{validation_detail}
"""


def main(path):
    data = json.loads(Path(path).read_text())
    errors = validate(data)
    print(render(data))
    if errors:
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: render_card.py input.json', file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
