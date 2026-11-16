# Attention, pretraining, and scale

## Summary

The Transformer is a sequence-transduction architecture built solely on attention mechanisms, dispensing with recurrence and convolutions [1]. BERT is pretrained with two unsupervised objectives: masked language modeling and next-sentence prediction [2]. GPT-3 is an autoregressive language model with 175 billion parameters [3]. Vaswani et al. introduced the Transformer [1]; BERT was introduced by Devlin et al. [2].

## Details

The Transformer reaches 28.4 BLEU on the WMT 2014 English-to-German translation task [1]. BERT reaches 80.5% on the GLUE benchmark [2] and 93.2 F1 on SQuAD v1.1 [2]. GPT-3 is evaluated in few-shot, one-shot, and zero-shot settings without gradient updates [3].

## Conclusion

Read together, the three papers line up with attention-based architecture, pretraining, and scale, respectively [1][2][3]. This framing is an interpretive synthesis of the three papers' separate contributions; none of the three sources states it as a finding.

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* NeurIPS 2017. arXiv:1706.03762. https://arxiv.org/abs/1706.03762 (DOI 10.48550/arXiv.1706.03762). Link resolves to the arXiv abstract page; abstract contains the quoted "dispensing with recurrence and convolutions entirely" language and the 28.4 BLEU English-to-German result.
2. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* NAACL-HLT 2019. arXiv:1810.04805. https://arxiv.org/abs/1810.04805 (DOI 10.48550/arXiv.1810.04805). Link resolves; abstract reports GLUE 80.5% and SQuAD v1.1 Test F1 93.2.
3. Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al. (2020). *Language Models are Few-Shot Learners.* NeurIPS 2020. arXiv:2005.14165. https://arxiv.org/abs/2005.14165 (DOI 10.48550/arXiv.2005.14165). Link resolves; abstract reports "175 billion parameters" and evaluation "without any gradient updates or fine-tuning."

Citation scope note: the two objectives listed for BERT (masked language modeling and next-sentence prediction) come from the research notes' summary of the paper body, not from the abstract fetched above; the abstract only states that BERT is pretrained on unlabeled text with bidirectional context.

Cross-check record: all three arXiv IDs match records in both the arXiv index (1706.03762v7, 1810.04805v2, 2005.14165v4) and OpenAlex (W2626778328, W2896457183, W3030163527), with matching titles, years, and first authors. Two venue/preprint records exist for BERT (arXiv 2018 preprint and NAACL 2019 conference paper, DOI 10.18653/v1/n19-1423); the citation above uses the arXiv preprint record. The BERT arXiv record is dated 2018 while the venue year is 2019; both are consistent with the paper's publication history.

## Removed Unsupported Claims

The draft's factual statements were checked one by one against the research notes and the three primary papers. The following were contradicted by, or not traceable to, any permitted source and were corrected or removed:

1. **"The Transformer uses recurrence to encode sequence order."** Contradicted by [1], which describes the Transformer as "dispensing with recurrence and convolutions entirely." Replaced with the source's description.
2. **"GPT-3 has 1.75 trillion parameters."** [3] reports 175 billion parameters. Corrected to 175 billion.
3. **"Vaswani et al. introduced BERT."** [1] is the Transformer paper; BERT is by Devlin et al. [2]. Corrected and split into two attributions.
4. **"BERT-Large reaches 81.5% on GLUE."** [2] reports 80.5%. Corrected to 80.5%.
5. **"The GPT-3 paper reports 93.2 F1 on SQuAD v1.1."** The 93.2 SQuAD v1.1 F1 figure is BERT's [2], not GPT-3's; the research notes contain no GPT-3 SQuAD result. The GPT-3 attribution was removed and the figure retained only as a BERT result.
6. **Conclusion claim that "recurrence, pretraining, and scale are the three key ingredients."** "Recurrence" is contradicted by [1], and the three-part synthesis is not stated by any of the sources. Recast as an explicitly labeled interpretive synthesis, with no claim of demonstrated causation.

No unsupported tables, figures, charts, dataset sizes, or further benchmarks were present in the draft. No TODO placeholders were required; nothing was retained that lacks a traceable source.
