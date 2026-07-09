# OSS Legitimacy Research Run — 2026-07-09

## Scope

Repository reviewed: `HyperNovelty/surviving-hypernovelty`.

Goal: identify small, reviewable repository-health improvements that increase public GitHub legitimacy without adding new primitives, exposing private material, or making inflated claims.

## Baseline checks

Before the Codex implementation wave:

- Local repo and `origin/main` were even: `0 0`.
- Codex CLI was available and logged in.
- README listed 30 primitives.
- Existing v0.1 strategy froze the primitive count and grouped primitives into five public-facing kits.
- Present files: `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.gitignore`, `.github/workflows/validate.yml`, issue templates.
- Missing files identified by the audit: `.github/pull_request_template.md`, `CHANGELOG.md`, `GOVERNANCE.md`, root `ROADMAP.md`, root `AGENTS.md`, and a maintainer release checklist.

## External guidance consulted

- GitHub repository best-practices guidance: README, license, citation/contribution guidance, code of conduct, security policy, branch protection, Dependabot/secret/code scanning where appropriate.
- OpenSSF-style project health guidance: public source repository, documented test suite, CI, contribution process, code of conduct, vulnerability reporting, release notes that are not raw git logs.
- OSPO-style public repository guidance: README purpose/usage/engagement, contribution instructions, issue reporting, release/version expectations, and clear maintainer contact/process.

## Implementation plan given to Codex

Codex was tasked to implement a first legitimacy wave, with these priorities:

1. Add a PR template with validation and public-boundary checkboxes.
2. Add a changelog with an `Unreleased` section and a `v0.1.0-public-candidate` candidate-state entry.
3. Add governance rules covering maintainer decisions, high-stakes human gates, and new-primitive routing.
4. Add a root roadmap for the next few improvement waves.
5. Add an AI/coding-agent contributor guide.
6. Update CI to run the repo's actual read-only validator.
7. Add a release checklist.
8. Link the new docs from README/START_HERE without bloating either file.

## Boundaries

- No new primitives.
- No new runtime dependencies.
- No private Hypernovelty material, private paths, customer/student data, secrets, credentials, account exports, grant strategy, or internal notes.
- No deploys, releases, GitHub settings changes, issue creation, or Codex-side push.
- Keep public claims modest: local-first review aids, not certification, adoption, compliance, or production readiness.

## Validation requested

- `python3 scripts/validate_repo.py --check`
- `git diff --check`
- CI-equivalent checks for any changed workflow behavior.
