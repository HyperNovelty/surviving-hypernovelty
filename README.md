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
14. **Agent Identity & Scope Roster** — inventory non-human identities, owners, scopes, logs, expiry dates, and escalation triggers before agents gain broader authority.
15. **AI Use Clarity Micro-Policy Card** — translate broad AI rules into one task-specific allowed/not-allowed/evidence/disclosure card.
16. **Adaptation Debt Ledger** — name stale assumptions, symptoms, owners, affected people, and cheap next reviews.
17. **Visible Thinking Repair Ticket** — repair missing learning evidence without detector-first overclaiming.
18. **Platformized News Diet Receipt** — track news source chains across platforms, creators, AI summaries, and direct sources.
19. **Non-Human Identity Review Receipt** — periodically renew, pause, revoke, or escalate non-human identities with permission evidence, log evidence, gates, and expiry dates.
20. **Human Recourse Path Card** — make the human review, appeal, repair, and fallback path visible when an AI-supported service gives a confusing, wrong, incomplete, or consequential answer.
21. **Scam Attention Receipt** — turn suspicious calls, texts, emails, DMs, ads, or social messages into a calm verification receipt before anyone clicks, pays, shares codes, or replies under pressure.
22. **Verification Literacy Mini-Lab: Scam Edition** — a 20–30 minute synthetic-message lab for practicing source-chain checks and confidence before/after verification.
23. **Human Recourse Path Card v2 — scam-contact example** — extends the recourse path primitive with claimed authority, source-of-truth, evidence preservation, and safe escalation for scam pressure.
24. **Provenance Breakage Receipt** — record where content-credential/provenance signals survive, transform, disappear, or become unverifiable as media moves through exports, reposts, screenshots, and slide decks.
25. **Agent Revocation Reality Check** — verify whether an agent pause/revoke path names the systems, owners, downstream effects, evidence preservation, and restart criteria needed before broader delegation.

26. **Workslop Review Receipt** — separate generated/drafted work from reviewed/defensible work with owner, checks, weak spots, edits, and next reviewer.
27. **Assessment Goal Drift Repair Card** — repair assignments when AI changes what the old task measures, without detector-first certainty.
28. **Provenance Interpretation Label Card** — explain what a provenance/content-credential label supports and what it does not prove.
29. **Shadow AI Amnesty Triage Sheet** — non-punitive intake for shadow-AI use patterns that reveal unmet workflow demand.
30. **Human Recourse Drill Card** — rehearse whether a human fallback path actually works after a confusing AI-supported answer.

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
python3 tools/agent-identity-scope-roster/render_roster.py examples/team/agent_identity_scope_roster_example.json
python3 tools/ai-use-clarity-micro-policy-card/render_card.py examples/education/ai_use_clarity_micro_policy_card_example.json
python3 tools/adaptation-debt-ledger/render_ledger.py examples/institution/adaptation_debt_ledger_example.json
python3 tools/visible-thinking-repair-ticket/render_ticket.py examples/education/visible_thinking_repair_ticket_example.json
python3 tools/platformized-news-diet-receipt/render_receipt.py examples/media/platformized_news_diet_receipt_example.json
python3 tools/non-human-identity-review-receipt/render_receipt.py examples/team/non_human_identity_review_receipt_example.json
python3 tools/human-recourse-path-card/render_card.py examples/education/human_recourse_student_financial_aid_example.json
python3 tools/human-recourse-path-card/render_card.py examples/team/human_recourse_healthcare_scheduling_example.json
python3 tools/human-recourse-path-card/render_card.py examples/team/human_recourse_hr_benefits_example.json
python3 tools/scam-attention-receipt/render_receipt.py examples/media/scam_attention_receipt_example.json
python3 tools/verification-literacy-mini-lab/render_lab.py examples/education/verification_literacy_scam_lab_example.json
python3 tools/human-recourse-path-card/render_card.py examples/media/human_recourse_scam_contact_example.json
python3 tools/provenance-breakage-receipt/render_receipt.py examples/media/provenance_breakage_receipt_example.json
python3 tools/agent-revocation-reality-check/render_check.py examples/team/agent_revocation_reality_check_example.json
python3 tools/workslop-review-receipt/render_receipt.py examples/team/workslop_review_receipt_example.json
python3 tools/assessment-goal-drift-repair-card/render_card.py examples/education/assessment_goal_drift_repair_card_example.json
python3 tools/provenance-interpretation-label-card/render_card.py examples/media/provenance_interpretation_label_card_example.json
python3 tools/shadow-ai-amnesty-triage-sheet/render_sheet.py examples/team/shadow_ai_amnesty_triage_sheet_example.json
python3 tools/human-recourse-drill-card/render_card.py examples/education/human_recourse_drill_card_example.json
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
# rendered example: docs/rendered/agent_identity_scope_roster_example.md
# rendered example: docs/rendered/non_human_identity_review_receipt_example.md
python3 tools/source-confidence-ledger/source_ledger.py examples/publishing/source_confidence_example.json
python3 scripts/validate_repo.py
```

Open `START_HERE.html` for a browser-readable overview.

For publication boundaries, see `docs/PUBLICATION_BOUNDARY.md`. For a 5-minute
review path, see `docs/REVIEWER_QUICKSTART.md`.

Open `forms/index.html` for offline browser-local forms for the five June 18
primitives. The forms work from `file://`, use synthetic defaults, preview
Markdown, and download Markdown/JSON without network calls or account actions.

Run `python3 scripts/build_demo_index.py` to generate `build/demo_index.html`, a
local reviewer-friendly index of the synthetic starter-tool demos.

## Status

Local starter kit v0.1 and early public candidate. Public publishing/GitHub repo creation should remain human-approved.
