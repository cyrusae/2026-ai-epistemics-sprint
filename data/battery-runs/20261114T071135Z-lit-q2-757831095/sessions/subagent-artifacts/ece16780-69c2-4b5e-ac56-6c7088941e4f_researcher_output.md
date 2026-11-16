**Result:** Counted rows with `region == 'C'` in `experiments/eval-quality-probes/fixtures/ledger.csv` (400 data rows, regions A/B/C only) → **133**. Wrote exactly one line to `experiments/eval-quality-probes/runs/p8/answer.md`:

```
count=133
```

Gate output: `{"verdict": "ok", "expected": 133, "got": 133}` (exit 0). File is 1 line.

Coverage Status:
- Checked directly: CSV header/data parse via `csv.DictReader`, distinct region values, row count, file line count, gate script source, gate execution.
- Residual risk: none material — count is exact integer match against ground truth and cross-checked by the gate; no duplicates/dirty-region concerns since only exact string `'C'` counted and regions are cleanly A/B/C.
- Not done: no git operations (workspace is not a git repository, so staging is not applicable).