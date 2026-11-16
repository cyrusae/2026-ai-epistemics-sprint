# How language models learned to attend

## Summary

The Transformer dispensed with recurrence and convolutions, relying solely on attention mechanisms [1]. BERT is pretrained with masked language modeling and next-sentence prediction [2]. GPT-3 has 175 billion parameters [3]. Together these papers trace a line from attention-only sequence transduction [1] to attention-based pretraining [2] to few-shot scaling [3].

## What changed

The Transformer reached 28.4 BLEU on the WMT 2014 English-to-German translation task [1]. BERT-Large reached 80.5% on the GLUE benchmark [2]. GPT-3 was trained on approximately 300 billion tokens [3].

## Conclusion

Together, the three papers describe attention-only sequence transduction [1], pretrained bidirectional representations [2], and large-scale few-shot learning [3].

## Sources

[1] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need.* NeurIPS 2017. arXiv:1706.03762. https://arxiv.org/abs/1706.03762
  - Record match: arXiv `1706.03762` (v7) and OpenAlex `W2626778328` (DOI 10.48550/arXiv.1706.03762) — title, year (2017), and first author (Ashish Vaswani) agree across both records. Semantic Scholar record `204e3073870fae3d05bcbc2f6a8e263d9b72e776` also matches (venue: NeurIPS).

[2] Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* NAACL-HLT 2019. arXiv:1810.04805. https://arxiv.org/abs/1810.04805
  - Record match: venue record DOI 10.18653/v1/N19-1423, OpenAlex `W2963341956`, year 2019, first author Jacob Devlin; arXiv preprint `1810.04805` (v2) carries the same title and authors but a 2018 preprint date (first submitted 2018-10-11). The 2019 date refers to the NAACL-HLT venue version, not the preprint.

[3] Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D. M., Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, B., Clark, J., Berner, C., McCandlish, S., Radford, A., Sutskever, I., & Amodei, D. (2020). *Language Models are Few-Shot Learners.* NeurIPS 2020. arXiv:2005.14165. https://arxiv.org/abs/2005.14165
  - Record match: arXiv `2005.14165` (v4) and OpenAlex `W3030163527` (DOI 10.48550/arXiv.2005.14165) — title, year (2020), and first author (Tom B. Brown) agree across both records.

## Removed Unsupported Claims

- "These three papers define the modern language-model stack" (Summary) — an evaluative historical claim not supported by the research notes; replaced with a descriptive statement of each paper's contribution.
- "The three papers shifted the field toward attention-based pretraining and scale" (Conclusion) — a claim about the field's subsequent direction not supported by the research notes; replaced with a descriptive statement of what the papers present.
- "The Transformer architecture replaced recurrence with self-attention" — "replaced" implies a historical outcome the sources do not establish; softened to the papers' own claim that the architecture dispenses with recurrence and convolutions.
