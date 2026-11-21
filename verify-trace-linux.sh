#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != Linux || "$(uname -m)" != x86_64 ]]; then
  echo 'Use the pinned Mathlib build instructions in the README on this platform.' >&2
  exit 2
fi
repo=$(cd "$(dirname "$0")" && pwd)
(cd "$repo" && sha256sum --check SHA256SUMS) >&2
scratch=$(mktemp -d)
trap 'rm -rf -- "$scratch"' EXIT
cd "$scratch"

download() {
  curl --fail --location --silent --show-error --retry 4 --output "$2" "$1"
  printf '%s  %s\n' "$3" "$2" | sha256sum --check - >&2
}
checkout() {
  git init -q "$1"
  git -C "$1" remote add origin "$2"
  git -C "$1" fetch --quiet --depth 1 origin "$3"
  git -C "$1" checkout --quiet --detach FETCH_HEAD
  test "$(git -C "$1" rev-parse HEAD)" = "$3"
}

download https://github.com/leanprover/lean4/releases/download/v4.33.1/lean-4.33.1-linux.tar.zst \
  lean.tar.zst 890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235
tar --zstd -xf lean.tar.zst
export PATH="$scratch/lean-4.33.1-linux/bin:$PATH"
checkout mathlib4 https://github.com/leanprover-community/mathlib4.git 0df444a360eaa60ab8c11dca51a86af692955474
checkout trace https://github.com/leecrossley/theta-prime-trace.git 7a7909d2dc7bb9d8d0ec7b2dc8c78e70f93782d7
download https://github.com/CocoSgt/riemann-hypothesis-lean/releases/download/v2026-11-20/lean.tar.gz \
  source.tar.gz 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc
tar -xzf source.tar.gz
cd mathlib4
lake exe cache get >&2
lake env python3 "$scratch/trace/verify.py" "$scratch/lean/src" "$scratch/build" >&2
lake env python3 "$repo/check_trace.py" "$scratch/build"
