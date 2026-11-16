# Verification Review — `cited.md`

**Scope:** citation-accuracy and evidence-integrity audit of `cited.md` against (a) the sources it cites, (b) the supplied research material in `research-notes.md`. This is a verification pass, not a peer review. Every surviving citation was opened and checked; every removal justification that was checkable was checked.
**Date of checks:** 2026-11-13.
**Bottom line:** **Not safe to deliver as-is.** Two delivery-blocking defects. The good news is that no surviving citation is fabricated — all four arXiv IDs, all four OpenAlex IDs, and all four DOIs resolve to the claimed works. The blocking problems are a *verifiably false* statement inside the corrections section, and a document whose surviving content does not support its title.

---

## Summary

`cited.md` is a short (33-line) evidence note. It carries four findings (ResNet, Transformer, GPT-4/MMLU, BERT/MLM), one open question, and a "Removed or Corrected Unsupported Claims" section that acts as an audit trail for eight prior-draft claims. The audit-trail bullet for GPT-4 and the two "unrelated paper" fingerprints (arXiv:2405.19999, arXiv:2502.14444) are the substantive verification work in the document, and those specific factual claims hold up under independent checking.

Three of the four surviving findings are exactly right, down to the table number and shot count. The fourth (BERT) misattributes the origin of masked-language-model pre-training to BERT, which the cited source does not claim and in fact contradicts internally. The corrections section contains one categorical negative assertion that is false against the report it describes. Separately, the document's title and framing ("Evidence notes on provenance gating for research agents") are unsupported by anything left in the body: after the two provenance-gating sources were removed, no finding in the document concerns provenance gating at all.

## Audit log (what was actually checked, and how)

| # | Claim in `cited.md` | Check performed | Result |
|---|---|---|---|
| 1 | ResNet: "ensemble … 3.57% top-5 error on the ImageNet test set" [1] | arXiv 1512.03385 metadata + full text (ar5iv) | **Supported.** Abstract: "An ensemble of these residual nets achieves 3.57% error"; §1: "Our ensemble has **3.57% top-5** error on the ImageNet *test* set, and won the 1st place in ILSVRC 2015." The "top-5" qualifier is body text, not abstract text. |
| 2 | Transformer: "28.4 BLEU on WMT 2014 English-to-German" [2] | arXiv 1706.03762 metadata + abstract | **Supported verbatim.** |
| 3 | GPT-4: "86.4% on MMLU under a 5-shot evaluation (Table 2)" [3] | arXiv 2303.08774v6 full text (ar5iv) | **Supported exactly.** Table 2, §4 Capabilities: MMLU, GPT-4 86.4%, "5-shot". Section and table number both correct. |
| 4 | "BERT … introduced masked-language-model (MLM) pre-training" [4] | arXiv 1810.04805 full text (§1, §3.1) | **Not supported — mischaracterization.** See [M1]. |
| 5 | "The 92.0% figure is not in the report." | Full-text search of arXiv 2303.08774v6 | **FALSE.** See [F2]. |
| 6 | arXiv:2405.19999 = "spectral radius … complements of block graphs," Chen/Fan/Shao/Wang, 2024 | arXiv API by ID | **Confirmed exactly** (math.CO, v1, 2024-05-30; authors Xu Chen, Dongjun Fan, Rongxiao Shao, Guoping Wang). |
| 7 | arXiv:2502.14444 = "An Enhancement of Jiang, Z., et al.'s Compression-Based Classification Algorithm…," Benavides et al., 2025 | arXiv API by ID | **Confirmed exactly** (cs.CL, v1, 2025-02-20; authors Benavides, Masapol, Morano, Cortez). |
| 8 | "No record with the cited title or author was found in OpenAlex or Crossref" (Krishnamurthy) | Crossref query by title; OpenAlex title search | **Consistent** — no exact-title match returned. Method not documented in the document itself; see [M3]. |
| 9 | No traceable record for "Provenance-Gated Retrieval for Autonomous Research Agents" | OpenAlex title search; Semantic Scholar bulk search | **Consistent** — no match. Top hits are unrelated 2025–2026 provenance/agent papers. |
| 10 | `https://example.com/feynman-eval-report` is a placeholder with no benchmark content | HTTP fetch | **Confirmed** — HTTP 404, standard "Example Domain" notice page. |
| 11 | OpenAlex record IDs W2949650786, W2626778328, W4327810158, W2896457183 match title/first author/year | OpenAlex API by ID (`select=id,doi,title,publication_year,authorships,type`) | **All four correct**, including DOI match to the cited arXiv IDs. |
| 12 | Not checkable | Items 3–5 of the removal list refer to "the draft," which is not supplied | **Unverifiable as written.** See [M4]. |

