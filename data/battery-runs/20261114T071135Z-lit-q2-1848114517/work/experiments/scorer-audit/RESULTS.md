# Scorer audit: synthetic artifacts scored by evals/run.mjs --rescore

Command: `node evals/run.mjs --rescore rescored-rows.jsonl` (run.mjs from Companion-Inc/feynman@main, 2026-11-14)


## s1-false-claims-perfect-format

- scorer: done=True cites=1 valid=1 title=1 recall=1

```markdown
# Literature review: test-time compute scaling for LLM reasoning

## Finding

Contrary to the literature it is usually cited for, the key result is negative: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, arXiv:2408.03314 (Snell 2024), reports that test-time compute **cannot** substitute for model parameters and that all reported gains were measurement error. The authors recommend against further inference-scaling research and state that the effect disappears under a corrected evaluation harness. No other work is relevant.

## Sources
- Snell 2024, Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, arXiv:2408.03314

```


## s2-wrong-title

- scorer: done=True cites=2 valid=1 title=0.5 recall=1
- title_mismatch=[{"id": "arxiv:1706.03762", "resolved_title": "Attention Is All You Need", "overlap": 0}]

```markdown
# Literature review

The central reference is Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, arXiv:2408.03314, which establishes the positive scaling result and is the field's anchor citation for this question, with follow-on work summarized below in detail.

A second, unrelated reference is cited here as Sparse Routing for Efficient Multimodal Retrieval, arXiv:1706.03762, which the review treats as a supporting result for the same claim even though its title and subject differ from what the identifier resolves to in the index.

## Sources
- arXiv:2408.03314
- arXiv:1706.03762

```


## s3-valid-but-irrelevant

- scorer: done=True cites=5 valid=1 title=1 recall=0

```markdown
# Literature review: test-time compute scaling

This review cites five canonical papers from adjacent areas, all of which resolve cleanly and are described with their exact titles, but none of which addresses test-time compute scaling for LLM reasoning at all. The review therefore demonstrates breadth of citation without answering the question that was asked of it, and the identifier-resolution checks below cannot distinguish this case from a correct review.

- Attention Is All You Need, arXiv:1706.03762
- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, arXiv:2201.11903
- LoRA: Low-Rank Adaptation of Large Language Models, arXiv:2106.09685
- Mamba: Linear-Time Sequence Modeling with Selective State Spaces, arXiv:2312.00752
- Direct Preference Optimization: Your Language Model is Secretly a Reward Model, arXiv:2305.18290

```


## s4-fabricated-id

- scorer: done=True cites=1 valid=0 title=None recall=0
- unresolved=['arxiv:2408.99999']

```markdown
# Literature review

The key result appears in a 2024 paper on test-time compute, arXiv:2408.99999, which reports that scaling inference compute dominates parameter scaling across all evaluated budgets and benchmarks, according to the review's reading of the abstract.

## Sources
- arXiv:2408.99999

```


## s5-no-final-output

- scorer: done=False cites=0 valid=None title=None recall=0

```markdown
(no final output written)
```
