LATEST=0.5.69
INSTALLED=0.5.65
SOURCE=npm view @companion-ai/feynman dist-tags (registry: {"latest":"0.5.69"}); feynman --version (runtime: 0.5.65, shim -> /opt/feynman/feynman-0.5.65-linux-arm64)

The npm registry's `latest` tag points to 0.5.69 (published 2026-11-13), whereas this runtime is a pinned standalone bundle of the earlier 0.5.65, so the installed CLI is one release line behind the newest published version.
