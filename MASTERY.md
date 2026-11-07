# Mastery gates and calibration

**Release:** v17
**Rule:** advance on evidence, not on calendar time.

## Weekly loop

1. Read the week's outcome in `OUTCOMES.csv`.
2. Do the exit ticket closed-book. Score 0–3:
   - 3 = accurate, complete, transferable.
   - 2 = correct core, one gap.
   - 1 = partial or recognition-only.
   - 0 = cannot attempt.
3. Record confidence 1–5 in `CALIBRATION-TEMPLATE.csv`.
4. If score <2, reread the specific section, redo the exit ticket, and retest after 24 hours.
5. If confidence − score ≥2, log the error and retest after 7 days.

## Gate criteria

| Gate | Week | Paper | Total | Section floor | Exit tickets | Portfolio |
|---|---:|---|---:|---:|---|---|
| G1 | 7 | Paper 1 | ≥70% | ≥60% each | ≥80% at ≥2 | Repository scaffold |
| G2 | 18 | Paper 2 | ≥70% | ≥60% each | ≥80% at ≥2 | Reviews 1 artifacts |
| G3 | 26 | Paper 3 | ≥70% | ≥60% each | ≥80% at ≥2 | Strain design |
| G4 | 31 | Paper 4 | ≥70% | ≥60% each | ≥80% at ≥2 | 13C and MCA |
| G5 | 39 | Paper 5 | ≥70% | ≥60% each | ≥80% at ≥2 | Toolbox artifacts |
| G6 | 55 | Paper 6 | ≥70% | ≥60% each | ≥80% at ≥2 | Capstone dossier |

These thresholds are **course design decisions**, not an external standard. An external examiner must ratify them before the module claims validation.

## If a gate is failed

- **Total below 70%:** do not advance. Revisit the weakest section, redo the relevant exit tickets, and retake an equivalent paper after 7 days.
- **One section below 60%:** targeted remediation in that section only; retake that section or an equivalent.
- **Exit tickets below 80%:** repeat the weak weeks before the paper.
- **Portfolio below 3:** revise the artifact and re-review; do not substitute prose for evidence.
- **Two consecutive failures:** reduce load, review the error log with a supervisor, and rebuild the prerequisite week before another attempt.

See `EXAM-BLUEPRINTS.csv` for the per-paper remediation map.

## Calibration review

At each gate, compute:

- mean confidence;
- mean exit score;
- calibration gap (confidence − score);
- percentage of errors that were overconfident.

A positive gap above 1.0 means the learner is recognising, not recalling. Add retrieval practice and reduce reading volume. A negative gap below −1.0 means underconfidence; do not add more content.

## Portfolio reviews

- Week 18: repository, enzyme dossier, kinetics, allostery, and the first balance artifacts.
- Week 31: pathway atlas, yields, reconciliation, FBA, deletion, design, metabolomics, 13C, MCA.
- Week 46: toolbox, omics, host/product matrix.
- Week 55: capstone dossier, proposal, external artefact.

Use `PORTFOLIO-RUBRICS.csv`. A score of 4 requires external review.

## What this does not yet prove

These gates are designed, not validated. The module still needs:

- external examiner ratification of thresholds;
- a pilot with 3–5 learners;
- a full numeric audit of all 55 weeks;
- runnable notebooks and CI checks.
