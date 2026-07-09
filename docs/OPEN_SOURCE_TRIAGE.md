# Surviving Hypernovelty Open-Source Triage v0.1

Recorded: 2026-07-09T12:21:16

## Reconciliation first

- Local repo `/home/aware1/surviving-hypernovelty` was compared against `origin/main` with `git fetch origin main`; local and remote were even (`0 0`).
- README currently lists 30 primitives. No new standalone primitive is required to proceed.
- The July 9 candidate ideas were compared against existing tools/examples. Most should become kit pages, examples, or article outlines rather than new schemas.

## Recommendation

Freeze the primitive count for v0.1. Package the existing 30 primitives into five public-facing kits and use future ideas as examples unless they pass a stricter new-audience/new-decision test.

## Five-pack open-source packaging

### 1. Agent Delegation Safety Kit

**Promise:** Before an AI agent touches tools, files, customers, accounts, money, publishing, or internal systems, make its authority reviewable.

**Audience:** Team leads, ops owners, security/IT partners, managers, creators using agent workflows.

**Included primitives:**
- AI Delegation Contract Card
- Agent Permission Receipt Card
- Agent Identity & Scope Roster
- Non-Human Identity Review Receipt
- Agent Revocation Reality Check

**Candidate handling:** Agent Onboarding Packet Lite should be a bundle/index card that references these existing tools, not primitive #31.

**Boundary:** Not a security certification, legal/compliance clearance, or deployment approval.

### 2. Scam / Deepfake Verification Kit

**Promise:** Slow down high-pressure impersonation, fraud, and bad source-chain decisions before people click, pay, share codes, or approve sensitive actions.

**Audience:** Families, school offices, nonprofits, small businesses, admins, finance/ops teams.

**Included primitives:**
- Scam Attention Receipt
- Verification Literacy Mini-Lab: Scam Edition
- Human Recourse Path Card v2 — scam-contact example
- Human Recourse Drill Card

**Candidate handling:** Deepfake Approval Pause Card should start as a scam/deepfake example, not a new primitive.

**Boundary:** Not fraud detection, cybersecurity certification, or financial/legal advice.

### 3. AI Work Quality Kit

**Promise:** Separate generated/drafted work from reviewed, owned, repairable work.

**Audience:** Managers, creators, teams, reviewers, instructors, service owners.

**Included primitives:**
- Workslop Review Receipt
- Human Premium Trust Surface Card
- Human Premium Service Readiness Review
- AI Use Clarity Micro-Policy Card
- Human Recourse Path Card

**Candidate handling:** AI Agent Error-Ownership Receipt should be a companion example, not a standalone tool yet.

**Boundary:** Not HR advice, incident-management replacement, or blame automation.

### 4. Future of Education Evidence Kit

**Promise:** Move from AI-cheating panic to visible learning evidence, local validity, and clear disclosure rules.

**Audience:** Teachers, students, program chairs, instructional designers, academic-integrity leads.

**Included primitives:**
- Learning Dossier Folder Template
- Assessment Evidence Packet Lite
- Assessment Goal Drift Repair Card
- Visible Thinking Repair Ticket
- Shadow AI Amnesty Triage Sheet

**Candidate handling:** Shadow AI Habit-to-Curriculum Translation Sheet is now an education example attached to Shadow AI Amnesty, not a new standalone schema.

**Boundary:** Does not normalize cheating, data leakage, AI-detector certainty, or automated grading.

### 5. Source Trust / Answer-Layer Kit

**Promise:** Make page-level claims more reviewable and citation-ready without promising search visibility or laundering provenance into truth.

**Audience:** Publishers, researchers, nonprofits, institutional comms, creators, iPublishOS users.

**Included primitives:**
- Source Confidence Ledger
- Answer-Layer Citation Readiness Card
- Provenance Interpretation Label Card
- Provenance Breakage Receipt
- Platformized News Diet Receipt

**Candidate handling:** Answer-Engine Source Fitness Receipt should be an example/variant under Answer-Layer Citation Readiness before becoming standalone.

**Boundary:** No GEO-spam framing; does not guarantee AI citation, ranking, traffic, trust, or correctness.

## New-idea disposition table

| Idea | Disposition | Reason |
|---|---|---|
| Agent Onboarding Packet Lite | Bundle/index card in Agent Delegation Safety Kit | Existing agent primitives already cover permission, identity, tool exposure, review, and revocation. |
| AI Agent Error-Ownership Receipt | Companion example in AI Work Quality Kit | Best attached to Workslop Review + Recourse rather than standalone incident schema. |
| AI Marking Local Validity Check Card | Future education example/prototype | Strong, but should anchor to Assessment Evidence and Goal Drift before new schema. |
| Learning-to-Work AI Readiness Gap Map | Article outline / later narrow example | Too consulting-shaped until tied to one course and one job task. |
| Shadow AI Habit-to-Curriculum Translation Sheet | Education-specific example added now | Differentiates curriculum/evidence from workplace amnesty without duplicating schema. |
| Answer-Engine Source Fitness Receipt | Example under Answer-Layer Citation Readiness | Avoids GEO-spam and duplicate citation-readiness tooling. |
| AI Journalism Oversight Disclosure Card | Media-trust example/article | Useful, but overlaps provenance/source-confidence until differentiated by oversight evidence. |
| Deepfake Approval Pause Card | Scam/deepfake example extension | Existing scam/recourse tools cover most fields. |
| Adaptation Load Transfer Map | Later worksheet feeding Adaptation Debt Ledger | Good thesis, but not first public pack. |
| Forecast Claim Review Receipt | Park | Wait for ForecastBench / Signal Atlas stabilization. |

## Backlog rule

If a new idea has the same audience and same decision as an existing primitive, make it an example. If it is same primitive/different domain, put it in a kit. If it is a new audience plus new decision, consider a new primitive. If it is useful but vague, make an article outline. If it is high-liability, park it.
