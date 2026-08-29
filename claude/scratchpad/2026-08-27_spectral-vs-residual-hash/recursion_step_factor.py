#!/usr/bin/env python3
"""
recursion_step_factor.py

Two recursions over synset context-vectors, in the LOG CHART (v_i * ln p_i).

  R1  ADD recursion   (PW3 sum)        Iterator = componentwise ADD (translation)
                                       -- no circle, expect central-limit drift
  R2  MOBIUS recursion                 Iterator = Z <- tanh( 0.5 * ln(Z / Z_next) )
                                       -- rotates; watch for fixed point vs
                                       period-q lock (Arnold tongue) vs torus

step factor  = per-step change in the tracked stable-law parameter (R1)
             = per-step complex map behaviour (R2)
recursion factor = how many steps (n)

Question: does the step factor hold CONSTANT (rational, reducible, no new
generator) or DRIFT/BIFURCATE (irrational rotation number -> torus -> a
genuinely new generator at this order)?
"""
import sys, math, cmath, random
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP")
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
import numpy as np
from wordnet_boxkite import context_vector, RELATION_METHODS, CONTEXT_PRIMES
from nltk.corpus import wordnet as wn

random.seed(20260827); np.random.seed(20260827)
LNP = np.array([math.log(p) for p in CONTEXT_PRIMES[:len(RELATION_METHODS)]])


def hill(x, frac=0.08):
    x = np.sort(np.abs(np.asarray(x, float)))[::-1]; x = x[x > 0]
    if len(x) < 30:
        return float("nan")
    k = max(15, int(len(x) * frac)); k = min(k, len(x) - 1)
    return 1.0 / np.mean(np.log(x[:k] / x[k]))


# ---- corpus of log-chart vectors -------------------------------------------
S = list(wn.all_synsets()); random.shuffle(S)
L = []
for syn in S:
    v = np.array(context_vector(syn), float)
    if v.sum() == 0:
        continue
    L.append(v * LNP)
    if len(L) >= 6000:
        break
L = np.array(L)
d = L.shape[1]
print(f"corpus: {len(L)} log-chart vectors x {d} dims\n")

# ==========================================================================
# R1  ADD recursion  -- track alpha of the heaviest component vs step n
# ==========================================================================
print("=" * 74)
print("R1  ADD recursion (PW3 sum, log chart) -- alpha of heaviest component")
print("=" * 74)
NREP = 4000
maxn = 40
# running sums: acc[rep] += random vector each step
acc = np.zeros((NREP, d))
idx_stream = np.random.randint(0, len(L), size=(maxn, NREP))
alpha_by_n = []
for n in range(1, maxn + 1):
    acc += L[idx_stream[n - 1]]
    # per-component alpha across the NREP running sums; take the min (heaviest)
    acol = [hill(acc[:, j]) for j in range(d)]
    acol = [a for a in acol if not math.isnan(a)]
    alpha_by_n.append(min(acol))
alpha_by_n = np.array(alpha_by_n)
d1 = np.diff(alpha_by_n)              # step factor
d2 = np.diff(d1)                      # change in step factor
print(f"  n :  1   2   3   5   8   13   21   34")
pick = [1, 2, 3, 5, 8, 13, 21, 34]
print(f"  a : " + " ".join(f"{alpha_by_n[i-1]:4.2f}" for i in pick))
print(f"\n  step factor  Delta-alpha : mean={d1.mean():+.4f}  std={d1.std():.4f}")
print(f"  2nd diff (is step factor constant?) : mean={d2.mean():+.5f}  "
      f"std={d2.std():.5f}  max|.|={np.abs(d2).max():.4f}")
# fit alpha(n) ~ a + b*sqrt(n)  (pure central limit) and ~ a+b*n (linear)
nn = np.arange(1, maxn + 1)
for name, basis in [("a+b*sqrt(n)", np.sqrt(nn)), ("a+b*n", nn),
                    ("a+b*ln(n)", np.log(nn))]:
    A = np.column_stack([np.ones_like(basis), basis])
    coef, resid, *_ = np.linalg.lstsq(A, alpha_by_n, rcond=None)
    pred = A @ coef
    r2 = 1 - np.sum((alpha_by_n - pred) ** 2) / np.sum((alpha_by_n - alpha_by_n.mean()) ** 2)
    print(f"    fit {name:12s}  R^2={r2:.4f}  coef={coef}")

# ==========================================================================
# R2  MOBIUS recursion -- rotation number of the tracked complex coordinate
# ==========================================================================
print("\n" + "=" * 74)
print("R2  MOBIUS recursion  Z <- tanh(0.5*ln(Z/Z_next))  -- rotation number")
print("=" * 74)


def cpairs(vec):
    m = (len(vec) // 2) * 2
    return vec[:m:2] + 1j * vec[1:m:2]


NSTEPS = 400
NIC = 24
rho_list, dtheta_std_list, converge_list, closed_list = [], [], [], []
for ic in range(NIC):
    z0 = cpairs(L[np.random.randint(len(L))]).astype(complex)
    z0 = z0 + (z0 == 0) * (1e-6 + 1e-6j)
    z = z0.copy()
    stream = L[np.random.randint(0, len(L), size=NSTEPS)]
    track = np.zeros(NSTEPS, complex)
    for t in range(NSTEPS):
        zn = cpairs(stream[t]).astype(complex)
        zn = zn + (zn == 0) * (1e-6 + 1e-6j)
        ratio = np.where(np.abs(zn) > 1e-12, z / zn, z)
        z = np.tanh(0.5 * np.log(ratio))
        track[t] = z[0]
    tail = track[NSTEPS // 2:]
    theta = np.unwrap(np.angle(tail))
    dtheta = np.diff(theta)
    rho = np.mean(dtheta) / (2 * math.pi)           # rotation number
    rho_list.append(rho)
    dtheta_std_list.append(np.std(dtheta))
    # converged to a fixed point?
    converge_list.append(np.mean(np.abs(np.diff(tail[-40:]))))
    # orbit closes? (min distance of last point to an earlier one)
    dists = np.abs(tail[-1] - tail[:-1])
    closed_list.append(dists.min() / (np.abs(tail).mean() + 1e-12))

rho_arr = np.array(rho_list)
print(f"  rotation number rho over {NIC} initial conditions:")
print(f"    mean={rho_arr.mean():+.4f}  std={rho_arr.std():.4f}  "
      f"range=({rho_arr.min():+.3f}, {rho_arr.max():+.3f})")


def nearest_rational(x, maxq=12):
    best = (1e9, 0, 1)
    for q in range(1, maxq + 1):
        p = round(x * q)
        err = abs(x - p / q)
        if err < best[0]:
            best = (err, p, q)
    return best


err, p, q = nearest_rational(rho_arr.mean())
print(f"    nearest low-order rational: {p}/{q}  (err {err:.4f})")
print(f"  mean |Delta-theta| step std   : {np.mean(dtheta_std_list):.4f}   "
      f"(low => mode-locked / Arnold tongue; high => torus/chaos)")
print(f"  mean fixed-point residual     : {np.mean(converge_list):.2e}   "
      f"(~0 => converged to a fixed point)")
print(f"  mean orbit-closure ratio      : {np.mean(closed_list):.3f}   "
      f"(~0 => closed periodic orbit; O(1) => does not close => torus)")

print("\n" + "-" * 74)
print("READ:")
print("  R1 step factor constant?  -> 2nd-diff std vs step-factor std above.")
print("  R2 fixed point / period-q lock / torus -> the three R2 lines.")
