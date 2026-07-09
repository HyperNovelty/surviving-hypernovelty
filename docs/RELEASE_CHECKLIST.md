# Release Checklist

Use this before a tagged release or public announcement. It is a maintainer
review aid, not an automated certification.

## Scope

- [ ] Release notes summarize user-facing changes and do not rely on raw git logs.
- [ ] Changelog has an entry for the candidate release.
- [ ] Primitive count and kit packaging are intentional and documented.
- [ ] No untriaged new standalone primitive is included.

## Safety and Public Claims

- [ ] No private Hypernovelty material, customer/student data, credentials, tokens, account exports, private paths, grant strategy, or internal notes are included.
- [ ] Examples are synthetic or public-safe.
- [ ] README, SECURITY, CONTRIBUTING, GOVERNANCE, ROADMAP, and kit docs keep claims modest.
- [ ] No certification, adoption, compliance, medical/legal/financial advice, production readiness, or institutional approval is implied.
- [ ] Human approval gates remain clear for public, account, money, legal, medical, schooling, customer data, deployment, and other high-stakes actions.

## Validation

- [ ] `python3 scripts/validate_repo.py --check`
- [ ] `git diff --check`
- [ ] CI workflow passes on the target branch.
- [ ] Generated indexes and rendered examples are fresh.

## Release Action

- [ ] Maintainer reviewed the exact diff being tagged.
- [ ] Tag name and changelog entry match.
- [ ] Announcement text, if any, is separately reviewed before posting.
