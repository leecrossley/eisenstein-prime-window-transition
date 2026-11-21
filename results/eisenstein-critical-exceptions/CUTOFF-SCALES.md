# The size and spacing of possible exceptions

Use $b=b_K$, $t=\log(by)$, $z=\sqrt y$, and $D=2\sqrt b(\sqrt b-1)^2$. The signed arithmetic remainder is $R(y)=A_b(y)-zF(t)=-zB(t)$. Except where an arithmetic assertion is explicitly unconditional, assume GRH for the primitive characters of discriminants $-4$ and $12$. The [original proof](PROOF.md) gives the cutoff identity, the positivity and multiplicity of the coefficients, and the absence of a central zero.

The remainder takes both signs on the $y^{1/4}$ scale. The spectral function has the pointwise floor $F(t)\gg_b t^2e^{-t/2}$. If there are exceptions, their positions cluster on a much shorter scale than the distances between clusters. These conclusions concern different quantities. The sign of $F(t)-B(t)$ at every sufficiently late $t$ remains open.

## The arithmetic correction

Let $\chi(\mathfrak p)=\chi_4(N\mathfrak p)$ on the retained prime ideals. In removing the higher powers from the full twisted explicit formula, all the even exponents contribute

$$
E(y)=\sum_{\mathfrak p\nmid6}\sum_{j\ge1}\log N\mathfrak p\,
             W_b((N\mathfrak p)^{2j}/y).
$$

Let $J(y)$ denote the analogous sum at odd exponents $k\ge3$, with weight $\chi(\mathfrak p)\log N\mathfrak p$. Set $D=2\sqrt b(\sqrt b-1)^2$ and $R_0(y)=E(y)+J(y)-D\sqrt y$. This is an arithmetic function defined without any zero hypothesis. Under the two GRHs, $R(y)=R_0(y)+O_b(1)$ for $y\ge2$. The bounded terms are the omitted local factor at 3 and the trivial zeros. In fact the trivial zeros enter $A$ with positive weights $y^{-m}H_b(-m)$, including $m=0$ for the even character. Here $H_b(s)=(b^s-1)(b^s-b)/(s(s-1))$ is the Mellin transform of $W_b$.

Write $\zeta_K^*$ for the Dedekind zeta function with its Euler factors above 2 and 3 omitted. Define $P_\chi(z)=\sum_{\mathfrak p\nmid6}\chi(\mathfrak p)\log N\mathfrak p/(N\mathfrak p)^z$ initially for $\Re z>1$. For $\Re s>1/2$ the Mellin transform $\int_1^\infty R_0(y)y^{-s-1}dy$ equals

