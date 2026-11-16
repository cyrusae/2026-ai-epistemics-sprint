LATEST=0.5.69
INSTALLED=0.5.65
SOURCE=`npm view @companion-ai/feynman dist-tags` + `feynman --version` (registry: https://registry.npmjs.org/@companion-ai%2Ffeynman)

LATEST is the newest version published to the npm registry (dist-tag `latest`), while INSTALLED is the older build actually running in this runtime (`/opt/feynman/feynman-0.5.65-linux-arm64`), so the runtime is behind the published latest.
