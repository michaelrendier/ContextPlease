"""
minkowski.py: spatial awareness in Minkowski spacetime (1+1 and 1+2 D), the pseudo-Euclidean viewport.  numpy only.
Signature (-, +, +): interval s2 = -(c dt)^2 + dx^2 + dy^2.  Units c = 1 unless stated.
Everything a renderer needs: events, boosts (hyperbolic rotations), light cones, worldlines and proper time, simultaneity slices,
the observer's past-light-cone viewport, Wick rotation, and assert_minkowski_sound() (the acceptance test).
"""
import numpy as np

def interval2(a, b, c=1.0):
    """squared interval between events a, b = (t, x[, y]): negative = timelike, 0 = null (on the light cone), positive = spacelike"""
    d = np.asarray(b, float) - np.asarray(a, float)
    return -(c*d[0])**2 + np.sum(d[1:]**2)

def classify(a, b, c=1.0, tol=1e-12):
    s = interval2(a, b, c)
    return "null" if abs(s) < tol else ("timelike" if s < 0 else "spacelike")

def boost_x(v, c=1.0):
    """Lorentz boost along x with velocity v (a hyperbolic rotation by rapidity eta = atanh(v/c)), acting on (t, x, y)"""
    b = v/c; g = 1/np.sqrt(1 - b*b)
    return np.array([[g, -g*b/c, 0], [-g*b*c, g, 0], [0, 0, 1.0]])

def boost(events, v, c=1.0):
    E = np.atleast_2d(np.asarray(events, float)); n = E.shape[1]
    B = boost_x(v, c)[:n, :n]
    return E @ B.T

def light_cone(apex=(0.0, 0.0, 0.0), height=1.0, n=96, future=True, c=1.0):
    """the null cone of an event as a surface: ring of events on |x| = c|t - t0| (the 'witch's hat' of Ainulindale/wiki/29)"""
    th = np.linspace(0, 2*np.pi, n, endpoint=False); sg = 1 if future else -1
    ring = np.stack([np.full(n, apex[0] + sg*height), apex[1] + c*height*np.cos(th), apex[2] + c*height*np.sin(th)], axis=1)
    return {"apex": np.array(apex, float), "ring": ring}

def worldline(fn, t0, t1, n=2001, c=1.0):
    """events (t, x[, y]) of a particle path x(t) from fn(t) (a vector of spatial coordinates), with proper time tau(t) along it.
    raises if the path is ever faster than light (it is not a worldline)"""
    t = np.linspace(t0, t1, n); X = np.array([np.atleast_1d(fn(tt)) for tt in t])
    v = np.gradient(X, t, axis=0); sp = np.sqrt((v**2).sum(1))
    if np.any(sp >= c): raise ValueError("speed >= c somewhere: not a timelike worldline")
    dtau = np.sqrt(1 - (sp/c)**2); tau = np.concatenate([[0], np.cumsum(0.5*(dtau[1:] + dtau[:-1])*np.diff(t))])
    return {"t": t, "x": X, "tau": tau, "events": np.column_stack([t, X])}

def simultaneity_slice(v, t0=0.0, half=3.0, n=2, c=1.0):
    """in the frame moving at v relative to the diagram, the line of simultaneity through (t0, 0): t = t0 + (v/c^2) x"""
    x = np.linspace(-half, half, n); return np.column_stack([t0 + (v/c**2)*x, x])

def past_cone_viewport(observer, events, c=1.0, tol=1e-9):
    """what an observer at `observer` can see: events on or inside its past light cone.  The Minkowski analogue of the camera frustum."""
    o = np.asarray(observer, float); E = np.atleast_2d(np.asarray(events, float))
    dt = o[0] - E[:, 0]; dr = np.sqrt(((E[:, 1:] - o[1:])**2).sum(1))
    return (dt > 0) & (c*dt >= dr - tol), np.where(dt > 0, dr/np.maximum(c*dt, 1e-30), np.inf)   # (visible, causal ratio: 1 = exactly seen)

def wick(events_t, sign=-1):
    """Wick rotation t -> -i tau (Lorentzian -> Euclidean): returns tau.  Under it the signature (-,+,+) becomes (+,+,+) and a
    particle moving in a potential V moves in -V (the hat's hilltop becomes a well): the bounce / instanton picture."""
    return np.asarray(events_t, float)

def euclidean_path(V, x0=1.0, eps=1e-3, dtau=1e-3, steps=60000):
    """Euclidean-time (Wick-rotated) motion of a unit mass in the potential V (radial, V(0) = 0 hilltop, V(brim) = -1): the particle moves in
    -V, so the brim (the minimum of V) is the CREST of -V and the hilltop is its bottom.  A particle released at rest just inside the brim
    rolls to the hilltop in finite Euclidean time, arriving with speed sqrt(2 (V(0) - V(x0))) by conservation of v^2/2 - V.
    This is the bounce / instanton path from the brim to the point.  Returns (tau, x, speed)."""
    h = 1e-6; dV = lambda x: (float(V(x + h)) - float(V(max(x - h, 1e-12))))/(x + h - max(x - h, 1e-12))
    x = x0 - eps; v = 0.0; tau = [0.0]; xs = [x]; sp = [0.0]
    for k in range(steps):
        v += dV(x)*dtau*(+1)          # x'' = +dV/dx   (motion in -V)
        x += v*dtau
        tau.append((k + 1)*dtau); xs.append(x); sp.append(abs(v))
        if x <= 1e-6: break
    return np.array(tau), np.array(xs), np.array(sp)

def assert_minkowski_sound(seed=0, c=1.0):
    """acceptance test: the interval is invariant under boosts; light rays stay at 45 degrees; causal class is frame-independent;
    a worldline's proper time never exceeds its coordinate time; the apex event sees exactly the past cone."""
    rng = np.random.default_rng(seed); ok = {}
    a, b = rng.normal(size=3), rng.normal(size=3)
    ok["interval_invariant"] = all(abs(interval2(*boost([a, b], v, c), c) - interval2(a, b, c)) < 1e-9 for v in (0.1, 0.6, 0.95))
    ray = np.array([[0, 0, 0], [1, 1, 0.0]]); rb = boost(ray, 0.8, c)
    ok["null_stays_null"] = abs(interval2(rb[0], rb[1], c)) < 1e-9
    ok["class_invariant"] = all(classify(a, b, c) == classify(*boost([a, b], v, c), c) for v in (0.3, 0.9))
    w = worldline(lambda t: [0.5*np.sin(t)], 0, 5); ok["proper_time_le_coordinate"] = bool(w["tau"][-1] <= w["t"][-1] - w["t"][0] + 1e-12)
    cone = light_cone(height=2.0, future=False); vis, _ = past_cone_viewport((0, 0, 0), cone["ring"]); ok["past_cone_ring_visible"] = bool(vis.all())
    s0 = simultaneity_slice(0.0); s1 = simultaneity_slice(0.5); ok["slices_tilt_with_velocity"] = bool(s0[1, 0] == s0[0, 0] and s1[1, 0] > s1[0, 0])
    return ok

if __name__ == "__main__":
    print(assert_minkowski_sound())
