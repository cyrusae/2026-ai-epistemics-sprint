# Efficient sequence models: a short evidence note

Vaswani et al. (2017) introduced the Transformer at NeurIPS [1][4]. The Transformer dispenses with recurrence and convolutions, relying solely on attention mechanisms, including multi-head self-attention [1]. GPT-3 reaches 64.3% zero-shot accuracy on TriviaQA [2]. The Transformer is more parallelizable and requires significantly less time to train than the recurrent and convolutional models it replaced [1]. BERT is pretrained with masked-language-model and next-sentence-prediction objectives [3]. Devlin et al. (2019) released BERT at NAACL [3][5].

## Removed Unsupported Claims

- A specific "10x" training-cost reduction for the Transformer was removed. Neither the paper's abstract nor its results state a 10x figure; the paper reports only that the model is "more parallelizable and requiring significantly less time to train" [1].
- An incorrect zero-shot TriviaQA accuracy for GPT-3 was replaced with the figure reported in the paper: 64.3% zero-shot (68.0% one-shot, 71.2% few-shot) [2].
- Publication years were corrected: Vaswani et al. is 2017, not 2019 [1][4]; Devlin et al. is 2019, not 2021 [3][5].

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. "Attention Is All You Need." NeurIPS 2017; arXiv:1706.03762. https://arxiv.org/abs/1706.03762
2. Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al. "Language Models are Few-Shot Learners." 2020; arXiv:2005.14165. https://arxiv.org/abs/2005.14165
3. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." arXiv:1810.04805 (2019). https://arxiv.org/abs/1810.04805
4. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. "Attention is All you Need." Advances in Neural Information Processing Systems 30 (NeurIPS 2017), proceedings record. https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
5. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." In Proceedings of NAACL-HLT 2019, Volume 1 (Long and Short Papers), pp. 4171–4186. https://aclanthology.org/N19-1423/
