# Evidence Note: "Sparse Mixture-of-Experts Routing for Low-Resource Translation" (Zhang et al., arXiv:2401.99999)

**Research date:** 2026-11-14
**Requested artifact:** title, authors, year, venue, URL, reported BLEU improvement
**Verdict: ❌ PAPER CANNOT BE VERIFIED — it does not appear to exist.**

---

## 1. Bottom line

No publication matching the title *"Sparse Mixture-of-Experts Routing for Low-Resource Translation"* by "Zhang et al." at arXiv ID `2401.99999` could be located in **any** primary index checked. The arXiv identifier itself returns a hard "Article not found" from arXiv.org, and arXiv's own API reports `totalResults = 0` for both a title-field and an all-field exact-phrase query.

Per the integrity constraints of this task, **every requested field is reported as unverifiable rather than guessed.** In particular, **no BLEU improvement is reported here, because none could be read from any source.** Any number attributed to this paper by another agent or draft should be treated as fabricated until a real source is produced.

## 2. Field-by-field status

| Requested field | Status | Value |
|---|---|---|
| Title | **Unverified / not found** | Requested string does not match any indexed record [1][2][3][4] |
| Authors ("Zhang et al.") | **Unverified** | No author list exists to check; the surname "Zhang" is extremely common in this literature and cannot be used to disambiguate [3][4] |
| Year | **Unverified** | Cannot be established. The ID prefix `2401` would imply January 2024 submission, but the ID is not allocated [1][2] |
| Venue | **Unverified** | No venue record in Crossref, OpenAlex, or arXiv [3][4][2] |
| URL | **Does not resolve** | `https://arxiv.org/abs/2401.99999` → "Article 2401.99999 not found" [1] |
| Reported BLEU improvement | **Unverified — NOT REPORTED** | No source read; deliberately left blank (see §1) |

## 3. Verification checks performed (all negative)

### 3.1 arXiv ID lookup — fails
The arXiv API `id_list` lookup for `2401.99999` returns `n_found: 0` with the identifier listed under `not_found` [2]. Fetching the abstract page directly returns HTTP-level "Article not found" HTML with the text *"There is no record of an article with identifier '2401.99999'"* [1].

### 3.2 arXiv exact-title search — zero hits
Two independent arXiv API queries returned `<opensearch:totalResults>0`:
- `ti:"Sparse Mixture-of-Experts Routing for Low-Resource Translation"` → 0
- `all:"Sparse Mixture-of-Experts Routing for Low-Resource Translation"` → 0 [2]

Note this is the exact-phrase, quoted form; a zero here means the title string does not occur in arXiv metadata at all.

### 3.3 Plausibility of the identifier
Beyond the 404, the ID is structurally implausible for the stated month. January 2024 submissions are observed in the `2401.0xxxx`–`2401.17xxx` range; a well-formed-but-nonexistent ID such as `2401.99999` is a documented failure mode that arXiv rejects explicitly, rather than something that silently resolves [5][6]. This is corroborating, not load-bearing — the direct 404 in §3.1 is the primary evidence.

### 3.4 OpenAlex — no matching work
A relevance search for the exact title returned 7,865 loose matches but **none with this title**; the top hits are unrelated MoE papers (expert-choice routing, representation collapse, speech-recognition routing, multilingual routing surveys) [3].

### 3.5 Crossref — no matching work
A Crossref bibliographic query returned 2,675,947 loose matches and again **no record with this title**; top hits are unrelated [4].

### 3.6 Note on Semantic Scholar
The Semantic Scholar backend was unavailable during this session (HTTP 429 on the shared anonymous pool) and the tool transparently fell back to OpenAlex [3]. **This is the one index I could not query directly.** Given that arXiv (the claimed host), Crossref, and OpenAlex all return nothing, the probability that S2 holds a unique record for a paper absent from its own claimed preprint server is negligible. I flag it for completeness rather than as a live uncertainty.

## 4. Closest *real* papers (not the requested paper — do not substitute)

These genuinely exist and are topically adjacent. They are listed **only** so a downstream agent can avoid conflating them with the phantom citation, and so a legitimate replacement citation is available if the parent wants one. **None of these is "Zhang et al., arXiv:2401.99999," and none should be relabeled as such.**

- **Lingual-SMoE** — Zhao, Chen, Cheng, Chen, *"Sparse MoE with Language Guided Routing for Multilingual Machine Translation,"* ICLR 2024. Reports >5% BLEU over a dense counterpart on OPUS-100 [7]. Note: first author is **Zhao**, not Zhang; different title; different ID.
- **THOR-MoE** — *"Beyond Token-Level Routing: Task-Guided and Context-Aware Routing in Sparse MoE for Neural Machine Translation,"* arXiv:2505.14173 (May 2025) [8]. Reports 0.75 average BLEU over vanilla Top-p routing on multi-domain translation.
- **Elbayad, Sun, Bhosale** — *"Fixing MoE Over-Fitting on Low-Resource Languages in Multilingual Machine Translation,"* Findings of ACL 2023 (arXiv:2212.07571). This is the canonical low-resource MoE-translation paper and reports improvements in **chrF++**, not BLEU [9].

The existence of several same-topic papers with near-identical framing is a likely mechanism by which a plausible-sounding but non-existent citation could be generated.

## 5. Recommendation

Do **not** cite this paper. If a citation is required for the underlying claim about sparse MoE routing helping low-resource translation, substitute one of the verified works in §4 and attribute the specific number to the paper that actually reports it [7][8][9].

