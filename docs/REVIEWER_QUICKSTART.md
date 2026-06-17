# Reviewer Quickstart

This is a 5-minute local path for reviewing the starter kit with synthetic
examples only. It does not publish, connect accounts, use private data, or call
external services.

## 1. Validate the Repository

Run from the repository root:

```bash
python3 scripts/validate_repo.py
```

The validator checks required files, runs the local tools against synthetic
examples, and performs lightweight schema checks.

## 2. Try a Few Tools

Novelty load calculator:

```bash
python3 tools/novelty-load-calculator/novelty_load.py examples/individual/novelty_load_example.json
```

Change triage worksheet:

```bash
python3 tools/change-triage/change_triage.py examples/individual/change_triage_example.json
```

Agent permission receipt:

```bash
python3 tools/agent-permission-receipt-card/render_receipt.py examples/team/agent_permission_receipt_example.json
```

## 3. Review the Boundary

Read `docs/PUBLICATION_BOUNDARY.md` before treating the repo as public-facing.
The safe public surface is the local starter kit, synthetic examples, schemas,
and general docs. Private sources, transcripts, grant strategy, customer data,
and internal paths stay out.
