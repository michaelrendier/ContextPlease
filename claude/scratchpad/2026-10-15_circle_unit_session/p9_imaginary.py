"""P9 — the imaginary circle (radius i·rho): measures, the n-ball Sign cycle, exp/i^i links, inscribed triangles,
laws of sines and cosines, the hyperbolic (cosh) form, the Gaussian continuation."""
import sys, math, cmath
sys.path.insert(0, "/home/rendier/Projects/ThePlace/GenerationalLineage")
from engine.toolsets import circle as C
pi = math.pi
print("1. n-ball volume V_n(R)=pi^(n/2) R^n / Gamma(n/2+1) at R=i  -> Sign rotates by i^n")
for n in range(0, 9):
    v = pi ** (n / 2) / math.gamma(n / 2 + 1) * (1j) ** n
    print(f"   n={n}: V_n(1)={pi**(n/2)/math.gamma(n/2+1):9.5f}  V_n(i)={v.real:+10.5f}{v.imag:+10.5f}j   phase i^n = {(1j)**n:.0f}")
print("   surface S_{n-1}(R)=n V_n R^-1 *R^n : S_1 (circumference) = 2 pi R -> 2 pi i ; S_2 = 4 pi R^2 -> -4 pi")

print("\n2. exp links: C(r=i)=2 pi i is the period of exp;  A(r=i)=-pi;  i^i = exp(A/2)")
print("   exp(C) =", cmath.exp(2j*pi), "  i^i =", (1j)**(1j), "  exp(-pi/2) =", math.exp(-pi/2), "  exp(A)=e^-pi =", math.exp(-pi), " (i^i)^2 =", ((1j)**(1j))**2)
print("   e^{i pi} = -1: the antipode (Sign) ; e^{i d/2 ...}: for r=i, e^{C/2} =", cmath.exp(pi*1j))

print("\n3. points of the imaginary unit circle  z = i(cos t, sin t) : chord, arc, sector")
t1, t2 = 0.3, 1.9
z1 = (1j*math.cos(t1), 1j*math.sin(t1)); z2 = (1j*math.cos(t2), 1j*math.sin(t2))
chord2 = (z1[0]-z2[0])**2 + (z1[1]-z2[1])**2         # bilinear (not Hermitian) distance^2
d = t2 - t1
print(f"   chord^2 = {chord2:.6f}   -4 sin^2(d/2) = {-4*math.sin(d/2)**2:.6f}   => chord = 2i sin(d/2) = {2j*math.sin(d/2):.6f}")
print(f"   arc = r*d = i*d = {1j*d:.6f} ; sector area = r^2 d/2 = {-d/2:.6f}")

print("\n4. triangle inscribed in the imaginary unit circle: sides imaginary, angles REAL, 2R = a/sinA")
ts = (0.2, 2.1, 4.0)
P = [(1j*math.cos(t), 1j*math.sin(t)) for t in ts]
def side(p, q): return cmath.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
a, b, c = side(P[1], P[2]), side(P[0], P[2]), side(P[0], P[1])
cosA = (b*b + c*c - a*a)/(2*b*c); A = cmath.acos(cosA)
cosB = (a*a + c*c - b*b)/(2*a*c); B = cmath.acos(cosB)
cosC = (a*a + b*b - c*c)/(2*a*b); Cc = cmath.acos(cosC)
print("   sides:", [f"{x:.4f}" for x in (a, b, c)])
print("   angles (rad):", [f"{x.real:.5f}{x.imag:+.1e}j" for x in (A, B, Cc)], " sum =", f"{(A+B+Cc).real:.6f}", "(pi =", f"{pi:.6f})")
print("   a/sinA, b/sinB, c/sinC:", [f"{x:.5f}" for x in (a/cmath.sin(A), b/cmath.sin(B), c/cmath.sin(Cc))], " => 2R =", "2i expected")
s = (a+b+c)/2; hs = s*(s-a)*(s-b)*(s-c); K = cmath.sqrt(hs)
print(f"   Heron: s(s-a)(s-b)(s-c) = {hs:.6f} (real, positive); area = +/-sqrt = {K:.6f};  1/2 b c sin A = {0.5*b*c*cmath.sin(A):.6f}")
print(f"   circumradius abc/(4K) with K = 1/2 bc sinA : {a*b*c/(4*0.5*b*c*cmath.sin(A)):.6f}  (expected i = 1j)")

print("\n5. 3-4-5 with imaginary sides is inscribed in a circle of radius 2.5 i:")
a, b, c = 3j, 4j, 5j; K = 0.5*a*b          # right angle between a,b
R = a*b*c/(4*K)
print(f"   area K = 1/2*(3i)(4i) = {K}   R = abc/4K = {R}   circle area pi R^2 = {pi*R*R:.5f}  (= -pi*6.25 = {-pi*6.25:.5f})")
print("   Real 3-4-5: R=2.5, K=6 ; ratio K/(pi R^2) real:", f"{6/(pi*6.25):.6f}", " imaginary:", f"{(K/(pi*R*R)).real:.6f}  (SAME: area ratio is scale/Sign free)")

print("\n6. Spherical -> hyperbolic: cos(c/R)=cos(a/R)cos(b/R)+sin sin cos C ; R=i rho  ->  cosh c/rho = cosh a/rho cosh b/rho - sinh a/rho sinh b/rho cos C")
a, b, c, rho = 0.5, 0.6, 0.7, 1.0
print("   cosh form residual:", abs(math.cosh(c/rho) - (math.cosh(a/rho)*math.cosh(b/rho) - math.sinh(a/rho)*math.sinh(b/rho)*math.cos(C.sphere_triangle_angle(a, b, c, 1j*rho).real))))
for R in (1.0, 2j, 1j, 0.5j):
    t = C.triangle(0.5, 0.6, 0.7, R)
    print(f"   R={R!s:6}: angle sum - pi = {t['angle_sum'].real - pi:+.6f}  area = R^2*excess = {t['area'].real:+.6f}   sine ratios equal: {abs(t['sine_ratios'][0]-t['sine_ratios'][1])<1e-9}")
print("   Curvature K=1/R^2:  R=1 -> +1 ; R=i -> -1 ; area scale R^2 flips sign with K.  Gauss-Bonnet: area = (angle sum - pi)/K")

print("\n7. Gaussian: polar integral of exp(-r^2/R^2) over the plane = pi R^2  (convergent for Re(1/R^2)>0)")
print("   R=1: pi.   R=i: exp(+r^2) DIVERGES; pi R^2 = -pi is the analytic continuation, NOT a convergent integral.")
print("   Rotated: s=1/R^2=-i  -> Fresnel: int exp(i r^2) over plane = i*pi (converges conditionally);  pi R^2 with R^2 = i : ", f"{pi*1j:.4f}")
print("   So the area -pi is the continuation at R^2=-1 ; R^2=+i (a 45-degree-rotated radius e^{i pi/4}) is the CONVERGENT Fresnel/oscillatory case: area i*pi")

print("\n8. the split-complex partner (real section): x^2 - y^2 = -1 hyperbola (j^2=+1); 'radius' rho, arc = rho*phi (hyperbolic angle), sector area = rho^2 phi/2 ; no pi: periods become 2 pi i in phi (Wick)")
print("   cosh^2 - sinh^2 = 1  <->  cos^2 + sin^2 = 1 under t -> i t :  cos(it)=cosh t, sin(it)= i sinh t ;", cmath.cos(1j*0.7), math.cosh(0.7), cmath.sin(1j*0.7), 1j*math.sinh(0.7))