If the parent has an independent copy of the PDF, a DOI, or a different identifier, send it and this note can be revised against a primary source.

---

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | arXiv.org abstract page for 2401.99999 | https://arxiv.org/abs/2401.99999 | Returns "Article 2401.99999 not found"; "There is no record of an article with identifier '2401.99999'" | primary | high |
| 2 | arXiv API (export.arxiv.org), id_list + exact-phrase title/all queries | https://export.arxiv.org/api/query?id_list=2401.99999 | `not_found: ["2401.99999"]`, `n_found: 0`; title and all-field exact-phrase queries both `totalResults=0` | primary | high |
| 3 | OpenAlex works search (fallback from Semantic Scholar 429) | https://api.openalex.org/works?search=Sparse+Mixture-of-Experts+Routing+for+Low-Resource+Translation | 7,865 loose matches, none bearing the requested title; top hits unrelated | primary (index) | high |
| 4 | Crossref REST API bibliographic query | https://api.crossref.org/works?query=Sparse+Mixture-of-Experts+Routing+for+Low-Resource+Translation | 2,675,947 loose matches, no record with the requested title | primary (index) | high |
| 5 | arXiv identifier format documentation (as quoted in third-party scraper docs) | https://magpiescraper.com/scrape/arxiv/ | Well-formed but nonexistent IDs fail loudly, e.g. "no entries for 2401.99999" | secondary | medium |
| 6 | arXiv listing, Computer Science, January 2024 | https://arxiv.org/list/cs/2024-01 | January 2024 IDs observed in the 2401.0xxxx–2401.16xxx range | primary | medium |
| 7 | Zhao et al., "Sparse MoE with Language Guided Routing for Multilingual MT," ICLR 2024 | https://proceedings.iclr.cc/paper_files/paper/2024/hash/3b4e1336f775c3dba16ebbb8d2afd258-Abstract-Conference.html | Lingual-SMoE outperforms dense counterpart by >5% BLEU on OPUS-100 | primary | high |
| 8 | "Beyond Token-Level Routing..." (THOR-MoE), arXiv:2505.14173 | https://arxiv.org/html/2505.14173 | +0.75 avg BLEU vs Top-p routing, multi-domain translation | primary | high |
| 9 | Elbayad, Sun, Bhosale, Findings of ACL 2023 | https://arxiv.org/abs/2212.07571 | MoE regularization for low-resource MT; reports ~+1 chrF++ (not BLEU) | primary | high |

## Findings

The requested paper is not discoverable. The arXiv identifier `2401.99999` is unallocated and returns an explicit not-found page [1][2]. Exact-title searches of arXiv's own metadata return zero results in both title and full-text field modes [2]. Independent bibliographic indexes (OpenAlex, Crossref) contain no work with this title; their top results are topically similar but distinct papers [3][4]. Consequently the title, authors, year, venue, URL, and BLEU improvement are all **unverified**, and the BLEU figure is intentionally omitted rather than estimated [1][2][3][4].

The "Zhang et al." attribution cannot be salvaged by name search: the surname is among the most common in NLP, and with no real record there is no author list to match against [3][4]. *(Inference, not a source claim: the combination of a plausible-sounding title, a common Chinese surname, a January-2024-shaped ID, and a research area dense with similarly-titled real papers [7][8][9] is characteristic of a hallucinated citation.)*

## Coverage Status

**Checked directly:** arXiv abstract page (404), arXiv API identifier lookup, arXiv API exact-phrase title and all-field queries, OpenAlex works search, Crossref works query. All negative.

**Not directly checked:** Semantic Scholar (HTTP 429 rate limit; tool fell back to OpenAlex) [3]; Google Scholar (no API access from this environment); any paywalled venue proceedings. Given the paper's claimed host (arXiv) returns 404 for the ID and 0 hits for the title, these gaps do not change the verdict.

**Could not complete:** None of the requested fields could be populated, because the paper does not exist in any index reachable from this environment.

## Sources

1. arXiv.org — abstract page for identifier 2401.99999 (not found) — https://arxiv.org/abs/2401.99999
2. arXiv API — identifier and exact-phrase title/all-field queries — https://export.arxiv.org/api/query?id_list=2401.99999
3. OpenAlex — works search for the requested title — https://api.openalex.org/works?search=Sparse+Mixture-of-Experts+Routing+for+Low-Resource+Translation
4. Crossref REST API — bibliographic query for the requested title — https://api.crossref.org/works?query=Sparse+Mixture-of-Experts+Routing+for+Low-Resource+Translation
5. Magpie Scraper docs — arXiv vertical, not-found error behavior — https://magpiescraper.com/scrape/arxiv/
6. arXiv — Computer Science listings, January 2024 — https://arxiv.org/list/cs/2024-01
7. Xinyu Zhao, Xuxi Chen, Yu Cheng, Tianlong Chen — "Sparse MoE with Language Guided Routing for Multilingual Machine Translation," ICLR 2024 — https://proceedings.iclr.cc/paper_files/paper/2024/hash/3b4e1336f775c3dba16ebbb8d2afd258-Abstract-Conference.html
8. "Beyond Token-Level Routing: Task-Guided and Context-Aware Routing in Sparse MoE for Neural Machine Translation," arXiv:2505.14173 — https://arxiv.org/html/2505.14173
9. Maha Elbayad, Anna Sun, Shruti Bhosale — "Fixing MoE Over-Fitting on Low-Resource Languages in Multilingual Machine Translation," Findings of ACL 2023 — https://arxiv.org/abs/2212.07571
