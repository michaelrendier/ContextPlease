#!/usr/bin/env python3
"""What is the ring-theory version of a derivative? A DERIVATION: any additive
map D satisfying Leibniz D(ab)=D(a)b+aD(b). No limit, no topology needed.
Tested here; engine relation: SedenionFactoralRelativity/engine/lineage.py,
ring.arithmetic_derivative (G8)."""
import os, sys, random
from fractions import Fraction
sys.path.insert(0, os.path.expanduser('~/Projects/ThePlace/SedenionFactoralRelativity'))
from engine.lineage import primary_decomposition, arith_deriv

print("== formal derivative on R[x]: gcd(f,f')!=1 <=> repeated root (ramification) ==")
def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): out[i+j]+=ai*bj
    return out
def D(a): return [i*a[i] for i in range(1,len(a))]
def poly_gcd(a,b):
    def trim(p):
        while len(p)>1 and p[-1]==0: p.pop()
        return p
    a=trim([Fraction(c) for c in a]); b=trim([Fraction(c) for c in b])
    while any(b):
        if len(a)<len(b): a,b=b,a
        while len(a)>=len(b) and any(a):
            coef=a[-1]/b[-1]; shift=len(a)-len(b)
            for i in range(len(b)): a[shift+i]-=coef*b[i]
            a=trim(a)
            if a==[Fraction(0)]: break
        a,b=b,a
    return trim(a)
f_rep=poly_mul([-2,1],poly_mul([-2,1],[-3,1]))          # (x-2)^2(x-3)
f_sf =poly_mul([-2,1],poly_mul([-3,1],[-5,1]))          # (x-2)(x-3)(x-5)
print("repeated-root gcd(f,f') degree:", len(poly_gcd(f_rep,D(f_rep)))-1, "(nontrivial)")
print("squarefree gcd(f,f') degree:   ", len(poly_gcd(f_sf,D(f_sf)))-1, "(trivial)")

print("\n== arithmetic derivative on Z: p'=1, Leibniz determines the rest ==")
random.seed(2)
bad=sum(1 for _ in range(500)
        for a,b in [(random.randint(2,800),random.randint(2,800))]
        if arith_deriv(a*b)!=arith_deriv(a)*b+a*arith_deriv(b))
print("Leibniz over 500 random pairs, mismatches:", bad)
for p,k in [(2,3),(3,4),(5,2)]:
    print(f"  D({p}^{k})={arith_deriv(p**k)} vs power rule k*p^(k-1)={k*p**(k-1)}")
print("D(0),D(1) =", arith_deriv(0), arith_deriv(1), " (the Mingling, killed)")
fixed=[n for n in range(2,4000) if arith_deriv(n)==n]
print("fixed points D(n)=n:", fixed, "= [2^2,3^3,5^5], the arithmetic e^x")
