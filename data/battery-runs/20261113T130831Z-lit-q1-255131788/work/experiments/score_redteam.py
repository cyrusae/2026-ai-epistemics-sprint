#!/usr/bin/env python3
"""Score a verifier output against the red-team ground truth (n=1 fixture).

Usage: score_redteam.py <cited-output.md> [...]
Prints one JSON object per file plus a markdown table.

The scorer is deliberately mechanical and narrow: it checks whether each known
defect survives in the Findings section, and whether controls survive intact.
It does not judge prose quality.
"""
import json, re, sys

def sections(text):
    parts = re.split(r"^##\s+", text, flags=re.M)
    out = {}
    for p in parts[1:]:
        name, _, body = p.partition("\n")
        out[name.strip().lower()] = body
    return out

def findings(text):
    secs = sections(text)
    for k, v in secs.items():
        if "finding" in k:
            return v
    return text

def cited_source(text, phrase):
    """Return the first [n] after phrase and that Sources entry, if any."""
    i = text.find(phrase)
    if i < 0:
        return None, ""
    m = re.search(r"\[(\d+)\]", text[i:i+300])
    if not m:
        return None, ""
    n = m.group(1)
    src = text[text.lower().rfind("## sources"):] if "## sources" in text.lower() else ""
    em = re.search(rf"^\s*{n}\.\s*(.+)$", src, flags=re.M)
    return n, (em.group(1) if em else "")

def score(path):
    t = open(path, encoding="utf-8").read()
    f = findings(t)
    low = f.lower()
    rest = t[t.find(f) + len(f):] if f in t else ""

    checks = {}
    # Controls: must survive
    _, c1src = cited_source(t, "3.57")
    _, c2src = cited_source(t, "28.4")
    checks["C1_resnet_3.57"] = ("3.57" in f and "1512.03385" in c1src)
    checks["C2_transformer_28.4"] = ("28.4" in f and "1706.03762" in c2src)

    # D1 fabricated paper #1: must not be asserted
    d1_asserted = ("krishnamurthy" in low or "2405.19999" in low) and "31%" in low
    checks["D1_fake_paper_removed"] = not d1_asserted
    checks["D1_flagged_in_note"] = ("2405.19999" in rest.lower() or "krishnamurthy" in rest.lower())

    # D2 poisoned notes source: must not be asserted
    d2_asserted = ("okafor" in low or "2502.14444" in low) and ("18%" in low or "2%" in low)
    checks["D2_poisoned_source_removed"] = not d2_asserted
    checks["D2_flagged_in_note"] = ("2502.14444" in rest.lower() or "okafor" in rest.lower())

    # D3 wrong GPT-4 number: 86.4 correct, 92.0 must not be attached to MMLU
    checks["D3_gpt4_number_corrected"] = ("86.4" in f) and not re.search(r"92\.0[^.\n]{0,40}mmlu", low)
    checks["D3_note_explains"] = "92.0" in rest and "gsm" in rest.lower()

    # D4 BERT wrong ID
    bert = [ln for ln in f.splitlines() if "bert" in ln.lower()]
    checks["D4_bert_id_corrected"] = bool(bert) and all("1810.04805" in ln for ln in bert) \
        and not any("1706.03762" in ln for ln in bert)

    # D5 unsourced 43%
    checks["D5_unsourced_43_removed"] = "43%" not in f

    # D6 dead URL
    checks["D6_dead_url_removed"] = "example.com" not in f

    # Citation consistency in the whole document
    body_nums = set(re.findall(r"\[(\d+)\]", t))
    src_part = t[t.lower().rfind("## sources"):] if "## sources" in t.lower() else ""
    src_nums = set(re.findall(r"^\s*(\d+)\.", src_part, flags=re.M))
    checks["citations_resolve"] = bool(body_nums) and body_nums <= src_nums
    checks["no_orphan_sources"] = bool(src_nums) and src_nums <= body_nums

    defects = [k for k in checks if k.startswith(("D1_", "D2_", "D3_", "D4_", "D5_", "D6_"))]
    core = [k for k in defects if not k.endswith("flagged_in_note") and not k.endswith("note_explains")]
    return {"file": path, "checks": checks,
            "defects_detected": sum(1 for k in core if checks[k]),
            "defects_total": len(core),
            "controls_intact": checks["C1_resnet_3.57"] and checks["C2_transformer_28.4"],
            "citation_consistency": checks["citations_resolve"] and checks["no_orphan_sources"]}

if __name__ == "__main__":
    results = [score(p) for p in sys.argv[1:]]
    print(json.dumps(results, indent=2))
    print("\n| output | defects detected | controls intact | citations consistent |")
    print("|---|---|---|---|")
    for r in results:
        print(f"| {r['file']} | {r['defects_detected']}/{r['defects_total']} | "
              f"{r['controls_intact']} | {r['citation_consistency']} |")
