# Codex Task: Offline browser-local forms for Surviving Hypernovelty primitives

## Goal
Build a genuinely useful offline/browser-local forms layer for the Surviving Hypernovelty repo so the primitives are usable without hand-editing JSON or running CLI commands.

## Workdir
`/home/aware1/surviving-hypernovelty`

## Safety / authority boundaries
Local-only repo work is approved. Do not publish, push, deploy, contact anyone, run network commands, touch accounts, spend money, or use real private customer/student/client data. Do not create legal/compliance/security/academic-integrity claims. Use only synthetic examples already in the repo or new synthetic examples.

## Baseline
Before this task, both validators pass:

```text
python3 scripts/validate_repo.py --check
validation=ok
checked_files= 52
checked_commands= 18
schema_checks= 15
demo_index_check=ok
mode= check
```

## Desired outcome
A Windows/browser-openable local forms system that lets a reviewer open HTML pages, fill in fields for key primitives, preview rendered Markdown, copy/download the result, and understand the safety boundary.

## Scope: build in phases

### Phase 1 — shared offline form framework
Create a small reusable local framework under a sensible path, for example:

- `forms/shared/form_runtime.js`
- `forms/shared/form_styles.css`
- `forms/index.html`
- `scripts/build_form_index.py` or similar

Requirements:
- No network calls, CDNs, external fonts, analytics, or telemetry.
- Plain static HTML/CSS/JS only.
- Works from `file://`.
- Uses synthetic defaults from repo examples where practical.
- Provides: form fields, preview pane, copy Markdown button, download Markdown/JSON buttons, reset-to-example button.
- Visible boundary notice on every form: local review aid only; no legal/compliance/security/academic-integrity authority; no public/account/spend/outreach/deploy actions.

### Phase 2 — forms for June 18 primitives
Build offline forms for these five first:

1. Agent Identity & Scope Roster
2. AI Use Clarity Micro-Policy Card
3. Adaptation Debt Ledger
4. Visible Thinking Repair Ticket
5. Platformized News Diet Receipt

Each form should:
- Load or embed the synthetic example.
- Let reviewer edit the most important fields.
- Generate Markdown compatible with the existing rendered examples in spirit.
- Make the boundary prominent.
- Link to README/example/schema/rendered source files.

### Phase 3 — forms index and repo surfaces
Update:
- `START_HERE.html`
- `build/demo_index.html` generation if appropriate
- `README.md`
- `docs/roadmap.md` or `docs/library-backlog.md` only if needed

The reviewer should be able to find the forms from `START_HERE.html` and `build/demo_index.html`.

### Phase 4 — validation
Add validation coverage:
- Check required form files exist.
- Check forms/index.html exists and links to the five forms.
- Check no form/shared files contain `http://`, `https://`, analytics, CDN, or network-fetch patterns.
- Check boundary text appears in each form.
- Check `python3 scripts/validate_repo.py` passes.
- Check `python3 scripts/validate_repo.py --check` passes and remains read-only.

## Implementation guidance
Prefer simple, robust static files over a large framework. A generic JS helper that takes a form spec is good if it stays readable. If full dynamic form generation from JSON Schema is too big, make a practical field-spec layer for these five forms and document the limitation.

Avoid overbuilding. This is a local demo/review surface, not a production app.

## Acceptance criteria
- `forms/index.html` opens from `file://` and links to five forms.
- Each of the five forms has useful editable fields and produces a Markdown preview.
- README/START_HERE/demo index expose the forms.
- `python3 scripts/validate_repo.py` passes.
- `python3 scripts/validate_repo.py --check` passes without changing repo status.
- Final answer includes files changed, tests run, limitations, and suggested next pass.
