# A sharp window width for an Eisenstein prime-ideal race

Take the prime ideals of the Eisenstein integers and group them by whether their norm is 1 or 3 modulo 4. Give the most weight to norms near the middle of a moving window. The width at which the two classes change behaviour lies between $4.49334142447806$ and $4.49334142447807$.

At width 5, the norm-3 class eventually leads if and only if the generalized Riemann hypothesis (GRH) holds for the two Dirichlet functions of discriminants $-4$ and $12$. At width 4, both classes take the lead arbitrarily late under those two GRHs and rational independence of their distinct positive zero ordinates.

## Statement

Fix $b>1$. The window runs from $y$ to $b^2y$ and peaks at $by$. A norm $n$ contributes its logarithm times $W_b(n/y)$, where

$$
W_b(t)=
\begin{cases}
 b(1-1/t), & 1 < t \le b,\\
 b^2/t-1, & b < t < b^2,\\
 0, & \text{otherwise}.
\end{cases}
$$

Let $A_b(y)$ be the weighted total for norm 3 modulo 4 minus the total for norm 1 modulo 4. Omit the prime ideals over 2 and 3. There is a unique cutoff $b_K$ for the sign of the difference between the prime-square contribution and the total absolute zero contribution.

| Width | Behaviour |
|---|---|
| $b>b_K$ | $A_b(y)>0$ for every sufficiently large $y$ if and only if both GRHs hold. |
| $1<b<b_K$ | Under both GRHs and the independence assumption, each class leads arbitrarily late. |
| $b=b_K$ | Under the same three assumptions the lower limit of $A_b(y)/\sqrt y$ is zero. Its eventual sign is open here. |

## How the proof goes

1. Splitting in the Eisenstein field gives two Dirichlet factors. Removing prime squares from their explicit formula supplies a positive drift.
2. The characters of conductors 4 and 12 have opposite parity. Pairing their trivial-zero terms reduces the competing zero contribution to one expression in $b$. Below 9 the only nonzero prime-power terms that change its slope occur at 3 and 7. The derivative and a separate large-width bound prove there is just one crossing.
3. In the reverse direction, a zero of either function to the right of the critical line gives a pole that a one-sided sum cannot have. At width 5 the forward estimate gives a lead exceeding $0.94\sqrt y$ for all sufficiently large $y$.

[Full proof and comparison with earlier work](PROOF.md)

## Prior work and scope

Grenié and Molteni used the same centered exponential kernel for class-group bounds. Zhao studied integrated errors for quadratic-character prime sums. Suzuki studied related sign criteria, and Fiorilli and Jouve proved eventual dominance in other prime-ideal races. The contribution examined here is the unique width for this particular norm race, the two-function criterion, and the proof locating the only crossing. I found no earlier derivation of that cutoff in the sources compared. [Grenié–Molteni, proof of Theorem 3.5](https://arxiv.org/pdf/1607.02430#page=6) · [Zhao, Theorem 3](https://arxiv.org/html/2411.18903v2#S1.SS2) · [Suzuki](https://arxiv.org/html/2411.07436v2) · [Fiorilli–Jouve](https://www.numdam.org/articles/10.5802/jep.192/)

Lean checks a finite trace identity on an upstream host and a restriction on which fields can serve as that host. Its degree over the rationals is divisible by four. The Eisenstein field has degree two, which rules out direct specialization of the trace to its prime ideals. The cutoff is proved analytically from the two Dirichlet factors. [Lean declarations](EisensteinTrace.lean) · [Upstream degree formula](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean#L183)

## Verification

With Python and the pinned arithmetic package installed in a virtual environment, the following command checks the manifest, runs both numerical certificates, replays the Lean declarations and compares the output with the release receipt. A fresh build uses x86-64 Linux with Git, curl, tar and zstd.

```sh
python3 -m pip install -r requirements.txt
bash verify-release.sh
```

The recorded run used arm64 macOS with the pinned imports. The proof gives that [cached build command](PROOF.md#verification). [Recorded output](evidence/check.txt) · [SHA-256 manifest](SHA256SUMS) · [Tagged publication](https://github.com/leecrossley/eisenstein-prime-window-transition/releases/tag/v1.0.2)
