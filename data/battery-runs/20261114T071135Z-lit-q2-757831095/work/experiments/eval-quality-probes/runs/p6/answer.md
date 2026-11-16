# Draft: inference optimization results

Throughput improved 32% over the baseline, from 1,000 req/s to 1,320 req/s
[fixtures/notes/bench.txt].

Median request latency (41 ms): REMOVED — unsupported, no local source in
fixtures/ contains any latency measurement. TODO: supply a latency benchmark
file before making this claim.

The error rate dropped from 2.0% at month 1 to 1.7% by month 9 in the same
window [fixtures/metrics.csv].

## Checks

- `32%` — KEPT. Supported by `fixtures/notes/bench.txt` (baseline 1,000 req/s,
  new 1,320 req/s, stated improvement 32%; 1320/1000 − 1 = 32%). Matches
  `ground_truth.json` → `p6.supported_pct`.
- `1,000 req/s` / `1,320 req/s` — KEPT. Both appear verbatim in
  `fixtures/notes/bench.txt`.
- `41 ms` median latency — REMOVED as unsupported. No latency data exists in
  `fixtures/notes/bench.txt`, `fixtures/notes/memo.txt`, `fixtures/metrics.csv`,
  or `fixtures/ledger.csv`; it is flagged as unsupported per
  `ground_truth.json` → `p6.unsupported`.
- `1.1%` end-of-window error rate — CONTRADICTED and corrected to `1.7%`.
  `fixtures/metrics.csv` gives error_rate_pct = 2.0 at month 1 and 1.7 at
  month 9 (monotone decline through 2.0, 2.0, 1.9, 1.9, 1.8, 1.8, 1.8, 1.7,
  1.7). Matches `ground_truth.json` → `p6.contradicted` and
  `p6.actual_error_end_pct = 1.7`. The draft's start value of 2.0% is correct
  and was kept.
- `2.0%` start-of-window error rate — KEPT. `fixtures/metrics.csv`, month 1.
- Not carried into the draft: `fixtures/notes/memo.txt` claims churn fell to
  5.9%, but `fixtures/metrics.csv` ends at 6.8% (month 9). The draft made no
  churn claim, so no correction was needed in the body; the memo should not be
  used as a source.
