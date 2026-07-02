# Agent Revocation Reality Check: CRM research assistant pause/revoke preflight

**Status:** REVOCATION PATH NEEDS WORK  
**Review owner:** Operations director  
**Review date:** 2026-07-02  
**Agent identity:** CRM Research Assistant  
**Roster link:** examples/team/agent_identity_scope_roster_example.json#crm-research-assistant

## Scenario
Synthetic pre-deployment review for an assistant that drafts partner-research notes from approved CRM exports and public web pages, with no direct CRM writeback or public outreach authority.

## Connected systems and revocation methods
| System | Access type | Revocation method | Owner | Verified status | Notes |
| --- | --- | --- | --- | --- | --- |
| Local CRM export folder | Read approved redacted CSV exports only | Remove folder ACL entry and rotate the export folder path | Operations analyst | partly_verified | ACL removal was tested; path rotation has not been included in the drill yet. |
| Research notes workspace | Write draft Markdown notes to a local review folder | Disable workspace service account and archive pending draft folder read-only | Knowledge manager | verified | No customer-facing publishing or email connector is attached. |
| Scheduled weekly batch runner | Runs a local enrichment job every Monday morning during the pilot | Disable scheduled job and preserve last run log | IT support lead | not_verified | The pause button in the project board does not stop the scheduler by itself. |

## Permissions to revoke
- Read access to the approved CRM export folder
- Write access to the draft research notes workspace
- Scheduled weekly batch-run permission
- Any cached local copy of the previous export after the review window

## Pause trigger and owner
**Pause owner:** Operations director  
**Pause trigger:** Any unexpected sensitive field in the export, unreviewed writeback request, unexplained run log, or partner complaint about generated notes.

## Revocation steps
| # | Step | Owner | Status | Evidence to check/preserve |
| --- | --- | --- | --- | --- |
| 1 | Freeze new runs and disable the scheduled job before reviewing drafts | IT support lead | needs_work | Scheduler screenshot or local job config export showing disabled state; no secrets copied into this card |
| 2 | Remove read access to the CRM export folder and move the current export to an archive path | Operations analyst | ready | Folder ACL export and archive manifest stored in the internal governance folder |
| 3 | Preserve generated draft notes, run logs, and review comments before deleting working cache | Knowledge manager | ready | Archive checklist with filenames and timestamps, excluding credentials or private tokens |
| 4 | Notify the human review queue that AI-generated partner notes are paused and must not be imported | Partnerships manager | ready | Local queue note and meeting decision record |

## Dependent workflows affected
- Partnerships team will lose weekly draft categorization notes while paused
- Quarterly partner cleanup metric may slip by one week
- Human reviewers need a fallback spreadsheet template for urgent partner updates

## Evidence to preserve
- Last successful run log
- Draft notes awaiting human review
- Export schema used for the run
- Human review comments that explain why the pause was triggered

## Restart criteria
- Scheduler disable/enable path tested by IT support lead
- Export schema excludes sensitive relationship notes by default
- Partnerships manager signs off on fallback review queue
- One dry-run produces no direct CRM writeback and no public outreach

## Open gaps
- Project-board pause status does not disable the scheduler
- No written maximum age for cached export files
- Fallback spreadsheet template exists but is not linked in the pause procedure

## Decision
**Decision:** test_before_deploy  
**Required next action:** Run a local revocation drill that disables the scheduler and preserves evidence before expanding the pilot beyond synthetic data.

## Reality-check flags
- Local CRM export folder: revocation status -> partly_verified
- Scheduled weekly batch runner: revocation status -> not_verified
- Scheduled weekly batch runner: high-impact access or control needs stronger verification
- Step needs work: Freeze new runs and disable the scheduled job before reviewing drafts -> needs_work
- Open gap: Project-board pause status does not disable the scheduler
- Open gap: No written maximum age for cached export files
- Open gap: Fallback spreadsheet template exists but is not linked in the pause procedure

## Boundary note
Local review aid only. Not an IAM system, security control, incident-response plan, compliance audit, legal opinion, vendor certification, or guarantee that revocation works. Do not store secrets, tokens, credentials, or sensitive logs here.

## Notes
Synthetic example; no real CRM, account, or scheduler was touched.

