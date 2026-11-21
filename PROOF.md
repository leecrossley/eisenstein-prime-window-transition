# Proof of the Eisenstein prime-ideal race cutoff

## Observable

Write $W_b(t)=b(1-1/t)$ for $1<t\le b$, $W_b(t)=b^2/t-1$ for $b<t<b^2$ and zero elsewhere. For the primitive character $\chi_4$ of discriminant $-4$ let

$$
A_b(y)=-\sum_{\mathfrak p\nmid6}\chi_4(N\mathfrak p)\log(N\mathfrak p)\thinspace
                                      W_b(N\mathfrak p/y).
$$

A positive value is a lead for norm 3 modulo 4. These are prime ideals of the Eisenstein integers. A split rational prime supplies two ideals of norm $p$, and an inert prime supplies one of norm $p^2$ with logarithmic weight $2\log p$.

Let $\chi_{12}$ be the primitive even character of discriminant $12$. It is the product of $\chi_4$ and the quadratic character of discriminant $-3$. The full prime-power series for $\chi_4\circ N$ has the two factors $L_4=L(s,\chi_4)$ and $L_{12}=L(s,\chi_{12})$, up to the excluded local factors. At a split prime the two characters agree. At an inert prime their values are opposite, so only even powers survive and carry coefficient $2\log p$. At 3 the primitive product includes the one ramified Euler factor. Removing it changes the window sum by $O_b(1)$ since only boundedly many powers of 3 fit in the window. This was the concrete character proposed in the earlier theta-trace calculation. [Theta trace and prime-ideal target](https://github.com/leecrossley/theta-prime-trace/tree/v1.0.0)

## The two endpoints

The Mellin transform is $H_b(s)=(b^s-1)(b^s-b)/(s(s-1))$, continued at 0 and 1. Under the two GRHs each nontrivial zero $\rho=1/2+i\tau$ has

$$
H_b(\rho)=e^{i\tau\log b}h_b(\tau),\qquad
h_b(\tau)=\frac{\sqrt b\thinspace(b+1-2\sqrt b\cos(\tau\log b))}{1/4+\tau^2}>0 .
$$

The prime-square term in $A_b$ has coefficient $B_b=2\sqrt b(\sqrt b-1)^2$ at scale $\sqrt y$. Indeed $\chi_4(N\mathfrak p)^2=1$ at the retained places, and the prime ideal theorem gives $B_b=\int_1^b W_b(v^2)\thinspace dv$. In this quadratic field the required prime ideal theorem also follows from the prime number theorem for the class $1\bmod3$, since those rational primes split and inert-prime norms are squares. Prime powers of exponent at least three contribute $O_b(y^{1/3}\log^2 y)$. The trivial zeros, including the possible zero at 0 of an even primitive character, contribute $O_b(1)$ to this compact window for $y\ge2$.

With zeros from both functions counted with multiplicities,

$$
A_b(y)/\sqrt y=B_b+\sum_{\rho}h_b(\tau)e^{i\tau\log(by)}+o(1).
$$

This is the ordinary von Mangoldt explicit formula for the two characters with the higher prime powers removed. Absolute convergence follows from the quadratic denominator and the Dirichlet zero-counting bound. Both central values are nonzero. For every real $s>0$ the $\chi_4$ series has positive two-term blocks. The $\chi_{12}$ blocks have the form $f(12k+1)-f(12k+5)-f(12k+7)+f(12k+11)>0$ with $f(x)=x^{-s}$, since $f(x)-f(x+4)$ decreases. [Dirichlet explicit formula and smoothed races](https://link.springer.com/article/10.1007/s11139-025-01238-9) · [Dirichlet zero counting](https://doi.org/10.1090/mcom/3599)

Put $L_b^\ast=\sum_\rho h_b(\tau)$. Simultaneous approximation of any finite set of phases to 1 gives $\limsup A_b(y)/\sqrt y=B_b+L_b^\ast$. Always $\liminf A_b(y)/\sqrt y\ge B_b-L_b^\ast$. With independence of the union of the distinct positive ordinates, finite phases also come arbitrarily close to $-1$, giving equality at that lower endpoint. An entire tail has uniformly small contribution by absolute convergence. [Rubinstein–Sarnak, distribution of prime races](https://www.math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf)

## Computing the crossing

For either character $\chi$ let $q$ be its conductor, $a\in\lbrace0,1\rbrace$ its parity, and $d_\chi=L'(1,\chi)/L(1,\chi)$. Write $\psi=\Gamma'/\Gamma$ and $\gamma$ for Euler's constant. The functional equation and Hadamard product of the completed function give

$$
C_\chi=\sum_{\rho_\chi}\frac{1}{\rho_\chi(1-\rho_\chi)}
      =\log(q/\pi)+\psi((1+a)/2)+2d_\chi .
$$

Indeed subtraction of the completed logarithmic derivatives at 1 and 0 removes the Hadamard constant, and the functional equation makes them opposites. The two zero sums are absolutely convergent in this paired expression.

Set $S_\chi(b)=\sum_{\rho_\chi}b^{\rho_\chi}/[\rho_\chi(1-\rho_\chi)]$ and $R_\chi(b)=\sum_n\chi(n)\Lambda(n)\max(b/n-1,0)$. In the inverse Mellin integral of $(-L'/L)(s)b^s/[s(s-1)]$ the residue at 1 is $-b d_\chi$. The residue at 0 is independent of $b$ for an odd character and increases by $\log b$ for an even one, due to the simple trivial zero there. A trivial zero at $-m<0$ contributes $-b^{-m}/[m(m+1)]$. Subtract the formula at $b=1$ to obtain

$$
 S_\chi(b)-C_\chi=R_\chi(b)+(b-1)d_\chi
    -{\bf1}_{a=0}\log b+T_\chi(b)-T_\chi(1),
$$

where $T_\chi$ sums the positive trivial-zero terms $b^{-m}/[m(m+1)]$ for its parity. The vanishing of the ramp at its endpoint makes this identity continuous at prime powers. The contour shift uses absolute convergence of the zero sum along the usual heights avoiding zeros. For the two characters together the trivial zeros supply every positive integer $m$ once, so $T_4(b)+T_{12}(b)=1+(b-1)\log(1-1/b)$.

Under GRH, pairing conjugates gives $L_b^\ast/\sqrt b=(b+1)(C_4+C_{12})-2(S_4(b)+S_{12}(b))$. The two logarithmic derivatives cancel. Hence with $C=2\gamma+\log(\pi^2/12)$ and $R=R_4+R_{12}$,

$$
 F(b):=\frac{B_b-L_b^\ast}{\sqrt b}
 =2(\sqrt b-1)^2+(b-1)C+2R(b)-2\log b
                  +2(b-1)\log(1-1/b).
$$


For $1<b\le9$ the only nonzero ramp coefficients strictly below 9 are $-\log3$ at 3 and $-2\log7$ at 7. The characters cancel at 5. Between these corners,

$$
 F'(b)=2-2/\sqrt b+C+2\log(1-1/b)+2R'(b),\qquad
 F''(b)=b^{-3/2}+2/[b(b-1)]>0 .
$$

The continuous extension has $F(1)=0$ and $F(3)<-0.82$, so convexity gives strict negativity on $(1,3]$. The right derivatives at 3 and 7 both exceed $0.04$. Thus $F$ is strictly increasing from 3 through 9. The certificates give opposite signs at the two stated decimal endpoints and $\sqrt5 F(5)>0.94$. For $b\ge9$ one has $L_b^\ast/\sqrt b\le(\sqrt b+1)^2(C_4+C_{12})$. The dimensionless drift $2((\sqrt b-1)/(\sqrt b+1))^2$ increases and already equals $1/2$ at 9. Both certificates bound $C_4+C_{12}<0.49$, proving positivity on the whole remaining half-line.

## Why eventual dominance implies the two GRHs

For $\Re s>1$ the Mellin integral of $A_b(y)$ over $1<y<\infty$, with measure $y^{-s-1}dy$, equals

$$
 H_b(s)\left(\frac{L'_4}{L_4}(s)+\frac{L'_{12}}{L_{12}}(s)\right)+E_b(s)
$$

with $E_b$ holomorphic for $\Re s>1/2$. Prime powers of exponent at least two give an absolutely convergent Dirichlet series there. Removing the finitely many local Euler factors preserves holomorphy there. Removing $0<y<1$ costs an entire function since the sum is zero near $y=0$. The multiplier has no zero in $0<\Re s<1$, by the absolute values of $b^s$. A zero of either function in $1/2<\Re s<1$ therefore gives a genuine pole, including at a common zero where the multiplicities add.

If $A_b$ has one sign eventually, Landau's theorem puts a singularity on the real axis at the abscissa of convergence of its Mellin integral, whenever the abscissa is finite. Both real Dirichlet functions are positive on $(0,\infty)$ by the block argument, and the displayed expression is holomorphic on the real interval $(1/2,\infty)$. Thus the abscissa is at most $1/2$, or is $-\infty$. A nonreal pole farther right is impossible. Functional equation symmetry now gives the two GRHs. For $b>b_K$ the forward sign estimate above supplies the converse. [Kaczorowski–Pintz, oscillation of arithmetical functions](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf) · [Suzuki, variants of Chebyshev’s conjecture](https://doi.org/10.1007/s11139-025-01238-9)

## Prior work and the distinguishing calculation

The kernel, the explicit formula and the one-sign Mellin argument all have precedents. Put $a=\log b$ and center the kernel in logarithmic coordinates. For $|u|\le a$ one obtains

$$
 e^{u/2}W_b(be^u)=b e^{-|u|/2}-e^{|u|/2}.
$$

The right side is the autocorrelation of $v\mapsto e^{v/2}{\bf1}_{[0,a]}(v)$. This is the cross term in Grenié and Molteni's proof of Theorem 3.5 with $T=b$. Their application bounds generators of a class group. The fixed dyadic ordinary-prime inequality also predates this work. [Grenié–Molteni](https://arxiv.org/pdf/1607.02430#page=6) · [bramble_trace, revision 24](https://rstation.ai/api/v1/posts/uw5cfb_J_Cj7XJO6/attachment?revision=24)

There is a direct comparison with Zhao's integrated first Mertens error for a real primitive character. Put $U_\chi(x)=\sum_{p>3}\chi(p)\log p\thinspace\max(x/p-1,0)$. This differs from the integrated error by an affine function for $x\ge3$, including the adjustment for the excluded primes. The compact rational-prime window for $\chi$ is $bU_\chi(y)-(b+1)U_\chi(by)+U_\chi(b^2y)$. Each affine term cancels. For an exact alternative description of the Eisenstein race, take the negative of both rational-prime windows and subtract the inert-prime contribution

$$
 2\sum_{\substack{p>3\\p\equiv2\!\!\pmod3}}\log p\thinspace W_b(p^2/y).
$$

Indeed the two rational characters agree at split primes and cancel at inert primes. Each inert prime gives one ideal of norm $p^2$, in the norm-1 class. Zhao's Theorem 3 classifies individual quadratic characters for a cumulative integral. Its sign alone does not determine this signed three-point difference or the inert-prime correction. [Zhao, Theorem 3 and Section 6](https://arxiv.org/html/2411.18903v2)

Suzuki proves sign criteria for other weighted sums. Fiorilli and Jouve prove eventual prime-ideal dominance in other extensions using different group-theoretic hypotheses. The argument here also uses the classical explicit formula and simultaneous approximation of zero phases. The part specific to this result is the cancellation of both logarithmic derivatives in the paired odd and even zero sums, the two downward changes of slope before 9, and control of all larger widths. These give the single certified cutoff for the stated signed ideal sum. The comparison found no prior paper proving that step for this observable. Publication priority remains open to additional sources. [Suzuki](https://arxiv.org/html/2411.07436v2) · [Fiorilli–Jouve](https://www.numdam.org/articles/10.5802/jep.192/) · [Rubinstein–Sarnak](https://www.math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf)

## What the Lean proof covers

The finite identity `EisensteinPrimeRace.trace_eq_norm_race` applies to primes of a tower host $E$ and uses `ThetaTransfer.theta_prime_trace_extract`. If the row character agrees with the norm character modulo four on the supplied places, the normalized difference of the consecutive Hecke traces equals the norm-1 sum minus the norm-3 sum on those places. This is the opposite sign convention to $A_b$. The row and its values are hypotheses. [Lean declarations](EisensteinTrace.lean) · [Pinned trace extraction](https://github.com/leecrossley/theta-prime-trace/blob/7a7909d2dc7bb9d8d0ec7b2dc8c78e70f93782d7/ThetaPrimeTrace.lean#L68)

There is a direct obstruction to using this identity for the Eisenstein field. Every `D7` host satisfies $[E:\mathbb Q]=4\thinspace\mathrm{ord}$, with $\mathrm{ord}$ a natural number. An isomorphism of rational algebras preserves degree. Since $\mathbb Q(\sqrt{-3})$ has degree two, it cannot be such a host. The declaration `EisensteinPrimeRace.no_quadratic_host` proves this obstruction for every rational field extension of degree two. Transferring a race on one field to a different host would need a theorem comparing their weighted prime ideals. The analytic argument used here works directly over the Eisenstein field. [Upstream `finrank_cmField`](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean#L183) · [Host structure](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalRingCardinality/DataHost.lean#L39)

## Verification

`verify.py` checks the local Euler coefficients through 100,000, computes the logarithmic derivatives using Hurwitz-zeta constants and bounds the cutoff using two expressions in ball arithmetic. `independent.py` uses 48,000 Dirichlet-series terms per character with bounds on the remainder and rational enclosures for the uncancelled trivial-zero series. The implications from the explicit formula, Landau's theorem, and the prime ideal theorem are written proofs.

For a fresh x86-64 Linux run, install Python, Git, curl, tar and zstd. From a virtual environment run

```sh
python3 -m pip install -r requirements.txt
bash verify-release.sh
```

On a machine with [the pinned base trace](https://github.com/leecrossley/theta-prime-trace/tree/7a7909d2dc7bb9d8d0ec7b2dc8c78e70f93782d7) already built, put the pinned Lean 4.33.1 `bin` directory on `PATH`. From this repository use

```sh
bash verify-release.sh /absolute/path/to/pinned-mathlib4 /absolute/path/to/compiled-trace
```

The recorded run used the cached arm64 macOS route. `leanchecker` replayed the local module, and both axiom reports contained only `propext`, `Classical.choice` and `Quot.sound`. The manifest covers the proof, the verification programs, the pinned requirements and the recorded output. [Verification output](evidence/check.txt) · [Checksums](SHA256SUMS)
