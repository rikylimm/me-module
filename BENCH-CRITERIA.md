# Bench criteria and risk screen

**Release:** v18
**Use:** 30 bench protocols in the tracker.

`BENCH-CRITERIA.csv` is a pre-run screen, not a legal risk assessment. Institutional biosafety, chemical-safety and waste rules supersede it. A protocol is **not ready** until the local supervisor signs the risk screen.

## Columns

- **risk_level** — low, medium or high, based on biological, chemical, pressure, aerosol and data risk.
- **hazards** — what can hurt a person, a sample or the dataset.
- **controls** — engineering and administrative controls required before starting.
- **acceptance_criteria** — what must be true to call the run valid.
- **failure_triage** — first checks when the run fails.
- **data_record** — the minimum metadata to save.

## Rules

1. No bench run without a named operator, date, protocol version and supervisor.
2. No result without a negative and a positive control where one exists.
3. No accepted run without the acceptance criteria met or a written deviation.
4. No sample without chain-of-custody and storage location.
5. No analysis without the raw data and the processing script.
6. Any contamination, injury, spill or near-miss stops the run and triggers the local incident process.

## Acceptance is binary

A run is **valid**, **valid with deviation**, or **invalid**. “Looks fine” is not a result. Record the deviation and the reason.

## Risk levels

- **Low** — standard wet-lab or pure data work; normal PPE and local rules.
- **Medium** — aerosol, pressure, viable organisms, toxic solvent, or a decision that can waste a long experiment.
- **High** — any protocol that the local biosafety committee classifies as high; do not run without explicit approval. This module does not assign high risk on its own.
