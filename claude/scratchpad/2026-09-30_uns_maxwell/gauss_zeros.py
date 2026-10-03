"""The monopole field E_r(R) = pi(R^2)/R is carried by the zeta zeros: pi(x) = R(x) - 2 sum_{gamma>0} Re li(x^rho) (Riemann explicit formula, first term),
so E_r(R) has radial standing-wave components of frequency 2*gamma in ln R.  Check numerically with the first K zeros."""
import mpmath as mp, sympy
mp.mp.dps = 30
K = 200
zeros = [mp.zetazero(k) for k in range(1, K + 1)]
def Rfun(x):    # Riemann R(x) = sum mu(k)/k li(x^(1/k))
    s = mp.mpf(0)
    for k in range(1, 60):
        mu = sympy.mobius(k)
        if mu: s += mu * mp.li(mp.mpf(x) ** (mp.mpf(1) / k)) / k
    return s
def pi_exact(x): return int(sympy.primepi(x))
print("   R      x=R^2   pi(x)   R(x)-pi   after 20 zeros   after 50   after 200      (errors pi - approx, in prime counts; divide by R for the field)")
for R in (100, 316, 1000):
    x = R * R; base = Rfun(x); exact = pi_exact(x); row = []
    for Kk in (0, 20, 50, 200):
        approx = base - 2 * sum(mp.re(mp.ei(z * mp.log(mp.mpf(x)))) for z in zeros[:Kk])
        row.append(float(exact - approx))
    print("%5d %9d %7d %9.2f %13.2f %10.2f %10.2f" % (R, x, exact, float(exact - base), row[1], row[2], row[3]))
print("amplitude of one zero's contribution to E_r: about 1/(2*gamma*ln R): gamma_1 = %.4f -> at R=1000: %.4f" % (float(zeros[0].imag), 1 / (2 * float(zeros[0].imag) * mp.log(1000))))
