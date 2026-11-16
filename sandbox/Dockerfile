# Clean-room Feynman sandbox. One image, many disposable runs.
# Every run gets a fresh FEYNMAN_HOME + workspace bind-mounted from the host,
# so no memory/session state leaks between runs.
FROM debian:bookworm-slim

ARG FEYNMAN_VERSION=0.5.65
ARG TARGETARCH

RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl git tar gzip python3 jq less procps tini \
    && rm -rf /var/lib/apt/lists/*

# Pinned release bundle, verified against the release's SHA256SUMS.
RUN set -eu; \
    case "${TARGETARCH:-$(dpkg --print-architecture)}" in \
      amd64|x64) arch=x64 ;; arm64|aarch64) arch=arm64 ;; *) echo "unsupported arch"; exit 1 ;; esac; \
    name="feynman-${FEYNMAN_VERSION}-linux-${arch}"; \
    base="https://github.com/Companion-Inc/feynman/releases/download/v${FEYNMAN_VERSION}"; \
    cd /tmp; curl -fsSLO "$base/$name.tar.gz"; curl -fsSLO "$base/SHA256SUMS"; \
    grep " $name.tar.gz\$" SHA256SUMS | sha256sum -c -; \
    mkdir -p /opt/feynman; tar -xzf "$name.tar.gz" -C /opt/feynman; \
    ln -s "/opt/feynman/$name" /opt/feynman/current; \
    printf '#!/bin/sh\nexec /opt/feynman/current/feynman "$@"\n' > /usr/local/bin/feynman; \
    chmod +x /usr/local/bin/feynman; rm -f /tmp/*.tar.gz /tmp/SHA256SUMS; \
    echo "$name" > /opt/feynman/BUNDLE

RUN useradd -m -u 1000 -s /bin/bash researcher && mkdir -p /state /work && chown researcher /state /work
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# /state  -> FEYNMAN_HOME (so ~/.feynman lives at /state/.feynman: sessions, memory, settings)
# /work   -> the project cwd Feynman writes outputs/, .drafts/, .plans/ into
ENV FEYNMAN_HOME=/state \
    FEYNMAN_TELEMETRY=off \
    PI_TELEMETRY=0 \
    PI_SKIP_VERSION_CHECK=1 \
    TERM=xterm-256color \
    LANG=C.UTF-8
USER researcher
WORKDIR /work
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/entrypoint.sh"]
CMD ["feynman"]
