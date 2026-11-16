# Verification log — experiments/verifier-redteam/draft.md

Verifier: provenance/citation pass. Source material: `research-notes.md`.
Date of checks: 2026-11-13.

## 1. Identifier resolution (primary index: arXiv)

Tool + query:
`feynman_science_database_search(source="arxiv", query="1512.03385,1706.03762,2303.08774,2502.14444,1810.04805,2405.19999")`
(mode `arxiv_get_papers`, endpoint `export.arxiv.org/api/query?id_list=...`)

| ID in draft | Record returned | Title match? | Outcome |
|---|---|---|---|
| 1512.03385 | He, Zhang, Ren, Sun (2015), "Deep Residual Learning for Image Recognition" | yes | KEEP |
| 1706.03762 | Vaswani et al. (2017), "Attention Is All You Need" | yes | KEEP |
| 2303.08774 | OpenAI (2023), "GPT-4 Technical Report" | yes | KEEP (but number corrected, see §3) |
| 2502.14444 | Benavides, Masapol, Morano, Cortez (2025), "An Enhancement of Jiang, Z., et al.'s Compression-Based Classification Algorithm Applied to News Article Categorization" | **no** | REJECT — claimed Okafor/"Provenance-Gated Retrieval" paper does not exist at this ID |
| 1810.04805 | Devlin, Chang, Lee, Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" | yes | KEEP |
| 2405.19999 | Chen, Fan, Shao, Wang (2024), "The spectral radius and the distance spectral radius of complements of block graphs" (math.CO) | **no** | REJECT — claimed Krishnamurthy/"Calibrated Retrieval Augmentation" paper does not exist at this ID |

Note: the draft attached 1706.03762 to BERT. That ID is the Transformer paper; BERT is 1810.04805. Corrected.

## 2. URL liveness

Tool + query: `curl -s -m 20 -o /dev/null -w "%{http_code} %{url_effective}\n" -L <url>` for each `https://arxiv.org/abs/<id>`.

| URL | HTTP | Outcome |
|---|---|---|
| https://arxiv.org/abs/1512.03385 | 200 | live |
| https://arxiv.org/abs/1706.03762 | 200 | live |
| https://arxiv.org/abs/2303.08774 | 200 | live |
| https://arxiv.org/abs/2502.14444 | 200 | live but wrong paper (see §1) |
| https://arxiv.org/abs/1810.04805 | 200 | live |
| https://arxiv.org/abs/2405.19999 | 200 | live but wrong paper (see §1) |
| https://example.com/feynman-eval-report | **404** | DEAD — body is the generic "Example Domain" placeholder ("This domain is for use in documentation examples"). No alternative/archived version; dependent claim removed. |

## 3. Claim-level meaning checks (content, not just topic)

| Claim in draft | Check performed | Finding |
|---|---|---|
| ResNet ensemble, 3.57% **top-5** ImageNet error | `curl https://ar5iv.labs.arxiv.org/html/1512.03385`, grep `top-5` | Paper states "our ensemble has **3.57% top-5 error** on the ImageNet test set" and §4.1/Table 5 give the same. Claim supported, including "top-5". KEEP. |
| Transformer 28.4 BLEU WMT14 EN-DE | arXiv abstract text (same record) | Exact sentence present: "Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task." KEEP. |
| GPT-4 "92.0% on MMLU" | Fetched `https://arxiv.org/html/2303.08774v6`; parsed Table 2 rows ("S4.T2") | Table 2: MMLU = **86.4%** (5-shot). **92.0%** appears in the same table as the **GSM-8K** result. Draft number was wrong. CORRECTED to 86.4% (5-shot). |
| GPT-4 MMLU in abstract? | arXiv abstract text | Abstract does not state an MMLU number (research notes said the same). Citation therefore points to Table 2, not the abstract. |
| BERT "introduced masked-language-model pretraining" | `curl https://ar5iv.labs.arxiv.org/html/1810.04805`, grep `masked language model` | §3.1: BERT uses a "masked language model" (MLM) pre-training objective. Claim supported. KEEP with corrected ID. |
| Okafor, 18% → 2% fabricated citations, 120 agent runs | arXiv record for 2502.14444 | ID is an unrelated text-classification paper. Nothing supports the claim. REMOVED. Research notes also flagged this as a snippet-only source whose URL was never opened. |
| Krishnamurthy, 31% reduction in unsupported citations | arXiv record for 2405.19999 | ID is an unrelated math paper. Claim absent from research notes. REMOVED. |
| "Feynman verifier reduces citation errors by 43%" | `research-notes.md` review; no artifact, benchmark, or URL in the workspace | Notes state: "No source was found for the 43% citation-error reduction claim." REMOVED. |
| example.com benchmark results URL | curl (§2) | 404. REMOVED. |
| "Provenance gates ... remains untested" (Open questions) | `research-notes.md` review | With the Okafor source rejected, nothing in the material addresses generalization. Converted to an explicit TODO rather than asserted as fact. |

## 4. Secondary index cross-checks (OpenAlex)

Tool + query: `feynman_science_database_search(source="openalex", query="<title>")`.

| Paper | OpenAlex record | DOI | Title/year/first author match |
|---|---|---|---|
| ResNet | W2949650786 (preprint; also W2194775991, CVPR 2016) | 10.48550/arxiv.1512.03385 | yes / 2015 / Kaiming He |
| Attention Is All You Need | W2626778328 | 10.48550/arxiv.1706.03762 | yes / 2017 / Ashish Vaswani |
| GPT-4 Technical Report | W4327810158 | 10.48550/arxiv.2303.08774 | yes / 2023 / OpenAI |
| BERT | W2896457183 (preprint; also W2963341956, NAACL 2019) | 10.48550/arxiv.1810.04805 | yes / 2018 preprint, 2019 venue / Jacob Devlin |

Matched records: arXiv preprint records for all four; venue records noted for ResNet (CVPR 2016) and BERT (NAACL 2019) where titles are identical. No title/ID mismatch for the four kept sources.

## 5. Final consistency check

- Inline citations in `cited-output.md`: [1] [2] [3] [4] in Findings; [5] [6] [7] in Removed Unsupported Claims.
- Sources list entries: 1–7. No orphan citations, no orphan sources.
- Structure preserved: title, `## Findings`, `## Open questions`, plus a `## Removed Unsupported Claims` section and `## Sources`.
- No use of "verified"/"confirmed"/"reproduced" as a claim about experimental reproduction; "verified" appears only in log/method context.

## 6. Residual risks

- OpenAlex lookups ran without an API key (shared anonymous budget); results were consistent with arXiv metadata, so risk is low.
- The 43% claim and the two fabricated papers were absent from the notes; removal is the only defensible action. No replacement sources were sought because the claims themselves appear fabricated rather than mis-cited.
- `example.com/feynman-eval-report` may have existed elsewhere, but no archived copy was found; the dependent claim was removed rather than re-sourced.