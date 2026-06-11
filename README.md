# Surviving Hypernovelty

Practical adaptation tools for living, working, learning, deciding, and staying sane when reality changes faster than institutions can update.

This repo is the open/free primitive library for Hypernovelty Institute: small tools, templates, schemas, worksheets, and local-first demos that help people convert overwhelm into reviewable decisions and practices.

## Starter kit

1. **Novelty Load Calculator** — estimate how much simultaneous change a person/team is carrying.
2. **Change Triage Worksheet** — sort incoming changes into act / monitor / delegate / ignore / learn later.
3. **AI Delegation Contract Card** — define what an AI/tool may do, must not do, and must prove.
4. **Learning Dossier Folder Template** — the “Next Classroom May Be a Folder” starter structure.
5. **Source Confidence Ledger** — track claims, sources, confidence, verification status, and downstream use.
6. **Agent Permission Receipt Card** — document what an agent can read, write, expose, spend, publish, or trigger.
7. **Assessment Evidence Packet** — add proof-of-learning evidence to the Learning Dossier verification layer.
8. **Answer-Layer Citation Readiness Card** — prepare page-level claim/source/date/update receipts for answer-layer citation hygiene.
9. **Agent Toolchain Exposure Map** — map multi-agent/tool workflows across identities, data touched, outputs, handoffs, and human checkpoints.

## Repo principles

- Useful before clever.
- Local-first and privacy-preserving by default.
- Free primitives first; paid tools later only where customization, hosting, support, or institutional review adds real value.
- Human approval remains explicit where decisions affect public actions, accounts, money, medicine, law, schooling, or other high-stakes domains.
- Genericity test: if a quick AI prompt can produce equivalent value, the tool needs sharper context, evidence, workflow, examples, or should be parked.

## Quick start

```bash
python3 tools/novelty-load-calculator/novelty_load.py examples/individual/novelty_load_example.json
python3 tools/change-triage/change_triage.py examples/individual/change_triage_example.json
python3 tools/ai-delegation-contract-card/render_contract.py examples/creator/ai_delegation_contract_example.json
python3 tools/agent-permission-receipt-card/render_receipt.py examples/team/agent_permission_receipt_example.json
python3 tools/agent-toolchain-exposure-map/render_map.py examples/team/agent_toolchain_exposure_map_example.json
python3 tools/answer-layer-citation-readiness-card/render_card.py examples/publishing/answer_layer_citation_readiness_example.json
python3 tools/source-confidence-ledger/source_ledger.py examples/publishing/source_confidence_example.json
python3 scripts/validate_repo.py
```

Open `START_HERE.html` for a browser-readable overview.

## Status

Local starter kit v0.1. Public publishing/GitHub repo creation should remain human-approved.
