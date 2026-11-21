# A continuous strict lead at the critical Eisenstein width

Assume GRH for the primitive Dirichlet characters of discriminants $-4$ and $12$. Use the [race and exact cutoff](PROOF.md) and put $b=b_K$, $x=by$, $t=\log x$ and $z=\sqrt y$. Define the signed correction $B(t)$ by $A_b(y)/z=F(t)-B(t)$, where $F(t)=\sum_{\gamma>0}a_\gamma(1+\cos(\gamma t))$. Every ordinate carries its full multiplicity.

**Theorem.** The race is zero for $0<y\le7/b^2$ and positive for every real $7/b^2<y\le\exp(10^{1058})/b$. There are also strict-lead intervals of logarithmic length exceeding $2\cdot10^{1058}$ arbitrarily far out. At every real $\log 11\le t\le10^{1058}$ one has $F(t)^2>B(t)$, so no prime $q\equiv11\pmod{12}$ in the certified range satisfies $F(\log q)^2\le B(\log q)$. The endpoint $b$ in these statements is the exact root.

The first part of the proof counts prime ideals directly. Above it, a finite set of actual zero ordinates gives lower bounds while explicit estimates for primes in progressions bound the correction. The final step uses an odd integer combination of twelve ordinates. The sign beyond the union of the verified intervals remains open.

## From the first prime through half a million

The smallest retained ideal norm is 7, from the two split ideals over 7. The tent first becomes positive there when $x>7/b$. For $x\le500000$ we sieve rational primes through $2250000$. Each split $p\equiv1\pmod3$ contributes at $m=p$ with signed coefficient $-2\chi_{-4}(p)\log p$. Each inert $p>2$ contributes at $m=p^2$ with coefficient $-2\log p$. Ramified 3 and inert 2 are omitted. We only need $m\le2250000$ since $b<4.5$.

