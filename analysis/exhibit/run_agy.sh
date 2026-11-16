#!/usr/bin/env bash
# run_agy.sh <prompt.md> <chunk.txt> <coder-name> [model]
# Runs agy -p from an empty temp dir (no repo access) with the prompt + chunk inline.
# Output: coders/<coder-name>__<chunk-basename>.jsonl
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
prompt="$1"; chunk="$2"; coder="$3"; model="${4:-gemini-3.8-flash-high}"
out="$HERE/coders/${coder}__$(basename "$chunk" .txt).jsonl"
[ -s "$out" ] && { echo "exists: $out"; exit 0; }
jail="$(mktemp -d -t agyjail)"
body="$(cat "$prompt")

----- BEGIN LOG SLICE ($(basename "$chunk")) -----
$(cat "$chunk")
----- END LOG SLICE -----"
(cd "$jail" && command agy -p "$body" --model "$model" --disable-slash-commands --output-format json) > "$out.raw" 2> "$out.err"
python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1])); open(sys.argv[2],"w").write(d.get("response",""))' "$out.raw" "$out" || echo "parse failed: $out.raw"
rm -rf "$jail"
echo "$(basename "$out"): $(grep -c '^{' "$out" 2>/dev/null) findings"
