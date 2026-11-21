"""Certify an odd integer combination of twelve low Dirichlet zero ordinates."""

from flint import acb, acb_series, arb, ctx, dirichlet_char


# Midpoints of disjoint sign brackets for each character, in sixteenths.
ROOT_SEEDS = (
    (4, 3, (97, 163, 207, 261, 293, 343)),
    (12, 11, (61, 107, 143, 179, 207, 243)),
)

# Coefficients in the order of ROOT_SEEDS. Only their certified sum matters.
ODD_COMBINATION = (
    -233251822251037186062758411671186572911655402578146316814190578914547603639433955727568020689978,
    239032762593962201861259145502257821567789822666775038173891220661208312592344283683784957404722,
    463908570828609317074046692662676012982629100227179538166330067971854980943036285993334868625892,
    -390507887066848524118518975835896731604100279678887358892536737283122055787319949001614563361241,
    12436768584721234384456788257617821328312618817069761730858596812214638673385705811823286595656,
    428865953328746428135635384418528646322523332161293975278228304212716032874299123921264966942612,
    -437465684839486437970275775008481625340374191631280103849468912677949001415620397480918880333971,
    -371818939872971353970847675766174618468526905289077062922600665574791530382523907753107806281369,
    -174410568263756121019969806315717282370288510313029946196330846007754180726248995200328756322891,
    328289311357929432654380081741681877037260591225555228232380568213049757435476112925792284487018,
    -321432950190945370919423227330501411238621706232469037485326828613695722298346016994131879305901,
    -257976971374593485533236567018468754203496470634732578613487965966680803845741818713360137102272,
)


def refined_height(character, seed):
    """Return a candidate midpoint. The sign tests certify the roots independently."""
    value = arb(seed)/16
    for precision, steps in ((128, 6), (240, 1), (464, 1), (912, 1),
                             (1808, 1), (3600, 1), (4260, 2)):
        with ctx.workprec(precision):
            for _ in range(steps):
                s = acb(arb(1)/2, value)
                jet = acb_series([s, 1], prec=2).dirichlet_l(character)
                correction = (jet[0]/(acb(0, 1)*jet[1])).real
                value = (value-correction).mid()
    return value


def root_brackets(euler_sum):
    """Enclose one root per interval by Hardy signs and a finite Euler transform."""
    roots = []
    with ctx.workprec(4260):
        radius = arb(10)**(-1180)
        for conductor, label, seeds in ROOT_SEEDS:
            character = dirichlet_char(conductor, label)
            step, offsets = (2, [(1, 1)]) if conductor == 4 else (6, [(1, 1), (5, -1)])
            for seed in seeds:
                middle = refined_height(character, seed)
                left, right = middle-radius, middle+radius
                if not (abs(middle-arb(seed)/16) < arb(1)/8 and left > 0 and right < 22):
                    raise ArithmeticError("candidate escaped the intended bracket")
                signs = []
                for height in (left, right):
                    hardy = character.hardy_z(height).real
                    if not (hardy > 0 or hardy < 0):
                        raise ArithmeticError("undecided Hardy sign")
                    signs.append(1 if hardy > 0 else -1)
                    s = acb(arb(1)/2, height)
                    value, error = euler_sum(s, step, offsets, 4176)
                    z = (s+character.parity())/2
                    completion = (z*(arb(conductor)/arb.pi()).log()).exp()*z.gamma()
                    if not signs[-1]*(completion*value).real > abs(completion)*error:
                        raise ArithmeticError("independent Euler transform at the bracket")
                if signs[0] == signs[1]:
                    raise ArithmeticError("opposite signs required")
                enclosure = left.union(right)
                if any(enclosure.overlaps(old) for old in roots):
                    raise ArithmeticError("overlapping root brackets")
                roots.append(enclosure)
    return roots


def check_odd_combination(euler_sum):
    roots = root_brackets(euler_sum)
    with ctx.workprec(4260):
        if len(roots) != len(ODD_COMBINATION) or sum(ODD_COMBINATION) % 2 != 1:
            raise ArithmeticError("length or parity of the certificate")
        frequency = abs(sum(m*r for m, r in zip(ODD_COMBINATION, roots)))
        if not arb("1.84875907e-1058") < frequency < arb("1.84875908e-1058"):
            raise ArithmeticError("enclosure for the odd combination")
        # b > 4 and every ordinate is below 22, so a_gamma > 4/(22^2+1/4).
        weight_bound = 125*sum(m*m for m in ODD_COMBINATION)
        if not (4*125 > 22**2+1 and 2*weight_bound < 10**195
                and frequency*10**1058 < 2*arb.pi()/3
                and (2*10**8+1)*10**390 < (10**100)**8
                and 4*arb.pi()/(3*frequency) > 2*10**1058):
            raise ArithmeticError("spectral floor, overlap or recurring interval length")
    print("Two evaluations certify twelve disjoint zero brackets and an odd combination with absolute value between 1.84875907e-1058 and 1.84875908e-1058.")
    print("Under the two stated GRHs the race is strictly positive on 7/b < x <= exp(10^1058). No class-11 prime satisfies F_q^2 <= B_q through that bound. Further certified log intervals have length greater than 2*10^1058.")
