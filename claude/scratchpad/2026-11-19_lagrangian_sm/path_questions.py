"""Measurements behind wiki 139 section 11: the moving-hat path, a rotating hat, the three SM stationary paths, the L_NN flow against the tilt, the action cone.
    PYTHONPATH=~/Projects/ThePlace ~/Projects/ThePlace/ValaQuenta/.venv/bin/python path_questions.py"""
import numpy as np, math
from scipy import integrate
from ValaQuenta.modules.witches_hat import action as A, maths as M
SM = M.lagrangian_sm(mu2=1.0, lam=1.0); V = lambda x, y: -0.5*(x*x + y*y) + 0.25*(x*x + y*y)**2
u = np.array([0.25, 0.0]); T = 8.0
def rhs(t, y):
    c = u*t; x = y[0] - c[0]; yy = y[1] - c[1]; f = -1 + x*x + yy*yy; return [y[2], y[3], -f*x, -f*yy]
s = integrate.solve_ivp(rhs, (0, T), [1.0, 0.0, 0.0, 0.7], t_eval=np.linspace(0, T, 2000), rtol=1e-11, atol=1e-13, method="DOP853")
q = s.y[:2].T; v = s.y[2:].T; t = s.t; rel = q - np.outer(t, u); Ec = 0.5*((v - u)**2).sum(1) + V(rel[:, 0], rel[:, 1])
print("(a) hat-frame energy drift %.1e ; lab dE %.4f = u.(v-v0) %.4f ; max distance from hat centre %.3f" % (np.abs(Ec - Ec[0]).max(), (0.5*(v**2).sum(1) + V(rel[:, 0], rel[:, 1]))[-1] - (0.5*(v**2).sum(1) + V(rel[:, 0], rel[:, 1]))[0], u@(v[-1] - v[0]), np.hypot(rel[:, 0], rel[:, 1]).max()))
def run(om, tilt=0.15, T=40.0):
    def f(t, y):
        x, yy = y[0], y[1]; g = -1 + x*x + yy*yy; c, s_ = math.cos(om*t), math.sin(om*t); return [y[2], y[3], -(g*x + tilt*c), -(g*yy + tilt*s_)]
    s = integrate.solve_ivp(f, (0, T), [1.0, 0.0, 0.0, 0.7], t_eval=np.linspace(0, T, 4000), rtol=1e-10, atol=1e-12, method="DOP853")
    x, yy = s.y[0], s.y[1]; E = 0.5*(s.y[2]**2 + s.y[3]**2) + V(x, yy) + tilt*(x*np.cos(om*s.t) + yy*np.sin(om*s.t)); return E - E[0]
print("(b) rotating tilt, dE_final by omega:", {om: round(float(run(om)[-1]), 3) for om in (0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 2.0, 3.0)})
fam = A.ray_family(SM, (1.0, 0.0), E=0.0, n_theta=9, t_max=2.0, n_t=201); B = fam["q"][2, 200]; Tt = fam["t"][200]
for p in A.stationary_paths(SM, (1.0, 0.0), B, Tt, N=200):
    qq = p["q"]; dt = Tt/200; sp = np.hypot(*(np.diff(qq, axis=0)/dt).T); rr = np.hypot(qq[:, 0], qq[:, 1])
    print("(c) index %d S=%.4f length=%.2f vmax=%.2f r_min=%.3f r_max=%.2f" % (p["index"], p["S"], sp.sum()*dt, sp.max(), rr.min(), rr.max()))
for g in (0.0, 0.05, 0.1, 0.2, 0.4):
    vap = M.lagrangian_vap(mu_sq=-1.0, lam=0.5, g=g, psi=(1.0, 0.0), convention="ssb"); R = vap["brim_radius"]; top = M.hilltop(vap); dev = []
    for k in range(12):
        a = 2*math.pi*k/12; st = np.array([R*math.cos(a), R*math.sin(a)]); p = M.trace_plane(vap, tuple(st), top, 0.0, float(vap["V2"](*top)))
        P = np.stack([p["x"], p["y"]], 1); d = top - st; d /= np.linalg.norm(d); rl = P - st; dev.append(np.abs(rl[:, 0]*d[1] - rl[:, 1]*d[0]).max()/R)
    print("(d) g=%.2f hilltop shift %.3f R, max path deviation from straight %.3f R" % (g, np.hypot(*top)/R, max(dev)))
for E in (0.0, 0.02, 0.1):
    r = np.linspace(1, 0, 400); p = np.sqrt(np.maximum(2*(E - V(r, 0*r)), 0)); W = np.concatenate([[0], np.cumsum(0.5*(p[1:] + p[:-1])*np.abs(np.diff(r)))])
    print("(e) E=%.2f action-cone apex W(0)=%.4f tip slope = momentum %.3f" % (E, W[-1], math.sqrt(2*E)))
print("(e) L_(I|O) along a straight spoke: integral J_red J_blue ds = exp(-E) s : a straight cone of slope exp(-E) = %.4f at E = 1" % math.exp(-1))
