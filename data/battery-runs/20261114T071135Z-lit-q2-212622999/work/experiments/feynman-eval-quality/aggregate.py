#!/usr/bin/env python3
"""Aggregate the Feynman eval-quality probe scores from marker checks.

`check_evidence.py` reads the raw verifier outputs and writes
`logs/evidence-check.json`. This script derives the table from those marker
verdicts and cross-checks them against the hand-authored labels in
`scores.json`. The marker check is a transparent string check, not a semantic
judge; the raw outputs remain the primary evidence.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "scores.json").read_text())
evidence = json.loads((ROOT / "logs" / "evidence-check.json").read_text())

RUN_FILE = {
    "verifier-flawed-a": "verifier-flawed-a.md",
    "verifier-flawed-b": "verifier-flawed-b.md",
    "verifier-hard-a": "verifier-hard-a.md",
    "verifier-hard-b": "verifier-hard-b.md",
    "verifier-clean": "verifier-clean.md",
}

rows = []
total_defects = 0
total_detected = 0
total_true = 0
total_true_kept = 0

for run in data["runs"]:
    condition = run["condition"]
    verdicts = evidence[RUN_FILE[run["id"]]]
    if condition in ("easy", "hard"):
        expected = data["fixtures"][condition]["defects"]
        true_expected = data["fixtures"][condition]["true_claims"]
        detected = [key for key in expected if verdicts.get(key)]
        kept = [key for key in true_expected if verdicts.get(key)]
        if set(detected) != set(run["defects_detected"]):
            print(f"WARNING: {run['id']} marker defects {detected} != labels {run['defects_detected']}")
        if set(kept) != set(run["true_claims_preserved"]):
            print(f"WARNING: {run['id']} marker true claims {kept} != labels {run['true_claims_preserved']}")
        total_defects += len(expected)
        total_detected += len(detected)
        total_true += len(true_expected)
        total_true_kept += len(kept)
        rows.append(
            f"| {run['id']} | {condition} | {len(detected)}/{len(expected)} | {len(kept)}/{len(true_expected)} |"
        )
    else:
        expected = data["fixtures"]["clean"]["claims"]
        kept = [key for key in expected if verdicts.get(key)]
        rows.append(
            f"| {run['id']} | clean | n/a | {len(kept)}/{len(expected)} |"
        )

print("| Run | Condition | Defects detected | True claims preserved |")
print("|---|---|---:|---:|")
print("\n".join(rows))
print()
print(f"Defect detection: {total_detected}/{total_defects}")
print(f"True-claim retention: {total_true_kept}/{total_true}")
print(f"Clean numeric-claim retention: {len([k for k in data['fixtures']['clean']['claims'] if evidence['verifier-clean.md'].get(k)])}/3")
print(f"Researcher fabrication refusal: {data['researcher_probe']['refused_to_fabricate']}")
print(f"Telemetry leak: {data['telemetry_probe']['leaked']} ({data['telemetry_probe']['leaked_field']})")
