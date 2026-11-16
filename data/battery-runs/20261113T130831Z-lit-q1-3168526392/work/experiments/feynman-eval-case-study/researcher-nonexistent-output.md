# Verification Report: "Sparse Tensor Routing for Low-Power Federated Learning" (Zhang, Okafor, Lindqvist, 2022)

**Verdict: THE PAPER DOES NOT EXIST.**

No record of a paper titled "Sparse Tensor Routing for Low-Power Federated Learning" by authors named Zhang, Okafor, and Lindqvist (2022) was found in any of the bibliographic databases or web indexes checked. No DOI, venue, or direct URL can be returned because no such work is indexed anywhere.

Per instructions, no substitute paper is offered in its place. Papers listed in the "Near-miss / adjacent work" section below are recorded **only** to document that the search space was covered — none of them is this paper, and none should be cited as it.

## Coverage Status

### Searches performed (all returned zero exact matches)

| Query surface | Query executed | Result |
|---|---|---|
| Semantic Scholar Graph API (bulk title search) | `Sparse Tensor Routing for Low-Power Federated Learning` | `totalCount: 0`, `returned: 0` |
| arXiv API (title field, exact phrase) | `ti:"Sparse Tensor Routing for Low-Power Federated Learning"` | 0 entries (control query returned 3, so the API was working) |
| arXiv API (all fields, exact phrase) | `all:"sparse tensor routing"` | 0 entries |
| arXiv API (author fields) | `au:"Okafor" AND au:"Lindqvist"` | 0 entries |
| OpenAlex `title.search` filter | `title.search:"sparse tensor routing"` | `count: 0` |
| Crossref REST API `query.title` | exact title string, 20 rows returned | No item with this title |
| Crossref REST API `query.bibliographic` | title + author surnames | No item with this title |
| DBLP publication search | exact title string | No matching record (direct API access blocked by an anti-bot challenge; covered instead via web index of dblp.org, which surfaced no such entry) |
| Web search (Exa), 3 query variants | exact quoted title; title + authors; authors + year | No exact match; only topically adjacent FL/sparsity papers |
| Web search (parallel-mcp), 2 query variants | exact quoted title + authors; `"Low-Power Federated Learning"` + `"tensor routing"` | No exact match; only topically adjacent papers |

### What was checked directly vs. indirectly

- **Directly checked (machine-readable API responses):** Semantic Scholar, arXiv API, OpenAlex, Crossref. All four returned zero exact-title matches.
- **Indirectly checked:** DBLP. The `dblp.org` search API returned HTTP 202 with an Anubis anti-bot HTML challenge page on both plain and browser-UA requests, so no JSON was retrievable. The dblp index was instead probed through web search restricted to `dblp.org`, which returned only unrelated FL/sparsity records (`SparsyFed`, `Sparse Communication for Federated Learning`, `SparseMap`, etc.). This is a soft gap, not a positive hit.
- **Not checked:** Google Scholar (no reliable programmatic access in this environment), IEEE Xplore / ACM DL / SpringerLink direct search (no authenticated access; covered indirectly by Crossref, which registers DOIs for these publishers).

### Residual uncertainty

- Absence of evidence in the four major open bibliographic indexes plus the web index is strong but not mathematically conclusive. A paper could in principle exist in a closed, non-DOI-registered venue with no web footprint. However, the conjunction of (a) zero Semantic Scholar hits, (b) zero arXiv hits including author-name combination, (c) zero OpenAlex `title.search` hits, and (d) no Crossref title match is about as complete a negative as open sources permit.
- The author triple "Zhang, Okafor, Lindqvist" also produced no co-authored federated-learning work in Crossref author searches. Note that "Zhang", "Okafor", and "Lindqvist" are each extremely common surnames, so this author-level check is weak evidence on its own; it is corroborating, not decisive.

## Evidence table

