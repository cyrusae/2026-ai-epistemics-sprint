# Internal Review: "Sparse Routing for Efficient Retrieval"

**Reviewed artifact:** `experiments/feynman-eval-case-study/fixtures/mini-eval-paper.md` (26 lines, 6 sections)
**Review mode:** Adversarial empirical-rigor / evaluation-validity audit
**Review date:** 2026-11-13
**Recommendation:** Major revision; the central claims are not currently supported by the reported evidence.

---

## Summary

The paper proposes SparseRoute, a learned top-k routing layer over 64 experts, applied to long-context retrieval. The claimed result is an accuracy improvement from 80.1% to 80.3% together with a halving of latency (40 ms → 20 ms), evaluated on a held-out split of 100 examples from an unnamed benchmark, against a baseline the authors trained themselves. The paper asserts a new state of the art and recommends production adoption.

The contribution is presented at a level of detail below what is needed to assess it. There is no named dataset, no published comparison, no ablation, no confidence interval, no per-seed result, no latency measurement protocol, and no related-work positioning. Most consequentially, the two headline accuracy numbers are arithmetically impossible under the evaluation protocol the paper itself states (100 examples, 3 seeds, mean over seeds), and the reported effect is roughly two orders of magnitude below the resolution of that evaluation design. The paper is best read as an early internal result note; in its current form it does not support its abstract, its results interpretation, or its conclusion.

## Strengths

- **[S1]** The paper reports latency alongside accuracy rather than accuracy alone (Results table). For an efficiency-motivated routing method this is the right pair of metrics to report, and many short papers omit latency entirely.
- **[S2]** The evaluation uses a held-out split rather than reporting training-set accuracy (Evaluation section). This is a genuine, if minimal, attempt at a clean generalization estimate.
- **[S3]** The authors ran 3 seeds and report the mean rather than the best seed (Evaluation section). Reporting a seed mean is the correct instinct and is preferable to max-over-seeds reporting, which is common and misleading.
- **[S4]** The baseline is described as trained "with the same budget" (Evaluation section). Attempting compute parity with the baseline is the right control to attempt, even though the execution is under-specified (see W4).
- **[S5]** The claims in the Abstract and Results are numerically consistent with the Results table (80.1 → 80.3; 40 → 20 ms). There is no internal contradiction between prose and table, which is not nothing in a short draft.

## Weaknesses

- **[W1] FATAL — The "state of the art" claim has no referent.** The Abstract states the method "establishes a new state of the art," and the Conclusion repeats it. SOTA is a comparative claim against the best published results on a named benchmark. The paper names no benchmark, cites no published system, and compares only to a baseline the authors trained. A self-trained baseline is not a SOTA comparison under any reading; it is at best an internal ablation. There is no evidence in the paper that any external result was consulted.

- **[W2] FATAL — The reported accuracy means are arithmetically impossible under the stated protocol, and the effect size is below the design's resolution.** The Evaluation section states a 100-example held-out split, 3 seeds, and mean accuracy over seeds. Per-seed accuracy on 100 examples must be an integer count out of 100; the mean of three such values must therefore be a multiple of 1/300 ≈ 0.333 percentage points. The reported means, 80.1% and 80.3%, correspond to 240.3/300 and 240.9/300 — non-integer numerators, hence unattainable. Either the split is not 100 examples, or more than 3 runs are averaged, or the numbers were not produced by the described procedure. Any of these possibilities is a serious reporting problem, and the paper does not acknowledge it. Separately, a 0.2-point difference on 100 examples is 0.2 example predictions per seed (0.6 across three seeds), whereas the binomial standard error at p ≈ 0.8, n = 100 is ≈ 4.0 points and the approximate 95% minimum detectable unpaired difference is ≈ 11 points. The claimed gain is roughly 1/20th of one standard error. With no confidence interval (explicitly declined in the Evaluation section), the result is indistinguishable from seed noise.

