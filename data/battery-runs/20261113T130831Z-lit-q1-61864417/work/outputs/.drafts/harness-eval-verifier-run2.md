# Benchmark validity in agent evaluation: a short brief

Agent benchmarks are widely used to track progress on AI agents, but many have issues in task setup or reward design [1]. Zhu et al. introduce the Agentic Benchmark Checklist (ABC), a set of guidelines synthesized from benchmark-building experience, a survey of best practices, and previously reported issues [1]. Applied to CVE-Bench, a benchmark with a particularly complex evaluation design, ABC reduces performance overestimation by 33% [1].

Miller (2024) argues that the evaluation literature has largely ignored the statistical methods other experimental sciences use to analyze and plan experiments [2]. He treats evaluations as experiments and sets out formulas for analyzing evaluation data, comparing models, and planning an evaluation, rather than relying on single point scores [2]. OpenAI's audit of SWE-bench Verified found that 59.4% of the 138 audited problems contained material issues in test design and/or problem description [3].

## Sources

1. Yuxuan Zhu et al., "Establishing Best Practices in Building Rigorous Agentic Benchmarks", NeurIPS 2025 Datasets & Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2025/hash/f316275b44ee2de533102913828a8107-Abstract-Datasets_and_Benchmarks_Track.html
2. Evan Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations", arXiv:2411.00640, 2024. https://arxiv.org/abs/2411.00640
3. OpenAI, "Why we no longer evaluate SWE-bench Verified", 2026-02-23. https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/

## Removed Unsupported Claims

- The draft's "63%" reduction in performance overestimation on CVE-Bench was corrected to **33%**, the figure stated in the paper's abstract [1].
- The claim that Zhu et al. evaluate their checklist on "ten widely used agentic benchmarks" was softened: the live NeurIPS abstract does not state a count of ten, describing only application to CVE-Bench.
- The paragraph on citation hygiene was removed in full. It attributed a 41% figure to "Smith et al. (2024), 'Citation Drift in Agent Benchmarks', arXiv:2411.99999"; arXiv:2411.99999 has no record, and no paper matching that title and claim was found.
- The claim that "Feynman's verifier catches 92% of fabricated citations" was removed: no supporting source exists in the research notes or public record.
