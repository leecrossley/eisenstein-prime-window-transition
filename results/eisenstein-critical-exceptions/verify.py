"""Verify two actual Dirichlet-zero brackets and their positive pair weights."""

from flint import arb, ctx, dirichlet_char

ctx.prec = 144


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def main():
    b = arb("4.49334142447806").union(arb("4.49334142447807"))
    r = b.sqrt()
    for q, label, parity, values, left, right, floor in (
        (4, 3, 1, [0, 1, 0, -1], 5, 7, "0.10"),
        (12, 11, 0, [0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1], 3, 4, "0.32"),
    ):
        char = dirichlet_char(q, label)
        require(char.is_real() and char.is_primitive() and int(char.parity()) == parity,
                "primitive character and parity")
        require(all(char(j) == v for j, v in enumerate(values)), "residue values")
        zl, zr = char.hardy_z(left), char.hardy_z(right)
        require(zl.real > 0 and zr.real < 0, "Hardy sign change")
        lower = 2*r*(r-1)**2/(arb("0.25")+right**2)
        require(lower > arb(floor), "pair weight")
        print(f"Conductor {q}: a critical-line ordinate lies in ({left},{right}); its conjugate pair has weight > {floor}.")


if __name__ == "__main__":
    main()
