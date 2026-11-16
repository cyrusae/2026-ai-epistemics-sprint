# Eval-claim audit — "Reflexion achieves 91% pass@1 on HumanEval, beating GPT-4's 80%"

**Verdict.** The two numbers are real and traceable, but the sentence is **not a like-for-like comparison** and should not be repeated as written. The 91% is the *task success rate of a multi-turn agent given up to 10 sequential attempts per problem with self-generated unit-test gating and self-reflection*; the 80% is a *single greedy sample* from GPT-4 under the Reflexion authors' own prompt/harness. The method is real and the gain is statistically detectable, but it is bought with roughly 10× the sampling budget plus test-generation and reflection calls. Separately, "GPT-4's 80%" is not a stable, citable property of GPT-4: OpenAI's own report says **67.0%** for zero-shot HumanEval, another contemporaneous paper says **82%**, and a third harness reports **88.4%** — all for "GPT-4".

---

## 1. The exact numbers and primary sources

| Claim | Paper | Value | Where |
|---|---|---|---|
| Reflexion HumanEval (Python) | Shinn et al., **arXiv:2303.11366** (v4, 10 Oct 2023; NeurIPS 2023) | **91.0** | Table 1, §4.3; abstract says "91%" |
| GPT-4 "SOTA" HumanEval (Python) | same | **80.1** | Table 1, §4.3; abstract says "80%" |
| Previous SOTA | same | 65.8 (CodeT + GPT-3.5) | Table 1 |

**Abstract, verbatim** [1]:
> "For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%."

**Table 1, verbatim rows** (arXiv:2303.11366v4) [1]:
> | Benchmark + Language | Prev SOTA Pass@1 | SOTA Pass@1 | Reflexion Pass@1 |
> | HumanEval (PY) | 65.8 (CodeT [5] + GPT-3.5) | 80.1 (GPT-4) | 91.0 |
> | HumanEval (RS) | – | 60.0 (GPT-4) | 68.0 |
> | MBPP (PY) | 67.7 (CodeT [5] + Codex [6]) | 80.1 (GPT-4) | 77.1 |
> | MBPP (RS) | – | 70.9 (GPT-4) | 75.4 |
> | Leetcode Hard (PY) | – | 7.5 (GPT-4) | 15.0 |
>
> Table 1: Pass@1 accuracy for various model-strategy-language combinations. The base strategy is a single code generation sample. All instruction-based models follow zero-shot code generation. [1]

Two provenance defects are visible in the primary source:
- **"80.1 (GPT-4)" carries no citation.** I inspected the arXiv HTML: the `<td>` for the HumanEval (PY) 80.1 and for MBPP (PY) 80.1 contain no `<cite>` element, while the neighbouring "65.8 (CodeT [5] ...)" does. So the origin of 80.1 is unattributed in the paper [1].
- **The same 80.1 is reported for two different benchmarks** (HumanEval and MBPP) — an exact coincidence for a 164-problem and a 427-problem suite that invites suspicion of a copy/rounding artefact [1]. (MBPP problem count not verified here; flag as inference.)

The GPT-3.5 neighbour 65.8 is exactly the "CodeT + GPT-3.5 [57]" entry in the GPT-4 Technical Report's own benchmark table [2], so the Reflexion authors were demonstrably reading that table when filling in this row — which makes the uncited 80.1 (rather than the 67.0 printed two cells away) more notable. (Inference from the matching value; not stated by the authors.)

---

## 2. What evaluation protocol produced the "GPT-4 80%" figure

It was produced **by the Reflexion authors**, using their own code, prompt and harness — not by OpenAI. Evidence, in decreasing order of directness:

