#!/usr/bin/env python3
"""Harness-native typed gate for probe p8: prints a JSON verdict on stdout."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GT = json.loads((ROOT / "ground_truth.json").read_text())
path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "runs/p8/answer.md"

if not path.exists():
    print(json.dumps({"verdict": "blocked", "reason": "missing output file"}))
    sys.exit(1)

text = path.read_text(errors="replace")
m = re.search(r"count\s*=\s*(\d+)", text)
got = int(m.group(1)) if m else None
expected = GT["p8"]["region_c_count"]
ok = got == expected
print(json.dumps({"verdict": "ok" if ok else "blocked", "expected": expected, "got": got}))
sys.exit(0 if ok else 1)
