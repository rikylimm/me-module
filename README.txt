Metabolic engineering module — v28
Updated 7 November 2026

WHAT IS HERE
- index.html — landing page, installable PWA entry.
- Tracker Sync tab — private `me-sync` push/pull, GitHub status and manual backup controls.
- start-here.html — three paths, core weeks, diagnostic and project links.
- diagnostic.html — 15-question entry diagnostic; no data saved.
- CORE-PATH.csv — 30 core weeks; 22 useful next; 3 optional depth.
- CATCH-UP.md — molecular biology, genetics and biochemistry modules.
- GUIDED-PROJECT.md, project/ — six-stage project from balance to evidence.
- CASE-THREAD.md — Fercaf and biodiesel touchpoints with transfer limits.
- TEACH-BACK-EXAMPLES.md — six worked examples and scoring.
- metabolic-engineering-tracker.html — 55-week tracker. Open this first.
- lecture-notes-all-55-weeks.html — complete single-file lecture notes.
- lecture-notes/ — split edition:
  - index.html — 55-week index, grouped by phase.
  - case-study.html — source-audited Fercaf thesis case study.
  - teach-back.html — the five-minute teach-back protocol.
  - week-01.html … week-55.html — one file per week.
- design-briefs.html, methods-handbook.html, ml-handbook.html, stats-handbook.html.
- COMPETENCIES.csv — 16 competencies.
- OUTCOMES.csv — 55 weekly outcomes, exit tickets, evidence and gates.
- CLAIMS.csv — claim register with source, locator and status.
- CASE-DOSSIER.md — page-level thesis evidence.
- ERRATA.md — corrections and unresolved conflicts.
- AUDIT.md — assurance summary and 10/10 blockers.
- RUBRIC-GUIDE.md — shared 4-level evidence standard.
- BRIEF-RUBRICS.csv — 19 brief rubrics.
- PORTFOLIO-RUBRICS.csv — 32 portfolio rubrics.
- EXAM-BLUEPRINTS.csv — 6 papers, gates and remediation.
- MASTERY.md — weekly loop, gates and calibration.
- CALIBRATION-TEMPLATE.csv — 55-week calibration log.
- BENCH-CRITERIA.md, BENCH-CRITERIA.csv — 30 bench protocols with risk, controls and acceptance criteria.
- practice/ — 10 runnable NumPy labs and 10 unit tests.
- PORTFOLIO-PACK.md, PORTFOLIO-EVIDENCE.csv — 32-item evidence pack and review workflow.
- tools/export_portfolio.py — deterministic portfolio export with SHA-256 manifest.
- search.html, search-index.json — site search across weeks, handbooks and audit files.
- manifest.webmanifest, sw.js, icons/ — installable PWA and offline shell.
- ACCESSIBILITY.md — automated checks and manual WCAG checklist.
- NUMERIC-AUDIT.md, NUMERIC-AUDIT.csv, NUMERIC-INVENTORY.csv — 30-claim audit and 9,593-token review queue.
- PILOT-PLAN.md, PILOT-FORM.csv — 3–5 learner pilot kit.
- EXTERNAL-REVIEW.md, REVIEW-FORM.csv — reviewer packet and sign-off form.
- VALIDATION.md — current validation status and 10/10 blockers.
- AXE-AUDIT.md — axe-core results and fixes.
- NUMERIC-TRIAGE.csv — 9,593-token review queue classified by type.
- PILOT-ANALYSIS.md — pilot summary command.
- ci/verify.yml, CI.md — workflow and activation instructions.
- VERSION.txt, SHA256SUMS.txt — release identity and file checksums.

WHAT THIS EDITION CHANGED
- The 55 weekly pages and index were regenerated from the updated lecture.
- 55 repeated generic teach-back blocks were replaced by one protocol page;
  each week keeps its specific transfer prompt and links to the protocol.
