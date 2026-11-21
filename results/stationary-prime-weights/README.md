# Prime weights at stationary minima of the Eisenstein race

Fix the exact critical width $b=b_K$ and assume GRH for the two primitive Dirichlet characters of discriminants $-4$ and $12$. Write the normalized ideal-prime race as $A_b(y)/\sqrt y=F(t)-B(t)$, $t=\log(by)$. Here $F$ is the nonnegative sum over the twisted zeros and $B$ is the prime-power correction. For ordinary primes put $F_q=F(\log q)$, $B_q=B(\log q)$ and $\mu_q=(\log q)/q$. [Observable, sign and hypotheses](../eisenstein-critical-exceptions/README.md)

## What the positive prime weights measure

Take a unit-separated family of centres $\tau$ where $F$ has a sufficiently small minimum on $I_\tau=[\tau-1/4,\tau+1/4]$ and a one-sided derivative of $B$ vanishes or its two slopes straddle zero. Two finite prime-power sums $P,Q$ give the positive value $M_\tau=(2\sqrt b(\sqrt b-1)^2-2\sqrt{PQ})_+$. At a corner the proof specifies the interpolation. For $1<p<2$ and every $N>0$,

$$
\sum_{\tau\ge T}\sum_{\log q\in I_\tau}
\frac{\mu_q}{F_q}\frac{|(B_q)_+-M_\tau|}{F_q^p}
\ll_{b,p,N} T^{-N}.
$$

The bound at $p=2$ is $O_b(\log(2T)/T^2)$. It covers $p=21/20$ and every prime in the intervals. The proof also bounds the difference between the minimum of the actual race and the value predicted by the two arithmetic products. A certified positive maximum of $B$ occurs at $12503.33699<y<12503.33700$, where $F$ is increasing. The theorem leaves the sum of the positive $M_\tau$ at the actual deep minima open. [Proof and finite example](PROOF.md)

For $j=5,11$, let $W_j$ sum $\mu_q/F_q$ over $q\equiv j\pmod{12}$ satisfying $B_q\ge F_q^2$. The difference of the two partial sums converges in prime order. Each positive sum also converges with the additional divisor $(\log(1/B_q))^\beta$ for $\beta>2/3$. Two explicit subranges converge with the original weights. An arbitrarily late sequence of real ties or losses would force $W_{11}=\infty$, with a fixed positive contribution per disjoint shell. We do not know whether $W_{11}$ converges, even on the strict-lead band $F_q^{21/20}\le B_q<F_q$. [Statements, constants and proofs](PRIME-SUMS.md)

## Prior work and verification

The short-interval prime number theorem, the upper-bound sieve and the sharp character estimates are existing inputs. The contribution here is their application to the reciprocal weight at the actual cutoff minima, including a finite arithmetic expression with an absolutely summable error and the signed class-11/class-5 cancellation. The previous cutoff paper controlled the logarithmic measure of exceptional real scales. Planat studies logarithmically weighted prime phases at a different threshold, with independence and a local-limit hypothesis in the weighted local-time law. [Thorner and Zaman](https://arxiv.org/abs/2108.10878) · [Montgomery and Vaughan](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf) · [Earlier cutoff paper](https://doi.org/10.5281/zenodo.24410852) · [Planat](https://doi.org/10.3390/axioms15090660)

With Python 3.11 or newer in a virtual environment, run from this directory

```sh
python3 -m pip install -r requirements.txt
python3 -B verify.py > replay.txt
diff -u evidence/check.txt replay.txt
```

The interval-arithmetic verifier evaluates the maximum by the original prime-ideal sum and by the product formula. It checks the slope at that maximum and the independent signed densities of the three prime-square jumps. The asymptotic series and error bounds have written proofs. [Recorded output](evidence/check.txt) · [File checksums](SHA256SUMS)
