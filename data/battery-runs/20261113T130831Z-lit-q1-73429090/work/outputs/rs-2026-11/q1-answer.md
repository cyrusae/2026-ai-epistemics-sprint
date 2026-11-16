# Q1 answer — Reflexion (Shinn et al., arXiv:2303.11366) on MBPP (Python)

## Direct answer

**Reflexion reports 77.1 pass@1 on MBPP (Python).** It compares against two reference
columns, and the operative baseline is **GPT-4 at 80.1 pass@1** (a single zero-shot code
generation sample). Reflexion **does not beat that baseline**: 77.1 vs 80.1 is a
**2.9–3.0 point loss**. It does beat the older "Prev SOTA" entry, CodeT + Codex at 67.7.
The paper says so explicitly: Reflexion "sets new state-of-the-art standards on all
benchmarks for Python and Rust **except for MBPP Python**" [2].

## Exact table row (Table 1, "Pass@1 accuracy for various model-strategy-language combinations")

Published NeurIPS 2023 version, p. 7 [1]; identical in arXiv v2/v3/v4 HTML [2][3]:

| Benchmark + Language | Prev SOTA Pass@1 | SOTA Pass@1 | Reflexion Pass@1 |
|---|---|---|---|
| **MBPP (PY)** | **67.7 (CodeT [5] + Codex [6])** | **80.1 (GPT-4)** | **77.1** |

Companion Table 2 ("Overall accuracy and test generation performance", p. 8) restates the
same comparison as base vs Reflexion: **MBPP (PY): Base 0.80, Reflexion 0.77**, with
TP 0.84 / FN 0.59 / FP 0.16 / TN 0.41 [1][2]. (HumanEval (PY) for contrast: 0.80 → 0.91.)

Table caption: "The base strategy is a single code generation sample. All instruction-based
models follow zero-shot code generation." [1]

## Why it loses (the paper's own explanation)

- The paper attributes the MBPP loss to unreliable self-generated unit tests: the false
  positive rate — probability a submission fails the hidden tests *given* it passed all
  self-written tests — is **16.3% on MBPP Python vs 1.4% on HumanEval Python**. A false
  positive terminates the loop on wrong code, so the agent never reflects or retries [1][2].
- Consequence for citing: Reflexion's gains on HumanEval (91.0 vs 80.1) do **not**
  generalize to MBPP Python; the authors report this as a self-evaluation quality limit,
  not a tuning artifact.

## Caveats / precision notes

- **Which "baseline" you mean matters.** If a claim says "Reflexion beats the baseline on
  MBPP", that is only true against the *previous* SOTA (67.7, CodeT + Codex). Against the
  contemporaneous GPT-4 baseline (80.1) it loses. Reflexion's own actor here *is* GPT-4,
  so the honest phrasing is "Reflexion underperforms its GPT-4 single-sample base on MBPP
  Python by ~3 points."
- **Version stability:** The MBPP row is absent from arXiv v1 (v1 had no MBPP experiments;
  its HTML contains zero "MBPP" mentions) and is stable at 67.7 / 80.1 / 77.1 across
  v2, v3, v4 and the NeurIPS camera-ready [1][3]. Cite v4 or the NeurIPS version.
- **Minor internal inconsistency:** the prose on p. 8 says the HumanEval and MBPP Python
  baseline pass@1 are "82% and 80%", while Table 2 lists HumanEval Base as 0.80 [1]. Does
  not affect the MBPP comparison (80.1 / 0.80 both stated consistently).