## Strengths

- **[S1] No fabricated surviving citations.** Every one of the four remaining references resolves to the correct work at the correct identifier, and the four OpenAlex IDs and DOIs are accurate. That is the failure mode most likely in this genre, and it is absent from the surviving body.
- **[S2] The removals are the strongest part of the document, and they are correct on the facts that matter.** The two "unrelated paper" fingerprints are exact matches, not approximations — same title, same author set, same year, same primary category. That is genuine verification, not a plausible-sounding dismissal.
- **[S3] The GPT-4 correction is precise where precision is hard.** 86.4% / 5-shot / Table 2 / §4 "Capabilities" all check out; the author got the table number right, which is the detail most easily fudged.
- **[S4] Removal rather than silent repair.** The document records what was cut and why, instead of quietly editing numbers. Where claims were unsupported, the default was deletion, which is the right default for an evidence note whose downstream use is unknown.
- **[S5] One internal error was caught and fixed with the right reason** (BERT's arXiv ID swapped for the Transformer's; 1706.03762 → 1810.04805). The diagnosis is correct.

## Weaknesses

### [F1] **FATAL — the document does not deliver evidence on its stated subject.**
The title is "Evidence notes on provenance gating for research agents." Every surviving finding concerns an unrelated result (ResNet top-5 error, Transformer BLEU, GPT-4 MMLU, BERT pre-training). Both sources that mentioned provenance gating were removed as untraceable. Nothing in the body defines a "provenance gate," states a mechanism, or reports an effect. The four generic benchmark facts read as residue from an earlier, differently-scoped draft that were left in place because they happened to verify. A reader receiving this as "evidence notes on provenance gating" would be misled about what has been established; a reader receiving it as a package of verified ML facts would be misled by the title. The document cannot be delivered under this title.

### [F2] **FATAL — a false negative assertion in the corrections section.**
> "The 92.0% figure is not in the report."

This is false. 92.0% appears twice in the GPT-4 Technical Report: (i) Table 2, GSM-8K row, GPT-4 = "92.0%*" with a "5-shot chain-of-thought" evaluation label; (ii) Table 11 (Appendix D, contamination), GSM-8K = 92.0%. The "not in the report" framing is also the wrong diagnosis: the draft's 92.0% for MMLU is best explained as a **row-mix inside Table 2** — 92.0% is the GSM-8K cell in the same table that contains the correct 86.4% MMLU cell. That is a materially different finding (transcription/lookup error in a source that *was* consulted) from "a number that does not exist" (fabrication). In a document whose entire value is the reliability of its negative claims, one categorical negative claim that is demonstrably wrong undermines the other four.

### [M1] **MAJOR — mischaracterization of the BERT source.**
> "BERT … introduced masked-language-model (MLM) pre-training [4]."

