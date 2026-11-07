# Errata and corrections

**Module:** Metabolic engineering — 55-week HTML edition
**Current release:** v25
**Last updated:** 7 November 2026
**Case-study source:** [TK4092] Kelompok C2.1516.B.02, *Pengembangan Reaktor untuk Produksi Tepung Fercaf* (ITB, 2017)

## v25 — audit spine added

- Added `CLAIMS.csv`, `OUTCOMES.csv`, `COMPETENCIES.csv`, this errata file, `CASE-DOSSIER.md`, and `AUDIT.md`.
- Added `VERSION.txt` and `SHA256SUMS.txt`.
- No course prose changed in this release except the v15 corrections below.

## v15 — thesis-audit corrections

### 1. Ratio notation
**Old:** 7:1 water-to-substrate and 1:7 substrate-to-water were described as “not interchangeable.”
**Correct:** They are reciprocal statements of the same condition if the basis is explicit. The real problems are:
- the methods table is headed *“Rasio air terhadap substrat”* but lists 1:7 and 1:12;
- Table 4.1 Run 2 is a separate 1:8 condition;
- the selected validation is 7:1 water-to-substrate.

The module now distinguishes reciprocal notation from a label/value conflict and from a different run.

### 2. Fungal identity
**Old:** the starter was called verified as *Aspergillus oryzae*.
**Correct:** most passages say *A. oryzae*, but one starter-preparation passage says *A. niger* (printed p. 46 / PDF p. 70). No strain identifiers or independent identity check are given. The identity is **unresolved**.

### 3. Replacement interval
**Old:** 25% replacement was stated only as “every 4 hours.”
**Correct:** abstract and methods say 25% at every residence time (8 h); the validation procedure says 25% every 4 h (printed p. 103 / PDF p. 127). Both are in the source. The interval is **unresolved**, not a single verified schedule.

### 4. Whiteness compliance
**Old:** the case study was described as verified while the conclusion’s SNI claim was unresolved.
**Correct:** SNI 7622:2011 Table 4.8 sets whiteness minimum 87. Validation reports 83.5. The abstract and conclusion say the product meets SNI. This is an **open discrepancy**, not a resolved pass.

### 5. Brief 8 mechanisms
**Old:** enzyme secretion, lactate inhibition and incompatible oxygen demands were stated as facts.
**Correct:** these are hypotheses. The thesis measured counts, pH, cyanogenic compounds, yield, moisture, swelling and whiteness; it did not measure enzyme activity, sugar release, organic-acid rates or oxygen demand. Brief 8 now says so.

## Earlier correction retained

- **v13:** the first split of the lecture notes was stale; all 55 weekly pages and the index were regenerated in v14.
- **v14:** the 4-hour replacement line was presented without the 8-hour general rule; v15 now states both as a source conflict.

## Open corrections

These are not silently resolved:

- *A. oryzae* / *A. niger* identity.
- Whiteness 83.5 vs SNI minimum 87, against a conclusion of compliance.
- 25% replacement every 8 h vs every 4 h.
- Ratio table label and Run 2 selection.

See `CASE-DOSSIER.md` for quotations and page locations, and `CLAIMS.csv` for status.
