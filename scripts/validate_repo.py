#!/usr/bin/env python3
import argparse
from pathlib import Path
import json
import subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description='Validate local repository examples, schemas, renderers, and generated index.')
parser.add_argument('--check', action='store_true', help='Read-only mode: do not rebuild generated artifacts; fail if demo index is stale.')
args = parser.parse_args()
required = [
 'README.md', 'docs/roadmap.md', 'docs/free-vs-paid.md', 'docs/research-run.md',
 'tools/novelty-load-calculator/novelty_load.py',
 'tools/change-triage/change_triage.py',
 'tools/ai-delegation-contract-card/render_contract.py',
 'tools/agent-permission-receipt-card/render_receipt.py',
 'tools/agent-identity-scope-roster/render_roster.py',
 'tools/non-human-identity-review-receipt/render_receipt.py',
 'tools/human-recourse-path-card/render_card.py',
 'tools/scam-attention-receipt/render_receipt.py',
 'tools/verification-literacy-mini-lab/render_lab.py',
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
 'scripts/build_form_index.py',
 'scripts/smoke_forms_static.py',
 'scripts/smoke_forms_runtime.js',
 'schemas/agent-toolchain-exposure-map.schema.json',
 'schemas/agent-identity-scope-roster.schema.json',
 'schemas/non-human-identity-review-receipt.schema.json',
 'schemas/human-recourse-path-card.schema.json',
 'schemas/scam-attention-receipt.schema.json',
 'schemas/verification-literacy-mini-lab.schema.json',
 'schemas/assessment-evidence-packet-lite.schema.json',
 'schemas/human-premium-trust-surface.schema.json',
 'schemas/policy-freshness-diff-card.schema.json',
 'examples/team/agent_toolchain_exposure_map_example.json',
 'examples/team/agent_identity_scope_roster_example.json',
 'examples/team/non_human_identity_review_receipt_example.json',
 'examples/education/human_recourse_student_financial_aid_example.json',
 'examples/team/human_recourse_healthcare_scheduling_example.json',
 'examples/team/human_recourse_hr_benefits_example.json',
 'examples/education/assessment_evidence_packet_lite_example.json',
 'examples/team/human_premium_trust_surface_example.json',
 'examples/team/human_premium_healthcare_front_desk_example.json',
 'examples/education/human_premium_student_support_example.json',
 'examples/institution/policy_freshness_diff_card_example.json',
 'examples/publishing/publisher_page_receipt_example.json',
 'docs/human_premium_service_readiness_review.md',
 'docs/rendered/policy_freshness_diff_card_example.md',
 'docs/rendered/agent_identity_scope_roster_example.md',
 'docs/rendered/non_human_identity_review_receipt_example.md',
 'docs/rendered/human_recourse_student_financial_aid_example.md',
 'docs/rendered/human_recourse_healthcare_scheduling_example.md',
 'docs/rendered/human_recourse_hr_benefits_example.md',
 'docs/rendered/scam_attention_receipt_example.md',
 'docs/rendered/verification_literacy_scam_lab_example.md',
 'docs/rendered/human_recourse_scam_contact_example.md',
 'tools/ai-use-clarity-micro-policy-card/render_card.py',
 'schemas/ai-use-clarity-micro-policy-card.schema.json',
 'examples/education/ai_use_clarity_micro_policy_card_example.json',
 'docs/rendered/ai_use_clarity_micro_policy_card_example.md',
 'tools/adaptation-debt-ledger/render_ledger.py',
 'schemas/adaptation-debt-ledger.schema.json',
 'examples/institution/adaptation_debt_ledger_example.json',
 'docs/rendered/adaptation_debt_ledger_example.md',
 'tools/visible-thinking-repair-ticket/render_ticket.py',
 'schemas/visible-thinking-repair-ticket.schema.json',
 'examples/education/visible_thinking_repair_ticket_example.json',
 'docs/rendered/visible_thinking_repair_ticket_example.md',
 'tools/platformized-news-diet-receipt/render_receipt.py',
 'schemas/platformized-news-diet-receipt.schema.json',
 'examples/media/platformized_news_diet_receipt_example.json',
 'docs/rendered/platformized_news_diet_receipt_example.md',
 'forms/index.html',
 'forms/shared/form_runtime.js',
 'forms/shared/form_styles.css',
 'forms/agent-identity-scope-roster.html',
 'forms/ai-use-clarity-micro-policy-card.html',
 'forms/adaptation-debt-ledger.html',
 'forms/visible-thinking-repair-ticket.html',
 'forms/platformized-news-diet-receipt.html',
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
 ['python3','tools/agent-identity-scope-roster/render_roster.py','examples/team/agent_identity_scope_roster_example.json'],
 ['python3','tools/non-human-identity-review-receipt/render_receipt.py','examples/team/non_human_identity_review_receipt_example.json'],
 ['python3','tools/human-recourse-path-card/render_card.py','examples/education/human_recourse_student_financial_aid_example.json'],
 ['python3','tools/human-recourse-path-card/render_card.py','examples/team/human_recourse_healthcare_scheduling_example.json'],
 ['python3','tools/human-recourse-path-card/render_card.py','examples/team/human_recourse_hr_benefits_example.json'],
 ['python3','tools/scam-attention-receipt/render_receipt.py','examples/media/scam_attention_receipt_example.json'],
 ['python3','tools/verification-literacy-mini-lab/render_lab.py','examples/education/verification_literacy_scam_lab_example.json'],
 ['python3','tools/human-recourse-path-card/render_card.py','examples/media/human_recourse_scam_contact_example.json'],
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
 ['python3','scripts/build_form_index.py'],
 ['python3','scripts/smoke_forms_static.py'],
 ['node','scripts/smoke_forms_runtime.js'],
 ['python3','tools/ai-use-clarity-micro-policy-card/render_card.py','examples/education/ai_use_clarity_micro_policy_card_example.json'],
 ['python3','tools/adaptation-debt-ledger/render_ledger.py','examples/institution/adaptation_debt_ledger_example.json'],
 ['python3','tools/visible-thinking-repair-ticket/render_ticket.py','examples/education/visible_thinking_repair_ticket_example.json'],
 ['python3','tools/platformized-news-diet-receipt/render_receipt.py','examples/media/platformized_news_diet_receipt_example.json'],
]
if args.check:
    commands = [
        cmd for cmd in commands
        if cmd not in (
            ['python3','scripts/build_demo_index.py'],
            ['python3','scripts/build_form_index.py'],
        )
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

def validate_schema_value(schema, value, label):
    expected_type = schema.get('type')
    if expected_type == 'object':
        if not isinstance(value, dict):
            errors.append(f'{label} expected object')
            return
        for field in schema.get('required', []):
            if field not in value:
                errors.append(f'{label} missing required field: {field}')
        for field, subschema in schema.get('properties', {}).items():
            if field in value:
                validate_schema_value(subschema, value[field], f'{label}.{field}')
    elif expected_type == 'array':
        if not isinstance(value, list):
            errors.append(f'{label} expected array')
            return
        if len(value) < schema.get('minItems', 0):
            errors.append(f'{label} expected at least {schema.get("minItems")} item(s)')
        item_schema = schema.get('items')
        if item_schema:
            for idx, item in enumerate(value, 1):
                validate_schema_value(item_schema, item, f'{label}[{idx}]')
    elif expected_type == 'string':
        if not isinstance(value, str):
            errors.append(f'{label} expected string')
    elif expected_type == 'boolean':
        if not isinstance(value, bool):
            errors.append(f'{label} expected boolean')
    if 'enum' in schema and value not in schema['enum']:
        errors.append(f'{label} invalid enum value: {value}')

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

roster_schema = json.loads((ROOT / 'schemas/agent-identity-scope-roster.schema.json').read_text())
roster = json.loads((ROOT / 'examples/team/agent_identity_scope_roster_example.json').read_text())
for field in roster_schema.get('required', []):
    if field not in roster:
        errors.append(f'agent identity roster missing required field: {field}')
roster_agent_schema = roster_schema['properties']['agents']['items']
allowed_public = set(roster_agent_schema['properties']['public_action']['enum'])
allowed_secrets = set(roster_agent_schema['properties']['secrets_access']['enum'])
allowed_spend = set(roster_agent_schema['properties']['spend_authority']['enum'])
allowed_approval = set(roster_agent_schema['properties']['approval_state']['enum'])
for idx, agent in enumerate(roster.get('agents', []), 1):
    for field in roster_agent_schema.get('required', []):
        if field not in agent:
            errors.append(f'agent identity roster agent {idx} missing required field: {field}')
    if agent.get('public_action') not in allowed_public:
        errors.append(f'agent identity roster agent {idx} invalid public_action: {agent.get("public_action")}')
    if agent.get('secrets_access') not in allowed_secrets:
        errors.append(f'agent identity roster agent {idx} invalid secrets_access: {agent.get("secrets_access")}')
    if agent.get('spend_authority') not in allowed_spend:
        errors.append(f'agent identity roster agent {idx} invalid spend_authority: {agent.get("spend_authority")}')
    if agent.get('approval_state') not in allowed_approval:
        errors.append(f'agent identity roster agent {idx} invalid approval_state: {agent.get("approval_state")}')
rendered_roster = (ROOT / 'docs/rendered/agent_identity_scope_roster_example.md').read_text(encoding='utf-8')
if 'Agent Identity & Scope Roster' not in rendered_roster or 'Visibility and review aid only' not in rendered_roster:
    errors.append('agent identity roster rendered example missing expected headings/boundary')


queued_specs = [
    ('schemas/non-human-identity-review-receipt.schema.json', 'examples/team/non_human_identity_review_receipt_example.json', 'docs/rendered/non_human_identity_review_receipt_example.md', 'Non-Human Identity Review Receipt', ['python3','tools/non-human-identity-review-receipt/render_receipt.py','examples/team/non_human_identity_review_receipt_example.json']),
    ('schemas/human-recourse-path-card.schema.json', 'examples/education/human_recourse_student_financial_aid_example.json', 'docs/rendered/human_recourse_student_financial_aid_example.md', 'Human Recourse Path Card', ['python3','tools/human-recourse-path-card/render_card.py','examples/education/human_recourse_student_financial_aid_example.json']),
    ('schemas/human-recourse-path-card.schema.json', 'examples/team/human_recourse_healthcare_scheduling_example.json', 'docs/rendered/human_recourse_healthcare_scheduling_example.md', 'Human Recourse Path Card', ['python3','tools/human-recourse-path-card/render_card.py','examples/team/human_recourse_healthcare_scheduling_example.json']),
    ('schemas/human-recourse-path-card.schema.json', 'examples/team/human_recourse_hr_benefits_example.json', 'docs/rendered/human_recourse_hr_benefits_example.md', 'Human Recourse Path Card', ['python3','tools/human-recourse-path-card/render_card.py','examples/team/human_recourse_hr_benefits_example.json']),
    ('schemas/scam-attention-receipt.schema.json', 'examples/media/scam_attention_receipt_example.json', 'docs/rendered/scam_attention_receipt_example.md', 'Scam Attention Receipt', ['python3','tools/scam-attention-receipt/render_receipt.py','examples/media/scam_attention_receipt_example.json']),
    ('schemas/verification-literacy-mini-lab.schema.json', 'examples/education/verification_literacy_scam_lab_example.json', 'docs/rendered/verification_literacy_scam_lab_example.md', 'Verification Literacy Mini-Lab', ['python3','tools/verification-literacy-mini-lab/render_lab.py','examples/education/verification_literacy_scam_lab_example.json']),
    ('schemas/human-recourse-path-card.schema.json', 'examples/media/human_recourse_scam_contact_example.json', 'docs/rendered/human_recourse_scam_contact_example.md', 'Human Recourse Path Card', ['python3','tools/human-recourse-path-card/render_card.py','examples/media/human_recourse_scam_contact_example.json']),
    ('schemas/ai-use-clarity-micro-policy-card.schema.json', 'examples/education/ai_use_clarity_micro_policy_card_example.json', 'docs/rendered/ai_use_clarity_micro_policy_card_example.md', 'AI Use Clarity Micro-Policy Card', ['python3','tools/ai-use-clarity-micro-policy-card/render_card.py','examples/education/ai_use_clarity_micro_policy_card_example.json']),
    ('schemas/adaptation-debt-ledger.schema.json', 'examples/institution/adaptation_debt_ledger_example.json', 'docs/rendered/adaptation_debt_ledger_example.md', 'Adaptation Debt Ledger', ['python3','tools/adaptation-debt-ledger/render_ledger.py','examples/institution/adaptation_debt_ledger_example.json']),
    ('schemas/visible-thinking-repair-ticket.schema.json', 'examples/education/visible_thinking_repair_ticket_example.json', 'docs/rendered/visible_thinking_repair_ticket_example.md', 'Visible Thinking Repair Ticket', ['python3','tools/visible-thinking-repair-ticket/render_ticket.py','examples/education/visible_thinking_repair_ticket_example.json']),
    ('schemas/platformized-news-diet-receipt.schema.json', 'examples/media/platformized_news_diet_receipt_example.json', 'docs/rendered/platformized_news_diet_receipt_example.md', 'Platformized News Diet Receipt', ['python3','tools/platformized-news-diet-receipt/render_receipt.py','examples/media/platformized_news_diet_receipt_example.json']),
]
for schema_rel, example_rel, rendered_rel, expected_title, render_cmd in queued_specs:
    schema = json.loads((ROOT / schema_rel).read_text())
    example = json.loads((ROOT / example_rel).read_text())
    validate_schema_value(schema, example, example_rel)
    rendered = (ROOT / rendered_rel).read_text(encoding='utf-8')
    if expected_title not in rendered or 'Boundary note' not in rendered:
        errors.append(f'{rendered_rel} missing expected title/boundary')
    proc = subprocess.run(render_cmd, cwd=ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        errors.append(f'{rendered_rel} renderer failed during freshness check: {" ".join(render_cmd)}')
    elif proc.stdout != rendered:
        errors.append(f'{rendered_rel} is stale: renderer stdout differs from committed rendered Markdown')

ai_policy = json.loads((ROOT / 'examples/education/ai_use_clarity_micro_policy_card_example.json').read_text())
if not ai_policy.get('allowed_uses') or not ai_policy.get('disallowed_uses'):
    errors.append('ai use clarity card must include allowed and disallowed uses')
if not any(item.get('requires_disclosure') for item in ai_policy.get('allowed_uses', [])):
    errors.append('ai use clarity card must require disclosure for at least one allowed use')

adaptation = json.loads((ROOT / 'examples/institution/adaptation_debt_ledger_example.json').read_text())
if not adaptation.get('adaptation_debts') or not adaptation.get('top_repair_queue'):
    errors.append('adaptation debt ledger must include debts and repair queue')
if not {item.get('priority') for item in adaptation.get('adaptation_debts', [])}.issubset({'high', 'medium', 'low'}):
    errors.append('adaptation debt ledger contains invalid debt priority')

repair_ticket = json.loads((ROOT / 'examples/education/visible_thinking_repair_ticket_example.json').read_text())
if not repair_ticket.get('missing_evidence') or not repair_ticket.get('repair_requests'):
    errors.append('visible thinking repair ticket must include missing evidence and repair requests')
if any(item.get('evidence_type') == 'detector_result' for item in repair_ticket.get('repair_requests', [])):
    errors.append('visible thinking repair ticket must not treat detector output as repair evidence')

news_receipt = json.loads((ROOT / 'examples/media/platformized_news_diet_receipt_example.json').read_text())
if not news_receipt.get('source_chain_items') or not news_receipt.get('reflection_prompts'):
    errors.append('platformized news diet receipt must include source-chain items and reflection prompts')
if any(item.get('confidence') not in {'higher', 'medium', 'low', 'unknown'} for item in news_receipt.get('source_chain_items', [])):
    errors.append('platformized news diet receipt contains invalid confidence label')

identity_review = json.loads((ROOT / 'examples/team/non_human_identity_review_receipt_example.json').read_text())
if len(identity_review.get('identity_reviews', [])) < 3:
    errors.append('non-human identity review receipt should include at least three synthetic identity reviews')
allowed_identity_decisions = {'renew', 'renew_with_changes', 'pause', 'revoke', 'escalate'}
if any(item.get('decision') not in allowed_identity_decisions for item in identity_review.get('identity_reviews', [])):
    errors.append('non-human identity review receipt contains invalid decision')
if not any(item.get('unresolved_gaps') for item in identity_review.get('identity_reviews', [])):
    errors.append('non-human identity review receipt should include at least one unresolved gap')
if any('secret' in ' '.join(item.get('permission_evidence', [])).lower() and 'absent' not in ' '.join(item.get('permission_evidence', [])).lower() for item in identity_review.get('identity_reviews', [])):
    errors.append('non-human identity review receipt must not store or expose secrets as permission evidence')

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
print('schema_checks= 17')

form_files = [
    'forms/agent-identity-scope-roster.html',
    'forms/ai-use-clarity-micro-policy-card.html',
    'forms/adaptation-debt-ledger.html',
    'forms/visible-thinking-repair-ticket.html',
    'forms/platformized-news-diet-receipt.html',
]
boundary_text = 'Local review aid only; no legal/compliance/security/academic-integrity authority; no public/account/spend/outreach/deploy actions.'
form_index = (ROOT / 'forms/index.html').read_text(encoding='utf-8')
form_errors = []
for form_file in form_files:
    if Path(form_file).name not in form_index:
        form_errors.append(f'forms/index.html missing link to {form_file}')
    text = (ROOT / form_file).read_text(encoding='utf-8')
    if 'boundary-text' not in text and boundary_text not in text:
        form_errors.append(f'{form_file} missing boundary text placeholder or text')
    if not all(token in text for token in ['Copy Markdown', 'Download Markdown', 'Download JSON', 'Reset to Example', 'Clear Draft', 'clear-draft']):
        form_errors.append(f'{form_file} missing expected form actions')
    if not all(token in text for token in ['requiredFields', 'fromJson', 'toJson']):
        form_errors.append(f'{form_file} missing JSON round-trip spec hooks')
runtime_text = (ROOT / 'forms/shared/form_runtime.js').read_text(encoding='utf-8')
for token in ['Import JSON', 'Load JSON into Form', 'importJson', 'exportJson', 'Malformed JSON', 'Missing required field', 'localStorage', 'draftKey', 'clearDraft', 'Local draft']:
    if token not in runtime_text:
        form_errors.append(f'forms/shared/form_runtime.js missing JSON import/export token: {token}')
for shared_file in ['forms/shared/form_runtime.js', 'forms/shared/form_styles.css']:
    text = (ROOT / shared_file).read_text(encoding='utf-8')
    blocked_patterns = ['http://', 'https://', 'fetch(', 'XMLHttpRequest', 'navigator.sendBeacon', '<iframe', 'form action=', 'analytics', 'telemetry', 'cdn']
    for pattern in blocked_patterns:
        if pattern.lower() in text.lower():
            form_errors.append(f'{shared_file} contains blocked local-only pattern: {pattern}')
for form_file in form_files + ['forms/index.html']:
    text = (ROOT / form_file).read_text(encoding='utf-8').lower()
    blocked_patterns = ['http://', 'https://', 'fetch(', 'xmlhttprequest', 'navigator.sendbeacon', '<iframe', 'form action=', 'analytics', 'telemetry', 'cdn']
    for pattern in blocked_patterns:
        if pattern in text:
            form_errors.append(f'{form_file} contains blocked local-only pattern: {pattern}')
if boundary_text not in form_index:
    form_errors.append('forms/index.html missing boundary text')
if args.check:
    sys.path.insert(0, str(ROOT))
    from scripts import build_form_index
    if form_index != build_form_index.render():
        form_errors.append('forms/index.html is stale')
if form_errors:
    print('forms_check=failed')
    for err in form_errors:
        print(err)
    sys.exit(1)
print('forms_check=ok')

demo_index = ROOT / 'build/demo_index.html'
if not demo_index.exists():
    print('demo_index_check=failed missing build/demo_index.html')
    sys.exit(1)
demo_text = demo_index.read_text(encoding='utf-8')
if 'Surviving Hypernovelty Demo Index' not in demo_text or 'Local starter-kit demos' not in demo_text:
    print('demo_index_check=failed unexpected content')
    sys.exit(1)
if args.check:
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(ROOT))
    from scripts import build_demo_index
    expected_demo_text = build_demo_index.render()
    if demo_text != expected_demo_text:
        print('demo_index_check=failed stale build/demo_index.html')
        sys.exit(1)
print('demo_index_check=ok')
print('mode=', 'check' if args.check else 'normal')