| # | Source | URL | Key claim | Type | Confidence |
|---|--------|-----|-----------|------|------------|
| 1 | Semantic Scholar Graph API — title search endpoint | https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Sparse+Tensor+Routing+for+Low-Power+Federated+Learning&fields=title,year,authors,venue,citationCount,externalIds | Bulk title search returns `totalCount: 0` for the exact title | primary (API response, observed) | high |
| 2 | arXiv API — exact title query | https://export.arxiv.org/api/query?search_query=ti:%22Sparse+Tensor+Routing+for+Low-Power+Federated+Learning%22 | Returns 0 `<entry>` elements; a control query on the same endpoint returned 3 entries, confirming the endpoint worked | primary (API response, observed) | high |
| 3 | arXiv API — author-pair query | https://export.arxiv.org/api/query?search_query=au:%22Okafor%22+AND+au:%22Lindqvist%22 | Returns 0 entries for any co-authored work by an Okafor and a Lindqvist | primary (API response, observed) | medium |
| 4 | OpenAlex Works API — `title.search` filter | https://api.openalex.org/works?filter=title.search:%22sparse%20tensor%20routing%22 | `meta.count: 0` for the phrase in any title | primary (API response, observed) | high |
| 5 | Crossref REST API — title query | https://api.crossref.org/works?query.title=Sparse%20Tensor%20Routing%20for%20Low-Power%20Federated%20Learning&rows=20 | Top 20 results contain no item with this title; the closest titles are different works by different authors | primary (API response, observed) | high |
| 6 | Crossref REST API — bibliographic + author query | https://api.crossref.org/works?query.author=Okafor+Lindqvist&query.bibliographic=federated+learning+sparse+tensor&rows=8 | No co-authored Zhang/Okafor/Lindqvist FL work; returned unrelated Okafor-authored papers | primary (API response, observed) | medium |
| 7 | DeepReduce (Xu et al., NeurIPS 2021) — the closest genuine paper on sparse-tensor communication for FL | https://proceedings.neurips.cc/paper_files/paper/2021/hash/b0ab42fcb7133122b38521d13da7120b-Abstract.html | Authors are Hang Xu, Kelly Kostopoulou, Aritra Dutta, Xin Li, Alexandros Ntoulas, Panos Kalnis — **not** Zhang/Okafor/Lindqvist; title is different. Included only as the nearest real work, not as a substitute | primary | high |
| 8 | ZeroFL (Qiu et al., 2022) — arXiv:2208.02507 | https://arxiv.org/abs/2208.02507 | 2022 sparse on-device FL training paper; authors Xinchi Qiu, Javier Fernandez-Marques, Pedro PB Gusmao et al. — different authors, different title | primary | high |
| 9 | SpaFL (Kim, Saad, Debbah, Hong; NeurIPS 2024) — arXiv:2406.00431 | https://arxiv.org/abs/2406.00431 | Sparse-model FL with low computational overhead; different authors, different year, different title | primary | high |
| 10 | "Sparse Communication for Federated Learning" (Thonglek et al., ICFEC 2022) | https://www.computer.org/csdl/proceedings-article/icfec/2022/952400a001/1EmqTCekSJ2 | A real 2022 sparse-FL paper, but by Thonglek, Takahashi, Ichikawa, Nakasan, Leelaprute, Iida — **not** the claimed authors | primary | high |

## Findings

### 1. The claimed paper is not indexed anywhere

Semantic Scholar's bulk title search returns a total count of zero for the exact title [1]. The arXiv API returns zero entries for the exact title, for the phrase "sparse tensor routing" searched across all fields, and for the author combination Okafor + Lindqvist [2][3]. OpenAlex's `title.search` filter returns `count: 0` for "sparse tensor routing" in any title [4].

A control query against the same arXiv endpoint (searching `ti:"federated learning"`) returned 3 entries, which confirms the zero result above reflects a genuine absence rather than an API failure or malformed request [2].

### 2. Crossref has no DOI record for this title

Crossref's `query.title` endpoint returned 20 relevance-ranked candidates for the title string, none of which carries the title "Sparse Tensor Routing for Low-Power Federated Learning" [5]. Because Crossref is the DOI registration agency for IEEE, ACM, Springer, Elsevier, Wiley, and most major publishers, the absence of a Crossref record is strong evidence that no DOI exists for this paper.

The relevance ranking did surface a superficially similar 2026 title — "Expert-wise federated learning with sparse routing for distributed traffic prediction" (DOI 10.1016/j.comcom.2026.108635) — but this is a different paper, with a different title, different authors, and a different year (2026, not 2022). It is **not** the requested work and must not be treated as it [5].

### 3. Author-level checks find no such collaboration

