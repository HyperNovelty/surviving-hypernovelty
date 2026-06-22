# Agent Identity & Scope Roster

A local-first roster for tracking every AI agent, automation, bot, workflow worker, or non-human identity that can read, write, trigger, expose, spend, publish, or route work.

Use this when the problem is no longer one agent permission card, but the growing inventory of agents and tool identities that need owners, expiry dates, logs, scopes, and review gates.

## Use

```bash
python3 render_roster.py ../../examples/team/agent_identity_scope_roster_example.json
```

From the repo root:

```bash
python3 tools/agent-identity-scope-roster/render_roster.py examples/team/agent_identity_scope_roster_example.json
```

## What to fill in

- Roster name, owner, purpose, data boundary, and review cadence.
- Each agent identity: owner, purpose, identity/auth surface, data classes, read/write scopes, allowed and blocked actions.
- Whether the agent has secrets access, public-action ability, or spend authority.
- Output destinations, connected tools, log location, expiry/review date, and approval state.
- Escalation triggers that require a fresh human review.

## Boundary

This is a visibility and review aid, not a security control, access-management system, compliance audit, legal opinion, or certification. Do not store secrets in the roster. Use local security, legal, HR, school, or governance review before connecting agents to sensitive data, credentials, money, public publishing, external messaging, production deployment, or high-stakes decisions.
