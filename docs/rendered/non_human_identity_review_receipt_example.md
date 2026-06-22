# Non-Human Identity Review Receipt: Quarterly review of grant, CRM, and website helper identities

**Status:** REVIEW ACTION REQUIRED  
**Review owner:** Operations director  
**Review date:** 2026-06-30  
**Review cadence:** Quarterly, plus any new public-action, spend, secrets, or sensitive-data scope

## Identity review summary
| Identity | Owner | Identity type | Purpose | Decision | Expiry/next review |
| --- | --- | --- | --- | --- | --- |
| Grant Drafting Agent | Development lead | LLM workspace bot using a shared service account | Draft first-pass grant narratives from approved program notes and public funder instructions. | renew_with_changes | 2026-09-30 |
| CRM Enrichment Bot | Partnerships manager | Automation connected to CRM export/import jobs | Suggest missing organization categories for partner records using local CSV exports. | escalate | 2026-07-31 |
| Website Update Agent | Communications lead | Local static-site helper with repository write access only | Prepare draft webpage copy updates and pull-request notes for human review. | renew | 2026-09-30 |

## Gates and current scope
| Identity | Public action gate | Spend gate | Secrets gate | Data touched | Current permissions |
| --- | --- | --- | --- | --- | --- |
| Grant Drafting Agent | not_allowed | none | not_allowed | Approved program descriptions, Public funder guidance, Non-sensitive budget category summaries | Read approved grant-prep folder, Write drafts to local review folder, No submission, email, or funder portal access |
| CRM Enrichment Bot | not_allowed | none | not_allowed | Partner organization names, Public website URLs, Relationship notes marked non-confidential | Read manually exported local CSV, Write suggested category CSV, No direct CRM writeback |
| Website Update Agent | human_approval_required | none | not_allowed | Published website copy, Approved event descriptions, Draft changelog notes | Read website repository, Write local branch drafts, No deploy, hosting, DNS, social posting, or newsletter access |

## Per-identity evidence
### Grant Drafting Agent

**Owner:** Development lead  
**Roster link:** examples/team/agent_identity_scope_roster_example.json#grant-drafting-agent  
**Decision:** renew_with_changes  
**Next expiry/review:** 2026-09-30

**Delta since last review**
- Added read access to the 2026 program outcomes summary
- Removed access to unrestricted staff notes folder

**Permission evidence**
- Workspace permission screenshot stored in local governance folder
- Folder ACL export reviewed by operations director

**Log evidence**
- Weekly usage log reviewed for unusual file access
- No public submissions or outgoing messages found

**Unresolved gaps**
- Need clearer label on budget summaries that are safe for drafting

**Required next action:** Development lead will add approved-for-agent labels before the next proposal cycle.

**Notes:** Human reviewer remains responsible for factual checks, tone, eligibility, and final submission.

### CRM Enrichment Bot

**Owner:** Partnerships manager  
**Roster link:** examples/team/agent_identity_scope_roster_example.json#crm-enrichment-bot  
**Decision:** escalate  
**Next expiry/review:** 2026-07-31

**Delta since last review**
- Pilot expanded from 50 records to 300 records
- Direct CRM API writeback requested but not granted

**Permission evidence**
- Automation config export shows no API token stored
- Import step requires human upload by partnerships manager

**Log evidence**
- Run logs stored in local operations folder
- Sample of 25 suggestions checked before upload

**Unresolved gaps**
- Scale increase changes review burden
- No written rule for which relationship notes are safe to include

**Required next action:** Pause expansion beyond 300 records until safe-export rules and sample-review size are approved.

**Notes:** This receipt does not approve direct CRM write access.

### Website Update Agent

**Owner:** Communications lead  
**Roster link:** examples/team/agent_identity_scope_roster_example.json#website-update-agent  
**Decision:** renew  
**Next expiry/review:** 2026-09-30

**Delta since last review**
- Added draft changelog generation
- Deploy credentials confirmed absent from local environment

**Permission evidence**
- Repository remote is read/write only for local draft branch workflow
- No deploy token present in local config review

**Log evidence**
- Git history reviewed for generated commits
- No direct production deployment recorded

**Unresolved gaps**
- None recorded

**Required next action:** Communications lead will keep deploy and publication actions outside the agent account.

**Notes:** Public website changes remain human-approved and manually deployed.

## Cross-roster questions
- Do any identities now have public-action, spend, secrets, or sensitive-data scope not shown in the main roster?
- Can every active identity be traced to a named business owner and log location?
- Which temporary pilots should expire instead of becoming background infrastructure?

## Receipt flags
- Grant Drafting Agent: review decision -> renew_with_changes
- Grant Drafting Agent: unresolved gaps present
- CRM Enrichment Bot: review decision -> escalate
- CRM Enrichment Bot: sensitive or governance-relevant data touched -> Relationship notes marked non-confidential
- CRM Enrichment Bot: unresolved gaps present
- Website Update Agent: public action gate -> human_approval_required

## Boundary note
Local review receipt only. Not a security certification, IAM system, compliance audit, legal opinion, or permission grant. Do not store secrets here; use authorized security/governance review for sensitive environments.

## Notes
Synthetic quarterly example for reviewing three non-human identities without touching real accounts.

