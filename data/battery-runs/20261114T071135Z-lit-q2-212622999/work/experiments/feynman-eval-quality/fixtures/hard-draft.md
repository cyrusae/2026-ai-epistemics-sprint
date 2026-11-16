# Attention, pretraining, and scale

## Summary

The Transformer uses recurrence to encode sequence order. BERT is pretrained with masked language modeling and next-sentence prediction. GPT-3 has 1.75 trillion parameters. Vaswani et al. introduced BERT.

## Details

The Transformer reaches 28.4 BLEU on WMT 2014 English-to-German translation. BERT-Large reaches 81.5% on GLUE. The GPT-3 paper reports 93.2 F1 on SQuAD v1.1. GPT-3 is evaluated in few-shot settings without gradient updates.

## Conclusion

These results show that recurrence, pretraining, and scale are the three key ingredients.
