#!/usr/bin/env python3
"""Summarise PILOT-FORM.csv without implying generalisation."""
import csv
import json
import statistics
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "PILOT-FORM.csv"
rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if r.get("exit_score_0_3", "").strip()]
out = {"n_rows": len(rows), "participants": len({r["participant_code"] for r in rows})}
scores = [float(r["exit_score_0_3"]) for r in rows]
out["median_exit_score"] = statistics.median(scores) if scores else None
conf = [float(r["confidence_1_5"]) for r in rows if r.get("confidence_1_5", "").strip()]
if conf and scores:
    out["mean_confidence"] = round(statistics.mean(conf), 2)
    out["mean_exit_score"] = round(statistics.mean(scores), 2)
    out["calibration_gap"] = round(statistics.mean(conf) - statistics.mean(scores), 2)
sus = [float(r["sus_score"]) for r in rows if r.get("sus_score", "").strip()]
out["mean_sus"] = round(statistics.mean(sus), 1) if sus else None
print(json.dumps(out, indent=2))
