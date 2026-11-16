# Research notes: three foundational language-model papers

Scope: primary sources only. Each entry was read from the arXiv abstract/HTML page named below. Numbers are copied from the paper text.

## [1] Attention Is All You Need

- Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
- Year: 2017
- Venue: NeurIPS 2017
- URL: https://arxiv.org/abs/1706.03762
- arXiv ID: 1706.03762
- Key claims:
  - The Transformer is a sequence-transduction architecture based solely on attention mechanisms; it dispenses with recurrence and convolutions.
  - On WMT 2014 English-to-German translation it reaches 28.4 BLEU.
  - On WMT 2014 English-to-French translation it reaches 41.8 BLEU after training for 3.5 days on 8 P100 GPUs.
- Direct quote: "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."

## [2] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

- Authors: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- Year: 2019
- Venue: NAACL-HLT 2019
- URL: https://arxiv.org/abs/1810.04805
- arXiv ID: 1810.04805
- Key claims:
  - BERT is pre-trained with two unsupervised objectives: masked language modeling and next-sentence prediction.
  - BERT-Large reaches 80.5% on the GLUE benchmark.
  - BERT-Large reaches 93.2 F1 on SQuAD v1.1 and 83.1 F1 on SQuAD v2.0.
- Direct quote: "BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers."

## [3] Language Models are Few-Shot Learners

- Authors: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei
- Year: 2020
- Venue: NeurIPS 2020
- URL: https://arxiv.org/abs/2005.14165
- arXiv ID: 2005.14165
- Key claims:
  - GPT-3 is an autoregressive language model with 175 billion parameters.
  - GPT-3 is trained on approximately 300 billion tokens.
  - GPT-3 is evaluated in few-shot, one-shot, and zero-shot settings without gradient updates.
- Direct quote: "We train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model."

## Source-quality notes

- All three entries are primary papers with stable arXiv identifiers.
- No secondary summaries were used.
- No benchmark table beyond the numbers listed above was inspected.
