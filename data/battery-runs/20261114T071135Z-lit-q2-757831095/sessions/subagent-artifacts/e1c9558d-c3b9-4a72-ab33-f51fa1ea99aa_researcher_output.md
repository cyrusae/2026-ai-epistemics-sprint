Done.

**Answer written to `eval-run/runs/p1/answer.md`:**
```
count=66
sum=17616.39
```

**Method & verification:**
- Read `eval-run/fixtures/ledger.csv`: 400 data rows + header, 6 fields per row, regions `{A,B,C}`, channels `{app,partner,web}`, `refunded` only ever the literals `true`/`false`, no blank regions, no non-numeric revenue, no duplicate ids.
- Selection `region == 'A' and refunded == 'false'` → 66 rows; Decimal sum = **17616.39** exactly (no rounding ambiguity — sum already lands on 2 decimals).
- Cross-checked independently with `awk` (corrected to column 5 for `refunded`; my first awk pass wrongly tested column 6 and returned 0 — that was an awk column-indexing bug, not a data issue). awk gave identical `count=66 sum=17616.39`.
- File contains exactly 2 lines, LF-only, no extra text.

**Residual risk:** the CSV is CRLF-encoded; Python's `csv` module handled this correctly and the repr check confirmed values arrive as `'false'` with no stray `\r`. A naive parser splitting on `,` without newline handling would see `refunded` as `false\r` and undercount — worth knowing for downstream replication.