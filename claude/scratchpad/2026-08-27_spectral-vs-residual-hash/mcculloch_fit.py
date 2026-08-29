#!/usr/bin/env python3
"""
mcculloch_fit.py -- proper stable-law (alpha-stable) parameter fit via the
McCulloch (1986) quantile estimator, as implemented in
scipy.stats.levy_stable._fitstart.

Two jobs:
  J1  LINEAGE  -- McCulloch alpha,beta at each generation G0..G5, replacing
                  the noisy Hill numbers from lineage_anomaly.py.
  J2  RECURSION -- McCulloch alpha(n),beta(n) for the ADD recursion (PW3 sum,
                  log chart), on the heaviest fixed component and on the
                  mode0 / residual projections. Does alpha -> 2 (the
                  Mingling / critical line) and hold?

Cross-checked against a proper Hill plot (median over k in [2%,15%]).
"""
import sys, math, random
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP")
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
import numpy as np
from scipy.stats import levy_stable
from wordnet_boxkite import context_vector, RELATION_METHODS, CONTEXT_PRIMES, compress_count
from nltk.corpus import wordnet as wn

random.seed(20260827); np.random.seed(20260827)
LNP = np.array([math.log(p) for p in CONTEXT_PRIMES[:len(RELATION_METHODS)]])


