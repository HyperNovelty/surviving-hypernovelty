# Assessment Evidence Packet Lite

A one-assignment/week proof-of-learning bundle for the AI era.

The goal is not to catch students using AI. The goal is to make learning evidence visible enough for a teacher, parent, mentor, or learner to review what was understood, what was assisted, what changed, and what still needs human attention.

## Use when

- A final answer is too weak to prove understanding.
- AI tools were allowed but need boundaries.
- A teacher wants lightweight evidence without surveillance.
- A parent/mentor wants to see whether the learner can explain the work.

## What the packet captures

- assignment and learning target;
- learner claim of understanding;
- attempt/process trace;
- allowed AI/help used;
- misconception or revision log;
- transfer check;
- human review notes;
- next learning action.

## Safety boundary

This is not an AI-detection tool, grading guarantee, legal/compliance artifact, or substitute for teacher judgment. It rejects detector-first false certainty and focuses on reviewable evidence.

## Local render

```bash
python3 tools/assessment-evidence-packet-lite/render_packet.py examples/education/assessment_evidence_packet_lite_example.json
```

## Output sections

The renderer prints a Markdown packet that can be copied into a learning dossier, teacher note, parent conference prep, or student reflection folder.
