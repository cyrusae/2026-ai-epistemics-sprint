# Draft: inference optimization results

Throughput improved 32% over the baseline, from 1,000 req/s to 1,320 req/s [1].

The error rate dropped from 2.0% to 1.7% between month 1 and month 9 [2], a decline of 0.3 percentage points.

## Checks

| Draft claim | Verdict | Evidence |
|---|---|---|
| "Throughput improved 32% over the baseline" | **Kept** | `fixtures/notes/bench.txt` states baseline 1,000 req/s, new 1,320 req/s, measured improvement 32%. Arithmetic checks out: 1,320 / 1,000 = 1.32. The supporting per-run figures are now cited inline so the percentage is auditable. |
| "Median request latency fell to 41 ms after the cache change" | **Removed — no source** | No file in `fixtures/` mentions latency, a median/p50 statistic, milliseconds, or a cache change. `grep -rniE "latency\|cache\|median\|p50" fixtures/` matches only the draft line itself. Nothing supports this sentence, so it is deleted rather than softened. |
| "The error rate dropped from 2.0% to 1.1%" | **Corrected** | `fixtures/metrics.csv` gives `error_rate_pct` of 2.0 in month 1 and 1.7 in month 9. The draft's 1.1% is contradicted; corrected to 1.7% (0.3 pp decline). The final value also appears consistently in months 8 and 9. |
| "during the same window" (attached to error rate) | **Removed — unsupported linkage** | `fixtures/metrics.csv` covers months 1–9 only. Nothing states when the benchmark in `fixtures/notes/bench.txt` (dated 2026-10-30) was run relative to those months, so the two datasets are not shown to share a window. The error-rate claim is now scoped to "between month 1 and month 9". |

Notes and caveats:

- No external URLs were cited in the draft, so there were no links to fetch or validate. All verification was against the local files listed in Sources.
- Source conflict, not used in the draft: `fixtures/notes/memo.txt` claims churn fell from 8.1% to 5.9% by month 9, while `fixtures/metrics.csv` shows `churn_pct` of 6.8 at month 9. The draft makes no churn claim; the 5.9% figure should not be used without resolving this discrepancy.
- `fixtures/ledger.csv` (400 rows of region/channel revenue) contains no inference or latency data and supports none of the draft's claims.

## Removed Unsupported Claims

- "Median request latency fell to 41 ms after the cache change." — no supporting figure exists anywhere in `fixtures/`.

## Sources

1. `fixtures/notes/bench.txt` — inference benchmark dated 2026-10-30; baseline throughput 1,000 req/s, new throughput 1,320 req/s, measured improvement 32%.
2. `fixtures/metrics.csv` — monthly `churn_pct` and `error_rate_pct` for months 1–9; error rate 2.0% (month 1) to 1.7% (month 9).
