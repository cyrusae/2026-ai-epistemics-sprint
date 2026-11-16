# Research notes for verifier fixture

Source [1] — "Establishing Best Practices in Building Rigorous Agentic Benchmarks", NeurIPS 2025 Datasets & Benchmarks Track.
URL: https://proceedings.neurips.cc/paper_files/paper/2025/hash/f316275b44ee2de533102913828a8107-Abstract-Datasets_and_Benchmarks_Track.html
Exact abstract text (verified 2026-11-13): "We apply ABC on ten widely used agentic benchmarks... When applied to CVE Bench, a benchmark with a particularly complex evaluation design, ABC reduces performance overestimation by 33%."

Source [2] — Evan Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations", 2024.
arXiv: 2411.00640
URL: https://arxiv.org/abs/2411.00640
Metadata verified 2026-11-13: title and 2024/11/01 date match.

Source [3] — OpenAI, "Why we no longer evaluate SWE-bench Verified", 2026-02-23.
URL: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
Claim used: "we found that 59.4% of the 138 problems contained material issues in test design and/or problem description".
Note: this page returned HTTP 403 to a command-line fetch from this environment; the quoted text is from a search-provider retrieval, so treat it as source-reported but not independently re-fetched.

No source exists for:
- any paper with arXiv ID 2411.99999;
- the claim that Feynman's verifier catches 92% of fabricated citations;
- a 63% reduction in overestimation on CVE Bench (the source says 33%).
## Post-run correction (added 2026-11-13, after both verifier runs)

The sentence "We apply ABC on ten widely used agentic benchmarks" was originally
labelled above as abstract text. That label is wrong: the NeurIPS HTML abstract
(https://proceedings.neurips.cc/paper_files/paper/2025/hash/f316275b44ee2de533102913828a8107-Abstract-Datasets_and_Benchmarks_Track.html,
checked 2026-11-13) does not contain the count "ten"; the sentence appears in the
paper body (Section 5 excerpt captured in a search result). The original wording is
left intact so the record shows what the verifier subagents actually received.
Consequence: the verifier's removal of the ten-benchmark count is defensible and is
not scored as a failure in `grade.py`; it is reported as an ambiguous control.
