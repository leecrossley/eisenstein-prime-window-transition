"""Replay the arithmetic and zero certificates for the extended critical range."""

from fractions import Fraction
from math import comb, gcd

from flint import acb, arb, ctx, dirichlet_char

from odd_ordinates import check_odd_combination
from range_cells import check_finite_range


DEN = 10**220
ORDINATES = {
    4: int(
        "60209489046975966549025115216120858688640339630061961583"
        "47297132892491764334911573374239654643989555092749906275"
        "73804740091006346272136803172581067967739936481097067745"
        "92805751108209362584516329331797258380435810917338228"
    ),
    12: int(
        "38046276330508650971443175400383478577372481559510229426"
        "12924854357022928107579077488250073503386532669389356605"
        "71051856214114071417993796046413765154648620594148269022"
        "34120368311348276172106858352036233506954864924999635"
    ),
}
Q_MAX = 3 * 10**100
SEPARATION = 400


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def euler_sum(s, step, offsets, length):
    """Sum the finite Euler transform of signed alternating progressions."""
    denominator = 2**length
    tail = denominator - 1
    total = acb(0)
    for j in range(length):
        coefficient = arb(tail if j % 2 == 0 else -tail) / denominator
        for offset, sign in offsets:
            total += sign * coefficient * (-s * arb(step*j + offset).log()).exp()
        tail -= comb(length, j + 1)
    require(tail == 0, "Euler weights")
    error = len(offsets) * arb.pi().sqrt() / (denominator * abs(s.gamma()))
    return total, error


def check_ordinates():
    for conductor, label, parity, step, offsets in (
        (4, 3, 1, 2, [(1, 1)]),
        (12, 11, 0, 6, [(1, 1), (5, -1)]),
    ):
        char = dirichlet_char(conductor, label)
        require(char.is_real() and char.is_primitive() and char.parity() == parity,
                "character identity")
        for i, sign in ((0, 1), (1, -1)):
            t = arb(ORDINATES[conductor] + i) / DEN
            require(sign * char.hardy_z(t).real > 0, "Hardy function sign")
            s = acb(arb(1)/2, t)
            series, error = euler_sum(s, step, offsets, 840)
            w = (s + parity)/2
            factor = (w * (arb(conductor)/arb.pi()).log()).exp() * w.gamma()
            require(sign * (factor*series).real > abs(factor)*error,
                    "Euler transform sign")
        print(f"Conductor {conductor}: both methods certify a sign change in the 220-decimal bracket.")

    for t, sign in ((14, -1), (15, 1)):
        s = acb(arb(1)/2, t)
        factor = (-s*arb.pi().log()/2).exp() * (s/2).gamma()
        require(sign * (factor*s.zeta()).real > 0, "completed zeta sign")
        eta, error = euler_sum(s, 1, [(1, 1)], 128)
        factor /= 1 - ((1-s)*arb(2).log()).exp()
        require(sign * (factor*eta).real > abs(factor)*error, "eta sign")
    print("Completed zeta changes sign between heights 14 and 15 by both methods.")


def approximants(value):
    numerator, denominator = value.numerator, value.denominator
    p0, p1, d0, d1 = 0, 1, 1, 0
    while denominator:
        a, rem = divmod(numerator, denominator)
        p, d = a*p1+p0, a*d1+d0
        yield p, d
        numerator, denominator = denominator, rem
        p0, p1, d0, d1 = p1, p, d1, d


