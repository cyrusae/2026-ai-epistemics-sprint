# Direct research notes: Transformer WMT 2014 EN-DE BLEU

## Search/fetch log (exact queries and URLs)
1. `fetch_content` https://arxiv.org/abs/1706.03762 — abstract + metadata.
2. `feynman_science_database_search` source=arxiv query=`1706.03762` — arXiv API record (v7).
3. `fetch_content` https://arxiv.org/html/1706.03762v7 — full text incl. Table 2.
4. `web_search` query=`Attention Is All You Need WMT 2014 English-to-German BLEU 28.4 Table 2 27.3 base` — corroborating snippets (arXiv HTML, Google Research page, PDF).
5. `fetch_content` https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html — NeurIPS abstract (shows 27.5 EN-DE).
6. `fetch_content` https://arxiv.org/abs/1706.03762v1 — v1 abstract (28.4).
7. `fetch_content` https://arxiv.org/abs/1706.03762v3 — v3 abstract (28.4).
8. `fetch_content` https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf — NeurIPS PDF body + Table 2.

## Findings
- arXiv ID: **1706.03762** ("Attention Is All You Need"), submitted 12 Jun 2017; latest v7 2 Aug 2023.
- Abstract (all arXiv versions checked: v1, v3, v7; NeurIPS PDF): "Our model achieves **28.4 BLEU** on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU."
- Table 2 (arXiv v7 HTML and NeurIPS PDF):
  - Transformer (base model): EN-DE **27.3**, EN-FR 38.1
  - Transformer (big): EN-DE **28.4**, EN-FR 41.8 (v7 HTML) / 41.0 (NeurIPS PDF table)
- Body §6.1: big model "establishing a new state-of-the-art BLEU score of 28.4", +2.0 over prior best incl. ensembles, 3.5 days on 8 P100 GPUs.

## Discrepancy found
- NeurIPS **HTML abstract metadata** page reports "27.5 BLEU on English-to-German ... 41.1" and "165 million parameters". This does **not** match the NeurIPS PDF (28.4; Table 2 base 27.3 / big 28.4) nor any arXiv version (v1 already 28.4). Inference: stale/early abstract text attached to the proceedings metadata page; the paper of record reports 28.4. Record as a caveat, not as an alternative headline number.
- Minor: v7 HTML body text says EN-FR 41.0 while its Table 2 and abstract say 41.8; irrelevant to EN-DE but indicates residual editing inconsistencies in v7.

## Bottom line
Answer: **28.4 BLEU (Transformer big, newstest2014 EN-DE)**, base model 27.3; **arXiv:1706.03762**.
