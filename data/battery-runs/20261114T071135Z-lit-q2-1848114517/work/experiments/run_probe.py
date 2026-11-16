#!/usr/bin/env python3
"""Run isolated Feynman subprocess probes and summarize the persisted session traces.

Each probe gets its own cwd, session dir, and run dir so it cannot write into /work.
Parent PI_* session vars are stripped so the child cannot append to this session.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("/work/experiments")
MODEL = "openrouter/deepseek/deepseek-v4.1-flash-1017"
FEYNMAN = os.environ.get("FEYNMAN_BIN_PATH", "feynman")


def clean_env() -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if k not in ("PI_SESSION_FILE", "PI_SESSION_ID")}
    env["FEYNMAN_TELEMETRY"] = "off"
    return env


def summarize_session(path: Path) -> dict:
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    out = {
        "session_file": str(path),
        "entries": len(rows),
        "types": {},
        "assistant_turns": 0,
        "assistant_turns_with_usage": 0,
        "tool_calls": [],
        "tool_results": 0,
        "tool_errors": 0,
        "unpaired_tool_calls": [],
        "total_cost_usd": 0.0,
        "total_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "wall_ms_from_trace": None,
        "has_system_prompt": False,
        "has_temperature_field": False,
        "has_scaffold_version_field": False,
        "model": None,
        "thinking": None,
    }
    call_ids: list[str] = []
    result_ids: set[str] = set()
    stamps: list[int] = []
    for r in rows:
        out["types"][r.get("type")] = out["types"].get(r.get("type"), 0) + 1
        if r.get("type") == "model_change":
            out["model"] = f"{r.get('provider')}/{r.get('modelId')}"
        if r.get("type") == "thinking_level_change":
            out["thinking"] = r.get("thinkingLevel")
        if r.get("timestamp"):
            stamps.append(int(time.mktime(time.strptime(r["timestamp"][:19], "%Y-%m-%dT%H:%M:%S"))))
        msg = r.get("message") or {}
        role = msg.get("role")
        if role == "system":
            out["has_system_prompt"] = bool(msg.get("content") or msg.get("sections"))
        if role == "assistant":
            out["assistant_turns"] += 1
            usage = msg.get("usage")
            if usage:
                out["assistant_turns_with_usage"] += 1
                out["total_tokens"] += usage.get("totalTokens", 0)
                out["input_tokens"] += usage.get("input", 0)
                out["output_tokens"] += usage.get("output", 0)
                out["total_cost_usd"] += (usage.get("cost") or {}).get("total", 0) or 0
            if "temperature" in msg:
                out["has_temperature_field"] = True
            for block in msg.get("content") or []:
                if isinstance(block, dict) and block.get("type") == "toolCall":
                    call_ids.append(block.get("id"))
                    args = block.get("arguments")
                    out["tool_calls"].append(
                        {
                            "name": block.get("name"),
                            "args": args if isinstance(args, dict) else str(args)[:200],
                        }
                    )
        if role == "toolResult":
            out["tool_results"] += 1
            result_ids.add(msg.get("toolCallId"))
            if msg.get("isError"):
                out["tool_errors"] += 1
    out["unpaired_tool_calls"] = [c for c in call_ids if c not in result_ids]
    if stamps:
        out["wall_ms_from_trace"] = (max(stamps) - min(stamps)) * 1000
    out["has_scaffold_version_field"] = any("version" in r for r in rows if r.get("type") == "session")
    return out


def run(probe: str, idx: int, argv: list[str], timeout: int = 900) -> dict:
    run_dir = ROOT / "runs" / f"{probe}-{idx}"
    workspace = run_dir / "workspace"
    sessions = run_dir / "sessions"
    workspace.mkdir(parents=True, exist_ok=True)
    sessions.mkdir(parents=True, exist_ok=True)
    cmd = [FEYNMAN, *argv, "--session-dir", str(sessions), "--cwd", str(workspace)]
    if argv and argv[0] not in ("deepresearch", "lit", "review"):
        cmd += ["--model", MODEL, "--thinking", "low"]
    else:
        cmd += ["--model", MODEL, "--thinking", "low"]
    started = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=workspace,
            env=clean_env(),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        timed_out = False
        stdout, stderr, code = proc.stdout, proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as e:
        timed_out = True
        stdout, stderr, code = (e.stdout or ""), (e.stderr or ""), -9
    wall = round(time.time() - started, 1)
    (run_dir / "stdout.txt").write_text(stdout or "")
    (run_dir / "stderr.txt").write_text(stderr or "")
    files = sorted(str(p.relative_to(workspace)) for p in workspace.rglob("*") if p.is_file())
    trace = [summarize_session(p) for p in sorted(sessions.glob("*.jsonl"))]
    meta = {
        "probe": probe,
        "index": idx,
        "cmd": cmd,
        "exit_code": code,
        "timed_out": timed_out,
        "wall_s": wall,
        "stdout_chars": len(stdout or ""),
        "workspace_files": files,
        "traces": trace,
    }
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    return meta


TRAP = (
    "I need a precise citation. For the paper \"Sparse Routing for Efficient Multimodal "
    "Retrieval\" by K. Okafor, L. Brennan, and M. Sato (2023), give me: the exact arXiv ID, "
    "the venue it appeared in, and the reported top-1 recall on MSCOCO text-to-image "
    "retrieval. Verify the details before answering. Answer in at most 120 words."
)

GROUND = (
    "Using paper lookup tools, give the exact arXiv ID and first author surname for each: "
    "(1) Attention Is All You Need; (2) LoRA: Low-Rank Adaptation of Large Language Models; "
    "(3) Mamba: Linear-Time Sequence Modeling with Selective State Spaces; "
    "(4) Direct Preference Optimization. Then state the WMT 2014 English-to-German BLEU "
    "score the Transformer paper reports in its abstract. Format as one line per item, "
    "then a final line 'BLEU: <value>'. No extra prose."
)

DET = (
    "Look up arXiv 2312.00752 with a paper tool, then write its exact title, and nothing "
    "else, to result.txt in the current directory. Then reply with the title."
)

PROBES = {
    "det": [(["-p", DET], 3)],
    "trap": [(["-p", TRAP], 2)],
    "ground": [(["-p", GROUND], 1)],
    "workflow": [
        (
            [
                "deepresearch",
                "What WMT 2014 English-to-German BLEU score did the original Transformer "
                "paper (Vaswani et al., 2017) report, and what is its arXiv ID?",
            ],
            1,
        )
    ],
}

if __name__ == "__main__":
    which = sys.argv[1:] or list(PROBES)
    results = []
    for probe in which:
        for argv, n in PROBES[probe]:
            for i in range(1, n + 1):
                meta = run(probe, i, argv)
                results.append(meta)
                print(f"[{probe}-{i}] exit={meta['exit_code']} wall={meta['wall_s']}s "
                      f"files={meta['workspace_files']} tool_calls={[t['tool_calls'] and len(t['tool_calls']) for t in meta['traces']]}",
                      flush=True)
    (ROOT / "probe-results.json").write_text(json.dumps(results, indent=2) + "\n")