- **[W3] FATAL — The 2× latency claim has no measurement protocol and a plausible confound.** The paper reports "40 ms" and "20 ms" with no hardware, batch size, sequence length, retrieval corpus size, percentile (mean vs p50 vs p95), warm-up, or repeat count. A routing layer over 64 experts adds computation and memory traffic; the paper never explains the mechanism by which adding a router halves end-to-end latency. The most likely explanation is that routing reduces the number of retrieved passages or tokens processed downstream — which would simultaneously change the accuracy task and invalidate the head-to-head accuracy comparison. This confound is not discussed anywhere. As written, neither the 2× nor the accuracy delta is attributable to the stated cause.

- **[W4] MAJOR — The baseline is under-specified and the parity claim is undefined.** "A baseline we trained ourselves with the same budget" does not identify the baseline architecture, whether it shares the retriever, whether it was tuned over the same hyperparameter grid, or what "budget" means (epochs, FLOPs, wall-clock, GPU-hours). Training a baseline for 10 epochs at a single learning rate (Method) is not evidence of a tuned baseline. An under-tuned self-trained baseline is the single most common way a small routing gain is manufactured. Without tuning-parity details, the 0.2-point delta has no clear interpretation even before the statistics are considered.

- **[W5] MAJOR — No ablation isolates the router.** The Method introduces three design choices — a learned router, top-k selection, and 64 experts — and the Results report only the full system versus one baseline. There is no ablation of the router (e.g., fixed/uniform routing, random top-k), no sweep over k, and no sweep over expert count. The paper therefore cannot attribute the measured difference to routing rather than to parameter count, changed retrieval depth, or added capacity. The number 64 is asserted without justification or sensitivity analysis.

- **[W6] MAJOR — "The gain is consistent across seeds" is unfalsifiable as reported.** The paper states results "were stable" and the gain is "consistent across seeds" while explicitly withholding per-seed numbers and confidence intervals. Consistency across seeds cannot be assessed from a single mean per method. This is a claim about variance made in the absence of any variance reporting — the strongest form of unsupported stability claim. If the per-seed counts were, e.g., 80/81/80 versus 81/80/80, the "consistent" gain would be an artifact of averaging.

- **[W7] MAJOR — Evaluation-set provenance and contamination are unaddressed.** "A held-out split of 100 examples from the benchmark" does not name the benchmark, the corpus, the split construction, or the deduplication procedure against training data. It is also unstated whether the 100 examples were used for any model or router selection (top-k, expert count, early stopping). A 100-example split is small enough that even inadvertent peeking would dominate the reported effect. For a retrieval benchmark, train/test passage overlap is a known and severe contamination channel; nothing in the paper rules it out.

- **[W8] MAJOR — No related work and no novelty positioning.** The paper contains zero citations. Sparse routing over experts and routing for retrieval are both well-established lines of work (e.g., sparsely-gated mixture-of-experts layers, Shazeer et al., 2017; retrieval-augmented and routed-retrieval systems). A reader cannot determine what is new here relative to that literature, and the paper makes no attempt to distinguish its router from standard top-k MoE routing. The absence of related work is not a formatting omission in a paper whose entire claim is novelty.

- **[W9] MINOR — Training and task specification are insufficient for reproduction.** The Method gives 10 epochs, Adam, lr = 1e-4, and nothing else: no dataset or corpus size, batch size, sequence length, warm-up/schedule, weight decay, hardware, total compute, or definition of "long context" (how many tokens?). The learning rate is stated as a single value with no indication that it was tuned. None of this is reproducible as written.

- **[W10] MINOR — Spurious precision.** Reporting 80.1% and 80.3% implies a measurement resolution of 0.1 points. On 100 examples the natural resolution is 1 point per seed. The extra digit conveys confidence the design does not have and is the surface symptom of W2.

- **[W11] MINOR — The Conclusion outruns the evidence by a wide margin.** "Should be adopted in production systems" is a deployment recommendation based on a 100-example offline evaluation with no cost model, no failure analysis, no distribution-shift analysis, and no serving benchmark. No limitations section exists to temper any of this.

## Questions for Authors

