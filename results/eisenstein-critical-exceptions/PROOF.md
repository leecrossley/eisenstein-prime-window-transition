# Exceptional scales at the critical Eisenstein width

Fix $K=\mathbb Q(\sqrt{-3})$, let $\chi_4$ and $\chi_{12}$ be the primitive real characters of discriminants $-4$ and $12$, and write

$$
A_b(y)=-\sum_{\mathfrak p\nmid6}\chi_4(N\mathfrak p)\log(N\mathfrak p)\thinspace W_b(N\mathfrak p/y).
$$

The weight is $b(1-1/t)$ on $1<t\le b$, $b^2/t-1$ on $b<t<b^2$ and zero elsewhere. Both outer endpoints have weight zero. Each retained ideal contributes to the class of its absolute norm. We assume GRH for $L(s,\chi_4)$ and $L(s,\chi_{12})$ throughout.

## The arithmetic error at a fixed width

In $K$, a rational prime $p>3$ congruent to 1 modulo 3 splits into two prime ideals of norm $p$. A prime congruent to 2 modulo 3 is inert and gives one ideal of norm $p^2$. The character $\chi_{12}$ is the product of $\chi_4$ with the quadratic character of $K$. Thus for the full ideal prime-power sum the factors are $L(s,\chi_4)L(s,\chi_{12})$ up to the omitted Euler factors. The factors have the same character value at split primes and opposite values at inert primes. At 2 both primitive factors have zero Dirichlet coefficient. At 3 the excess primitive Euler factor contributes $O_b(1)$ in a compact multiplicative window, since only boundedly many powers of 3 fit inside it. [Exact factorization and earlier endpoint proof](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/c1e11263b1cf6e8de187742f246b32992455658f/PROOF.md)

Write $\vartheta_K^\ast(x)=\sum_{\mathfrak p\nmid6,\ N\mathfrak p\le x}\log N\mathfrak p$. Splitting gives

$$
\vartheta_K^\ast(x)=2\vartheta(x;3,1)+O(\sqrt x\log(2x))
                 =x+O\big(xe^{-c_0\sqrt{\log x}}\big),\qquad x\ge2,
$$

