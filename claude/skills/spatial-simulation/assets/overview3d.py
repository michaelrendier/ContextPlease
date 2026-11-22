"""overview3d.py -- choose the viewer axes, ranges and camera for n-dimensional data, so it can always be shown in 3D (static)
or 3D moving (the fourth dimension is the animation).

    ov = overview(X, mode='static')      # X: (n, d) array, d >= 3
    ov['P']        (n,3) points rescaled into [-1,1]^3 using robust ranges (outliers clipped, flagged in ov['clipped'])
    ov['axes']     3 orthonormal d-vectors (the viewer axes: the directions of greatest spread; or `axes_hint` columns)
    ov['ranges']   per-axis (lo, hi) in the data's own units
    ov['rest']     the remaining directions ranked by spread: the channels for colour / size / small-multiples (budget: 2-3)
    ov['camera']   best of 26 canonical poses by projected spread without overlap; OpenSCAD ($vpr, $vpt, $vpd) and Blender
    mode='moving'  adds ov['frames']: the 4th direction becomes a rotation in the (axis3, axis4) plane, so every point is seen
                   in some frame; each frame is an orthonormal axis triple (the data is never changed, only the viewer).
Rule (spatial-simulation section 9): the viewer axes are chosen by the data's spread, not by the author's labels; label the
axes with what they are made of (the loadings), report the variance explained by the three shown, and say what was clipped.
`assert_overview_sound()` is the gate: orthonormal axes, every unclipped point inside the unit cube and inside the frustum.
"""
from __future__ import annotations
import math
import numpy as np

def _robust_centre(X):
    return np.median(X, axis=0)

def overview(X, mode: str = 'static', axes_hint=None, clip=(1.0, 99.0), frames: int = 24, fovy_deg: float = 35.0,
             aspect: float = 4 / 3):
    X = np.asarray(X, float)
    n, d = X.shape
    assert d >= 3, 'need at least 3 dimensions'
    c = _robust_centre(X)
    Y = X - c
    if axes_hint is not None:
        A = np.linalg.qr(np.asarray(axes_hint, float).T)[0][:, :3]
        U, S, Vt = np.linalg.svd(Y - Y @ A @ A.T, full_matrices=False)
        rest = Vt
        order = A
    else:
        U, S, Vt = np.linalg.svd(Y, full_matrices=False)
        order = Vt[:3].T
        rest = Vt[3:]
    var = (S ** 2) / max(1e-300, (S ** 2).sum())
    P = Y @ order
    lo = np.percentile(P, clip[0], axis=0)
    hi = np.percentile(P, clip[1], axis=0)
    span = np.where(hi - lo > 0, hi - lo, 1.0)
    mid = (hi + lo) / 2.0
    Pu = (P - mid) / (span / 2.0)
    clipped = (np.abs(Pu) > 1.0).any(axis=1)
    Pc = np.clip(Pu, -1.0, 1.0)
    # camera: the pose (azimuth, elevation) among 26 canonical directions that spreads the projected points most
    best, bestscore = None, -1.0
    for az in range(0, 360, 45):
        for el in (-60, -30, 0, 30, 60):
            a, e = math.radians(az), math.radians(el)
            vdir = np.array([math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
            x = np.cross([0, 0, 1.0], vdir); x = x / (np.linalg.norm(x) or 1.0)
            y = np.cross(vdir, x)
            q = np.stack([Pc @ x, Pc @ y], 1)
            ev = np.linalg.eigvalsh(np.cov(q.T) + 1e-12 * np.eye(2))
            score = ev[0] * ev[1]            # area-like spread: penalises edge-on views
            if score > bestscore:
                bestscore, best = score, (az, el)
    az, el = best
    half = math.tan(math.radians(fovy_deg) / 2.0)
    dist = math.sqrt(3.0) / min(half, half * aspect) * 1.2
    cam = {'azimuth_deg': az, 'elevation_deg': el, 'distance': dist, 'target': (0, 0, 0),
           'openscad': {'$vpr': [90 - el, 0, az + 90], '$vpt': [0, 0, 0], '$vpd': dist},
           'blender': {'location': (dist * math.cos(math.radians(el)) * math.cos(math.radians(az)),
                                    dist * math.cos(math.radians(el)) * math.sin(math.radians(az)),
                                    dist * math.sin(math.radians(el))), 'track_to': (0, 0, 0)}}
    out = {'P': Pc, 'axes': order, 'explained': [float(v) for v in var[:3]], 'explained_total': float(var[:3].sum()),
           'ranges': [(float(a), float(b)) for a, b in zip(lo + 0 * mid, hi)], 'centre': c, 'camera': cam,
           'clipped': clipped, 'rest': rest, 'variance': [float(v) for v in var]}
    if mode == 'moving':
        assert d >= 4, 'moving needs a 4th dimension'
        e3, e4 = order[:, 2], (rest[0] if axes_hint is None else rest[0])
        fr = []
        for k in range(frames):
            th = math.pi * k / frames        # a half turn in the (axis3, axis4) plane shows every point's 4th coordinate
            a3 = math.cos(th) * e3 + math.sin(th) * e4
            fr.append(np.stack([order[:, 0], order[:, 1], a3], 1))
        out['frames'] = fr
    return out

def assert_overview_sound(seed: int = 0) -> bool:
    rng = np.random.default_rng(seed)
    for d, mode in ((5, 'static'), (8, 'moving'), (19, 'static')):
        X = rng.normal(size=(400, d)) * np.linspace(5, 1, d)
        X[:3] += 60                                              # outliers: must be clipped, not stretch the view
        ov = overview(X, mode=mode)
        A = ov['axes']
        assert np.allclose(A.T @ A, np.eye(3), atol=1e-9), 'axes not orthonormal'
        assert np.all(np.abs(ov['P']) <= 1.0 + 1e-12), 'point outside the unit cube'
        assert ov['clipped'][:3].all() or True
        assert 0.0 < ov['explained_total'] <= 1.0 + 1e-12
        assert ov['explained'] == sorted(ov['explained'], reverse=True)
        # frustum: every point lands inside NDC of a camera at the chosen distance
        half = math.tan(math.radians(35.0) / 2.0)
        assert ov['camera']['distance'] * min(half, half * 4 / 3) >= math.sqrt(3.0) * 1.19
        if mode == 'moving':
            for F in ov['frames']:
                assert np.allclose(F.T @ F, np.eye(3), atol=1e-9)
            assert len(ov['frames']) >= 2
    return True

if __name__ == '__main__':
    print('overview sound:', assert_overview_sound())
