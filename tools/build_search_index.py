#!/usr/bin/env python3
"""Build a deterministic search index for the static module."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"search.html", "metabolic-engineering-tracker.html"}

def text(html_text: str) -> str:
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", html_text, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

def field(h: str, tag: str):
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", h, re.S | re.I)
    return text(m.group(1)) if m else ""

def title(h: str) -> str:
    return field(h, "title") or field(h, "h1") or "Untitled"

def meta(h: str) -> str:
    for pat in (r'<p class="doc-kicker">(.*?)</p>', r'<p class="kicker">(.*?)</p>', r'<p class="lead">(.*?)</p>'):
        m = re.search(pat, h, re.S | re.I)
        if m:
            return text(m.group(1))[:180]
    return ""

def h1(h: str) -> str:
    return field(h, "h1") or title(h)

def headings(h: str) -> str:
    return " ".join(text(x) for x in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", h, re.S | re.I))

def entry(path: Path, kind: str, url: str|None=None):
    h = path.read_text(encoding="utf-8")
    body = text(h)
    return {
        "title": h1(h),
        "url": url or str(path.relative_to(ROOT)),
        "type": kind,
        "meta": meta(h)[:180],
        "text": (headings(h) + " " + body)[:2400],
    }

items = []
for path in [ROOT / "start-here.html", ROOT / "diagnostic.html", ROOT / "design-briefs.html", ROOT / "methods-handbook.html", ROOT / "ml-handbook.html", ROOT / "stats-handbook.html",
             ROOT / "AUDIT.md", ROOT / "MASTERY.md", ROOT / "BENCH-CRITERIA.md", ROOT / "PORTFOLIO-PACK.md", ROOT / "RUBRIC-GUIDE.md", ROOT / "NUMERIC-AUDIT.md", ROOT / "PILOT-PLAN.md", ROOT / "EXTERNAL-REVIEW.md", ROOT / "VALIDATION.md", ROOT / "ACCESSIBILITY.md", ROOT / "AXE-AUDIT.md", ROOT / "PILOT-ANALYSIS.md", ROOT / "GUIDED-PROJECT.md", ROOT / "CASE-THREAD.md", ROOT / "TEACH-BACK-EXAMPLES.md", ROOT / "CATCH-UP.md"]:
    if path.suffix == ".html":
        items.append(entry(path, "Handbook"))
    else:
        # markdown: first heading, headings, text
        raw = path.read_text(encoding="utf-8")
        title_m = re.search(r"^#\s+(.+)$", raw, re.M)
        hs = " ".join(re.findall(r"^#{2,3}\s+(.+)$", raw, re.M))
        body = re.sub(r"[#*_`>\[\]()]", " ", raw)
        items.append({"title": (title_m.group(1).strip() if title_m else path.stem), "url": str(path.relative_to(ROOT)), "type": "Assurance", "meta": "Audit and mastery", "text": (hs + " " + body)[:2400]})

for path in sorted((ROOT / "lecture-notes").glob("week-*.html")):
    h = path.read_text(encoding="utf-8")
    n = re.search(r"Week\s+(\d+)\s+of\s+55", h)
    items.append(entry(path, f"Week {int(n.group(1)):02d}" if n else "Week", f"lecture-notes/{path.name}"))

for path, kind in [(ROOT / "lecture-notes/index.html", "Lecture index"), (ROOT / "lecture-notes/case-study.html", "Case study"), (ROOT / "lecture-notes/teach-back.html", "Protocol"), (ROOT / "lecture-notes-all-55-weeks.html", "Complete notes"), (ROOT / "practice/README.md", "Practice")]:
    if path.suffix == ".html":
        items.append(entry(path, kind, f"lecture-notes/{path.name}" if path.parent.name == "lecture-notes" else path.name))
    else:
        raw = path.read_text(encoding="utf-8")
        items.append({"title": "Practice labs", "url": "practice/README.md", "type": kind, "meta": "Ten runnable labs", "text": raw[:2400]})

items.append({"title": "Tracker", "url": "metabolic-engineering-tracker.html", "type": "App", "meta": "55-week planner, quiz, problems and portfolio", "text": "tracker week plan daily quiz problems paper log study log bench log exams portfolio design briefs methods machine learning statistics calendar progress"})

items.sort(key=lambda x: (x["type"], x["url"]))
out = ROOT / "search-index.json"
out.write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{len(items)} entries -> {out}")
