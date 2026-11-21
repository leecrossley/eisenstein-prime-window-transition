# The undivided reciprocal prime sum

Assume GRH for the primitive Dirichlet characters of discriminants $-4$ and $12$. At the exact cutoff $b=b_K$, the normalized Eisenstein race is $F(t)-B(t)$ at $t=\log(by)$. For a prime $q$ write $F_q=F(\log q)$, $B_q=B(\log q)$, $\mu_q=(\log q)/q$, and define

```math
 W_j=\sum_{\substack{q\ {\rm prime},\ q\equiv j\ (12)\\ B_q\ge F_q^2}}\frac{\mu_q}{F_q},
 \qquad j\in\{1,5,7,11\}.
```

All statements about series start sufficiently late, where $F(t)>0$. The displayed inequality includes equality and implies $B_q>0$. The convergence of $W_{11}$ itself remains unresolved. The results below remove the divisor on a growing part of the selected set, prove convergence of the signed difference between the two inert classes, and give a necessary divergence test at an actual tie.

## Two parts of the positive sum converge with no divisor

Put $K_q=\log(1/F_q)$, $D_q=\log(B_q/F_q^2)$ for selected primes, and $g(t)=t^{3/5}/(\log t)^{1/5}$. For every fixed $\epsilon>0$ each of the following sets has finite total $\sum\mu_q/F_q$, even on summing over all prime classes.

1. The selected primes with
   $0\le D_q\le K_q^{1/3}/(\log(2+K_q))^{4/3+\epsilon}$.
2. All primes with
   $F_q\le q^{-1/2}\exp\bigl((\log q)/(\log\log q)^{1+\epsilon}\bigr)$.
   This assertion allows either sign of the correction.

In the first assertion the upper bound can in particular be replaced by $K_q^\theta$ for any $0\le\theta<1/3$. More generally, for $T$ large, $V\gg1$, $v,w\ge0$,

```math
\sum_{\substack{T\le\log q\le2T,\ V\le K_q\lt 2V\\ v\le D_q\le v+w}}\frac{\mu_q}{F_q}
 \ll_b \frac{T(1+w)}{V^2}. \tag{1}
```

Here $D_q$ is restricted to selected primes. The constant is independent of $v,w,T,V$. The same proof applies to $-C\le D_q\le C$ when $B_q>0$, for any fixed $C$.

Use the integer block $[n,n+1]$. Choose a minimizer $\tau$ of $F$ there and write $a=F(\tau)$, $b_0=B(\tau)$, $d=B'(\tau+)$, $h=t-\tau$, $x=e^\tau$, and $k=\log(1/F(t))$. Write $C_b=\sqrt b(b+1)$. The estimates used below are

$$
\begin{split}
 a&\gg_b n^2e^{-n/2},&
 |B(t)|+|B'(t\pm)|&\ll_b e^{-\kappa g(n)},\\
 F(t)&\asymp_b a+|h|\log(e/|h|),&
 F_-(h)&=C_b|h|\log(1/|h|)+O_b(|h|)\quad(h\to0).
\end{split} \tag{2}
$$

