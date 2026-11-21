"""Certify the entire interval between the direct prime check and the two-zero bound."""

from fractions import Fraction
from functools import lru_cache
from math import isqrt

import numpy as np
from flint import arb


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def lower_integer(value):
    return int(value.lower().floor().unique_fmpz())


def check_race_vertices(b):
    """Evaluate every linear piece twice, using slope changes and prefix sums."""
    top = 500000
    limit = top * 9 // 2
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit - p*p) // p + 1)
    coefficients = []
    for p in range(5, limit + 1, 2):
        if not sieve[p]:
            continue
        if p % 3 == 1:
            signed_multiplicity = 2 if p % 4 == 3 else -2
            coefficients.append((p, signed_multiplicity * arb(p).log()))
        elif p*p <= limit:
            coefficients.append((p*p, -2 * arb(p).log()))
    coefficients.sort(key=lambda item: item[0])
    total, reciprocal = [arb(0)], [arb(0)]
    events = []
    for m, weight in coefficients:
        total.append(total[-1] + weight)
        reciprocal.append(reciprocal[-1] + weight / m)
        for kind, (position, jump) in enumerate((
            (arb(m) / b, b * weight / m),
            (arb(m), -(b + 1) * weight / m),
            (b * m, weight / m),
        )):
            if position < top:
                events.append((position, kind, jump))
            else:
                require(position > top, "terminal vertex separated from every knot")
    events.append((arb(top), 3, arb(0)))
    events.sort(key=lambda item: float(item[0].mid()))
    require(coefficients[0][0] == 7 and events[0][0].overlaps(7/b), "first active norm")
    previous = arb(0)
    value, slope = arb(0), arb(0)
    counts = [0, 0, 0]
    for index, (position, kind, jump) in enumerate(events):
        require(position > previous, "certified order of real knots")
        value += slope * (position - previous)
        if kind != 3:
            counts[kind] += 1
        hi, mid, lo = counts
        prefix_value = (b * (total[mid] - total[lo])
                        - position * (reciprocal[mid] - reciprocal[lo])
                        + b * position * (reciprocal[hi] - reciprocal[mid])
                        - (total[hi] - total[mid]))
        require(prefix_value.overlaps(value), "slope and prefix enclosures at the knot")
        if index:
            require(value > 0 and prefix_value > 0, "both evaluations give a strict lead")
        else:
            require(prefix_value.contains(0) and value.is_zero(), "first knot has zero race")
        slope += jump
        previous = position
    require(arb(13).exp() < top, "overlap with spectral intervals")
    print(f"Both arithmetic evaluations give a strict lead after x=7/b through x={top}, checking {len(events)} successive knots and endpoints.")


def check_arithmetic_constants():
    """Use the two explicit progression bounds of Ramare and Rumely."""
    upper_b = arb(9)/2
    coeff = 8 * (upper_b + upper_b**(arb(5)/4) - upper_b**(arb(1)/4)
                 - upper_b.sqrt()) / 3
    require(coeff < 20, "coefficient in the integrated square-root error")
    require(2*(upper_b-1)*upper_b*arb("0.002238") < arb("0.071"), "relative square error")
    require(4*(upper_b-1)*arb(2).log() < 10, "omitted prime above 2")
    require(2*(upper_b-1)*arb(3).log() < 8, "single ramified power")
    require(upper_b**2 < 27, "at most three powers of 3 in the prime window")
    require(13 + upper_b.log() - 3*arb(7).log() > arb(10)/3, "monotone tail of the odd-power bound")
    for t, target in ((13, "2.76"), (14, "2.18"), (19, "0.74"), (32, "0.115")):
        z = (arb(t)/2).exp() / upper_b.sqrt()
        log_x = t + upper_b.log()
        def odd_bound(k):
            return arb("0.26") * (log_x/k).exp() + (log_x/(2*k)).exp()
        higher = log_x/(2*arb(7).log()) - arb(3)/2
        bound = (20/z.sqrt() + arb("0.071") + 40/z
                 + 7 * (odd_bound(3) + higher*odd_bound(5)) / z)
        require(bound < arb(target), f"arithmetic upper bound starting at log x={t}")
    print("The upper bounds for B from log x=13, 14, 19 and 32 are 2.76, 2.18, 0.74 and 0.115.")


