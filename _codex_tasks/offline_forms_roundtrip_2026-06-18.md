# Codex Task: Offline forms JSON round-trip + schema-aligned field coverage

## Goal
Improve the offline/browser-local forms layer so each form can import/export useful JSON and cover the domain-specific schema fields more completely. Keep the implementation static, local, and review-demo friendly.

## Workdir
`/home/aware1/surviving-hypernovelty`

## Safety / authority boundaries
Local-only repo work is approved. Do not publish, push, deploy, contact anyone, run network commands, touch accounts, spend money, or use real private customer/student/client data. Do not create legal/compliance/security/academic-integrity claims. Use synthetic examples only.

## Baseline
Before this task:

```text
python3 scripts/validate_repo.py --check
validation=ok
checked_files= 61
checked_commands= 18
schema_checks= 15
forms_check=ok
demo_index_check=ok
mode= check
```

Existing forms:
- `forms/agent-identity-scope-roster.html`
- `forms/ai-use-clarity-micro-policy-card.html`
- `forms/adaptation-debt-ledger.html`
- `forms/visible-thinking-repair-ticket.html`
- `forms/platformized-news-diet-receipt.html`
- shared runtime/style under `forms/shared/`

## Desired outcome
A reviewer can:
1. Open any of the five forms from `file://`.
2. Edit fields.
3. Export JSON.
4. Paste/import that JSON back into the form.
5. See the form and Markdown preview restored accurately enough for practical round-tripping.
6. Start from the repo’s synthetic examples without losing important schema fields.

## Required improvements

### 1. Add JSON import/round-trip UX
Add to every form:
- An **Import JSON** textarea or modal/section.
- A **Load JSON into Form** button.
- A clear validation/error message area for malformed JSON or missing key fields.
- Existing **Download JSON** should produce JSON that can be pasted back into the same form.

If a perfect lossless round-trip is too large, preserve all schema-significant fields and document any intentionally omitted presentation-only fields.

### 2. Improve schema-aligned field coverage
For each of the five forms, compare against its current schema and example JSON. Add practical editable coverage for missing required or important fields.

Minimum expectations:
- Preserve/edit all required top-level fields.
- Preserve/edit key arrays/objects that define the primitive’s meaning.
- Keep simple row-based editors acceptable; no large framework needed.
- Avoid raw JSON-only as the sole editing experience, but raw import/export is welcome.

### 3. Keep everything static/local
- No network calls, CDNs, external fonts, analytics, telemetry, iframes, form posts, or account surfaces.
- Must work from `file://`.
- Keep boundary text prominent.

### 4. Validation and smoke checks
Update `scripts/validate_repo.py` to check:
- Each form exposes Import JSON / Load JSON into Form.
- Shared runtime has functions or hooks for JSON import and export.
- Blocked network patterns are still absent in forms/shared and form HTML files.
- Existing form checks still pass.

Add a small local static smoke script if helpful, e.g. `scripts/smoke_forms_static.py`, that checks HTML contains expected IDs/buttons/spec names without a browser.

### 5. Surfaces/docs
Update README / START_HERE / forms index only if needed to explain import/export round-trip. Keep copy concise.

## Acceptance criteria
- `python3 scripts/validate_repo.py` passes.
- `python3 scripts/validate_repo.py --check` passes and does not change repo status.
- Each form has visible Import JSON + Load JSON into Form controls.
- Downloaded JSON from each form is designed to be accepted by that form’s import path.
- No network patterns in `forms/`.
- Final answer includes files changed, tests run, limitations, and recommended next pass.
