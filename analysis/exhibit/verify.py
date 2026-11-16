#!/usr/bin/env python3
"""Check coder findings against the corpus and merge them.

usage: verify.py <corpus-dir> <coders-dir> <out.md>
Coder outputs: coders/<coder>__<chunk>.jsonl (any text; lines that parse as JSON objects
with entry+quote are findings). A quote is VERIFIED if it occurs (whitespace- and
quote-mark-normalized) in that entry's full text, NEARBY if it occurs within ±3 entries,
else REJECTED.
"""
import json, sys, re, os, glob, collections
corpus, coders, outp = sys.argv[1:4]
index = json.load(open(f"{corpus}/index.json"))
order = list(index.keys()); pos = {k: i for i, k in enumerate(order)}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    s = s.replace("\\n", " ").replace("⏎", " ")
    return re.sub(r"\s+", " ", s).strip().lower()
cache = {}
def ntext(eid):
    if eid not in cache: cache[eid] = norm(index.get(eid) or "")
    return cache[eid]
rows, stats = [], collections.Counter()
for f in sorted(glob.glob(f"{coders}/*.jsonl")):
    coder, chunk = os.path.basename(f)[:-6].split("__", 1)
    for line in open(f):
        line = line.strip().strip(",")
        if not line.startswith("{"): continue
        try: d = json.loads(line)
        except Exception: stats[(coder, "unparseable")] += 1; continue
        eid, q = str(d.get("entry", "")).strip(), d.get("quote", "")
        qn = norm(q)[:300]
        status, where = "REJECTED", ""
        if eid in index and qn and qn in ntext(eid): status, where = "VERIFIED", eid
        elif qn:
            i = pos.get(eid)
            cand = order[max(0, i - 3): i + 4] if i is not None else []
            for c in cand:
                if qn in ntext(c): status, where = "NEARBY", c; break
        stats[(coder, status)] += 1
        rows.append(dict(coder=coder, chunk=chunk, code=d.get("code") or d.get("label") or "?", entry=where or eid,
                         claimed_entry=eid, quote=q, note=d.get("note", ""), status=status))
json.dump(rows, open(os.path.splitext(outp)[0] + ".json", "w"), indent=1, ensure_ascii=False)
L = ["# Merged coder findings", "", "## Verification by coder", "", "| coder | verified | nearby | rejected | unparseable |", "|---|---|---|---|---|"]
for c in sorted({k[0] for k in stats}):
    L.append(f"| {c} | {stats[(c,'VERIFIED')]} | {stats[(c,'NEARBY')]} | {stats[(c,'REJECTED')]} | {stats[(c,'unparseable')]} |")
ok = [r for r in rows if r["status"] != "REJECTED"]
fam = lambda c: c.split("-")[0]
L += ["", "## By code (verified + nearby only)", "", "Agreement = how many distinct coders flagged the same entry with the same code.", ""]
by = collections.defaultdict(list)
for r in ok: by[r["code"]].append(r)
for code, rs in sorted(by.items(), key=lambda x: -len(x[1])):
    ents = collections.defaultdict(list)
    for r in rs: ents[r["entry"]].append(r)
    L.append(f"### {code}: {len(ents)} entries, {len(rs)} findings\n")
    for e, rr in sorted(ents.items(), key=lambda x: (-len({r['coder'] for r in x[1]}), x[0])):
        cs = sorted({r["coder"] for r in rr})
        L.append(f"- **{e}** ({len(cs)} coder{'s' if len(cs)>1 else ''}: {', '.join(cs)}) — \"{rr[0]['quote'][:220]}\"")
        for r in rr: L.append(f"  - {r['coder']}: {r['note']}")
    L.append("")
rej = [r for r in rows if r["status"] == "REJECTED"]
L += ["## Rejected (quote not found)", ""] + [f"- {r['coder']} {r['claimed_entry']} [{r['code']}]: \"{r['quote'][:150]}\"" for r in rej]
open(outp, "w").write("\n".join(L) + "\n")
print("\n".join(L[:12 + len({k[0] for k in stats})]))
