# Human Premium Trust Surface Card: Healthcare front-desk trust surface

**Status:** HUMAN PREMIUM PROTECTED — REVIEW BEFORE CHANGE  
**Organization/team:** Small clinic or care-navigation team  
**Review owner:** Clinic operations lead with clinical/privacy owner review  
**Last reviewed:** 2026-06-12  
**Decision:** needs_owner_review  

## Trust context
The team wants AI to reduce appointment, intake, and follow-up paperwork while preserving the human moments where patients need reassurance, privacy judgment, escalation, or accountable care navigation.

## Stakeholders
- Patient or caregiver
- Front-desk coordinator
- Nurse or care navigator
- Clinician or domain lead
- Privacy/compliance owner

## Posture counts
- Remove machine-work: 1
- Support human work: 1
- Protect from automation pressure: 1
- Leave human: 1
- High-trust steps: 2

## Surface steps
### Step 1: Confirm appointment logistics and routine reminders
- Current owner: Front-desk coordinator
- Trust weight: low
- AI posture: remove
- Reason: This is repeatable administrative burden when the patient has a visible human fallback and the message is approved by the practice.
- Risk if automated: Patients may feel trapped if the reminder system makes rescheduling or human contact difficult.
### Step 2: Pre-fill non-sensitive intake fields already supplied by the patient
- Current owner: Front-desk coordinator with patient confirmation
- Trust weight: medium
- AI posture: support
- Reason: AI can reduce duplicate typing, but the patient or staff member must confirm the record before it is used.
- Risk if automated: Incorrect demographics, contact details, or visit context could propagate into later workflow steps.
### Step 3: Respond to anxiety, confusion, grief, anger, or embarrassment
- Current owner: Trained human staff member
- Trust weight: high
- AI posture: leave_human
- Reason: The valuable work is human presence, tone, repair, and accountable listening. AI may prepare private notes but should not substitute for the trust-bearing exchange.
- Risk if automated: The patient may experience the clinic as indifferent, unsafe, or evasive at the exact moment trust is being formed.
### Step 4: Flag possible escalation, safety, privacy, or special-handling needs
- Current owner: Nurse, clinician, or privacy/compliance owner
- Trust weight: high
- AI posture: protect
- Reason: AI may surface a possible flag, but a named human must decide whether and how to escalate.
- Risk if automated: Unaccountable triage, missed urgency, inappropriate disclosure, or unauthorized handling of sensitive information.

## Human premium dimensions
- presence
- privacy judgment
- care navigation
- accountability
- relationship repair

## Approved AI roles
- Prepare routine reminder drafts from approved templates
- Identify missing routine intake fields for staff review
- Create a private prep checklist for the human staff member
- Flag possible escalation for human review without sending patient-facing decisions

## Protected human work
- Reassurance and emotional acknowledgment
- Clinical, privacy, or safety escalation decisions
- Promises about care, diagnosis, timing, cost, or outcomes
- Sensitive conversation repair after confusion or system failure

## Human checkpoints
- Approved scripts/templates before any patient-facing automation is used
- Named human fallback visible in every automated reminder or intake path
- Escalation flags routed to a human before patient-facing action
- Pilot review after 10 patient interactions or 30 days, whichever comes first
- Privacy/compliance owner reviews data handling before any live workflow change

## Boundary notes
- Review aid only; not medical, legal, compliance, employment, or financial advice.
- Do not use this example with real patient data in the repo or demo.
- Any live clinic workflow requires domain-owner, privacy/compliance, and human staff approval.
- The purpose is to remove machine-like burden while protecting trust-bearing human work.

## Boundary
This card does not decide policy, staffing, compliance, employment action, medical/legal/financial advice, or customer promises. It is a local review aid only. Domain owners approve actual workflow changes.

## Validation
valid
- No validation errors

