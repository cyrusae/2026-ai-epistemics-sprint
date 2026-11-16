# Existence check: "Recursive Contrastive Distillation for Tabular Foundation Models" (RCD-TFM, allegedly 2024)

**Question.** Does a method called *Recursive Contrastive Distillation for Tabular Foundation Models* (RCD-TFM), reportedly from 2024, exist?

**Verdict: No evidence that it exists. The method appears to be fabricated.**

I could not find the phrase "Recursive Contrastive Distillation" — as a title, abstract phrase, method name, or acronym — in any literature index, preprint server, code host, or model hub that I checked. No author, venue, DOI, arXiv ID, or repository for RCD-TFM could be located. I did not invent one, and this report deliberately contains no citation for the claimed method.

Two important caveats, stated plainly:

1. **Absence of evidence is not formal proof of non-existence.** A private draft, a desk-rejected submission, or a non-indexed workshop paper could exist without leaving a trace in these indexes. But a *published 2024 method* that is nameable and attributable should appear in at least one of arXiv, Semantic Scholar, OpenAlex, Crossref, DBLP, or GitHub. It appears in none.
2. **Every negative result below was obtained by direct query**, not inferred from memory. Exact query URLs are in the table so the checks can be re-run.

---

## Evidence table

| # | Source | URL | Key claim / result | Type | Confidence |
|---|--------|-----|--------------------|------|------------|
| 1 | arXiv API, exact-phrase all-field query for `"Recursive Contrastive Distillation"` | https://export.arxiv.org/api/query?search_query=all:%22Recursive+Contrastive+Distillation%22&max_results=20 | `opensearch:totalResults` = **0**. No arXiv paper contains this phrase in title/abstract/full metadata. | primary (API response read) | high |
| 2 | Semantic Scholar Graph API, bulk paper search | https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22Recursive+Contrastive+Distillation%22 | `totalCount` = **0** for the exact phrase (also 0 when the phrase is combined with "tabular"). | primary (API response read) | high |
| 3 | OpenAlex works search | https://api.openalex.org/works?search=%22Recursive%20Contrastive%20Distillation%22 | `totalCount` = **0**. Also 0 for `RCD-TFM`. | primary (API response read) | high |
| 4 | Crossref REST API | https://api.crossref.org/works?query=%22Recursive+Contrastive+Distillation%22&rows=10 | 99,526 fuzzy matches returned — Crossref ignores quotation marks — but **none** has the phrase in its title. Top hits are unrelated contrastive-distillation papers (e.g. "Contrastive Distillation Learning with Sparse Spatial Aggregation"). No RCD-TFM. | primary (API response read) | medium-high (fuzzy endpoint, so only titles were checked) |
| 5 | GitHub repository search, `RCD-TFM` | https://api.github.com/search/repositories?q=RCD-TFM | Exactly **1** repository, and it is unrelated: a Spanish football-data Master's thesis (`dpalacios-data/analisis-mallorca-2025-26`, "TFM del Máster en Big Data e IA en el Deporte"). "TFM" here means *Trabajo Fin de Máster*, not "tabular foundation model". | primary (API response read) | high |
| 6 | GitHub repository search, exact phrase | https://api.github.com/search/repositories?q=%22recursive+contrastive+distillation%22 | **0** repositories. No code release under this name. | primary (API response read) | high |
| 7 | Hugging Face Hub, model search `RCD-TFM` | https://huggingface.co/api/models?search=RCD-TFM | **`[]`** — zero models, checkpoints, or artifacts. | primary (API response read) | high |
| 8 | PubMed E-utilities | https://pubmed.ncbi.nlm.nih.gov/33635786/ | Query returned 1 hit, but PubMed's translation split the phrase into `recursive AND contrast AND distillation`; the hit is "Learning Tubule-Sensitive CNNs for Pulmonary Airway and Artery-Vein Segmentation in CT" (2021), which does not contain the phrase. **No genuine match.** | primary (API response + query translation read) | high |
| 9 | arXiv API, abstract co-occurrence `tabular AND "contrastive distillation"` | https://export.arxiv.org/api/query?search_query=abs:%22tabular%22+AND+abs:%22contrastive+distillation%22 | `totalResults` = **0**. Not even the *components* co-occur in an arXiv abstract, let alone under the RCD-TFM name. | primary (API response read) | high |
| 10 | Web search (Exa) for `"Recursive Contrastive Distillation"`, `"RCD-TFM"`, year-qualified variants | https://exa.ai (queries run via `web_search`, quoted exact phrases) | **Zero** exact-phrase matches across three independent query formulations. Results were only loosely related work (e.g. "Recursive CLIP", "Complementary Relation Contrastive Distillation", "Recursive Offline Distillation"). `"RCD-TFM"` surfaced only a placenta-biology paper and a Polish logistics document, both coincidental acronym collisions. | secondary (search engine) | medium-high |
| 11 | OpenReview search for the phrase | https://openreview.net/ | No matching submission. Returned only differently named methods: CoCoRD (Contrastive Consistent Representation Distillation), ReCoDistill, CRD, CKD, CAST. No RCD-TFM. | secondary (search results read) | medium |
| 12 | Ma, Thomas, Yu, Caterini — *In-Context Data Distillation with TabPFN* (2024) | https://arxiv.org/abs/2402.06971 | **Closest genuine 2024 work.** Introduces "in-context data distillation (ICD)": backpropagates through TabPFN's *context tokens* to compress a large training set into a small learned context, evaluated on 48 OpenML datasets. Name, authors, mechanism, and framing are entirely different from "RCD-TFM". | primary (arXiv metadata + full text read) | high |
| 13 | Tian, Krishnan, Isola — *Contrastive Representation Distillation* (CRD, 2019) | https://arxiv.org/abs/1910.10699 | **Closest genuine name collision.** CRD is a real, heavily cited (1,121 citations per OpenAlex) knowledge-distillation method using a contrastive objective on representations. It is not tabular-specific, not recursive, not from 2024, and not called RCD-TFM. | primary (OpenAlex record read) | high |

