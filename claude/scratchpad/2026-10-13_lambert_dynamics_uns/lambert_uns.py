#!/usr/bin/env python3
"""Lambert W as a fixed-point object: (1) the four tests and their multiplicity, (2) the values in Universal Native Space
(decimal-log scale, divide by ln 10; and in units of d*_taut), (3) W as the fixed-point MULTIPLIER of x -> exp(-lam x)
(fold at multiplier +1, flip at -1), (4) the fold as a projection artifact, (5) the cardioid cusp as the same multiplier-+1 point."""
import math, cmath
import numpy as np
import mpmath as mp
mp.mp.dps = 40
LN10 = mp.log(10); E = mp.e
W0_0 = mp.lambertw(0, 0).real; W0_1 = mp.lambertw(1, 0).real
W0_m = mp.lambertw(-1 / E, 0).real; Wm1_m = mp.lambertw(-1 / E, -1).real
print("1. THE FOUR TESTS (principal branch W0 at x = 0, 1, -1/e ; the second real branch W-1 at x = -1/e)")
tests = [("W0(0)", W0_0), ("W0(1)", W0_1), ("W0(-1/e)", W0_m), ("W-1(-1/e)", Wm1_m)]
for n, v in tests: print("   %-11s = %s" % (n, mp.nstr(v, 25)))
distinct = sorted({mp.nstr(v, 15) for _, v in tests}); print("   distinct values (to 15 digits): %d ; counted with multiplicity (the branch point is a double root): %d" % (len(distinct), len(tests)))
print("   numerical splitting of the double root: W0(-1/e) - W-1(-1/e) = %s  (evaluating at a 40-digit -1/e, error ~1e-41, splits the pair by ~ sqrt(2 e x error): the square-root sensitivity IS the double root)" % mp.nstr(W0_m - Wm1_m, 5))
dst = W0_1 / LN10
print("\n2. THE VALUES IN UNIVERSAL NATIVE SPACE (UNS = decimal-log metric ds = d.log10(p): divide a natural-log quantity by ln 10)")
print("   ln 10 = %s ; 1/ln 10 = log10(e) = %s ; d*_taut = W(1)/ln 10 = %s" % (mp.nstr(LN10, 20), mp.nstr(1 / LN10, 20), mp.nstr(dst, 20)))
print("   %-11s %-26s %-26s %-26s" % ("value", "natural scale", "UNS (value / ln 10)", "in units of d*_taut"))
for n, v in tests:
    print("   %-11s %-26s %-26s %-26s" % (n, mp.nstr(v, 20), mp.nstr(v / LN10, 20), mp.nstr(v / dst, 20)))
S = sum(v for _, v in tests)
print("   sum of the four tests: %s = Omega - 2 ; UNS: %s = d*_taut - 2/ln10 : %s ; in d*_taut units: %s" % (mp.nstr(S, 20), mp.nstr(S / LN10, 20), mp.nstr(dst - 2 / LN10, 20), mp.nstr(S / dst, 20)))
print("   W(1) in UNS IS d*_taut (the Flow);  W(-1/e) in UNS is -log10(e) = -0.4342944819...;  W(1) = ln10 x d*_taut (the Translator)")
print("   1/d*_taut = ln10/Omega = %s" % mp.nstr(1 / dst, 20))

print("\n3. W AS THE FIXED-POINT MULTIPLIER.  f_lam(x) = exp(-lam x): fixed point x* = W(lam)/lam ; multiplier f'(x*) = -lam x* = -W(lam)")
def fp_mult(lam):
    x = 0.5
    for _ in range(4000): x = math.exp(-lam * x)
    return x, -lam * math.exp(-lam * x)
print("   lam      W(lam)        multiplier -W(lam)   numerical f'(x*)   behaviour of the iteration (last values)")
for lam in (0.0 + 1e-12, 1.0, 2.0, math.e * 0.98, math.e, 3.0, 4.0, 8.0):
    x = 0.5; orb = []
    for i in range(6000):
        x = math.exp(-lam * x)
        if i > 5900: orb.append(round(x, 6))
    per = next((p for p in range(1, 33) if all(abs(orb[i] - orb[i - p]) < 1e-5 for i in range(p, len(orb)))), None)
    w = float(mp.lambertw(lam).real)
    xs = w / lam
    print("   %-8.4f %-13.8f %-20.8f %-18.8f %s" % (lam, w, -w, -lam * xs, "attracting fixed point" if per == 1 else ("period %d" % per if per else "aperiodic / chaotic (no period <= 32)")))
print("   NOTE: past lam = e the orbit settles on a period-2 cycle and stays there (tested to lam = 8): exp(-lam x) is DECREASING, so its second iterate is increasing and the real map cannot be chaotic; no cascade, no crisis in the technical sense on the real line.")
print("   multiplier = -1 (FLIP: period doubling) at W(lam) = 1  <=>  lam = e ;  multiplier = 0 at lam = 0 (superstable) ; the idle point is lam = 1 : multiplier -Omega")
print("   GROWTH family g_lam(x) = exp(lam x): fixed points are solutions of exp(lam x) = x, i.e. x = -W(-lam)/lam ; multiplier = -W(-lam)")
for lam in (0.30, 1 / math.e, 0.40):
    xs = np.linspace(-1, 12, 200001); h = np.exp(lam * xs) - xs; roots = int(np.sum(np.diff(np.sign(h)) != 0))
    print("      lam = %.6f : number of real fixed points = %d%s" % (lam, roots, "   (tangent: the double root; fixed point x = e, multiplier +1)" if abs(lam - 1 / math.e) < 1e-9 else ""))
print("   (at lam = 1/e: W(-1/e) = -1 and the multiplier -W = +1: the FOLD / saddle-node; tetration's critical base e^{1/e})")

print("\n4. THE FOLD IS A PROJECTION.  The curve (w, x = w e^w) is smooth and single-valued in w; dx/dw = e^w (1+w) vanishes at w = -1.  Number of real w with w e^w = x:")
for x in (2.0, 0.5, 0.0, -0.1, -1 / math.e, -0.4):
    ws = np.linspace(-12, 4, 800001); h = ws * np.exp(ws) - x; n = int(np.sum(np.diff(np.sign(h)) != 0))
    print("      x = %+.6f : %d real preimage(s)%s" % (x, n, "   <- the branch point (exactly ONE preimage, a double root; the float -1/e sits a hair above the true value, so the grid sees 2)" if abs(x + 1 / math.e) < 1e-12 else ""))
print("   (Whitney: the generic singularity of a projection of a smooth curve/surface is a fold; the two-valuedness of W is the shadow of a smooth curve with a vertical tangent)")

print("\n5. THE CARDIOID CUSP IS THE SAME MULTIPLIER +1.  Boundary of the main cardioid: c(mu) = mu/2 - mu^2/4 for the fixed-point multiplier mu = e^{i t} of z -> z^2 + c")
print("   dc/dmu = 1/2 - mu/2 vanishes on the unit circle only at mu = 1 : c(1) = %.4f ; at c = 1/4 the fixed point z = 1/2 has multiplier 2z = %.4f (the saddle-node)" % ((1 / 2 - 1 / 4), 2 * 0.5))
ts = np.linspace(-0.2, 0.2, 5)
print("   |dc/dt| along the boundary near t = 0 (speed of the boundary point; 0 = cusp):", [round(abs(0.5j * cmath.exp(1j * t) - 0.5j * cmath.exp(2j * t)), 4) for t in ts])
print("   So the cardioid is the unit circle |mu| = 1 seen through a map with a critical point at mu = 1: a circle, flattened.")
