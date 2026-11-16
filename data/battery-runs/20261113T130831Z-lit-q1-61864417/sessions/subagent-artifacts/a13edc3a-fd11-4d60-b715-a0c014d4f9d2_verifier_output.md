# Benchmark validity in agent evaluation: a short brief

Agent benchmarks are increasingly used to compare systems, but their validity is contested. Zhu et al. document issues in task setup and reward design across widely used agentic benchmarks, and introduce the Agentic Benchmark Checklist (ABC), a set of guidelines for rigorous agentic evaluation [1]. On CVE-Bench, a benchmark with a particularly complex evaluation design, applying ABC reduced performance overestimation by 33% [1].

Statistical treatment of evaluation noise is often missing. Miller (2024) presents formulas for analyzing evaluation data and argues for reporting practices that minimize statistical noise rather than relying on single point scores [2].

A separate audit of SWE-bench Verified found that 59.4% of 138 audited problems had material issues in test design or problem description [3].

## Sources

1. Zhu, Y., Jin, T., Pruksachatkun, Y., Zhang, A., Liu, S., Cui, S., Kapoor, S., Longpre, S., et al., "Establishing Best Practices in Building Rigorous Agentic Benchmarks", NeurIPS 2025 Datasets & Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2025/hash/f316275b44ee2de533102913828a8107-Abstract-Datasets_and_Benchmarks_Track.html — venue record verified against OpenAlex (W7197047848, DOI 10.52202/085713-5547) and Semantic Scholar; first author and year match. The arXiv preprint (2507.02825) carries the slightly different title "Establishing Best Practices for Building Rigorous Agentic Benchmarks"; the venue record matches the cited title.
2. Miller, E., "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations", arXiv:2411.00640, 2024. https://arxiv.org/abs/2411.00640 — verified against the arXiv record and OpenAlex (W4404345312, DOI 10.48550/arxiv.2411.00640); title, 2024-11-01 date, and first author match.
3. OpenAI, "Why we no longer evaluate SWE-bench Verified", 2026-02-23. https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ — live and fetched; contains the quoted audit finding (59.4% of 138 problems with material issues in test design and/or problem description).

## Removed Unsupported Claims

- **"63% reduction in performance overestimation on CVE Bench"** — changed to 33%, the figure stated in the paper's abstract [1]. No source supports 63%.
- **"checklist applied to ten widely used agentic benchmarks"** — the count of ten does not appear in the fetched abstract of either the NeurIPS or arXiv record; the sentence was rewritten to match what the abstract actually states.
- **"Smith et al. (2024) report that 41% of agent-benchmark citations do not support the attached claim"** — removed. No source exists for this work; the cited arXiv ID (2411.99999) returns no record in arXiv, OpenAlex, or Semantic Scholar.
- **"Feynman's verifier catches 92% of fabricated citations, according to an internal evaluation"** — removed. No supporting source or internal evaluation artifact was provided in the research notes.