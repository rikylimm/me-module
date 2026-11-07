#!/usr/bin/env python3
"""Triage numeric inventory tokens into review categories. Not verification."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def category(token, ctx):
    t = token.replace(",", "")
    try:
        n = float(t)
        if 1900 <= n <= 2100 and not re.search(r"(pH|mM|µM|%|°|h\b|min|s\b)", ctx, re.I):
            return "year"
    except ValueError:
        pass
    if re.search(r"\b(Fig(?:ure)?|Table|Eq(?:uation)?|Chapter|§|week|Week|run|Run|Brief|Paper)\s*\.?\s*\d", ctx):
        return "reference"
    if re.fullmatch(r"[1-9]", token) and re.search(r"(Step|step|^\s*\d+[.)])", ctx):
        return "enumerator"
    if re.search(r"(%|mM|µM|nM|mg|g/L|kg|kDa|kJ|kcal|mol|M\b|h\b|min|s\b|°C|µm|nm|mL|L\b|ppm|bar|rpm|Da\b|bp\b|CFU|OD)", ctx, re.I):
        return "quantity"
    return "candidate"

rows = list(csv.DictReader(open(ROOT / "NUMERIC-INVENTORY.csv", encoding="utf-8")))
out = ROOT / "NUMERIC-TRIAGE.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["week", "file", "token", "context", "category", "status", "reviewer", "note"])
    for r in rows:
        cat = category(r["token"], r["context"])
        w.writerow([r["week"], r["file"], r["token"], r["context"], cat, "unreviewed", "", ""])
from collections import Counter
print(Counter(category(r["token"], r["context"]) for r in rows))
print(f"{len(rows)} rows -> {out}")
