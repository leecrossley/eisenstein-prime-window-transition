# Which part of the cutoff race oscillates?

Assume GRH for $L(s,\chi_{-4})$ and $L(s,\chi_{12})$. Write $z=\sqrt y$, $t=\log(by)$ and $A_b(y)/z=F(t)-B(t)$ at the exact critical width. A point of depth $\alpha>1$ means $B(t)>0$ and $F(t)\le B(t)^\alpha$. For ordinary primes $p$ use $F_p=F(\log p)$, $B_p=B(\log p)$. The floor $F(t)\gg_b t^2/z$ and both derivative bounds for $B$ are proved in the [estimates for real scales](CUTOFF-SCALES.md). The nontrivial zeros of $\zeta(s)L(s,\chi_{-3})$ below are untwisted. Their real parts are unrestricted by the two assumptions.

## A late point of depth two would force an off-line zero

At every sufficiently late point of depth $\alpha\ge 3/2$, put $u=F(t)^{1/\alpha}$. There is a nontrivial zero $\rho=\beta+i\gamma$ of $\zeta(s)$ or $L(s,\chi_{-3})$ such that

```math
\begin{split}
0\lt \gamma &\ll_b u^{-1}\log(2/u),\\[0pt]
\beta &>1-\frac{\log(1/u)+C_b}{\log z}
 \ \ge\ 1-\frac1\alpha+
       \frac{(2/\alpha)\log t-C_{b,\alpha}}{\log z},\\[0pt]
\Re\!\left(H_b(\rho/2)e^{i\gamma\log z}\right)&>0 ,
\qquad H_b(s)=\frac{(b^s-1)(b^s-b)}{s(s-1)} .
\end{split}
```

In particular, at $\alpha=2$ the forced real part exceeds $1/2+(\log t-O_b(1))/\log z$. Either untwisted function could supply the zero. The two GRHs in the question concern different functions.

To see this, let $D_2=H_b(1/2)/2=2\sqrt b(\sqrt b-1)^2$. Write $E(y)$ for the unsigned sum over all even ideal-prime exponents and $J(y)$ for the signed sum over odd exponents at least three. With weights $`\log N\mathfrak p\,W_b((N\mathfrak p)^k/y)`$ one has $zB(t)=D_2z-E(y)-J(y)+O_b(1)$. Taking residues in the untwisted full prime-power formula gives

```math
E(y)=D_2z-\tfrac12\sum_{\rho_K} H_b(\rho_K/2)z^{\rho_K}+O_b(1),
\qquad \zeta_K=\zeta L(\,\cdot\,,\chi_{-3}).
```