for some $c_0>0$. In the first equality the inert primes have $p\le\sqrt x$. The second uses the unconditional prime number theorem in the single fixed progression $1\bmod3$. In particular the untwisted prime-ideal input here has a quantitative remainder independent of the two GRH assumptions. [Fixed-modulus prime number theorem, Corollary 21](https://personal.science.psu.edu/rcv4/568s20/568chapter11.pdf) · [Siegel–Walfisz estimate, Theorem 2.2](https://doi.org/10.1017/prm.2024.42)

All retained prime squares carry character $+1$. Their contribution when higher powers are removed from the signed explicit formula is

$$
\int W_b((u/\sqrt y)^2)\thinspace d\vartheta_K^\ast(u)
    =B_b\sqrt y+O_b\big(\sqrt y\thinspace e^{-c_1\sqrt{\log y}}\big),
\qquad B_b=2\sqrt b\thinspace(\sqrt b-1)^2 .
$$

Indeed the integral is supported on $[\sqrt y,b\sqrt y]$. Replacing $d\vartheta_K^\ast$ by $du$ gives $\sqrt y\int_1^b W_b(v^2)\thinspace dv=B_b\sqrt y$. Integration by parts bounds the remainder by the supremum of the counting error on that interval times the total variation $2(b-1)$ of the weight. A smaller constant $c_1>0$ absorbs the change of scale. The powers of exponent at least three have total absolute contribution $O_b(y^{1/3}\log^2 y)$ by counting possible rational primes and exponents. This allows either sign for the cubes.

Let $t=\log(by)$. If $\rho=1/2+i\tau$, the Mellin coefficient of the weight at $\rho$ has phase $e^{i\tau\log b}$ and magnitude

$$
h_b(\tau)=\frac{\sqrt b\thinspace[b+1-2\sqrt b\cos(\tau\log b)]}{1/4+\tau^2}>0 .
$$

Neither factor has a central zero. For positive real $s$, the Dirichlet series for $\chi_4$ has positive paired terms. For $\chi_{12}$ each block is $f(12j+1)-f(12j+5)-f(12j+7)+f(12j+11)>0$, since $f(x)=x^{-s}$ has decreasing positive differences $f(x)-f(x+4)$. Grouping complete periods is valid for real $s>0$. The zero sums converge absolutely by the quadratic denominator and standard zero counting. The trivial zeros, including the even character's zero at $s=0$, cost $O_b(1)$ for $y\ge2$.

Let $\Gamma$ be the union of the **distinct** positive ordinates. For $\tau\in\Gamma$, let $m(\tau)$ count its total multiplicity in both factors, and put $a_\tau=2m(\tau)h_b(\tau)$. The explicit formula and the estimates above give, with some $\eta>0$,

$$
\frac{A_b(y)}{\sqrt y}=B_b+\sum_{\tau\in\Gamma}a_\tau\cos(\tau t)+O_b(e^{-\eta\sqrt t}) .
$$

Here and below $t$ is sufficiently large. The constants depend only on the fixed field, characters and width. The prime-cube, ramified and trivial-zero errors after normalization are absorbed in this remainder. At $b=b_K$ the equality $B_b=\sum_{\tau\in\Gamma}a_\tau$ is exact. Consequently the full main expression at this width is the nonnegative function

$$
F(t)=\sum_{\tau\in\Gamma}a_\tau(1+\cos(\tau t)).
$$

The identity uses the exact root, even though its value is specified numerically by an enclosure. Substitution of a rounded decimal could leave a fixed signed term. [Root definition, uniqueness and bracket](https://github.com/leecrossley/eisenstein-prime-window-transition/tree/c1e11263b1cf6e8de187742f246b32992455658f)

## One zero controls the logarithmic measure

Fix any $\lambda\in\Gamma$. For $d(x)=\mathrm{dist}(x,\pi(2\mathbb Z+1))$ we have $0\le d(x)\le\pi$ and

$$
1+\cos x=2\sin^2(d(x)/2)\ge2d(x)^2/\pi^2.
$$

At every sufficiently large $y$ with $A_b(y)\le0$ we therefore have

$$
d(\lambda t)\le C_\lambda e^{-\eta\sqrt t/2}.
$$

On any unit interval $[U,U+1]$, the admissible values of $t$ lie in a bounded number of intervals about the points $(2k+1)\pi/\lambda$, each of length $O_\lambda(e^{-\eta\sqrt U/2})$. Indeed their centres have constant spacing and the widths tend to zero. Since $dt=dy/y$, summation over the unit intervals starting at $T=\log(bY)$ bounds the exceptional measure on $[Y,\infty)$. For $a>0$ the tail $\sum_{n\ge0}e^{-a\sqrt{T+n}}$ is $O_a((1+\sqrt T)e^{-a\sqrt T})$ by the integral test. A smaller positive exponent absorbs the polynomial. It follows that

$$
\int_{\lbrace y\ge Y\thinspace:\thinspace A_{b_K}(y)\le0\rbrace}\frac{dy}{y}\ll e^{-c\sqrt{\log Y}}
$$

for some $c>0$. Any bounded interval in $[1,\infty)$ has finite logarithmic measure. This proves the finite-measure and density-one statements, including ties.

## Two zeros and eventual positivity

Take distinct $\lambda,\mu\in\Gamma$ and let $\alpha=\mu/\lambda$. For large $t$ choose odd positive integers $q,p$ nearest to $\lambda t/\pi,\mu t/\pi$, respectively. Then

$$
\pi|q\alpha-p|\le\alpha\thinspace d(\lambda t)+d(\mu t),\qquad q\asymp_{\lambda}t.
$$

If the exceptional scales are unbounded, the preceding one-zero estimate applied to both phases yields an unbounded sequence of odd $q$ and odd $p$ with

$$
|q\alpha-p|\le C_{\lambda,\mu}\exp(-c_{\lambda,\mu}\sqrt q).
$$

This is necessary for **each** fixed pair of distinct ordinates. The denominators may depend on the chosen reference ordinate. There is no simplicity or independence assumption.

Conversely, suppose for **one** pair there are $d_0,\nu>0$ such that $|q\alpha-p|\ge d_0q^{-\nu}$ for all sufficiently large odd positive $q$ and all odd $p$. At every large $t$, one of $d(\lambda t),d(\mu t)$ is then $\gg t^{-\nu}$. The two positive coefficients in $F$ give $F(t)\gg t^{-2\nu}$. The error $O(e^{-\eta\sqrt t})$ is smaller than half that lower bound eventually. Hence

$$
A_{b_K}(y)\gg_{\lambda,\mu,d_0,\nu}\frac{\sqrt y}{(\log y)^{2\nu}}
$$

for all sufficiently large $y$. An irrational ratio of finite irrationality exponent satisfies the required inequality, by taking a rational approximation exponent strictly larger than its irrationality exponent and multiplying through by $q$. Reduced fractions suffice for that definition, since reducing a denominator only strengthens the lower bound.

Qualitative rational independence supplies no rate in this argument. For example, let $m_1=2$, $m_{j+1}=3^{m_j}$ and $\alpha=1+\sum_{j\ge1}2\cdot3^{-m_j}$. The nonperiodic ternary digits give an irrational number. Its truncations have odd numerator and denominator $q_j=3^{m_j}$, with $|q_j\alpha-p_j|\ll q_j3^{-q_j}$. Taking $t=\pi q_j$ makes the phases for $1,\alpha$ approach odd multiples exponentially closely. This tests the inference from independence in a two-frequency model. The arithmetic sign at the true cutoff under the two GRHs alone remains undetermined.

## Checking actual ordinates

The release supplies witnesses $\lambda\in(5,7)$ for $\chi_4$ and $\mu\in(3,4)$ for $\chi_{12}$. These are disjoint intervals of sign change for the real completed functions on the critical line. Each contains at least one zero, and the phase argument works for any such choice. The earlier bracket for $b_K$ gives pair weights exceeding $0.10$ and $0.32$, respectively, since $2h_b(\tau)\ge 2\sqrt b(\sqrt b-1)^2/(1/4+\tau^2)$.

The first calculation encloses the Hardy functions at the four endpoints and verifies the primitive characters, parities and residue values. The independent calculation directly sums $\sum_{n\le12000}\chi(n)n^{-1/2-it}$. The cutoff is a multiple of each conductor and every incomplete subsequent period has character sum of modulus at most one. Partial summation bounds the whole complex tail by $2|1/2+it|/\sqrt{12000}$. Multiplication by the completed gamma factor keeps the signs separated from zero even with this error. Both real primitive quadratic characters have root number $+1$, so the completed functions are real on the line. These certificates locate witnesses for the phase inequalities. Irrationality properties of their ratio are outside the scope of the computation. [Recorded output](evidence/check.txt) · [Dirichlet zero counting and completed functions](https://doi.org/10.1090/mcom/3599)

## Earlier results

The earlier Eisenstein theorem gives the crossing and the limiting endpoints. Merely knowing a normalized liminf of zero allows both eventual positivity and arbitrarily late losses. The new assertions are a shrinking upper bound for the logarithmic measure of the critical race's actual nonpositive scales and an odd-rational approximation obstruction to unbounded losses. They use the fixed-modulus remainder and one or two positive zero coefficients. [Earlier Eisenstein result](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/c1e11263b1cf6e8de187742f246b32992455658f/PROOF.md)

Sheth's Corollary 4.2 gives, outside a set of finite logarithmic measure, a cumulative rational-prime bias with weights $1/\sqrt p$ and main term $\frac12\log\log x$. That main term, support and normalization differ from this compact ideal-norm sum at exact cancellation. An asymptotic for the cumulative sum up to $x$ would lose its growing drift on taking a compact difference. The result here also bounds the exceptional tail beyond each $Y$ and constrains the ratios of zero ordinates at any unbounded sequence of losses. [Sheth, §4.1 and Corollary 4.2](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/euler-products-at-the-centre-and-applications-to-chebyshevs-bias/1DA1AFD9BE7EBCF9D5B49FE792E55E81)

Rubinstein–Sarnak and Devin obtain limiting distributions and logarithmic densities for prime races. Fiorilli and Jouve obtain eventual dominance for prime-ideal races through different conjugacy-class conditions. Bailleul and coauthors use quantitative approximations involving zero ordinates to bound generalized Skewes numbers for races between residue classes. Their effective linear-independence hypothesis concerns collections of ordinates, and their bounds concern first occurrences of prescribed deviations. The condition above concerns only one ratio, restricted to two odd integers. I found no prior derivation of the two critical-window assertions for this norm race in these sources. [Rubinstein–Sarnak](https://www.math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf) · [Devin](https://arxiv.org/abs/1706.06394) · [Fiorilli–Jouve](https://www.numdam.org/articles/10.5802/jep.192/) · [Bailleul and coauthors](https://arxiv.org/abs/2603.20093)

Grenié–Molteni used the same centered kernel. Zhao treated integrated quadratic-character errors, and Suzuki studied one-sided sign criteria for other weighted sums. The underlying investigation began with Alpöge's theta lifts. The present proof uses the Dirichlet factors and the untwisted prime count in the actual Eisenstein field. [Grenié–Molteni](https://arxiv.org/pdf/1607.02430#page=6) · [Zhao](https://arxiv.org/html/2411.18903v2) · [Suzuki](https://arxiv.org/html/2411.07436v2) · [Alpöge's announcement](https://alpo.ge/remark.pdf)
