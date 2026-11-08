# Axe audit

**Tool:** axe-core 4.13.0 via `@axe-core/cli`
**Target:** v26 source pages
**Date:** 7 November 2026

## Results before fixes

- Landing: **0 violations**.
- Tracker: **1** — `region` on the tablist.
- Week 1: **5** — missing main landmark, heading order, in-text link distinction, 43 region nodes, 2 unlabeled SVG figures.
- Statistics handbook: **2** — missing main landmark, region.

## Fixes applied

- `<main>` landmark around the document wrapper.
- Hidden `h2` before weekly `h3` content.
- In-text links underlined.
- `aria-label` copied from figure captions onto `role="img"` SVGs.
- Tracker tablist wrapped in a navigation landmark.
- Primary button and dark secondary text contrast fixed.

## After fixes

Rerun on v26 source:

- Landing: **0 violations**.
- Tracker: **0 violations**.
- Search: **0 violations**.
- Week 1: **0 violations**.
- Statistics handbook: **0 violations**.

These are automated results on the original five pages. The new `start-here.html` and `diagnostic.html` pass static checks but have not been axe-audited. Manual WCAG remains.

## Limits

Axe detects only a subset of WCAG issues. Manual screen-reader, keyboard, 200% zoom and 320 px reflow checks remain.
