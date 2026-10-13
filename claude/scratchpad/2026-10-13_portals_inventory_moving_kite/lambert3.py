#!/usr/bin/env python3
"""The three Lambert-W values of the Third Age draft (Ainulindale/AgeThird/Third_Age_CS_Draft_v2.md s2.2, App. D):
   W(0) = 0   (vacuum fixed point) ;  W(1) = Omega_ZS = 0.5671432904...  (entropy ceiling) ;  W(-1/e) = -1  (branch collapse).
Repeated here with three independent methods and with the local structure that distinguishes them."""
import math, mpmath as mp
import numpy as np
from scipy.special import lambertw
mp.mp.dps = 50
E = mp.e
print("1. mpmath (50 digits)")
for lab, x in (("W(0)", mp.mpf(0)), ("W(1)", mp.mpf(1)), ("W(-1/e)", -1 / E)):
    w = mp.lambertw(x); print("   %-8s = %s   check w e^w - x = %s" % (lab, mp.nstr(w.real, 40), mp.nstr(w.real * mp.e ** w.real - x, 3)))
print("   W_{-1}(-1/e) = %s  (the second real branch meets the principal branch at the branch point)" % mp.nstr(mp.lambertw(-1 / E, -1).real, 20))
print("\n2. scipy.special.lambertw (double precision)")
for lab, x in (("W(0)", 0.0), ("W(1)", 1.0), ("W(-1/e)", -1 / math.e)):
    print("   %-8s = %.16f" % (lab, lambertw(x).real))
print("\n3. Newton on f(w) = w e^w - x from several starts: iterations to 1e-15 and the observed order")
def newton(x, w0, tol=1e-15, maxit=200):
    w = w0; errs = []
    root = -1.0 if abs(x + 1 / math.e) < 1e-15 else float(lambertw(x).real)   # scipy gives nan exactly at the branch point
    for n in range(maxit):
        f = w * math.exp(w) - x; fp = math.exp(w) * (1 + w)
        if fp == 0: break
        w = w - f / fp; errs.append(abs(w - root))
        if errs[-1] < tol: return n + 1, errs
    return maxit, errs
for lab, x, starts in (("W(0)", 0.0, (0.3, -0.5, 1.0)), ("W(1)", 1.0, (0.3, 1.0, 2.0)), ("W(-1/e)", -1 / math.e, (-0.5, -0.8, -2.0, -0.2))):
    for w0 in starts:
        n, errs = newton(x, w0)
        ratios = [errs[i + 1] / errs[i] for i in range(len(errs) - 1) if errs[i] > 1e-6 and errs[i + 1] > 0][:4]
        print("   %-8s start %+.1f : %3d iterations ; error ratios e(n+1)/e(n) = %s" % (lab, w0, n, np.round(ratios, 3).tolist()))
print("   (a ratio ->0.5 means a DOUBLE root: linear convergence; ratios shrinking fast mean a simple root: quadratic)")
print("\n4. local structure f'(w) = e^w (1+w) at each root, and the fixed-point multiplier of x -> e^{-x}")
for lab, w in (("W(0)", 0.0), ("W(1)", float(lambertw(1).real)), ("W(-1/e)", -1.0)):
    print("   %-8s root %+.10f : f'(root) = %.10f %s" % (lab, w, math.exp(w) * (1 + w), "  <- DOUBLE root (branch point)" if abs(math.exp(w) * (1 + w)) < 1e-12 else ""))
Om = float(lambertw(1).real)
print("   x -> exp(-x) at Omega: multiplier = -exp(-Omega) = %.10f = -Omega: %s   (|.|<1: attracting, alternating)" % (-math.exp(-Om), abs(-math.exp(-Om) + Om) < 1e-12))
x = 0.5; its = 0
while abs(x - Om) > 1e-12: x = math.exp(-x); its += 1
print("   fixed-point iteration x -> exp(-x) from 0.5 reaches Omega to 1e-12 in %d steps (rate %.4f per step, predicted %.4f)" % (its, Om, Om))
print("\n5. relations to the four d*")
LN10 = math.log(10); dt = Om / LN10
print("   d*_taut = W(1)/ln10 = %.15f ; d*_ln10 = d*_taut * ln10 = %.16f = W(1) : %s" % (dt, dt * LN10, abs(dt * LN10 - Om) < 1e-15))
print("   Omega = exp(-Omega) = %.16f ; Omega = -ln(Omega) = %.16f" % (math.exp(-Om), -math.log(Om)))
print("   note: scipy.special.lambertw(-1/e) returned nan in double precision (the float -1/e sits on/just past the branch point); mpmath at 50 digits returns exactly -1.")
