#!/usr/bin/env bash
set -euo pipefail

repo=$(cd "$(dirname "$0")" && pwd)
if [[ $# -ne 0 && $# -ne 2 ]]; then
  echo "Usage: bash verify-release.sh [pinned-mathlib4 compiled-trace]" >&2
  exit 2
fi
if [[ $# -eq 2 ]]; then
  mathlib=$(cd "$1" && pwd)
  trace=$(cd "$2" && pwd)
fi

cd "$repo"
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum --check SHA256SUMS
else
  shasum -a 256 -c SHA256SUMS
fi

run_dir=$(mktemp -d)
trap 'rm -rf -- "$run_dir"' EXIT
python3 verify.py >"$run_dir/receipt"
python3 independent.py >>"$run_dir/receipt"
if [[ $# -eq 2 ]]; then
  (cd "$mathlib" && lake env python3 "$repo/check_trace.py" "$trace") >>"$run_dir/receipt"
else
  bash verify-trace-linux.sh >>"$run_dir/receipt"
fi
diff -u evidence/check.txt "$run_dir/receipt"
cat "$run_dir/receipt"
