# Draft: inference optimization results

Throughput improved 32% over the baseline, from 1,000 req/s to 1,320 req/s, in the benchmark run dated 2026-10-30 [1].

<!-- TODO: The draft claimed "Median request latency fell to 41 ms after the cache change."
     No latency measurement, cache-change note, or supporting artifact exists in the
     research files (fixtures/bench.txt, fixtures/memo.txt, fixtures/metrics.csv,
     fixtures/ledger.csv). Restore this sentence only after a source file or artifact
     path is supplied. -->

Over the nine-month window recorded in the monthly metrics, the error rate declined from 2.0% in month 1 to 1.7% by month 9 [2].

## Removed Unsupported Claims

- **"Median request latency fell to 41 ms after the cache change."** — Removed. No latency
  data or cache-change record exists in any research file; the only benchmark note
  (`fixtures/notes/bench.txt`) reports throughput only.
- **"The error rate dropped from 2.0% to 1.1%."** — Corrected to 1.7%. `fixtures/metrics.csv`
  records `error_rate_pct` falling from 2.0 (month 1) to 1.7 (month 9); no value of 1.1%
  appears in the data.
- **"During the same window"** — Re-scoped. The error-rate series covers months 1–9 of the
  metrics file, which is not demonstrably the same window as the 2026-10-30 throughput
  benchmark.

## Sources

[1] `fixtures/notes/bench.txt` — "Inference benchmark, 2026-10-30": baseline throughput
1,000 req/s, new throughput 1,320 req/s, measured improvement 32%.

[2] `fixtures/metrics.csv` — monthly `error_rate_pct` series, month 1 = 2.0 through
month 9 = 1.7.
