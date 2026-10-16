"""P5 — translation machinery: the same circle under different labels.
(a) gravity / Coulomb / wire are ONE flux law in n dimensions (the 'circle' is the (n-1)-sphere of radius r).
(b) the wire's inside/outside fold = circle inversion = Kelvin transform; exactly symmetric only in n = 2.
(c) inside-the-wire |B| ~ |mu| of an attracting fixed point; outside ~ 1/|mu| (the same map run backwards): Mandelbrot main cardioid is the image of the unit disk of multipliers."""
import numpy as np, math
from math import gamma, pi
def S(n, r): return 2*pi**(n/2)/gamma(n/2)*r**(n-1)        # area of the (n-1)-sphere of radius r
def V(n, r): return pi**(n/2)/gamma(n/2+1)*r**n              # ball volume
def F(n, r, R=1.0):                                          # field of a uniformly filled n-ball, total source 1 (Gauss/Ampere/Newton law)
    enclosed = (V(n, r)/V(n, R)) if r < R else 1.0
    return enclosed/S(n, r)
print("(a) flux law  S_{n-1}(r) F(r) = enclosed source:   n=2 wire (Ampere), n=3 gravity/Coulomb (Newton/Gauss), n=4,5 higher")
print("    constants: 2D: 1/S_1(r) = 1/(2 pi r)  [circumference];  3D: 1/(4 pi r^2) [sphere area];  n: 1/S_{n-1}")
for n in (2, 3, 4, 5):
    Rr = (F(n, 1.0000001), F(n, 2.0))
    out_slope = (math.log(F(n, 4.0)) - math.log(F(n, 2.0)))/(math.log(4)-math.log(2))
    in_slope = (math.log(F(n, 0.5)) - math.log(F(n, 0.25)))/(math.log(.5)-math.log(.25))
    print(f"    n={n}: log-log slope inside {in_slope:+.3f}, outside {out_slope:+.3f}  (expected +1 and {1-n:+d}); peak at r=R, F(R)={F(n,1.0):.5f} = 1/S_{n-1}(1) = {1/S(n,1):.5f}")
print("\n(b) inversion r -> R^2/r :  F(R^2/r)/F(r) for r<R")
for n in (2, 3, 4):
    ratios = [F(n, 1/r)/F(n, r) for r in (0.2, 0.5, 0.9)]
    kel = [r**(n-2) for r in (0.2, 0.5, 0.9)]
    print(f"    n={n}: ratio {np.round(ratios, 6)}   Kelvin weight (r/R)^(n-2) = {np.round(kel, 6)}   {'EXACT SYMMETRY (n=2)' if n == 2 else 'symmetric only after the Kelvin weight'}")
print("    -> the wire is symmetric under the circle fold ONLY in 2D, where inversion is conformal and the Laplacian is covariant with weight 1.")
print("       gravity (n=3) has the same fold with weight (r/R): the tent in u=ln r has slopes +1/-2, not +1/-1.")
print("\n(c) Mandelbrot: f(z) = z^2 + c.  fixed point z* = (1 - sqrt(1-c))/... ; multiplier mu = f'(z*) = 2 z*.   c(mu) = mu/2 - mu^2/4")
rng = np.random.default_rng(1)
err = 0
for _ in range(2000):
    mu = rng.uniform(0, 1)**.5*np.exp(1j*rng.uniform(0, 2*pi)); c = mu/2 - mu*mu/4
    zs = mu/2                                                   # fixed point z* = mu/2 ; check z*^2 + c = z*
    err = max(err, abs(zs*zs + c - zs))
print(f"    fixed point z*=mu/2 solves z*^2+c=z*: max residual {err:.1e};  attracting iff |mu|<1  (|mu| = r/R of the wire interior)")
th = np.linspace(0, 2*pi, 200001); mu = np.exp(1j*th); c = mu/2 - mu**2/4; dc = np.gradient(c, th)
print(f"    c(mu) on |mu|=1: cusp at mu=1 gives c={c[0]:.4f} (=1/4); min speed |dc/dtheta| = {np.abs(dc).min():.2e} at theta={th[np.argmin(np.abs(dc))]:.4f} (critical point of c(mu): dc/dmu = (1-mu)/2 = 0 at mu=1)")
area = 0.5*np.trapezoid((c.real*np.gradient(c.imag, th) - c.imag*np.gradient(c.real, th)), th); per = np.trapezoid(np.abs(dc), th)
print(f"    cardioid area {area:.6f} (3π/8 = {3*pi/8:.6f});  perimeter {per:.6f} (4)")
print("    c=0: Julia set = the unit circle (mu=0).  c inside the cardioid: Julia set is a quasicircle (deformed unit circle).  Outside: Cantor dust.  |mu|=1: Siegel/parabolic boundary.")
print("    fold mu -> 1/conj(mu): the SAME fixed point of f^{-1} has multiplier 1/mu:  B_wire(r) = min(|mu|, 1/|mu|) = contraction strength of the fixed point under f or under f^{-1}")
for r in (0.3, 0.7, 1.6, 3.0):
    print(f"      r/R={r}: |B|/Bmax={min(r, 1/r):.4f} = min(|mu|,1/|mu|) with |mu|=r/R ;  e^(-|u|) = {math.exp(-abs(math.log(r))):.4f}")