$$
H_b(s)\left[-\frac{(\zeta_K^*)'}{\zeta_K^*}(2s)
       +\sum_{\substack{k\ge3\\k\ {\rm odd}}}P_\chi(ks)\right]
       -\frac{D}{s-1/2}+G(s).
$$

Here $G$ is entire, since the finite-window sums below $y=1$ have compact support away from zero. Unconditionally $P_\chi$ is meromorphic in $\Re z>1/2$. Subtract from the negative logarithmic derivative of the two twisted factors, with the omitted local factor removed, the absolutely convergent contributions of exponents at least two. Any zero of the twisted product there contributes a negative residue equal to its multiplicity with a minus sign. This continues the whole odd sum meromorphically to $\Re s>1/6$. Its terms with $k\ge7$ converge absolutely and locally uniformly there. Under the two GRHs the entire odd sum is holomorphic in this half-plane.

The simple pole at $s=1/2$ cancels because $H_b(1/2)/2=D$. There are no further real poles for $s>1/6$. Indeed $\zeta_K(z)=\zeta(z)L(z,\chi_{-3})$. The alternating eta series excludes real zeta zeros for $0<z<1$, while the positive paired blocks $(3n+1)^{-z}-(3n+2)^{-z}$ exclude them for the second factor at every real $z>0$. The two twisted functions also have no positive real zeros. For $f(x)=x^{-z}$ and real $z>0$, the conductor-4 series has positive paired differences and the conductor-12 blocks $f(12n+1)-f(12n+5)-f(12n+7)+f(12n+11)$ are positive by convexity. Omitting local factors introduces no zero with positive real part.

Take a critical-line zeta zero $\rho=1/2+i\gamma$ with $14<\gamma<15$. Two independent computations certify opposite endpoint signs of the real completed function. At $s_0=\rho/2$ the transform has a genuine pole of residue $r=-(m/2+n/3)H_b(s_0)$, where $m\ge1$ is the order of the zero upstairs in $\zeta_K$ and $n\ge0$ is the order of vanishing of the twisted product at $3s_0$. The cubic contribution, if present, has the same sign in the residue multiplier. All $k\ge5$ have $\Re(ks_0)>1$. Under the two GRHs $n=0$. Since $1.45<b^{1/4}<1.46$, the two numerator factors in $|H_b(s_0)|$ exceed $0.45$ and $3$, and each denominator factor has modulus below $8$. Thus $|r|>1/100$.

For completeness, suppose $R_0(y)\le c y^{1/4}$ eventually with $0<c<|r|$. The Mellin transform of $c y^{1/4}-R_0(y)$ has no real singularity to the right of $1/4$. By Landau's theorem its defining integral converges there, after discarding a bounded initial interval. Its nonnegative tail gives $|\widehat G_c(\sigma+i\gamma/2)|\le\widehat G_c(\sigma)+O(1)$ as $\sigma\downarrow1/4$. Multiplication by $\sigma-1/4$ gives $|r|\le c$, a contradiction. Applying the same argument to $-R_0$ proves the following inequalities unconditionally for $R_0$ and, under the two GRHs, for $R$ as well.

$$
\limsup_{y\to\infty}\frac{R(y)}{y^{1/4}}\ge |r|>\tfrac1{100},\qquad
\liminf_{y\to\infty}\frac{R(y)}{y^{1/4}}\le-|r|<-\tfrac1{100}.
$$

This precludes a proof by eventual nonnegativity of the prime-power correction. It leaves open the size of $F$ when the correction is negative. The oscillation mechanism is classical. Kaczorowski and Staś discuss antecedents of this argument for the prime-ideal theorem. [Kaczorowski and Staś](https://bibliotekanauki.pl/articles/727867.pdf) · [Landau's one-sign criterion in this prime race](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/c1e11263b1cf6e8de187742f246b32992455658f/PROOF.md)

## A positive lower bound from the conductor-4 zeros

For $x=e^t$ and $0<w<\min(1,t/2)$ set $k(u)=2(1-\cos u)/u^2$, with $k(0)=1$. For either primitive character the explicit formula for a log tent gives

$$
\sum_n\frac{\Lambda(n)\chi(n)}{\sqrt n}
     (1-|\log(n/x)|/w)_+
  =-2w\sum_{\gamma_\chi>0} k(w\gamma_\chi)\cos(\gamma_\chi t)
       +O(w x^{-1/2})
$$

for $x$ large. Its Mellin transform at $s$ is $x^{s-1/2}w\int_{-1}^1(1-|u|)e^{(s-1/2)wu}du$. On the critical line this gives $k$ and the sum converges absolutely. The negative integer residues form a geometric bound. At a fixed $x>1$ the implied constant can depend on $x$ and the same argument applies as $w\downarrow0$. There is no pole at one or central zero.

## How far apart two exceptions can be

Choose $\eta>0$ from the known arithmetic bound $|R(y)|/\sqrt y\ll e^{-\eta\sqrt t}$. If both $t$ and $t+h$ are logarithmic scales of ties or reversals, with $t$ sufficiently large and $h>0$, then

$$
h\ll_b\frac{e^{-\eta\sqrt t}}{\sqrt t}
\qquad\text{or}\qquad
h\ge 2\eta\sqrt t+2\log t-O_b(1).
$$

In particular only $O_b(\sqrt T)$ unit logarithmic blocks meeting $[T,2T]$ can contain any exception. Writing $\mathcal E=\{t:A_{b_K}(e^t/b_K)\le0\}$, one also has

$$
|\mathcal E\cap[T,\infty)|\ll_b\frac{e^{-\eta\sqrt T}}{\sqrt T}.
$$

The proof uses both signs of the spectral expression

$$
F_\pm(h)=\sum_{\gamma>0}a_\gamma(1\pm\cos(\gamma h)),\qquad F_+=F .
$$

For all sufficiently large $h$ one has $\min(F_+(h),F_-(h))\gg_b h^2e^{-h/2}$. Here is a direct proof at the square-root scale. Use just the conductor-4 zeros to get a lower bound for each nonnegative sum. Set $z=e^h$, take $w=\epsilon h/\sqrt z$ with a sufficiently small fixed $\epsilon>0$, and use the even tent formula from the preceding section with $T=1/w$. With $k(u)=2(1-\cos u)/u^2$, its zero count gives

$$
2w\sum_{\gamma_4>0} k(w\gamma_4)\gg \log(1/w)\gg h .
$$

The first lower bound follows already from $1/w\le\gamma_4\le2/w$. On the other hand the absolute value of the signed prime-power side is $O(\epsilon h)+o(1)$ as $h\to\infty$. Indeed the interval has length $Y=2z\sinh w\asymp\epsilon h\sqrt z$. The Brun–Titchmarsh inequality bounds the rational prime count by $2Y/\log Y$, and each normalized log weight is $O(h/\sqrt z)$. For each fixed $\epsilon$, $\log Y\ge h/3$ eventually, so the implied constant multiplying $\epsilon h$ is absolute. The rational squares contribute $O((1+w\sqrt z)h/\sqrt z)=o(1)$ and all exponents at least three contribute $O(h^2 z^{-1/6})$. The trivial-zero remainder is $O(w z^{-1/2})$. Choosing $\epsilon$ small therefore gives $2w\sum k(w\gamma_4)(1\pm\cos(\gamma_4 h))\gg h$ for both signs. Since $w^2 k(w\gamma)\ll(1+\gamma^2)^{-1}$, the coefficient lower bound implies $F_\pm(h)\gg_b wh\gg_b h^2e^{-h/2}$. In particular the unnormalized leading term $\sqrt y\,F(\log(b_K y))$ grows at least as a constant times $(\log y)^2$. The oscillating arithmetic correction can reach order $y^{1/4}$. [Montgomery and Vaughan, Theorem 2 and equation (1.12)](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf#page=3)

For $0<h<h_0$ with $h_0$ sufficiently small, the same band $1/h\le\gamma_4\le2/h$ in the zero count gives $F_-(h)\gg_b h\log(1/h)$, because $1-\cos(\gamma_4h)$ is bounded below on that band. Also $F_-(h)>0$ at every fixed $h>0$. Otherwise all conductor-4 phases there would equal one. Letting $w\downarrow0$ in the tent formula at that fixed $z=e^h>1$ would give an unbounded log-weight from the zeros, whereas the compactly supported prime-power sum stays bounded. Continuity of $F_-$ by absolute convergence gives a positive minimum on each compact subinterval of $(0,\infty)$.

Now $|1-e^{i\gamma h}|\le |1+e^{i\gamma t}|+|1+e^{i\gamma(t+h)}|$, so a pair of exceptions gives $F_-(h)\le2F(t)+2F(t+h)\ll_b e^{-\eta\sqrt t}$. The small-$h$ estimate first gives $h\ll e^{-\eta\sqrt t}$ and then $h\ll e^{-\eta\sqrt t}/\sqrt t$ on substituting back. The compact range is excluded for large $t$. In the large range, $h^2 e^{-h/2}\ll e^{-\eta\sqrt t}$ first gives $h\ge 2\eta\sqrt t-O_b(1)$, and substituting this into $h\ge2\eta\sqrt t+4\log h-O_b(1)$ gives the claimed logarithmic term.

For the covering and measure estimates partition the tail at $T_j=(\sqrt T+j\eta/2)^2$, $j=0,1,\ldots$. Each successive interval has length $\eta\sqrt{T_j}+O_b(1)$, below the long-gap threshold. Its exceptional subset thus has diameter $O_b(e^{-\eta\sqrt{T_j}}/\sqrt{T_j})$. Summing gives the tail bound by a geometric series. There are $O_b(\sqrt T)$ such intervals meeting $[T,2T]$ and each exceptional subset meets at most two consecutive unit blocks for large $T$, up to endpoint conventions. These estimates still allow an unbounded sequence of isolated exceptions. [Earlier single-zero measure bound](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/main/results/eisenstein-critical-exceptions/PROOF.md)

### Using the fixed-modulus Vinogradov–Korobov region

Put $g(t)=t^{3/5}/(\log t)^{1/5}$ for $t$ large. There is a fixed $\kappa>0$ such that $|R(y)|/\sqrt y\ll_b \exp(-\kappa g(t))$. To see this directly, the Mellin formula for $E(y)$ above puts the nontrivial zeros of $\zeta(s)L(s,\chi_{-3})$ into the error with terms $-\tfrac12 y^{\rho/2}H_b(\rho/2)$ counted with multiplicity. This is the usual smoothed explicit formula with Mellin multiplier $H_b(s)$ and the change of variable $2s$ in the logarithmic derivative. The pole at $1/2$ gives $D\sqrt y$. The omitted Euler factors make bounded contributions in the compact multiplicative window. The residue at zero and the trivial-zero sum are $O_b(1)$ for large $y$, since the multiplier is regular at zero and the terms at negative arguments decay in $y$.

The multiplier at the nontrivial zeros is $O_b((1+|\Im\rho|^2)^{-1})$. Above height $H=\exp(g(t))$ the absolute normalized tail is $O_b((\log H)/H)$ by zero counting and $\Re\rho\le1$. Up to this height the fixed-conductor Vinogradov–Korobov regions for both factors give $1-\Re\rho\gg(\log H)^{-2/3}(\log\log H)^{-1/3}$. The bounded-height range is included by nonvanishing on $\Re s=1$ and discreteness. Thus $y^{-(1-\Re\rho)/2}\ll_b\exp(-\kappa' g(t))$ and the sum of the multiplier bounds is finite. The odd powers cost $O_b(y^{1/3}\log^2 y)$ in unnormalized units, completing the claim with some $\kappa>0$. The two zero-free regions used in this remainder estimate are unconditional. [Vinogradov–Korobov region for zeta and Khale's Theorem 1.1 for Dirichlet functions](https://arxiv.org/pdf/2210.06457#page=1)

Write $\Delta(t)=\exp(-\kappa g(t))$. At an exception $F(t)\ll_b\Delta(t)$, which is $o(v^A)$ for every fixed $A>0$ at each width $v=e^{-c\sqrt t}$ for fixed $c>0$. For two exceptions the small-gap bound now becomes $h\ll_b\Delta(t)/g(t)$ and the large-gap bound becomes $h\ge2\kappa g(t)+4\log g(t)-O_b(1)$, by the same estimates for $F_-$. Subdivide $[T,2T]$ into intervals of length at most $\kappa g(T)$ and comparable to $g(T)$ except possibly the last. Each contains at most one exceptional subset of the stated small diameter. Hence the number of unit blocks containing exceptions in $[T,2T]$ is $O_b(T/g(T))$. One also obtains $|\mathcal E\cap[T,\infty)|\ll_b\Delta(T)/g(T)$ by using the previous partition at $T_j=(\sqrt T+j\eta/2)^2$. Indeed $g(T_{j+1})-g(T_j)\gg1$ uniformly for large $T$, since $\sqrt u\,g'(u)\to\infty$. These conclusions concern the actual ideal-prime race at the exact cutoff.

### A common odd divisor for the exceptional scales

Fix the conductor-4 ordinate $\lambda\in(5,7)$ used in the finite certificate. Choose any $0<\epsilon<\kappa/4$ and put $Y=\exp(\epsilon g(T))$. To each exceptional $t\in[T,Y]$ attach the nearest odd integer $k(t)$ to $\lambda t/\pi$. If this range contains exceptions, all these integers have a common odd divisor $m$ satisfying

$$
\frac{\pi m}{\lambda}\ \ge\ (2\kappa-8\epsilon)g(T)-O_b(1).
$$

In particular, on a dyadic range $[T,2T]$ there is a single spacing $\tau\ge 2\kappa g(T)-O_b(\log T)$ such that every exceptional scale in the range lies within $O_b(T\Delta(T)/g(T)^2)$ of an **odd** multiple of $\tau$. This also covers a range containing just one exceptional scale. The spacing can depend on the range.

For the proof write $\delta=\Delta(T)$. The individual term at $\lambda$ in $F$ gives $|t-\pi k(t)/\lambda|\ll_b\sqrt\delta$ at every such $t$. In particular the nearest odd integer is unique for large $T$. There are at most $O_b(Y)$ different labels. Take a representative $t_i$ for each, put $m=\gcd_i k(t_i)$ and $r_i=k(t_i)/m$. The $r_i$ are coprime as a set, and all are odd. There are integers $b_i$ such that $\sum b_i r_i=1$ and $\sum|b_i|\ll_b Y^2$. Indeed, take any Bézout solution, reduce each $b_i$ for $i\ne0$ to $[0,r_0)$ modulo $r_0$, and restore the equality using $b_0$. The other coefficients sum to $O_b(Yr_0)$ and $|b_0|\le1+\sum_{i\ne0}r_i=O_b(Y^2)$.

Put $h=\sum b_i t_i$. Then $|h-\pi m/\lambda|\ll_b Y^2\sqrt\delta=o(1)$. Since $\sum b_i$ is odd, the triangle inequality on the unit circle, followed by Minkowski's inequality with weights $a_\gamma$, gives $F_+(h)^{1/2}\le\sum |b_i|F(t_i)^{1/2}$. Thus $F_+(h)\ll_b Y^4\delta$. At every fixed $h>0$ the function $F_+(h)$ is strictly positive by the same tent argument as for $F_-$: exact alignment at $-1$ makes the zero sum unbounded at that fixed argument as the width tends to zero. Also $F_+(0)>0$. Continuity excludes every bounded $h$ here for large $T$. Using $F_+(h)\gg_b h^2 e^{-h/2}$ now gives $h\ge2\kappa g(T)-8\log Y-O_b(1)$. Taking $Y=\exp(\epsilon g(T))$ proves the first assertion. The same proof with $Y=2T$ gives $\pi m/\lambda\ge2\kappa g(T)-O_b(\log T)$.

In the dyadic case fix one representative $t_0$, let $r_0=k(t_0)/m$ and take $\tau=t_0/r_0$. For any exception $t$ put $r=k(t)/m$. The two integers $r_0,r$ are odd and comparable to $T/m$. Write $u=r_0t-rt_0$. The single-ordinate approximation gives $|u|\ll_b (T/m)\sqrt\delta$. The weighted triangle inequality for these two integer multiples gives $F_-(u)\ll_b(T/m)^2\delta$. If $u\ne0$, then $\log(1/|u|)\gg_b g(T)$ and the small-argument lower bound for $F_-$ improves this to $|u|\ll_b(T/m)^2\delta/g(T)$. Dividing by $r_0$ and using $m\gg_b g(T)$ gives the claimed distance to $r\tau$. Also $|\tau-\pi m/\lambda|\ll_b\sqrt\delta/r_0$. This simultaneous restriction allows isolated exceptions at unbounded scales.

### Size of the derivative

Write $\delta_n=\exp(-\kappa g(n))$ and $w(v)=W_b(v^2)$. Both one-sided derivatives with respect to $t$ satisfy $|B'(t\pm)|\ll_b\delta_n$ on $[n-1,n+2]$, after decreasing $\kappa>0$ if necessary. In the rational prime-power expression for $E/z$, the differentiated weight is $-(w(v)+vw'(v))/(2z)$, with $v=n'/z$ for the rational prime power $n'$. The function $w+vw'$ has bounded variation and integral $[v w(v)]_1^b=0$. The summatory retained untwisted coefficients are $u+O_b(u\exp(-c(\log u)^{3/5}/(\log\log u)^{1/5}))$ by the fixed-modulus prime number theorem with its Vinogradov–Korobov error. Partial summation gives the stated bound for $(E/z)'$, also at the one-sided prime-power endpoints. Direct differentiation of the original odd-power tents costs $O_b(y^{-1/6}\log^2(2y))$ for $(J/z)'$, using the elementary unsigned count. The ramified and trivial terms have one-sided derivatives $O_b(1/z)$ after normalization. Continuity across all corners gives $|B(t+h)-B(t)|\ll_b\delta_n |h|$ for $|h|\le1$. [Fixed-modulus prime number theorem](https://arxiv.org/pdf/2108.10878#page=3)

### The lead on either side of a hypothetical exception

The two GRHs give an asymptotic for the actual normalized race at every sufficiently separated neighbour of a hypothetical exception. With $b=b_K$ and $c_*=\log(2\sqrt3/\pi)-\gamma_{\rm E}$, the spectral function $F_-$ has the expansion

$$
F_-(h)=\sqrt b(b+1)|h|\big(\log(1/|h|)+1+c_*\big)
           +O_b\!\big(h^2\log^2(2/|h|)\big)\qquad(h\to0).
$$

To see this separately for each conductor $q$, replace $(1/4+\gamma^2)^{-1}$ by $\gamma^{-2}$ in the sum of $1-\cos(h\gamma)$ at a cost $O_q(h^2)$. The positive-ordinate count is $u(2\pi)^{-1}\log(qu/(2\pi e))+O_q(\log(2+u))$, with multiplicities. Integration by parts bounds the counting remainder by $O_q(h^2\log^2(2/|h|))$. Indeed the derivative of $(1-\cos(hu))/u^2$ is $O(h^2/u)$ on $1\le u\le1/|h|$ and $O(|h|/u^2+1/u^3)$ above. On $0<u<1$ the integrand is bounded and smooth at zero. The main integral gives

$$
\sum_{\gamma_q>0}\frac{1-\cos(h\gamma_q)}{1/4+\gamma_q^2}
=\frac{|h|}{4}\left(\log(1/|h|)+1-\gamma_{\rm E}+\log\frac q{2\pi}\right)
 +O_q\!\big(h^2\log^2(2/|h|)\big).
$$

The constants follow from the value and derivative at $z=0$ of $\int_0^\infty (1-\cos u)u^{z-2}du=\Gamma(z)\sin(\pi z/2)/(1-z)$, obtained by integration by parts for $0<\Re z<1$ and continued across zero. This gives $\pi/2$ and $\pi(1-\gamma_{\rm E})/2$. The factor $\cos(\gamma\log b)$ in $a_\gamma$ contributes $O_b(h^2)$. For $J_q(u)=\sum_{\gamma_q>0}\cos(\gamma_q u)/(1/4+\gamma_q^2)$ its contribution is a constant times $J_q(\log b)-(J_q(\log b+h)+J_q(\log b-h))/2$. Write $G_q(u)=\sum_\gamma e^{i\gamma u}/(1/2+i\gamma)$ in symmetric order, summing over both signs. In distributions $2J'_q=J_q-G_q$ by pairing the two signs of each ordinate. The sharp explicit formula for $G_q$ is smooth near $\log b$ since $4<b<5$. Thus $J_q$ has two continuous derivatives there. Summing the two conductor formulas proves the displayed expansion. [Dirichlet zero count](https://arxiv.org/abs/2005.02989) · [Sharp explicit formula for a primitive character](https://www.impan.pl/shop/en/publication/transaction/download/product/91016)

If $t=\log(by)$ is exceptional set $\delta=\exp(-\kappa g(t))$. In the weighted Hilbert norm of the zero phases, $|\sqrt{F(t+h)}-\sqrt{F_-(h)}|\le\sqrt{F(t)}\ll_b\sqrt\delta$. This follows from $|(1+e^{i\gamma(t+h)})-(1-e^{i\gamma h})|=|1+e^{i\gamma t}|$ and the weights $a_\gamma/2$. The arithmetic error at $t+h$ is $O_b(\delta)$ uniformly for $|h|=o(1)$. Hence for $h\to0$ with $|h|\log(1/|h|)/\delta\to\infty$,

$$
\frac{A_b(e^{t+h}/b)}{\sqrt{e^{t+h}/b}}
   \sim \sqrt b(b+1)|h|\log(1/|h|).
$$

If $\delta\log(1/|h|)=o(|h|)$, the same expression equals $\sqrt b(b+1)|h|(\log(1/|h|)+1+c_*)+o(|h|)$. Indeed the extra error is $O_b(\sqrt{\delta |h|\log(1/|h|)}+\delta)$. The error is uniform whenever the stated scale separation is uniform. At the central scale itself the leading term is still only known to be of the order allowed by the arithmetic error.

There is a discrete version of the remaining test. Every sufficiently late exception $t$ lies within $O_b(\delta/g(t))$ of an exceptional $t_*$ for which $e^{t_*}$ is one of

$$
p\ (p\equiv1\bmod12),\qquad
p^2\ (p\equiv5,11\bmod12),\qquad
bp\ \text{or}\ p/b\ (p\equiv7\bmod12).
$$

To prove the claim, use the strictly positive values at $t\pm v$ with $v=\exp(-\sqrt t)$ to enclose an interior nonpositive minimum. In the variable $y$, the actual prime-ideal sum is continuous and affine between finitely many neighbouring breakpoints. The leftmost minimizer has a strictly positive jump of slope, including when the minimum occupies an interval. For a norm $m$ of signed log weight $s_m$, its jumps at $y=m/b^2,m/b,m$ are $s_m b^2/m,-s_m(b^2+b)/m,s_m b/m$. A positive jump therefore involves a negative norm weight at its peak or a positive norm weight at one of its two ends. The splitting in the Eisenstein field gives exactly the displayed possibilities for $by$. Coincident breakpoints still require at least one positive summand in the slope jump. The small-gap alternative for two exceptions gives the stated distance since $|t_*-t|\le v$. This reduces the continuum test to primes and their indicated dilates and squares.

## Prime counts forced by a deep minimum

Let $M_j(w)$ denote the tent on the left of the explicit formula restricted to ordinary primes in class $j$ modulo 12, without a character. Suppose $t\to\infty$ with $w\to0$, $tw\to0$ and $F(t)/w\to0$. For either character replacing $-\cos(\gamma t)$ by 1 in its tent costs $O_b(F(t)/w)$ by $w^2k(w\gamma)\ll(1+\gamma^2)^{-1}$. Partial summation in the positive-ordinate count gives
$$
 2w\sum_{\gamma_\chi>0} k(w\gamma_\chi)
    = \log(1/w)+\log(q/(2\pi))
       +\pi^{-1}\int_0^\infty k(u)\log u\,du+O_q(w\log(2/w))
$$
for conductor $q$. Here $\int_0^\infty k(u)\,du=\pi$ and $k'(u)=O((1+u)^{-2})$ at infinity. Removing squares costs $O(t(w+e^{-t/2}))$ by counting their integer roots. For exponents at least three the unrestricted count gives $O(t^2e^{-t/6})$. Thus the half-difference for the two characters gives
$$
                       M_{11}(w)-M_5(w)=\tfrac12\log 3+o(1).
$$
The half-sum gives $M_1(w)-M_7(w)=\log(1/w)+C+o(1)$ with the same constant $C$ at every such width. This is a statement for a triangularly weighted interval. At a late tie the hypotheses hold for every fixed $w=\exp(-c\sqrt t)$, $c>0$, by the preceding bound for $B$.

In particular, for any fixed $\alpha>1$, a centre with $B(t)>0$ and $0<F(t)\le B(t)^\alpha$ forces class-11 prime centres at each smaller fixed depth $1<s<\alpha$. Choose $s<\sigma<\alpha$ and take $w=B(t)^\sigma$. On $|h|\le w$ the cusp and the phase triangle inequality give $F(t+h)\ll F(t)+w\log(e/w)=o(B(t)^s)$, and the derivative bound gives $B(t+h)=(1+o(1))B(t)$. Since each prime in the tent contributes at most $(1+o(1))t e^{-t/2}$, the positive excess puts at least $((\log3)/2-o(1))e^{t/2}/t$ class-11 primes there. Hence recurrence at *some* depth greater than one is equivalent on real centres and on class-11 prime centres. This implication proves no such recurrence.
