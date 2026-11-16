# Citation check: Reflexion on HumanEval

## Verdict

**No — the number is 91%, not 92%.** There is no 92% HumanEval pass@1 result anywhere in the Reflexion paper. The paper's abstract, Table 1, Table 2, and the NeurIPS 2023 camera-ready all say **91%** (Table 1 gives **91.0**, against a quoted GPT-4 single-sample baseline of **80.1**) [1][2][3].

The 92% figure belongs to a *different* paper — **"Past as a Guide" (PaG)**, which reports **92.07%** pass@1 on HumanEval with GPT-4 and, in the same table, lists Reflexion at **91.00** [4]. That is almost certainly where the 92 came from: it is the row directly above/below Reflexion in PaG's comparison table. Do not attribute it to Reflexion.

## The citation

```bibtex
@inproceedings{shinn2023reflexion,
  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},
  author    = {Shinn, Noah and Cassano, Federico and Berman, Edward and
               Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS 2023)},
  year      = {2023},
  eprint    = {2303.11366},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url       = {https://arxiv.org/abs/2303.11366}
}
```

Authors/affiliations as printed in the camera-ready: Noah Shinn, Federico Cassano (Northeastern), Edward Berman, Ashwin Gopinath (MIT), Karthik Narasimhan, Shunyu Yao (Princeton) [3]. Note the author list has **six** authors including Edward Berman — some secondary pages drop him.

Links: arXiv abstract https://arxiv.org/abs/2303.11366 (v4, 10 Oct 2023) · NeurIPS proceedings https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html · official code https://github.com/noahshinn/reflexion [5].

## What the paper actually says

Abstract, verbatim [1][3]:

> "For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%."

Table 1, HumanEval (PY) row, verbatim [1]:

| Benchmark + Language | Prev SOTA Pass@1 | SOTA Pass@1 | Reflexion Pass@1 |
|---|---|---|---|
| HumanEval (PY) | 65.8 (CodeT + GPT-3.5) | 80.1 (GPT-4) | **91.0** |

Table 2 gives the same pair as fractions: Base **0.80**, Reflexion **0.91** [1].

**Independent check.** The official repo ships the raw per-task log for this exact run (`programming_runs/root/reflexion_humaneval_py_pass_at_1/reflexion_humaneval_py_pass_at_1.jsonl`, 164 tasks, model `gpt-4`, `pass_at_k=1` per `run_reflexion.sh`). Counting `is_solved` in that file gives **150/164 = 91.46%** [5]. So the headline number is reproducible from the authors' own logs and rounds to 91% — it does not round to 92%.

## Two things to get right in the related-work sentence

1. **91.0 is not "GPT-4 one-shot."** It is Reflexion's *final* accuracy after its self-reflection loop: the agent writes up to 6 of its own unit tests per problem, and on failure writes a reflection that conditions the next attempt [1]. Table 1's caption says the baseline column "is a single code generation sample" — i.e. the 91.0 sits in a pass@1 column but is measured over multiple attempts. In the released logs, 30 of 164 problems used at least one reflection and a few used up to 9, i.e. up to 10 attempts [5]. If your related-work section contrasts "single-sample" vs "agentic" numbers, say so explicitly, because 91.0 vs 80.1 is not a like-for-like comparison of one generation each.
2. **Do not cite it as a clean win without the MBPP row.** In the same table Reflexion *loses* on MBPP Python, 77.1 vs GPT-4's 80.1, which the authors attribute to a 16.3% false-positive rate in self-generated tests (vs 1.4% on HumanEval) [1]. Also be aware the paper contains an internal inconsistency: the §4.3 analysis prose says the HumanEval baseline is "82%" while Tables 1 and 2 say 80.1 / 0.80 [1]. Use 80.1 and cite the table, not the prose.

## Suggested wording

> Reflexion (Shinn et al., NeurIPS 2023) reports 91.0% pass@1 on HumanEval in Python with GPT-4 as the base model, versus 80.1% for GPT-4 with a single sample, by iteratively generating self-tests and verbal self-reflections across attempts [1]. The same method degrades on MBPP (77.1% vs 80.1%).

If you specifically want a 92% HumanEval number, cite PaG (Shin et al., 2023, arXiv:2311.07635), which reports 92.07% — and note it is a different method [4].

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | Shinn et al., *Reflexion*, NeurIPS 2023 (arXiv:2303.11366v4, HTML) | https://arxiv.org/html/2303.11366v4 | Abstract: 91% HumanEval; Table 1: Reflexion 91.0 vs GPT-4 80.1; Table 2: 0.91 vs 0.80; MBPP 77.1 vs 80.1; §4.3 prose says baseline "82%" | primary | high |
| 2 | NeurIPS 2023 proceedings abstract page | https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html | Camera-ready abstract states 91% vs GPT-4 80% | primary | high |
| 3 | NeurIPS 2023 camera-ready PDF | https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf | Six authors incl. Edward Berman; 91% in abstract; NeurIPS 2023 | primary | high |
| 4 | Shin, Chang, Choi, *Past as a Guide* (arXiv:2311.07635) | https://arxiv.org/abs/2311.07635 | Reports 92.07% pass@1; its Table 2 lists Reflexion at 91.00 | primary | high |
| 5 | Official Reflexion repo + `run_reflexion.sh` + HumanEval log | https://github.com/noahshinn/reflexion | `--model gpt-4 --pass_at_k 1`; log gives 150/164 solved = 91.46%; 30 tasks with ≥1 reflection | primary (authors' artifact) | high |
| 6 | arXiv API metadata for 2303.11366 | https://export.arxiv.org/api/query?id_list=2303.11366 | v4 published 2023-10-10; abstract text confirms 91% | primary | high |

## Sources

1. Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao — *Reflexion: Language Agents with Verbal Reinforcement Learning* (v4 HTML) — https://arxiv.org/html/2303.11366v4
2. NeurIPS 2023 proceedings, paper abstract page — https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html
3. NeurIPS 2023 camera-ready PDF — https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf
4. Seunggyoon Shin, Seunggyu Chang, Sungjoon Choi — *Past as a Guide: Leveraging Retrospective Learning for Python Code Completion* — https://arxiv.org/abs/2311.07635
5. Official Reflexion code repository — https://github.com/noahshinn/reflexion (file `programming_runs/root/reflexion_humaneval_py_pass_at_1/reflexion_humaneval_py_pass_at_1.jsonl`)
6. arXiv API record for 2303.11366 — https://export.arxiv.org/api/query?id_list=2303.11366

## Coverage Status

- **Checked directly:** arXiv v4 HTML (abstract, Table 1, Table 2, §4.3 prose, Table 3 caption), NeurIPS abstract page, NeurIPS camera-ready PDF abstract, arXiv API metadata, official repo README/run script and the raw HumanEval Python log (counted 164 records, 150 solved).
- **Inference, not verified:** that the user's "92%" came from PaG's comparison table. I confirmed PaG reports 92.07% and lists Reflexion at 91.00; I found no Reflexion source claiming 92%, but I cannot prove the exact provenance of the user's number.
- **Not checked:** whether older Reflexion arXiv versions (v1–v3) differ numerically from v4; the v1 text predates the NeurIPS camera-ready and may contain minor wording changes, though the 91% headline appears to be stable.
- **Unresolved internal inconsistency in the source:** §4.3 prose ("82%") vs Tables 1/2 ("80.1"/"0.80"). Reported above rather than silently reconciled.
