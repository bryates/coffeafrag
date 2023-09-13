[![CI](https://github.com/bryates/coffeafrag/actions/workflows/main.yml/badge.svg)](https://github.com/bryates/coffeafrag/actions/workflows/main.yml)
# coffeafrag
Coffea based b-fragmentation analyzer. This analyzer uses the [`TopCoffea`](https://github.com/TopEFT/topcoffea) framework.

## Installing
I suggest using `micromamba` for faster installs than conda.
To setup `micromamba` use (only once per machine):
```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

### Setup environment
```bash
micromamba create -f environment.yml
```

### Clone and install repo
```bash
git clone git@github.com:bryates/coffeafrag.git
git clone git@github.com:TopEFT/topcoffea.git
```