1. **Table 2 of Reflexion** reports the baseline in the authors' own experiment: row HumanEval (PY) `Base 0.80 | Reflexion 0.91 | TP 0.99 | FN 0.40 | FP 0.01 | TN 0.60` [1]. The table caption calls these "Overall accuracy and test generation performance for HumanEval and MBPP" — i.e. measured in their pipeline.
2. **The released code defines the baseline.** `programming_runs/simple.py` — `run_simple()` generates one implementation via `gen.func_impl(item["prompt"], model, "simple")` and scores it with `exe.evaluate(..., item["test"])` against the official HumanEval tests; the generation wrapper defaults to **`temperature: float = 0.0`** (`generators/model.py`), i.e. a single greedy sample [3].
3. **The cited "SOTA" is that same base agent.** Table 1's caption: "The base strategy is a single code generation sample. All instruction-based models follow zero-shot code generation." [1]

So "GPT-4 = 80.1%" is: **GPT-4, zero-shot, one greedy sample per problem, generated with the Reflexion repo's "You are a programming assistant…" prompt (`SIMPLE_CHAT_INSTRUCTION`), scored on the 164 original HumanEval tests.** It is a valid measurement, but it is *their* measurement, and its quotability as "GPT-4's HumanEval score" ends at their harness.

**Direct check of the released artefacts (my recomputation, not the authors' statement):**

| File in `noahshinn/reflexion` | Content | Solved | Rate |
|---|---|---|---|
| `programming_runs/root/reflexion_humaneval_py_pass_at_1/reflexion_humaneval_py_pass_at_1.jsonl` | 164 problems, `is_solved` | 150 | **91.46%** (Wilson 95% CI 86.2–94.8%) |
| `programming_runs/root/simple_human_eval_py_logging/humaneval-py..gz_simple_1_gpt-4_pass_at_k_1_py.jsonl` | 164 problems, `is_solved` | 141 | **86.0%** (CI 79.8–90.5%) |
| First attempt inside the Reflexion log (problems with zero reflections) | 164 problems | 134 | **81.7%** (CI 75.1–86.9%) |

- The headline 91% **does** reproduce from the shipped log (150/164 = 91.5%, reported as 91.0 — a one-problem rounding gap) [3].
- The Reflexion log uses **up to 9 reflections = 10 attempts**: distribution of reflections per problem was {0: 134, 1: 7, 2: 2, 3: 1, 9: 20}, max 9 — consistent with the CLI default `--max_iters 10` in `main.py` [3].
- **16 of 164 problems (9.8%)** were solved only via reflection; **6 of those only on the 10th and final attempt** (the code force-evaluates on `cur_iter == max_iters - 1`). 134 problems (81.7%) were solved on attempt one, with no reflection at all [3, computed].
- **The shipped baseline log gives 86.0%, not 80.1%.** And the Reflexion run's own first attempts give 81.7%. Neither number in the repo reproduces 80.1% [3, computed].
- The two released logs disagree on **11 of 164 problems** (2×2: both 140, reflexion-only 10, simple-only 1, neither 13) despite both being greedy decoding — evidence of model-snapshot drift and/or API nondeterminism between runs [3, computed].

---

## 3. What the GPT-4 Technical Report says, and why it differs

**OpenAI's number is 67.0%, not 80%.** arXiv:2303.08774v6, Table 2 (academic benchmarks), HumanEval row, verbatim [2]:
> "HumanEval [43] 67.0% 48.1% 26.2% 65.8% Python coding tasks 0-shot 0-shot 0-shot PaLM [3] CodeT + GPT-3.5 [57]"

i.e. **GPT-4 = 67.0% (0-shot), GPT-3.5 = 48.1% (0-shot)**, PaLM = 26.2%, CodeT+GPT-3.5 = 65.8%. No temperature or n-samples footnote is given for HumanEval; the only protocol label is "0-shot" [2]. Contamination is also disclosed (Table 11, verbatim): `HumanEval 67.0% 48.1% 25% 65.58% -2.12%` — an estimated ~25% contamination, 65.58% on the non-contaminated subset [2].

**Why the figures differ so much (67 vs 80 vs 82 vs 88):**

| Source | GPT-4 HumanEval pass@1 | Protocol as documented |
|---|---|---|
| OpenAI tech report (**2303.08774**) [2] | **67.0%** | 0-shot, OpenAI's own prompt/scoring harness, pre-release snapshot |
| "Sparks of AGI" (**2303.12712**) [4] | **82%** | Table 1 "Zero-shot pass@1 accuracy comparison of different models on HumanEval": GPT-4 82%, text-davinci-003 65%, Codex 39%, CodeGen-16B 30% |
| Reflexion baseline (**2303.11366**) [1] | **80.1%** | 0-shot, single greedy sample, Reflexion's prompt, official tests |
| Reflexion released simple log [3] | **86.0%** | same harness, different run/snapshot |
| EvalPlus / HumanEval+ (**2305.01210**) [5] | **88.4%** base, **76.2%** on HumanEval+ | greedy decoding (`pass@1*`), EvalPlus harness with 80× more tests |

Prompt format, stopping rule, temperature, test-suite strength, and **which GPT-4 snapshot** all move this metric by 10–20 points. Sparks of AGI attaches an explicit disclaimer [4]: "our experiments were run on an early version of GPT-4. In particular all quantitative results will be different on the final version of GPT-4." The GPT-4 report itself documents per-benchmark snapshot differences (Appendix A.7) [2], and the EvalPlus maintainers publicly note that "'ChatGPT' and 'GPT4' [are] a product whose internal implementation can change over time" [5]. My own recomputation above (86.0 vs 81.7 on the same 164 items, greedy) shows this drift inside a single repo [3].

---

## 4. Is 91% vs 80% like-for-like? No. Caveats an auditor should attach

**Short answer: no.** It compares a 10-attempt agentic process against a 1-sample baseline, and it compares two different harnesses' numbers as if they were the same measurement.

**C1 — Budget asymmetry (the decisive caveat).** Reflexion's "pass@1" is the fraction of problems solved *at any point* within up to 10 sequential attempts, each with a self-written test suite (≤6 tests), a self-reflection call, and a regenerated implementation; `run_reflexion` sets `is_solved` and exits on success [3]. The baseline is one greedy sample. Per-problem cost is roughly 10 generation calls + ~10 reflection calls + 10 test-generation calls at the ceiling. This is closer to "pass@1 under a fixed agentic budget" than to Chen et al.'s pass@1. HumanEval's own definition [6]: "k code samples are generated per problem, a problem is considered solved if any sample passes the unit tests" — with pass@1 estimated from n=200 samples per task. Reflexion reports a single deterministic trajectory per problem, which is a *different estimator* (no unbiased pass@k correction, one trajectory).
  - The fair control is **compute-matched**: N i.i.d. GPT-4 samples per problem, selected with the same non-oracle rule. Olausson et al. (arXiv:2306.09896) do exactly this for self-repair on HumanEval/APPS: "when the cost of carrying out repair is taken into account, performance gains are often modest, vary a lot between subsets of the data, and are sometimes not present at all," and they ask "whether you would—at an equivalent compute budget—have had a greater chance of success if you had simply drawn more code samples i.i.d." [7]. Reflexion reports no such control.
- **C2 — The gain is concentrated in a small number of items.** 150 vs 141 (repo baseline) or 150 vs 134 (first attempts): +6 to +16 problems out of 164. Each problem is 0.61 pp, so "91% vs 80%" = 18 problems. My Wilson CIs: 86.2–94.8% vs 75.1–86.9% (first-attempt baseline) and 79.8–90.5% (shipped baseline log) — overlapping at the shipped-baseline comparison [3, computed]. Paired tests: 16 improvements/0 regressions → exact McNemar p ≈ 3×10⁻⁵; against the shipped baseline log, 10 improvements/1 regression → p ≈ 0.012 [3, computed]. Statistically detectable, but the *effect size* rests on ~10 problems.
- **C3 — Self-generated-test selection is a partly invalid verifier.** The agent stops and submits when its *own* tests pass; official HumanEval tests then judge it. Reflexion's own Table 2 measures the false-positive rate: HumanEval (PY) `FP 0.01` and, in §4.3, "the false positive test execution rate for MBPP Python is 16.3% while the rate for HumanEval Python is a mere 1.4%, leading to 91% overall accuracy" [1]. A 1.4% FP rate on 164 problems is ~2 problems; small but nonzero, and it is measured by the authors alone.
- **C4 — Internal inconsistency of the baseline in the same paper.** Three different GPT-4 HumanEval baselines appear: **80.1** (Table 1), **0.80** (Table 2 "Base"), and **82%** in §4.3 prose ("For HumanEval and MBPP Python, the baseline pass@1 accuracies are relatively similar, 82% and 80%, respectively") [1]. The abstract quotes "80%". An auditor cannot tell which run the abstract refers to; my log recomputation gives 86.0% and 81.7% [3]. The 82% prose value also conflicts with Table 2's 0.80 for the *same* table.
- **C5 — Evaluator weakness inflates both sides.** Original HumanEval has "an average of 7.7 tests per problem" [6]; EvalPlus adds 80× tests and reports "over 10% of them [ground-truth solutions] are incorrectly implemented" and pass@k reductions of 19.3–28.9%, with GPT-4 dropping 88.4% → 76.2% [5]. Neither 91% nor 80% is measured with an adequate test suite; the comparison's *sign* is probably robust, its *size* is not.
- **C6 — Contamination.** HumanEval is public and old; OpenAI estimates ~25% HumanEval contamination for GPT-4 with a 65.58% non-contaminated score (Table 11) [2]. Reflexion reports no contamination analysis for either arm.
- **C7 — Model drift / unrecorded snapshot.** Neither the paper nor the log filenames record a GPT-4 snapshot [1, 3]. The repo's own two greedy runs differ on 11/164 items [3]. "GPT-4's 80%" and "Reflexion's 91%" are not reproducible point values today, even by the authors' own code.
- **C8 — Benchmark-specific scope.** Reflexion loses to its own GPT-4 baseline on MBPP (77.1 vs 80.1) in the same table [1], and on a weak model (starchat-beta) Reflexion gives no gain at all ("Baseline 0.26 / Reflexion 0.26", Table 4 [1]). Any generalisation to "Reflexion beats GPT-4" must be scoped to HumanEval-Python with a strong model.

**Suggested corrected sentence:** *"Shinn et al. (arXiv:2303.11366) report that a GPT-4 Reflexion agent solves 91% of HumanEval-Python problems within up to 10 self-reflective attempts, versus 80% (their own harness; 67% in OpenAI's technical report) for a single greedy GPT-4 sample — a gain concentrated in ~10–16 of 164 problems and obtained at roughly 10× the sampling cost, with no compute-matched i.i.d. control."*

---

## 5. Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|---|---|---|---|---|
| 1 | Shinn et al., Reflexion, arXiv:2303.11366v4 (NeurIPS 2023) | https://arxiv.org/abs/2303.11366 ; https://arxiv.org/html/2303.11366v4 | Abstract "91% … GPT-4 that achieves 80%"; Table 1 HumanEval(PY) 80.1 (GPT-4) → 91.0; Table 2 Base 0.80; §4.3 prose "82% and 80%"; FP rate 1.4% HumanEval vs 16.3% MBPP | primary | high (read directly) |
| 2 | OpenAI, GPT-4 Technical Report, arXiv:2303.08774v6 | https://arxiv.org/abs/2303.08774 ; https://arxiv.org/html/2303.08774v6 | Table 2 HumanEval: GPT-4 67.0%, GPT-3.5 48.1%, 0-shot; Table 11: 25% contamination, 65.58% non-contaminated | primary | high (read directly) |
| 3 | noahshinn/reflexion code + released logs | https://github.com/noahshinn/reflexion | `simple.py` (1 greedy sample baseline), `reflexion.py` (≤10 attempts, internal-test gating), `model.py` temperature 0.0, `main.py --max_iters 10`; logs 150/164 and 141/164 | primary (artefact) | high (code read; logs recomputed by me) |
| 4 | Bubeck et al., Sparks of AGI, arXiv:2303.12712v5 | https://arxiv.org/abs/2303.12712 | Table 1 "Zero-shot pass@1 … on HumanEval": GPT-4 82%; early-version disclaimer | primary | high (table row read) |
| 5 | Liu et al., EvalPlus, arXiv:2305.01210 (NeurIPS 2023) | https://arxiv.org/abs/2305.01210 | HumanEval+ 80× tests; >10% ground truths wrong; GPT-4 88.4% base → 76.2% +extra | primary | high |
| 6 | Chen et al., HumanEval/Codex, arXiv:2107.03374 | https://arxiv.org/abs/2107.03374 | 164 problems, "average of 7.7 tests per problem"; pass@k definition and unbiased estimator | primary | high |
| 7 | Olausson et al., Is Self-Repair a Silver Bullet?, arXiv:2306.09896 (ICLR 2024) | https://arxiv.org/abs/2306.09896 | Compute-matched critique: gains "often modest … sometimes not present at all" at equal budget; i.i.d. control | primary | high |
| 8 | Huang et al., LLMs Cannot Self-Correct Reasoning Yet, arXiv:2310.01798 (ICLR 2024) | https://arxiv.org/abs/2310.01798 | LLMs struggle to self-correct without external feedback (scope: reasoning, not code) | primary | high (abstract only) |

---

## 6. Findings

**Q1 — exact numbers and primary sources.** Reflexion = 91.0 on HumanEval-Python, GPT-4 = 80.1 in the same table; both in Table 1 of arXiv:2303.11366v4, and both quoted in the abstract as "91%" and "80%" [1]. The 80.1 cells carry **no citation** in the HTML source, and the identical value 80.1 is used for both HumanEval and MBPP [1, verified in HTML]. GPT-4's own report says 67.0% [2].

**Q2 — what produced the GPT-4 80%.** The Reflexion authors' own baseline: one zero-shot greedy sample per problem (`temperature=0.0`), their prompt template, scored on official HumanEval tests [1, 3]. Table 2 labels it "Base 0.80" and Table 1's caption states "The base strategy is a single code generation sample" [1]. It is not an OpenAI figure.

**Q3 — what the GPT-4 report says.** 67.0% zero-shot, 48.1% for GPT-3.5, with 0-shot the only protocol label and a 25%-contamination disclosure (non-contaminated 65.58%) [2]. The 13-point gap to Reflexion's 80.1 has no stated cause; the plausible causes are prompt format, stopping rule, temperature/sampling, test-suite/scoring details, and model snapshot (inference). Corroborating the "harness matters" explanation: Sparks of AGI reports 82% on the same benchmark with an early GPT-4 and its own prompt, with an explicit version disclaimer [4]; EvalPlus reports 88.4% under greedy decoding with its own harness [5]; the Reflexion repo's own greedy baseline log shows 86.0% [3].

**Q4 — like-for-like?** No. Four independent mismatches: (i) **sampling budget** — up to 10 sequential attempts + reflections + generated tests vs 1 sample (verified in `reflexion.py`/`main.py`, and in the released log's reflection counts) [3]; (ii) **selection rule** — self-written tests decide when to stop, with an author-measured 1.4% HumanEval false-positive rate [1]; (iii) **baseline provenance/number instability** — three different baselines in one paper (80.1, 0.80, 82%) and two more in the repo (86.0, 81.7) [1, 3]; (iv) **evaluator adequacy and contamination** — 7.7 tests per problem, >10% bad ground truths, ~25% contamination [2, 5, 6]. The paired gain is significant (16 vs 0 discordant, McNemar p≈3×10⁻⁵) but amounts to ~16 problems, with Wilson CIs that overlap against the shipped 86.0% baseline [3, computed]. No compute-matched i.i.d. control is reported, which is precisely the control Olausson et al. show to be necessary [7].

---

## 7. Coverage status

**Checked directly (read the artefact):**
- Reflexion arXiv:2303.11366 abstract, Table 1, Table 2, Table 4, §4.3 prose, and HTML citation markup for the 80.1 cells.
- Reflexion GitHub: `README.md`, `main.py`, `simple.py`, `reflexion.py`, `generators/model.py`, `generators/py_generate.py`; downloaded and recomputed both HumanEval-Python logs (164 rows each).
- GPT-4 Technical Report v6: Table 2 HumanEval row, Table 11 contamination row, Appendix A.7 snapshot note, Table 2 caption.
- Sparks of AGI v5: Table 1 HumanEval row (82/65/39/30) and the early-version disclaimer (via PDF read).
- EvalPlus (2305.01210) abstract and NeurIPS PDF table (GPT-4 88.4 base / 76.2 +extra; >10% incorrect ground truths).
- HumanEval (2107.03374): 164 problems, 7.7 tests/problem, pass@k definition and unbiased estimator.
- Olausson et al. abstract and the equal-budget argument paragraph.

**Not checked / uncertain:**
- Where exactly "80.1" came from. It is uncited in the paper; I did not find a third-party source reporting 80.1 with matching protocol. **Unresolved.**
- Whether the paper's 91.0 came from the same run as the released log (log yields 91.5%); whether an averaging over trials produced 91.0. **Unresolved; minor.**
- The exact GPT-4 snapshot(s) used for either arm; not recorded in paper or filenames. **Unresolved and material.**
- MBPP's problem count (427) — asserted from memory, not verified; the "identical 80.1 on two benchmarks" point stands regardless.
- Sparks of AGI's exact HumanEval prompt text — not extractable from the PDF slice I read.
- The `test_acc.py` internal-test accuracy computation (Table 2's TP/FN/FP/TN) was not re-run.

**Tasks I could not complete:** none from the brief. All four questions answered.

---

## Sources

1. Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao — *Reflexion: Language Agents with Verbal Reinforcement Learning* — https://arxiv.org/abs/2303.11366 (v4 HTML: https://arxiv.org/html/2303.11366v4)
2. OpenAI — *GPT-4 Technical Report* — https://arxiv.org/abs/2303.08774 (v6 HTML: https://arxiv.org/html/2303.08774v6)
3. Noah Shinn et al. — *Reflexion* repository (code and logs) — https://github.com/noahshinn/reflexion ; baseline log https://github.com/noahshinn/reflexion/blob/main/programming_runs/root/simple_human_eval_py_logging/humaneval-py..gz_simple_1_gpt-4_pass_at_k_1_py.jsonl ; reflexion log https://github.com/noahshinn/reflexion/blob/main/programming_runs/root/reflexion_humaneval_py_pass_at_1/reflexion_humaneval_py_pass_at_1.jsonl
4. Sébastien Bubeck et al. — *Sparks of Artificial General Intelligence: Early experiments with GPT-4* — https://arxiv.org/abs/2303.12712
5. Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, Lingming Zhang — *Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of LLMs for Code Generation* (EvalPlus / HumanEval+) — https://arxiv.org/abs/2305.01210
6. Mark Chen et al. — *Evaluating Large Language Models Trained on Code* (HumanEval) — https://arxiv.org/abs/2107.03374
7. Theo X. Olausson, Jeevana Priya Inala, Chenglong Wang, et al. — *Is Self-Repair a Silver Bullet for Code Generation?* — https://arxiv.org/abs/2306.09896
8. Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Paper P — *Large Language Models Cannot Self-Correct Reasoning Yet* — https://arxiv.org/abs/2310.01798
