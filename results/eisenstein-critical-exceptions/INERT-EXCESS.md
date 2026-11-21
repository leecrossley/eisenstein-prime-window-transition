# The 11-over-5 excess forced by a cutoff exception

Assume the two GRHs for $\chi_4=\chi_{-4}$ and $\chi_{12}$, put $b=b_K$, $x=by$ and $t=\log x$. The cutoff formula gives $A_b(y)/\sqrt y=F(t)-B(t)$ and $B(t)=O_b(e^{-\eta\sqrt t})$ for some $\eta>0$. For ordinary primes put

$$
\Theta(X)=\sum_{p\le X,\ p\equiv11\ (12)}\log p-
          \sum_{p\le X,\ p\equiv5\ (12)}\log p,\quad
D(s,v)=e^{-s/2}\big(\Theta(e^{s+v})-\Theta(e^{s-v})\big),\qquad d=\tfrac12\log3.
$$

On any sequence of arbitrarily late exceptional blocks the positive fourth moment of this excess has order at least the forced width, with the explicit lower bound below. This calculation concerns rational primes near $x$. Each of these two inert residue classes enters the ideal race at its squared norms. [Cutoff identity](PROOF.md) · [Bounds for the correction](CUTOFF-SCALES.md)

## The forced change in the inert race

Use $C(s)=e^{-s/2}\Theta(e^s)$ and $Q_\chi(s)=e^{-s/2}\psi(e^s,\chi)$. As $s\to\infty$,

$$
C(s)=\tfrac12(Q_{12}(s)-Q_4(s))+O\big((1+s)^2 e^{-s/6}\big).
$$

Indeed every good square is $1\bmod12$, all higher odd powers have total log-weight $O(X^{1/3}\log^2(2X))$ through $X$, and the signed contribution of powers of 3 to $`\psi(\,\cdot\,,\chi_4)`$ is bounded by $\log3$. Both characters vanish at 2.

At a tie or loss the cutoff formula gives $F(t)\ll e^{-\eta\sqrt t}$ for a fixed $\eta>0$. Take $V=e^{-\eta\sqrt t/4}$ and $H=V^{-2}$. Write

$$
G_\chi(r)=\lim_{L\to\infty}\sum_{|\gamma|\le L}
                 \frac{e^{i\gamma r}}{1/2+i\gamma}.
$$

