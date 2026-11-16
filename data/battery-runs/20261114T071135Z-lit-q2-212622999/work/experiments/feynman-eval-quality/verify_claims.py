#!/usr/bin/env python3
"""Check the quantitative claims in the case study against saved artifacts."""
import glob
import json
import os
import re

ROOT = os.path.dirname(__file__)
checks = []

def check(name, condition, detail=""):
    checks.append((name, bool(condition), detail))

# Probe scores
scores = json.load(open(os.path.join(ROOT, "scores.json")))
runs = scores["runs"]
easy = [r for r in runs if r["condition"] == "easy"]
hard = [r for r in runs if r["condition"] == "hard"]
clean = [r for r in runs if r["condition"] == "clean"][0]
evidence = json.load(open(os.path.join(ROOT, "logs", "evidence-check.json")))
run_file = {
    "verifier-flawed-a": "verifier-flawed-a.md",
    "verifier-flawed-b": "verifier-flawed-b.md",
    "verifier-hard-a": "verifier-hard-a.md",
    "verifier-hard-b": "verifier-hard-b.md",
    "verifier-clean": "verifier-clean.md",
}
defects = 0
expected_defects = 0
true_kept = 0
expected_true = 0
for r in easy + hard:
    expected = scores["fixtures"][r["condition"]]["defects"]
    expected_true_keys = scores["fixtures"][r["condition"]]["true_claims"]
    verdicts = evidence[run_file[r["id"]]]
    defects += sum(1 for k in expected if verdicts.get(k))
    expected_defects += len(expected)
    true_kept += sum(1 for k in expected_true_keys if verdicts.get(k))
    expected_true += len(expected_true_keys)
check("24/24 defects", defects == 24 and expected_defects == 24, f"{defects}/{expected_defects}")
check("12/12 true claims", true_kept == 12 and expected_true == 12, f"{true_kept}/{expected_true}")
check("3/3 clean numeric claims", sum(1 for k in scores["fixtures"]["clean"]["claims"] if evidence["verifier-clean.md"].get(k)) == 3)

# Official eval
rows = []
for path in glob.glob(os.path.join(ROOT, "official-eval", "results", "*.jsonl")):
    rows.extend(json.loads(line) for line in open(path) if line.strip())
check("22 official rows", len(rows) == 22, str(len(rows)))
check("18 completed", sum(1 for r in rows if r.get("completed")) == 18)
check("137664710 tokens", sum((r.get("usage") or {}).get("total_tokens", 0) for r in rows) == 137664710)
check("20591 wall seconds", sum(r.get("wall_s", 0) for r in rows) == 20591)
check("cost all zero", all((r.get("usage") or {}).get("cost_usd", 0) == 0 for r in rows))
check("4 distinct question ids", len({r["id"] for r in rows}) == 4, str(sorted({r["id"] for r in rows})))
check("12 questions", len(open(os.path.join(ROOT, "official-eval", "questions.jsonl")).read().strip().splitlines()) == 12)
check("6 result files", len(glob.glob(os.path.join(ROOT, "official-eval", "results", "*.jsonl"))) == 6)

# Version provenance
gpt03 = [r for r in rows if r.get("feynman_version") == "0.5.3" and r.get("model", "").endswith("gpt-5.6-terra")]
gpt02 = [r for r in rows if r.get("feynman_version") == "0.5.2" and r.get("model", "").endswith("gpt-5.6-terra")]
gpt00 = [r for r in rows if r.get("feynman_version") == "0.5.0" and r.get("model", "").endswith("gpt-5.6-terra")]
check("0.5.3 gpt run 44 cites, 4/4", sum(r["citations"] for r in gpt03) == 44 and sum(1 for r in gpt03 if r["completed"]) == 4)
check("0.5.2 gpt run 28 cites, 3/4", sum(r["citations"] for r in gpt02) == 28 and sum(1 for r in gpt02 if r["completed"]) == 3)
check("0.5.0 gpt run 43 cites, 4/4", sum(r["citations"] for r in gpt00) == 43 and sum(1 for r in gpt00 if r["completed"]) == 4)
check("0.5.3 dirty", all(r.get("git_dirty") for r in rows if r.get("feynman_version") == "0.5.3"))

# Published self-checks
pub = open(os.path.join(ROOT, "logs", "published-selfchecks.txt")).read()
check("npm test 0 tests", "tests 0" in pub and "exit=0" in pub)
check("architecture MODULE_NOT_FOUND", "MODULE_NOT_FOUND" in pub and "exit=1" in pub)

# Telemetry leak
leak = json.load(open(os.path.join(ROOT, "logs", "telemetry-leak-0565.json")))
check("telemetry leak", leak.get("leaked") is True and "PATIENT_ZERO_SECRET" in leak["toolEvent"]["properties"]["error_message"])

# Blindspot
blind = json.loads(open(os.path.join(ROOT, "probes", "eval-scorer-blindspot", "row.jsonl")).read().strip().splitlines()[-1])
check("false claim scores 100%", blind.get("completed") and blind.get("citation_validity") == 1 and blind.get("title_match") == 1 and blind.get("key_recall") == 1)

# Test inventory
check("61 test files", len(glob.glob("/tmp/feynman-src/tests/*.test.ts")) == 61)
test_count = 0
for path in glob.glob("/tmp/feynman-src/tests/*.test.ts"):
    test_count += len(re.findall(r"^\s*(?:test|it)\(", open(path).read(), re.M))
check("349 test declarations", test_count == 349, str(test_count))

for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
print(f"\n{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks passed")
raise SystemExit(0 if all(ok for _, ok, _ in checks) else 1)
