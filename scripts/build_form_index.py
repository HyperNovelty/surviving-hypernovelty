#!/usr/bin/env python3
"""Build the local browser form index."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "forms" / "index.html"

FORMS = [
    {
        "name": "Agent Identity & Scope Roster",
        "href": "agent-identity-scope-roster.html",
        "description": "Inventory local-only agents, owners, scopes, permissions, logs, expiry dates, and escalation triggers.",
    },
    {
        "name": "AI Use Clarity Micro-Policy Card",
        "href": "ai-use-clarity-micro-policy-card.html",
        "description": "Make one assignment or task-level AI-use boundary clear with allowed uses, disallowed uses, evidence, and review triggers.",
    },
    {
        "name": "Adaptation Debt Ledger",
        "href": "adaptation-debt-ledger.html",
        "description": "Name stale assumptions, symptoms, affected people, owners, cheap reviews, and top repair priorities.",
    },
    {
        "name": "Visible Thinking Repair Ticket",
        "href": "visible-thinking-repair-ticket.html",
        "description": "Give a low-conflict repair path when submitted work lacks visible learning evidence.",
    },
    {
        "name": "Platformized News Diet Receipt",
        "href": "platformized-news-diet-receipt.html",
        "description": "Track source chains across platforms, creators, AI summaries, direct sources, confidence, and missing context.",
    },
]

BOUNDARY = "Local review aid only; no legal/compliance/security/academic-integrity authority; no public/account/spend/outreach/deploy actions."


def render() -> str:
    cards = "\n".join(
        f"""      <article class="form-card">
        <h2><a href="{html.escape(form["href"])}">{html.escape(form["name"])}</a></h2>
        <p>{html.escape(form["description"])}</p>
      </article>"""
        for form in FORMS
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Surviving Hypernovelty Offline Forms</title>
  <link rel="stylesheet" href="shared/form_styles.css">
</head>
<body>
  <main>
    <div class="topbar">
      <div>
        <h1>Offline Browser Forms</h1>
        <p>Static, browser-local forms for turning synthetic primitive examples into editable Markdown and JSON without running commands.</p>
      </div>
      <p><a href="../START_HERE.html">Back to START_HERE</a></p>
    </div>

    <section class="boundary">
      <strong>Boundary:</strong> {html.escape(BOUNDARY)}
    </section>

    <section class="index-grid">
{cards}
    </section>
  </main>
</body>
</html>
"""


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(), encoding="utf-8")
    print(f"form_index={OUT.relative_to(ROOT).as_posix()}")
    print(f"forms_indexed={len(FORMS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
