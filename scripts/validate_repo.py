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
 'tools/learning-dossier-folder-template/template/mission.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/assessment-evidence-template.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/examples/math-science-proportional-reasoning.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/examples/writing-research-source-checking.md',
 'tools/source-confidence-ledger/source_ledger.py',
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
 ['python3','tools/source-confidence-ledger/source_ledger.py','examples/publishing/source_confidence_example.json'],
]
for cmd in commands:
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        print('FAILED:', ' '.join(cmd))
        print(proc.stdout)
        print(proc.stderr)
        sys.exit(proc.returncode)

# Minimal stdlib schema check for safety-critical agent permission receipts.
schema = json.loads((ROOT / 'schemas/agent-permission-receipt.schema.json').read_text())
receipt = json.loads((ROOT / 'examples/team/agent_permission_receipt_example.json').read_text())
errors = []
for field in schema.get('required', []):
    if field not in receipt:
        errors.append(f'agent receipt missing required field: {field}')
for field in ['secrets_access', 'public_action']:
    allowed = set(schema['properties'][field]['enum'])
    if receipt.get(field) not in allowed:
        errors.append(f'agent receipt invalid {field}: {receipt.get(field)}')
if errors:
    print('schema_check=failed')
    for err in errors:
        print(err)
    sys.exit(1)
print('validation=ok')
print('checked_files=', len(required))
print('checked_commands=', len(commands))
print('schema_checks= 1')
