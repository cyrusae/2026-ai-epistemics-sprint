Verified the draft against the supplied research notes and the live sources, corrected the planted errors, and wrote the document.

**What changed in the body** (silent corrections, no audit section — consistent with the `noaudit-cited` output slot):
- EN–DE BLEU `41.8` → `28.4` (41.8 is EN–FR); improvement `5.1 BLEU` → `more than 2 BLEU`
- base model `16 heads` → `8 heads` (16 is the big model)
- EN–DE training set `36M` → `about 4.5 million` (36M is EN–FR)
- `GLUE and SQuAD` → WSJ Section 23 constituency parsing (§6.3; neither GLUE nor SQuAD occurs in the paper)
- fabricated quote "attention is all you need for vision as well" removed
- code URL `https://example.com/transformer-bleu` removed (HTTP 404; notes contain no verified code URL)
- paper ID `1706.03799` → `1706.03762` (1706.03799 resolves to *Verb Physics: Relative Physical Knowledge of Actions and Objects*)

**Source checks:** both cited URLs return HTTP 200; arXiv API record (v7, 2017-06-12, first author Ashish Vaswani) and OpenAlex `W2626778328` (DOI `10.48550/arxiv.1706.03762`) match the citation. Table 3 and §3.1/§3.2.2/§5.1/§5.2/§5.4/§6.3 values confirmed in the v7 HTML; `GLUE`/`SQuAD` confirmed absent. Both sources are cited; no orphan citations.