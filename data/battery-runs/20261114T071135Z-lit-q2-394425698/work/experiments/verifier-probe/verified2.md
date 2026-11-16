# Benchmark Quality: A Short Evidence Brief (v2)

## Findings

1. HELM evaluates models on seven metrics across 16 core scenarios [1].
2. SWE-bench consists of 2,294 software engineering problems drawn from 12 Python repositories [2].
3. Zhu et al. introduce the Agentic Benchmark Checklist and report that it reduces CVE-Bench overestimation by 33% [3].
4. Bean et al. report that only 16.0% of the 445 benchmarks they reviewed used uncertainty estimates or statistical tests to compare results [8].
5. Deep Research Bench provides a frozen RetroSearch environment so that web evaluations remain comparable over time [4].
6. PaperBench grades replication attempts against 8,316 individually gradable tasks [5].
7. Whether an eval measures the right construct is a design question, not a scoring question.
8. tau-bench reports that even state-of-the-art function-calling agents succeed on fewer than 50% of tasks [6].
9. Kapoor et al. argue that agent benchmarks should report cost alongside accuracy [7].

## Sources

1. Liang et al., "Holistic Evaluation of Language Models," 2022, https://arxiv.org/abs/2211.09110
2. Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", 2023, https://arxiv.org/abs/2310.06770
3. Zhu et al., "Establishing Best Practices for Building Rigorous Agentic Benchmarks," 2025, https://arxiv.org/abs/2507.02825
4. FutureSearch (Bosse et al.), "Deep Research Bench: Evaluating AI Web Research Agents," 2025, https://arxiv.org/abs/2506.06287
5. Starace et al., "PaperBench: Evaluating AI's Ability to Replicate AI Research," 2025, https://arxiv.org/abs/2504.01848
6. Yao et al., "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," 2024, https://arxiv.org/abs/2406.12045
7. Kapoor et al., "AI Agents That Matter," 2024, https://arxiv.org/abs/2407.01502
8. Bean et al., "Measuring what Matters: Construct Validity in Large Language Model Benchmarks," 2025, https://arxiv.org/abs/2511.04703

## Removed Unsupported Claims

- **Draft finding 7 of 10** ("In internal testing, the Feynman verifier caught 94% of seeded citation errors"): no source URL, note, or artifact in `draft2.md`/`sources2.md` supports this figure; removed. Findings were renumbered 8→7, 9→8, 10→9.

## Citation Corrections (flagged)

- **Draft finding 2:** problem count corrected from 2,942 to 2,294, per the SWE-bench abstract ("2,294 software engineering problems ... across 12 popular Python repositories"). The 12-repository figure was already correct.
- **Draft finding 3 / source 3:** DOI `10.9999/abc.2025.001` returns HTTP 404 and is not a registered DOI; replaced with `https://arxiv.org/abs/2507.02825`. Title, year (2025), first author (Yuxuan Zhu), and the 33% CVE-Bench overestimation-reduction figure all match the arXiv abstract. The NeurIPS 2025 venue record (OpenAlex W7197047848, DOI 10.52202/085713-5547) carries the near-identical title variant "Establishing Best Practices **in** Building Rigorous Agentic Benchmarks"; author and content match. Record used: arXiv 2507.02825.
- **Draft finding 4:** the 16.0% statistic was attributed to HELM [1], but HELM does not report a review of benchmarks. It comes from Bean et al., whose systematic review of 445 benchmarks states "16.0% used uncertainty estimates or statistical tests to compare the results." Re-attributed to a newly added source [8] (verified: arXiv 2511.04703; NeurIPS 2025 Datasets & Benchmarks record OpenAlex W4416268504). The claim was tightened to the paper's wording and sample size.
- **Draft finding 5 / source 4:** `https://arxiv.org/abs/2406.99999` returns HTTP 404 and has no matching paper. The claimed paper is real at a different identifier — arXiv 2506.06287 (FutureSearch/Bosse et al., 2025) — whose abstract confirms the frozen "RetroSearch" environment "enabling reliable evaluations of models over time." URL replaced; claim retained.
- **Draft finding 6 / source 5:** the source title "Deep Research Bench: Evaluating AI Web Research Agents" did not match arXiv:2504.01848, which is PaperBench (Starace et al., 2025). Title and first author corrected; the 8,316 individually gradable tasks figure is confirmed in that abstract.

## Verification notes

- All eight final URLs were fetched and returned HTTP 200 on 2026-11-14; each abstract page contains the cited title, year, and first author.
- Identifier cross-checks: arXiv abstract pages plus OpenAlex work records for every entry (`10.48550/arXiv.*` DOIs); Zhu et al. additionally checked against its NeurIPS 2025 venue record. Semantic Scholar lookups were rate-limited during this pass, so OpenAlex served as the second index.
