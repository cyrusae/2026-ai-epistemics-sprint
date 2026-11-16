Audit complete. Result written to `eval-run/runs/p6/answer.md`.

**Findings:**
- **32% throughput** — supported by `fixtures/notes/bench.txt` (baseline 1,000 → 1,320 req/s; recomputed 32.0%). Kept, path cited.
- **41 ms median latency** — no support anywhere in the fixtures (only match was the draft itself). Removed from the body and explicitly marked as withdrawn with a TODO rather than silently dropped.
- **Error rate 2.0% → 1.1%** — start value correct, end value contradicted: `metrics.csv` ends at **1.7%** in month 9. Corrected, path cited.
- **"Same window"** — softened: `bench.txt` is dated 2026-10-30, `metrics.csv` is indexed by months 1–9.
- **Incidental conflict:** `memo.txt` says churn ends at 5.9%, `metrics.csv` says 6.8%. No churn numbers appear in the draft; flagged so it isn't picked up uncritically later.