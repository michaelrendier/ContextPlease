"""Every anomaly met while building the L_SM engine and the path-of-action tools (2026-11-19), chased to its source.  Run with the ValaQuenta venv:
    PYTHONPATH=~/Projects/ThePlace ~/Projects/ThePlace/ValaQuenta/.venv/bin/python anomaly_chase.py
Each section prints the measurement that explains one oddity."""
import math, numpy as np
from scipy import integrate
from ValaQuenta.modules.lagrangian_sm import maths as S, compare as C
from ValaQuenta.modules.witches_hat import action as A, maths as M

print("1. SM anomaly cancellation: SU(5) embedding"); print("  ", S.su5_embedding())
print("2. hypercharges and N_c"); [print("  N_c=%d" % n, S.hypercharges_from_anomalies(n)["charges"]) for n in (1, 2, 3, 4, 5)]
alpha0 = 1/137.035999; GF = S.INPUTS["G_F"][0]; mW = S.pdg_mass("W+")[0]; mZ = S.pdg_mass("Z0")[0]
A0 = math.pi*alpha0/(math.sqrt(2)*GF); s2 = 1 - mW**2/mZ**2
print("3. tree m_W, m_Z offsets: on-shell sin2=%.5f, Delta r=%.4f (literature ~0.036)" % (s2, 1 - A0/(mW**2*s2)))
print("4. one-loop lambda->0 scale vs y_t(M_Z): see notebook 25 (none below 1e19 at 0.92; 1.7e5 GeV at 1.00)")
print("5. coded L_NN vs SM:"); [print("  ", k, v) for k, v in C.measured_exponents().items()]
print("  seagull:", C.seagull_correspondence(), "| 1/phi applied:", C.one_over_phi_on_bias()["applied"], "| bias conventions:", C.bias_conventions())
def harm(w): return {"model": "h", "V2": lambda x, y: 0.5*w*w*(np.asarray(x, float)**2 + np.asarray(y, float)**2), "grad": lambda x, y: (w*w*np.asarray(x, float), w*w*np.asarray(y, float)), "brim_radius": 1.0}
P, Q = (1.0, 0.0), (0.3, 0.4); T = 1.1*math.pi; cl = 1/(2*math.sin(T))*(1.25*math.cos(T) - 0.6)
print("6. discretisation error vs N:", [round(abs(A.stationary_paths(harm(1.0), P, Q, T, N=N)[0]["S"] - cl), 6) for N in (50, 100, 200, 400)], "(ratio 4 each doubling)")
SM = M.lagrangian_sm(mu2=1.0, lam=1.0)
fam = A.ray_family(SM, (1.0, 0.0), E=0.0, n_theta=9, t_max=2.0, n_t=201); B = fam["q"][2, 200]; ps = A.stationary_paths(SM, (1.0, 0.0), B, fam["t"][200], N=200)
print("7. three stationary paths between two events on the hat:", [(round(p["S"], 6), p["index"]) for p in ps], " shot ray S =", round(fam["S"][2, 200], 6))
print("8. Euclidean tau, r0=0.5:", A.euclidean_radial_release(SM, 0.5)["tau"], "(mpmath 1.744581748021)")
r = A.moving_hat_exchange(SM, (1.0, 0.0), (0.0, 0.7), (0.6, 0.0), 20.0); print("9. moving hat: dE_final %.4f, max excursion %.4f, identity residual %.1e" % (r["dE_final"], r["dE_max_excursion"], r["identity_residual"]))
