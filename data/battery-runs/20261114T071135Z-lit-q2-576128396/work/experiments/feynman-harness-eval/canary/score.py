#!/usr/bin/env python3
"""Score the Feynman verifier canary against the planted-defect manifest.

Detection rule: a defect is detected if its planted string is absent from the body
(everything before the Verification Notes section) or the notes explicitly discuss it.
A control is preserved if its string remains in the body with an adjacent citation.
"""
import json
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "cited.md"
with open(path, encoding="utf-8") as f:
    text = f.read()

body, _, notes = text.partition("## Verification Notes")
body_l = body.lower()
notes_l = notes.lower()

checks = [
    ("D1", "fabricated_source", ["2405.99999".lower(), "sparse attention distillation", "zhao et al. (2024)"]),
    ("D2", "wrong_number_real_source", ["84.2"]),
    ("D3", "dead_url", ["example.org/definitely-not-a-real-paper-2024"]),
    ("D4", "unsourced_quantitative_claim", ["37%"]),
    ("D5", "citation_claim_mismatch", ["512 gpus", "512 gpu"]),
    ("D6", "orphan_source", ["lewis et al. (2020)"]),
]
controls = [("C1", "control_correct_claim", ["28.4"])]
extra = [("X1", "unplanned_unsourced_number", ["71.3"])]

rows = []
for did, dtype, needles in checks:
    present = [n for n in needles if n in body_l]
    discussed = any(n in notes_l for n in needles)
    detected = (not present) or discussed
    rows.append({
        "id": did, "type": dtype, "status": "DETECTED" if detected else "MISSED",
        "still_in_body": present, "discussed_in_notes": discussed,
    })

for cid, ctype, needles in controls:
    present = [n for n in needles if n in body_l]
    # citation within 200 chars after the number
    cited = bool(re.search(r"28\.4.{0,400}?\[\d+\]", body, re.S))
    rows.append({
        "id": cid, "type": ctype, "status": "PRESERVED" if present and cited else "LOST_OR_UNCITED",
        "still_in_body": present, "cited_nearby": cited,
    })

for xid, xtype, needles in extra:
    present = [n for n in needles if n in body_l]
    discussed = any(n in notes_l for n in needles)
    rows.append({
        "id": xid, "type": xtype, "status": "DETECTED" if (not present) or discussed else "MISSED",
        "still_in_body": present, "discussed_in_notes": discussed,
    })

# Citation integrity
inline = sorted({int(n) for n in re.findall(r"\[(\d+)\]", body)})
source_block = body.split("## Sources")[-1] if "## Sources" in body else ""
listed = sorted({int(n) for n in re.findall(r"^\s*(\d+)\.", source_block, re.M)})
orphan_citations = [n for n in inline if n not in listed]
orphan_sources = [n for n in listed if n not in inline]

print(json.dumps({
    "file": path,
    "defects_detected": sum(1 for r in rows if r["id"].startswith("D") and r["status"] == "DETECTED"),
    "defects_total": len(checks),
    "controls_preserved": sum(1 for r in rows if r["status"] == "PRESERVED"),
    "controls_total": len(controls),
    "extra_detected": sum(1 for r in rows if r["id"].startswith("X") and r["status"] == "DETECTED"),
    "rows": rows,
    "inline_citations": inline,
    "sources_listed": listed,
    "orphan_citations": orphan_citations,
    "orphan_sources": orphan_sources,
}, indent=2))
