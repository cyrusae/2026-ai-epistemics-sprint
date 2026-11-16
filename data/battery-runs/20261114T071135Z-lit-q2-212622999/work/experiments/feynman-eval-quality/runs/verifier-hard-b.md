# Attention, pretraining, and scale

## Summary

The Transformer is a sequence-transduction architecture based solely on attention mechanisms; it dispenses with recurrence and convolutions entirely [1]. BERT is pre-trained with two unsupervised objectives: masked language modeling and next-sentence prediction [2]. GPT-3 is an autoregressive language model with 175 billion parameters [3]. The Transformer was introduced by Vaswani et al. [1], and BERT was introduced by Devlin et al. [2].

## Details

The Transformer reaches 28.4 BLEU on the WMT 2014 English-to-German translation task [1]. BERT-Large reaches 80.5% on the GLUE benchmark [2]. BERT-Large also reaches 93.2 F1 on SQuAD v1.1 [2]. GPT-3 is evaluated in few-shot, one-shot, and zero-shot settings without gradient updates or fine-tuning [3].

## Conclusion

Read together, these papers are consistent with attention-only architecture, pretraining objectives, and scale being three important ingredients in language-model progress. That framing is an interpretation of the cited results rather than a claim advanced by any one of the papers [1, 2, 3].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* NeurIPS 2017. arXiv:1706.03762. https://arxiv.org/abs/1706.03762
2. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* NAACL-HLT 2019. arXiv:1810.04805 (preprint 2018). https://arxiv.org/abs/1810.04805
3. Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., et al. (2020). *Language Models are Few-Shot Learners.* NeurIPS 2020. arXiv:2005.14165. https://arxiv.org/abs/2005.14165

## Source verification

All three URLs were fetched on 2026-11-14 and resolve to live arXiv abstract pages containing the cited numbers.

| Ref | URL status | Identifier cross-check | Result |
| --- | --- | --- | --- |
| [1] | Live (HTTP page served, abstract text matched) | arXiv 1706.03762; OpenAlex W2626778328 / DOI 10.48550/arxiv.1706.03762 | Title, year (2017), first author (Vaswani) match |
| [2] | Live (HTTP page served, abstract text matched) | arXiv 1810.04805; OpenAlex W2896457183 (preprint, 2018) and W2963341956 / DOI 10.18653/v1/n19-1423 (NAACL-HLT 2019) | Title, first author (Devlin) match; preprint and venue records carry different years, and the notes cite the 2019 venue with the arXiv ID, which is consistent with these two records |
| [3] | Live (HTTP page served, abstract text matched) | arXiv 2005.14165; OpenAlex W3030163527 / DOI 10.48550/arxiv.2005.14165 | Title, year (2020), first author (Brown) match |

Note on [3]: OpenAlex lists the first author as "Brown, Tom B."; the notes list "Tom B. Brown". Same author, formatting difference only.

## Removed or corrected unsupported claims

The draft as supplied contained claims that its own research notes contradict. Each was corrected against the primary source rather than preserved:

- **"The Transformer uses recurrence to encode sequence order."** Contradicted by [1], whose abstract states the Transformer works "solely on attention mechanisms, dispensing with recurrence and convolutions entirely." Rewritten in the Summary.
- **"GPT-3 has 1.75 trillion parameters."** The notes and the GPT-3 abstract give 175 billion parameters [3]. Corrected.
- **"Vaswani et al. introduced BERT."** Attribution error: Vaswani et al. introduced the Transformer [1]; BERT is Devlin et al. [2]. Corrected.
- **"BERT-Large reaches 81.5% on GLUE."** The cited figure is 80.5% [2]. Corrected.
- **"The GPT-3 paper reports 93.2 F1 on SQuAD v1.1."** Removed. The 93.2 SQuAD v1.1 F1 figure belongs to BERT-Large [2]; the research notes record no SQuAD result for GPT-3, so the claim is now attributed to BERT and no GPT-3 SQuAD number is stated.
- **"These results show that recurrence, pretraining, and scale are the three key ingredients."** Rewritten. "Recurrence" is contradicted by [1], and no cited paper asserts a three-ingredient causal conclusion; the Conclusion now presents the framing explicitly as an interpretation. No claim of demonstrated causality is retained.
