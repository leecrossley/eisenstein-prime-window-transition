"""Sign crossings by finite Dirichlet series with a partial-summation error."""

from fractions import Fraction
from flint import acb, arb, ctx

ctx.prec = 144
LIMIT = 12000


def main():
    for q, parity, residues, endpoints in (
        (4, 1, {1: 1, 3: -1}, (5, 7)),
        (12, 0, {1: 1, 5: -1, 7: -1, 11: 1}, (3, 4)),
    ):
        # LIMIT is a full number of periods. Every partial tail block has sum in [-1,1].
        partial = 0
        for j in range(1, q+1):
            partial += residues.get(j % q, 0)
            if abs(partial) > 1:
                raise ArithmeticError("character sum")
        if LIMIT % q or partial:
            raise ArithmeticError("period")
        for t, sign in zip(endpoints, (1, -1)):
            s = acb(arb("0.5"), arb(t))
            series = acb(0)
            for n in range(1, LIMIT+1):
                value = residues.get(n % q, 0)
                if value:
                    series += value*(-s*arb(n).log()).exp()
            w = (s+parity)/2
            completion = (w*(arb(q)/arb.pi()).log()).exp()*w.gamma()
            error = abs(completion)*2*abs(s)/arb(LIMIT).sqrt()
            if not sign*(series*completion).real > error:
                raise ArithmeticError(("completed L-function sign", q, t))
        print(f"Conductor {q}: the completed Dirichlet series through {LIMIT}, with its entire tail bounded, confirms both endpoint signs.")
    # A rational lower bound for sqrt(b_K) suffices for both pair-weight bounds.
    r = Fraction(2117, 1000)
    if not r*r < Fraction(449, 100):
        raise ArithmeticError("lower sqrt bound")
    for t, floor in ((7, Fraction(1,10)), (4, Fraction(32,100))):
        if not 2*r*(r-1)**2 > floor*(Fraction(1,4)+t*t):
            raise ArithmeticError("pair coefficient")
    print("Rational bounds confirm both pair weights throughout the published cutoff bracket.")


if __name__ == "__main__":
    main()
