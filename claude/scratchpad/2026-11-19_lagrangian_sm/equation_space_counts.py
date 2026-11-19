"""Bracketing counts and associativity spread over random words (EquationSpace stub).
   PYTHONPATH=~/Projects/ThePlace ValaQuenta/.venv/bin/python equation_space_counts.py"""
import math, random
from fractions import Fraction as F
from ValaQuenta.modules.emerger.maths import cd_mul
def e(i): v=[F(0)]*16; v[i]=F(1); return tuple(v)
def brackets(seq):
    if len(seq)==1: return [seq[0]]
    return [tuple(cd_mul(list(L),list(R))) for k in range(1,len(seq)) for L in brackets(seq[:k]) for R in brackets(seq[k:])]
cat=lambda n: math.comb(2*n,n)//(n+1)
print([cat(n-1) for n in range(2,9)], 24*cat(3), math.factorial(7)*cat(6), "%.4e"%(math.factorial(16)*cat(15)))
random.seed(7)
for alg,idx in (("octonion",range(1,8)),("sedenion",range(1,16))):
    for n in (4,5):
        d=[];z=0
        for _ in range(300):
            vals=brackets([e(random.choice(list(idx))) for _ in range(n)]); nz=[v for v in vals if any(x!=0 for x in v)]
            z+=len(nz)<len(vals); d.append(len(set(nz)))
        print(alg,n,sum(d)/300,z)
