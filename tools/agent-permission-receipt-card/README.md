# Agent Permission Receipt Card

A plain-language receipt for what an AI agent/workflow can read, write, expose, spend, publish, or trigger.

This extends the AI Delegation Contract idea into a more infrastructure-aware record: identity, scopes, secrets boundary, audit log, rollback owner, and human approval point.

## Use

```bash
python3 render_receipt.py ../../examples/team/agent_permission_receipt_example.json
```

## Boundary

This is a review aid, not a security certification. It helps people ask better questions before connecting agents to tools, accounts, credentials, or public actions.
