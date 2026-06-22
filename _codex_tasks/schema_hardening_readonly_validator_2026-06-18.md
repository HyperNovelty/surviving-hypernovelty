# Codex Task: Schema hardening + read-only validator mode

## Goal
Harden the June 18 Surviving Hypernovelty queued-build primitives and make validation friendlier for read-only review.

## Workdir
`/home/aware1/surviving-hypernovelty`

## Scope
Implement local-only changes. Do not publish, push, deploy, contact anyone, run network commands, touch accounts, spend money, or use real private customer/student/client data.

## Target primitives
- AI Use Clarity Micro-Policy Card
- Adaptation Debt Ledger
- Visible Thinking Repair Ticket
- Platformized News Diet Receipt

## Required improvements
1. Replace/extend the four generic schemas so each has domain-specific required fields and enums, not only a generic `sections` array.
2. Update each example JSON to satisfy the stronger schema while preserving the current content and boundaries.
3. Update each renderer to use the stronger domain-specific fields directly. It is acceptable to keep renderers separate, but they should not be only identical generic section renderers.
4. Update `scripts/validate_repo.py` to validate the stronger fields/invariants for these four primitives.
5. Add a read-only validation mode to `scripts/validate_repo.py`, e.g. `--check`, that does not write generated artifacts. It should either skip rebuilds or compare generated demo-index content against `build/demo_index.html` in memory and fail if stale.
6. Preserve normal `python3 scripts/validate_repo.py` behavior unless there is a clear reason to improve it; normal mode may rebuild generated artifacts.
7. Update README/START_HERE/demo index builder/roadmap/backlog only if field/path/command changes require it.

## Acceptance criteria
- `python3 scripts/validate_repo.py` passes.
- `python3 scripts/validate_repo.py --check` passes and does not modify tracked or untracked files.
- The five June 18 tools remain exposed from README, START_HERE, and build/demo_index.html.
- Boundary language remains clear: local review aid only; no legal/compliance/security/academic-integrity authority; no public/account/spend/outreach/deploy actions.
- Final answer includes files changed, tests run, and any remaining limitations.

## Baseline before Codex
Current validator passes:

```text
validation=ok
checked_files= 52
checked_commands= 19
schema_checks= 11
demo_index_check=ok
```
