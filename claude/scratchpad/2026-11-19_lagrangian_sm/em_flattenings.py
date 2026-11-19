"""The electromagnetic units as two flattenings of the ampere axis (ESU / EMU), Maxwell's relation, the free-space impedance, Stoney/Planck, and the d* GAP (Ainulindale wiki 142).
    python3 em_flattenings.py"""
import math
c = 299792458.0; mu0 = 1.25663706212e-6; eps0 = 8.8541878128e-12
print("eps0*mu0*c^2 = %.12f ; Z0 = mu0*c = %.6f ohm = %.6f pi" % (eps0*mu0*c*c, mu0*c, mu0*c/math.pi))
A_esu = (0.5, 1.5, -2); A_emu = (0.5, 0.5, -1); print("A_ESU - A_EMU over (kg, m, s) =", tuple(a - b for a, b in zip(A_esu, A_emu)), "(one velocity)")
cgs = {"volt": (299.792458, 1e-8, -1), "ohm": (8.9875517923e11, 1e-9, -2), "farad": (1.11265005545e-12, 1e9, 2)}
for k, (es, em, a) in cgs.items(): print("%-6s statunit/abunit = %.6e ; c(cm/s)^%d = %.6e" % (k, es/em, -a, (c*100)**(-a)))
G = 6.67430e-11; hb = 1.054571817e-34; e = 1.602176634e-19
lP = math.sqrt(hb*G/c**3); lS = math.sqrt(G*e**2/(4*math.pi*eps0*c**4)); alpha = e**2/(4*math.pi*eps0*hb*c)
print("l_P = %.6e m ; l_Stoney = %.6e m ; ratio %.5f ; sqrt(alpha) = %.5f ; 1/2 ln(1/alpha) = %.4f nepers" % (lP, lS, lS/lP, math.sqrt(alpha), 0.5*math.log(1/alpha)))
Om = 0.5671432904097838; ds = Om/math.log(10); print("d* = %.10f decades ; Omega = %.10f nepers ; GAP = Omega - 0.24600*ln10 = %.6e" % (ds, Om, Om - 0.24600*math.log(10)))
