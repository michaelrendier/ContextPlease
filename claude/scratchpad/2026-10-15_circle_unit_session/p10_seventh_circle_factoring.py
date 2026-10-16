"""P10 — the seventh circle (l_p) and factoring: Fermat curves, Euler (circle) vs Fermat (hyperbola) factorisation, conjugate exponents."""
import math, itertools
from math import isqrt, gcd
print("1. integer points of the l_p circle of radius c, |x|^p+|y|^p=c^p, 0<x<=y<c, c<=300  (p integer = the FERMAT CURVE x^p+y^p=z^p)")
for p in (2, 3, 4, 5):
    n = 0; ex = []
    for c in range(2, 301):
        for x in range(1, c):
            r = c**p - x**p
            y = round(r ** (1/p))
            for yy in (y-1, y, y+1):
                if yy >= x and yy < c and yy**p == r:
                    n += 1; ex.append((x, yy, c)) if len(ex) < 3 else None
    print(f"   p={p}: {n} primitive+non-primitive solutions with z<=300   e.g. {ex}")
print("   (p=2 has them all — Pythagorean triples; p>=3 none: Fermat's Last Theorem, Wiles 1995. Non-integer exponents have no rational structure to count.)")

print("\n2. Three conics, three factorisation methods (Cayley-Klein triple), N = p q")
def euler(N):
    reps = [(a, isqrt(N-a*a)) for a in range(1, isqrt(N)+1) if isqrt(N-a*a)**2 == N-a*a and isqrt(N-a*a) >= a]
    if len(reps) < 2: return None
    (a, b), (c, d) = reps[0], reps[1]
    # N = a^2+b^2 = c^2+d^2 => gcd(a-c, N) or gcd(a+c, N)
    # CHASED 2026-10-15: the first version used gcd(a-c, N) etc., which only worked for N=65 by luck (221 -> None).
    # Correct Euler step: N | (ad - bc)(ad + bc), so gcd(N, ad - bc) is a proper factor.
    for g in (gcd(N, abs(a*d - b*c)), gcd(N, a*d + b*c)):
        if 1 < g < N: return g, N//g, reps
    return None
def fermat(N):
    a = isqrt(N)
    if a*a < N: a += 1
    k = 0
    while True:
        b2 = a*a - N
        b = isqrt(b2)
        if b*b == b2: return a-b, a+b, k
        a += 1; k += 1
for N in (5*13, 13*17, 29*37, 53*61, 101*113):
    e = euler(N); f = fermat(N)
    print(f"   N={N}: Euler (circle x^2+y^2=N) -> {e[:2] if e else None} from reps {e[2] if e else None};  Fermat (hyperbola a^2-b^2=N) -> {f[:2]} in {f[2]+1} steps")
print("   Euler needs p,q = 1 (mod 4) [two sum-of-squares reps exist]; Fermat is general. The elliptic conic is the Gaussian-integer lattice; the hyperbolic conic is the split-complex one.")

print("\n3. the imaginary circle x^2+y^2 = -N: (x+iy)(x-iy) = -N ; Fermat's hyperbola is the REAL section after y -> i y")
N = 3*7*1  # irrelevant example of sign; use N=91
N = 7*13
a, b = 10, 3   # 10^2 - 3^2 = 91
print(f"   a^2 - b^2 = N: ({a})^2 - ({b})^2 = {a*a-b*b};  as a circle: a^2 + (ib)^2 = {a*a + (1j*b)**2}  -> radius^2 = N: the circle of radius sqrt(N) with the second coordinate imaginary")
print("   A(r=sqrt N) = pi N; the same circle with the second axis imaginary has the hyperbola's 'area' sign flip: -> hyperbolic sector area = (N/2) * phi, no pi")

print("\n4. conjugate exponents 1/p+1/q=1 : the Holder dual. Table (p, q, pi_p) — the dual pair always has the same pi_p")
import sys; sys.path.insert(0, "/home/rendier/Projects/ThePlace/GenerationalLineage")
from engine.toolsets import circle as C
for p in (1.25, 1.5, 2.0, 3.0, 4.0, 5.0):
    q = p/(p-1)
    print(f"   p={p:<5} q={q:<8.4f} pi_p={C.pi_p(p):.6f} pi_q={C.pi_p(q):.6f}  area_p={C.lp_circle(p)['area']:.5f} area_q={C.lp_circle(q)['area']:.5f}")
print("   pi_p equal on the dual pair, AREAS differ -> duality preserves circumference/diameter, not area.")
