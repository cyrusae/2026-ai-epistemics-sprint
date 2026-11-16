#!/bin/sh
# Seeds a fresh FEYNMAN_HOME on first use of a run directory, then execs the command.
set -eu
AGENT="$FEYNMAN_HOME/.feynman/agent"
mkdir -p "$AGENT"
if [ ! -f "$AGENT/settings.json" ] && [ -n "${SEED_SETTINGS:-}" ] && [ -f "$SEED_SETTINGS" ]; then
  cp "$SEED_SETTINGS" "$AGENT/settings.json"
fi
if [ ! -f "$AGENT/web-search.json" ] && [ -n "${SEED_WEBSEARCH:-}" ] && [ -f "$SEED_WEBSEARCH" ]; then
  cp "$SEED_WEBSEARCH" "$AGENT/web-search.json"   # no secrets; EXA_API_KEY comes from env
fi
# Record exactly what ran, once per run dir.
if [ ! -f /work/.sandbox/environment.txt ]; then
  mkdir -p /work/.sandbox
  {
    echo "bundle: $(cat /opt/feynman/BUNDLE)"
    echo "feynman --version: $(feynman --version 2>/dev/null || echo '?')"
    echo "model: ${FEYNMAN_MODEL:-<settings default>}"
    echo "thinking: ${FEYNMAN_THINKING:-<settings default>}"
    echo "exa key present: $([ -n "${EXA_API_KEY:-}" ] && echo yes || echo no)"
    echo "image: ${SANDBOX_IMAGE_ID:-?}"
    echo "created: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  } > /work/.sandbox/environment.txt
fi
exec "$@"