- **Repo link in the paper is dead:** the paper prints
  `https://github.com/noahshinn024/reflexion`, which returns HTTP 404; the live repo is
  `https://github.com/noahshinn/reflexion` (HTTP 200) [4].

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning", NeurIPS 2023 proceedings PDF (19 pp.) | https://proceedings.neurips.cc/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf | Table 1 p.7: MBPP (PY) 67.7 (CodeT+Codex) / 80.1 (GPT-4) / 77.1; Table 2 p.8: Base 0.80 vs Reflexion 0.77; FP 16.3% vs 1.4% | primary (published) | high |
| 2 | Shinn et al., arXiv:2303.11366v4 HTML full text | https://arxiv.org/html/2303.11366v4 | Same Table 1/Table 2 values; "sets new state-of-the-art standards on all benchmarks ... except for MBPP Python" | primary (preprint) | high |
| 3 | arXiv:2303.11366v2 and v3 HTML | https://arxiv.org/html/2303.11366v3 | Same MBPP row 67.7 / 80.1 / 77.1 (version-stability check); v1 HTML has no MBPP content | primary | high |
| 4 | noahshinn/reflexion GitHub repository | https://github.com/noahshinn/reflexion | Live repo for paper code/logs (HTTP 200); paper's printed URL `noahshinn024/reflexion` returns 404 | self-reported / primary artifact | high |
| 5 | arXiv abstract page 2303.11366 (v4, 10 Oct 2023) | https://arxiv.org/abs/2303.11366 | Paper identity, authors, version history; abstract foregrounds only the HumanEval 91% vs GPT-4 80% result (MBPP loss not in abstract) | primary (metadata) | high |
| 6 | alphaXiv summary page for 2303.11366 | https://www.alphaxiv.org/abs/2303.11366 | Secondary restatement: "On MBPP Python, Reflexion reports 77.1%, compared with GPT-4's 80.1% [p7]" | secondary | medium |

## Findings

Reflexion's MBPP (Python) result is **77.1 pass@1**, listed in Table 1 of the NeurIPS
camera-ready alongside a "Prev SOTA Pass@1" of 67.7 (CodeT + Codex) and a "SOTA Pass@1" of
80.1 (GPT-4) [1]. The same numbers appear unchanged in arXiv v2–v4 [2][3]. The authors
state directly that Reflexion "outperforms all baseline accuracies and sets new
state-of-the-art standards on all benchmarks for Python and Rust except for MBPP Python,"
and then devote the following paragraph to "the inferior performance of Reflexion on MBPP
Python" [1][2].

So the answer to "does Reflexion beat that baseline" is **no, not on MBPP (Python)** — it
is 2.9 points below GPT-4's 80.1, while being 9.4 points above the older CodeT + Codex
number. The paper's diagnosis is test-suite reliability: Table 2 reports a 16.3% false
positive rate on MBPP Python versus 1.4% on HumanEval Python, meaning self-written tests
frequently pass incorrect solutions and end the Reflexion loop prematurely [1][2]. (This
causal reading is stated by the authors, not inferred.) One implication worth flagging for
downstream writing: citing "Reflexion improves code generation" without qualification is
only supported for HumanEval Python/Rust, MBPP Rust and LeetcodeHard — an inference from
the table, but a direct one.

## Sources

1. Shinn, Cassano, Gopinath, Narasimhan, Yao — "Reflexion: Language Agents with Verbal Reinforcement Learning," NeurIPS 2023 — https://proceedings.neurips.cc/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf
2. Shinn et al. — arXiv:2303.11366v4 HTML — https://arxiv.org/html/2303.11366v4
3. Shinn et al. — arXiv:2303.11366v3 HTML — https://arxiv.org/html/2303.11366v3
4. noahshinn/reflexion — https://github.com/noahshinn/reflexion
5. arXiv:2303.11366 abstract page — https://arxiv.org/abs/2303.11366
6. alphaXiv summary, arXiv:2303.11366 — https://www.alphaxiv.org/abs/2303.11366

## Coverage Status

- **Checked directly:** Table 1 and Table 2 in the NeurIPS PDF text [1] and in arXiv v4
  HTML, including the raw `<table>` markup [2]; the MBPP row in arXiv v2/v3 HTML [3];
  presence/absence of MBPP in v1 HTML; HTTP status of both candidate repo URLs.
- **Uncertain / not checked:** I did not independently verify the CodeT/Codex 67.7 and
  GPT-4 80.1 numbers against the original CodeT, Codex or GPT-4 papers — they are taken
  as reported by Reflexion. I did not check the paper's own logged runs in the repo to
  confirm 77.1 reproduces. No statistical-significance testing is reported by the paper,
  so the 2.9-point gap has no stated confidence interval.
- **Tasks not completed:** none blocked; single lookup only.