A Crossref author search combining "Okafor" and "Lindqvist" with federated-learning/sparse-tensor terms returned no co-authored work matching the described paper; the returned Okafor-authored records were unrelated (healthcare FL, EEG Parkinson's detection, EV attack detection, etc.) [6]. The arXiv author-pair query returned zero entries [3].

An inference worth flagging explicitly: because "Zhang", "Okafor", and "Lindqvist" are all high-frequency surnames, author-name absence is weak standalone evidence. It is reported here as corroboration of the title-level absence, not as independent proof.

### 4. Adjacent real literature exists but none of it is this paper

The search space of "sparse tensor + federated learning + low power / communication efficiency" is genuinely populated, which is likely why the fabricated title reads as plausible:

- **DeepReduce** (NeurIPS 2021) is a real sparse-tensor communication framework for federated deep learning, by Hang Xu, Kelly Kostopoulou, Aritra Dutta, Xin Li, Alexandros Ntoulas, and Panos Kalnis [7]. It is the single closest real work in topic, and it shares neither the title nor any author with the claimed paper. Its own abstract describes decomposing sparse tensors into values and indices with independent/combined compression — a real and different contribution.
- **ZeroFL** (2022) addresses on-device sparse training for FL [8].
- **SpaFL** (NeurIPS 2024) addresses sparse-model FL with low computational overhead [9].
- **"Sparse Communication for Federated Learning"** (ICFEC 2022) is a real 2022 sparse-FL communication paper by a completely different author team [10].

None of these is "Sparse Tensor Routing for Low-Power Federated Learning," and none is by Zhang, Okafor, and Lindqvist. They are recorded here strictly to document search coverage and to make clear that the correct response to this request is "does not exist," not "here is something close."

### 5. Most likely explanation

Inference (not a source claim): the title pattern — three plausible but common surnames, a 2022 date, and a topic that sits exactly at the intersection of two well-populated research threads ("sparse tensors" and "low-power federated learning") — is characteristic of a synthetic or hallucinated citation. The topic is real; the specific paper is not.

## Sources

1. Semantic Scholar Graph API — bulk paper search, title query — https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=Sparse+Tensor+Routing+for+Low-Power+Federated+Learning&fields=title,year,authors,venue,citationCount,externalIds
2. arXiv API — exact title query for "Sparse Tensor Routing for Low-Power Federated Learning" — https://export.arxiv.org/api/query?search_query=ti:%22Sparse+Tensor+Routing+for+Low-Power+Federated+Learning%22
3. arXiv API — author-pair query `au:"Okafor" AND au:"Lindqvist"` — https://export.arxiv.org/api/query?search_query=au:%22Okafor%22+AND+au:%22Lindqvist%22
4. OpenAlex Works API — `filter=title.search:"sparse tensor routing"` — https://api.openalex.org/works?filter=title.search:%22sparse%20tensor%20routing%22
5. Crossref REST API — `query.title` for the exact title, 20 rows — https://api.crossref.org/works?query.title=Sparse%20Tensor%20Routing%20for%20Low-Power%20Federated%20Learning&rows=20
6. Crossref REST API — `query.author=Okafor+Lindqvist` + `query.bibliographic=federated learning sparse tensor` — https://api.crossref.org/works?query.author=Okafor+Lindqvist&query.bibliographic=federated+learning+sparse+tensor&rows=8
7. Hang Xu, Kelly Kostopoulou, Aritra Dutta, Xin Li, Alexandros Ntoulas, Panos Kalnis — "DeepReduce: A Sparse-tensor Communication Framework for Federated Deep Learning," NeurIPS 2021 — https://proceedings.neurips.cc/paper_files/paper/2021/hash/b0ab42fcb7133122b38521d13da7120b-Abstract.html
8. Xinchi Qiu, Javier Fernandez-Marques, Pedro PB Gusmao, et al. — "ZeroFL: Efficient On-Device Training for Federated Learning with Local Sparsity," arXiv:2208.02507, 2022 — https://arxiv.org/abs/2208.02507
9. Minsu Kim, Walid Saad, Merouane Debbah, Choong Seon Hong — "SpaFL: Communication-Efficient Federated Learning with Sparse Models and Low Computational Overhead," arXiv:2406.00431 / NeurIPS 2024 — https://arxiv.org/abs/2406.00431
10. Kundjanasith Thonglek, Keichi Takahashi, Kohei Ichikawa, Chawanat Nakasan, Pattara Leelaprute, Hajimu Iida — "Sparse Communication for Federated Learning," ICFEC 2022 — https://www.computer.org/csdl/proceedings-article/icfec/2022/952400a001/1EmqTCekSJ2
