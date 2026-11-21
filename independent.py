"""Independent rational and Dirichlet-series checks for the Eisenstein threshold."""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt


def point(x):
    return Q(x),Q(x)


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def sub(a,b):
    return a[0]-b[1],a[1]-b[0]


def mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)


def unit_log(x):
    z=(x-1)/(x+1)
    n=45
    t=2*sum(z**(2*k+1)/(2*k+1) for k in range(n))
    return t,t+2*z**(2*n+1)/((2*n+1)*(1-z*z))


@lru_cache(maxsize=None)
def logq(x):
    x=Q(x)
    if x <= 0:
        raise ValueError("positive logarithm argument required")
    j=0
    while x>=2:
        x/=2
        j+=1
    while x<1:
        x*=2
        j-=1
    return add(unit_log(x),mul(point(j),unit_log(Q(2))))


def atan_inv(d):
    z=Q(1,d)
    n=32
    partial=sum((-1)**k*z**(2*k+1)/(2*k+1) for k in range(n))
    following=partial+(-1)**n*z**(2*n+1)/(2*n+1)
    return min(partial,following),max(partial,following)


def constants():
    pi=sub(mul(point(16),atan_inv(5)),mul(point(4),atan_inv(239)))
    n=1024
    h=sum(Q(1,j) for j in range(1,n+1))
    approx=sub(point(h-Q(1,2*n)+Q(1,12*n**2)-Q(1,120*n**4)),logq(n))
    gamma=add(approx,(Q(0),Q(1,252*n**6)))
    lnpi=logq(pi[0])[0],logq(pi[1])[1]
    ln2pi=add(logq(2),lnpi)
    c0=sub(add(point(2),gamma),add(logq(2),ln2pi))
    return gamma,c0,ln2pi


def root(b):
    scale = 10**40
    n = isqrt(b.numerator*scale**2//b.denominator)
    return Q(n,scale),Q(n+1,scale)


def inverse(a):
    require(a[0]>0, "inverse of an interval that is not positive")
    return 1/a[1],1/a[0]


def require(test, reason):
    if not test:
        raise ArithmeticError(reason)


def signs(n):
    four = {1:1,3:-1}.get(n%4,0)
    twelve = {1:1,5:-1,7:-1,11:1}.get(n%12,0)
    return four,twelve


def direct_ramp(b):
    value=point(0)
    for n in range(2,10):
        if n>=b:
            break
        # Only prime powers appear among n=2,...,9 other than 6.
        if n==6:
            continue
        p={4:2,8:2,9:3}.get(n,n)
        value=add(value,mul(point(sum(signs(n))*(b/n-1)),logq(p)))
    return value


def original_endpoint(b, constant):
    x=1/b
    # Combined trivial zeros of the odd and even characters give every positive m.
    terms=55
    s=sum(x**m/(m*(m+1)) for m in range(1,terms+1))
    tail=x**(terms+1)/((terms+1)*(terms+2)*(1-x))
    r=sub(root(b),point(1))
    return add(add(mul(point(2),mul(r,r)),mul(point(b-1),constant)),
               mul(point(2),add(direct_ramp(b),sub(sub((s,s+tail),point(1)),logq(b)))))


def dirichlet_derivatives():
    # At the end of each twelve-term period, all subsequent partial sums
    # of either character are between -1 and +1.
    from decimal import Decimal,localcontext
    N=48000
    scale=10**24
    def ceilq(v):return -(-v.numerator//v.denominator)
    accum=[[0,0,0,0] for k in range(2)]
    with localcontext() as context:
        context.prec=60
        for n in range(1,N+1):
            sg=signs(n)
            if sg==(0,0):continue
            v=Decimal(n).ln()
            L=Q(v.next_minus())*scale/n if n>1 else Q(0)
            U=Q(v.next_plus())*scale/n if n>1 else Q(0)
            a,zz=scale//n,-(-scale//n)
            c,d=L.numerator//L.denominator,ceilq(U)
            for j,s in enumerate(sg):
                if s==1: lower,upper,dlo,dhi=a,zz,-d,-c
                elif s==-1: lower,upper,dlo,dhi=-zz,-a,c,d
                else: continue
                acc=accum[j]
                for k,t in enumerate((lower,upper,dlo,dhi)):acc[k]+=t
    tail1=Q(1,N)
    taild=logq(N)[1]/N
    answer=point(0)
    for a,b,c,d in accum:
        denom=(Q(a,scale)-tail1,Q(b,scale)+tail1)
        numer=(Q(c,scale)-taild,Q(d,scale)+taild)
        answer=add(answer,mul(numer,inverse(denom)))
    return answer


def main():
    g,_,ln2pi=constants()
    # C=2 gamma + 2 log pi - log 12.
    lnpi=sub(ln2pi,logq(2))
    C=sub(add(mul(point(2),g),mul(point(2),lnpi)),logq(12))
    full_mass=sub(mul(point(2),dirichlet_derivatives()),C)
    require(full_mass[1]<Q("0.49"),"upper bound for the two zero masses")
    require(original_endpoint(Q(3),C)[1]<0,"convex first interval")
    jumps=point(0)
    for n,co in [(3,Q(-2,3)),(7,Q(-4,7))]:
        jumps=add(jumps,mul(point(co),logq(n)))
        s=add(sub(point(2),mul(point(2),inverse(root(Q(n))))),
              add(C,add(mul(point(2),logq(Q(n-1,n))),jumps)))
        require(s[0]>0,"positive right derivative")
    for digits,side in [("4.49334142447806",-1),("4.49334142447807",1)]:
        require(mul(point(side),original_endpoint(Q(digits),C))[0]>0,"uncancelled trivial-zero series")
    require(mul(root(Q(5)),original_endpoint(Q(5),C))[0]>Q("0.94"),"width-five sign")
    print("48000 Dirichlet-series terms per character bound the total zero mass below 0.49.")
    print("Exact rational intervals and 55 trivial-zero terms confirm the transition and width-five margin.")


if __name__=="__main__":
    main()
