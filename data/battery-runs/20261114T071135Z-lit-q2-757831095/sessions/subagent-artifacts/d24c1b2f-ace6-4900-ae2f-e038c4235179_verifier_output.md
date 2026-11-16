Verification complete. `runs/p6/answer.md` written.

**What I found in the draft vs. fixtures:**

| Claim | Verdict |
|---|---|
| Throughput +32% (1,000→1,320 req/s) | ✅ Supported by `fixtures/notes/bench.txt` → cited [1] |
| Median latency fell to 41 ms after cache change | ❌ No latency or cache data in any fixture → removed, left as TODO |
| Error rate 2.0% → 1.1% | ❌ Wrong figure; `metrics.csv` shows 2.0 → **1.7** → corrected and cited [2] |
| "same window" | ⚠️ Re-scoped — error series (months 1–9) is not demonstrably the bench window |

No web sources/URLs were involved, so no link or DOI checks applied. Citation integrity confirmed: body cites [1],[2]; Sources lists exactly [1],[2]; no orphans either direction. A `Removed Unsupported Claims` section documents every deletion/correction.

**Residual risk worth flagging:** `fixtures/notes/memo.txt` says churn fell to **5.9%** by month 9, but `fixtures/metrics.csv` shows **6.8%** at month 9. The draft makes no churn claim, so this didn't affect the output — but the two fixtures disagree and the memo may be stale or refer to a different metric definition.