def farey_neighbors(value, cap):
    """Find adjacent fractions of order cap around an exact rational."""
    n, m = value.numerator, value.denominator
    a, b, c, d = 0, 1, 1, 1
    while b+d <= cap:
        below, above = n*b - m*a, m*c - n*d
        require(below != above, "midpoint found at a small denominator")
        if below > above:
            jump = min((cap-b)//d, (below-1)//above)
            a, b = a+jump*c, b+jump*d
        else:
            jump = min((cap-d)//b, (above-1)//below)
            c, d = c+jump*a, d+jump*b
    require(b*c-a*d == 1 and b+d > cap, "Farey determinant")
    return Fraction(a,b), Fraction(c,d)


def check_denominators():
    l, m = ORDINATES[4], ORDINATES[12]
    lo, hi = Fraction(m, l+1), Fraction(m+1, l)
    mid = (lo+hi)/2
    witnesses = []
    for p, d in approximants(mid):
        require(gcd(p,d) == 1, "witness reduced")
        error = max(abs(Fraction(p,d)-lo), abs(Fraction(p,d)-hi))
        witnesses.append((d, error))
        if d > 1000*Q_MAX:
            break
    for k in range(Q_MAX.bit_length()):
        low = 2**k
        high = 2*low-1
        require(any(d > high and 2*high*d*e < 1 and 2*d <= SEPARATION*low
                    for d, e in witnesses), "missing determinant witness")
        left, right = farey_neighbors(mid, high)
        require(SEPARATION * low**2 * min(lo-left, right-hi) > 1,
                "Farey separation")
    print(f"Both integer checks give |q alpha-p| > 1/(400q) in {Q_MAX.bit_length()} dyadic blocks through q = 3 * 10^100.")


def check_constants():
    t0 = 10**6
    b = arb("4.49334142447806").union(arb("4.49334142447807"))
    r = b.sqrt()
    for t, a in ((7, "0.10"), (4, "0.32")):
        require(2*r*(r-1)**2/(arb(t)**2+arb(1)/4) > arb(a), "pair weight")
    q = 3**11
    cutoff = (arb(24)/100) * arb(q).sqrt() * arb(q).log()**3
    require(cutoff < (t0-arb(5).log())/2, "progression range")
    require(q >= 10**5 and Fraction(2*3**10,160) + 1 < 740, "lifted progression error")
    require(8*740*5*3**8 < 2*10**8, "partial summation")
    require((arb(t0)-2)/2 > 499000 and 9*arb(499000).log() < 499000,
            "omitted powers of two")
    require(arb(2100).log()+10*arb(t0).log() < arb(t0)/6, "odd and ramified powers")
    require(Fraction(1,180*SEPARATION**2) - Fraction(2*10**8+1,t0**6)
            > Fraction(1,10**8), "finite sign")
    require(t0**4 > (2*10**8+1)*(180*SEPARATION**2)**2, "continuum exclusion for F squared")
    require(b > arb("1.45")**4 and b < arb("1.46")**4 and b-arb("1.46") > 3,
            "Mellin numerator bound")
    require(Fraction(45,100)*3/(2*8**2) > Fraction(1,100), "Mellin residue bound")
    print("The finite-range margin exceeds 10^-8/t^2; the absolute correction residue exceeds 1/100.")


def low_zero_brackets():
    """Enclose at least one zero in each bracket by two sign evaluations."""
    roots = []
    for conductor, label, step, offsets in (
        (4, 3, 2, [(1, 1)]),
        (12, 11, 6, [(1, 1), (5, -1)]),
    ):
        char = dirichlet_char(conductor, label)
        previous = char.hardy_z(0).real
        character_roots = []
        for index in range(1, 4*43+1):
            right = arb(index)/4
            current = char.hardy_z(right).real
            require(current > 0 or current < 0, "decided Hardy sign")
            if previous*current < 0:
                left = arb(index-1)/4
                for _ in range(202):
                    middle = (left+right)/2
                    sign = char.hardy_z(middle).real
                    require(sign > 0 or sign < 0, "decided bisection")
                    if previous*sign > 0:
                        left = middle
                    else:
                        right = middle
                margin = 2*(right-left)
                left -= margin
                right += margin
                signs = []
                for endpoint in (left, right):
                    s = acb(arb(1)/2, endpoint)
                    value, error = euler_sum(s, step, offsets, 416)
                    z = (s+char.parity())/2
                    factor = (z*(arb(conductor)/arb.pi()).log()).exp()*z.gamma()
                    completed = (factor*value).real
                    require(abs(completed) > abs(factor)*error, "Euler-transform sign")
                    signs.append(completed)
                require(signs[0]*signs[1] < 0, "independent change of sign")
                enclosure = left.union(right)
                require(not any(enclosure.overlaps(old) for old in character_roots),
                        "disjoint brackets within each character")
                character_roots.append(enclosure)
            previous = current
        roots.extend(character_roots)
    require(len(roots) == 39, "selected zero count")
    print("Hardy signs and independent Euler sums certify 39 zero brackets below height 43.")
    return roots


if __name__ == "__main__":
    with ctx.workprec(1000):
        check_ordinates()
        check_denominators()
        check_constants()
    with ctx.workprec(272):
        roots = low_zero_brackets()
    with ctx.workprec(160):
        check_finite_range(roots)
        check_odd_combination(euler_sum)
