#!/usr/bin/env python3
"""Static accessibility smoke checks; not a WCAG audit."""
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
            errors.append(f"{rel}: no lang")
        if not re.search(r"<title>[^<]+</title>", s, re.I):
            errors.append(f"{rel}: no title")
        if not re.search(r'name="viewport"', s, re.I):
            errors.append(f"{rel}: no viewport")
        if len(re.findall(r"<h1\b", s, re.I)) != 1:
            errors.append(f"{rel}: h1 count != 1")
        for a in re.findall(r"<a\b[^>]*target=[\"']_blank[\"'][^>]*>", s, re.I):
            if not re.search(r"rel=[\"'][^\"']*noopener", a, re.I):
                errors.append(f"{rel}: target=_blank without rel=noopener")
        for img in re.findall(r"<img\b[^>]*>", s, re.I):
            if "alt=" not in img.lower():
                errors.append(f"{rel}: img without alt")
    if errors:
        print("static accessibility problems:")
        for e in errors:
            print(" ", e)
        return 1
    print(f"static accessibility checks OK across {len(FILES)} files")
    print("manual WCAG 2.2 AA review still required; see ACCESSIBILITY.md")
    return 0

if __name__ == "__main__":
    sys.exit(main())
