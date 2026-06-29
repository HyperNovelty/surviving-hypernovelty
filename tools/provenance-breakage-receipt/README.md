# Provenance Breakage Receipt

A local-first receipt for tracking when a provenance or content-credential signal survives, changes, disappears, or becomes unverifiable as media moves through normal sharing routes.

Use it for synthetic or manually reviewed examples such as an original signed image moving through a CMS resize, social repost, screenshot, slide deck, or AI summary. The goal is provenance humility: record what the chain-of-custody signal can and cannot support before anyone treats a label, credential, screenshot, or missing metadata as proof.

## Use when

- A media item or document has a credential, watermark, label, metadata trail, source-chain note, or claimed origin.
- A file has been resized, exported, screenshotted, reposted, summarized, or copied into another platform.
- A newsroom, classroom, creator, or civic group needs a calm record of where trust signals survived or broke.

## Local command

```bash
python3 tools/provenance-breakage-receipt/render_receipt.py examples/media/provenance_breakage_receipt_example.json
```

## Boundary

This is not a fact check, forensic analysis, authenticity certification, C2PA validator, legal/compliance review, or claim that a piece of media is true or false. Valid credentials do not prove context or truth. Missing credentials do not prove fakery. Use primary sources, domain expertise, and human editorial/educational review before consequential action.
