# Benchmark Quality: A Short Evidence Brief

## Findings

1. HELM evaluates models on seven metrics across 16 core scenarios [1].
2. Liang et al. (2022) introduced HELM as a standardized multi-metric evaluation suite [1].
3. Madaan et al. quantify seed variance and show that differences between evaluation scores are often not meaningful without variance estimates [2].
4. Bean et al. report that only 16.0% of the 445 benchmarks they reviewed used uncertainty estimates or statistical tests to compare models [4].
5. SWE-bench consists of 2,294 software engineering problems drawn from 12 Python repositories [6].
6. Bean et al. find that 81.3% of reviewed benchmarks use exact matching at least partially, while 40.7% rely on it exclusively [4].
7. Zhu et al. introduce the Agentic Benchmark Checklist and report that it reduces CVE-Bench overestimation by 33% [5].
8. PaperBench grades replication attempts against 8,316 individually gradable tasks [7].
9. Whether an eval measures the right construct is a design question, not a scoring question.
10. tau-bench reports that even state-of-the-art function-calling agents succeed on fewer than 50% of tasks [8].
11. Kapoor et al. argue that agent benchmarks should report cost alongside accuracy [3].

## Sources

1. Liang et al., "Holistic Evaluation of Language Models," 2022, https://arxiv.org/abs/2211.09110
2. Madaan et al., "Quantifying Variance in Evaluation Benchmarks," 2024, https://arxiv.org/abs/2406.10229
3. Kapoor et al., "AI Agents That Matter," 2024, https://arxiv.org/abs/2407.01502
4. Bean et al., "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," 2025, https://arxiv.org/abs/2511.04703
5. Zhu et al., "Establishing Best Practices for Building Rigorous Agentic Benchmarks," 2025, https://arxiv.org/abs/2507.02825
6. Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", 2023, https://arxiv.org/abs/2310.06770
7. Starace et al., "PaperBench: Evaluating AI's Ability to Replicate AI Research," 2025, https://arxiv.org/abs/2504.01848
8. Yao et al., "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," 2024, https://arxiv.org/abs/2406.12045

## Removed Unsupported Claims

- **Draft finding 8** ("In internal testing, the Feynman verifier caught 94% of seeded citation errors"): no source, artifact, or note in the research file supports this figure; removed.
- **Draft finding 10** (Deep Research Bench "frozen RetroSearch environment"): its only citation was draft source 8, `https://arxiv.org/abs/2406.99999`, which returns HTTP 404 and has no documented alternative in the research file; removed.
- **Draft finding 14** ("HELM's contribution is primarily a new model architecture rather than an evaluation suite"): contradicted by [1], which presents HELM as an evaluation suite; removed.
- **Draft source 9** (Mialon et al., GAIA): orphan source, never cited in the body; removed.

Findings and sources were renumbered contiguously after these deletions (draft findings 9→8, 11→9, 12→10, 13→11; draft source 10→8).

## Citation Corrections (flagged)

- **Draft finding 2:** year corrected from 2019 to 2022 (arXiv v1 November 2022; TMLR 2023).
- **Draft finding 4:** the 16.0% statistic was attributed to HELM [1]; it comes from Bean et al. [4], whose review reports "16.0% used uncertainty estimates or statistical tests to compare the results." Re-attributed.
- **Draft finding 5:** problem count corrected from 2,942 to 2,294, per the SWE-bench abstract.
- **Draft finding 6:** "81.3% ... rely exclusively on exact matching" misread the source; the paper reports 81.3% at least partially and 40.7% exclusively. Corrected.
- **Draft source 5:** DOI `10.9999/abc.2025.001` resolves to HTTP 404 and is not a registered DOI; replaced with `https://arxiv.org/abs/2507.02825`. Note that the OpenAlex venue record (W7197047848, NeurIPS 2025) carries the title variant "Establishing Best Practices in *Building* Rigorous Agentic Benchmarks"; first author and content match the arXiv record.
- **Draft source 7:** the title "Deep Research Bench: Evaluating AI Web Research Agents" did not match arXiv:2504.01848, which is PaperBench (Starace et al., 2025). Title corrected and author added; the 8,316-task figure is confirmed in that paper's abstract.