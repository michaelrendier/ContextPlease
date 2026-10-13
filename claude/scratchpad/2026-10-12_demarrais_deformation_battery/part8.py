#!/usr/bin/env python3
"""PART 8 — the 4 d* faces and the 3 Lambert-W values as the sedenion doubling parameter mu4.
(Constants restricted to the ones necessary for ln(10) in Universal Native Space, per Cody 2026-10-13;
everything else is in Appendix B / Future work of the record.)"""
import math, mpmath as mp
from zdscan import *
LN10 = math.log(10)
W0 = float(mp.lambertw(0).real); W1 = float(mp.lambertw(1).real)
Wm = float(mp.lambertw(-1 / math.e, 0).real); Wm1 = float(mp.lambertw(-1 / math.e, -1).real)
print("Lambert W values (mpmath):  W(0) = %.16f   W(1) = %.16f   W(-1/e) principal = %.16f   W_-1(-1/e) = %.16f" % (W0, W1, Wm, Wm1))
print("   W(1)*exp(W(1)) = %.16f (the fixed point of x -> exp(-x): %.16f)" % (W1 * math.exp(W1), math.exp(-W1)))
DST = W1 / LN10
print("   d*_taut = W(1)/ln10 = %.12f ; d*_ln10 = d* x ln10 = %.16f = W(1): %s" % (DST, DST * LN10, abs(DST * LN10 - W1) < 1e-15))
def row(label, mus):
    sm = summarise(mus)
    print("   %-46s pairs=%-5d degree=%-6s within-chart=%-4d kappa=%s" % (label, sm['capable_ordered_plane_pairs'], sm['degree_set'], sm['within_chart'], sm['kappa_x'][:2]), flush=True)
print("\nTHE THREE LAMBERT-W VALUES as the doubling parameter mu4 (mu1..3 = -1):")
row("mu4 = W(0) = 0", (-1., -1., -1., W0))
row("mu4 = W(1) = +0.5671 (as the value itself)", (-1., -1., -1., W1))
row("mu4 = -W(1) = -0.5671", (-1., -1., -1., -W1))
row("mu4 = W(-1/e) = -1", (-1., -1., -1., Wm))
print("\nTHE FOUR d* FACES as mu4 = -d  (tilt of the standard kite):")
row("d*  (Boundary) = 0.24631", (-1., -1., -1., -0.24631))
row("d*_taut (Flow) = W(1)/ln10", (-1., -1., -1., -DST))
row("d*_ln(10) (Translator) = W(1)", (-1., -1., -1., -W1))
row("d*_RG (Stability): dimension 8 as -8", (-1., -1., -1., -8.0))
row("d*_RG target value 0.24631 (same as d*)", (-1., -1., -1., -0.24631))
row("ln(10)  (the thing being built)", (-1., -1., -1., -LN10))
print("\nTHE 4 x 3 TABLE: mu4 = -(d*_face x W_value) is NOT used (no defined interaction); see record §6 for what is and is not established.")
