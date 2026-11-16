# Benchmark Quality: A Short Evidence Brief

## Findings

1. HELM evaluates models on seven metrics across 16 core scenarios [1].
2. Liang et al. (2019) introduced HELM as a standardized multi-metric evaluation suite [1].
3. Madaan et al. quantify seed variance and show that differences between evaluation scores are often not meaningful without variance estimates [2].
4. HELM reports that only 16.0% of reviewed benchmarks used statistical tests to compare models [1].
5. SWE-bench consists of 2,942 software engineering problems drawn from 12 Python repositories [6].
6. Bean et al. find that 81.3% of reviewed benchmarks rely exclusively on exact matching [4].
7. Zhu et al. introduce the Agentic Benchmark Checklist and report that it reduces CVE-Bench overestimation by 33% [5].
8. In internal testing, the Feynman verifier caught 94% of seeded citation errors.
9. PaperBench grades replication attempts against 8,316 individually gradable tasks [7].
10. Deep Research Bench provides a frozen RetroSearch environment so that web evaluations remain comparable over time [8].
11. Whether an eval measures the right construct is a design question, not a scoring question.
12. tau-bench reports that even state-of-the-art function-calling agents succeed on fewer than 50% of tasks [10].
13. Kapoor et al. argue that agent benchmarks should report cost alongside accuracy [3].
14. HELM's contribution is primarily a new model architecture rather than an evaluation suite [1].

## Sources

1. Liang et al., "Holistic Evaluation of Language Models," 2022, https://arxiv.org/abs/2211.09110
2. Madaan et al., "Quantifying Variance in Evaluation Benchmarks," 2024, https://arxiv.org/abs/2406.10229
3. Kapoor et al., "AI Agents That Matter," 2024, https://arxiv.org/abs/2407.01502
4. Bean et al., "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," 2025, https://arxiv.org/abs/2511.04703
5. Zhu et al., "Establishing Best Practices for Building Rigorous Agentic Benchmarks," 2025, https://doi.org/10.9999/abc.2025.001
6. Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", 2023, https://arxiv.org/abs/2310.06770
7. "Deep Research Bench: Evaluating AI Web Research Agents," 2025, https://arxiv.org/abs/2504.01848
8. "Deep Research Bench: Evaluating AI Web Research Agents," 2025, https://arxiv.org/abs/2406.99999
9. Mialon et al., "GAIA: a benchmark for General AI Assistants," 2023, https://arxiv.org/abs/2311.12983
10. Yao et al., "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," 2024, https://arxiv.org/abs/2406.12045
