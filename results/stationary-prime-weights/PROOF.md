# Prime weights at stationary minima of the Eisenstein race

Assume the two GRHs for the primitive characters of discriminants $-4$ and $12$. Let $b=b_K$ be the exact critical width and use $t=\log(by)$, $z=\sqrt y$, $A_b(y)/z=F(t)-B(t)$. For an ordinary rational prime $q$ let $F_q=F(\log q)$, $B_q=B(\log q)$, $\mu_q=(\log q)/q$ and $u_+=\max(u,0)$. A strict lead has $F>B$. The estimates below bound the error in replacing $B_q^+$ by an explicit finite-prime value on entire intervals. Its main term can be positive. [Race and spectral expansion](../eisenstein-critical-exceptions/PROOF.md)

## Estimates for one interval

Put $g(t)=t^{3/5}/(\log t)^{1/5}$ and $C_b=\sqrt b(b+1)$. The companion cutoff proof establishes $|B(t)|+|B'(t\pm)|\ll_b e^{-\kappa g(t)}$ and $F(t)\gg_b t^2 e^{-t/2}$ for some $\kappa>0$. It also proves $F_-(h)=C_b|h|\log(1/|h|)+O_b(|h|)$ as $h\to0$, strict positivity of $F_-(h)$ on compact subsets of $(0,\infty)$, and $F_-(h)\gg_b h^2e^{-h/2}$ for large $h$. Here $F_-(h)=\sum a_\gamma(1-\cos(\gamma h))$ with the same weights as $F$. [Bounds and cusp](../eisenstein-critical-exceptions/CUTOFF-SCALES.md)

