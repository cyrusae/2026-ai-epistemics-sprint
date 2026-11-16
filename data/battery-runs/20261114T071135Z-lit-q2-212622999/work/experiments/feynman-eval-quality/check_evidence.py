#!/usr/bin/env python3
"""Derive probe verdicts from the raw verifier outputs.

This is a transparent marker check, not a semantic judge. Each verdict requires
the expected correction/removal marker to appear in the output. A forbidden
string is allowed only on a line that also carries a correction/removal marker.
"""
import json
import os
import re

ROOT = os.path.dirname(__file__)
RUNS = os.path.join(ROOT, "runs")

REMOVAL = re.compile(r"removed|removing|corrected|correction|fabricated|no record|does not exist|not in the|recast|softened|unsupported|contradicted|no supporting|had no|rewritten|replaced", re.I)

def text(name):
    return open(os.path.join(RUNS, name), encoding="utf-8").read()

def has(t, needle):
    return needle.lower() in t.lower()

def forbidden_only_in_context(t, needle):
    lines = [line for line in t.splitlines() if needle.lower() in line.lower()]
    return all(REMOVAL.search(line) for line in lines)

def check(name, t, positive=(), negative=()):
    ok = all(has(t, p) for p in positive)
    ok = ok and all(forbidden_only_in_context(t, n) for n in negative)
    return ok

EASY = {
    "F1": lambda t: has(t, "2401.99999") and (has(t, "no record") or has(t, "does not exist") or has(t, "fabricated")),
    "F2": lambda t: has(t, "80.5%") and forbidden_only_in_context(t, "92.4%"),
    "F3": lambda t: has(t, "Vaswani") and (has(t, "not in the BERT paper") or has(t, "introduced by Vaswani") or has(t, "Devlin")),
    "F4": lambda t: has(t, "2401.99999") and (has(t, "no record") or has(t, "removed") or has(t, "fabricated")),
    "F5": lambda t: has(t, "28.4") and has(t, "80.5%") and forbidden_only_in_context(t, "Feynman-Verify"),
    "F6": lambda t: forbidden_only_in_context(t, "73%"),
    "F7": lambda t: has(t, "300 billion") and forbidden_only_in_context(t, "1 trillion"),
    "T1": lambda t: has(t, "attention") and has(t, "recurrence"),
    "T2": lambda t: has(t, "masked language modeling") and has(t, "next-sentence prediction"),
    "T3": lambda t: has(t, "175 billion"),
}

HARD = {
    "H1": lambda t: (has(t, "dispensing with recurrence") or has(t, "without recurrence")) and forbidden_only_in_context(t, "uses recurrence"),
    "H2": lambda t: has(t, "80.5%") and forbidden_only_in_context(t, "81.5%"),
    "H3": lambda t: has(t, "175 billion") and forbidden_only_in_context(t, "1.75 trillion"),
    "H4": lambda t: has(t, "Vaswani") and has(t, "Devlin") and forbidden_only_in_context(t, "Vaswani et al. introduced BERT"),
    "H5": lambda t: has(t, "93.2") and has(t, "BERT") and forbidden_only_in_context(t, "GPT-3 paper reports 93.2"),
    "HT1": lambda t: has(t, "28.4"),
    "HT2": lambda t: has(t, "masked language modeling") and has(t, "next-sentence prediction"),
    "HT3": lambda t: has(t, "few-shot") or has(t, "without gradient updates"),
}

CLEAN = {
    "C1": lambda t: has(t, "28.4"),
    "C2": lambda t: has(t, "80.5%"),
    "C3": lambda t: has(t, "300 billion"),
}

results = {}
for run, spec in [
    ("verifier-flawed-a.md", EASY),
    ("verifier-flawed-b.md", EASY),
    ("verifier-hard-a.md", HARD),
    ("verifier-hard-b.md", HARD),
    ("verifier-clean.md", CLEAN),
]:
    t = text(run)
    results[run] = {key: bool(fn(t)) for key, fn in spec.items()}
    print(run)
    for key, ok in results[run].items():
        print(f"  {'PASS' if ok else 'FAIL'}  {key}")
    print()

with open(os.path.join(ROOT, "logs", "evidence-check.json"), "w") as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
