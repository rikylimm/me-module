#!/usr/bin/env python3
"""Fail on broken local links in HTML files."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted(ROOT.rglob("*.html"))
SKIP = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#")

def main() -> int:
    errors = []
    for p in FILES:
        s = p.read_text(encoding="utf-8", errors="ignore")
        for attr, value in re.findall(r'(href|src)\s*=\s*["\']([^"\']+)["\']', s, re.I):
            v = value.strip()
            if not v or v.lower().startswith(SKIP) or v.startswith("#"):
                continue
            target = urlsplit(v)
            if target.scheme or target.netloc:
                continue
            path = unquote(target.path)
            if not path:
                continue
            base = ROOT if path.startswith("/") else p.parent
            candidate = (base / path.lstrip("/")).resolve()
            if not candidate.exists():
                errors.append(f"{p.relative_to(ROOT)} -> {v}")
    if errors:
        print("broken local links:")
        for e in errors:
            print(" ", e)
        return 1
    print(f"links OK across {len(FILES)} HTML files")
    return 0

if __name__ == "__main__":
    sys.exit(main())
