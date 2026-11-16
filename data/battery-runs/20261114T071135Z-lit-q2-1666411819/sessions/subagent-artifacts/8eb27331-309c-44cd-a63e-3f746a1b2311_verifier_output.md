Verification complete. `verified.md` contains only claims traceable to primary sources, with inline citations and a three-entry Sources list. `draft.md` was not modified.

Key findings:
- **Fabricated paper:** `arXiv:2409.99999` ("[related work], Retrieval Calibration...") has no arXiv record, and Semantic Scholar returns zero hits for the title. The paragraph and its 31% claim were removed.
- **Contradicted claim:** the draft said RAG underperforms closed-book models and scores 94.2% EM on NQ. The paper's Table 1 reports RAG-Seq 44.5 / RAG-Token 44.1 vs closed-book T5-11B 34.5, and "94.2" appears nowhere in the PDF. Replaced with the actual table values.
- **Dead URL:** `https://feynman.is/docs/evals/research-quality` returns HTTP 404 (no archive or indexed eval page). The 12-question and 71%→100% claims were removed.
- **Uncited claim fixed:** Komor et al. had no source; added the Nature DOI/PubMed record after matching title, year, journal, and first author across PubMed, Europe PMC, and OpenAlex.
- **Identity checks:** Lewis 2020 matched on arXiv + Semantic Scholar; Vaswani 2017 matched on arXiv + Semantic Scholar; Komor 2016 matched on PubMed/Europe PMC + OpenAlex.