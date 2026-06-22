# Non-Human Identity Review Receipt

A local-first quarterly (or event-triggered) receipt for reviewing one or more non-human identities after they already appear in an Agent Identity & Scope Roster.

Use this when an agent, bot, service account, OAuth app, browser profile, or automation identity needs a concrete renewal/pause/revoke decision backed by permission evidence, log evidence, expiry date, owner, and unresolved gaps.

## Use

```bash
python3 render_receipt.py ../../examples/team/non_human_identity_review_receipt_example.json
```

From the repo root:

```bash
python3 tools/non-human-identity-review-receipt/render_receipt.py examples/team/non_human_identity_review_receipt_example.json
```

## What to fill in

- Receipt name, review owner, review date, and cadence.
- Each identity's owner, type, purpose, roster link, data touched, and current permissions.
- Delta since last review: new scopes, removed scopes, scale changes, new tools, or requested capabilities.
- Evidence: where permission state and logs were reviewed without storing secrets in the receipt.
- Gates for public action, spend, and secrets.
- Expiry/next review date, decision, unresolved gaps, and required next action.
- Cross-roster questions that catch drift across multiple identities.

## Decisions

- `renew` — continue as-is until the next review.
- `renew_with_changes` — continue only with the listed repairs or limits.
- `pause` — stop use until the listed blocker is fixed.
- `revoke` — remove the identity or its access.
- `escalate` — route to an authorized security, governance, legal, HR, school, or operational owner.

## Boundary

This is a visibility and review aid, not a security certification, IAM system, compliance audit, legal opinion, or permission grant. Do not store API keys, passwords, OAuth secrets, customer records, student records, patient records, or private data in the receipt. Use authorized review before connecting non-human identities to sensitive data, credentials, money, public publishing, external messaging, production deployment, or high-stakes decisions.
