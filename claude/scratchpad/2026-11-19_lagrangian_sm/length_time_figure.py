"""Figure for Ainulindale wiki 140: length and time as one thing, and the swap.  Writes Ainulindale/wiki/images/140_length_time.svg.
    PYTHONPATH=~/Projects/ThePlace ~/Projects/ThePlace/ValaQuenta/.venv/bin/python length_time_figure.py"""
import math, os
import numpy as np
import matplotlib; matplotlib.use("svg")
import matplotlib.pyplot as plt
from ValaQuenta.modules.witches_hat import length_time as LT, maths as M
plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans"})
BG, PANEL, FG, MUTED, GOLD = "#0b1220", "#0f1a2e", "#e6edf3", "#8b98a9", "#f2cc60"
SM = M.lagrangian_sm(mu2=1.0, lam=1.0); V = lambda r: -0.5*r*r + 0.25*r**4
fig, ax = plt.subplots(2, 2, figsize=(15, 12), facecolor=BG)
for a in ax.ravel():
    a.set_facecolor(PANEL); [s.set_color("#1f2c44") for s in a.spines.values()]; a.tick_params(colors=MUTED); a.xaxis.label.set_color(FG); a.yaxis.label.set_color(FG); a.title.set_color(FG)
# 1 speed field and the signature
a = ax[0, 0]; r = np.linspace(0, 2.0, 600)
for E, c in ((0.0, "#5ce1e6"), (0.05, "#fff4b8")):
    v2 = 2*(E - V(r)); a.plot(r, np.sqrt(np.maximum(v2, 0)), color=c, lw=2.4, label="E = %.2f: v = √(2(E − V))" % E)
a.axvspan(math.sqrt(2), 2.0, color="#8b3fa8", alpha=0.25); a.text(1.62, 0.12, "forbidden: v² < 0\nEuclidean signature\n(time is imaginary)", color="#d2a8ff", fontsize=10)
a.text(0.05, 0.62, "allowed: v² > 0\nLorentzian optical metric", color=MUTED, fontsize=10); a.axvline(1, color=GOLD, ls="--", lw=1.4); a.axvline(math.sqrt(2), color="white", lw=1.0)
a.set_xlabel("radius r / R   (gold: brim; white: the turning circle r = √2 at E = 0)"); a.set_ylabel("speed v = the conversion of length into time"); a.set_title("The hat is the conversion field: length = v · time", fontsize=12); a.legend(facecolor=PANEL, edgecolor="#1f2c44", labelcolor=FG, fontsize=9)
# 2 (rho, t): the 45-degree lines
a = ax[0, 1]; E = 0.05; rho1 = LT.tortoise(SM, E, 1.0); rt = LT.wall_transit(SM, E); rho_t = rho1 + rt["rho_brim_to_wall"]
def zigzag(start, direction, T, lo, hi):
    ts = [0.0]; xs = [start]; t = 0.0; x = start; d = direction
    while t < T:
        step = ((hi - x) if d > 0 else (x - lo)); step = min(step, T - t); x += d*step; t += step; ts.append(t); xs.append(x); d = -d
    return np.array(xs), np.array(ts)
xs, ts = zigzag(rho1, -1, 14.0, -rho_t, rho_t); a.plot(xs, ts, color="#fff4b8", lw=2.2, label="E = 0.05: bounces between walls at ρ = ±%.3f" % rho_t)
for off in (-1.5, 0.7): x2, t2 = zigzag(off, 1, 14.0, -rho_t, rho_t); a.plot(x2, t2, color="#5ce1e6", lw=1.0, alpha=0.7)
a.axvline(rho_t, color="white", lw=1.2); a.axvline(-rho_t, color="white", lw=1.2); a.axvline(0, color=MUTED, lw=0.8, ls=":")
a.set_xlabel("ρ = ∫dr/v : length measured in transit time"); a.set_ylabel("time t"); a.set_title("In the transit ruler every radial path is a 45° line: the potential has become the ruler", fontsize=11); a.legend(facecolor=PANEL, edgecolor="#1f2c44", labelcolor=FG, fontsize=9, loc="lower right")
# 3 Penrose compactification of the same lines
a = ax[1, 0]
def comp(rr, tt): U = np.arctan(tt - rr); Vv = np.arctan(tt + rr); return (Vv - U)/2, (Vv + U)/2
for x_, t_ in ((xs, ts),):
    n = 400; xi = np.concatenate([np.linspace(x_[i], x_[i + 1], n) for i in range(len(x_) - 1)]); ti = np.concatenate([np.linspace(t_[i], t_[i + 1], n) for i in range(len(x_) - 1)]); X, T = comp(xi, ti); a.plot(X, T, color="#fff4b8", lw=2.2, label="E = 0.05, compactified: U = arctan(t − ρ), V = arctan(t + ρ)")
