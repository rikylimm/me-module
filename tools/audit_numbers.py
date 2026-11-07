#!/usr/bin/env python3
"""Inventory numeric tokens in weekly pages for review. Does not verify them."""
import csv
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK = sorted((ROOT / "lecture-notes").glob("week-*.html"))

def plain(h: str) -> str:
    h = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(h)).strip()

rows = []
for p in WEEK:
    n = int(re.search(r"week-(\d+)", p.name).group(1))
    t = plain(p.read_text(encoding="utf-8"))
    for m in re.finditer(r"(?<![A-Za-z])\d+(?:[.,]\d+)?(?:\s?[×x]\s?10[-−]?\d+)?", t):
        token = m.group(0)
        ctx = t[max(0, m.start() - 90):m.end() + 90]
        rows.append([n, p.name, token, ctx])

with open(ROOT / "NUMERIC-INVENTORY.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["week", "file", "token", "context", "status", "reviewer", "note"])
    for r in rows:
        w.writerow(r + ["unreviewed", "", ""])
print(f"{len(rows)} numeric tokens -> NUMERIC-INVENTORY.csv")
