# Policy Freshness Diff Card

A local-first card for comparing a policy, rule, or operating assumption against a new signal without overreacting to every headline.

Use it when an external or internal change may make a handbook rule, classroom AI policy, team workflow, or public guidance stale, but the right response is still a small human-reviewed diff rather than an immediate rewrite.

## What it captures

- policy or workflow being checked;
- current rule/assumption;
- change signal and evidence strength;
- freshness verdict;
- proposed interim language;
- affected people;
- decision owner and review date;
- do-not-change-yet boundary.

## Safety boundary

This is not legal, compliance, HR, academic-integrity, medical, security, or risk-management advice. It is a review worksheet. High-stakes policy changes still require the appropriate local policy owner, counsel, accessibility/security review, and affected-person review.

## Local render

```bash
python3 tools/policy-freshness-diff-card/render_card.py examples/institution/policy_freshness_diff_card_example.json
```

## Output

The renderer prints a Markdown diff card with a status, freshness flags, and review checklist that can be copied into a local policy review folder.
