# Agent Toolchain Exposure Map

A local-first worksheet and renderer for seeing what a multi-agent or multi-tool workflow can read, write, trigger, expose, or hand off.

Use this when one agent permission receipt is not enough: the risk may sit in the chain between agents, tools, data stores, output destinations, and human checkpoints.

## Use

```bash
python3 render_map.py ../../examples/team/agent_toolchain_exposure_map_example.json
```

From the repo root:

```bash
python3 tools/agent-toolchain-exposure-map/render_map.py examples/team/agent_toolchain_exposure_map_example.json
```

## What to fill in

- Workflow name, owner, purpose, and review cadence.
- Each agent/tool identity, owner, connected tools, data touched, actions, outputs, and checkpoint.
- Handoffs between agents/tools, including payload, trigger, and human checkpoint.
- Shared boundaries: secrets, public actions, audit evidence, rollback owner.
- Review triggers that force a fresh map before expansion.

## Boundary

This is a visibility and review aid, not a security certification, compliance audit, or guarantee that a toolchain is safe. Use local security, legal, HR, school, or governance review before connecting agents to sensitive data, credentials, money, public publishing, external messaging, production deployment, or high-stakes decisions.
