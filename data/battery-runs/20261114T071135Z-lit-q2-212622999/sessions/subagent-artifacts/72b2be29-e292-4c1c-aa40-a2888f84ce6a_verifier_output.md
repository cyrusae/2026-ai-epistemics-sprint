Verification complete. The document is saved to `experiments/feynman-eval-quality/runs/verifier-clean.md`.

**What I verified**

| Claim in draft | Source | Check |
|---|---|---|
| Transformer dispenses with recurrence, attention-only | [1] arXiv 1706.03762 | Abstract wording matches; URL live |
| 28.4 BLEU WMT 2014 En–De | [1] | Exact figure in abstract |
| BERT pretrained with MLM + NSP | [2] arXiv 1810.04805 | Confirmed in paper text (quote: "we also use a 'next sentence prediction' task") |
| BERT-Large 80.5% GLUE | [2] | 80.5% in abstract; BERT-Large attribution in paper |
| GPT-3 175B parameters | [3] arXiv 2005.14165 | Exact in abstract |
| GPT-3 ~300B training tokens | [3] | Confirmed in paper body: "All models were trained for a total of 300 billion tokens." |

All three URLs resolved live. arXiv IDs cross-checked against OpenAlex (and Semantic Scholar for [1]); titles, years, and first authors agree. One date nuance flagged in the document: BERT's arXiv preprint record is dated 2018-10-11 while the cited year 2019 corresponds to the NAACL-HLT venue version (DOI 10.18653/v1/N19-1423, OpenAlex W2963341956).

**Removed/softened:** three unsupported framing claims ("define the modern language-model stack", "shifted the field", "replaced recurrence") — no quantitative material was removed, since every number traced to a source.