def mcculloch(x):
    """(alpha, beta, loc, scale) via McCulloch quantile estimator."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if len(x) < 200 or np.allclose(x, x[0]):
        return (float("nan"),) * 4
    try:
        a, b, loc, sc = levy_stable._fitstart(x)
        return float(a), float(b), float(loc), float(sc)
    except Exception:
        return (float("nan"),) * 4


def hill_median(x):
    x = np.sort(np.abs(np.asarray(x, float)))[::-1]
    x = x[x > 0]
    if len(x) < 100:
        return float("nan")
    est = []
    for frac in np.linspace(0.02, 0.15, 14):
        k = max(15, int(len(x) * frac)); k = min(k, len(x) - 1)
        est.append(1.0 / np.mean(np.log(x[:k] / x[k])))
    return float(np.median(est))


# ============================ corpus ======================================
S = list(wn.all_synsets()); random.shuffle(S)
raw, cmp_ = [], []
for syn in S:
    counts = []
    for m in RELATION_METHODS:
        try:
            counts.append(len(getattr(syn, m)()))
        except Exception:
            counts.append(0)
    if sum(counts) == 0:
        continue
    raw.append(counts)
    cmp_.append([compress_count(c) for c in counts])
    if len(raw) >= 8000:
        break
R = np.array(raw, float)
C = np.array(cmp_, float)
Clog = C * LNP
n, d = C.shape
print(f"corpus {n} synsets x {d} dims\n")

# ============================ J1  LINEAGE =================================
print("=" * 78)
print("J1  LINEAGE  --  McCulloch alpha (Hill in parens) per generation")
print("=" * 78)


def gen_report(tag, M):
    als, bes, hills = [], [], []
    for j in range(M.shape[1]):
        a, b, _, _ = mcculloch(M[:, j])
        if not math.isnan(a):
            als.append(a); bes.append(b); hills.append(hill_median(M[:, j]))
    if not als:
        print(f"  {tag:32s}  (all columns degenerate)")
        return
    als = np.array(als)
    j_min = int(np.argmin(als))
    print(f"  {tag:32s}  alpha: min={als.min():4.2f}  med={np.median(als):4.2f}  "
          f"max={als.max():4.2f}   #(a<2)={int((als<2).sum())}/{len(als)}   "
          f"|beta|@min={abs(bes[j_min]):.2f}  Hill@min={hills[j_min]:.2f}")


gen_report("G0 raw counts", R)
Rlog = np.log1p(R)  # what compress_count approximates
gen_report("G0' log1p(raw)  (smooth compress)", Rlog)
gen_report("G1 compress_count", C)
gen_report("G1log v_i*ln p_i (log chart)", Clog)
Mc = C - C.mean(0)
gen_report("G3 mean-centred", Mc)
Mclog = Clog - Clog.mean(0)
gen_report("G3log centred log-chart", Mclog)
U, sv, Vt = np.linalg.svd(Mc, full_matrices=False)
res1 = Mc - (U[:, :1] * sv[:1]) @ Vt[:1]
gen_report("G5 residual after mode0", res1)
Ul, svl, Vtl = np.linalg.svd(Mclog, full_matrices=False)
res1l = Mclog - (Ul[:, :1] * svl[:1]) @ Vtl[:1]
gen_report("G5log residual (log chart)", res1l)

# single scalars: log(context_code), and mode0 / residual projections
lcode = C @ LNP
a, b, _, _ = mcculloch(lcode)
print(f"\n  log(context_code)=sum v_i ln p_i   alpha={a:.2f}  beta={b:+.2f}  "
      f"Hill={hill_median(lcode):.2f}")
proj0 = U[:, 0] * sv[0]
a, b, _, _ = mcculloch(proj0)
print(f"  mode0 projection                   alpha={a:.2f}  beta={b:+.2f}  "
      f"Hill={hill_median(proj0):.2f}")
projr = np.linalg.norm(res1, axis=1)
a, b, _, _ = mcculloch(projr)
print(f"  residual magnitude                 alpha={a:.2f}  beta={b:+.2f}  "
      f"Hill={hill_median(projr):.2f}")

# ============================ J2  RECURSION ==============================
print("\n" + "=" * 78)
print("J2  ADD recursion (PW3 sum, log chart) -- McCulloch alpha(n), beta(n)")
print("=" * 78)
NREP = 6000
# pick the fixed heaviest component at n=1 (by McCulloch alpha on single vecs)
base_al = [mcculloch(Clog[:, j])[0] for j in range(d)]
jheavy = int(np.nanargmin(base_al))
print(f"  heaviest component at n=1: '{RELATION_METHODS[jheavy]}'  "
      f"(alpha={base_al[jheavy]:.2f})\n")

maxn = 55
idx_stream = np.random.randint(0, n, size=(maxn, NREP))
acc = np.zeros((NREP, d))
# also track mode0/residual coords of the running sum shape
rows = []
for step in range(1, maxn + 1):
    acc += Clog[idx_stream[step - 1]]
    xh = acc[:, jheavy]
    ah, bh, _, _ = mcculloch(xh)
    # residual-after-mode0 of the accumulated shapes at this step
    Ac = acc - acc.mean(0)
    uu, ss, vv = np.linalg.svd(Ac, full_matrices=False)
    r = Ac - (uu[:, :1] * ss[:1]) @ vv[:1]
    rh = r[:, jheavy]
    ar, br, _, _ = mcculloch(rh)
    am, bm, _, _ = mcculloch((uu[:, 0] * ss[0]))
    rows.append((step, ah, bh, ar, am, hill_median(xh)))

print(f"   n |  alpha_h  beta_h | alpha_resid | alpha_mode0 | Hill_h")
print(f"  ---+-----------------+-------------+-------------+-------")
for (step, ah, bh, ar, am, hh) in rows:
    if step in (1, 2, 3, 4, 5, 6, 8, 10, 13, 17, 21, 28, 34, 42, 55):
        print(f"  {step:3d}|  {ah:5.2f}   {bh:+5.2f} |   {ar:5.2f}     |   {am:5.2f}     | {hh:5.2f}")

al_h = np.array([r[1] for r in rows])
d1 = np.diff(al_h)
print(f"\n  alpha_h:  start={al_h[0]:.2f}  end={al_h[-1]:.2f}  "
      f"mean={np.nanmean(al_h):.2f}  std={np.nanstd(al_h):.3f}")
print(f"  step factor  Delta-alpha_h : mean={np.nanmean(d1):+.4f}  "
      f"std={np.nanstd(d1):.4f}")
# is it pinned at 2? one-sample: fraction within 0.15 of 2.0
within = np.mean(np.abs(al_h - 2.0) < 0.15)
print(f"  fraction of steps with |alpha_h - 2.0| < 0.15 : {within:.2f}")
# trend fits
nn = np.arange(1, maxn + 1)
for name, basis in [("const", np.zeros_like(nn, float)),
                    ("a+b*n", nn.astype(float)),
                    ("a+b*ln n", np.log(nn))]:
    if name == "const":
        pred = np.full_like(al_h, np.nanmean(al_h))
    else:
        A = np.column_stack([np.ones_like(basis, float), basis])
        m = np.isfinite(al_h)
        coef, *_ = np.linalg.lstsq(A[m], al_h[m], rcond=None)
        pred = A @ coef
    m = np.isfinite(al_h)
    ss_res = np.sum((al_h[m] - pred[m]) ** 2)
    ss_tot = np.sum((al_h[m] - np.nanmean(al_h)) ** 2) or 1.0
    print(f"    fit {name:9s} R^2={1 - ss_res/ss_tot:+.3f}"
          + ("" if name == "const" else f"  coef={coef}"))
