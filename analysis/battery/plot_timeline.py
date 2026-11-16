#!/usr/bin/env python3
"""Static timeline figure for the paper: one block per run-turn, shared minute axis.

usage: uv run --with matplotlib python plot_timeline.py derived/timeline.tsv derived/timeline   (writes .pdf and .png)

Each block: the lead's lane (model calls blue, tool calls orange; gaps = harness/bookkeeping),
then sub-agent sessions packed into as few lanes as they need (aqua; overlapping = concurrent).
Blocks sorted by lead wall time. Colors: reference palette slots 1-3 (validated all-pairs).
"""
import csv, sys, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

src, stem = sys.argv[1:3]
MODEL, TOOL, SUB = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"

rows = list(csv.DictReader(open(src), delimiter="\t"))
for r in rows: r["t0"], r["t1"] = float(r["t0"]) / 60, float(r["t1"]) / 60
# one block per run; later turns placed back to back after the previous turn (idle time removed)
PAD = 20 / 60
byturn = collections.defaultdict(list)
for r in rows: byturn[(r["run"], int(r["turn"]))].append(r)
blocks, breaks = collections.defaultdict(list), collections.defaultdict(list)
for run, turn in sorted(byturn):
    off = 0
    if blocks[(run, 1)]:
        off = max(r["t1"] for r in blocks[(run, 1)] if r["kind"] != "session" or r["session"] == "L") + PAD; breaks[(run, 1)].append(off - PAD / 2)
    for r in byturn[(run, turn)]: r["t0"] += off; r["t1"] += off; blocks[(run, 1)].append(r)
def wall(k): return max(r["t1"] for r in blocks[k] if r["session"] == "L")
import os
keys = sorted(blocks) if os.environ.get("SORT") == "run" else sorted(blocks, key=wall, reverse=True)

def pack(spans):
    lanes = []
    for s in sorted(spans, key=lambda r: r["t0"]):
        for lane in lanes:
            if lane[-1]["t1"] <= s["t0"]: lane.append(s); break
        else: lanes.append([s])
    return lanes

layout, y = [], 0
for k in keys:
    subs = pack([r for r in blocks[k] if r["kind"] == "session"])
    layout.append((k, y, subs)); y += 1 + len(subs) + 0.9 + (0.8 if breaks[k] else 0)
H = y
fig, ax = plt.subplots(figsize=(7.2, max(4, H * 0.16)))
for k, y0, subs in layout:
    lead = [r for r in blocks[k] if r["session"] == "L"]
    ax.broken_barh([(r["t0"], max(r["t1"] - r["t0"], 0.02)) for r in lead if r["kind"] == "model"], (y0, 0.8), facecolors=MODEL, linewidth=0)
    ax.broken_barh([(r["t0"], max(r["t1"] - r["t0"], 0.02)) for r in lead if r["kind"] == "tool"], (y0, 0.8), facecolors=TOOL, linewidth=0)
    for i, lane in enumerate(subs):
        ax.broken_barh([(r["t0"], r["t1"] - r["t0"]) for r in lane], (y0 + 1 + i, 0.7), facecolors=SUB, edgecolors="white", linewidth=0.6)
    run, turn = k
    label = run.replace("lit-", "") + (f"  ({len(breaks[k]) + 1} turns)" if breaks[k] else "")
    for i, bx in enumerate(breaks[k]):
        ax.plot([bx, bx], [y0 - 0.3, y0 + 1 + len(subs)], color=MUTED, linewidth=0.8, linestyle=(0, (2, 2)))
        ax.text(bx + 0.1, y0 + 1 + len(subs) + 0.2, f"turn {i + 2}" + (" (human reply; idle time removed)" if len(breaks[k]) == 1 else ""), fontsize=5.5, color=MUTED, va="top")
    ax.text(-0.3, y0 + 0.4, label, ha="right", va="center", fontsize=6.5, color=INK)
    if subs: ax.text(-0.3, y0 + 1 + len(subs) / 2 - 0.1, (lambda n: f"{n} sub-agent" + ("s" if n != 1 else ""))(sum(len(l) for l in subs)), ha="right", va="center", fontsize=5.5, color=MUTED)
ax.set_ylim(H, -0.5); ax.set_yticks([])
ax.set_xlim(0, max(r["t1"] for r in rows) * 1.02)
ax.set_xlabel("minutes since the human's message", fontsize=7, color=MUTED)
ax.tick_params(axis="x", labelsize=6.5, colors=MUTED, length=0)
ax.grid(axis="x", color=GRID, linewidth=0.6); ax.set_axisbelow(True)
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
ax.legend(handles=[Patch(color=MODEL, label="lead: model call"), Patch(color=TOOL, label="lead: tool call"), Patch(color=SUB, label="sub-agent session")],
          loc="lower right", fontsize=6.5, frameon=False, ncol=3, bbox_to_anchor=(1, 1.0))
fig.tight_layout()
for ext in ("pdf", "png"): fig.savefig(f"{stem}.{ext}", dpi=220, bbox_inches="tight")
print("wrote", stem + ".pdf/.png")