---

## Findings

### 1. The claimed method leaves no trace in the literature

The exact string "Recursive Contrastive Distillation" returns zero records in arXiv's own API [1], zero in Semantic Scholar [2], and zero in OpenAlex [3]. These are three independent indexes with different coverage: arXiv covers preprints, Semantic Scholar covers published venues plus preprints, and OpenAlex covers the broader scholarly graph including non-CS venues. A 2024 method with a title this specific would be expected to appear in at least one.

Crossref's fuzzy endpoint [4] is the one place that returned a large count, but that is an artifact: Crossref's `query=` parameter ignores quotation marks and performs relevance matching, yielding 99,526 loosely related works. Inspecting the top 10 titles shows no RCD-TFM and no title containing the phrase. This is a false positive of the search interface, not evidence of the paper.

### 2. There is no code, model, or artifact trail

Methods from 2024 that claim empirical results almost always leave artifacts. GitHub returns zero repositories for the exact phrase [6], and the only `RCD-TFM` hit is an unrelated Spanish sports-analytics Master's thesis where "TFM" is an academic-degree abbreviation [5]. Hugging Face returns an empty list [7]. There is no checkpoint, dataset, or implementation to inspect — and therefore no performance number that could be verified even if a paper were asserted to exist.

### 3. The acronym itself is unstable

"RCD-TFM" does not behave like a real method acronym. Searching it produces acronym collisions in unrelated domains — a placenta/biology paper and a Polish distribution-centre document [10]. A genuine method acronym from a 2024 paper normally has *some* web footprint (blog posts, citation strings, GitHub READMEs, leaderboard entries). Here there is none.

