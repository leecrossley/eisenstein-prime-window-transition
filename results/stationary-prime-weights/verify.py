"""Check a positive stationary value of the Eisenstein correction using Arb."""

from math import isqrt

from flint import arb


def check_stationary_intercept():
    b = (arb(449334142447806) / 10**14).union(arb(449334142447807) / 10**14)
    left, right = arb("12503.33699"), arb("12503.33700")
    y = left.union(right)
    limit = 254000
    if not b**2 * y < limit:
        raise ArithmeticError("insufficient prime-power cutoff")
    chi4 = (0, 1, 0, -1)
    chi12 = (0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1)
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes(2)
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime*prime::prime] = bytes((limit-prime*prime)//prime+1)

    h0 = (b-1)*b.log()
    constant, slope = h0, arb(0)
    race, race_log_derivative = arb(0), arb(0)
    direct_terms = []
    for prime in range(2, limit + 1):
        if not sieve[prime]:
            continue
        norm = prime if prime % 3 == 1 else prime**2
        if prime > 3 and not (norm < y or b*b*y < norm):
            if y < norm < b*y:
                tent = b*(1-y/norm)
                tent_log_derivative = -b*y/norm
            elif b*y < norm < b*b*y:
                tent = b*b*y/norm-1
                tent_log_derivative = b*b*y/norm
            else:
                raise ArithmeticError("an ideal-prime knot meets the bracket")
            multiplicity = 2 if prime % 3 == 1 else 1
            weight = -multiplicity*chi4[norm % 4]*arb(norm).log()
            race += weight*tent
            race_log_derivative += weight*(tent_log_derivative-tent/2)
        m, exponent = prime, 1
        while m <= limit:
            raw = chi4[m % 4] + chi12[m % 12]
            if prime > 3 and m == norm:
                raw -= 2*chi4[m % 4]
            if prime == 3:
                projected = (-1)**exponent
            elif prime % 3 == 1 and exponent >= 2:
                projected = 2*chi4[prime % 4]**exponent
            elif prime > 3 and prime % 3 == 2 and exponent >= 4 and exponent % 2 == 0:
                projected = 2
            else:
                projected = 0
            if raw != projected:
                raise ArithmeticError("prime-ideal projection disagrees")
            if projected and not (m < y or b*b*y < m):
                weight = projected*arb(prime).log()
                if y < m < b*y:
                    constant += b*weight
                    slope -= b*weight/m
                    direct_terms.append((m, weight, True))
                elif b*y < m < b*b*y:
                    constant -= weight
                    slope += b*b*weight/m
                    direct_terms.append((m, weight, False))
                else:
                    raise ArithmeticError("a prime-power knot meets the bracket")
            m *= prime
            exponent += 1

    # Positive remainder and its logarithmic derivative after the constant H_b(0).
    def trivial_terms(value):
        rem, weighted = arb(0), arb(0)
        for j in range(1, 7):
            term = (1-b**(-j))*(b-b**(-j))/(j*(j+1)*value**j)
            rem += term
            weighted += (2*j+1)*term
        tail = 2*b*value**(-7)/(1-1/value)
        return rem + arb(0).union(tail), weighted + arb(0).union(tail)

    def stationary_equation(value):
        _, weighted = trivial_terms(value)
        return constant-slope*value+weighted

    if not (constant > 0 and slope > 0
            and stationary_equation(left) > 0 and stationary_equation(right) < 0):
        raise ArithmeticError("stationary point not bracketed")
    drift = 2*b.sqrt()*(b.sqrt()-1)**2
    numerical_bound = drift-2*(constant*slope).sqrt()
    # Evaluate the original tent at the root bracket without using its affine product.
    direct = h0 + trivial_terms(y)[0]
    for m, weight, first_branch in direct_terms:
        tent = b*(1-y/m) if first_branch else b*b*y/m-1
        direct += weight*tent
    correction = drift-direct/y.sqrt()
    # The signed identity avoids subtracting two nearly equal interval values.
    difference = (constant.sqrt()-(slope*y).sqrt())**2/y.sqrt() + trivial_terms(y)[0]/y.sqrt()
    if not (arb("0.11519") < correction < arb("0.11522")
            and arb("0.00000118") < difference < arb("0.00000120")
            and (correction+difference).overlaps(numerical_bound)):
        raise ArithmeticError("direct value and product bound at the maximum")
    balance_point = constant/slope
    if not (arb("12503.31985") < balance_point < arb("12503.31988") < left):
        raise ArithmeticError("stationary point displacement")
    spectral_value = correction+race/y.sqrt()
    spectral_derivative = race_log_derivative/y.sqrt()  # B' is zero at this root.
    if not (arb("3.217") < spectral_value < arb("3.220")
            and arb("12.218") < spectral_derivative < arb("12.221")):
        raise ArithmeticError("spectral value and derivative at the correction maximum")

    # Directly differentiate -W(m/y)/sqrt(y) on the two nonzero branches.
    # Multiplying by sqrt(y) leaves these branch slopes as functions of y/m.
    def rising_branch(ratio):
        return -(b*b*ratio+1)/2

    def falling_branch(ratio):
        return b*(1+ratio)/2

    jumps = (rising_branch(1/b**2),
             falling_branch(1/b)-rising_branch(1/b),
             -falling_branch(arb(1)))
    expected_jumps = (-arb(1), b+1, -b)
    if any(not abs(actual-expected) < arb("1e-12")
           for actual, expected in zip(jumps, expected_jumps)):
        raise ArithmeticError("signed square jumps")
    mean_density = b.sqrt()*(b.sqrt()*jumps[0]+jumps[1]+jumps[2]/b.sqrt())/2
    if not abs(mean_density-drift/4) < arb("1e-12"):
        raise ArithmeticError("square jump density and smooth curvature")
    print("A smooth positive maximum of B lies at 12503.33699 < y < 12503.33700. The direct tent gives 0.11519 < B < 0.11522 and the arithmetic product upper bound exceeds it by between 1.18e-6 and 1.20e-6.")
    print("At that maximum 3.217 < F < 3.220 and 12.218 < F' < 12.221. The three signed prime-square jumps give mean density D/4.")


if __name__ == "__main__":
    from flint import ctx

    with ctx.workprec(256):
        check_stationary_intercept()
