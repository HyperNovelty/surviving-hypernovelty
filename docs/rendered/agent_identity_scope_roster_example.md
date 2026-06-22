# Agent Identity & Scope Roster: Small nonprofit local AI helper roster

**Status:** REVIEW REQUIRED  
**Roster owner:** Operations director  
**Purpose:** Inventory draft-only AI helpers before deciding whether any should receive broader access, external outputs, or recurring automation.  
**Data boundary:** Synthetic or approved internal planning notes only. No donor records, payroll, credentials, student/client files, health data, or private legal/financial records.  
**Review cadence:** Monthly, and before adding any connector, credential, external output, or production workflow.

## Identity scope table
| Agent | Owner | Purpose | Identity type | Auth surface | Data classes | Read scopes | Write scopes | Approval state | Expiry/review date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Meeting Notes Summarizer | Program coordinator | Summarize approved staff meeting notes into internal action drafts. | Local script run by coordinator | Coordinator laptop; no separate service account | internal meeting notes, project task notes | approved notes folder | local draft summaries folder | approved_local_only | 2026-07-31 |
| Grant Evidence Packet Drafter | Executive director | Draft local-only grant evidence packet sections from approved public project artifacts and internal metrics. | Draft-only assistant account | Manually pasted approved source snippets; no live account connectors | public project descriptions, aggregated program metrics, private funding strategy notes | approved public artifacts, manual excerpts only | draft-only application packet folder | review_required | 2026-07-15 |
| Website Draft QA Checker | Communications lead | Run local QA over staged website draft pages before a human decides whether to deploy. | Local CLI checker | No account login; local static files only | staged public website drafts, source links, QA notes | staged site folder | local QA report folder | approved_local_only | 2026-07-31 |

## Permissions and controls
| Agent | Secrets access | Public action | Spend authority | Allowed actions | Blocked actions | Log location |
| --- | --- | --- | --- | --- | --- | --- |
| Meeting Notes Summarizer | not_allowed | not_allowed | none | summarize, extract_open_questions | email_external, publish, delete_source_notes, access_secrets | project-folder/logs/meeting-summary-runs.md |
| Grant Evidence Packet Drafter | not_allowed | review_required | none | draft_text, flag_missing_evidence, create_review_checklist | submit_form, email_external, invent_metrics, store_credentials, make_legal_claims | funding-packets/logs/draft-runs.md |
| Website Draft QA Checker | not_allowed | not_allowed | none | check_links, flag_boundary_language, generate_report | deploy_production, change_dns, post_social, email_subscribers | site-qa/logs/local-checks.md |

## Escalation triggers
- Adding credentials, API keys, browser login, or service-account auth
- Allowing external messages, public publishing, form submission, production deploy, DNS/account changes, or spend
- Introducing customer, student, patient, donor, payroll, legal, financial, health, or other sensitive data
- Changing any local-only agent to a recurring or unattended workflow
- Missing logs, unexpected output destination, failed handoff, or unclear owner

## Roster flags
- Grant Evidence Packet Drafter: public action -> review_required
- Grant Evidence Packet Drafter: sensitive data class -> private funding strategy notes
- Grant Evidence Packet Drafter: approval state -> review_required

## Boundary note
Visibility and review aid only. Do not store secrets in this roster. Local development is allowed; public actions, outreach, submissions, spend, real private data, and legal/compliance claims need separate human approval.

## Notes
Fictional example for local practice. It supports internal preparation for grant/partner review by showing governance discipline without claiming certification.