The BERT paper introduces *BERT*, and uses MLM as one of two pre-training objectives. It explicitly attributes the objective elsewhere: "we … use a 'masked language model' (MLM) pre-training objective, **inspired by the Cloze task [Taylor 1953]**," and in §3.1: "We refer to this procedure as a 'masked LM' (MLM), although it is often referred to as a Cloze task in the literature." Its own related work cites prior cloze-style objectives ([Fedus et al. 2018](https://arxiv.org/abs/1810.04805)) and prior LM pre-training ([Dai and Le 2015](https://arxiv.org/abs/1810.04805)). So the cited source, read end to end, does not support "introduced MLM pre-training" and provides part of the counter-evidence. This is a single-source priority/attribution claim carried by a source that is not a priority source for it — the exact pattern the removal list is supposed to catch, applied to text that was kept.

### [M2] **MAJOR — the open question presupposes a construct the document never establishes.**
> "Whether provenance gates generalize beyond English-language scientific text is an open question; the supplied research notes contain no study that evaluates it"

Two problems. (i) "Beyond English-language scientific text" smuggles in an established baseline result in English scientific text — no such result survives anywhere in the document, so the question has no established premise. (ii) The sentence's truth is trivially guaranteed by the document's own state (notes with no such study), so it reads as a substantive open question while carrying no information. "TODO: source needed" is honest; the surrounding sentence is not.

### [M3] **MAJOR — negative literature claims are asserted without a reproducible method.**
> "No record with the cited title or author was found in OpenAlex or Crossref"

I concur with the conclusion, but only after running the queries myself. The document does not state the query string, the database endpoint, whether matching was exact or fuzzy, or the date. Crossref title queries are fuzzy by default and return millions of "results," so "not found" is only meaningful under an exact-title/similarity criterion that the note never specifies. For an audit trail, an unreproducible negative is a weak negative — and it is the load-bearing claim for the largest removal.

### [M4] **MAJOR — most of the audit trail is unverifiable because the draft is not attached.**
The section is framed as "The following material **in the draft** could not be traced." Items 3–5 (the 43% production claim, the example.com URL, the corrected 92.0%) cannot be checked without the draft: the 43% claim is attested only by the notes, and the example.com URL I could only check because the URL itself was quoted. Either attach the draft (or an appendix of the exact removed sentences) or restate the section as "claims reviewed and rejected," with the rejected text quoted inline. As written, the reader cannot distinguish a real audit from a plausible narrative.

### [M5] **MAJOR — a supplied source is dropped without saying what happened to its number.**
The notes' source 4 (Okafor et al., 18% → 2% fabricated citations over 120 runs) is cited nowhere in `cited.md` and does not appear in the Sources list. The removal bullet correctly notes the snippet was never opened and that the arXiv ID resolves to a different paper. But the document never says the obvious consequence: **the 18% → 2% figure itself is now untraced**, not merely mis-addressed. It is possible a real paper exists whose ID was misrecorded, in which case "removed as untraceable" is right but "removed as fabricated attribution" would be wrong. The note should state which it is claiming.

### Minor

- **[m1]** Sources entry 4 says "preprint record dated 2018 … title, first author, and year match" while the reference itself is dated 2019. OpenAlex's `publication_year` for W2896457183 is 2018 (preprint), so the parenthetical is honest — but "year match" then contradicts the "(2019)" citation year. Pick one convention and state it.
- **[m2]** "The original Transformer reaches 28.4 BLEU" omits the configuration that makes the number comparable: the *big* model, newstest2014, single model (the base model is 27.3). Not an error; a comparability gap if the note is reused.
- **[m3]** The ResNet "top-5" qualifier is supported by §1 of the paper, not the abstract that the notes quote. Worth annotating the source-of-truth location, since the numbers differ between top-1 and top-5 and the note is the kind of artifact people cite secondhand.
- **[m4]** The GPT-4 finding omits the report's own contamination caveat: Table 11 gives MMLU contamination ~0.6% with degradation "-" (not computed). If the note's purpose is to characterize a benchmark number as "verified," that caveat belongs next to it.
- **[m5]** Reference numbering drifts from the notes (notes' source 5 → document's [4]; notes' source 4 unlisted). Harmless internally, confusing if the two documents are read together.
- **[m6]** The 43% bullet is a *vendor/product* claim about "Feynman's verifier," removed with the same rationale as a scholarly claim. It deserves a distinct label ("product/marketing claim, no external source exists") because no literature search could ever confirm it.

## Questions for Authors

- [Q1] Which draft is the removal list auditing? Can it be attached, or the removed sentences quoted inline, so items 3–5 become checkable? *(→ [M4])*
- [Q2] Was the 92.0% MMLU value traced back to Table 2's GSM-8K row, or was it only observed to be absent from the MMLU cell? The current wording asserts absence from the whole report, which the full text contradicts. *(→ [F2])*
- [Q3] What exact query and matching rule produced "no record … in OpenAlex or Crossref"? Was any secondary index (Semantic Scholar, Google Scholar, DBLP) consulted? *(→ [M3])*
- [Q4] What is a "provenance gate" as used in the title and open question, and which surviving sentence in the document supports any claim about it? *(→ [F1], [M2])*
- [Q5] Is the 18% → 2% figure claimed to be (a) fabricated alongside a fabricated citation, or (b) real but mis-addressed? The two support different conclusions about the source material. *(→ [M5])*
- [Q6] Does "introduced MLM pre-training" mean "introduced the BERT model using MLM" or a priority claim over the Cloze-task lineage? If the former, reword; if the latter, the BERT paper is not adequate support. *(→ [M1])*

## Verdict

**Not safe to deliver.** Two blocking defects: a categorical negative claim that is false against the primary source it describes [F2], and a document whose surviving content does not support its title or framing [F1]. Neither is a fabrication problem — the surviving citations are clean, and the two "unrelated paper" fingerprints are exactly right, which is the hardest verification in the document and it was done correctly. The failure mode is overconfident bookkeeping: the corrections section asserts more than was checked, and the retained body was never re-scoped after the removals.

Revision risk is moderate and the cost is low: both blocking items are fixable with text edits plus one re-scoped title, no new sourcing required for the four surviving facts. Confidence in these findings is high — every check in the audit log was run against the primary source (arXiv full text or API) or the index API directly, and the two contested points ([F2], [M1]) are settled by quotation from the source, not by inference.

## Revision Plan

1. **Fix [F2] first.** Replace the 92.0% bullet with the accurate finding: 92.0% is GPT-4's GSM-8K score in the same Table 2 (5-shot chain-of-thought, flagged `*` for training-set contamination), so the draft's MMLU figure is a row-mix inside a consulted table, not an absent number. Retitle the bullet "Corrected — value taken from the wrong row of Table 2."
2. **Re-scope [F1].** Either (a) retitle to what the document is — "Verified reference facts (4) plus rejected citations (5)" — and drop the provenance-gating framing entirely, or (b) hold delivery until at least one traceable provenance-gating source is found. Option (a) is honest and costs one sentence.
3. **Reword [M1]** to "BERT introduced the BERT model and used MLM as its primary pre-training objective, attributing the objective to the Cloze task [Taylor 1953]" — or add a second, dedicated priority source and label the claim as a priority claim.
4. **Delete or ground [M2].** Remove "beyond English-language scientific text" unless an English-language baseline is cited; otherwise state plainly: "No evidence on provenance gating was found; this section is empty pending sourcing."
5. **Document method for [M3].** One line per negative claim: query string, index, matching rule (exact title, normalized), date. Note which indexes were *not* searched.
6. **Attach or inline the draft [M4].** Quote each removed sentence verbatim in the bullet, or append the draft. Keep the bullet order stable so the audit trail is diffable.
7. **Split [M5] into fact and inference.** "arXiv:2502.14444 is Benavides et al. (verified); the 18%→2% figure has no traceable origin in the notes; whether a real source exists under a different ID is unresolved."
8. **Apply the minors** (m1–m6): one date convention, note the Transformer/ResNet configurations, add the GPT-4 contamination caveat, annotate where in the paper each number lives, and relabel the 43% item as a product claim.

---

## Inline Annotations

> "# Evidence notes on provenance gating for research agents"
**[F1] FATAL:** Nothing that follows concerns provenance gating. Both provenance-gating sources were removed (correctly), and no surviving finding defines or evaluates the construct. The title asserts a subject the body does not cover.

> "An ensemble of residual networks reaches 3.57% top-5 error on the ImageNet test set [1]."
**Verified.** Abstract: "An ensemble of these residual nets achieves 3.57% error"; §1: "Our ensemble has **3.57% top-5** error on the ImageNet *test* set … won the 1st place in ILSVRC 2015." Accurate, including "ensemble" and "top-5."
**[m3] MINOR:** The "top-5" qualifier lives in §1, not the abstract quoted in the notes. Annotate the location — the number is meaningless without the metric.

> "The original Transformer reaches 28.4 BLEU on WMT 2014 English-to-German translation [2]."
**Verified** against the abstract verbatim.
**[m2] MINOR:** Specify the *big* model / newstest2014 / single-model setting. The base model is 27.3 BLEU, and previous SOTA at 28.4-comparison was an ensemble; without the configuration the number is not reusable.

> "The GPT-4 Technical Report reports 86.4% on MMLU under a 5-shot evaluation (Table 2) [3]."
**Verified exactly** against arXiv 2303.08774v6, Table 2, §4 Capabilities: MMLU, GPT-4 86.4%, "5-shot". Table number and shot count both correct.
**[m4] MINOR:** Table 11 reports ~0.6% MMLU contamination in pre-training data with degradation not computed. Add it if this number is meant to carry weight downstream.

> "BERT: Pre-training of Deep Bidirectional Transformers (arXiv:1810.04805) introduced masked-language-model (MLM) pre-training [4]."
**[M1] MAJOR:** The source does not support "introduced MLM pre-training." BERT introduces BERT; the paper says the MLM objective is "inspired by the Cloze task [Taylor 1953]" and notes it "is often referred to as a Cloze task in the literature." It cites prior cloze-style objectives (Fedus et al. 2018) and prior LM pre-training (Dai and Le 2015). This is a priority claim resting on a non-priority source that partly contradicts it.

> "Whether provenance gates generalize beyond English-language scientific text is an open question; the supplied research notes contain no study that evaluates it (TODO: source needed)."
**[M2] MAJOR:** Presupposes an established English-language scientific-text result that appears nowhere in the document. As written the sentence is unfalsifiable by construction (the notes contain no such study, by definition). Replace with an explicit statement of absence.

> "The GPT-4 Technical Report ... reports 92.0% on MMLU." Corrected to 86.4% (5-shot, Table 2 of the report) [3]. **The 92.0% figure is not in the report.**
**[F2] FATAL:** False. 92.0% is in the report twice: Table 2, GSM-8K row (GPT-4, "92.0%*", 5-shot chain-of-thought) and Table 11 (Appendix D, GSM-8K = 92.0%). The correct diagnosis is a row-mix inside Table 2, not an invented number. Fix the wording and the diagnosis.

> "No record with the cited title or author was found in OpenAlex or Crossref, and the research notes list no source for this claim."
**[M3] MAJOR:** Conclusion is consistent with my own Crossref/OpenAlex title searches (no exact match), but the note records no query, no matching rule, and no date. Crossref title search is fuzzy and returns millions of hits, so "no record" is only meaningful under a stated exact-match criterion.

> "arXiv:2502.14444 resolves to an unrelated NLP paper ... The research notes also flag that this source was recorded from a search-result snippet and never opened."
**Verified** — the arXiv record is Benavides, Masapol, Morano & Cortez (cs.CL, 2025), title matches the document's quotation exactly.
**[M5] MAJOR:** The bullet stops one step short: it discredits the *citation* but never says the *number* (18% → 2%) is now untraced, and never distinguishes "fabricated" from "real paper, misrecorded ID."

> "**Krishnamurthy et al. (2024), "Calibrated Retrieval Augmentation for Scientific Agents" (arXiv:2405.19999), and its "31% reduction in unsupported citations."** Removed."
**Verified** — arXiv:2405.19999 is "The spectral radius and the distance spectral radius of complements of block graphs" (Chen, Fan, Shao, Wang; math.CO; 2024-05-30). Author set and year as stated.

> "**"Feynman's verifier reduces citation errors by 43% in production deployments."** Removed. The research notes state that no source was found for this claim."
**[m6] MINOR:** This is a product claim, not a literature claim; no search could confirm it. Label it as such so a later reader does not assume a failed search rather than an absent source.

> "4. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). ... (DOI 10.48550/arxiv.1810.04805; preprint record dated 2018, published at NAACL 2019); title, first author, and year match."
**[m1] MINOR:** "Year match" against a record dated 2018, cited as 2019. The parenthetical is accurate; the phrase "year match" is not. OpenAlex `publication_year` for W2896457183 is 2018.

> "The following material in the draft could not be traced to a source, or was contradicted by the source it cited."
**[M4] MAJOR:** "The draft" is not attached, so three of the five bullets are unverifiable by the reader. Quote the removed sentences inline.

---

## Sources

Primary sources opened or queried during this review:

- arXiv 1512.03385 (ResNet) — metadata + full text: https://arxiv.org/abs/1512.03385 ; https://ar5iv.labs.arxiv.org/html/1512.03385
- arXiv 1706.03762 (Transformer) — metadata: https://arxiv.org/abs/1706.03762
- arXiv 2303.08774v6 (GPT-4 Technical Report) — full text, Tables 2 and 11: https://arxiv.org/abs/2303.08774 ; https://ar5iv.labs.arxiv.org/html/2303.08774
- arXiv 1810.04805 (BERT) — full text, §1 and §3.1: https://arxiv.org/abs/1810.04805 ; https://ar5iv.labs.arxiv.org/html/1810.04805
- arXiv 2405.19999 (verification target for the removed Krishnamurthy citation): https://arxiv.org/abs/2405.19999
- arXiv 2502.14444 (verification target for the removed Okafor citation): https://arxiv.org/abs/2502.14444
- OpenAlex API records: https://api.openalex.org/works/W2949650786 ; /W2626778328 ; /W4327810158 ; /W2896457183
- Crossref title query: https://api.crossref.org/works?query=Calibrated+Retrieval+Augmentation+for+Scientific+Agents
- OpenAlex title search: https://api.openalex.org/works?search=Provenance-Gated+Retrieval+for+Autonomous+Research+Agents
- Semantic Scholar bulk search (provenance-gate / fabricated-citation literature): https://api.semanticscholar.org/graph/v1/paper/search/bulk
- Placeholder URL check: https://example.com/feynman-eval-report (HTTP 404, standard example-domain notice)
