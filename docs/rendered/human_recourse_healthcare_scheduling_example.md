# Human Recourse Path Card: Healthcare scheduling assistant recourse path

**Status:** DO NOT USE UNTIL OWNER REVIEW  
**Service context:** A healthcare scheduling assistant helps patients find appointment options, preparation instructions, and routine follow-up routes. It must not triage urgent symptoms, make clinical decisions, deny access, or promise costs/outcomes.  
**Review owner:** Clinic operations lead with clinician and privacy/compliance owner review  
**Last reviewed:** 2026-06-25  
**Card state:** do_not_use_until_reviewed  

## AI role
Collect routine scheduling preferences, offer approved appointment instructions, and prepare private staff notes for human review when a patient needs escalation or accommodation.

## The AI/tool does not decide
- Medical urgency, diagnosis, treatment, medication, cost promise, eligibility, refusal of care, or privacy/safety escalation decision.
- Whether a patient should delay urgent or emergency care.

## Human-review triggers
### Trigger 1: Patient describes urgent, worsening, safety-related, or confusing symptoms.
- Human owner: Nurse/clinician escalation owner
- Why this leaves the AI path: The assistant cannot assess urgency or clinical risk.
### Trigger 2: Patient cannot access a needed appointment, interpreter, disability accommodation, transport option, or caregiver support through the automated path.
- Human owner: Care-navigation or front-desk lead
- Why this leaves the AI path: Access barriers require accountable human repair.
### Trigger 3: Patient disputes a scheduling instruction, cost-related message, privacy issue, or cancellation/no-show consequence.
- Human owner: Clinic operations lead or privacy/compliance owner
- Why this leaves the AI path: The case may affect trust, privacy, money, or care continuity.

## Visible recourse path
- Label shown to the person: Need a person to review this scheduling answer?
- Contact route: Call the clinic front desk or use the secure patient portal message category 'Scheduling answer review'.
- Appeal/review step: A staff member checks the scheduling record and routes clinical, privacy, access, or cost questions to the right human owner.
- Fallback if no response: If symptoms may be urgent, use the clinic's approved urgent-care instructions or emergency guidance; otherwise ask for the operations lead callback queue.
- Response-time expectation: Synthetic example: same business day for access, cancellation, or confusing-care-route issues; routine questions by next business day. Real timelines require clinic approval.

## Evidence to include
- Date/time of assistant interaction and copied answer if available.
- Appointment type requested and any appointment/case reference number.
- What part of the answer seems unsafe, inaccessible, conflicting, or incorrect.
- Do not paste sensitive medical details beyond what the approved clinic channel requests.

## Repair commitments
- Provide a visible human fallback in every scheduling path.
- Review disputed access/cancellation/cost messages before applying consequences.
- Update approved scripts when recurring confusion appears.

## Boundary notes
- Review aid only; not medical, legal, privacy/compliance, insurance, or emergency advice.
- Use synthetic/demo data only in repo examples.
- Actual urgent-care language and escalation authority require clinician and privacy/compliance approval.

## Boundary
This card does not create a legal appeals process, rights guarantee, medical/financial/employment/schooling decision, compliance assurance, or promise of outcome. It is a local review aid for making the human path visible. Domain owners approve real timelines, escalation language, and authority.

## Validation
valid
- No validation errors