Let $\tau$ minimize $F$ on a log interval of diameter at most one, and write $a=F(\tau)$. The phase triangle inequalities give $|\sqrt{F(\tau+h)}-\sqrt{F_-(h)}|\le\sqrt a$. Combining $F\ge a$ with these inequalities yields $F(\tau+h)\asymp_b a+|h|\log(e/|h|)$ on the interval. If $k\le\log(1/F(t))<k+1$ with $k$ large, every such point is within $O_b(e^{-k}/k)$ of $\tau$. At an occupied strip $k\le\tau/2-2\log\tau+O_b(1)$ by the floor. The enclosing physical interval has length $\gg_b\tau e^{\tau/2}$ on choosing this scale, so Brun–Titchmarsh gives total $\mu_q/F_q$ at most $O_b(1/k)$. The same upper bound holds for the weight $dt/F(t)$. Two centres of depth $F\le e^{-V}$ have $F_-$ at their difference at most $4e^{-V}$. Consequently at most $O_b(1+T/V)$ unit-separated such centres can occur in $[T,2T]$ for large $V$. [Montgomery and Vaughan, Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf#page=3)

We will use the uniform formula
```math
 B(\tau+h)=B(\tau)+B'(\tau+)h+
 O_b\big(\tau h^2+\tau\log(2\tau)e^{-\tau/2}|h|\big) .
```
Indeed between knots $B''=O_b(1)$ by the arithmetic formula below. For exponent $j\ge2$ the three scales contribute $O_b(1+|h|e^{\tau/j}/j)$ possible integer roots each, and a jump costs $O_b((\tau/j)e^{-\tau/2})$. Summing up to $j=O_b(\tau)$ and integrating gives the formula, with either side at a corner. At a point with $k=\log(1/F(t))\gg_b g(\tau)$ its remainder divided by $F(t)^2$ is $O_b(\tau/k^2+\tau\log(2\tau)e^{-\tau/2}/(kF(t)))=o(1)$. This uses $g(\tau)/\sqrt\tau\to\infty$ and the spectral floor.

## The positive correction at a stationary minimum

Write $y=e^t/b$, $z=\sqrt y$, $D=2\sqrt b(\sqrt b-1)^2$ and $H_j=H_b(-j)$. Assume the two original GRHs. The following calculation recovers $B(t)_+$ with a summable error after division by $F(t)^{21/20}$ at stationary minima. Its main term is a positive deficit in a product of two finite arithmetic sums. The sum of those main terms at the actual deep minima remains undetermined.

Let $c_m$ be the following real coefficients, with all other coefficients zero.

| Rational prime power $m$ | $c_m$ |
| --- | --- |
| $3^k$, $k\ge1$ | $(-1)^k\log3$ |
| $\ell^k$, $\ell\equiv1\pmod3$ prime, $k\ge2$ | $2\chi_{-4}(\ell)^k\log\ell$ |
| $\ell^k$, $\ell>3$ prime, $\ell\equiv2\pmod3$, even $k\ge4$ | $2\log\ell$ |

These are the coefficients of the sum of the two primitive von Mangoldt terms and the signed ideal-prime race. At split primes the first powers cancel. At inert primes the square cancels the first ideal-prime contribution. The conductor-4 local factor supplies the displayed powers of 3. Let $\mathcal L=(y,by)$ and $\mathcal R=(by,b^2y)$ when $y$ is between successive breakpoints of these coefficients. Define constants throughout each such interval by

$$
 P=H_0+b\sum_{m\in\mathcal L}c_m-\sum_{m\in\mathcal R}c_m,\qquad
 Q=b^2\sum_{m\in\mathcal R}\frac{c_m}{m}
       -b\sum_{m\in\mathcal L}\frac{c_m}{m}.                           \tag{1}
$$

At a knot use the constants of either adjoining interval by continuity, with the corresponding one-sided derivative. Put $V(y)=\sum_{j\ge1}H_j y^{-j}$ and $T(y)=\sum_{j\ge1}(2j+1)H_j y^{-j}$. Here $H_0=(b-1)\log b$, $H_j=(1-b^{-j})(b-b^{-j})/(j(j+1))>0$ and $V(y),T(y)\ll_b y^{-1}$ for $y\ge2$. The exact formula and its derivative are

$$
 B(t)=D-\frac{P}{z}-Qz-\frac{V(y)}{z},\qquad
 2B'(t\pm)=\frac{P}{z}-Qz+\frac{T(y)}{z}.                             \tag{2}
$$

Indeed the two affine branches of $W_b(m/y)$ give (1), and $H_0+V(y)$ is precisely the trivial-zero term of the two twisted functions. In particular the sign of $V$ is fixed. As $B,B'(t\pm)\to0$, both $P/z$ and $Qz$ tend uniformly to $D/2$. They are positive on all sufficiently late intervals. [Explicit formula](../eisenstein-critical-exceptions/PROOF.md) · [Variation of the correction](#estimates-for-one-interval)

Set $M_B=D-2\sqrt{PQ}$. Everywhere on a sufficiently late interval,

$$
 M_B-B(t)=\frac{(\sqrt P-\sqrt{Qy})^2}{z}+\frac{V(y)}{z}>0,\qquad
 M_B-B(t)\ll_b |B'(t\pm)|^2+z^{-3}.                                  \tag{3}
$$

For the upper bound write the square term as $(P/z-Qz)^2/(P/z+Qz+2\sqrt{PQ})$ and use (2). Thus $PQ\ge D^2/4$ excludes every positive correction on the interval. At $B'(\tau)=0$, $a=F(\tau)$ and $p=21/20$, (3) gives

$$
 0\le \frac{(M_B)_+-B(\tau)_+}{a^p}
 \ll_b \frac{z^{-3}}{a^p}
 \ll_b \tau^{-21/10}\exp(-39\tau/40).                                 \tag{4}
$$

The last step uses $a\gg_b\tau^2/z$. The bound sums over any unit-separated sequence and also when either one-sided derivative is zero. The positive upper bound $(M_B)_+$ depends only on the prime powers in (1). The estimate in (4) controls the error in this upper bound.

There is a further arithmetic restriction at an interior minimum of $F$ with an exactly vanishing one-sided derivative of $B$. Write $Y=P/Q$ using the corresponding side of the correction interval. Equation (2) gives $Qy=P+T(y)$. The left side minus the right side is strictly increasing for $y>1$, so at most one stationary point lies in the open interval. Since $Qy\asymp_b z$ and $T(y)=3H_1/y+O_b(y^{-2})$,

$$
       y>Y,\qquad y=Y+\frac{3H_1}{P}+O_b(y^{-3/2}).                   \tag{5}
$$

For example, $1/(Qy)=1/P+O_b(y^{-2})$ at the stationary point. An interior sufficiently deep minimum of $F$ must lie at an upward prime-power knot: between knots $F''=(F-D)/4+O_b(z^{-1})<0$. Hence $b^i y=m$ at such a minimum for $`i\in\{0,1,2\}`$ and some contributing prime power. In particular $b^iY$ lies below $m$ by $3b^iH_1/P+O_b(y^{-3/2})$. This is a test at the individual arithmetic interval. Its required frequency of occurrence at large $y$ is unknown. [Signs and residue classes of upward knots](#candidate-knots-and-a-one-sided-sign-test)

One can replace the denominator $a$ in (4) by prime sums as well. For $F$ use the coefficients $c_m^F=(\chi_{-4}(m)+\chi_{12}(m))\Lambda(m)$ in (1). Its exact formulas are (2) with $F$ in place of $B$. At a sufficiently deep interior minimum $\tau$, the left and right derivatives satisfy $F'(\tau-)\le0\le F'(\tau+)$. Their jump costs $O_b(\tau/z)$, since at most one prime power per scale supplies a jump and its coefficient is $O(\tau)$. Thus the two affine constants on each side have $P_F/z,Q_Fz\to D/2$ along deep minima. Interpolate the left and right pairs $(P_F,Q_F)$ linearly with parameter $\theta\in[0,1]$ and set

$$
             M_F=D-2\sqrt{\max_{0\le\theta\le1}P_F(\theta)Q_F(\theta)}.
$$

The two branches have identical values of $P_F/z+Q_Fz$ at the knot. Maximizing the product minimizes $|P_F/z-Q_Fz|$, and some interpolated difference equals $-T(y)/z$ by the derivative signs. Therefore $0\le M_F-a\ll_b z^{-3}$. The same interpolation gives (4) for $(M_B)_+$ when the two one-sided derivatives of $B$ straddle zero, including a corner maximum. It gives the same bound if just one side is stationary.

In particular at separated joint minima of $F$ and stationary points of $B$ the total absolute error in replacing $`B(\tau)_+/a^p`$ by $`(M_B)_+/M_F^p`$ is finite for $1<p\le2$. The pointwise error is $O_b(z^{-3}a^{-p}+z^{-3}a^{-p-1})$, by $M_F\ge a$, boundedness of $B$ and the mean value theorem. The second term is $O_{b,p}(\tau^{-2p-2}z^{p-2})$, still summable at $p=2$. For $p=21/20$ it decays at least as fast as $e^{-19\tau/40}$. The upward knots and both products are specified by finite rational-prime sums and $b$.

As a finite check on the sign and size of (3), the arithmetic verifier brackets an actual smooth local maximum of $B$ at $12503.33699<y<12503.33700$. There $0.11519<B<0.11522$, $12503.31985<P/Q<12503.31988$, and $1.18\cdot10^{-6}<M_B-B<1.20\cdot10^{-6}$. It checks the prime-power coefficients against the two primitive characters and ideal norms, brackets the unique root of (2) and evaluates both the original tent sum and (3) by interval arithmetic. Direct summation over the ideal primes on the entire bracket gives $3.217<F<3.220$ at the stationary point and $12.218<F'<12.221$ there. This maximum of $B$ occurs with $F$ strictly increasing. [Arithmetic verifier](verify.py) · [Replay output](evidence/check.txt)

### Candidate knots and a one-sided sign test

All sufficiently late deep interior minima of $F$ with one one-sided derivative of $B$ exactly zero in $X<by\le2X$ are covered by $O_b(\sqrt X/\log X)$ candidate knots constructible from (1). To see the count, each nonzero correction coefficient gives at most three breakpoints. Split squares in the relevant fixed-ratio range cost $O_b(\sqrt X/\log X)$ by the elementary upper bound for primes. All exponents at least three cost $O_b(X^{1/3}\log X)$, and powers of 3 cost $O_b(\log X)$. Include all the boundaries. For each open interval take $Y=P/Q$ and, for each $i=0,1,2$, round $b^iY$ to the nearest integer $m$. Equation (5) forces the actual $b^iy$ at an upward knot to be that integer, since $|b^i(y-Y)|\ll_b X^{-1/2}<1/2$ eventually. Test $y=m/b^i$ in the interval. The count concerns potential testing locations, not primality evaluations or the runtime for forming the sums.

In an open correction interval an upward knot of $F$ must come from an actual prime-ideal norm. A peak can come from $by=\ell$ with $\ell\equiv1\pmod{12}$ or from $by=\ell^2$ for an inert $\ell>3$. An edge can come from $y=\ell$ or $b^2y=\ell$ with $\ell\equiv7\pmod{12}$. The signs follow by taking the jumps of $-c_m^F W_b(m/y)/z$. Every other nonzero twisted coefficient at a higher power or a power of 3 already supplied a correction boundary. Coincident knots are covered by including every boundary or, in an open interval, at least one upward contribution.

At a candidate which is a true local minimum of $F$ and has $B'(\tau\pm)=0$ on a chosen side, let $J_B=PQ$ on that side, $J_F=\max_\theta P_F(\theta)Q_F(\theta)$, and $`\ell_F=P_F(\theta_*)/z-Q_F(\theta_*)z`$ at a maximizer. Then the sign of the race is exactly the sign of

$$
            4(J_B-J_F)+\frac{T(y)^2}{z^2}-\ell_F^2,\qquad
            0\le\frac{T(y)^2}{z^2}-\ell_F^2\ll_b y^{-3}.              \tag{6}
$$

Indeed both normalized sums have the same additive $D-V(y)/z$. Subtract their affine parts and multiply by their positive sum. For either pair the square of its affine part is four times its product plus the square of its difference. Equation (2) makes the difference for $B$ exactly $-T(y)/z$. The maximizing pair for $F$ has difference of at most that magnitude. In particular $J_B>J_F$ suffices for a strict lead at this point, and $4(J_F-J_B)>T(y)^2/z^2$ suffices for a reversal. The unresolved comparison in (6) involves prime powers from two distinct arithmetic sums.

## How much positive weight a stationary minimum supplies

Fix $1<p<2$, eventually taking $p=21/20$. Let $\tau$ be a minimum of $F$ on $[\tau-1/4,\tau+1/4]$, $a=F(\tau)$, $A=\log(1/a)$, $v=B(\tau)>0$ and $L=\log(1/v)$. Suppose that $B'(\tau+)=0$, or more generally $|B'(\tau+)|\ll_b \tau\log(2\tau)e^{-\tau/2}$. This also covers every local maximum of $B$ at a corner, since its two slopes straddle zero and the jump is $O_b(\tau e^{-\tau/2})$. Use a sequence of such minima with $\tau_{j+1}\ge2\tau_j$ and consider the class-11 weight in these disjoint intervals. The same assertions hold separately for every reduced class modulo 12. Write $W_\tau$ for the weight on $F_q^p\le B_q<F_q$ and set

$$
 C_b=\sqrt b(b+1),\qquad
 H_\tau=\left[\log\frac{p\min(A,L)}{L}\right]_+ .
$$

All sufficiently late participating minima have $A,L\gg_b g(\tau)$. Restrict throughout to deep minima with $A\gg_b g(\tau)$, and use the convention $H_\tau=0$ when $v=0$. There is a **full positive upper bound**

$$
                  W_\tau\ll_{b,p} H_\tau+\frac{\log(2\tau)}{g(\tau)}.  \tag{7}
$$

Moreover, when $\min(A,L)\le(5/12-\delta)\tau$ for any fixed $\delta>0$, the untruncated prime weight satisfies

$$
                  W_\tau=\frac{H_\tau}{2C_b}
                       +O_{b,p,\delta}\left(\frac{\log(2\tau)}{g(\tau)}\right).     \tag{8}
$$

The errors in both estimates are summable. Thus in the range of (8) the sum of the positive $H_\tau$ is necessary and sufficient. In the full range it is sufficient. If $v/a$ stays between two fixed positive constants and $a$ is comparable to $e^{-\tau/4}$, (8) gives $W_\tau\to\log(21/20)/(2C_b)$ for $p=21/20$. Even when $v/a\to0$, if $L/A\to s$ with $1<s<21/20$ in the range of (8), then $W_\tau\to\log((21/20)/s)/(2C_b)>0$. These are implications about any sequence with the specified sizes.

To prove the estimates, write $r=|t-\tau|$ and $\phi(r)=C_b r\log(1/r)$ for $r$ small. Outside the core where $F(t)\le C a$, one has $\phi(r)\asymp_b F(t)$ and $r\ll_b F(t)/\log(1/F(t))$. On the core the total prime weight is $O_b(1/A)$, by the interval sieve, the spectral floor and $F\ge a$. At an actual selected point $k=\log(1/F(t))\gg_{b,p}g(\tau)$. The Taylor bound for $B$ now gives $B(t)=v+o_b(F(t)^2)$ uniformly there. The same estimate holds on the proposed replacement intervals where $\phi$ is small, $F\asymp_b\phi$ and $k\gg_b g(\tau)$. The local minimum condition and the phase inequalities exclude all fixed positive $r$ from the support eventually. [Cusp, Taylor estimate, core and prime bounds](#estimates-for-one-interval)

On each side replace the support by

$$
           \max(16a,v)\le\phi(r)\le v^{1/p}
$$

and the denominator by $\phi(r)$. Away from the core, disagreement in support forces $\log(1/\phi)$ to be within $O_b(1)$ of $L/p$ or $L$. For example $F_q^p\le B_q$ and $\phi^p>v$ imply $v\asymp_b\phi^p$ since $B_q-v=o(F_q^2)$. The other endpoint follows from comparison with $F_q$. A fixed number of strips at either boundary costs $O_b(1/g(\tau))$. The relative error in the denominator is $O_b(1/k+\sqrt{a/\phi})$. Summing it against the $O_b(1/k)$ cost of each unit strip gives $O_b(1/g(\tau))$ across the whole cluster.

The integral of $dr/\phi(r)$ over one replacement interval is $H_\tau/C_b+O_b(\log(2\tau)/g(\tau))$. Indeed $\phi(r)=c e^{-u}$ gives $\log(1/r)=u+O_b(\log(2u))$ at its ends. Whenever an end matters one has $u\gg_b g(\tau)$ and $u\ll_{b,p}\tau$; if $L>pA+O_b(1)$ the interval is empty. Brun–Titchmarsh over complete doubling intervals gives (7), with an incomplete interval costing $O_b(1/g(\tau))$. The shortest relevant physical length before removing an endpoint interval is $\gg_b e^\tau a/A\gg_b \tau e^{\tau/2}$.

For (8) choose $\min(A,L)/\tau\le5/12-\delta<\lambda<5/12$. Every radius of the replacement interval satisfies $r\gg_b e^{-\lambda\tau}/\tau$. For radii in that interval the fixed-modulus prime number theorem on the appropriate side of $e^\tau$ gives cumulative mass $\sum_{q\equiv11\pmod {12}}(\log q)/q=r/4+O_{b,\lambda,M}(r\tau^{-M}+r^2)$ from the centre to radius $r$, for each fixed $M$. The physical length exceeds $e^{(7/12+\epsilon')\tau}$ for some fixed $\epsilon'>0$. Partial summation against $1/\phi(r)$ costs $O_{b,\lambda}(\tau^{-2})$ on taking $M$ sufficiently large; the endpoints and the weighted variation multiply the relative error by $O_b(1+\log\tau)$, and here $r\ll_b e^{-c_b g(\tau)}$. Both sides contribute the factor $1/(2C_b)$. Geometric separation makes $\sum_j\log(2\tau_j)/g(\tau_j)$ finite. This argument uses the fixed-modulus short-interval prime number theorem in its classical exponent range. [Thorner and Zaman, Theorem 1.1 and Remark 1.2](https://arxiv.org/pdf/2108.10878#page=2)

For exact stationary minima one can use only products in $H_\tau$: set $\widehat A=\log(1/M_F)$ and $`\widehat L=\log(1/(M_B)_+)`$, interpreting the latter as $`+\infty`$ when $`(M_B)_+=0`$. Use zero weight when $\widehat L=+\infty$. Equations (3)–(4) and the interpolation bound give a summable change in $H_\tau$. Indeed $\widehat A-A=O_b(z^{-3}/a)$. If $v<a^p/2$, then $`(M_B)_+\lt a^p`$ eventually and both weights vanish. Otherwise $`\widehat L-L=O_{b,p}(z^{-3}/a^p)`$, and the positive part, the clipping at $A=L$ and the logarithms of $A,L\gg_b g(\tau)$ preserve summability. The actual arithmetic comparison is now whether these positive clipped logarithms have finite sum. Sparsity and stationarity alone leave a fixed contribution in the example following (8).

## A summable error for the minimum of the actual race

Suppose the centres $\tau$ are unit-separated, $I_\tau=[\tau-1/4,\tau+1/4]$, and $a=F(\tau)=\min_{I_\tau}F$ is sufficiently small. Write $A=\log(1/a)$, $v=B(\tau)$ and $m_\tau=\min_{I_\tau}(F-B)$. Suppose $B'(\tau)=0$, one one-sided derivative vanishes, or the two slopes straddle zero. This includes a corner maximum. For every fixed $C>0$ and all large $T$,

$$
 \sum_{\tau\ge T}\frac{\displaystyle
       \sup_{|h|\le C a/A}|B(\tau+h)-v|}{a^2}\ll_{b,C}\frac1{T\log T},
 \qquad
 0\le\sum_{\tau\ge T}\frac{a-v-m_\tau}{a^2}\ll_b\frac1{T\log T}.     \tag{9}
$$

The same estimates allow $|B'(\tau+)|\le C_0\tau\log(2\tau)e^{-\tau/2}$ with a constant depending also on $C_0$. Taking the positive part is 1-Lipschitz. In particular, for the stationary cases use the products $M_B,M_F$ of (3)–(6), interpolating when the slopes straddle zero. Then

$$
 \sum_{\tau\ge T}\frac{\displaystyle
       \sup_{|h|\le C a/A}|B(\tau+h)_+-(M_B)_+|
       +\big|m_\tau-(M_F-M_B)\big|}{a^2}
       \ll_{b,C}\frac1{T\log T}.                                       \tag{10}
$$

The signed estimate also bounds the error for the maximum positive reversal $`(-m_\tau)_+`$. On intervals where the centre still leads but the race has a tie or reversal elsewhere, $`\sum_{\tau\ge T}(a-v)/a^2\ll_b 1/(T\log T)`$. On every interval with $M_F-M_B\ge\epsilon a^2$ for a fixed $\epsilon>0$, the whole interval has a strict lead once $\tau$ is sufficiently large. These statements leave open the possibility that $(M_B-M_F)_+$ itself is large, even at widely separated centres.

To locate the minimum, take $t_*=\tau+h$ attaining $m_\tau$. Since $F(\tau+h)-a\le B(\tau+h)-v$ and $B$ is uniformly Lipschitz with constant $o(1)$ on $I_\tau$, the phase bound $F(\tau+h)\gg_b a+|h|\log(e/|h|)$ gives $|h|\log(e/|h|)\ll_b a$. Hence $|h|\ll_b a/A$ and

$$
           0\le a-v-m_\tau\le B(\tau+h)-v.
$$

This argument allows $v$ of either sign. The stationarity assumption enters only in bounding the resulting variation.

For $0<\delta<5/24$ and a fixed $N>0$, if $e^{-(5/24-\delta)\tau}\le R\le1/4$, there is a uniform estimate

$$
 \sup_{|h|\le R}|B(\tau+h)-v-B'(\tau+)h|
                        \ll_{b,\delta,N} R^2\tau^{-N}.                 \tag{11}
$$

Here the signs of the jumps are essential. Between knots (2) gives $B''=(B-D)/4-z^{-1}\sum_{j\ge1}j(j+1)H_j y^{-j}=-D/4+O_b(e^{-c g(\tau)})$ on the interval. For each split prime $\ell\equiv1\pmod3$ its square contributes slope jumps at $u=2\log\ell-\log b,\ 2\log\ell,\ 2\log\ell+\log b$. The respective multipliers of $`2\sqrt b\,e^{-u/2}\log\ell`$ are $-1,\ b+1,\ -b$. All higher powers together have total absolute jump on $[\tau-R,\tau+R]$ bounded by $O_b(\tau\log(2\tau)e^{-\tau/2}+\tau R e^{-\tau/6})$. Indeed for exponent $k\ge3$ there are $O_b(1+Re^{\tau/k}/k)$ possible integer roots at any one scale, each costing $O_b((\tau/k)e^{-\tau/2})$. This includes powers of 3 on late intervals.

Replace the logarithmically weighted split primes by $d\ell/2$ separately at each of the three scales. On every prefix of either side of $[\tau-R,\tau+R]$ the error for the unweighted-in-$`u`$ sum of $\log\ell$ is $O_{b,\delta,N}(e^{\tau/2}R\tau^{-N})$. For a prefix of log length at least $R\tau^{-N-1}$ the physical length at $\ell\asymp_b e^{\tau/2}$ exceeds $\ell^{7/12+\delta'}$ for some $\delta'>0$. The fixed-modulus short-interval prime number theorem gives arbitrary log savings there. Shorter prefixes have both their prime mass and their expected mass bounded by those on a prefix of length $R\tau^{-N-1}$. Endpoints cost $O_b(\tau)$, within the displayed error. Partial summation introduces the exact factor $`2\sqrt b\,e^{-u/2}`$ at cost $O_{b,\delta,N}(R\tau^{-N})$ in the signed jump sum. Under $u=2\log\ell+s$ each mean jump density is constant in $`u`$. Their sum is

$$
       -\frac b2+\frac{\sqrt b(b+1)}2-\frac b2=\frac D4.
$$

This cancels the constant between knots. The integrated smooth error and the higher-power jumps are also $O_{b,\delta,N}(R\tau^{-N})$ on every prefix. The possible jump at $\tau$ costs $O_b(\tau e^{-\tau/2})$. Integrating the uniform bound for the difference of the slopes proves (11). [Thorner and Zaman, Theorem 1.1 and Remark 1.2](https://arxiv.org/pdf/2108.10878#page=2) · [Prime-power variation](#estimates-for-one-interval)

For (9), fix $R=C a/A$, reducing the upper bound allowed for $a$ if necessary. If $A\le\tau/6$, then $R\gg_C e^{-\tau/6}/\tau$ and (11) applies with a fixed margin. The possible linear term divided by $a^2$ is $\ll_{b,C}\tau\log(2\tau)e^{-\tau/2}/(aA)$, exponentially small here. With $N=3$ each normalized variation is $O_{b,C}(\tau^{-3})$.

If $A>\tau/6$, write $Y=R e^{\tau/2}$. The floor $a\gg_b \tau^2 e^{-\tau/2}$ gives $Y\gg_{b,C}\tau$ and $A\le\tau/2+O_b(1)$. Each of the three square-root intervals has length $\asymp_b Y$. Brun–Titchmarsh bounds the number of prime roots by $O_b(Y/\log Y)$ on the full interval, hence also bounds its subintervals. Each jump costs $O_b(\tau e^{-\tau/2})$. Include the smooth part, the higher powers estimated above and the possible linear term. After integration and division by $a^2$ the result is

$$
 O_{b,C}\left(\frac{1}{A^2}+\frac{\tau}{A^2\log Y}
           +\frac{\tau\log(2\tau)e^{-\tau/2}}{aA}\right)
        =O_{b,C}\big(1/(\tau\log\tau)\big).
$$

Only $O_b(1)$ of these deeper unit-separated centres can occur in $[U,2U]$. Indeed two such values give $F_-(|\tau_1-\tau_2|)\ll_b e^{-U/6}$, whereas $F_-$ has a positive minimum on bounded gaps of at least one and is $\gg_b h^2e^{-h/2}$ at large gaps $h$. Thus distinct centres of this depth are separated by $\gg_b U$. Dyadic summation gives $O_{b,C}(1/(T\log T))$ for the deeper centres. The shallower contribution is $O_{b,C}(1/T^2)$ by unit separation. The entire bound improves to $O_{b,C,\epsilon}(1/T^2)$ on $A\le(1/2-\epsilon)\tau$, since then $\log Y\gg_\epsilon\tau$ in the deeper range and its last term is exponentially small. Finally (3) and the interpolation bound replace $v,a$ by $M_B,M_F$ at cost $O_b(z^{-3}/a^2)\ll_b \tau^{-4}e^{-\tau/2}$ per centre. The triangle inequality gives (10) and the whole-interval sign test. [Interval sieve of Montgomery and Vaughan](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf#page=3) · [Spectral floor and spacing](#estimates-for-one-interval)

## The positive correction at every prime in the stationary intervals

The changing part of $B_q^+$ has summable *undivided* prime weight on the entire intervals, including outside the central region of (9). Take the stationary assumptions and products of (10). With $\mu_q=(\log q)/q$, $q$ ranging over all rational primes, define

```math
 {\cal D}_p(T)=
 \sum_{\tau\ge T}\ \sum_{\log q\in I_\tau}
    \frac{\mu_q}{F_q}\,
    \frac{|(B_q)_+-(M_B(\tau))_+|}{F_q^p}.
```

Then for every fixed $1<p<2$ and every $N>0$,

$$
 {\cal D}_p(T)\ll_{b,p,N}T^{-N},\qquad
 {\cal D}_2(T)\ll_b\frac{\log(2T)}{T^2}.                              \tag{12}
$$

In particular (12) applies with $p=21/20$ and to the strict-lead class-11 primes themselves. It proves that, after division by $F_q^p$, replacing their positive corrections by their own interval's finite-prime value has absolutely summable error against $(\log q)/(qF_q)$. The positive values $(M_B(\tau))_+$ in that sum are still uncontrolled.

First use $v=B(\tau)$ in place of $M_B(\tau)$. At primes where $F_q$ exceeds a fixed small constant, the error from $B_q-v$ is $\ll_b e^{-c g(\tau)}$, and $\sum_{\log q\in I_\tau}\mu_q=O_b(1)$. For the rest put $k=\lfloor\log(1/F_q)\rfloor$ and $R_k=C_b' e^{-k}/k$. The phase bound used in (9) puts all the primes of this strip within $R_k$ of $\tau$. Their total $\mu_q/F_q$ is $O_b(1/k)$ by the interval sieve. When the strip is occupied, $k\le\tau/2-2\log\tau+O_b(1)$ by the floor. Thus even at the last strip the length of the enclosing physical interval is $\gg_b \tau e^{\tau/2}$. The cutoff for small $F_q$ can be chosen so $R_k<1/4$ on all these strips.

For $k\le\tau/6$ the signed estimate (11) gives

$$
 \frac{|B_q-v|}{F_q^2}
 \ll_{b,M}\frac{\tau^{-M}}{k^2}
       +\frac{\tau\log(2\tau)e^{k-\tau/2}}{k}
$$

for any $M>0$. Summing against the strip weights costs $O_{b,M}(\tau^{-M})$ on this part. For $k>\tau/6$ put $U=\tau/2-k$. Now $U\ge2\log\tau-O_b(1)$, so $\log(R_ke^{\tau/2})=U-\log k+O_b(1)\gg_b U$. Apply the upper bound for the number of prime squares in the proof of (9) at radius $R_k$. It gives

$$
 \frac{|B_q-v|}{F_q^2}
 \ll_b \frac1{k^2}+\frac{\tau}{k^2 U}
            +\frac{\tau\log(2\tau)e^{-U}}{k}.
$$

Multiplication by the strip weight $O_b(1/k)$ and summation costs $O_b(\log(2\tau)/\tau^2)$. Indeed $k\asymp\tau$, the harmonic sum in $U$ is $O(\log\tau)$, and $\sum_U e^{-U}=O_b(\tau^{-2})$. An interval meeting this part has $A>\tau/6$ and, by the spacing proof for (9), only $O_b(1)$ of them occur per dyadic range. This proves the bound for $p=2$. For $p<2$ these deeper terms acquire the further factor $F_q^{2-p}\le e^{-(2-p)\tau/6}$. Unit separation and arbitrary $M$ on the shallower strips give the claimed tail for $p<2$. Finally $|M_B-v|\ll_b e^{-3\tau/2}$ in the stated stationary cases. Even at $p=2$, division by $F_q^p$ costs $O_b(e^\tau/\tau^4)$ and the whole interval has total $\mu_q/F_q=O_b(1+\log\tau)$. This replacement is summable with exponential tails. Taking positive parts decreases each difference.

Estimate (12) extends to $|B'(\tau+)|\le C_0\tau\log(2\tau)e^{-\tau/2}$ using $M_B$ from the right interval. Equation (3) costs an additional $O_{b,C_0}(\tau^2\log^2(2\tau)e^{-\tau})$ in replacing $v$ by $M_B$. This is exponentially small after division by $F_q^2$ in the shallow strips. In the deeper strips its total normalized prime weight is $O_{b,C_0}(\tau\log^2(2\tau)\sum_U e^{-2U})=O_{b,C_0}(\log^2(2\tau)/\tau^3)$ per interval. For $p<2$ the same extra exponential factor applies.

There is also an all-depth test for the original sharp inequalities using only these arithmetic values and the primes either side of $\tau$. Use the exact stationary cases and put $m=(M_B)_+$, $f=M_F$, $r_q=|\log q-\tau|$, and $\phi(r)=C_b r\log(1/r)$. Define a finite sum

```math
 P_{\tau,p}=
  \sum_{\substack{q\ {\rm prime},\ q\equiv11\pmod {12},\ 0\lt r_q\le e^{-4}\\[0pt]
         \max(16f,m)\le\phi(r_q)\le m^{1/p}} \frac{\mu_q}{\phi(r_q)} .
```

For $1<p<2$, with $W_\tau$ the actual undivided strict-lead sum on $I_\tau$,

$$
 \sum_{\tau\ge T}|W_\tau-P_{\tau,p}|\ll_{b,p}
 \begin{cases}
       1/g(T),&\tau_{j+1}\ge2\tau_j,\\
       T/g(T)^2,&\text{unit-separated centres}.
 \end{cases}                                                           \tag{13}
$$

Indeed $f=a+O_b(z^{-3})$ and $M_B=v+O_b(z^{-3})$. If either support is occupied then $A\gg_{b,p}g(\tau)$ and $m\gg_{b,p}a^p$, by the stationary Taylor estimate at the actual primes or by the lower radial cutoff on the new support. In particular $v>0$ eventually and $m/v\to1$ on such intervals. Their union lies at radii tending to zero, since $F_-(h)$ stays positive on every fixed compact subinterval of $(0,1/4]$. The core, the bounded number of endpoint strips, and the replacement of $1/F_q$ by $1/\phi(r_q)$ together cost $O_{b,p}(1/g(\tau))$ per occupied interval, as shown in the proof of (7). Passing there from $a,v$ to $f,m$ shifts the endpoints by $O_{b,p}(1)$ in $\log(1/\phi)$ and has the same bound. The only prime count needed is the upper sieve. On a dyadic range $[U,2U]$ phase spacing allows $O_b(U/g(U))$ occupied unit-separated centres and geometric separation allows $O(1)$. Summing proves (13). In particular the positive finite sums $P_{\tau,p}$ test convergence on the stationary intervals down to the full spectral floor. A summable bound for their main terms at the actual centres remains missing.
