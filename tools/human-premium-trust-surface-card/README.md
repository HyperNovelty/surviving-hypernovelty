# Human Premium Trust Surface Card

A local, review-only worksheet for deciding what AI should remove, support, protect, or leave human in trust-sensitive work.

It is for moments where the main risk is not whether automation is possible, but whether automation would weaken the human premium: presence, judgment, accountability, care, discretion, taste, or relationship repair.

## Use

```bash
python3 render_card.py ../../examples/team/human_premium_trust_surface_example.json
python3 render_card.py ../../examples/team/human_premium_healthcare_front_desk_example.json
python3 render_card.py ../../examples/education/human_premium_student_support_example.json
```

## What it is for

- Name the work surface being considered for AI support.
- Separate admin machine-work from trust-bearing human work.
- Record which parts AI can remove, support, protect, or should not touch.
- Add human checkpoints before any live process change.

## Example choices

- `human_premium_trust_surface_example.json` — generic client onboarding surface for professional-services or operations teams.
- `human_premium_healthcare_front_desk_example.json` — healthcare front-desk/care-navigation surface that keeps patient trust, escalation, privacy, and clinical judgment human-owned. Use synthetic/demo data only.
- `human_premium_student_support_example.json` — education/student-support surface that keeps care, safeguarding/escalation, disability/privacy, and placement/discipline decisions human-owned. Use synthetic/demo data only.

## Decision language

- `remove` means AI may take repeatable machine-work off the human desk after template and fallback review.
- `support` means AI may prepare private drafts, summaries, or checklists for a human owner.
- `protect` means the step may use AI flags only if a named human owns escalation and final judgment.
- `leave_human` means the trust-bearing exchange should not be automated.

## Boundary

This does **not** decide policy, staffing, compliance, employment action, medical/legal/financial advice, or customer promises. It is a local review aid only. Domain owners approve actual workflow changes.