def sine_lower_table():
    """Integer lower bounds for 2 sin(pi d)^2 at d=j/1024 on [0,1/2]."""
    table = []
    for j in range(513):
        lo = Fraction(314159*j, 100000 * 1024)
        hi = Fraction(314160*j, 100000 * 1024)
        bound = lo - hi**3/6 + lo**5/120 - hi**7/5040
        require(bound >= 0, "nonnegative lower sine polynomial")
        table.append(int(2 * bound**2 * 10**7))
    return table


def cover_spectral_ranges(roots, b, method):
    """Integer phases enclose every real point of every closed dyadic cell."""
    scale = 10000
    bins = 256
    midpoint = method == "cosine"
    phase_bits = 42 if midpoint else 38
    denominator = 1 << phase_bits
    pi = arb.pi()
    waves = []
    for root in roots:
        rate = root / (2*pi)
        weight = 2*b.sqrt() * (b+1-2*b.sqrt()*(root*b.log()).cos()) / (arb(1)/4 + root**2)
        mark = int((rate*denominator).mid().floor().unique_fmpz())
        require(abs(rate*denominator-mark) < 1, "rounded frequency")
        waves.append((weight, mark, rate))
    waves.sort(key=lambda item: float(item[0].mid()), reverse=True)
    require(1000000*1024 < denominator, "accumulated frequency rounding")
    sine = sine_lower_table() if not midpoint else []
    if not midpoint:
        require(arb("3.14159") < pi < arb("3.14160"), "rational endpoints for pi")

    @lru_cache(maxsize=None)
    def kernel(wave_number, splits):
        weight, mark, rate = waves[wave_number]
        entries = []
        if midpoint:
            spread = rate/(2*splits) + arb(1000000)/denominator
            for j in range(bins):
                phase = (arb(j)/bins-spread).union(arb(j+1)/bins+spread)
                entries.append(max(0, lower_integer(scale * weight * (1+(2*pi*phase).cos()))))
        else:
            radial_loss = int((1024*rate/splits).upper().ceil().unique_fmpz()) + 1
            w = lower_integer(10**7 * weight)
            for j in range(bins):
                distance = 4 * min(abs(j-128), abs(j+1-128))
                index = max(0, distance-radial_loss)
                entries.append(w*sine[index]*scale // 10**14)
        return np.asarray(entries, dtype=np.int64)

    counts = []
    for start, stop, goal in ((2, 13, 10000), (13, 14, 28000), (14, 19, 22000),
                              (19, 32, 10000), (32, 1000000, 3500)):
        initial = 4 if midpoint else 8
        examined, finest = 0, initial
        for block in range(start*initial, stop*initial, 65536):
            cells = np.arange(block, min(block+65536, stop*initial), dtype=np.uint64)
            splits = initial
            while cells.size:
                require(splits <= 4096, "coverage attained within maximum depth")
                finest = max(finest, splits)
                examined += cells.size
                total = np.zeros(cells.size, dtype=np.int64)
                modulus = denominator * splits * (2 if midpoint else 1)
                require(modulus <= 2**64, "phase modulus divides 2^64")
                mask = np.uint64(modulus - 1)
                shift = np.uint64(modulus.bit_length() - 1 - 8)
                for i, (_, mark, _) in enumerate(waves):
                    centres = 2*cells+1 if midpoint else cells
                    phases = ((centres*np.uint64(mark) & mask) >> shift).astype(np.intp)
                    total += kernel(i, splits)[phases]
                    if i % 4 == 3 or i == len(waves)-1:
                        keep = total <= goal
                        cells, total = cells[keep], total[keep]
                        if not cells.size:
                            break
                if cells.size:
                    left = cells*2
                    cells = np.concatenate((left, left+1))
                    splits *= 2
        counts.append((examined, finest))
    print(f"The {method} certificate covers all five closed log intervals using {sum(n for n, _ in counts)} cells, with smallest width 1/{max(s for _, s in counts)}.")


def check_finite_range(roots):
    b = (arb(449334142447806)/10**14).union(arb(449334142447807)/10**14)
    check_race_vertices(b)
    check_arithmetic_constants()
    for method in ("cosine", "sine"):
        cover_spectral_ranges(roots, b, method)
    require(arb(2).exp() < 11 and 11 < arb(13).exp(), "overlap for the first class-11 prime")
    require(arb("0.35")**2 > arb("0.115"), "smallest spectral threshold")
    print("Under the two stated GRHs the sign is strict on 7/b < x <= exp(10^100), and every class-11 prime through that upper bound has F_q^2 > B_q.")
