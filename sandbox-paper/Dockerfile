# Paper audit/replicate variant: the baseline Feynman sandbox plus a Python
# toolchain so `replicate` can actually execute ("Local" = inside this container).
# Deliberately no scientific packages preinstalled: installing them is part of what we observe.
FROM feynman-sandbox:0.5.65
USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends python3 python3-venv python3-pip git unzip build-essential \
 && rm -rf /var/lib/apt/lists/*
USER researcher
