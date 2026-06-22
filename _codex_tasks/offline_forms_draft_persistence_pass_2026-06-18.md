# Codex task: Offline forms draft-persistence and browser QA pass

## Repo / scope
- Work in `/home/aware1/surviving-hypernovelty` only.
- Local-only static/offline forms. No network calls, no public pushes, no deploys, no account actions.
- Preserve the five existing form pages and schema/example/rendered docs.

## Context
Previous pass added JSON import/round-trip support for all five offline forms:
- Import JSON section
- Load JSON into Form button
- malformed JSON handling
- missing required field errors
- per-form required fields
- `fromJson` hooks

Baseline commands currently pass:
```bash
python3 scripts/validate_repo.py --check
python3 scripts/smoke_forms_static.py
```

## Goal for this pass
Make the offline forms safer and more useful for real manual review work by adding **local draft persistence** and corresponding static/browser checks.

## Required product behavior
1. Each form should automatically save field edits to `localStorage` using a per-form key (slug-based).
2. On open, if a saved draft exists for that form, the form should restore the saved draft instead of overwriting it with the synthetic example.
3. Provide visible user controls/status:
   - show when a local draft was restored or saved
   - add a button to clear the saved draft and reset to the synthetic example
   - existing `Reset to Example` should also clear draft state or make the draft behavior unambiguous
4. JSON import should save/mark the imported data as the current local draft after successful load.
5. Download Markdown/JSON and Copy Markdown should continue to work from current form values.
6. Must remain static/offline-browser compatible. No build server required.

## Testing / verification requirements
1. Extend or add static smoke coverage for:
   - localStorage draft key/runtime hooks present
   - clear/reset draft control present on every form page
   - import still present on every form page
2. If practical, add a lightweight browser smoke script or extend existing one to simulate:
   - edit a field
   - reload/reinitialize enough to prove saved draft can be restored
   - clear draft
   This can be Playwright if already present, or a dependency-free static/runtime probe if not.
3. Rerun:
```bash
python3 scripts/validate_repo.py --check
python3 scripts/smoke_forms_static.py
```
4. Update the Windows review packet if there is an existing script/path for it. Do not invent claims; if packet refresh is out of scope, report it as remaining work.

## Deliverable
- Implement the changes.
- Keep changes minimal and readable.
- Final message should summarize changed files and exact verification output.
