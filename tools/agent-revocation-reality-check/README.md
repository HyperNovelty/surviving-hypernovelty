# Agent Revocation Reality Check

A local-first companion card for checking whether an agent pause/revoke control is real enough to rely on before a team delegates consequential work.

Use it after an Agent Identity & Scope Roster entry or Non-Human Identity Review Receipt flags an identity that may need a pause, revoke, or restart path. The goal is to avoid a paper "red button" by naming what is revoked, where, who owns the pause, what breaks downstream, what evidence must be preserved, and what criteria allow restart.

## Use when

- A non-human identity or agent is being deployed with read/write, public-action, spend, secrets, or operational workflow scope.
- A team claims it can pause or revoke an agent but has not tested which systems, tokens, queues, scheduled jobs, or handoffs are actually stopped.
- A review needs to separate policy intent from operational reality before broader rollout.

## Local command

```bash
python3 tools/agent-revocation-reality-check/render_check.py examples/team/agent_revocation_reality_check_example.json
```

## Boundary

This is not an IAM system, security control, incident-response plan, compliance audit, legal opinion, vendor certification, or guarantee that revocation works. It is a local review artifact for finding gaps and routing them to authorized owners. Do not store secrets, tokens, credentials, or sensitive logs in the card.