The series includes both signs of the ordinates with multiplicity. It converges absolutely at each $z>1$, since $H_b(\rho_K/2)\ll_b(1+|\Im\rho_K|^2)^{-1}$. The residue at zero, the trivial zeros and the two omitted rational primes cost $O_b(1)$. Both untwisted functions have no real zero in $(0,1)$. This follows from the alternating eta series and the positive paired differences in the conductor-3 series. [Prime-power decomposition and Mellin formula](CUTOFF-SCALES.md#the-arithmetic-correction)

We need a cancellation estimate for the signed higher powers,

$$
J(y)=O_b(y^{1/6}).
$$

For $k=3,5$, extend the $`k`$th prime-ideal term to all ideal prime powers. With $\chi(\mathfrak p)=\chi_{-4}(N\mathfrak p)$ the extension weights the $`\ell`$th power by $\chi(\mathfrak p)^\ell$. Its explicit formula has nontrivial zero sum $-k^{-1}\sum_{\rho_\chi}H_b(\rho_\chi/k)y^{\rho_\chi/k}$ for the product of the two given functions. The omitted Euler factors and trivial zeros cost $O_{b,k}(1)$. Absolute summation on the two assumed critical lines gives $O_{b,k}(y^{1/(2k)})$. The extension's even powers have unsigned mass $O_{b,k}(y^{1/(2k)})$ by the elementary Chebyshev bound for $\psi_K$. The odd powers with $\ell\ge3$ have unsigned mass $O_{b,k}(y^{1/(3k)}\log^2(2y))$. Indeed each norm arises from at most two prime ideals, and there are $O_b(\log(2y))$ possible exponents. The sum in the original $J$ over $k\ge7$ costs $O_b(y^{1/7}\log^2(2y))$ by the same count. These bounds prove the estimate, including its lack of logarithmic loss. Hence

$$
B(t)=\tfrac12\sum_{\rho_K}H_b(\rho_K/2)z^{\rho_K-1}
       +O_b(z^{-2/3}). \tag{1}
$$

At the specified depth $B(t)\ge u\gg_{b,\alpha}t^{2/\alpha}z^{-1/\alpha}$, so the error in (1) is $o(u)$ even at $\alpha=3/2$. The absolute contribution above height $T$ is $O_b(\log(2T)/T)$ by the unit-interval zero count. Choose $T=C'_b u^{-1}\log(2/u)$ so this is at most $u/8$. The entire contribution from $\beta\le1-(\log(1/u)+C_b)/\log z$ is at most $u/8$ in absolute value by summability of the coefficients. The remaining conjugate pairs must have a positive real contribution, proving the claim. The same argument detects a zero using $u=B(t)$ whenever $B(t)>0$ and $B(t)z^{2/3}\to\infty$, with no depth restriction.

If $\Theta=\sup_{\rho_K}\Re\rho_K$, then $1/2\le\Theta\le1$ and (1) gives $|B(t)|\ll_b z^{\Theta-1}$. Comparing with the floor for $F$ excludes all sufficiently late points of depth $\alpha$ whenever $\alpha(1-\Theta)\ge1$. At equality the factor $t^2$ decides the comparison. In particular RH for both *untwisted* factors would give $F(t)\gg_b t^2 B(t)^2$ at every sufficiently late centre and would rule out every depth $\alpha\ge2$. Even with those additional hypotheses this comparison leaves $1<\alpha<2$ open.

## Both signs of the correction in every sufficiently late multiplicative interval of fixed ratio

There are constants $c>0$ and $K>1$ such that every sufficiently late $[X,KX]$ contains two primes $p_+,p_-\equiv11\pmod {12}$ for which

```math
 F_{p_+}>c,\qquad F_{p_-}>c,\qquad
 B_{p_+}>c\,p_+^{-1/4},\qquad -B_{p_-}>c\,p_-^{-1/4}. \tag{2}
```

Both primes give a normalized lead bounded below by $c/2$ eventually. In fact, for every fixed $0<\varepsilon<1$ and each choice of sign, every sufficiently late $[X,KX]$ contains **at least $X^{1-\varepsilon}$ distinct primes** of class 11 satisfying

```math
 F_p>c,\qquad \pm B_p>\max\{c\,p^{-1/4},\ p^{(\Theta-1)/2-\varepsilon}\}.
```

Here $\Theta$ is the supremum of the real parts of the nontrivial zeros of $\zeta_K(s)=\zeta(s)L(s,\chi_{-3})$. The constants $c,K$ can be fixed independently of $\varepsilon$. Consequently for each sign

```math
\limsup_{\substack{p\to\infty,\ p\equiv11\ (12)\\F_p>c,\ \pm B_p>0}}
\frac{\log(\pm B_p)}{\log p}=\frac{\Theta-1}{2}. \tag{3}
```

Use $u=\log z$ and $D(u)=B(\log b+2u)$. The absolutely convergent explicit formula and its error are

```math
D(u)=\tfrac12\sum_{\rho}\! H_b(\rho/2)e^{(\rho-1)u}+O_b(e^{-2u/3}),\qquad
H_b(s)=\frac{(b^s-1)(b^s-b)}{s(s-1)} .
```

Here $\rho$ runs over both signs with multiplicities in the untwisted factors, which have no nontrivial real zeros. The coefficients are absolutely summable and nonzero. In particular $D(u)\ll_b e^{(\Theta-1)u}$ since $1/2\le\Theta\le1$. The positive-summand series for $F$ is uniformly almost periodic. Its pointwise lower bound is $F(t)\gg_b t^2 e^{-t/2}$ for large $t$. These facts use only the two stated GRHs and unconditional estimates. [Explicit formula and spectral floor](CUTOFF-OSCILLATION.md#a-late-point-of-depth-two-would-force-an-off-line-zero)

**When a zero attains $\Theta$.** The normalized correction $e^{(1-\Theta)u}D(u)=G(u)+o(1)$, where

$$
G(u)=\tfrac12\sum_{\Re\rho=\Theta}H_b(\rho/2)e^{i(\Im\rho)u}.
$$

The remainder tends to zero by dominated convergence. The real uniformly almost periodic function $G$ has mean zero and a nonzero Fourier coefficient at each displayed ordinate, with repeated zeros adding the same coefficient. It therefore takes both signs. Indeed a strictly positive value of a nonnegative uniformly almost periodic function gives positive-length intervals, occurring with bounded gaps, on which it is bounded below, and hence a positive mean. Apply this argument also to $-G$. Each strict sign occurs arbitrarily late, where $F(\log b+2u)>0$. Choose two fixed short intervals on which the corresponding sign of $G$ and the value of $F$ have fixed positive margins. The pair $(G(u),F(\log b+2u))$ is uniformly almost periodic, so translates preserving these margins within a factor of two occur with bounded gaps. This follows also by simultaneously approximating both functions by finite trigonometric polynomials and using compactness of the joint phase group. On the late translates $\pm D(u)\gg_b e^{(\Theta-1)u}$. Each interval of fixed positive $u$-length contains primes of class 11 on the $p=be^{2u}$ scale by the prime number theorem in fixed progressions. As $\Theta\ge1/2$ this proves (2) and (3) in this case.

**When no zero attains $\Theta$.** Here $\Theta>1/2$ by the functional equation and existence of zeros. Fix an arbitrarily small length $L>0$ and $d<\Theta$. Montgomery's density theorem at the two fixed conductors gives, for each $1/2<\sigma<1$,

$$
N_K(\sigma,T)\ll_\sigma T^{3(1-\sigma)/(2-\sigma)}(\log(2T))^{13}.
$$

The exponent is strictly below one. Summing in dyadic height intervals gives $`\sum_{\Re\rho>\sigma,\,\Im\rho>0}1/\Im\rho\lt \infty`$. Since no zero attains $\Theta$, the sum tends to zero as $\sigma\uparrow\Theta$ by dominated convergence. Choose $\sigma>\max(1/2,d)$ so the sum of $2\pi/\Im\rho$ over all such distinct zeros is less than $`L/2`$. Select any one of them, $`\rho_*=\beta_*+i\gamma_*`$. [Montgomery, *Zeros of L-functions*](https://www.mathnet.ru/eng/mat564) [Statement of the density estimate in Inoue, Lemma 1](https://numdam.org/item/10.5802/jtnb.1162.pdf#page=11)

We construct a positive averaging measure which removes every other zero strictly right of $`\sigma`$. For an unwanted distinct upper-half-plane zero $\rho_j=\beta_j+i\gamma_j$ put $h_j=2\pi/\gamma_j$. On $[0,h_j]$ use the probability density proportional to $e^{(1-\beta_j)v}$. Its transform $`M_j(w)=\int e^{wv}\,d\nu_j(v)`$ vanishes at $w=\rho_j-1$ and at its conjugate. At $`w_*=\rho_*-1`$ the exponential integral can vanish only if $\beta_* =\beta_j$ and $\gamma_*/\gamma_j$ is a positive integer $`k`$. In that case $k\ge2$ because the zeros are distinct. Multiply the density by $1+\tfrac12\cos(k\gamma_j v)$ and renormalize. The Fourier coefficients at $\pm1$ over the full period still vanish. The coefficient at $`k`$ is now nonzero, with unnormalized integral $h_j/4$ after cancellation of the real exponent. This deals with exact harmonic coincidences.

Let $`\nu`$ be the convolution of these measures for all unwanted zeros, using the point mass at zero if there are none. It exists as the law of a sum of independent variables between zero and $h_j$ with $\sum_j h_j<\infty$. Its transform is the product of their transforms. It is nonzero at $`w_*`$ since all the factors there are nonzero and $`\sum_j|1-M_j(w_*)|\ll_{w_*,L}\sum_j h_j\lt \infty`$. Apply the average to the formula for $D(u+v)$. The omitted spectrum has $\Re\rho\le\sigma$ and absolutely summable coefficients. Hence, uniformly for $u\to\infty$,

```math
\int D(u+v)\,d\nu(v)
 =2\Re\bigl(c_*e^{(\rho_*-1)u}\bigr)+O_b(e^{(\sigma-1)u}),\qquad c_*\ne0 .
```

In any full retained period $`2\pi/\gamma_*`$ the cosine reaches both extrema. This period plus the support length of $`\nu`$ is less than $`L/2`$. For all sufficiently large $`U`$, each interval $`[U,U+L]`$ therefore contains individual values of both signs with $`\pm D(u)\gg_{b,L,d} e^{(\beta_*-1)U}`$. The positivity and total mass one of $`\nu`$ justify going from averaged to individual values.

To impose $`F>c`$, choose any one fixed positive-weight twisted ordinate $\lambda$. In every $u$-interval of sufficiently large fixed length there is a subinterval of fixed length on which $1+\cos(\lambda(\log b+2u))\ge1$. Choose $L$ small enough to fit strictly inside that subinterval with fixed margins. Both witnesses then satisfy the fixed lower bound on $F$. The correction is uniformly Lipschitz, so moving each witness by $O(e^{-2u/3})$ in $u$ changes $D$ by $`o(e^{(\beta_*-1)u})`$ since $`\beta_*>1/2`$. At $x=be^{2u}$ this permits a physical interval of length $x^{2/3}$, which contains primes of class 11 by the fixed-modulus short-interval prime number theorem. The margins preserve the bound on $F$. Taking $d$ at least $1/2$ and arbitrarily close to $\Theta$ proves (2) and the lower bound in (3). The upper bound follows from the displayed bound on $D$. [Variation of the correction](CUTOFF-SCALES.md#size-of-the-derivative) [Thorner and Zaman, fixed-modulus consequence of Theorem 1.1](https://arxiv.org/pdf/2108.10878#page=3)

For the asserted number of primes, the attained case already supplies intervals of fixed positive log-length for each sign, hence $\gg X/\log X$ primes in $[X,KX]$. In the unattained case choose $d$ so close to $\Theta$ that $`0\lt \Delta=\Theta-\beta_*\lt \min(\varepsilon,1/4)`$. Split the explicit series at the same $`\sigma`$ as in the averaging argument. The part with $`\Re\rho>\sigma`$ can be differentiated absolutely and has derivative $`O_{b,\sigma}(e^{(\Theta-1)U})`$ on $`[U-1,U+L+1]`$, since $`\sum_{\Re\rho>\sigma}(1+|\gamma|)^{-1}\lt \infty`$. The rest, including the explicit-formula error, is uniformly $`O_b(e^{(\sigma-1)U})=o(e^{(\beta_*-1)U})`$. Thus each signed witness from the average retains its sign and at least half its lower bound on a log interval of length $`c_{b,\sigma,\rho_*,L}e^{-\Delta U}`$. The fixed padding preserves $`F>c`$. In the ordinary prime variable this interval has length $`\gg_{b,\varepsilon}X^{1-\Delta/2}`$, and contains $`\gg_{b,\varepsilon}X^{1-\Delta/2}/\log X`$ primes of the required residue. Since $`\Delta/2\lt \varepsilon`$ and $`\beta_*>1/2`$, both the claimed count and the two thresholds on $\pm B_p$ follow for sufficiently large $X$. The choice of a good arc inside each block used only $\lambda$, so $K$ is fixed.

Multiplicative-interval oscillation already appears in Ingham's work on the ordinary prime number theorem. Kaczorowski and Pintz prove sign changes with an amplitude bound in every $[Y^{1-\varepsilon},Y]$ under analytic hypotheses on a Mellin transform. The calculation here exploits the absolute convergence of this smoothed correction and also controls $F$ at prime sampling points. The result-specific refinement is the fixed-ratio conclusion at ordinary primes of class 11 with a simultaneous positive lower bound on $F$. [Ingham, *A note on the distribution of primes*](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/1/2/93180/a-note-on-the-distribution-of-primes) · [Kaczorowski and Pintz, *Oscillatory properties of arithmetical functions II*, (1.6)–(1.8)](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1987.Kaczorowski_2.pdf)