for k, off in enumerate((-1.5, 0.7)):
    x2, t2 = zigzag(off, 1, 14.0, -rho_t, rho_t); xi = np.concatenate([np.linspace(x2[i], x2[i + 1], 200) for i in range(len(x2) - 1)]); ti = np.concatenate([np.linspace(t2[i], t2[i + 1], 200) for i in range(len(x2) - 1)]); X, T = comp(xi, ti); a.plot(X, T, color="#5ce1e6", lw=0.9, alpha=0.7)
for sgn in (-1, 1): a.axvline(sgn*(math.atan(rho_t)), color="white", lw=1.0)
# E = 0: the hilltop at rho = -infinity: i+ point
tt = np.linspace(0, 60, 2000); X, T = comp(-tt, tt); a.plot(X, T, color="#ff7b72", lw=2.0, label="E = 0: inward path, ρ = −t: reaches the hilltop only at t = ∞ (a point on the boundary)")
a.scatter([comp(np.array([-1e9]), np.array([1e9]))[0][0]], [comp(np.array([-1e9]), np.array([1e9]))[1][0]], color="#ff7b72", s=60, zorder=5)
a.set_xlabel("compactified length"); a.set_ylabel("compactified time"); a.set_title("Penrose compactification of the same lines: finite diagram, infinity on the boundary", fontsize=11); a.legend(facecolor=PANEL, edgecolor="#1f2c44", labelcolor=FG, fontsize=8, loc="lower left")
# 4 two rulers
a = ax[1, 1]; rr = LT.two_rulers(SM, (1.0, 0.0), (-0.6, 0.8), 0.05, N=100)
th = np.linspace(0, 2*math.pi, 300); a.plot(np.cos(th), np.sin(th), color=GOLD, lw=2.0, label="the brim"); a.plot([0], [0], "o", color="white", ms=5)
rv = np.sqrt(1 + math.sqrt(1 + 4*0.05*4))/1.0
a.plot(rr["action_path"][:, 0], rr["action_path"][:, 1], color="#5ce1e6", lw=2.6, label="least ACTION (what the particle does): T = %.3f, W = %.3f" % (rr["T_of_action_path"], rr["W_of_action_path"]))
a.plot(rr["time_path"][:, 0], rr["time_path"][:, 1], color="#ff7b72", lw=2.6, label="least TIME (Fermat): T = %.3f, W = %.3f" % (rr["T_min"], rr["W_of_time_path"]))
a.plot([1.0, -0.6], [0.0, 0.8], color=MUTED, lw=1.0, ls=":", label="straight line (the two coincide only if v is constant)"); a.set_aspect("equal"); a.set_xlim(-1.3, 1.3); a.set_ylim(-1.1, 1.1)
a.set_title("Two rulers: least action weights length by v, least time by 1/v (time differs by %.0f %%)" % (100*rr["split"]), fontsize=10); a.legend(facecolor=PANEL, edgecolor="#1f2c44", labelcolor=FG, fontsize=8, loc="lower center")
fig.suptitle("Length and time as one thing, and the swap (Ainulindale wiki 140)", color=FG, fontsize=17, fontweight="bold", y=0.995); fig.tight_layout(rect=(0, 0, 1, 0.97))
out = os.path.expanduser("~/Projects/ThePlace/Ainulindale/wiki/images/140_length_time.svg"); fig.savefig(out, facecolor=BG); print("wrote", out)
