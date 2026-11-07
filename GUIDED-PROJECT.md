# Guided project — from cassava to a defensible flux claim

**Release:** v23
**Use after:** Week 8. Finish by Week 29.
**Data:** synthetic teaching data in `project/data/teaching_fermentation.csv`. Not the Fercaf thesis.

One question: *what can a carbon balance, a toy constraint model, a designed experiment and isotope labelling each establish about a cassava fermentation — and what can they not?*

## Stage 1 — Carbon and electron balance

Use `project/data/teaching_fermentation.csv`. Build:

- a C-mol balance for glucose, biomass, ethanol, lactate and acetate;
- a degree-of-reduction balance;
- a closure table with the missing stream named.

Deliverable: `project/report.md`, Stage 1, with units and a one-paragraph interpretation. Template: `project/templates/stage1_balance.py`.

## Stage 2 — Redox and pH hypothesis

The dataset contains pH and organic acids. State one metabolic explanation for the pH trajectory and one competing explanation. Name the measurement that would distinguish them. Do not infer intracellular flux from pH.

Deliverable: Stage 2 in `project/report.md`.

## Stage 3 — Toy constraint-based model

Build a five-reaction toy network for glucose uptake, biomass, ethanol, lactate and CO2. Use `practice/labs/lab05_fba.py` or write the LP. Report:

- the predicted maximum ethanol yield;
- one gene/reaction deletion;
- one alternative optimum or loop;
- the assumptions the toy makes.

Deliverable: Stage 3 plus a model file and the command to run it.

## Stage 4 — Design the experiment

Choose one question the toy cannot answer. Design a two-factor experiment with replication, randomisation and a power calculation. State the effect size you would pay for and why.

Deliverable: Stage 4 with a sampling table and a blank data sheet.

## Stage 5 — Isotope evidence

Choose a 13C tracer that would resolve a flux split in your toy. Write the atom transitions, the MDVs you would measure, and the precision you need. State what the labelling still cannot resolve.

Deliverable: Stage 5 with an atom map and an evidence table.

## Stage 6 — Interpretation and defence

Write one page:

1. the claim you can defend;
2. the strongest alternative;
3. the measurement that would change your mind;
4. what the toy and the dataset leave out;
5. the next experiment.

Deliverable: `project/report.md` complete, plus a 10-minute defence.

## Rubric

Use `project/RUBRIC.md`. Pass requires all six stages and no unsupported central claim. A score of 4 requires external review.

## What the project does not do

- It does not reproduce the Fercaf thesis.
- It does not estimate intracellular fluxes from pH or counts.
- It does not make the toy model predictive of the real process.
- It does not replace the 13C-MFA or FBA weeks.
