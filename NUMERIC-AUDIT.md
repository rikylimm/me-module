# Numeric audit

**Release:** v25
**Purpose:** make the unverified-number problem visible and reviewable.

## What is done

- `NUMERIC-AUDIT.csv` audits 30 high-risk numeric claims: core course counts, the main worked anchors, and the thesis claims.
- `NUMERIC-INVENTORY.csv` lists **9,593 numeric tokens** across the 55 weekly pages, with context and blank status fields.
- Verified: course counts, figure/table counts, and the thesis values that are consistent in the source.
- Derived: internal worked-anchor arithmetic; still convention-dependent.
- Pending: cell size, ribosome count, yeast volume ratio and similar textbook values.
- Unresolved: whiteness vs SNI, replacement interval, ratio labels, fungal identity.

## What is not done

The inventory is not a completed audit. It is a 9,593-row work queue. A 10/10 claim requires:

1. A reviewer to mark each token `verified`, `conditional`, `derived`, `remove` or `not-a-claim`.
2. A source/page for every verified numeric claim.
3. A decision on every `pending` and `unresolved` item.
4. A second reviewer for the thesis claims.

Run:

```bash
python tools/audit_numbers.py
```

This regenerates `NUMERIC-INVENTORY.csv` from the current week pages. It strips scripts, styles and SVG geometry so the inventory is about prose claims, not figure coordinates.

## Rules

- A number in a worked example is a **derived** value, not an independently verified fact.
- A textbook order-of-magnitude is **conditional** until a page is cited.
- A source conflict is **unresolved**, never silently chosen.
- A number removed from the prose must be removed from the inventory status, not deleted from the audit trail.
