# Surviving Hypernovelty

Early public candidate for practical adaptation tools for living, working, learning, deciding, and staying sane when reality changes faster than institutions can update.

This repo is a local-first starter-kit candidate: small tools, templates, schemas, worksheets, and synthetic demos that help people convert overwhelm into reviewable decisions and practices.

## Starter kit

1. **Novelty Load Calculator** — estimate how much simultaneous change a person/team is carrying.
2. **Change Triage Worksheet** — sort incoming changes into act / monitor / delegate / ignore / learn later.
3. **AI Delegation Contract Card** — define what an AI/tool may do, must not do, and must prove.
4. **Learning Dossier Folder Template** — the “Next Classroom May Be a Folder” starter structure.
5. **Source Confidence Ledger** — track claims, sources, confidence, verification status, and downstream use.
6. **Agent Permission Receipt Card** — document what an agent can read, write, expose, spend, publish, or trigger.
7. **Assessment Evidence Packet** — add proof-of-learning evidence to the Learning Dossier verification layer.
8. **Answer-Layer Citation Readiness Card** — prepare page-level claim/source/date/update receipts for answer-layer citation hygiene, including a public-page survival receipt example.
9. **Agent Toolchain Exposure Map** — map multi-agent/tool workflows across identities, data touched, outputs, handoffs, and human checkpoints.
10. **Assessment Evidence Packet Lite** — one-assignment/week proof-of-learning bundle that avoids AI-detector false certainty.
11. **Human Premium Trust Surface Card** — decide what AI should remove, support, protect, or leave human in trust-sensitive work. Current examples cover generic client onboarding, healthcare front desk/care navigation, and student support first response.
12. **Human Premium Service Readiness Review** — consolidated practical screen for deciding whether a service workflow is ready for AI support without weakening trust-bearing human work.
13. **Policy Freshness Diff Card** — compare a policy/rule against a new signal and propose a bounded, owner-reviewed interim update.

## Repo principles

- Useful before clever.
- Local-first and privacy-preserving by default.
- Free primitives first; any hosted, paid, institutional, or customer-facing use requires separate human review.
- Human approval remains explicit where decisions affect public actions, accounts, money, medicine, law, schooling, or other high-stakes domains.
- Genericity test: if a quick AI prompt can produce equivalent value, the tool needs sharper context, evidence, workflow, examples, or should be parked.

## Quick start

```bash
python3 tools/novelty-load-calculator/novelty_load.py examples/individual/novelty_load_example.json
python3 tools/change-triage/change_triage.py examples/individual/change_triage_example.json
python3 tools/ai-delegation-contract-card/render_contract.py examples/creator/ai_delegation_contract_example.json
python3 tools/agent-permission-receipt-card/render_receipt.py examples/team/agent_permission_receipt_example.json
python3 tools/agent-toolchain-exposure-map/render_map.py examples/team/agent_toolchain_exposure_map_example.json
python3 tools/assessment-evidence-packet-lite/render_packet.py examples/education/assessment_evidence_packet_lite_example.json
python3 tools/answer-layer-citation-readiness-card/render_card.py examples/publishing/answer_layer_citation_readiness_example.json
python3 tools/answer-layer-citation-readiness-card/render_card.py examples/publishing/publisher_page_receipt_example.json
python3 tools/human-premium-trust-surface-card/render_card.py examples/team/human_premium_trust_surface_example.json
python3 tools/human-premium-trust-surface-card/render_card.py examples/team/human_premium_healthcare_front_desk_example.json
python3 tools/human-premium-trust-surface-card/render_card.py examples/education/human_premium_student_support_example.json
# rendered example: docs/rendered/human_premium_healthcare_front_desk_card.md
# rendered example: docs/rendered/human_premium_student_support_card.md
python3 tools/policy-freshness-diff-card/render_card.py examples/institution/policy_freshness_diff_card_example.json
# rendered example: docs/rendered/policy_freshness_diff_card_example.md
python3 tools/source-confidence-ledger/source_ledger.py examples/publishing/source_confidence_example.json
python3 scripts/validate_repo.py
```

Open `START_HERE.html` for a browser-readable overview.

For publication boundaries, see `docs/PUBLICATION_BOUNDARY.md`. For a 5-minute
review path, see `docs/REVIEWER_QUICKSTART.md`.

Run `python3 scripts/build_demo_index.py` to generate `build/demo_index.html`, a
local reviewer-friendly index of the synthetic starter-tool demos.

## Status

Local starter kit v0.1 and early public candidate. Public publishing/GitHub repo creation should remain human-approved.
