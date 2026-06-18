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
 'tools/assessment-evidence-packet-lite/render_packet.py',
 'tools/human-premium-trust-surface-card/render_card.py',
 'tools/policy-freshness-diff-card/render_card.py',
 'tools/learning-dossier-folder-template/template/mission.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/assessment-evidence-template.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/examples/math-science-proportional-reasoning.md',
 'tools/learning-dossier-folder-template/template/assessment-evidence/examples/writing-research-source-checking.md',
 'tools/source-confidence-ledger/source_ledger.py',
 'scripts/build_demo_index.py',
 'schemas/agent-toolchain-exposure-map.schema.json',
 'schemas/assessment-evidence-packet-lite.schema.json',
 'schemas/human-premium-trust-surface.schema.json',
 'schemas/policy-freshness-diff-card.schema.json',
 'examples/team/agent_toolchain_exposure_map_example.json',
 'examples/education/assessment_evidence_packet_lite_example.json',
 'examples/team/human_premium_trust_surface_example.json',
 'examples/team/human_premium_healthcare_front_desk_example.json',
 'examples/education/human_premium_student_support_example.json',
 'examples/institution/policy_freshness_diff_card_example.json',
 'examples/publishing/publisher_page_receipt_example.json',
 'docs/human_premium_service_readiness_review.md',
 'docs/rendered/policy_freshness_diff_card_example.md',
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
 ['python3','tools/answer-layer-citation-readiness-card/render_card.py','examples/publishing/publisher_page_receipt_example.json'],
 ['python3','tools/assessment-evidence-packet-lite/render_packet.py','examples/education/assessment_evidence_packet_lite_example.json'],
 ['python3','tools/human-premium-trust-surface-card/render_card.py','examples/team/human_premium_trust_surface_example.json'],
 ['python3','tools/human-premium-trust-surface-card/render_card.py','examples/team/human_premium_healthcare_front_desk_example.json'],
 ['python3','tools/human-premium-trust-surface-card/render_card.py','examples/education/human_premium_student_support_example.json'],
 ['python3','tools/policy-freshness-diff-card/render_card.py','examples/institution/policy_freshness_diff_card_example.json'],
 ['python3','tools/source-confidence-ledger/source_ledger.py','examples/publishing/source_confidence_example.json'],
 ['python3','scripts/build_demo_index.py'],
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
allowed_ready = set(citation_schema['properties']['claim_list']['items']['properties']['citation_ready']['enum'])
for example_path in [
    'examples/publishing/answer_layer_citation_readiness_example.json',
    'examples/publishing/publisher_page_receipt_example.json',
]:
    citation = json.loads((ROOT / example_path).read_text())
    for field in citation_schema.get('required', []):
        if field not in citation:
            errors.append(f'{example_path} missing required field: {field}')
    for idx, claim in enumerate(citation.get('claim_list', []), 1):
        for field in citation_schema['properties']['claim_list']['items'].get('required', []):
            if field not in claim:
                errors.append(f'{example_path} claim {idx} missing required field: {field}')
        if claim.get('citation_ready') not in allowed_ready:
            errors.append(f'{example_path} claim {idx} invalid citation_ready: {claim.get("citation_ready")}')
    if 'page_receipt' in citation:
        receipt = citation.get('page_receipt') or {}
        for field in ['canonical_url', 'intended_audience', 'citation_friendly_summary', 'next_review_trigger']:
            if not receipt.get(field):
                errors.append(f'{example_path} page_receipt missing required local field: {field}')
        for field in ['answer_layer_risks', 'human_reader_checks', 'do_not_claim']:
            if not receipt.get(field):
                errors.append(f'{example_path} page_receipt missing required local list: {field}')

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

assessment_schema = json.loads((ROOT / 'schemas/assessment-evidence-packet-lite.schema.json').read_text())
assessment = json.loads((ROOT / 'examples/education/assessment_evidence_packet_lite_example.json').read_text())
for field in assessment_schema.get('required', []):
    if field not in assessment:
        errors.append(f'assessment packet missing required field: {field}')
allowed_ai = set(assessment_schema['properties']['allowed_help']['properties']['ai_allowed']['enum'])
if assessment.get('allowed_help', {}).get('ai_allowed') not in allowed_ai:
    errors.append(f'assessment packet invalid ai_allowed: {assessment.get("allowed_help", {}).get("ai_allowed")}')
allowed_review = set(assessment_schema['properties']['human_review']['properties']['review_needed']['enum'])
if assessment.get('human_review', {}).get('review_needed') not in allowed_review:
    errors.append(f'assessment packet invalid review_needed: {assessment.get("human_review", {}).get("review_needed")}')
