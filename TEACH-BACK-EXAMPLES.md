# Teach-back examples

**Release:** v23
Six worked examples for the weekly protocol. Use them to calibrate your own answer, not to replace it.

## Example 1 — Week 1: cell as reactor

**Prompt:** Why is a cell a reactor, and which two numbers set the scale?

**3:** Compartments create transport problems; volume sets concentration, surface area sets exchange; gives 1 fL and 1.7 nM with assumptions.
**2:** Correct analogy, one number missing or units wrong.
**1:** “Cells are factories” with no quantities.
**Common failure:** treating the cell as well mixed without naming the compartment.

## Example 2 — Week 2: weak acid

**Prompt:** At pH 4.8, what fraction of lactic acid is undissociated?

**3:** 1/(1+10^(4.8−3.86)) ≈ 0.10; explains why the neutral form crosses and the anion does not.
**2:** Correct arithmetic, no membrane consequence.
**1:** Uses pH as the fraction, or ignores pKa.
**Common failure:** reporting 10% as “10 times more toxic” without a mechanism.

## Example 3 — Week 5: model discrimination

**Prompt:** Why is a Lineweaver-Burk fit biased, and what would you do instead?

**3:** Reciprocal transformation distorts errors, especially at low substrate; weighted nonlinear fit; shows bias numerically.
**2:** Says “nonlinear is better” without the error structure.
**1:** Reports only R².
**Common failure:** comparing models on the same data without an information criterion or held-out check.

## Example 4 — Week 8: ATP yield

**Prompt:** Compute ATP per glucose at 4.3 H+/ATP and state the convention.

**3:** 10 NADH × 1.86 + 2 FADH2 × 0.93 + 2 GTP ≈ 24.5; states P/O and H+/ATP.
**2:** Correct total, convention implicit.
**1:** Uses 38 without stating the older convention.
**Common failure:** mixing mitochondrial and bacterial proton costs.

## Example 5 — Week 18: Monod identifiability

**Prompt:** Why can one batch growth curve fail to identify µmax and Ks?

**3:** Both parameters trade off; substrate range may not sample saturation; design a chemostat or wide substrate series.
**2:** Names correlation but proposes no design.
**1:** Reports a fit with no interval.
**Common failure:** treating a low-R² fit as a biological result.

## Example 6 — Week 23: FBA

**Prompt:** What does an FBA shadow price mean, and what does it not mean?

**3:** Marginal change in objective per unit constraint; a model sensitivity, not a measured price or flux.
**2:** Correct definition, no caveat.
**1:** Calls it a real metabolite concentration.
**Common failure:** reporting an optimal flux as the cell’s actual flux.

## Scoring

Use the 0–3 exit-ticket scale in `MASTERY.md`. A score of 2 is a pass with one gap. A score of 3 requires a mechanism, a number and a boundary.
