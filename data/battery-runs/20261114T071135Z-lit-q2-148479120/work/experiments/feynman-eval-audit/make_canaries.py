#!/usr/bin/env python3
"""Build canary documents for auditing Feynman's own evals/run.mjs scorer.

Each canary is a minimal final output (plus provenance sidecar) whose seeded
defect is known. Running `node evals/run.mjs --rescore seed.jsonl` then shows
which defect classes the shipped scorer can and cannot see.
"""
import json
import pathlib

BASE = pathlib.Path(__file__).resolve().parent

# (name, question id, filename, body, seeded defect)
CANARIES = [
    ("c0-correct", "q01", "test-time-compute-scaling.md", """# Test-time compute

Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (arXiv:2408.03314) reports that smaller models with extra inference compute can match larger models.
""", "none (control)"),
    ("c1-wrong-title-real-id", "q01", "test-time-compute-scaling.md", """# Test-time compute

Fast Inference from Transformers via Speculative Decoding (arXiv:2408.03314) is the central reference for test-time scaling.
""", "resolvable ID attached to a different paper's title"),
    ("c2-fabricated-id", "q01", "test-time-compute-scaling.md", """# Test-time compute

Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (arXiv:2499.99999) reports large gains.
""", "fabricated arXiv ID"),
    ("c3-right-paper-false-claim", "q01", "test-time-compute-scaling.md", """# Test-time compute

Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (arXiv:2408.03314) proves that additional test-time compute never improves accuracy and should not be used in practice.
""", "correct paper/title, claim contradicted by the paper"),
    ("c4-uncited-number", "q01", "test-time-compute-scaling.md", """# Test-time compute

Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters reports a 400% accuracy improvement on GSM8K from test-time compute alone.
""", "fabricated number, no citation"),
    ("c5-web-only", "q01", "test-time-compute-scaling.md", """# Test-time compute

The standard treatment is Sutton and Barto's Reinforcement Learning: An Introduction (http://incompleteideas.net/book/the-book-2nd.html), which covers the relevant control problem.
""", "web/book source only, no arXiv ID or DOI"),
    ("c6-pmid-only", "q04", "crispr-base-editing.md", """# CRISPR base editing

Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage is reported in PMID 27096365.
""", "key paper cited by PMID only"),
    ("c7-generic-citation-line", "q01", "test-time-compute-scaling.md", """# Test-time compute

For details see this paper (arXiv:2408.03314).
""", "correct ID, terse citation line (no title)"),
    ("c8-reference-only-contradiction", "q01", "test-time-compute-scaling.md", """# Test-time compute

Test-time compute is ineffective and should not be used; the evidence is unambiguous.

## References

1. Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (arXiv:2408.03314)
""", "body contradicts the cited paper; citation only in References"),
    ("c9-doi-correct", "q04", "crispr-base-editing.md", """# CRISPR base editing

Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage (doi:10.1038/nature17946) introduced cytosine base editors.
""", "none (DOI control)"),
    ("c10-doi-wrong-title", "q04", "crispr-base-editing.md", """# CRISPR base editing

Genome-scale CRISPR-Cas9 knockout screening in human cells (doi:10.1038/nature17946) introduced cytosine base editors.
""", "resolvable DOI attached to a different paper's title"),
    ("c11-datacite-doi", "q04", "crispr-base-editing.md", """# CRISPR base editing

An archived dataset (doi:10.5281/zenodo.8404160) is cited alongside the key result.
""", "DataCite DOI: resolves via handle, no Crossref title"),
]


def main() -> None:
    rows = []
    for name, qid, fname, text, defect in CANARIES:
        root = BASE / "work" / name
        out = root / "ws" / "outputs"
        out.mkdir(parents=True, exist_ok=True)
        (out / fname).write_text(text, encoding="utf-8")
        (out / fname.replace(".md", ".provenance.md")).write_text(
            "# Provenance\n\n- Verification: PASS\n", encoding="utf-8"
        )
        (root / "home").mkdir(exist_ok=True)
        (root / "tmp").mkdir(exist_ok=True)
        rows.append({"id": qid, "workdir": str(root), "canary": name, "defect": defect})
    (BASE / "seed.jsonl").write_text(
        "\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8"
    )
    (BASE / "canary-key.json").write_text(
        json.dumps({r["canary"]: r["defect"] for r in rows}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(rows)} canaries")


if __name__ == "__main__":
    main()