The symmetric sum is also defined in local mean square. On $|r|\le 3V$ one has $Q_\chi(t+r)=G_\chi(r)+o(1)$ simultaneously for both characters outside a set of length $o(V)$. For $|\gamma|\le H$ the total error in replacing $-e^{i\gamma t}$ by $1$ in the sharp formula is $O_b(\sqrt{H\log H}\sqrt{F(t)})=o(1)$. For each of the tails above $H$, at $t+r$ and at $r$, the integral of its square on any unit interval is $O(\log^2 H/H)$. The set where any tail exceeds $V^{1/8}$ thus has length $O(V^{7/4}\log^2(1/V))$. These bounds include multiplicities. [Sharp formula and local mean-square proof](#the-two-sharp-character-sums) · [Kisilevsky and Rubinstein, equation (2.27)](https://www.impan.pl/shop/en/publication/transaction/download/product/91016)

For $r\downarrow0$ one has $G_\chi(\pm r)=\pm\tfrac12\log(1/r)+g_{\chi,\pm}+o(1)$. With parity $a$, constant Laurent coefficient $b_\chi$ of $L'/L$ at zero, and $K_\chi=\sum_{\gamma>0}(1/4+\gamma^2)^{-1}$, the sharp formula at $1<e^r<2$ gives

$$
g_{\chi,+}=-b_\chi+(2a-1)\tfrac12\log2,\qquad
g_{\chi,-}=2K_\chi-g_{\chi,+}.
$$

The two logarithmic terms of the same sign cancel in $C$. Define $c_\pm=(g_{12,\pm}-g_{4,\pm})/2$. The conductor computation gives $c_+-c_-=d$. [Evaluation of the conductor difference](#the-two-sharp-character-sums)

Fix $0<\epsilon<1$. For $v/V\to1$ and all but $o(V)$ of the centres $s$ with $|s-t|\le(1-\epsilon)V$, the two offsets $s-t\pm v$ avoid the discarded set. They have opposite signs and absolute values between $\epsilon V/2$ and $3V$. Therefore

$$
D(s,v)=e^{v/2}C(s+v)-e^{-v/2}C(s-v)=d+o(1).
$$

At these same endpoints both $Q_\chi(s-v)$ equal $-\tfrac12\log(1/V)+O_\epsilon(1)$ and both $Q_\chi(s+v)$ equal $+\tfrac12\log(1/V)+O_\epsilon(1)$. This also holds with the width prescribed separately at each centre, $v=e^{-\eta\sqrt{s}/4}$. The two endpoint maps $s\mapsto s-t\pm v(s)$ have derivatives $1+o(1)$, so the preimages of the discarded sets still have length $o(V)$.

Most of these nearby centres themselves give strict leads. Fix a positive zero ordinate $\lambda$ of either factor. Its term in $F(t)$ puts $\lambda t$ within $O(V^2)$ of an odd multiple of $\pi$. If $V^{3/2}\le |s-t|\le (1-\epsilon)V$, the distance for $\lambda s$ is $\gg_\lambda |s-t|$. Hence $F(s)\gg_b |s-t|^2\ge V^3$ (with the chosen $\lambda$ fixed). The arithmetic error in $A_b(e^s/b)/\sqrt{e^s/b}$ is $O(V^4)$. This proves strict positivity there. This conclusion about neighbours is conditional on the existence of the exceptional centre.

## A sufficient fourth-moment bound at the required width

For integers $n\to\infty$ put $v_n=e^{-\eta\sqrt n/4}$ and $D_+=\max(D,0)$. An unbounded sequence of exceptions in the blocks $[n,n+1)$ would force

```math
\limsup_{n\to\infty}\frac{1}{v_n}
   \int_{n-1}^{n+2}D_+(s,v_n)^4\,ds
   \ \ge\ 2d^4=\frac{(\log3)^4}{8}.
```

Indeed $v_n/V\to1$ on each such block. The interval about an exceptional centre in the preceding calculation has length $2(1-\epsilon)V$ and lies inside the integration range. Let $\epsilon$ decrease to zero after taking the limit. A strict upper bound below this constant, in particular an $o(v_n)$ integral, would prove an eventual lead using the inert race alone.

The direct GRH estimate from unit-interval zero counts gives $O(v_n\log^4(1/v_n))$ for the integral. To see the loss, the coefficient of an ordinate in the sharp increment for each character has modulus $|2\sinh((1/2+i\gamma)v)/(1/2+i\gamma)|\ll\min(v,(1+|\gamma|)^{-1})$. The total absolute weight in the unit bin $j$ is bounded by $a_j\ll\log(2+|j|)\min(v,(1+|j|)^{-1})$. Square a finite zero sum and apply the local mean-square estimate. The bin weights of the square are bounded by two adjacent copies of the discrete convolution $`a*a`$. Young's inequality gives an integral $`\ll\|a*a\|_2^2\le\|a\|_{4/3}^4\ll v\log^4(1/v)`$. Truncation then passes to the limit in local fourth mean by the same bound on tails. The exponentially small prime-power and trivial-zero errors are absorbed at $v=v_n$. The usual prime-race densities do not control this local fourth moment. Montgomery and Soundararajan study moments of ordinary primes with additional hypotheses and different window ranges. [Dirichlet zero counts](https://arxiv.org/abs/2005.02989) [Races modulo 12](https://arxiv.org/abs/math/9910184) [Montgomery and Soundararajan](https://arxiv.org/abs/math/0409258)

## The two sharp character sums

Set $T=1/V$ and $Q_\chi(u)=e^{-u/2}\psi(e^u,\chi)$, where $\psi(X,\chi)=\sum_{m\le X}\Lambda(m)\chi(m)$.

Write $\rho=1/2+i\gamma$ and count signed ordinates with multiplicity within each factor. Put $Q_\chi(u)=e^{-u/2}\psi(e^u,\chi)$. The sharp explicit formula, for $u\ge1$ away from prime-power endpoints, gives

$$
Q_\chi(u)=-\lim_{H'\to\infty}\sum_{|\gamma|\le H'}\frac{e^{i\gamma u}}{\rho}
            +O_\chi((1+u)e^{-u/2}).
$$

The error includes the residue at zero and the trivial zeros. The countably many endpoints do not affect any measure below. [Kisilevsky and Rubinstein, equation (2.27)](https://www.impan.pl/shop/en/publication/transaction/download/product/91016)

For a finite set of frequencies with coefficients $c_\gamma$, on any interval $J$ of length at most one,

```math
\int_J\left|\sum_\gamma c_\gamma e^{i\gamma u}\right|^2du
 \ll\sum_{j\in\mathbb Z}
       \left(\sum_{j\le\gamma\lt j+1}|c_\gamma|\right)^2.
```

Majorize the indicator of $J$ by a constant times a Gaussian centered at its midpoint. After expanding the square, the Fourier transform bounds each pair of unit bins by $O((1+|j-k|)^{-2})$. The inequality follows by $2ab\le a^2+b^2$ and summation. Each unit bin contains $O_\chi(\log(2+|j|))$ zeros, so the integral of the squared tail with $|\gamma|>H$ and coefficients $1/\rho$ is $O_\chi(\log^2 H/H)$ uniformly in $J$. The bound first applies to finite tails. It gives convergence in local mean square and agrees almost everywhere with the symmetric explicit formula. [Bennett, Martin, O'Bryant and Rechnitzer, zero counting](https://arxiv.org/abs/2005.02989)

Take $H=T^2$. On our sequence $F(t)\ll T^{-4}$. Cauchy–Schwarz and the positive coefficients give

$$
\sum_{|\gamma|\le H}\frac{|1+e^{i\gamma t}|}{|\rho|}
  \ll_b \sqrt{H\log H}\sqrt{F(t)}
  \ll_b \frac{\sqrt{\log T}}{T}.
$$

For each choice of character and sign the squared tail of $Q_\chi(t\pm v)$ has mean $O(T\log^2 H/H)$ on $1/T\le v\le2/T$. Excluding the points where one of these four tails exceeds $T^{-1/8}$ discards a fraction $O(T^{-3/4}\log^2 T)$. On the remaining set,

$$
Q_\chi(t\pm v)=G_{\chi,H}(\pm v)+o(1),\qquad
G_{\chi,H}(v)=\sum_{|\gamma|\le H}\frac{e^{i\gamma v}}{\rho}.
$$

Pairing conjugate zeros gives $G_{\chi,H}(v)+G_{\chi,H}(-v)=O_\chi(1)$ by absolute convergence of $\sum_{\gamma>0}(1/4+\gamma^2)^{-1}$. The difference is

$$
G_{\chi,H}(v)-G_{\chi,H}(-v)
=4\sum_{0<\gamma\le H}\frac{\gamma\sin(v\gamma)}{1/4+\gamma^2}
=4\sum_{0<\gamma\le H}\frac{\sin(v\gamma)}{\gamma}+o(1).
$$

The replacement error tends to zero by dominated convergence with a summable $O_\chi(\gamma^{-3})$ weight. All the following estimates are uniform over $1/T\le v\le2/T$. For conductor $q$, the positive-ordinate count of this real character is

$$
N_\chi(s)=\frac{s}{2\pi}\log\frac{qs}{2\pi e}+O_\chi(\log(2+s)).
$$

Integration by parts with $f(s)=\sin(vs)/s$ gives

```math
4\sum_{0\lt \gamma\le H}\frac{\sin(v\gamma)}{\gamma}
=\frac{2}{\pi}\int_0^\infty\frac{\sin(vs)}s\log\frac{qs}{2\pi}\,ds+o(1)
=\log(1/v)+\log\frac q{2\pi}-\gamma_{\rm E}+o(1).
```

Indeed $|f'(s)|\le 2v/s$ for $s\ge1$, and $|f'(s)|\ll v^3s$ below 1. The counting error contributes $O_\chi(v\log^2 H+\log H/H)$. One integration by parts bounds the tail of the main integral by $O_\chi(\log H/(Hv))$. The sine integral and its logarithmic moment are $\pi/2$ and $-\pi\gamma_{\rm E}/2$, from the value and derivative at zero of $\Gamma(s)\sin(\pi s/2)$. This proves the two estimates for $Q_\chi(t\pm v)$. Since $v\log T=o(1)$, replacing their denominators $\sqrt{z_\pm}$ by $\sqrt x$ changes their difference by $o(1)$.

There is an independent check on the sign and the order-one constant. Write $a=0,1$ for even and odd parity, $b_\chi$ for the constant Laurent coefficient of $L'/L$ at zero and $\Xi_\chi(s)=(q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi)$. Set $K_\chi=\Xi_\chi'(1)/\Xi_\chi(1)$. The symmetric Hadamard product about $s=1/2$ gives $K_\chi=\sum_{\gamma>0}(1/4+\gamma^2)^{-1}$. For the full symmetric zero sum $G_\chi(v)$, the sharp formula at $1<e^v<2$ gives

$$
G_\chi(v)=e^{-v/2}\left[-b_\chi-(1-a)v+
              \sum_{k\ge1,\ k\equiv a\bmod2}\frac{e^{-kv}}k\right].
$$

The series is $-\tfrac12\log(1-e^{-2v})$ for $a=0$ and $\tfrac12\log((1+e^{-v})/(1-e^{-v}))$ for $a=1$. Also $G_\chi(v)+G_\chi(-v)\to2K_\chi$ by absolute convergence of the paired cosine sum. Thus the jump constant after subtracting $\log(1/v)$ is $-2b_\chi+(2a-1)\log2-2K_\chi$. Using $K_\chi=-\Xi_\chi'(0)/\Xi_\chi(0)$ and the constant terms of the digamma function at $0$ and $1/2$ gives $\log(q/(2\pi))-\gamma_{\rm E}$ for both parities.
