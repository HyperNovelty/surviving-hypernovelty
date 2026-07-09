# Roadmap

This roadmap starts from the `v0.1.0-public-candidate` state: 30 existing
primitives, five public-facing kits, synthetic examples, local-first tools, and
human approval for public or high-stakes actions.

## Current Direction

- Keep the v0.1 primitive count frozen.
- Package existing primitives into coherent kits.
- Improve validation, examples, browser-local forms, and release hygiene before
  adding new standalone tools.

## Near-Term Waves

1. Agent Delegation Safety Kit first
   - Tighten the kit page around delegation, permission, identity, exposure,
     review, and revocation.
   - Add small synthetic examples that show handoffs without adding new primitives.
   - Keep security claims modest: visibility and review aid, not certification.

2. Browser-local forms expansion
   - Add offline forms for the most useful kit workflows.
   - Preserve file-local behavior with no network calls, accounts, telemetry, or deployment.
   - Keep import/export round trips covered by validation.

3. Examples and rendered demos
   - Add synthetic examples where they clarify an existing primitive or kit.
   - Prefer domain examples over new schemas unless the new primitive rule is met.
   - Keep generated rendered files fresh and reproducible.

4. Validation hardening
   - Expand read-only checks for generated indexes, rendered examples, schemas,
     and browser-local boundaries.
   - Keep checks standard-library-first and easy to run locally.
   - Avoid mutating generated files in CI check mode.

5. Docs and release hygiene
   - Keep README, kit index, changelog, governance, roadmap, security, and
     contributing docs aligned.
   - Use release checklists before tags.
   - Avoid raw git logs as release notes.

## Out of Scope for v0.1

- New standalone primitive #31 without explicit maintainer triage.
- Hosted services, telemetry, account integrations, deployments, or paid workflows.
- Claims of adoption, certification, compliance, medical/legal/financial advice,
  or production readiness.
