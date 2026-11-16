#!/usr/bin/env python3
"""Build four synthetic /lit workdirs to probe evals/run.mjs scoring sensitivity.

Each case is a completed-looking artifact (plus provenance sidecar unless noted)
for q01 (test-time compute). The scorer never sees the model; it only sees text.
"""
import json, os, pathlib

ROOT = pathlib.Path("/work/experiments/feynman-eval-audit/work")
Q01_TITLE = "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
Q01_URL = "https://arxiv.org/abs/2408.03314"
ATTN_TITLE = "Attention Is All You Need"
ATTN_URL = "https://arxiv.org/abs/1706.03762"

cases = {
    # control: relevant claim, real ID, correct title
    "f1-control": (
        f"Test-time compute can be scaled more effectively than model parameters for reasoning tasks "
        f"[{Q01_TITLE}]({Q01_URL}).\n",
        True,
    ),
    # fabricated identifier: title is right, ID does not resolve
    "f2-fake-id": (
        f"Test-time compute can be scaled more effectively than model parameters for reasoning tasks "
        f"[{Q01_TITLE}](https://arxiv.org/abs/2408.99999).\n",
        True,
    ),
    # real, resolvable, correctly titled, irrelevant to the question
    "f3-irrelevant": (
        f"Test-time compute can be scaled more effectively than model parameters for reasoning tasks "
        f"[{ATTN_TITLE}]({ATTN_URL}).\n",
        True,
    ),
    # correct citation, absurd unsupported quantitative claim
    "f4-absurd-number": (
        f"Test-time compute improves MATH accuracy by 1000% [{Q01_TITLE}]({Q01_URL}).\n",
        True,
    ),
    # correct ID, wrong title on the same line
    "f5-wrong-title": (
        f"Test-time compute can be scaled more effectively than model parameters "
        f"[Scaling Laws for Neural Language Models]({Q01_URL}).\n",
        True,
    ),
    # bare arXiv ID, no URL/prefix and no exact key-paper title
    "f7-bare-id": (
        "Test-time compute scaling (Snell et al.) 2408.03314.\n",
        True,
    ),
    # key paper appears only in a rejected-sources list
    "f8-rejected": (
        f"# Test-time compute\n\n## Rejected sources\n\n"
        f"- [{Q01_TITLE}]({Q01_URL}) - not relevant to the final synthesis; excluded.\n",
        True,
    ),
    # artifact present, provenance sidecar missing
    "f6-no-provenance": (
        f"Test-time compute can be scaled more effectively than model parameters "
        f"[{Q01_TITLE}]({Q01_URL}).\n",
        False,
    ),
}

rows = []
for name, (body, with_prov) in cases.items():
    root = ROOT / name
    ws = root / "ws"
    out = ws / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    slug = "test-time-compute"
    (out / f"{slug}.md").write_text("# Test-time compute\n\n" + body)
    if with_prov:
        (out / f"{slug}.provenance.md").write_text("# Provenance\n\nSynthetic fixture for scorer probe.\n")
    (root / "home").mkdir(exist_ok=True)
    (root / "tmp").mkdir(exist_ok=True)
    rows.append({
        "case": name,
        "id": "q01",
        "workflow": "lit",
        "model": "fixture/none",
        "exit_code": 0,
        "timed_out": False,
        "wall_s": 0,
        "workdir": str(root),
        "usage": {"total_tokens": 0, "cost_usd": 0},
    })

rows.sort(key=lambda r: r["case"])
dest = pathlib.Path("/work/experiments/feynman-eval-audit/fixtures.jsonl")
dest.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
print(f"wrote {dest} with {len(rows)} cases under {ROOT}")
