Wrote `experiments/eval-quality-probes/runs/p1/answer.md` with `count=66` / `sum=17616.39`.

Rows: 400 data rows, clean values (region ∈ {A,B,C}, refunded ∈ {true,false}, all revenue numeric). 126 region-A rows, of which 66 unrefunded. Sum computed two ways (Python `Decimal` exact and `awk` float), both 17616.39 — no rounding ambiguity. File verified at exactly 2 lines, no trailing text.