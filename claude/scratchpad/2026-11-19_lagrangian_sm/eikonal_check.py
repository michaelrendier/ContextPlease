"""Is the path of action defined by the hat's values?  Build W(q) ONLY from shot rays (S + E t), then test |grad W|^2 = 2(E - V(q)) and that each ray's velocity is parallel to grad W.
    PYTHONPATH=~/Projects/ThePlace ~/Projects/ThePlace/ValaQuenta/.venv/bin/python eikonal_check.py      (2026-11-19: median relative error 0.014 %, median angle 0.003 deg)"""
import numpy as np, math
from scipy.interpolate import griddata, RegularGridInterpolator
from ValaQuenta.modules.witches_hat import action as A, maths as M
SM = M.lagrangian_sm(mu2=1.0, lam=1.0); E = 0.0; V = lambda x, y: -0.5*(x*x + y*y) + 0.25*(x*x + y*y)**2
fam = A.ray_family(SM, (1.0, 0.0), E=E, n_theta=361, t_max=1.2, n_t=150); Q = fam["q"].reshape(-1, 2); Wv = fam["W"].reshape(-1); D = fam["D"]; V3 = fam["v"].reshape(-1, 2)
ok = np.ones_like(D, bool)
for i in range(D.shape[0]):                                  # keep the pre-caustic part of each ray, where W is single valued
    s = np.sign(D[i, 1:]); ch = np.where(s[1:]*s[:-1] < 0)[0]
    if len(ch): ok[i, ch[0] + 2:] = False
m = ok.reshape(-1) & (np.hypot(Q[:, 0], Q[:, 1]) < 1.35); Qm, Wm, Vm = Q[m], Wv[m], V3[m]
xs = np.linspace(0.2, 1.3, 160); ys = np.linspace(-0.8, 0.8, 160); X, Y = np.meshgrid(xs, ys); Wg = griddata(Qm, Wm, (X, Y), method="cubic"); gy, gx = np.gradient(Wg, ys, xs)
g2 = gx**2 + gy**2; rhs = 2*(E - V(X, Y)); core = np.isfinite(g2) & (rhs > 0.05) & (np.hypot(X - 1, Y) > 0.15) & (np.hypot(X - 1, Y) < 0.9); rel = np.abs(g2[core] - rhs[core])/rhs[core]
print("eikonal: n=%d median relative error %.3f%% 90th percentile %.2f%%" % (core.sum(), 100*np.median(rel), 100*np.percentile(rel, 90)))
fx = RegularGridInterpolator((ys, xs), gx, bounds_error=False, fill_value=np.nan); fy = RegularGridInterpolator((ys, xs), gy, bounds_error=False, fill_value=np.nan)
pts = np.stack([Qm[:, 1], Qm[:, 0]], 1); gxv, gyv = fx(pts), fy(pts); d = np.hypot(Qm[:, 0] - 1, Qm[:, 1]); good = np.isfinite(gxv) & np.isfinite(gyv) & (d > 0.2) & (d < 0.9) & (np.hypot(Vm[:, 0], Vm[:, 1]) > 1e-3)
c = (Vm[good, 0]*gxv[good] + Vm[good, 1]*gyv[good])/(np.hypot(Vm[good, 0], Vm[good, 1])*np.hypot(gxv[good], gyv[good])); ang = np.degrees(np.arccos(np.clip(c, -1, 1)))
print("velocity vs grad W: median %.3f deg, 90th percentile %.3f deg (n=%d)" % (np.median(ang), np.percentile(ang, 90), good.sum()))
