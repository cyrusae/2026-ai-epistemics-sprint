**Summary:** `experiments/verifier-probe/verified2.md` written — one fabricated statistic removed, two dead/fake identifiers replaced with the correct papers, one misattributed statistic re-attributed to a newly verified source, and one title/ID mismatch corrected; all 8 final URLs return HTTP 200 and all citation/source numbers reconcile (no orphans either direction).

**Corrected**
- Finding 2: SWE-bench problem count 2,942 → **2,294** (abstract), 12 repos unchanged.
- Finding 4: 16.0% statistic detached from HELM and re-attributed to **Bean et al. [8]** with the paper's exact wording ("used uncertainty estimates or statistical tests") and n=445.
- Finding 6 / source 5: source titled "Deep Research Bench…" at arXiv:2504.01848 → corrected to **Starace et al., "PaperBench…"**; 8,316 tasks confirmed in that abstract.

**Removed**
- Finding 7 ("Feynman verifier caught 94% of seeded citation errors") — no source or artifact; findings renumbered to 1–9.

**Replaced (dead/fake identifiers)**
- Source 3: DOI `10.9999/abc.2025.001` (HTTP 404, unregistered) → arXiv:2507.02825 (Zhu et al.; title/author/33% match; NeurIPS venue record W7197047848 uses "…**in** Building…" variant — flagged).
- Source 4: arXiv:2406.99999 (HTTP 404) → arXiv:**2506.06287** (FutureSearch/Bosse et al.), which confirms the frozen RetroSearch claim; claim retained.

**Flagged / notes**
- All entries cross-checked against arXiv + OpenAlex (Semantic Scholar was rate-limited); all URLs fetched 200 on 2026-11-14.
- Residual: finding 1 states "seven metrics across 16 core scenarios" without HELM's "when possible (87.5% of the time)" qualifier — retained as a fair summary.