- **[Q1]** Please provide the per-seed accuracy as integer counts (k/100) for both Baseline and SparseRoute. This is the minimum needed to check W2 and W6.
- **[Q2]** Given 100 examples and 3 seeds, how were means of 80.1% and 80.3% computed? Is the split actually 100 examples, and is the mean over exactly 3 runs?
- **[Q3]** What is the benchmark, and how was the 100-example held-out split constructed? Was it deduplicated against training passages, and was it used for any hyperparameter or design selection?
- **[Q4]** What exactly is the baseline architecture, and what does "same budget" mean operationally? Was the baseline tuned over a comparable hyperparameter grid?
- **[Q5]** What is the latency measurement protocol — hardware, batch size, context length, corpus size, statistic (mean/p50/p95), warm-up, and number of repeats? Are the 40 ms and 20 ms single measurements?
- **[Q6]** Does routing change the number of retrieved passages or tokens passed to the reader? If so, how is the accuracy comparison made apples-to-apples?
- **[Q7]** What is the mechanism by which adding a 64-expert router halves latency? A cost breakdown (router overhead vs downstream savings) would settle W3.
- **[Q8]** What happens to accuracy and latency as k and the expert count vary? Is 64 experts selected by validation or asserted?
- **[Q9]** What does "stable" mean quantitatively — what was the seed-to-seed range for each method?
- **[Q10]** Is code or a run artifact available? At minimum, the per-example predictions behind the reported numbers.

## Verdict

**Not ready for external submission; major revision required.** The paper has the shape of an evaluation (held-out split, multiple seeds, latency metric, compute-matched baseline) but not the substance: the headline comparison is under-powered by roughly an order of magnitude, the reported means are inconsistent with the stated evaluation design, the latency claim lacks a protocol and has an unexamined confound, and the SOTA claim has no external referent. These are not polish issues; W1–W3 each independently invalidate a headline claim, and W2 additionally raises a reporting-integrity question that must be resolved before the numbers can be trusted at all.

The revision path is tractable: the underlying experiment (router vs. matched baseline, accuracy plus latency, multiple seeds) is the right experiment. It needs a larger and identified evaluation set, variance reporting, a tuning-parity description, an ablation, and an honest latency protocol. Confidence in this assessment: **high** for W2 (arithmetic, verifiable), W6, and W8; **high** for W1 and W3 as stated-evidence gaps; **medium** for the severity of W4/W5/W7, which could be resolved by details the paper may simply have omitted rather than failed to do.

## Revision Plan

1. **Recompute and re-report all accuracy numbers (W2, W10).** Report integer per-seed counts, then mean ± 95% CI (or per-seed range) for each method. If the 0.1-point precision cannot be reproduced from the stated protocol, correct the protocol description or the numbers, and state which.
2. **Either substantiate or delete the SOTA claim (W1).** Name the benchmark, report at least two published baselines on the same split, and compare. If no external comparison exists, retitle the claim as "improves over a compute-matched internal baseline" everywhere, including the Abstract and Conclusion.
3. **Fix the latency protocol (W3).** Specify hardware, batch, context length, statistic, warm-up, repeats; report variance or a percentile. Add a cost breakdown separating router overhead from downstream savings, and state whether retrieval depth changes. If it does, report an accuracy-matched operating point.
4. **Enlarge the evaluation and report power (W2, W7).** Move to a split large enough that the minimum detectable difference is below the claimed effect, or explicitly frame the study as a pilot and drop inferential language.
5. **Describe baseline tuning parity (W4).** Architecture, shared components, search space, selection criterion, and the operational definition of "same budget."
6. **Add the router ablation (W5).** Uniform/fixed routing and random top-k at matched parameter count; sweep k and expert count.
7. **Report per-seed results and define "stable" (W6, Q9).** Replace the consistency claim with the actual seed spread.
8. **Document data provenance and contamination checks (W7).** Benchmark name, split construction, dedup procedure, and an explicit statement that the eval split was untouched during development.
9. **Add related work and a limitations section (W8, W11).** Position against sparsely-gated MoE and retrieval-routing work; state the 100-example and single-benchmark limitations explicitly.
10. **Complete the Method for reproducibility (W9).** Dataset/corpus size, batch size, sequence length definition, schedule, hardware, compute, and evidence that lr = 1e-4 was selected rather than defaulted.
11. **Soften the Conclusion (W11).** Replace the production-adoption recommendation with a scoped statement of what the evidence supports.

