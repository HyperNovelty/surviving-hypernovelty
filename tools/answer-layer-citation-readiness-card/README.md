# Answer-Layer Citation Readiness Card

A local, page-level evidence card for articles, essays, explainers, and institutional pages that may be summarized or cited by answer engines, search features, newsletters, or research assistants.

It builds on the Source Confidence Ledger by making the public-facing page easier to review: clear claims, source references, author/owner, dates, changed-since-publication notes, uncertainty notes, and update policy.

## Use

```bash
python3 render_card.py ../../examples/publishing/answer_layer_citation_readiness_example.json
python3 render_card.py ../../examples/publishing/publisher_page_receipt_example.json
```

## What it is for

- Check whether the main claims on a page have explicit evidence references.
- Separate citation hygiene from confidence or ranking promises.
- Give publishers and researchers a repeatable local review artifact before public use.
- Add a public-page survival receipt with canonical URL, audience, citation-friendly summary, answer-layer risks, human reader checks, “do not claim” boundaries, and review triggers.

## Example extension: Answer-Layer Survival Receipt

`examples/publishing/publisher_page_receipt_example.json` shows a fictional public FAQ receipt. It is designed for human review before publication and for local rendering only; it does not imply that answer engines will cite, summarize, or update from the receipt.

## Boundary

This does **not** guarantee AI citation, rankings, traffic, answer-engine visibility, or factual correctness. It is a review aid and evidence-hygiene checklist only.
