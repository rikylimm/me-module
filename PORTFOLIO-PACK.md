# Portfolio evidence pack

**Release:** v18
**Purpose:** turn 32 portfolio items into an assessable, exportable pack.

## Folder convention

```
portfolio/
  P01_repository_scaffold/
    README.md
    artifact...
    evidence/
      source_data.csv
      run_log.md
  P02_enzyme_dossier/
  ...
  P32_external_research_artefact/
```

Each `README.md` states:

1. the question;
2. what the artifact is;
3. how to run or open it;
4. the data source and provenance;
5. what the artifact does **not** show;
6. the rubric score and reviewer.

## Required evidence

`PORTFOLIO-EVIDENCE.csv` gives the evidence for every item. A folder without the required evidence is not a portfolio item, regardless of prose.

## Review workflow

1. Learner self-scores against `PORTFOLIO-RUBRICS.csv` and `RUBRIC-GUIDE.md`.
2. Course reviewer scores independently.
3. Scores differ by more than one level → discuss and rescore.
4. A score of 4 requires external review.
5. Record the score, reviewer and date in `PORTFOLIO-EVIDENCE.csv`.

## Export

From the repo root:

```bash
python3 tools/export_portfolio.py --root portfolio --out portfolio-export.zip
```

The export includes each `README.md`, the artifact, the evidence folder, the rubric row and a manifest with SHA-256 hashes. Do not include unpublished third-party data without permission.

## Red flags

- A screenshot without the underlying data.
- A result that cannot be regenerated from the folder.
- A cited source with no page, DOI or accession.
- A figure whose caption overstates the measurement.
- A folder dated in one weekend but claiming fifty-five weeks of work.
