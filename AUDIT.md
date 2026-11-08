# Course assurance — v26 Phase 9

This is the audit spine, not a claim that the module is already 10/10.

## What exists

| Artifact | What it does |
|---|---|
| `COMPETENCIES.csv` | 16 competencies mapped across the course. |
| `OUTCOMES.csv` | 55 weekly outcomes, exit tickets, evidence and gates. |
| `CLAIMS.csv` | 52 claims with source, locator and status. |
| `CASE-DOSSIER.md` | Page-level evidence for the Fercaf thesis case. |
| `ERRATA.md` | Corrections, including unresolved source conflicts. |
| `BRIEF-RUBRICS.csv` | 19 brief rubrics with non-negotiables and 4 levels. |
| `PORTFOLIO-RUBRICS.csv` | 32 portfolio rubrics with criteria and review cadence. |
| `EXAM-BLUEPRINTS.csv` | 6 papers: sections, marks, gates, pass floors and remediation. |
| `MASTERY.md`, `CALIBRATION-TEMPLATE.csv` | Gates, weekly loop and confidence calibration. |
| `RUBRIC-GUIDE.md` | Shared scoring rules and evidence standard. |
| `ACCESSIBILITY.md` | Static checks and manual WCAG checklist. |
| `search.html`, `search-index.json` | Site search and deterministic index. |
| `manifest.webmanifest`, `sw.js`, `icons/` | Installable PWA shell. |
| `ci/verify.yml`, `CI.md` | Clean-environment CI and activation. |
| `VERSION.txt`, `SHA256SUMS.txt` | Release identity and file integrity. |

## Claim status

| Status | Count |
|---|---:|
| verified | 36 |
| conditional | 6 |
| pending | 5 |
| unresolved | 4 |
| derived | 1 |

## Verified scope

- All 55 week headings and 55 weekly files.
- Published structural counts: 55 weeks, 660 sessions, 41 problems, 162 quiz items, 30 bench protocols, 6 exams, 32 portfolio items, 19 briefs, 42 methods entries, 17 statistics sections, 13 ML sections, 64 figures, 57 tables.
- Case-study process facts where the thesis is consistent.
- Case-study outputs where the thesis reports them.

## Open, not resolved

- *A. oryzae* vs *A. niger*; no strain identifiers.
- Whiteness 83.5 vs SNI minimum 87, against a conclusion of compliance.
- 25% replacement every 8 h vs every 4 h.
- Ratio table label and Run 2 selection.

## What is not yet audited

The ledger covers the case study, structural counts and a first tranche of lecture, statistics and ML claims. It does **not** yet cover every number in all 55 weeks. Those are registered as `pending` where sampled; the rest still need a full numeric audit.

## Phase 9 status

- Reverted the v24 course shell to the v21 design.
- Tracker: original mast, stat strip, tabs and calendar; no rail, dashboard cards or module hero.
- Weekly pages: original document layout; no rail or hero.
- Removed `course-ui.css`, `course-ui.js` and `course-data.js`.
- Service-worker cache bumped; stale shell assets removed.
- Content added after v21 is retained.

## Phase 8 status

- Shared course shell: left module rail, dashboard cards, module hero and open week plan.
- Tracker restyled to the reference dashboard: welcome card, stat cards, phase-coloured course cards.
- Weekly modules restyled with phase-coloured hero, objectives and 12-session plan.
- Rendered axe audit: tracker 0 violations; week 1 0 violations.
- Visual refresh only; learner and external validation still open.

## Phase 7 status

- 30-week core path, 22 useful-next weeks and 3 optional-depth weeks.
- 15-question entry diagnostic and three catch-up modules.
- Six-stage guided project with synthetic teaching data and templates.
- Fercaf/biodiesel case thread and 11 week callouts.
- Six worked teach-back examples.
- Release labels aligned at v26.
- These are design changes, not learner validation.

## Phase 6 status

- Axe-core found missing main landmarks, heading-order skips, in-text link contrast and unlabeled SVGs. Fixes applied: `<main>` landmarks, hidden `h2`, underlined in-text links, SVG labels and a navigation landmark around the tablist.
- Numeric inventory triaged into 7,816 quantities, 1,560 references, 207 enumerators, 6 candidates and 4 years. Still a review queue, not a completed audit.
- Pilot analysis command added.
- Axe rerun on v26: 0 violations on landing, tracker, search, week 1 and statistics handbook. CI activation remains.

## Phase 5 status

- 30 high-risk numeric claims audited; 9,593-token inventory created.
- Pilot kit ready; not run.
- External-review packet ready; no sign-off.
- Lighthouse: landing 1.00, tracker 1.00 after contrast fixes.
- Full WCAG manual audit, pilot, external review, CI activation and complete numeric audit remain.

## Phase 4 status

- CI workflow defined at `ci/verify.yml` for labs, index freshness, links, HTML, static accessibility, manifest, service worker and checksums. It requires the GitHub `workflow` scope to activate.
- Local CI equivalent passes: 10 tests, 10 labs, 66 HTML files, 0 broken links, deterministic search.
- PWA manifest/icons/service worker added.
- Search covers 70 entries.
- Static accessibility checks pass; full WCAG 2.2 AA remains manual.

## Phase 3 status

- 10/10 practice labs implemented and tested.
- 30/30 bench protocols have risk, controls, acceptance criteria and failure triage.
- 32/32 portfolio items have evidence paths and review cadence.
- Portfolio export tool tested.

## Phase 2 status

- 19/19 brief rubrics: designed.
- 32/32 portfolio rubrics: designed.
- 6/6 exam blueprints and remediation maps: designed.
- 55/55 weekly outcomes and exit tickets: mapped.
- Calibration template: 55 weeks.

These are design artifacts, not validation. Thresholds require external examiner ratification.

## 10/10 blockers

1. Close the 9,593-row numeric inventory, including every `pending` and `unresolved` item.
2. External review by a metabolic engineer and a statistician/ML reviewer; respond to every condition.
3. Full WCAG 2.2 AA manual audit after the contrast fix: screen reader, 200% zoom, 320 px reflow, axe-core in CI.
4. Run the 3–5 learner pilot and report results.
5. Activate `ci/verify.yml` under `.github/workflows/` with a workflow-scoped token and confirm green on GitHub.
6. Ratify pass thresholds, rubric levels and bench risk levels with the external examiner.
7. Rerun axe after the v26 deploy and close any remaining violations.

A self-awarded 10 would repeat the error this audit exists to prevent. This page records what is proven and what is not.
