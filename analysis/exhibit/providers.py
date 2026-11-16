#!/usr/bin/env python3
"""Resolve OpenRouter generation ids (derived/response_ids.tsv) to upstream provider.
usage: OPENROUTER_API_KEY=... providers.py derived/response_ids.tsv derived/providers.tsv"""
import sys, os, json, time, urllib.request, collections
key = os.environ["OPENROUTER_API_KEY"]
rows = [l.rstrip("\n").split("\t") for l in open(sys.argv[1])][1:]
out = open(sys.argv[2], "w"); out.write("entry\tresponseId\tprovider_name\tmodel\tcost\tnative_tokens_prompt\tnative_tokens_completion\tfinish_reason\n")
c = collections.Counter()
for entry, rid, *_ in rows:
    if not rid.startswith("gen-"): continue
    for attempt in range(3):
        try:
            req = urllib.request.Request(f"https://openrouter.ai/api/v1/generation?id={rid}", headers={"Authorization": f"Bearer {key}"})
            d = json.load(urllib.request.urlopen(req, timeout=30))["data"]; break
        except Exception as e:
            d = {"provider_name": f"ERR {e}"}; time.sleep(1.5)
    c[(entry.split("-")[0][0] if "-" in entry else "L", d.get("provider_name"))] += 1
    out.write("\t".join(str(x) for x in (entry, rid, d.get("provider_name"), d.get("model"), d.get("total_cost"), d.get("native_tokens_prompt"), d.get("native_tokens_completion"), d.get("native_finish_reason") or d.get("finish_reason"))) + "\n")
    out.flush()
for k, v in sorted(c.items(), key=str): print(k, v)
