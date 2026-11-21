# How often can the Eisenstein prime race lose its lead at the cutoff?

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24410852.svg)](https://doi.org/10.5281/zenodo.24410852)

At the critical width, the norm-3 class of Eisenstein prime ideals leads the norm-1 class outside a set of **finite logarithmic measure**, assuming GRH for the primitive Dirichlet characters of discriminants $-4$ and $12$. Ties count as exceptions. If exceptions occur arbitrarily late, they force exceptionally accurate odd-over-odd approximations to ratios of actual zero ordinates.

## The race

In $\mathbb Q(\sqrt{-3})$ omit the prime ideals above 2 and 3. Let $A_b(y)$ be the weighted total for norms $3\bmod4$ minus the total for norms $1\bmod4$. A norm $n$ contributes $\log n$ times $W_b(n/y)$, where

$$
W_b(t)=\begin{cases}
b(1-1/t),&1 < t\le b,\\
b^2/t-1,&b < t < b^2,\\
0,&\text{otherwise}.
\end{cases}
$$

Fix **the exact critical width** $b=b_K$, the unique crossing of the square drift and the absolute zero mass. It lies between $4.49334142447806$ and $4.49334142447807$. The preceding cutoff theorem gives normalized lower limit zero there under the two GRHs and rational independence of the distinct positive ordinates. [Cutoff theorem and definition](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/c1e11263b1cf6e8de187742f246b32992455658f/PROOF.md)

## What happens at the crossing

Assume the two GRHs. There are constants $c,C>0$ such that, for every sufficiently large $Y$,

$$
\int_{\lbrace y\ge Y\thinspace:\thinspace A_{b_K}(y)\le0\rbrace}\frac{dy}{y}
\le C\exp(-c\sqrt{\log Y}).
$$

This gives finite logarithmic measure on $[1,\infty)$ and logarithmic density one for a strict norm-3 lead. No independence assumption is required for this estimate.

For eventual strict positivity it suffices that one ratio of two distinct positive zero ordinates be irrational with finite irrationality exponent. More precisely, if $\alpha=\mu/\lambda$ satisfies $|q\alpha-p|\ge d q^{-\nu}$ for all sufficiently large positive odd $q$ and all odd integers $p$, with some $d,\nu>0$, then $A_{b_K}(y)\gg\sqrt y/(\log y)^{2\nu}$ for every sufficiently large $y$. Whether the two GRHs alone give an eventual lead remains open here.

The prime number theorem in the fixed class $1\bmod3$ bounds the error in the square term. At the crossing the main expression becomes a sum of nonnegative cosine terms. A tie or loss forces each selected phase close to an odd multiple of $\pi$. One phase gives the measure estimate. Two give the rational-approximation condition. [Full proof](PROOF.md)

## Prior work and verification

Sheth proved a finite-logarithmic-measure theorem for a cumulative mod-4 sum weighted by $1/\sqrt p$. The result here concerns a compact prime-ideal window whose leading drift exactly equals its total zero mass. It gives a tail bound and a necessary approximation condition for arbitrarily late failures. Rubinstein–Sarnak, Devin, Fiorilli–Jouve and Bailleul and coauthors give related distribution, dominance and effective approximation results. [Sheth, Corollary 4.2](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/euler-products-at-the-centre-and-applications-to-chebyshevs-bias/1DA1AFD9BE7EBCF9D5B49FE792E55E81) · [Comparisons and sources](PROOF.md#earlier-results)

With Python 3.10 or later in a virtual environment, run

```sh
python3 -m pip install -r requirements.txt
python3 verify-release.py
```

The computations certify two zero brackets and positive coefficient bounds by independent routes. The exceptional-set and eventual-sign implications are written proofs. The approximation condition on the actual ordinates is an additional hypothesis. [Recorded checks](evidence/check.txt) [SHA-256 manifest](SHA256SUMS) [Latest release](https://doi.org/10.5281/zenodo.24410852)

## The continuous range at the exact cutoff

The extension proves a strict lead for every real $7/b_K^2<y\le\exp(10^{1058})/b_K$ under the same two GRHs. Equality holds at the lower endpoint, where the first retained ideal norm meets the edge of the window. Direct enumeration covers $b_Ky\le500000$ unconditionally throughout the certified width enclosure. The full proof also gives arbitrarily late strict-lead intervals of log length greater than $2\cdot10^{1058}$. The eventual sign outside these ranges remains open. [Continuous range, certificate and replay](CUTOFF-RANGE.md) · [Recorded arithmetic checks](evidence/critical-range.txt)

The correction oscillates, including at class-11 ordinary primes where the race has a strict lead. At a hypothetical exception the two twisted characters force a normalized 11-over-5 excess with leading constant $(\log3)/2$. This gives an explicit fourth-moment lower bound along any unbounded sequence of exceptional blocks. The extension also gives a spectral floor and stronger bounds on the size and spacing of exceptional sets. [Correction oscillation and zero conditions](CUTOFF-OSCILLATION.md) · [Forced excess and fourth moment](INERT-EXCESS.md) · [Spacing, floor and local shape](CUTOFF-SCALES.md)

The companion result studies reciprocal prime weights and finite arithmetic expressions at stationary minima. The DOI above identifies the original exceptional-set paper. These extensions have their own tagged family release. [Prime-weight results](../stationary-prime-weights/) · [Cutoff extension release](https://github.com/leecrossley/eisenstein-prime-window-transition/releases/tag/critical-cutoff-v1.0.0)
