#!/bin/bash
# usage: run_agy.sh <task: battery|rubric> <run> <coder> [model]
# Runs agy headless inside a temp copy of packets/<run> (so it can read only that run), writes coders/<coder>__<task>__<run>.json
set -u
task=$1 run=$2 coder=$3 model=${4:-gemini-3.8-flash-high}
here=$(cd "$(dirname "$0")" && pwd)
out="$here/coders/${coder}__${task}__${run}.json"
[ -s "$out" ] && { echo "skip $out"; exit 0; }
tmp=$(mktemp -d); cp -R "$here/packets/$run/." "$tmp/"
[ "$task" = rubric ] && { rm -rf "$tmp/transcript" "$tmp/reference" "$tmp/FACTS.md"; grep -E "  (design/|PROMPTS)" "$tmp/MANIFEST.txt" > "$tmp/M" ; mv "$tmp/M" "$tmp/MANIFEST.txt"; }
cd "$tmp" || exit 1
start=$(date +%s)
command agy -p "$(cat "$here/prompts/$task.md")

Your run id is: $run" --model "$model" > "$out.tmp" 2> "$here/coders/${coder}__${task}__${run}.err"
rc=$?
mv "$out.tmp" "$out"; cd /; rm -rf "$tmp"
echo "$coder $task $run rc=$rc $(( $(date +%s) - start ))s $(wc -c < "$out")B"
