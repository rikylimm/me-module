# Validation status

**Release:** v24
**Status:** learning-path build complete; learner and external validation not complete.

## Learning path

- 30 core weeks, 22 useful-next weeks, 3 optional-depth weeks.
- 15-question diagnostic and catch-up modules.
- Six-stage guided project; synthetic teaching data, clearly labelled.
- The path has not been tested with learners. The pilot is still not run.

## Numeric audit

- 30 high-risk claims in `NUMERIC-AUDIT.csv`.
- 20 verified, 3 derived, 1 conditional, 3 pending, 3 unresolved.
- 9,593 numeric tokens inventoried in `NUMERIC-INVENTORY.csv`.
- The inventory is a review queue, not a completed audit.

## Accessibility

- Static checks pass on 66 HTML files.
- Lighthouse: landing **1.00**, tracker **1.00** after contrast fixes (`#0066CC` buttons; `#A1A1A6` dark secondary text).
- Axe-core before fixes: landing 0; tracker 1; week 1 5; statistics handbook 2.
- Axe-core after v24 fixes: 0 violations on landing, tracker, search, week 1 and statistics handbook.
- Numeric inventory triaged into 7,816 quantities, 1,560 references, 207 enumerators, 6 candidates, 4 years. Still requires review.
- Manual screen-reader and 200% zoom checks are still required.

## Pilot

- Protocol and form exist: `PILOT-PLAN.md`, `PILOT-FORM.csv`.
- **Not run.** No participant data collected.

## External review

- Packet and form exist: `EXTERNAL-REVIEW.md`, `REVIEW-FORM.csv`.
- **No reviewer has signed.** No names are invented.

## CI

- Local equivalent passes: 10 tests, 10 labs, 66 HTML files, 0 broken links, deterministic search, checksums.
- Workflow is at `ci/verify.yml`; it needs a token with the GitHub `workflow` scope to activate.

## What 10/10 still requires

1. Close the 9,593-row numeric inventory.
2. Run the 3–5 learner pilot and report n, not percentages alone.
3. Obtain two external sign-offs and respond to every condition.
4. Run axe and manual WCAG checks after the contrast fix.
5. Activate CI on GitHub and confirm green.
6. Ratify thresholds, rubrics and bench risk levels with the external examiner.

No self-awarded 10. The remaining work is evidence, not more prose.
