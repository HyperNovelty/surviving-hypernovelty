#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
required = [
 'README.md', 'docs/roadmap.md', 'docs/free-vs-paid.md', 'docs/research-run.md',
 'tools/novelty-load-calculator/novelty_load.py',
 'tools/change-triage/change_triage.py',
 'tools/ai-delegation-contract-card/render_contract.py',
 'tools/agent-permission-receipt-card/render_receipt.py',
 'tools/agent-toolchain-exposure-map/render_map.py',
 'tools/answer-layer-citation-readiness-card/render_card.py',
 'tools/learning-dossier-folder-template/template/mission.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/assessment-evidence-template.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/examples/math-science-proportional-reasoning.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/examples/writing-research-source-checking.md',
 'tools/source-confidence-ledger/source_ledger.py',
 'schemas/agent-toolchain-exposure-map.schema.json',
 'examples/team/agent_toolchain_exposure_map_example.json',
]
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    print('missing files:', missing)
    sys.exit(1)
commands = [
 ['python3','tools/novelty-load-calculator/novelty_load.py','examples/individual/novelty_load_example.json'],
 ['python3','tools/change-triage/change_triage.py','examples/individual/change_triage_example.json'],
 ['python3','tools/ai-delegation-contract-card/render_contract.py','examples/creator/ai_delegation_contract_example.json'],
 ['python3','tools/agent-permission-receipt-card/render_receipt.py','examples/team/agent_permission_receipt_example.json'],
 ['python3','tools/agent-toolchain-exposure-map/render_map.py','examples/team/agent_toolchain_exposure_map_example.json'],
 ['python3','tools/answer-layer-citation-readiness-card/render_card.py','examples/publishing/answer_layer_citation_readiness_example.json'],
 ['python3','tools/source-confidence-ledger/source_ledger.py','examples/publishing/source_confidence_example.json'],
]
for cmd in commands:
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        print('FAILED:', ' '.join(cmd))
        print(proc.stdout)
        print(proc.stderr)
        sys.exit(proc.returncode)

# Minimal stdlib schema checks for locally validated JSON examples.
errors = []

agent_schema = json.loads((ROOT / 'schemas/agent-permission-receipt.schema.json').read_text())
receipt = json.loads((ROOT / 'examples/team/agent_permission_receipt_example.json').read_text())
for field in agent_schema.get('required', []):
    if field not in receipt:
        errors.append(f'agent receipt missing required field: {field}')
for field in ['secrets_access', 'public_action']:
    allowed = set(agent_schema['properties'][field]['enum'])
    if receipt.get(field) not in allowed:
        errors.append(f'agent receipt invalid {field}: {receipt.get(field)}')

citation_schema = json.loads((ROOT / 'schemas/answer-layer-citation-readiness.schema.json').read_text())
citation = json.loads((ROOT / 'examples/publishing/answer_layer_citation_readiness_example.json').read_text())
for field in citation_schema.get('required', []):
    if field not in citation:
        errors.append(f'citation readiness missing required field: {field}')
allowed_ready = set(citation_schema['properties']['claim_list']['items']['properties']['citation_ready']['enum'])
for idx, claim in enumerate(citation.get('claim_list', []), 1):
    for field in citation_schema['properties']['claim_list']['items'].get('required', []):
        if field not in claim:
            errors.append(f'citation readiness claim {idx} missing required field: {field}')
    if claim.get('citation_ready') not in allowed_ready:
        errors.append(f'citation readiness claim {idx} invalid citation_ready: {claim.get("citation_ready")}')

toolchain_schema = json.loads((ROOT / 'schemas/agent-toolchain-exposure-map.schema.json').read_text())
toolchain = json.loads((ROOT / 'examples/team/agent_toolchain_exposure_map_example.json').read_text())
for field in toolchain_schema.get('required', []):
    if field not in toolchain:
        errors.append(f'agent toolchain map missing required field: {field}')
agent_required = toolchain_schema['properties']['agents']['items'].get('required', [])
allowed_secrets = set(toolchain_schema['properties']['agents']['items']['properties']['secrets_access']['enum'])
for idx, agent in enumerate(toolchain.get('agents', []), 1):
    for field in agent_required:
        if field not in agent:
            errors.append(f'agent toolchain map agent {idx} missing required field: {field}')
    if agent.get('secrets_access') not in allowed_secrets:
        errors.append(f'agent toolchain map agent {idx} invalid secrets_access: {agent.get("secrets_access")}')
handoff_required = toolchain_schema['properties']['handoffs']['items'].get('required', [])
for idx, handoff in enumerate(toolchain.get('handoffs', []), 1):
    for field in handoff_required:
        if field not in handoff:
            errors.append(f'agent toolchain map handoff {idx} missing required field: {field}')
for field in toolchain_schema['properties']['shared_boundaries'].get('required', []):
    if field not in toolchain.get('shared_boundaries', {}):
        errors.append(f'agent toolchain map shared_boundaries missing required field: {field}')

if errors:
    print('schema_check=failed')
    for err in errors:
        print(err)
    sys.exit(1)
print('validation=ok')
print('checked_files=', len(required))
print('checked_commands=', len(commands))
print('schema_checks= 3')
