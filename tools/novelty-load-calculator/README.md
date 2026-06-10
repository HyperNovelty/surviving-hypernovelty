# Novelty Load Calculator

Estimate how much simultaneous change a person, family, team, or institution is carrying.

## Use

```bash
python3 novelty_load.py ../../examples/individual/novelty_load_example.json
```

Input fields:

- `subject`: who/what is being assessed
- `changes`: list of changes with `domain`, `description`, `impact`, `urgency`, `uncertainty`, `agency`

Scores use 1–5 scales. Higher impact, urgency, uncertainty, and lower agency increase load.
