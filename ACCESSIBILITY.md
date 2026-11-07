# Accessibility status

**Release:** v25
**Scope:** landing page, start page, diagnostic, tracker, search, 55 weekly pages, handbooks, audit files.

## Automated checks

`tools/check_a11y.py` passes on 68 HTML files:

- `lang` present.
- page title present.
- viewport present.
- exactly one `h1`.
- images have `alt` (there are no raster content images).
- `target="_blank"` links carry `rel="noopener"`.

`tools/check_links.py` passes: no broken local links.
`tools/check_html.py` passes: basic structure.

## Lighthouse

Final Lighthouse accessibility scores after fixes:

- Landing: **1.00**.
- Tracker: **1.00**.

The initial failures were color contrast on primary buttons and dark footer text. Primary buttons changed to `#0066CC`; dark `--ink-3` changed to `#A1A1A6`. Manual WCAG checks below remain external work.

## Axe-core

Before fixes: landing 0 violations; tracker 1 region violation; week 1 five violations (missing main, heading order, in-text link, region, two unlabeled SVGs); statistics handbook two violations.

Fixes applied: main landmarks, hidden h2, underlined in-text links, SVG labels, tablist navigation landmark. Rerun on v25: **0 violations** on landing, tracker, search, week 1 and statistics handbook.

## Manual checklist

| Check | Status |
|---|---|
| Keyboard tab order reaches every control | Pass, spot-checked |
| Visible focus on links, buttons, inputs | Pass |
| Skip link on landing, search and tracker | Pass |
| Dark and light contrast | Pass, spot-checked |
| Mobile 390 px | Pass, spot-checked |
| Reduced motion | Tracker respects it; static pages do not animate |
| Screen-reader landmark check | **Not yet externally verified** |
| WCAG 2.2 AA full audit | **Not yet externally verified** |
| 200% zoom / reflow | **Not yet externally verified** |
| Form error messaging | **Not yet externally verified** |

## Known limitations

- The tracker is a single-page app; tab changes are not announced by a live region.
- The weekly pages use a sticky local bar; screen-reader order is DOM order.
- No automated axe/Lighthouse run is in CI yet. The current checks are static and structural, not a WCAG conformance claim.
- The PWA service worker is not tested in CI; it is tested by syntax check only.

## What would close the gap

1. Run axe-core against landing, tracker, search, one week page and one handbook in CI.
2. Manual screen-reader pass (VoiceOver on macOS, NVDA on Windows).
3. 200% zoom and 320 px reflow pass.
4. Document the results here and record the reviewer.
