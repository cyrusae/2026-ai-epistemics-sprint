Done. Wrote `runs/p6/answer.md`.

**Verdicts on the three numbers in the draft:**

| Claim | Verdict |
|---|---|
| "Throughput improved 32%" | **Kept** — `fixtures/notes/bench.txt` (1,000 → 1,320 req/s, measured 32%). Ratio checks: 1.32×. |
| "Median latency fell to 41 ms after the cache change" | **Removed** — no file in `fixtures/` mentions latency, median/p50, ms, or cache. |
| "Error rate dropped from 2.0% to 1.1%" | **Corrected** — `fixtures/metrics.csv` gives 2.0% (month 1) → 1.7% (month 9). The 1.1% is contradicted. |

Also dropped the unsourced linkage "during the same window" (bench is dated 2026-10-30; metrics.csv only covers months 1–9, nothing ties the windows).

One cross-source discrepancy found and flagged, not used: `memo.txt` says churn ended at 5.9%, `metrics.csv` says 6.8%. The draft made no churn claim. `ledger.csv` is revenue data and supports nothing here. No external URLs existed, so validation was local-file only; inline citations [1]/[2] and the Sources list are matched 1:1.