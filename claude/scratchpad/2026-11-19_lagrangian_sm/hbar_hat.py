"""Reproduces the numbers of Ainulindale wiki 141 (hbar from the hat).
    PYTHONPATH=~/Projects/ThePlace ~/Projects/ThePlace/ValaQuenta/.venv/bin/python hbar_hat.py"""
from ValaQuenta.modules.witches_hat import maths as M, semiclassical as SC
SM = M.lagrangian_sm(mu2=1.0, lam=1.0); a = SC.separatrix_actions(SM)
print({k: round(v, 6) for k, v in a.items() if k != "checks"}); print("quadrature checks:", {k: round(v, 9) for k, v in a["checks"].items()})
th = SC.exact_thresholds(SM, n_states=6, h_lo=0.03, n_grid=900); print("thresholds:", [round(h, 5) for h in th]); print("gamma_n:", [round(g, 4) for g in SC.offset_gamma(SM, th)])
for h in (0.30, 0.20, 0.14, 0.10): print("hbar %.2f: exact 2D count %d, Weyl %.2f" % (h, SC.exact_count_2d(SM, h), SC.weyl_count(SM, h)))
import math; W = a["W_wall"]; print("untested sheet-interference ladder hbar_k = W_wall/(pi(k+1/4)):", [round(W/(math.pi*(k + 0.25)), 4) for k in range(3)])
