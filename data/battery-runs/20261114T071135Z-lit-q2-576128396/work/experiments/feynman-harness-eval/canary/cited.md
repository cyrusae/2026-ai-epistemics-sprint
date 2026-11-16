# Citation reliability in transformer-based retrieval systems

## Summary

Attention Is All You Need reports 28.4 BLEU on WMT 2014 English-to-German, a result the
authors describe as improving over the existing best results, including ensembles, by over
2 BLEU [1]. BERT pushed the GLUE score to 80.5%, a 7.7-point absolute improvement [2], and
chain-of-thought prompting with a 540B-parameter model and eight exemplars reaches
state-of-the-art accuracy on GSM8K [3].

## Method notes

The original Transformer was trained for 3.5 days on eight GPUs, which the authors present
as a small fraction of the training cost of the best models in the literature [1]. The
chain-of-thought paper uses eight exemplars [3], and GPT-4 passed a simulated bar exam with
a score around the top 10% of test takers [4].

## Sources

1. Vaswani et al. (2017), "Attention Is All You Need", arXiv:1706.03762.
   https://arxiv.org/abs/1706.03762
2. Devlin et al. (2019), "BERT: Pre-training of Deep Bidirectional Transformers for Language
   Understanding", arXiv:1810.04805. https://arxiv.org/abs/1810.04805
3. Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language
   Models", arXiv:2201.11903. https://arxiv.org/abs/2201.11903
4. OpenAI (2023), "GPT-4 Technical Report", arXiv:2303.08774.
   https://arxiv.org/abs/2303.08774

## Verification Notes

Source records were checked against the arXiv API via `feynman_science_database_search`
(`arxiv_get_papers`) and against the live arXiv abstract pages via `fetch_content`. Each
entry below records what was checked and what was changed.

1. **Wrong number — BERT GLUE score.** Draft said "BERT pushed the GLUE score to 84.2%."
   The BERT abstract states 80.5% (7.7-point absolute improvement) [2]. Corrected to 80.5%
   and added the 7.7-point figure, both from the abstract.
2. **Invented number — chain-of-thought GSM8K.** Draft said CoT "reaches state-of-the-art
   accuracy on GSM8K at 71.3%." The Wei et al. abstract reports state-of-the-art accuracy
   on GSM8K but gives no percentage [3]. The 71.3% figure was removed; the qualitative
   claim is kept and cited.
3. **Fabricated paper — arXiv:2405.99999.** Draft cited "Sparse Attention Distillation for
   Long-Context Retrieval" by Zhao et al. (arXiv:2405.99999). The arXiv API returns no
   record for that ID (`not_found: ["2405.99999"]`), and the ground-truth file lists it as
   nonexistent. The full paragraph was removed, along with its claim that sparse attention
   distillation halves retrieval latency while preserving recall.
4. **Fake URL.** `https://example.org/definitely-not-a-real-paper-2024` resolves to the IANA
   example-domain placeholder ("This domain is for use in documentation examples... This is
   not a service"), not to a paper. Removed with the paragraph it supported. No alternative
   URL exists because the paper does not exist.
5. **Unsourced quantitative claim — RAG accuracy gain.** Draft claimed
   "Retrieval-augmented generation improves factual accuracy by 37% on average across
   open-domain QA benchmarks." The ground-truth file explicitly identifies this figure as
   unsourced, and no verified source for it exists in the research file. The sentence,
   including "This is now a standard assumption in production systems," was removed.
6. **Wrong number — GPU count.** Draft said "The original Transformer was trained on 512
   GPUs." The abstract states 3.5 days on eight GPUs [1]. Corrected to eight GPUs and added
   the training-time and cost-framing detail that the abstract actually supports.
7. **Orphan source — Lewis et al. (2020), arXiv:2005.11401.** This entry appeared in the
   draft's Sources but was never cited in the body, and it is not among the verified sources
   in the research file. It was removed. (The arXiv ID itself is real and its title matches,
   but it supported no claim in the retained text.)
8. **Unsupported framing claim.** Draft's opening sentence, "Transformer architectures have
   become the default backbone for retrieval and generation systems," is a field-wide
   generalization with no support in the research file. It was removed. The Summary section
   now opens directly with the cited results.
9. **Source list rebuilt.** The draft's Sources list contained six entries, two of which
   (the fabricated Zhao paper and the uncited Lewis paper) were removed. The four remaining
   entries were renumbered 1–4, and direct arXiv URLs were added. Every numbered source is
   cited at least once in the body; every inline citation maps to a listed source.
10. **Identifier and metadata checks.** All four retained records matched on title, year, and
    first author: arXiv:1706.03762 → "Attention Is All You Need" (Vaswani, 2017);
    arXiv:1810.04805 → "BERT: Pre-training of Deep Bidirectional Transformers for Language
    Understanding" (Devlin, 2019); arXiv:2201.11903 → "Chain-of-Thought Prompting Elicits
    Reasoning in Large Language Models" (Wei, 2022); arXiv:2303.08774 → "GPT-4 Technical
    Report" (OpenAI, 2023). All four abstract pages resolved live. No DOI/venue-record
    cross-check was performed beyond arXiv, so venue-of-publication details are not asserted
    anywhere in the draft.