---

## Inline Annotations

> "We introduce SparseRoute, a routing layer for long-context retrieval. SparseRoute improves accuracy from 80.1% to 80.3% on our benchmark and is 2x faster. It establishes a new state of the art."

**[W1] FATAL:** "Our benchmark" is never named, and "state of the art" is asserted without a single external comparison. SOTA is a claim about the best published result on a defined task; the paper compares only to a baseline the authors trained. Delete or substantiate. See also **[W2]**: 80.1% and 80.3% cannot both be seed-means over 3 runs of a 100-example split.

> "SparseRoute adds a learned top-k router over 64 experts. We train for 10 epochs with Adam at a learning rate of 1e-4."

**[W5] MAJOR:** The router, the top-k selection, and the choice of 64 experts are three separable design decisions, none ablated and none justified. 64 is asserted, not selected. **[W9] MINOR:** Ten epochs, Adam, and one learning rate are not a reproducible training description — no batch size, sequence length, schedule, data size, hardware, or compute, and no indication that 1e-4 was tuned.

> "We evaluate on a held-out split of 100 examples from the benchmark."

**[W2] FATAL:** A 100-example split cannot resolve a 0.2-point difference; the binomial SE at p ≈ 0.8 is ≈ 4 points, so the claimed effect is ~1/20 of one SE. **[W7] MAJOR:** "The benchmark" is unnamed, the split construction is unspecified, and there is no dedup or contamination check against training passages — the dominant contamination channel for retrieval. **[Q3]** Was this split used for any design selection?

> "We compare against a baseline we trained ourselves with the same budget."

**[W4] MAJOR:** The baseline architecture is unidentified and "same budget" is undefined (epochs? FLOPs? wall-clock?). A baseline trained by the authors at one learning rate is not evidence of a tuned baseline. This is the single most common source of spurious small gains in routing papers.

> "We ran 3 seeds and the results were stable. We report mean accuracy over the seeds. We do not report confidence intervals or per-seed numbers."

**[W6] MAJOR:** "Results were stable" is a variance claim made while explicitly withholding all variance information. Per-seed numbers are the minimum needed to evaluate it. **[W2] FATAL:** These three sentences together make the reported means checkable — and they fail the check: the mean of 3 runs on 100 examples must land on a multiple of 1/300, so 80.1% and 80.3% are unreachable. The paper states the protocol that contradicts its own table.

> "| Baseline | 80.1% | 40 ms |" / "| SparseRoute | 80.3% | 20 ms |"

**[W3] FATAL:** Latency is given as bare single numbers with no hardware, batch size, context length, statistic, warm-up, or repeats. **[W10] MINOR:** Both accuracy values carry a tenth-of-a-point digit that the 100-example design cannot produce. **[Q1]/[Q5]** Request integer per-seed counts and the latency protocol.

> "SparseRoute improves accuracy by 0.2 points and halves latency. The gain is consistent across seeds."

**[W2]/[W6] FATAL:** "Consistent across seeds" is asserted with no per-seed data, and 0.2 points is 0.6 example predictions across all three seeds — far inside noise. **[W3] FATAL:** "Halves latency" restates an unprotocoled measurement. **[W5]** No ablation supports attributing either change to routing rather than to changed retrieval depth or added capacity.

> "SparseRoute is a new state of the art for efficient retrieval and should be adopted in production systems."

**[W11] MINOR (severity of claim: major):** A production-adoption recommendation from a 100-example offline evaluation with no cost model, failure analysis, or serving benchmark. Restate as a scoped claim about the internal comparison, and add a limitations section.

---

## Sources

- Reviewed artifact: `experiments/feynman-eval-case-study/fixtures/mini-eval-paper.md` (local, no URL).
- Case-study protocol and evaluation ground truth: `experiments/feynman-eval-case-study/protocol.md` (local, no URL).
- Statistical checks (Wilson interval, SE, achievable-mean arithmetic) were computed locally with Python; method is standard binomial/Wilson and requires no external source.
- Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer" (2017), cited in W8 as prior art for sparse expert routing: https://arxiv.org/abs/1701.06538
