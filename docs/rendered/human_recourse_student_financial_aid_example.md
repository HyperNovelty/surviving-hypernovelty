# Human Recourse Path Card: Student financial-aid chatbot recourse path

**Status:** HUMAN RECOURSE REQUIRED — OWNER REVIEW BEFORE LIVE USE  
**Service context:** A college financial-aid chatbot explains deadlines, document status, and next steps for students. It must not decide eligibility, denial, aid amount, dependency overrides, satisfactory academic progress appeals, or emergency support.  
**Review owner:** Financial aid operations lead with student-services review  
**Last reviewed:** 2026-06-25  
**Card state:** needs_owner_review  

## AI role
Answer routine questions from approved aid-office guidance, help students find forms, summarize missing-document checklists, and route complex or consequential cases to a named human team.

## The AI/tool does not decide
- Aid eligibility, award amount, denial, repayment, satisfactory academic progress status, dependency override, emergency grant, or disciplinary/student-record consequence.
- Whether a student should stop attending, drop a course, take debt, or ignore an official notice.

## Human-review triggers
### Trigger 1: The student says the answer would affect enrollment, housing, food, debt, eligibility, or ability to stay in school.
- Human owner: Financial aid counselor or student emergency support lead
- Why this leaves the AI path: The consequence is material and may require context, discretion, or emergency routing.
### Trigger 2: The chatbot gives conflicting deadlines, missing-document statuses, or denial reasons.
- Human owner: Financial aid operations lead
- Why this leaves the AI path: Records and policy interpretation must be reconciled before the student acts.
### Trigger 3: The student asks for appeal, exception, dependency override, disability-related accommodation, or hardship review.
- Human owner: Authorized aid-office reviewer with student-services support
- Why this leaves the AI path: The AI cannot grant exceptions or evaluate protected/sensitive circumstances.

## Visible recourse path
- Label shown to the person: Need a human review of this financial-aid answer?
- Contact route: Use the aid-office secure message form or visit the student-services desk; include the chatbot answer and date.
- Appeal/review step: A human counselor reviews the issue, identifies the governing policy/process, and tells the student the official appeal or correction path if one exists.
- Fallback if no response: If no response arrives by the stated window, contact the student-services escalation desk or the aid-office supervisor.
- Response-time expectation: Synthetic example: one business day for deadline/eligibility-impact issues; three business days for routine explanation questions. Real timelines require owner approval.

## Evidence to include
- Screenshot or copied text of the chatbot answer with date/time.
- Student ID or case/reference number if appropriate; do not include passwords or unnecessary private details.
- The official notice, form, or deadline that conflicts with the answer.
- What decision or deadline the student is worried about.

## Repair commitments
- Correct or withdraw misleading chatbot guidance after owner review.
- Route time-sensitive hardship or enrollment-impact cases to a human before a deadline when possible.
- Log recurring confusion as a policy/content update candidate.

## Boundary notes
- Review aid only; not legal, financial, counseling, academic, or institutional policy advice.
- Do not store real student records, aid documents, or private hardship details in this repo example.
- Actual appeal rights, response times, and authority must be approved by the institution.

## Boundary
This card does not create a legal appeals process, rights guarantee, medical/financial/employment/schooling decision, compliance assurance, or promise of outcome. It is a local review aid for making the human path visible. Domain owners approve real timelines, escalation language, and authority.

## Validation
valid
- No validation errors

