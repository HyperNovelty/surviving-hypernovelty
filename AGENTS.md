# Agent Contributor Guide

This file is for AI and coding-agent contributors working in this repository.

## Local-First Boundary

Work only inside the repository unless a human maintainer explicitly asks
otherwise. Do not deploy, publish, tag releases, push branches, create GitHub
issues, change repository settings, call account services, or modify secrets.

## Data Boundary

Do not add private Hypernovelty material, customer/student data, credentials,
tokens, account exports, grant strategy, private paths, internal notes, or
machine-specific home paths. Use repo-relative paths and synthetic examples.

## Scope Boundary

The v0.1 primitive count is frozen at 30. Do not add a new standalone primitive
without maintainer triage. Route most ideas to one of:

- an example for an existing primitive
- a kit page
- an article or backlog note
- a parked item for later review

## Validation

Before handing work back, run:

```bash
python3 scripts/validate_repo.py --check
git diff --check
```

If you change CI behavior, generated indexes, forms, renderers, schemas, or
validation logic, run the closest local equivalent as well.

## Public Claims

Keep claims modest. These tools are local review aids. Do not claim adoption,
certification, compliance, search ranking, production readiness, institutional
approval, or legal, medical, financial, security, employment, or educational
authority.

## Safe Editing

Prefer small, reviewable changes. Preserve human approval gates for public
actions, accounts, money, medicine, law, schooling, customer data, deployments,
and other high-stakes contexts.
