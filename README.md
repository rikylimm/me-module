# Metabolic engineering — 55-week HTML module

A self-contained 55-week curriculum: tracker, full lecture notes, 55 weekly lecture files, design briefs, methods, machine learning, statistics, and a source-audited Fercaf thesis case study. Current release: v25, with a 30-week core path, entry diagnostic, catch-up modules, a six-stage guided project, case-thread callouts, teach-back examples, and all v22 assurance artifacts. No build step, no server, no install.

## Start here

- `index.html` — landing page.
- `metabolic-engineering-tracker.html` — the 55-week tracker.
- `lecture-notes/index.html` — weekly lecture notes, grouped by phase.
- `lecture-notes/case-study.html` — the source-audited Fercaf thesis case study.
- `lecture-notes/teach-back.html` — five-minute teach-back protocol.
- `lecture-notes-all-55-weeks.html` — complete notes in one file.
- `start-here.html`, `CORE-PATH.csv`, `diagnostic.html`, `CATCH-UP.md` — paths, placement and catch-up.
- `GUIDED-PROJECT.md`, `project/` — six-stage applied project.
- `course-ui.css`, `course-ui.js`, `course-data.js` — shared rail and dashboard shell.
- `CASE-THREAD.md`, `TEACH-BACK-EXAMPLES.md` — recurring case and worked assessment examples.
- `AUDIT.md` — assurance summary, open conflicts and 10/10 blockers.
- `CLAIMS.csv` — claim register with source, locator and status.
- `OUTCOMES.csv` — 55 weekly outcomes, exit tickets, evidence and gates.
- `COMPETENCIES.csv` — 16 competencies mapped across the course.
- `CASE-DOSSIER.md` — page-level thesis evidence and open questions.
- `ERRATA.md` — corrections and unresolved source conflicts.
- `RUBRIC-GUIDE.md` — shared 4-level scoring standard.
- `BRIEF-RUBRICS.csv` — 19 brief rubrics with non-negotiables.
- `PORTFOLIO-RUBRICS.csv` — 32 portfolio rubrics.
- `EXAM-BLUEPRINTS.csv` — 6 papers with gates and remediation.
- `MASTERY.md`, `CALIBRATION-TEMPLATE.csv` — mastery gates and confidence calibration.
- `BENCH-CRITERIA.md`, `BENCH-CRITERIA.csv` — 30 bench protocols with risk, controls and acceptance criteria.
- `practice/` — 10 runnable NumPy labs and 10 unit tests.
- `PORTFOLIO-PACK.md`, `PORTFOLIO-EVIDENCE.csv` — 32-item evidence pack.
- `tools/export_portfolio.py` — deterministic portfolio zip with SHA-256 manifest.
- `search.html`, `search-index.json` — site search.
- `manifest.webmanifest`, `sw.js`, `icons/` — installable PWA / offline shell.
- `ACCESSIBILITY.md` — static checks and manual WCAG checklist.
- `NUMERIC-AUDIT.md`, `NUMERIC-AUDIT.csv`, `NUMERIC-INVENTORY.csv` — numeric audit and review queue.
- `PILOT-PLAN.md`, `PILOT-FORM.csv` — 3–5 learner pilot kit.
- `EXTERNAL-REVIEW.md`, `REVIEW-FORM.csv` — reviewer packet and sign-off.
- `VALIDATION.md` — current validation status.
- `AXE-AUDIT.md`, `NUMERIC-TRIAGE.csv`, `PILOT-ANALYSIS.md` — external-quality checks and work queues.
- `ci/verify.yml`, `CI.md` — clean-environment CI and activation instructions.
- `VERSION.txt`, `SHA256SUMS.txt` — release identity and checksums.

## Contents

- 55 weeks, 660 sessions, 41 problems, 162 quiz items, 30 bench protocols, 6 exams, 32 portfolio items, 19 design briefs, 42 methods entries, 17 statistics sections.
- 64 figures and 57 tables across the lecture notes.
- 55 weekly files plus index, case study, and teach-back.
- Four handbooks: design briefs, methods, machine learning, statistics.

## Thesis audit

The case study is checked against `[TK4092] Kelompok C2.1516.B.02, Pengembangan Reaktor untuk Produksi Tepung Fercaf (ITB, 2017)`.

Confirmed: 60 kg/day, 8 trays, 2.5 kg/tray/hour, 1–1.5 mm chips, 24 L starter (8 L each), 8 h residence, five-day validation, 35% yield, 13% moisture, 10.4% swelling power, 83.5% whiteness. The two bacterial names are confirmed; the fungal identity is not.

Open source conflicts, not resolved:
- Fungal identity: most passages say *A. oryzae*; one starter-preparation passage says *A. niger* (PDF p. 70). No strain identifiers or independent identity check.
- SNI 7622:2011 Table 4.8 sets whiteness minimum 87; validation reports 83.5, while the abstract and conclusion say the product meets SNI.
- Ratio: abstract/conclusion use water-to-substrate 7:1; the methods narrative uses reciprocal substrate-to-water 1:7 (same condition if stated). The methods table header says water-to-substrate but lists 1:7 and 1:12, so label and values conflict; Table 4.1 Run 2 is a separate 1:8 condition. The issue is the table labelling and run selection, not reciprocal arithmetic.
- Replacement interval: 25% at every residence time (8 h) in abstract/methods; 25% every 4 h in the validation procedure (printed p. 103).

Release identity: `VERSION.txt`; file checksums: `SHA256SUMS.txt`. See `AUDIT.md` for what is verified and what remains open, `MASTERY.md` for gates, `ACCESSIBILITY.md` for the manual checklist, and `README.txt` for edition notes.

## GitHub Pages

Open `index.html` at the repo root. Keep all files and the `lecture-notes/` folder together.