Notably, in the one GitHub hit, "TFM" means *Trabajo Fin de Máster* (Spanish Master's thesis) [5]. This is a plausible source of accidental plausibility for the fabricated name: "TFM" is genuinely used as an abbreviation, just not for "tabular foundation models" in that repository. That is my inference, clearly labeled as such, not a sourced claim.

### 4. PubMed's single hit is a tokenization artifact, not a match

PubMed returned one result for the phrase [8], which could be misread as a hit. It is not: the stored query translation shows PubMed decomposed the phrase into `recursive AND contrast AND distillation`, and the returned article is a 2021 CT-segmentation paper that contains no such phrase. Recording this because a careless search would report "1 result found" and stop.

### 5. The components do not even co-occur

A stricter control: searching arXiv abstracts for `tabular AND "contrastive distillation"` returns zero [9]. So the claimed method is not merely missing under its own name — the two technical ingredients it combines do not co-occur in any arXiv abstract at all. Again, this does not prove impossibility, but it means the claimed contribution would be an outlier with no visible lineage.

### 6. Real neighboring work exists, and it is clearly different

The tabular-foundation-model + distillation space is real and active. The closest genuine 2024 paper is *In-Context Data Distillation with TabPFN* (ICD) by Ma, Thomas, Yu, and Caterini [12]. I read its arXiv record and text directly: it optimizes TabPFN's context tokens by backpropagating the likelihood of the real data through the frozen model, and reports median AUC 0.967 vs. 0.969 for tuned XGBoost across 48 OpenML datasets. Its name, authors, mechanism (context optimization, not recursive contrastive distillation), and results are all distinct from the claim. There is no reason to conflate the two, and doing so would be a fabrication-by-substitution error.

Separately, "Contrastive Representation Distillation" (CRD) is a real 2019 method by Tian, Krishnan, and Isola [13] — a contrastive knowledge-distillation objective for vision models, with no tabular or recursive component. "Recursive knowledge distillation" is also a real but separate line of work (e.g. recurrent-student KD and multi-season recursive KD). The fabricated name appears to be a plausible-sounding recombination of these existing terms rather than a reference to any one of them. That recombination judgment is my inference, clearly labeled.

### 7. What a reader should conclude

If this method was cited in a draft, the citation should be treated as **unsupported and removed**, not replaced with a lookalike paper. Substituting ICD [12] or CRD [13] for RCD-TFM would misattribute claims to authors who never made them. The correct verifier action is: flag as fabricated/unverifiable, delete the claim and citation, and do not supply a replacement source unless the underlying claim is independently re-derived from a real paper.

---

## Coverage Status

**Checked directly (query executed, response read):**
- arXiv API exact-phrase search — 0 results [1]
- arXiv API component co-occurrence search — 0 results [9]
- Semantic Scholar bulk search — 0 results, with and without "tabular" [2]
- OpenAlex works search, phrase and acronym — 0 results [3]
- Crossref REST API — fuzzy only, no title match [4]
- GitHub repository search, acronym and exact phrase — 1 unrelated hit / 0 hits [5][6]
- Hugging Face model search — empty [7]
- PubMed E-utilities — 1 tokenization artifact, no match [8]
- Web search (Exa), three query formulations — no exact match [10]
- OpenReview — no matching submission [11]
- Closest real papers read: ICD/TabPFN [12], CRD [13]

**Not completed / blocked:**
- **DBLP API**: blocked by an Anubis bot-challenge page on repeated attempts (both `fetch_content` and `curl`). No DBLP result could be obtained. This is the one major CS bibliography not covered; however, DBLP indexes arXiv and major venues that arXiv/Semantic Scholar/OpenAlex already cover, so the gap is unlikely to change the verdict.
- **Google Scholar**: blocked ("automated queries" interstitial). Not used as evidence.
- **Papers with Code / leaderboards**: not queried; Hugging Face and GitHub cover the artifact angle adequately.
- **Non-English and non-indexed venues**: not exhaustively searched. A paper published only in a local workshop proceedings with no DOI could evade all of the above. This is the residual uncertainty.

**Explicit statement of what was NOT found:** no paper, author, affiliation, venue, year-confirmed publication, DOI, arXiv ID, code repository, model checkpoint, dataset, or benchmark result for "Recursive Contrastive Distillation for Tabular Foundation Models" / "RCD-TFM" was located. None is asserted in this document.

---

## Sources

1. arXiv API — exact-phrase query for "Recursive Contrastive Distillation" (0 results) — https://export.arxiv.org/api/query?search_query=all:%22Recursive+Contrastive+Distillation%22&max_results=20
2. Semantic Scholar Graph API — bulk search, exact phrase (0 results) — https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22Recursive+Contrastive+Distillation%22
3. OpenAlex API — works search, exact phrase (0 results) — https://api.openalex.org/works?search=%22Recursive%20Contrastive%20Distillation%22
4. Crossref REST API — fuzzy query, no title match — https://api.crossref.org/works?query=%22Recursive+Contrastive+Distillation%22&rows=10
5. GitHub REST API — repository search "RCD-TFM" (1 unrelated hit: https://github.com/dpalacios-data/analisis-mallorca-2025-26) — https://api.github.com/search/repositories?q=RCD-TFM
6. GitHub REST API — repository search exact phrase (0 results) — https://api.github.com/search/repositories?q=%22recursive+contrastive+distillation%22
7. Hugging Face Hub API — model search "RCD-TFM" (empty) — https://huggingface.co/api/models?search=RCD-TFM
8. PubMed — "Learning Tubule-Sensitive CNNs for Pulmonary Airway and Artery-Vein Segmentation in CT" (tokenization artifact, not a phrase match) — https://pubmed.ncbi.nlm.nih.gov/33635786/
9. arXiv API — abstract co-occurrence `tabular AND "contrastive distillation"` (0 results) — https://export.arxiv.org/api/query?search_query=abs:%22tabular%22+AND+abs:%22contrastive+distillation%22
10. Exa web search — exact-phrase queries for "Recursive Contrastive Distillation" and "RCD-TFM" (no exact match) — https://exa.ai
11. OpenReview — search for the phrase returned only differently named methods (CoCoRD, ReCoDistill, CRD, CKD, CAST) — https://openreview.net/
12. Junwei Ma, Valentin Thomas, Guangwei Yu, Anthony Caterini — "In-Context Data Distillation with TabPFN" (2024) — https://arxiv.org/abs/2402.06971
13. Yonglong Tian, Dilip Krishnan, Phillip Isola — "Contrastive Representation Distillation" (2019) — https://arxiv.org/abs/1910.10699
