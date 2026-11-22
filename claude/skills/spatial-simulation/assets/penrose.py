"""penrose.py -- Penrose (conformal) space as a viewport: the whole of Minkowski space drawn in a finite triangle.

Spherically symmetric Minkowski space ds^2 = -dt^2 + dr^2 (+ r^2 dOmega^2), null coordinates u = t - r, v = t + r.
Compactify:  p = atan(v), q = atan(u), T = p + q, R = p - q.   The image is the triangle  R >= 0, |T| + R <= pi.
The unphysical metric  -dT^2 + dR^2 = Omega^2 (-dt^2 + dr^2)  with  Omega = 2 cos p cos q  (checked below).
Null rays stay at 45 degrees; the infinities become the boundary:
    scri+  (p = pi/2)   future null infinity       scri-  (q = -pi/2)  past null infinity
    i+  (p = q = pi/2)   future timelike infinity   i-  (p = q = -pi/2)  past timelike infinity   i0  (p = pi/2, q = -pi/2)
A timelike worldline ends at i+ only as proper time -> infinity: i+ is approached, never reached.

Use: `penrose(t, r)` -> (T, R) for plotting; `boundary_pieces()` for the labelled boundary; `assert_penrose_sound()` is the gate.
Render rules: draw in (R horizontal, T vertical) with equal axes so null rays are exactly 45 degrees; label every boundary piece;
say which radial coordinate (r, or the curvature radius of a black-hole diagram) is meant; a Penrose diagram carries causal
structure only: distances and areas in it are not distances and areas in spacetime.
"""
from __future__ import annotations
import math, random

def penrose(t: float, r: float):
    p, q = math.atan(t + r), math.atan(t - r)
    return (p + q, p - q)

def conformal_factor(t: float, r: float) -> float:
    return 2.0 * math.cos(math.atan(t + r)) * math.cos(math.atan(t - r))

def boundary_pieces():
    P = math.pi
    return {'scri+': [(P / 2 + q, P / 2 - q) for q in (-P / 2 + 1e-9 + k * (P - 2e-9) / 20 for k in range(21))],
            'scri-': [(p - P / 2, p + P / 2) for p in (-P / 2 + 1e-9 + k * (P - 2e-9) / 20 for k in range(21))],
            'i+': [(P, 0.0)], 'i-': [(-P, 0.0)], 'i0': [(0.0, P)]}

def in_triangle(T: float, R: float, tol: float = 1e-9) -> bool:
    return R >= -tol and abs(T) + R <= math.pi + tol

def assert_penrose_sound(seed: int = 0) -> bool:
    rnd = random.Random(seed)
    for _ in range(500):
        t, r = rnd.uniform(-50, 50), rnd.uniform(0.0, 50)
        T, R = penrose(t, r)
        assert in_triangle(T, R), (t, r, T, R)                                  # everything lands in the triangle
        # conformal: -dT^2 + dR^2 == Omega^2 (-dt^2 + dr^2)
        h = 1e-6; dt, dr = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
        T1, R1 = penrose(t + h * dt, r + h * dr)
        lhs = -(T1 - T) ** 2 + (R1 - R) ** 2
        rhs = conformal_factor(t, r) ** 2 * (-(h * dt) ** 2 + (h * dr) ** 2)
        assert abs(lhs - rhs) <= 1e-6 * max(1e-12, abs(rhs)) + 1e-14, (lhs, rhs)
        # a null direction (dt = +-dr) stays null, i.e. 45 degrees
        for s in (+1, -1):
            T2, R2 = penrose(t + h, r + s * h)
            assert abs(abs(T2 - T) - abs(R2 - R)) < 1e-6 * h + 1e-12 * 0 + 1e-9, (s,)
    # a timelike worldline (r = 0.5 t) approaches i+ as t -> infinity but is never AT it
    T, R = penrose(1e6, 0.5e6)
    assert abs(T - math.pi) < 1e-5 and R < 1e-5 and not (T == math.pi)
    # a light ray reaching infinity ends on scri+
    T, R = penrose(1e6, 1e6 - 3.0)
    assert abs(T + R - math.pi) < 1e-5
    return True

if __name__ == '__main__':
    print('penrose sound:', assert_penrose_sound())
