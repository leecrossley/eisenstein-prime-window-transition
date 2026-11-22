# Eisenstein prime-ideal race

Open a result to read its statement, hypotheses and replay instructions. Run its verification commands from that result’s directory. The source link identifies the revision brought into this project. The publication and review links lead to the original records.

| Result | Source revision | Publication | Reviews |
| --- | --- | --- | --- |
| [A sharp window width for an Eisenstein prime-ideal race](README.md) | [f4cc9cdbf4](https://github.com/leecrossley/eisenstein-prime-window-transition/tree/f4cc9cdbf423bbcf596e8f311ba496639f4d12e7) | [Releases](https://github.com/leecrossley/eisenstein-prime-window-transition/releases) · [DOI](https://doi.org/10.5281/zenodo.24410867) | [Issues](https://github.com/leecrossley/eisenstein-prime-window-transition/issues) · [PRs](https://github.com/leecrossley/eisenstein-prime-window-transition/pulls) |
| [How often can the Eisenstein prime race lose its lead at the cutoff?](results/eisenstein-critical-exceptions/) | [d037f77da2](https://github.com/leecrossley/eisenstein-critical-exceptions/tree/d037f77da267797dc0a813cfe546d21e3b2bd456) | [DOI](https://doi.org/10.5281/zenodo.24410852) | [Issues](https://github.com/leecrossley/eisenstein-prime-window-transition/issues) · [PRs](https://github.com/leecrossley/eisenstein-prime-window-transition/pulls) |
| [Prime weights at stationary minima of the Eisenstein race](results/stationary-prime-weights/) | [Tagged proof](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/critical-cutoff-v1.0.0/results/stationary-prime-weights/PROOF.md) | [Critical cutoff release](https://github.com/leecrossley/eisenstein-prime-window-transition/releases/tag/critical-cutoff-v1.0.0) | [Issues](https://github.com/leecrossley/eisenstein-prime-window-transition/issues) |

The first two rows retain their original publication records. The exceptional-set result now includes a [continuous strict-lead certificate](results/eisenstein-critical-exceptions/CUTOFF-RANGE.md), [bounds for possible exceptions](results/eisenstein-critical-exceptions/CUTOFF-SCALES.md), [oscillation of the correction](results/eisenstein-critical-exceptions/CUTOFF-OSCILLATION.md), and [a fourth-moment test using ordinary primes](results/eisenstein-critical-exceptions/INERT-EXCESS.md). The new certificate and the prime-weight result share the [critical cutoff release](https://github.com/leecrossley/eisenstein-prime-window-transition/releases/tag/critical-cutoff-v1.0.0).

## Checking the collection

When a collection file changes, stage new paths with Git, then run `python3 tools/collection_manifest.py --write` to refresh `COLLECTION.sha256`.

Run `sh verify-collection.sh` from the repository root to check the collection files and the manifests for every result directory. The index must point to an existing result with a manifest. Each result’s README gives its mathematical replay and environment requirements. [Contribution and publication guidance](AGENTS.md)

## Edition DOIs

Each DOI identifies a fixed release. The final column identifies the archive with the proof files in this revision. A shared release can contain several papers. The collection as archived on 21 November 2026 is available at [10.5281/zenodo.24425816](https://doi.org/10.5281/zenodo.24425816).

| Result | Published release | Version DOI | Current proof files |
| --- | --- | --- | --- |
| [A sharp window width for an Eisenstein prime-ideal race](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/d5e823b72f32c4314e732374661b7e7ea2e43b3b/README.md) | [v1.0.6-archive](https://github.com/leecrossley/eisenstein-prime-window-transition/releases/tag/v1.0.6-archive) | [10.5281/zenodo.24438088](https://doi.org/10.5281/zenodo.24438088) | [v1.0.6 proof files](https://github.com/leecrossley/eisenstein-prime-window-transition/tree/d5e823b72f32c4314e732374661b7e7ea2e43b3b) |
| [A sharp window width for an Eisenstein prime-ideal race](README.md) | [v1.0.7](https://github.com/leecrossley/eisenstein-prime-window-transition/releases/tag/v1.0.7) | [10.5281/zenodo.24425816](https://doi.org/10.5281/zenodo.24425816) | Same edition |
| [How often can the Eisenstein prime race lose its lead at the cutoff?](results/eisenstein-critical-exceptions/README.md) | [v1.0.3](https://github.com/leecrossley/eisenstein-critical-exceptions/releases/tag/v1.0.3) | [10.5281/zenodo.24410853](https://doi.org/10.5281/zenodo.24410853) | [10.5281/zenodo.24425816](https://doi.org/10.5281/zenodo.24425816) |
| [Prime weights at stationary minima of the Eisenstein race](results/stationary-prime-weights/README.md) | [critical-cutoff-v1.0.1](https://github.com/leecrossley/eisenstein-prime-window-transition/releases/tag/critical-cutoff-v1.0.1) | [10.5281/zenodo.24425810](https://doi.org/10.5281/zenodo.24425810) | Same edition |