As a function of $x$, the tent for norm $m$ is linear between $m/b,m,bm$, with slope jumps $b/m,-(b+1)/m,1/m$ before multiplication by the signed coefficient. Sort the knots using floating midpoints as hints and certify **every** strict ordering using interval arithmetic across the full published enclosure of $b$. Starting with slope and value zero, integrate the slope to each successive knot. A second evaluation sums the two linear branches from prefix sums of the signed coefficients and their quotients by $m$. The first knot gives zero. Both evaluations give strictly positive values at every later knot and at the final endpoint. The 109,123 endpoints cover the entire interval by linearity. Also $e^{13}<500000$. This arithmetic part holds unconditionally at the enclosed width. [Published width enclosure](https://github.com/leecrossley/eisenstein-prime-window-transition/blob/c1e11263b1cf6e8de187742f246b32992455658f/evidence/check.txt)

## An explicit upper bound for the correction

Write $z=\sqrt y$, $U=9/2$, $z_0=e^{t/2}/\sqrt U$, $X=Ue^t$ and $H_k=0.26X^{1/k}+X^{1/(2k)}$. For all $t\ge13$ we have

$$
 B(t)\le \frac{20}{\sqrt{z_0}}+0.071+\frac{40}{z_0}
 +\frac7{z_0}\left(H_3+
       \left(\frac{\log X}{2\log7}-\frac32\right) H_5\right).                 \tag{1}
$$

Here the even prime powers form $`E=\int w\,d\psi_K^*`$ with $w(u)=W_b((u/z)^2)$ on $[z,bz]$. Their continuous main term is $D_2z$, where $D_2=2\sqrt b(\sqrt b-1)^2$. In the exact formula for $zB(t)$ the even powers enter as $D_2z-E$. The remaining terms are the negative of the signed odd powers of exponents at least three, the ramified correction at 3 of magnitude below 30, and the nonpositive trivial-zero correction. The bound for the ramified correction also follows by counting at most three powers of 3 in a window of ratio $b^2<27$. [Arithmetic identity and signs](CUTOFF-SCALES.md#the-arithmetic-correction)

The exact identity $\psi_K^*(u)=2\psi(u;3,1)-2\log2\lfloor\log u/\log4\rfloor$ accounts for the omitted prime 2. At most two powers of 4 occur in $[z,bz]$. Their effect is at most $4(b-1)\log2<10$. For $u\ge14$ the fixed-modulus estimates of Ramaré and Rumely give

$$
 |2\psi(u;3,1)-u|\le2\sqrt u+0.002238u .
$$

Use their Theorem 5.2.1 through $10^{10}$ and Table 1 above it. Here $z\ge z_0>14$. Partial summation against the two branches of $w$ gives

```math
 \frac{2}{\sqrt z}\int_z^{bz}\sqrt u\,|dw(u)|
 =\frac83(b+b^{5/4}-b^{1/4}-\sqrt b)\lt 20 .
```

The coefficient is increasing for $1\le b\le U$. Also $z^{-1}\int u|dw|\le2b(b-1)$, with $0.002238\cdot2U(U-1)<0.071$. This gives the first two terms of (1) and the omitted-prime allowance. [Ramaré and Rumely, Theorem 5.2.1 and Table 1](https://ramare-olivier.github.io/Maths/rumely.pdf)

A negative odd-power summand is possible only for split primes $p\equiv7\pmod{12}$. Both ideals then have norm $p$. The same paper gives $\theta(v;12,7)\le0.26v+\sqrt v$ for $v\ge0$, using Theorem 5.2.1 for $v\le10^{10}$ and the entry $0.002781$ in Table 1 above that point. Here $\theta\le\psi$, so the small-range upper bound for $\psi$ at modulus 12 applies to $\theta$ as well. Thus the loss at odd exponent $k\ge3$ is at most $2(b-1)H_k$. Since $p\ge7$, the number of possible odd $k\ge5$ is at most $(\log X)/(2\log7)-3/2$ in the stated range. Combine the even, odd and ramified estimates using $z\ge z_0$ to obtain (1). The right-hand side decreases for $t\ge13$. For its terms involving the exponent count this follows from $\log X-3\log7>10/3$. The rigorous upper bounds at $t=13,14,19,32$ are respectively $2.76$, $2.18$, $0.74$ and $0.115$.

## Uniform lower bounds from 39 zeros

Take the 39 disjoint sign-changing brackets below height 43 for the two twisted characters, counted within each character. Each bracket was certified using Hardy functions and independently using a finite Euler transform. One zero per bracket gives a lower bound for $F(t)$ because every omitted summand is nonnegative under the two GRHs. An ordinate shared by the two functions would have both contributions. Each selected zero contributes

```math
  \frac{2\sqrt b\,(b+1-2\sqrt b\cos(\gamma\log b))}{1/4+\gamma^2}
             (1+\cos(\gamma t)).
```

The following bounds hold at **every real point** of the intervals.

| Range of $t$ | Strict lower bound on $F(t)$ |
| --- | ---: |
| $[2,13]$ | 1 |
| $[13,14]$ | 2.8 |
| $[14,19]$ | 2.2 |
| $[19,32]$ | 1 |
| $[32,10^6]$ | 0.35 |

Two independent phase bounds certify the table. Both start with dyadic cells and keep all endpoints. For each zero and cell the first bounds the cosine over the whole phase interval. It rounds $\gamma/(2\pi)$ at denominator $2^{42}$ and encloses the midpoint phase in one of 256 bins, enlarged by the maximum change within the cell and the frequency rounding error. The positivity of each unused term permits early termination on a cell. If the sum of lower bounds falls short, bisect and cover both halves. This certificate took 4,460,208 cells with minimum width $1/256$.

The second uses left endpoints, denominator $2^{38}$, and the distance $d$ in cycles to $1/2+\mathbb Z$. It rounds a lower bound on that distance down to $j/1024$ after subtracting a whole cell's phase variation and the accumulated frequency error. The phase weight is $2\sin^2(\pi d)$, increasing on $0\le d\le1/2$. A rational degree-seven Taylor lower bound for $\sin(\pi j/1024)$ uses $3.14159<\pi<3.14160$. This check took 8,954,956 cells with minimum width $1/1024$. In both checks every phase modulus divides $2^{64}$, so reducing the machine integer product preserves its exact residue. The positive weights are rounded down. The zero brackets and the stated enclosure of $b$ are included throughout. [Zero brackets and independent evaluation](verify_range.py) · [Two real-interval verifiers](range_cells.py)

On $[\log11,13]$ the arithmetic race is positive and $F>1$. The identity $A_b(y)/\sqrt y=F-B$ then gives $F^2>B$. On $[13,10^6]$ the table and (1) give both $F>B$ and $F^2>B$, using $0.35^2>0.115$ in the longest interval.

## A strict lead over a finite continuum of scales

For every real $10^6\le t\le10^{100}$, the estimate is

$$
A_b(y)>10^{-8}\frac{\sqrt y}{t^2}.
$$

Choose zeros $\lambda\in(5,7)$ for $\chi_4$ and $\mu\in(3,4)$ for $\chi_{12}$ in the two sign-changing intervals of width $10^{-220}$ recorded in the verifier. Put $\alpha=\mu/\lambda$. Its enclosing rational interval $[l,u]$ gives

$$
|q\alpha-p|>\frac1{400q}\qquad (1\le q\le3\cdot10^{100},\ p\in\mathbb Z).
$$

There are two integer certificates. In each dyadic denominator block $L\le q<2L$ the first finds a reduced $r/d$, with $d>2L-1$, $2d\le400L$, and $2(2L-1)d\max(|r/d-l|,|r/d-u|)<1$. The nonzero integer $qr-pd$ gives the claimed lower bound. The second finds enclosing Farey neighbors $a/b',c/d'$ with $b'c-ad'=1$ and $b'+d'>2L-1$. Any strict intermediate reduced fraction has denominator at least $b'+d'$. The check $400L^2\min(l-a/b',c/d'-u)>1$ then suffices. These tests cover all 334 blocks, including every odd choice of $p,q$.

The zero brackets are verified with Arb's Hardy functions and independently through the alternating progressions making up each Dirichlet series. For $s=1/2+iv$, expand $1/(1+e^{-hw})$ in powers of $(1-e^{-hw})/2$ in the gamma integral for $\sum_j(-1)^j(hj+a)^{-s}$. After $M$ terms the absolute remainder is at most $2^{-M}\sqrt\pi/(a^{1/2}|\Gamma(s)|)$. In the finite sum the coefficient of $(hj+a)^{-s}$ is $(-1)^j2^{-M}\sum_{k=j+1}^M\binom{M}{k}$. Conductor 4 uses $h=2,a=1$. Conductor 12 uses the difference between $h=6,a=1$ and $h=6,a=5$. The computation with $M=840$ and the real completion gives both endpoint signs independently of the Hardy routine. The same alternating method for $\eta(s)=(1-2^{1-s})\zeta(s)$ verifies the zeta bracket used for the correction in the companion proof.

Let $d_\lambda,d_\mu$ be the distances of $\lambda t,\mu t$ to the nearest odd multiples $\pi q,\pi p$. Here $q\le3t$ and $0<\alpha<1$, so $\pi|q\alpha-p|\le d_\mu+\alpha d_\lambda$ gives $\max(d_\lambda,d_\mu)>\pi/(6\cdot400t)$. The two pair weights are greater than $0.10$ and $0.32$, respectively. The inequality $1+\cos v\ge 2d(v)^2/\pi^2$ therefore gives $F(t)>1/(180\cdot400^2t^2)$ over the whole interval.

It remains to bound the actual arithmetic correction with explicit constants. Write $\psi_K^*(u)$ for the untwisted sum over retained prime ideal powers, each weighted by $\log N\mathfrak p$. Splitting at rational primes gives the exact identity

$$
\psi_K^*(u)=2\psi(u;3,1)-2\log2\left\lfloor\frac{\log u}{2\log2}\right\rfloor .
$$

An inert prime contributes at its even rational exponents and a split prime at every exponent. The last term removes the inert prime 2. Use Corollary 6.17 of Bennett, Martin, O'Bryant and Rechnitzer with modulus $Q=3^{11}$ and exponent 8. It bounds the error for each reduced class by $u/(160\log^8 u)$ when $\log u\ge0.24\sqrt Q\log^3 Q$. The class $1\bmod3$ consists of exactly $3^{10}$ of those classes. On $\sqrt y\le u\le b\sqrt y$ and $t\ge10^6$, the lower endpoint exceeds the required threshold in logarithmic scale. The omitted powers of 2 cost at most $\log u<u/(\log u)^8$. Hence $|\psi_K^*(u)-u|<740u/(\log u)^8$. [Bennett et al., Corollary 6.17](https://arxiv.org/pdf/1802.00085#page=78)

In $E(y)$ the weight $W_b((u/\sqrt y)^2)$ has variation $2(b-1)<8$ and zero endpoints. Partial summation, $u<5\sqrt y$ and $\log u\ge t/3$ give $|E(y)-D_2\sqrt y|/\sqrt y<2\cdot10^8/t^8$. Put $X=b^2y<25y$. There are at most $2X^{1/3}$ admissible ideals per odd exponent $k\ge3$, at most $\log X/\log2$ such exponents and weight at most $4\log X$. The omitted ramified sum at 3 costs less than 30, and the trivial-zero terms in $A$ are nonnegative. The odd and ramified losses after normalization are bounded by $2100t^2e^{-t/6}<t^{-8}$. Combining these inequalities proves the stated strict margin. The same bounds give $F(t)^2>B(t)$ throughout this interval, since $t^4>(2\cdot10^8+1)(180\cdot400^2)^2$ for $t\ge10^6$.

## Twelve ordinates give a continuous range and recurring intervals

Choose one zero ordinate $\gamma_i$ in each of the twelve disjoint intervals in the verifier, six from each primitive function. The listed integer vector $m$ has odd coefficient sum. Put $\Omega=\left|\sum_i m_i\gamma_i\right|$ and $S=\sum_i m_i^2/a_{\gamma_i}$, where $a_\gamma$ is its positive coefficient in $F(t)=\sum_{\gamma>0}a_\gamma(1+\cos(\gamma t))$. Direct enclosures give

$$
  1.84875907\cdot10^{-1058}<\Omega<1.84875908\cdot10^{-1058},
  \qquad 2S<10^{195}.
$$

Indeed all selected heights are below 22 and $b>4$, so the coefficient formula gives $a_{\gamma_i}>4/(22^2+1/4)>1/125$. All summands of $F$ are nonnegative and multiplicity only increases the coefficient. Telescoping the products of the twelve unit phases and of their reference values $-1$, including negative integer powers, gives

```math
 |1+e^{it\Omega}|\le\sum_i |m_i|\,|1+e^{it\gamma_i}|
 \le \sqrt{2S F(t)}.                                                   \tag{2}
```

Thus $F(t)>10^{-195}$ whenever $|t\Omega-2\pi k|\le2\pi/3$ for an integer $k$. The upper bound $B(t)\le(2\cdot10^8+1)t^{-8}$ for $t\ge10^6$ is smaller than $10^{-390}$ for $t\ge10^{100}$. Both $F>B$ and $F^2>B$ follow on all these intervals after that point. The interval for $k=0$ reaches beyond $t=10^{1058}$. Joining to the earlier certificate gives $A_b(y)>0$ throughout $7/b^2<y\le\exp(10^{1058})/b$ and $F_q^2>B_q$ at every class-11 prime $q\le\exp(10^{1058})$. For every $k\ge1$ the interval in (2) with the stated angular cut has length $4\pi/(3\Omega)>2\cdot10^{1058}$.

The twelve ordinates each have an enclosure of radius $10^{-1180}$ about a candidate obtained by Newton iteration. Two changes of sign, one from the Hardy function and one from the completed 4,176-term Euler transform, certify existence. The verifier tests disjointness, parity, the integer norm and the enclosing interval for the combination. Finding the integer vector by lattice reduction does not enter its verification. [Integer vector and checks](odd_ordinates.py)

## Comparison and replay

The [original exceptional-set publication](https://doi.org/10.5281/zenodo.24410852) proves finite logarithmic measure for possible failures and a sufficient condition for eventual dominance in terms of a zero ratio. It leaves room for isolated ties. This extension certifies each real point in the displayed initial range and in the stated recurring intervals. The contribution is the range and its reproducible arithmetic certificate for this observable. Explicit prime-counting bounds, finite zero enclosures and integer-relation methods have prior uses. Bailleul, Hayani and Untrau study generalized Skewes numbers for other races with an effective independence hypothesis. [Bailleul, Hayani and Untrau](https://arxiv.org/abs/2603.20093)

Use Python 3.11 or newer where the pinned wheels are available. From this directory run

```sh
python3 -m pip install -r range-requirements.txt
python3 -B verify_range.py > range-replay.txt
diff -u evidence/critical-range.txt range-replay.txt
```

The interval and integer calculations certify the finite inequalities. The use of the explicit formula and the prime-counting theorems is a written proof. [Verifier](verify_range.py) · [Recorded output](evidence/critical-range.txt)
