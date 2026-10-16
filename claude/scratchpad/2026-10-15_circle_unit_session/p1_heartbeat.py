"""P1 — the heartbeat's area under the curve, and where the 1/2 radius comes from.
Heartbeat (Ainulindale wiki/96): the standing wave  y = sin^2 x  (and cos^2 x), x in [0, 2pi].
Questions: area under the curve; mean; the circle hiding in it; relation to the zeta critical-line loops."""
import mpmath as mp, numpy as np
mp.mp.dps = 30
A_s = mp.quad(lambda x: mp.sin(x)**2, [0, 2*mp.pi]); A_c = mp.quad(lambda x: mp.cos(x)**2, [0, 2*mp.pi])
print("∫0^2π sin² =", A_s, "   ∫ cos² =", A_c, "  sum =", A_s + A_c, "(= 2π:", mp.mpf(2)*mp.pi, ")")
print("mean of sin² over the cycle =", A_s/(2*mp.pi), "  <- the 1/2")
print("area under the curve / bounding rectangle (2π x 1) =", A_s/(2*mp.pi))
# the circle in the curve: pair sin²x with its quadrature partner sin x cos x
th = np.linspace(0, 2*np.pi, 9)
X = np.sin(th)**2; Y = np.sin(th)*np.cos(th)
print("(sin²x − 1/2)² + (sin x cos x)²  =", np.round((X-.5)**2 + Y**2, 15), " <- constant 1/4: circle radius 1/2 centre (1/2, 0)")
print("that circle: radius 1/2, diameter 1, circumference π, area π/4 ;  it passes through the origin (x=0 at sin x=0)")
print("polar form about the origin: r = cos φ  (φ = x):  x = r cos φ = cos²x ... check r²= x²+y² ->", np.round(np.hypot(np.cos(th)**2, np.sin(th)*np.cos(th)) - np.abs(np.cos(th)), 15))
# areas: area under sin² over one cycle (=π) vs the circle's quantities
r = mp.mpf(1)/2
print("circle d=1: circumference", mp.pi*1, " area", mp.pi*r**2, " | area under heartbeat over one cycle =", A_s, "= circumference of that circle (pi*d)")
print("                         and  = 4 * (area of that circle):", 4*mp.pi*r**2)
# the polar area of the circle r=cos(phi), phi in [-pi/2,pi/2]: 1/2 ∫ r² dφ
print("polar area ½∫cos²φ dφ over [-π/2,π/2] =", mp.quad(lambda p: mp.cos(p)**2/2, [-mp.pi/2, mp.pi/2]), " = π/4")
print("area under sin² over HALF cycle [0,π] =", mp.quad(lambda x: mp.sin(x)**2, [0, mp.pi]), " = π/2")
