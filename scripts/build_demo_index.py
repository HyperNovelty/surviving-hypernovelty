#!/usr/bin/env python3
"""Build a local HTML demo index from existing synthetic examples."""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
OUT = ROOT / "build" / "demo_index.html"

TOOL_DEMOS = [
    {
        "name": "Novelty Load Calculator",
        "tool": "tools/novelty-load-calculator/novelty_load.py",
        "example": "examples/individual/novelty_load_example.json",
        "description": "Estimates how much simultaneous change a person or team is carrying.",
    },
    {
        "name": "Change Triage Worksheet",
        "tool": "tools/change-triage/change_triage.py",
        "example": "examples/individual/change_triage_example.json",
        "description": "Sorts changes into act, monitor, delegate, ignore, or learn-later buckets.",
    },
    {
        "name": "AI Delegation Contract Card",
        "tool": "tools/ai-delegation-contract-card/render_contract.py",
        "example": "examples/creator/ai_delegation_contract_example.json",
        "description": "Turns a synthetic delegation boundary into a reviewable contract card.",
    },
    {
        "name": "Agent Permission Receipt Card",
        "tool": "tools/agent-permission-receipt-card/render_receipt.py",
        "example": "examples/team/agent_permission_receipt_example.json",
        "description": "Documents what an agent can read, write, expose, spend, publish, or trigger.",
    },
    {
        "name": "Agent Toolchain Exposure Map",
        "tool": "tools/agent-toolchain-exposure-map/render_map.py",
        "example": "examples/team/agent_toolchain_exposure_map_example.json",
        "description": "Maps agent/tool workflows across identities, data touched, outputs, and checkpoints.",
    },
    {
        "name": "Assessment Evidence Packet Lite",
        "tool": "tools/assessment-evidence-packet-lite/render_packet.py",
        "example": "examples/education/assessment_evidence_packet_lite_example.json",
        "description": "Renders a compact proof-of-learning packet from a synthetic education example.",
    },
    {
        "name": "Answer-Layer Citation Readiness Card",
        "tool": "tools/answer-layer-citation-readiness-card/render_card.py",
        "example": "examples/publishing/answer_layer_citation_readiness_example.json",
        "description": "Reviews page-level claim/source/date/update readiness for answer-layer citation hygiene.",
    },
    {
        "name": "Human Premium Trust Surface Card",
        "tool": "tools/human-premium-trust-surface-card/render_card.py",
        "example": "examples/team/human_premium_trust_surface_example.json",
        "description": "Identifies what AI should remove, support, protect, or leave human in trust-sensitive work.",
    },
    {
        "name": "Policy Freshness Diff Card",
        "tool": "tools/policy-freshness-diff-card/render_card.py",
        "example": "examples/institution/policy_freshness_diff_card_example.json",
        "description": "Compares a policy or rule against a new signal and proposes a bounded owner-reviewed diff.",
    },
    {
        "name": "Source Confidence Ledger",
        "tool": "tools/source-confidence-ledger/source_ledger.py",
        "example": "examples/publishing/source_confidence_example.json",
        "description": "Tracks claims, source confidence, verification status, and downstream use.",
    },
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {"items": data}


def one_line(value: Any, limit: int = 150) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def summarize_json(data: dict[str, Any]) -> str:
    for key in (
        "subject",
        "purpose",
        "ledger",
        "agent_name",
        "workflow_name",
        "page_title",
        "service_context",
        "assignment_title",
        "scenario",
        "title",
    ):
        if data.get(key):
            return one_line(data[key])
    for key in ("changes", "claims", "agents", "surface_steps", "claim_list"):
        value = data.get(key)
        if isinstance(value, list):
            return f"{len(value)} {key.replace('_', ' ')}"
    return "Synthetic example fixture."


def example_summaries() -> dict[str, str]:
    summaries: dict[str, str] = {}
    for path in sorted(EXAMPLES.rglob("*")):
        if path.suffix.lower() == ".json":
            summaries[rel(path)] = summarize_json(load_json(path))
        elif path.suffix.lower() in {".md", ".markdown"}:
            text = path.read_text(encoding="utf-8").strip().splitlines()
            summaries[rel(path)] = one_line(next((line.strip("# ").strip() for line in text if line.strip()), "Markdown example"))
    return summaries


def render() -> str:
    summaries = example_summaries()
    cards: list[str] = []
    for demo in TOOL_DEMOS:
        example = demo["example"]
        tool = demo["tool"]
        command = f"python3 {tool} {example}"
        cards.append(
            f"""
      <section class="card">
        <h2>{html.escape(demo["name"])}</h2>
        <p>{html.escape(demo["description"])}</p>
        <p><b>Example:</b> <a href="../{html.escape(example)}">{html.escape(example)}</a></p>
        <p><b>Example summary:</b> {html.escape(summaries.get(example, "Synthetic example fixture."))}</p>
        <p><b>Tool:</b> <a href="../{html.escape(tool)}">{html.escape(tool)}</a></p>
        <pre>{html.escape(command)}</pre>
      </section>"""
        )

    all_examples = "\n".join(
        f'          <li><a href="../{html.escape(path)}">{html.escape(path)}</a> - {html.escape(summary)}</li>'
        for path, summary in summaries.items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Surviving Hypernovelty Demo Index</title>
  <style>
    body {{ margin: 0; padding: 40px; font: 16px/1.55 system-ui, Segoe UI, Arial, sans-serif; background: #f7f5ef; color: #20242a; }}
    main {{ max-width: 1040px; margin: auto; }}
    h1 {{ margin-bottom: 0; }}
    a {{ color: #235789; }}
    .boundary {{ border-left: 4px solid #9b5de5; padding: 12px 16px; background: #fff; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }}
    .card {{ background: #fff; border: 1px solid #d9d4c7; border-radius: 8px; padding: 18px; }}
    pre {{ white-space: pre-wrap; background: #20242a; color: #f7f5ef; padding: 10px; border-radius: 6px; }}
  </style>
</head>
<body>
  <main>
    <h1>Surviving Hypernovelty Demo Index</h1>
    <p>Local starter-kit demos generated from existing synthetic examples.</p>
    <section class="boundary">
      <b>Boundary:</b> review aid only. No private sources, customer data, account actions, network calls, funding claims, or adoption claims are included in this demo index.
    </section>
    <h2>Starter Tool Demos</h2>
    <div class="grid">
      {''.join(cards)}
    </div>
    <h2>All Example Files Read</h2>
    <ul>
{all_examples}
    </ul>
  </main>
</body>
</html>
"""


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(), encoding="utf-8")
    print(f"demo_index={rel(OUT)}")
    print(f"examples_indexed={len(example_summaries())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
