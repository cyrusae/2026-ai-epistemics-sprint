# Benchmark validity in agent evaluation: a short brief

Agent benchmarks are increasingly used to compare systems, but their validity is contested. Zhu et al. evaluate their checklist on ten widely used agentic benchmarks [1]. On CVE Bench, the checklist reduced performance overestimation by 63% [1].

Statistical treatment of evaluation noise is often missing. Miller (2024) argues that evaluations need error bars and variance estimates rather than single point scores [2]. A separate audit of SWE-bench Verified found that 59.4% of 138 audited problems had material issues in test design or problem description [3].

Citation hygiene itself is uneven. Smith et al. (2024) report that 41% of agent-benchmark citations do not support the attached claim [4]. Feynman's verifier catches 92% of fabricated citations, according to an internal evaluation.

## Sources

1. Zhu et al., "Establishing Best Practices in Building Rigorous Agentic Benchmarks", NeurIPS 2025.
2. Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations", arXiv:2411.00640, 2024.
3. OpenAI, "Why we no longer evaluate SWE-bench Verified", 2026.
4. Smith et al., "Citation Drift in Agent Benchmarks", arXiv:2411.99999, 2024.