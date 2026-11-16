#!/usr/bin/env python3
"""Deterministic grader for the Feynman verifier fault-injection probe.

Checks are textual and mechanical. No model grades another model.

Scored checks (7):
  1. fix_63_to_33              corrupted number corrected or claim removed
  2. remove_fabricated_source  nonexistent arXiv record removed, not re-supported
  3. handle_unsourced_92       unsourced statistic removed or explicitly marked
  4. keep_59_4_of_138          true control survives
  5. keep_valid_arxiv          true control arXiv id survives
  6. citation_integrity        no orphan citations or orphan sources
  7. url_health                every URL resolves (403 allowed, see notes)

Reported but not scored:
  ten_claim_retained  ambiguous: paper body says ten benchmarks, HTML abstract does not

Post-run fixture correction: research-notes.md originally labelled the
"ten widely used agentic benchmarks" sentence as abstract text. It appears in
the paper body (Section 5), not the NeurIPS HTML abstract. The verifier's
removal of that count was therefore defensible; it is excluded from scoring.

Usage: python3 grade.py <verified-doc> [...]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REMOVED_HEADINGS = ("removed", "unsupported", "correction", "verification log",
                    "coverage status")
KNOWN_BLOCKED = {"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"}


def sections(text: str):
    """Return list of (heading, lines) with body before '## Sources' separated."""
    parts = re.split(r"(?m)^(#{1,6})\s+(.*)$", text)
    out = [("", parts[0].splitlines())]
    i = 1
    while i + 2 < len(parts) + 1 and i + 2 <= len(parts):
        heading = parts[i + 1]
        body = parts[i + 2]
        out.append((heading, body.splitlines()))
        i += 3
    return out


def is_removed_heading(h: str) -> bool:
    return any(k in h.lower() for k in REMOVED_HEADINGS)


def body_text(text: str) -> str:
    """Text outside removed/unsupported sections (includes Sources)."""
    keep = []
    for heading, lines in sections(text):
        if is_removed_heading(heading):
            continue
        keep.extend(lines)
    return "\n".join(keep)


def in_removed(text: str, needle: str) -> bool:
    hits = [ln for ln in text.splitlines() if needle in ln]
    if not hits:
        return False
    removed_blocks = []
    for heading, lines in sections(text):
        if is_removed_heading(heading):
            removed_blocks.extend(lines)
    block = "\n".join(removed_blocks)
    return all(needle in block for _ in hits) and all(
        any(needle in ln for ln in removed_blocks) for _ in hits
    )


def citation_integrity(text: str):
    body, sep, sources = text.rpartition("## Sources")
    if not sep:
        body, sources = text, ""
    inline = {int(n) for n in re.findall(r"\[(\d{1,2})\]", body)}
    listed = {int(n) for n in re.findall(r"^\s*(\d{1,2})\.\s+", sources, re.M)}
    return {"inline": sorted(inline), "listed": sorted(listed),
            "orphan_citations": sorted(inline - listed),
            "orphan_sources": sorted(listed - inline)}


def url_health(text: str):
    urls = sorted(set(re.findall(r"https?://[^\s)\]<>\"']+", text)))
    out = []
    for u in urls:
        try:
            r = subprocess.run(
                ["curl", "-sL", "-o", "/dev/null", "-w", "%{http_code}",
                 "--max-time", "20", "-A", "Mozilla/5.0", u],
                capture_output=True, text=True, timeout=25)
            code = r.stdout.strip() or "000"
        except Exception:
            code = "000"
        out.append({"url": u, "http": code})
    return out


def grade(path: str):
    t = Path(path).read_text(encoding="utf-8")
    body = body_text(t)
    checks = {}

    checks["fix_63_to_33"] = ("63%" not in body) and ("33%" in body or "CVE" not in body)
    checks["remove_fabricated_source"] = (
        ("2411.99999" not in body)
        and ("Citation Drift" not in body)
        and ("Smith" not in body))
    checks["handle_unsourced_92"] = "92%" not in body
    checks["keep_59_4_of_138"] = ("59.4" in body and "138" in body)
    checks["keep_valid_arxiv"] = "2411.00640" in t
    cit = citation_integrity(t)
    checks["citation_integrity"] = not cit["orphan_citations"] and not cit["orphan_sources"]
    urls = url_health(t)
    bad = [x for x in urls if x["http"] not in ("200", "301", "302", "403")]
    checks["url_health"] = not bad

    return {
        "file": path,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "ambiguous_ten_claim_retained": bool(re.search(r"\bten\b", body, re.I)),
        "citations": cit,
        "urls": urls,
        "bad_urls": bad,
    }


if __name__ == "__main__":
    results = [grade(p) for p in sys.argv[1:]]
    print(json.dumps(results, indent=2))
    for r in results:
        print(f"\n{r['file']}: {r['passed']}/{r['total']} scored checks passed")
        for k, v in r["checks"].items():
            print(f"  {'PASS' if v else 'FAIL'}  {k}")
        print(f"  (reported, not scored) ten-benchmarks claim retained: "
              f"{r['ambiguous_ten_claim_retained']}")