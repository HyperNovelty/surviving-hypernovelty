# Human Recourse Path Card

A local, review-only card for making AI-supported services answer the practical question: **who can fix this when the AI path is wrong, confusing, incomplete, or not allowed to decide?**

Use it when a chatbot, intake assistant, scheduling tool, benefits helper, tutoring assistant, triage layer, or other automated support surface touches people who may need human review, appeal, repair, or accountable follow-up.

## Use

```bash
python3 render_card.py ../../examples/education/human_recourse_student_financial_aid_example.json
python3 render_card.py ../../examples/team/human_recourse_healthcare_scheduling_example.json
python3 render_card.py ../../examples/team/human_recourse_hr_benefits_example.json
```

## What it is for

- Name what the AI/tool may explain, route, draft, or collect.
- Name what the AI/tool must **not** decide.
- Define the human-review triggers that move the case out of the AI path.
- Give the person a visible recourse path: contact/appeal route, response-time expectation, evidence to include, and owner.
- Record repair commitments and unresolved gaps without promising legal, medical, employment, benefits, or schooling outcomes.

## Good recourse language

- "Use this path when the answer affects eligibility, money, placement, safety, health, discipline, employment, or rights."
- "Include the AI answer, the date, your account/case ID if appropriate, and what seems wrong or missing."
- "A named human owner reviews the case before any denial, escalation, penalty, or final decision."

## Boundary

This is **not** a legal appeals process, rights guarantee, medical/financial/employment/schooling decision, compliance assurance, or promise of outcome. It is a local review aid for making the human path visible. Domain owners approve real timelines, escalation language, and authority.