for section, required_fields in [
    ('allowed_help', assessment_schema['properties']['allowed_help'].get('required', [])),
    ('evidence', assessment_schema['properties']['evidence'].get('required', [])),
    ('human_review', assessment_schema['properties']['human_review'].get('required', [])),
]:
    for field in required_fields:
        if field not in assessment.get(section, {}):
            errors.append(f'assessment packet {section} missing required field: {field}')

human_premium_schema = json.loads((ROOT / 'schemas/human-premium-trust-surface.schema.json').read_text())
allowed_decisions = set(human_premium_schema['properties']['decision']['enum'])
step_schema = human_premium_schema['properties']['surface_steps']['items']
allowed_trust = set(step_schema['properties']['trust_weight']['enum'])
allowed_posture = set(step_schema['properties']['ai_posture']['enum'])
for example_path in [
    'examples/team/human_premium_trust_surface_example.json',
    'examples/team/human_premium_healthcare_front_desk_example.json',
    'examples/education/human_premium_student_support_example.json',
]:
    human_premium = json.loads((ROOT / example_path).read_text())
    for field in human_premium_schema.get('required', []):
        if field not in human_premium:
            errors.append(f'{example_path} missing required field: {field}')
    if human_premium.get('decision') not in allowed_decisions:
        errors.append(f'{example_path} invalid decision: {human_premium.get("decision")}')
    for idx, step in enumerate(human_premium.get('surface_steps', []), 1):
        for field in step_schema.get('required', []):
            if field not in step:
                errors.append(f'{example_path} step {idx} missing required field: {field}')
        if step.get('trust_weight') not in allowed_trust:
            errors.append(f'{example_path} step {idx} invalid trust_weight: {step.get("trust_weight")}')
        if step.get('ai_posture') not in allowed_posture:
            errors.append(f'{example_path} step {idx} invalid ai_posture: {step.get("ai_posture")}')

policy_schema = json.loads((ROOT / 'schemas/policy-freshness-diff-card.schema.json').read_text())
policy = json.loads((ROOT / 'examples/institution/policy_freshness_diff_card_example.json').read_text())
for field in policy_schema.get('required', []):
    if field not in policy:
        errors.append(f'policy freshness diff missing required field: {field}')
allowed_evidence = set(policy_schema['properties']['evidence_strength']['enum'])
allowed_verdicts = set(policy_schema['properties']['freshness_verdict']['enum'])
allowed_change_types = set(policy_schema['properties']['proposed_diff']['properties']['change_type']['enum'])
if policy.get('evidence_strength') not in allowed_evidence:
    errors.append(f'policy freshness diff invalid evidence_strength: {policy.get("evidence_strength")}')
if policy.get('freshness_verdict') not in allowed_verdicts:
    errors.append(f'policy freshness diff invalid freshness_verdict: {policy.get("freshness_verdict")}')
for field in policy_schema['properties']['proposed_diff'].get('required', []):
    if field not in policy.get('proposed_diff', {}):
        errors.append(f'policy freshness diff proposed_diff missing required field: {field}')
if policy.get('proposed_diff', {}).get('change_type') not in allowed_change_types:
    errors.append(f'policy freshness diff invalid change_type: {policy.get("proposed_diff", {}).get("change_type")}')
for field in policy_schema['properties']['review'].get('required', []):
    if field not in policy.get('review', {}):
        errors.append(f'policy freshness diff review missing required field: {field}')
rendered_policy = (ROOT / 'docs/rendered/policy_freshness_diff_card_example.md').read_text(encoding='utf-8')
if 'Policy Freshness Diff Card' not in rendered_policy or 'Review aid only' not in rendered_policy:
    errors.append('policy freshness rendered example missing expected headings/boundary')

if errors:
    print('schema_check=failed')
    for err in errors:
        print(err)
    sys.exit(1)
print('validation=ok')
print('checked_files=', len(required))
print('checked_commands=', len(commands))
print('schema_checks= 6')

demo_index = ROOT / 'build/demo_index.html'
if not demo_index.exists():
    print('demo_index_check=failed missing build/demo_index.html')
    sys.exit(1)
demo_text = demo_index.read_text(encoding='utf-8')
if 'Surviving Hypernovelty Demo Index' not in demo_text or 'Local starter-kit demos' not in demo_text:
    print('demo_index_check=failed unexpected content')
    sys.exit(1)
print('demo_index_check=ok')
