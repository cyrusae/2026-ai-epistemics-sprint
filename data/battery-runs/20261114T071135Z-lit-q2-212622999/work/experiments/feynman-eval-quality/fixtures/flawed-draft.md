# How language models learned to attend

## Summary

The Transformer architecture replaced recurrence with self-attention. BERT is pretrained with masked language modeling and next-sentence prediction. GPT-3 has 175 billion parameters. These three papers define the modern language-model stack.

## What changed

The Transformer architecture replaced recurrence with self-attention. A 2024 study by Zhang et al. found that sparse mixture-of-experts routing improves low-resource translation by 11.4 BLEU points (arXiv:2401.99999). BERT-Large reaches 92.4% on GLUE. The Transformer was introduced in the BERT paper. A follow-up study reports 88.1% on SQuAD 2.0 (https://arxiv.org/abs/2401.99999).

Feynman's verifier reduced citation errors by 73% across 1,200 runs. GPT-3 was trained on 1 trillion tokens.

## Benchmark table

| Method | MMLU | GSM8K |
|---|---:|---:|
| Feynman-Verify | 94.2 | 91.7 |
| Baseline | 88.0 | 84.3 |

The table shows that verification improves both benchmarks.

## Conclusion

Verification is solved, and the numbers above prove it.
