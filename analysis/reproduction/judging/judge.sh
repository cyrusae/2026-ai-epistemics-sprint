#!/bin/bash
# usage: judge.sh <judge: son|hai|gem> <unit, e.g. U07>
# Runs one blind judge in a temp copy of packets/<unit> (+ RUBRIC.md, JUDGE.md) and writes out/<judge>__<unit>.json
# (raw text in .raw.txt). Rate/usage limits: waits 15 min and retries, up to 16 times (4 h), so a limit
# pauses the queue instead of losing the unit. Safeguard refusals (Sonnet): recorded, then retried with Haiku as "hai".
set -u
judge=$1 unit=$2
here=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$here/out"; out="$here/out/${judge}__${unit}"
[ -s "$out.json" ] && { echo "$(date '+%T') skip $judge $unit"; exit 0; }
log() { echo "$(date '+%F %T') $judge $unit $*"; }
tmp=$(mktemp -d); cp -R "$here/packets/$unit/." "$tmp/"; cp "$here/RUBRIC.md" "$here/JUDGE.md" "$tmp/"
( cd "$tmp" && find . -type f | sed 's#^\./##' | sort | while read -r f; do printf "%10s  %s\n" "$(wc -c < "$f" | tr -d ' ')" "$f"; done > MANIFEST.txt )
prompt="$(cat "$here/JUDGE.md")

Your unit id is $unit."
for attempt in $(seq 1 16); do
  start=$(date +%s)
  cd "$tmp" || exit 1
  case $judge in
    son|hai) model=$([ "$judge" = son ] && echo sonnet || echo haiku)
             command claude -p "$prompt" --model "$model" --tools "Read,Grep,Glob" --allowedTools "Read,Grep,Glob" \
               --no-session-persistence --output-format json > "$out.cli.json" 2> "$out.err"; rc=$? ;;
    gem)     command agy -p "$prompt

Shell commands are blocked in this environment: do not run any. Use only your file-reading, listing and search tools (start with MANIFEST.txt)." --model gemini-3.8-flash-high > "$out.raw.txt" 2> "$out.err"; rc=$? ;;
  esac
  cd /
  if [ "$judge" != gem ]; then
    python3 -I - "$out.cli.json" "$out.raw.txt" <<'PY'
import json, sys
try: d = json.load(open(sys.argv[1])); t = d.get("result") or ""; e = d.get("is_error")
except Exception: t = open(sys.argv[1]).read(); e = True
open(sys.argv[2], "w").write(t)
sys.exit(1 if e else 0)
PY
    [ $? -ne 0 ] && rc=1
  fi
  text=$(cat "$out.raw.txt" "$out.err" "$out.cli.json" 2>/dev/null)
  if python3 -I - "$out.raw.txt" "$out.json" <<'PY'
import json, sys, re
t = open(sys.argv[1]).read()
s, e = t.find("{"), t.rfind("}")
try: j = json.loads(t[s:e + 1]); assert "A" in j
except Exception: sys.exit(1)
json.dump(j, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
PY
  then log "ok attempt=$attempt $(( $(date +%s) - start ))s"; rm -rf "$tmp"; exit 0; fi
  if echo "$text" | grep -qi "safeguards flagged\|usage policy\|aup"; then
    log "SAFEGUARD"; cp "$out.raw.txt" "$out.safeguard.txt" 2>/dev/null; rm -rf "$tmp"
    [ "$judge" = son ] && exec "$0" hai "$unit"; exit 2
  fi
  if echo "$text" | grep -qiE "rate.?limit|usage limit|429|403|overloaded|quota|exceeded|try again|resets? at|credit"; then
    log "LIMIT (attempt $attempt): waiting 15 min"; sleep 900; continue
  fi
  log "bad output rc=$rc (attempt $attempt)"; [ "$attempt" -ge 3 ] && break; sleep 60
done
log "GAVE UP"; rm -rf "$tmp"; exit 1
