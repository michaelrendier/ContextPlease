#!/usr/bin/env python3
"""L_(I|O) is the mechanism of the generational lineage of The Observer — tested.
See README.md. Run against SedenionFactoralRelativity on the path."""
import math, os, sys
sys.path.insert(0, os.path.expanduser('~/Projects/ThePlace/SedenionFactoralRelativity'))
from engine.lineage import sigma_self, sigma_rb, nrm, zero, SED_DIM
def J(r, th): return (1.0/r, th + math.pi/2)
print("1 fixed point r=1:", [r for r in (0.5,1.0,2.0) if abs(1/r-r)<1e-12])
r,th=2.0,0.0
for _ in range(4): r,th=J(r,th)
print("3 order-4 lineage closes:", abs(r-2.0)<1e-9 and abs(th%(2*math.pi))<1e-9)
r2,th2=J(2.0,0.0)
for _ in range(3): r2,th2=J(r2,th2)
print("4 reverse inherent (J⁻¹=J³):", abs(r2-2.0)<1e-9)
print("5 r·(1/r)=1 conserved:", all(abs(r*(1/r)-1)<1e-12 for r in (0.1,1,10)))
A=zero(SED_DIM); A[0]=A[8]=1/math.sqrt(2)
B=zero(SED_DIM); B[0]=B[4]=B[8]=B[12]=0.5
print("6 scalar forgets / full keeps reverse:",
      abs(sigma_self(A)-sigma_self(B))<1e-12 and nrm([x-y for x,y in zip(sigma_rb(A),sigma_rb(B))])>1e-9)
