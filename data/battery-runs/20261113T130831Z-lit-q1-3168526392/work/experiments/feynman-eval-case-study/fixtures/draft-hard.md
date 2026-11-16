# Efficient sequence models: a short evidence note

*(Draft. Citations to be verified.)*

Vaswani et al. (2019) introduced the Transformer at NeurIPS [1]. The Transformer replaces recurrence with multi-head self-attention [1]. GPT-3 reaches 95.2% zero-shot accuracy on TriviaQA [2]. The Transformer reduces training cost by 10x compared with recurrent networks [1]. BERT is pretrained with masked-language-model and next-sentence objectives [3]. Devlin et al. (2021) released BERT at NAACL [3].

## Sources

1. Vaswani et al., "Attention Is All You Need," NeurIPS 2017. https://arxiv.org/abs/1706.03762
2. Brown et al., "Language Models are Few-Shot Learners," 2020. https://arxiv.org/abs/2005.14165
3. Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers," 2019. https://arxiv.org/abs/1810.04805
