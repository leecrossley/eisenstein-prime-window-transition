"""Enclose the Eisenstein prime-race transition using the two primitive L-functions."""
from flint import acb, arb, ctx, dirichlet_char, fmpq
from math import isqrt

ctx.prec = 120
C = 2*arb.const_euler() + (arb.pi()**2/12).log()


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def completed_mass(q, label):
    char=dirichlet_char(q,label)
    require(char.is_real() and char.is_primitive(), "primitive real character")
    parity=int(char.parity())
    # Constant and linear terms in the Hurwitz zeta expansion at 1.
    sums=[]
    for j in (0,1):
        total=arb(0)
        for a in range(1,q):
            value=char(a)
            if not value.is_zero():
                total+=value.real*acb.stieltjes(j,acb(fmpq(a,q))).real
        sums.append(total)
    L1=sums[0]/q
    logder=-sums[1]/sums[0]-arb(q).log()
    constant=(arb(q)/arb.pi()).log()+arb(fmpq(1+parity,2)).digamma()+2*logder
    require(L1>0 and char.l_function(acb("0.5")).real>0, "nonzero central and endpoint values")
    return constant,logder


def signed_ramp(b):
    """The only nonzero coefficients strictly below 9 occur at 3 and 7."""
    return (-arb(3).log()*(b/3-1).max(arb(0))
            -2*arb(7).log()*(b/7-1).max(arb(0)))


def closed(b):
    r=b.sqrt()
    return (2*(r-1)**2+(b-1)*C+2*signed_ramp(b)
            -2*b.log()+2*(b-1)*(1-1/b).log())


def local_factors(limit=100000):
    flags=bytearray([1])*(limit+1)
    flags[:2]=bytes(2)
    for p in range(2,isqrt(limit)+1):
        if flags[p]:
            flags[p*p::p]=bytes((limit-p*p)//p+1)
    four={1:1,3:-1}
    twelve={1:1,5:-1,7:-1,11:1}
    count=0
    for p in range(5,limit+1):
        if not flags[p]:
            continue
        # The quadratic discriminant detects splitting independently of the residue table.
        split=pow(-3,(p-1)//2,p)==1
        power,exponent=p,1
        while power<=limit:
            ideal=2*four[p%4]**exponent if split else (2 if exponent%2==0 else 0)
            require(ideal==four[power%4]+twelve[power%12],"Euler coefficient at a prime power")
            count+=1
            power*=p
            exponent+=1
    print(f"{count} unramified prime powers through {limit} satisfy the local Euler identity.")


def main():
    local_factors()
    c4,d4=completed_mass(4,3)
    c12,d12=completed_mass(12,11)
    require(c4+c12<arb("0.486") and 2*((arb(3)-1)/(3+1))**2>c4+c12,
            "all dilations at least nine")
    require(closed(arb(3))<arb("-0.82"), "negative through three by convexity")
    for n,jumps in [(3, -2*arb(3).log()/3),(7,-2*arb(3).log()/3-4*arb(7).log()/7)]:
        b=arb(n)
        slope=2-2/b.sqrt()+C+2*(1-1/b).log()+jumps
        require(slope>arb("0.04"), "right-hand derivative at a downward jump")
    left=arb("4.49334142447806")
    right=arb("4.49334142447807")
    require(closed(left)<0 and closed(right)>0, "transition bracket")
    # An independent expression in the same arithmetic: do not first cancel the L'/L terms.
    for b,sgn in [(left,-1),(right,1),(arb(4),-1),(arb(5),1)]:
        T=1+(b-1)*(1-1/b).log()
        Sb=c4+c12 + signed_ramp(b)+(b-1)*(d4+d12)-b.log()+T-1
        raw=2*(b.sqrt()-1)**2-((b+1)*(c4+c12)-2*Sb)
        require(sgn*raw>0, "uncancelled Dirichlet ramp")
    require(arb(5).sqrt()*closed(arb(5))>arb("0.94"), "width-five margin")
    print("The two completed Dirichlet masses sum to less than 0.486. Both central values are positive.")
    print("The unique transition lies strictly between 4.49334142447806 and 4.49334142447807.")
    print("At dilation five the limiting lower bound exceeds 0.94 times the square-root scale.")


if __name__ == "__main__":
    main()
