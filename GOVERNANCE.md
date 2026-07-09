# Governance

Surviving Hypernovelty is maintained as a small, local-first public-candidate
repository. Governance should keep the repo useful, modest in its claims, and
safe to review in public.

## Maintainer Decisions

Maintainers may merge small documentation, example, schema, validation, and tool
changes when they:

- preserve the local-first boundary
- use synthetic or public-safe examples only
- pass repository validation
- keep public claims modest
- do not create new high-stakes authority

When a change affects public positioning, primitive scope, security boundaries,
release readiness, or contribution expectations, maintainers should leave a
short rationale in the PR or commit message.

## Human Gate

Human maintainer approval is required before any action that would:

- publish, deploy, tag, announce, or market the project
- change repository settings, accounts, credentials, secrets, domains, or paid services
- use customer, student, medical, legal, financial, private Hypernovelty, or internal data
- authorize agents or tools to take public, account, payment, outreach, or high-stakes actions
- claim compliance, certification, adoption, institutional approval, production readiness, or professional advice

Repository tools and documents are review aids only. They do not replace human
judgment in legal, medical, financial, educational, security, employment, or
other consequential contexts.

## Issues and Pull Requests

Issues should describe a concrete documentation gap, validation failure,
example need, usability problem, or proposed local-first improvement.

Pull requests should be small enough to review, name their changed paths, and
include validation results. Maintainers may close or redirect PRs that add
private material, make inflated public claims, create unreviewed runtime
dependencies, bypass human gates, or expand scope without triage.

Security-sensitive reports should follow `SECURITY.md` and avoid posting
secrets or private records in public issues.

## New Primitive Rule

The v0.1 primitive count is frozen at 30. New ideas should use this routing rule:

- Same audience and same decision as an existing primitive: make an example.
- Same primitive in a different domain: add it to a kit or rendered example.
- New audience plus new decision: consider a future primitive after maintainer review.
- Useful but broad: make an article outline, backlog item, or kit note.
- High-liability or unclear: park it until the boundary and review model are stronger.

Maintainers should prefer kit packaging and examples over new standalone
schemas until the v0.1 public-candidate surface is stable.
