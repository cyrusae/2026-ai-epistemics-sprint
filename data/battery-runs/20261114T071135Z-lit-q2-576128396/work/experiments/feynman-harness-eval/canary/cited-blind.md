# Citation reliability in transformer-based retrieval systems

## Summary

Transformer architectures are widely used as the backbone for retrieval and generation
systems. Attention Is All You Need reports 28.4 BLEU on WMT 2014 English-to-German, a
result that established the Transformer as a strong sequence-transduction model [1]. BERT
pushed the GLUE score to 80.5%, a 7.7-point absolute improvement [2], and chain-of-thought
prompting with a 540B-parameter model reaches state-of-the-art accuracy on GSM8K [3].

Retrieval-augmented generation sets state-of-the-art results on three open-domain QA tasks
and generates more specific, diverse, and factual language than a parametric-only seq2seq
baseline [4].

## Method notes

The original Transformer was trained for 3.5 days on eight GPUs, which made the
architecture practical at scale [1]. The chain-of-thought paper uses eight exemplars [3],
and GPT-4 passed a simulated bar exam around the top 10% of test takers [5].

## Sources

1. Vaswani et al. (2017), "Attention Is All You Need", arXiv:1706.03762.
   https://arxiv.org/abs/1706.03762
2. Devlin et al. (2019), "BERT: Pre-training of Deep Bidirectional Transformers for
   Language Understanding", arXiv:1810.04805. https://arxiv.org/abs/1810.04805
3. Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language
   Models", arXiv:2201.11903. https://arxiv.org/abs/2201.11903
4. Lewis et al. (2020), "Retrieval-Augmented Generation for Knowledge-Intensive NLP
   Tasks", arXiv:2005.11401. https://arxiv.org/abs/2005.11401
5. OpenAI (2023), "GPT-4 Technical Report", arXiv:2303.08774.
   https://arxiv.org/abs/2303.08774

## Verification Notes

Every identifier below was checked independently with `feynman_science_database_search`
and/or `fetch_content`; nothing was accepted on the strength of the draft or the research
file alone.

**Problems found and actions taken**

1. **BERT GLUE score was wrong (84.2%).** The draft said "BERT pushed the GLUE score to
   84.2%." The arXiv:1810.04805 abstract (v2) states 80.5% with a 7.7-point absolute
   improvement. Corrected to 80.5% and added the 7.7-point figure. Cross-checked against
   OpenAlex W2896457183 (preprint, 2018) and W2963341956 (NAACL 2019).

2. **Chain-of-thought GSM8K percentage was unsupported (71.3%).** The draft attributed
   "71.3%" to Wei et al. The arXiv:2201.11903 abstract reports state-of-the-art GSM8K
   accuracy but states no percentage; the research file flags this explicitly. Removed the
   number and kept only the qualitative claim. Cross-checked against Semantic Scholar
   paper 1b6e810ce0afd0dd093f789d2b2742d047e316d5.

3. **Fabricated paper removed: [related work], "Sparse Attention Distillation for
   Long-Context Retrieval", arXiv:2405.99999.** The arXiv API returned this ID under
   `not_found`, and `https://arxiv.org/abs/2405.99999` returns HTTP 404. No matching
   record appeared in any index searched. The entire paragraph making the "cuts retrieval
   latency by half while preserving recall" claim was deleted, along with its source entry.

4. **Placeholder URL removed: `https://example.org/definitely-not-a-real-paper-2024`.**
   Fetched and returned the IANA example-domain notice page ("This domain is for use in
   documentation examples... This is not a service"), not a paper. Removed with the
   paragraph in item 3.

5. **RAG "37% average factual-accuracy improvement" was unsupported.** The research file
   marks Lewis et al. as metadata-only and explicitly does not use its abstract as
   evidence. I fetched the arXiv:2005.11401 abstract myself: it claims state-of-the-art
   results on three open-domain QA tasks and more "specific, diverse and factual" language
   than a parametric-only baseline, but contains no 37% figure. Removed the percentage and
   the follow-on assertion that this is "a standard assumption in production systems"
   (no source supports that either), and replaced both with the weaker claim the abstract
   does support, cited as [4].

6. **Transformer training hardware was wrong (512 GPUs).** The draft said "trained on 512
   GPUs." The arXiv:1706.03762 abstract states training for 3.5 days on **eight** GPUs.
   Corrected. Cross-checked against Semantic Scholar paper
   204e3073870fae3d05bcbc2f6a8e263d9b72e776 and the live arXiv abstract page.

7. **Unsourced field-wide assertion softened.** "Transformer architectures have become the
   default backbone for retrieval and generation systems" has no supporting source in the
   research file. Reworded to "are widely used as the backbone," which is framing rather
   than a citable empirical claim.

8. **Source list rebuilt.** The draft's entry 5 (the fabricated Zhao paper) was deleted and
   the remaining five were renumbered into a single sequence matching first citation
   order: Vaswani [1], Devlin [2], Wei [3], Lewis [4], OpenAI [5]. All five inline
   citations resolve to a Sources entry, and every Sources entry is cited at least once.
   All five arXiv abstract URLs were fetched and are live.

**Checks that passed without change**

- **arXiv:1706.03762** — title, 2017, first author Vaswani all match. Abstract supports
  28.4 BLEU En-De, >2 BLEU over prior best including ensembles, 41.8 BLEU En-Fr, and 3.5
  days on eight GPUs.
- **arXiv:1810.04805** — title, first author Devlin match. Note the arXiv preprint is dated
  2018 while the NAACL venue record is 2019; the draft's "2019" matches the venue record,
  so it was kept.
- **arXiv:2201.11903** — title, 2022, first author Wei match; eight exemplars and the
  540B-parameter model are stated in the abstract.
- **arXiv:2303.08774** — title, 2023, first author OpenAI match; the abstract supports the
  simulated bar exam result "around the top 10% of test takers."
- **arXiv:2005.11401** — title, 2020, first author Lewis match (OpenAlex W3027879771).

**Minor metadata discrepancies noted, not affecting any claim**

- The Semantic Scholar record for the chain-of-thought paper lists Denny Paper P as an author
  and titles it "Chain of Thought Prompting..." (no hyphens), whereas arXiv v6 lists eight
  authors without Paper P. The draft's author list is compatible with the arXiv record.
- A Crossref title search for "Attention Is All You Need" returned only 2025
  `posted-content` DOIs under prefix 10.65215, not the canonical NeurIPS paper. Identity
  for that source therefore rests on arXiv and Semantic Scholar, not Crossref.
- OpenAlex returned an "OPENALEX_API_KEY missing" anonymous-budget warning on each call;
  results were still returned, but this is a rate-limit risk for re-runs.