At $h=0$ the continuous value of the product is zero. The two triangle inequalities give $|\sqrt{F(t)}-\sqrt{F_-(h)}|\le\sqrt a$. Two centres of $F\le e^{-V}$ give $F_-(t_2-t_1)\le4e^{-V}$. The local cusp, positivity at bounded nonzero arguments and $F_-(u)\gg_b u^2e^{-u/2}$ for large $u$ imply that only $O_b(1+T/V)$ unit blocks meeting $[T,2T]$ can contain such a centre. On occupied bands $V\ll_b T$ by the floor. [Spectral and arithmetic estimates](../eisenstein-critical-exceptions/CUTOFF-SCALES.md) · [Unit-block estimates](PROOF.md#estimates-for-one-interval)

The following approximation holds on the whole block, including the corners.

```math
 B(\tau+h)=b_0+dh+
 O_b\!\left(nh^2+n\log(2n)e^{-n/2}|h|\right). \tag{3}
```

Between corners $B''=O_b(1)$. The first-power coefficients of every good rational prime cancel in $B$. A remaining corner comes from a prime power $l^m$, $2\le m\ll_b n$, at one of the three fixed scales $l^m,bl^m,l^m/b$. The ramified powers of $3$ are included for late blocks. On a log interval of length $r\le1$ near $\tau$ there are $O_b(1+rx^{1/m}/m)$ possible integers $l$ for each exponent and scale. Each jump of $B'$ costs $O_b((\log l)/\sqrt x)=O_b(n/(m\sqrt x))$. Summing gives total jump size $O_b(n\log(2n)/\sqrt x+nr)$, since $x^{1/m}\le\sqrt x$ and $\sum_{m\ge2}m^{-2}<\infty$. Integrate this bound on slope variation from $\tau$, including a possible jump at $\tau$ when $h<0$. This proves (3). [Prime-power coefficients and jumps](PROOF.md)

At all points with $F(t)\ll e^{-c g(n)}$ for a fixed $c>0$, (2) gives $|h|\ll_b F(t)/k$ and $k\gg_c g(n)$. Consequently the error in (3), divided by $F(t)^2$, is

```math
 O_b\!\left(\frac n{k^2}+\frac{n\log(2n)e^{-n/2}}{k F(t)}\right)=o(1). \tag{4}
```

Here $g(n)/\sqrt n\to\infty$ and the pointwise floor controls the second term, including at the smallest allowed spectral values. This proves that the linear term is accurate on the scale of the square that defines the selection.

Within one occupied block and one strip $k_0\le k<k_0+1$, the total $\mu_q/F_q$ is $O_b(1/k_0)$. In fact the centres lie in a log interval of diameter $O_b(e^{-k_0}/k_0)$ by the phase inequality. An enclosing physical interval of the corresponding length has logarithm comparable to $n$ by the floor. Brun–Titchmarsh bounds $\sum\mu_q$ there by $O_b(e^{-k_0}/k_0)$. The same strip bound holds with $dt/F(t)$ in place of the prime weights. [Interval sieve estimate of Montgomery and Vaughan](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf#page=3)

It remains to count how many strips can occur in (1) per block. The core $F(t)\le C a$ occupies $O_b(1)$ strips for any fixed $C$. Away from this core choose $C$ sufficiently large. Then $|h|\asymp_b e^{-k}/k$ by (2). At selected points (4) gives $b_0+dh=(1+o(1))B(t)>0$, uniformly. If $|dh|\le|b_0|/2$ then $B(t)\asymp |b_0|$ and $D=2k+\log|b_0|+O_b(1)$. If $|dh|\ge2|b_0|$ and $dh\ne0$ then $B(t)\asymp |dh|$ and $D=k-\log k+\log|d|+O_b(1)$. On $k\gg1$ the latter function of $k$ has derivative at least $1/2$. In the remaining case $|h|\asymp |b_0/d|$, which itself confines $k$ to $O_b(1)$ consecutive strips. A vanishing intercept or slope is covered by its dominating nonzero term. They cannot both vanish at a selected point for large $n$. Therefore each block costs $O_b((1+w)/V)$ in (1). Summing over $O_b(T/V)$ blocks proves the estimate.

Since $K_q\gg_b g(T)$ for every selected prime, summing the dyadic $V$ estimates for the first assertion gives a contribution on $[T,2T]$ of
$O_{b,\epsilon}(Tg(T)^{-5/3}(\log T)^{-4/3-\epsilon})=O_{b,\epsilon}((\log T)^{-1-\epsilon})$ for large $T$. Sum over dyadic $T$. For the second assertion, $K_q\ge n/2-O_\epsilon(n/(\log n)^{1+\epsilon})$ on the block of a qualifying prime, whereas the floor gives $K_q\le n/2-2\log n+O_b(1)$. There are $O_b(1)$ blocks on each dyadic range because $K_q\gg T$, and the unit-strip bound costs $O_{b,\epsilon}((\log T)^{-1-\epsilon})$ per block. This proves the second assertion.

There is a version on the full selected set with a smaller pointwise divisor. Write $L_q=\log(1/B_q)$. For every $\beta>2/3$,

```math
\sum_{B_q\ge F_q^2}\frac{\mu_q}
 {F_q\,\min\{L_q,1+D_q\}^{\beta}}\lt \infty. \tag{1a}
```

Indeed on a band $V\le K_q<2V$ one has $D_q\le 4V$. Sum (1) with $w=1$, $v=0,1,\ldots,\lfloor4V\rfloor$ and weights $(1+v)^{-\beta}$. For $2/3<\beta<1$ the result is $O_{b,\beta}(T/V^{1+\beta})$. Dyadic summation in $V\gg g(T)$ and then in $T$ converges, and larger $\beta$ follow by monotonicity beyond finitely many initial terms. For the $L_q^\beta$ bound, (2) gives $L_q\gg_b g(T)$ and selection gives $K_q\ge L_q/2$. An occupied band $V\le K_q<2V$ costs $O_b(T/V)$ by summing the unit-strip bound in its $O_b(T/V)$ blocks. Summing over dyadic $V\gg_b g(T)$ gives $O_b(T/g(T)^{1+\beta})$ after division, summable over dyadic $T$ for $\beta>2/3$. Adding the bounds controls the reciprocal of the smaller divisor.

## Two intervals at each spectral minimum

The following construction describes the entire remaining sum up to an absolutely summable error. Retain the notation of (2) and put

```math
 \phi(r)=C_b r\log(1/r),\qquad 0\lt r\le e^{-4}.
```

On each side $`\xi\in\{-1,1\}`$ of $\tau$ keep the radii in

```math
 I_{n,\xi}=\{r:\ 0\lt r\le e^{-4},\ n\le\tau+\xi r\le n+1,\space{}
     \phi(r)\ge\max(16a,n^5e^{-n/2}),\space{}
     \phi(r)^2\le b_0+\xi dr\}. \tag{5}
```

Each nonempty set is an interval, allowing a single point. Indeed $\phi$ is increasing and $`(\phi^2)^{\prime\prime}=2C_b^2\bigl[(\log(1/r))^2-3\log(1/r)+1\bigr]\gt 0`$ throughout the displayed range. Use half-open blocks for the prime sums, assigning a boundary prime to one block.

For each class $j$, replace the original prime weight in its block by $\mu_q/\phi(r)$ on these intervals and zero elsewhere. The sum over all primes of the absolute errors of this replacement is finite. The same assertion holds with Lebesgue measure in place of $\mu_q$. The following details prove summability, including at the boundaries of (5).

* A block meeting either selection has $a\ll_b e^{-c g(n)}$ for some fixed $c>0$. For (5) this uses $|b_0|+|d|\ll_b e^{-\kappa g(n)}$ and $\phi(r)\ge16a$. Thus only $O_b(T/g(T))$ blocks can occur on $[T,2T]$. All selected centres have $|h|< e^{-4}$ eventually.
* The core $\phi(|h|)<16a$ of the original selection has $F(t)\asymp_b a$ and costs $O_b(1/g(n))$ per occupied block, including $h=0$. The discarded floor range $\phi(r)< n^5 e^{-n/2}$ outside the core implies $F(t)\ll_b n^5 e^{-n/2}$ and costs a finite total by the second assertion above. The same counts apply to the real integral.
* Elsewhere $F(t)\asymp_b\phi(r)$ by (2) and $\phi(r)\ge16a$. If the two threshold conditions differ, (4) and the phase inequalities give $B(t)\asymp_b F(t)^2$. For example, on an original member outside (5) one has $F(t)^2\le B(t)=b_0+dh+o(F(t)^2)\le\phi(r)^2+o(F(t)^2)$. In the other direction $B(t)\ge\phi(r)^2-o(F(t)^2)$ and $B(t)<F(t)^2$. Thus the two weights disagree in support only on a fixed-width strip treated by (1), also allowing a fixed negative $D$. These errors are absolutely summable.
* On common support set $k=\log(1/\phi(r))$ and $A=\log(1/a)$. The relative error of replacing $F(t)$ by $\phi(r)$ is $O_b(1/k+\sqrt{a/\phi(r)})$ from (2) and the phase triangle inequalities. On $k_0\le k<k_0+1$ the model costs $O_b(1/k_0)$, by the length $O_b(e^{-k_0}/k_0)$ and the same interval sieve. Summing from $k_0\gg_b g(n)$ up to $A+O_b(1)$ bounds the block error by $O_b(1/g(n))$ because the two scalar sums are bounded by $\sum k_0^{-2}$ and $\sum e^{(k_0-A)/2}/k_0$. Finally $\sum_{\rm occupied}1/g(n)<\infty$ by the preceding block count and dyadic summation. All upper estimates still apply after restricting a block to an arbitrary subinterval.

## What the two GRHs cancel in the undivided sum

In the natural increasing order of the primes the signed series $W_{11}-W_5$, defined by subtracting the two finite partial sums before taking the limit, converges. More precisely, the supremum over partial subintervals of each block of the absolute difference between its two class contributions is summable in $n$. In particular the *positive* sum $W_{11}$ converges if and only if $W_5$ does. The same holds separately for $W_1-W_7$.

After the absolutely summable replacement it suffices to treat at most two intervals (5) per block. The characteristic function of class 11 minus that of class 5 on units is $(\chi_{12}-\chi_{-4})/2$. For class 1 minus class 7 use $(\chi_{12}+\chi_{-4})/2$. The two stipulated GRHs and the usual explicit formula give each sharp signed log-prime count over an arbitrary subinterval of $[e^n,e^{n+1}]$ the bound $O_b(e^{n/2}n^2)$. Removing prime powers costs at most this amount. Partial summation gives $O_b(e^{-n/2}n^2)$ for the corresponding sums of $\mu_q$. On either side of $\tau$ the amplitude $1/\phi(r)$ is monotone and bounded by $e^{n/2}/n^5$. A second partial summation therefore bounds the signed contribution on any subinterval of (5) by $O_b(n^{-3})$. This proves the signed assertion. The absolute value at each individual prime would sum the two positive series, whose convergence is precisely the unresolved issue. [Ernvall-Hytönen and Palojärvi on the fixed-character GRH error](https://arxiv.org/abs/2003.01925)

Quantitatively the signed tail for $\log q\ge T$ is $O_b(T/g(T)^2)$. On $[T,2T]$ the core, threshold comparison and weight replacement cost $O_b(T/g(T)^2)$, the discarded polynomial-width floor strip costs $O_b(\log T/T)$, and the signed interval estimates cost $O_b(T^{-2})$. The same bounds hold for partial blocks. Summing over dyadic $T$ proves the tail claim.

## What a real tie would force

A sequence of real ties or reversals tending to infinity implies $W_{11}=\infty$. Each event forces, on one side of its centre, a shell of class-11 primes of asymptotic weight $\log(9/8)/(4C_b)>0$. Thus convergence of the positive series would prove eventual strict positivity at all real scales.

Write $x=e^t$, $b_0=B(t)$, $L=\log(1/b_0)$. An exceptional centre satisfies $0<F(t)\le b_0$, so the floor gives $b_0\gg_b t^2/\sqrt x$. On a log interval of radius $r=c\sqrt{b_0}$, all one-sided slopes of $B$ differ by $O_b(r)$. Indeed its smooth second derivative is bounded. The three ranges for split prime squares have root length comparable to $r\sqrt x\gg_b x^{1/4}$ and Brun–Titchmarsh bounds the sum of their absolute slope jumps by $O_b(r)$. The remaining jumps cost $O_b(t\log(2t)/\sqrt x+rtx^{-1/6})$ by the root count in (3). Move right if $B'(t+)\ge0$ and left otherwise. Integration gives $B(t\pm h)\ge b_0/2$ on that side for $0\le h\le r$ when $c$ is sufficiently small.

For $u=2/3,3/4$ put $h_u=b_0^u/(C_b u L)$. On $h_{3/4}\le h\le h_{2/3}$ the phase inequalities and the cusp in (2) yield $F(t\pm h)\sim C_b h\log(1/h)$ uniformly since $F(t)\le b_0=o(b_0^{3/4})$. In particular $F(t\pm h)^2<b_0/2$. The shortest physical length $xh_{3/4}\gg_b x^{5/8}t^{1/2}$ exceeds $x^{7/12+\delta}$ for some $\delta>0$. The fixed-modulus prime number theorem gives cumulative class-11 weight $(1+o(1))h/4$ from the centre out to every such $h$, uniformly on either side. Partial summation against $1/(C_bh\log(1/h))$ gives $\log(9/8)/(4C_b)+o(1)$ per shell because $\log(1/h_u)\sim uL$. Take disjoint shells along a subsequence. The common positive weight could therefore diverge even though the signed difference converges. [Fixed-modulus short-interval prime number theorem](https://arxiv.org/pdf/2108.10878#page=2)
