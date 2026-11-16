#!/usr/bin/env python3
"""Check every judge quote against its packet; write derived/judges.json (scores + quote status) and a summary.

usage: verify_judges.py      (run from analysis/reproduction/judging)
Status: VERIFIED (exact after whitespace/quote normalisation in the cited file), ELSEWHERE (in another file
of the same packet), REJECTED (nowhere in the packet). A score > 0 whose quotes are all REJECTED is flagged.
"""
import json, os, glob, re, collections, csv

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    s = re.sub(r"[`*_]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()

texts = {}
def packet(unit):
    if unit not in texts:
        d = {}
        for p in glob.glob(f"packets/{unit}/**/*", recursive=True):
            if os.path.isfile(p):
                try: d[os.path.relpath(p, f"packets/{unit}")] = norm(open(p, errors="replace").read())
                except Exception: pass
        texts[unit] = d
    return texts[unit]

def check(unit, q, where):
    if not q: return "EMPTY"
    n = norm(q)
    if len(n) < 8: return "SHORT"
    P = packet(unit)
    w = (where or "").split(":")[0].split("#")[0].strip().lstrip("./")
    if w in P and n in P[w]: return "VERIFIED"
    # tolerate ellipses: all fragments present in order
    frags = [f for f in re.split(r"\s*(?:\.\.\.|…|\[\.\.\.\])\s*", n) if len(f) > 6]
    for name, t in P.items():
        if n in t or (len(frags) > 1 and all(f in t for f in frags)):
            return "VERIFIED" if name == w else "ELSEWHERE"
    return "REJECTED"

def evid(x):
    if isinstance(x, dict):
        if "quote" in x: yield x.get("quote"), x.get("where")
        for e in x.get("evidence") or []:
            if isinstance(e, dict): yield e.get("quote"), e.get("where")

res, stats = {}, collections.Counter()
for p in sorted(x for x in glob.glob("out/*__U*.json") if re.fullmatch(r"[a-z]+__U\d+\.json", os.path.basename(x))):
    judge, unit = os.path.basename(p)[:-5].split("__")
    j = json.load(open(p))
    for part in ("A", "C", "D"):
        for item, x in (j.get(part) or {}).items():
            if not isinstance(x, dict): continue
            st = [check(unit, q, w) for q, w in evid(x)]
            for s in st: stats[(judge, s)] += 1
            x["_quotes"] = st
            sc = x.get("score")
            x["_unsupported"] = bool(isinstance(sc, (int, float)) and sc > 0 and not any(s in ("VERIFIED", "ELSEWHERE") for s in st))
    for part in ("B", "E", "new_claims", "A_bonus", "audit_computed"):
        for x in j.get(part) or []:
            if isinstance(x, dict):
                st = [check(unit, q, w) for q, w in evid(x)]
                x["_quotes"] = st
                for s in st: stats[(judge, s)] += 1
    res[f"{judge}|{unit}"] = j
os.makedirs("derived", exist_ok=True)
json.dump(res, open("derived/judges.json", "w"), indent=1, ensure_ascii=False)
for k in sorted(stats): print(*k, stats[k])
print(len(res), "judge outputs")
