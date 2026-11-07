#!/usr/bin/env python3
"""Minimal static HTML structure checks."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted(ROOT.rglob("*.html"))

def main() -> int:
    errors = []
    for p in FILES:
        s = p.read_text(encoding="utf-8", errors="ignore")
        rel = p.relative_to(ROOT)
        if not re.search(r"<html[^>]+lang=", s, re.I):
            errors.append(f"{rel}: missing html lang")
        if not re.search(r"<title>[^<]+</title>", s, re.I):
            errors.append(f"{rel}: missing title")
        if not re.search(r'name="viewport"', s, re.I):
            errors.append(f"{rel}: missing viewport")
        if len(re.findall(r"<h1\b", s, re.I)) != 1:
            errors.append(f"{rel}: expected exactly one h1")
        for img in re.findall(r"<img\b[^>]*>", s, re.I):
            if "alt=" not in img.lower():
                errors.append(f"{rel}: img without alt")
    if errors:
        print("HTML problems:")
        for e in errors:
            print(" ", e)
        return 1
    print(f"HTML structure OK across {len(FILES)} files")
    return 0

if __name__ == "__main__":
    sys.exit(main())