- Tracker week notes link to the case study and weekly prompts.
- Design Brief 8 now uses the thesis starter, records its identity conflict,
  and treats the division-of-labour mechanisms as hypotheses to test.

THESIS SOURCE AND AUDIT
Source: [TK4092] Kelompok C2.1516.B.02, Pengembangan Reaktor untuk
Produksi Tepung Fercaf (ITB, 2017).

Confirmed in the source: 60 kg/day, 8 trays, 2.5 kg per tray per hour,
1–1.5 mm chips, 24 L starter (8 L each), 8 h residence, 5-day validation,
35% yield, 13% moisture, 10.4% swelling power, 83.5% whiteness.

Open source conflicts, not transcription errors:
- Fungal identity: most passages say Aspergillus oryzae; one starter-preparation
  passage says Aspergillus niger (printed p. 46 / PDF p. 70). No strain identifiers or independent
  identity check. Treat the fungal identity as unresolved.
- Whiteness: SNI 7622:2011 Table 4.8 sets a minimum of 87; validation reports 83.5,
  while the abstract and conclusion say the product meets SNI.
- Ratio: the abstract and conclusion use water-to-substrate 7:1. The methods
  narrative uses the reciprocal substrate-to-water 1:7, which is the same condition
  if the basis is stated. The methods table is headed "Rasio air terhadap substrat"
  but lists 1:7 and 1:12, so its label and values conflict; Table 4.1 Run 2 is a
  separate 1:8 condition. The issue is the table labelling and which run is compared,
  not the reciprocal arithmetic.
- Replacement interval: abstract and methods say 25% at every residence time (8 h);
  the validation procedure (printed p. 103 / PDF p. 127) says 25% every 4 h. Both are in the
  source; neither interval is settled.

MASTERY (PHASE 2)
- 55/55 weekly outcomes and exit tickets.
- 19/19 brief rubrics, with non-negotiables and 4 levels.
- 32/32 portfolio rubrics, with review cadence.
- 6/6 exam blueprints, gates and remediation maps.
- Calibration log for all 55 weeks.
- Pass thresholds are design decisions requiring external ratification.

PRACTICE (PHASE 3)
- 10 runnable labs: pH, kinetics, balances, Monod, toy FBA, MDV, power, DOE, ML, bootstrap.
- 10 unit tests; all pass with NumPy only.
- 30/30 bench protocols screened for risk, controls, acceptance and failure triage.
- 32/32 portfolio items mapped to artifact paths and evidence.
- Portfolio exporter produces a deterministic zip with SHA-256 manifest.

RELIABILITY (PHASE 4)
- 10/10 practice tests pass in the current environment.
- 66/66 HTML files pass static structure and accessibility checks.
- Zero broken local links.
- Search index is deterministic and covers 70 entries.
- PWA manifest, icons and service worker are present; service worker syntax checked.
- CI workflow at ci/verify.yml runs labs, search-index freshness, link/HTML/a11y checks, manifest validation, SW syntax and checksums once activated.
- Static checks are not a full WCAG 2.2 AA audit; manual screen-reader and 200% zoom checks remain.

VALIDATION (PHASE 5)
- 30 high-risk numeric claims audited; 9,593-token inventory generated for the rest.
- Lighthouse found primary-button contrast failures on landing (0.95) and tracker (0.96); buttons darkened to #0066CC. Rerun pending.
- 3–5 learner pilot kit ready; not run.
- Two-reviewer external packet ready; no signatures invented.
- CI local equivalent passes; activation still needs workflow scope.

AUDIT SCOPE
The claim ledger covers all case-study claims, all published structural counts, and
a first tranche of lecture, statistics and ML claims. It does not yet cover every
number in all 55 weeks; those are listed as pending where sampled. See AUDIT.md for
the 10/10 blockers.

CONTENT COUNTS
- 55 weeks, 64 figures, 57 tables.
- 55 weekly pages + index + case study + teach-back.

The original thesis PDF is not included. Keep the lecture-notes folder beside the
HTML files.
