# Ground truth for blind canary audit

Verified 2026-11-14 via `feynman_science_database_search` (source: arxiv) and the
abstracts returned by the arXiv API.

## Verified sources

1. Vaswani et al. (2017), "Attention Is All You Need", arXiv:1706.03762.
   - 28.4 BLEU on WMT 2014 English-to-German; over 2 BLEU above the prior best, including ensembles.
   - 41.8 BLEU on WMT 2014 English-to-French.
   - Trained for 3.5 days on eight GPUs.
2. Devlin et al. (2019), "BERT: Pre-training of Deep Bidirectional Transformers for
   Language Understanding", arXiv:1810.04805.
   - GLUE score 80.5% (7.7 point absolute improvement).
   - MultiNLI accuracy 86.7%.
   - SQuAD v1.1 Test F1 93.2.
3. Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language
   Models", arXiv:2201.11903.
   - 540B-parameter model with eight chain-of-thought exemplars achieves state-of-the-art
     accuracy on GSM8K.
   - The abstract does not state a single GSM8K percentage.
4. OpenAI (2023), "GPT-4 Technical Report", arXiv:2303.08774.
   - Simulated bar exam around the top 10% of test takers.
5. Lewis et al. (2020), "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
   arXiv:2005.11401. (Metadata only; abstract not used as evidence here.)

## Instruction to the verifier

Use this file as the research file. Preserve the draft's structure. Add inline citations
where the ground truth supports a claim. Independently check every source identifier and
URL with your own tools. Remove, correct, or explicitly flag any claim that the ground
truth does not support. Add a short `Verification Notes` section listing every problem you
found and what you did about it.
