#!/usr/bin/env python3
"""
csn_powerlaw.py -- Clauset-Shalizi-Newman (2009) discrete power-law fit,
the correct tool for RAW relation-target counts (discrete, heavy, sparse).

For each count distribution:
  - x_min chosen by minimising KS distance (tail x >= x_min vs best-fit PL)
  - discrete power-law exponent by MLE (Newton on the exact discrete
    likelihood, Hurwitz-zeta normalisation)
  - goodness-of-fit p via semiparametric bootstrap (200 resamples):
    p >= 0.1  => power law not rejected
  - map to stable index: a power-law TAIL  P(X>x) ~ x^-(gamma-1)  gives
    stable alpha = gamma - 1  (infinite variance iff gamma <= 3)
"""
import sys, math, random
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP")
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
import numpy as np
from scipy.special import zeta
from wordnet_boxkite import context_vector, RELATION_METHODS
from nltk.corpus import wordnet as wn

random.seed(20260827); np.random.seed(20260827)


def discrete_pl_loglik(gamma, x, xmin):
    # L = -n ln(zeta(gamma, xmin)) - gamma sum ln x
    n = len(x)
    return -n * math.log(zeta(gamma, xmin)) - gamma * np.sum(np.log(x))


def fit_gamma(x, xmin, lo=1.01, hi=6.0):
    x = x[x >= xmin]
    if len(x) < 10:
        return float("nan")
    # golden-section maximise loglik
    gr = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c = b - gr * (b - a); d = a + gr * (b - a)
    for _ in range(80):
        if discrete_pl_loglik(c, x, xmin) < discrete_pl_loglik(d, x, xmin):
            a = c
        else:
            b = d
        c = b - gr * (b - a); d = a + gr * (b - a)
    return (a + b) / 2


def ks_stat(x, xmin, gamma):
    xt = np.sort(x[x >= xmin])
    if len(xt) < 10:
        return np.inf
    cdf_emp = np.arange(1, len(xt) + 1) / len(xt)
    # theoretical discrete PL CDF
    xs = np.arange(xmin, xt.max() + 1)
    pmf = xs.astype(float) ** (-gamma) / zeta(gamma, xmin)
    cdf_the_full = np.cumsum(pmf)
    cdf_the = np.interp(xt, xs, cdf_the_full)
    return np.max(np.abs(cdf_emp - cdf_the))


def csn_fit(data):
    data = np.asarray(data)
    data = data[data >= 1]
    if len(data) < 50:
        return None
    cand = np.unique(data)
    cand = cand[(cand >= 1) & (cand <= np.percentile(data, 99))]
    best = None
    for xmin in cand:
        if np.sum(data >= xmin) < 15:
            break
        g = fit_gamma(data, xmin)
        if math.isnan(g):
            continue
        ks = ks_stat(data, xmin, g)
        if best is None or ks < best[2]:
            best = (xmin, g, ks, int(np.sum(data >= xmin)))
    return best


def bootstrap_p(data, xmin, gamma, ks_obs, B=200):
    data = np.asarray(data); data = data[data >= 1]
    n = len(data)
    ntail = int(np.sum(data >= xmin))
    ptail = ntail / n
    body = data[data < xmin]
    xs = np.arange(xmin, max(xmin + 1, data.max() * 3))
    pmf = xs.astype(float) ** (-gamma); pmf /= pmf.sum()
    wins = 0
    for _ in range(B):
        n_syn_tail = np.random.binomial(n, ptail)
        samp_tail = np.random.choice(xs, size=n_syn_tail, p=pmf)
        n_body = n - n_syn_tail
        samp_body = (np.random.choice(body, size=n_body, replace=True)
                     if len(body) else np.array([], int))
        samp = np.concatenate([samp_body, samp_tail]).astype(float)
        fb = csn_fit(samp)
        if fb is None:
            continue
        if fb[2] >= ks_obs:
            wins += 1
    return wins / B


# ---- collect raw counts --------------------------------------------------
S = list(wn.all_synsets()); random.shuffle(S)
cols = {m: [] for m in RELATION_METHODS}
total = []
for syn in S:
    row = []
    for m in RELATION_METHODS:
        try:
            c = len(getattr(syn, m)())
        except Exception:
            c = 0
        cols[m].append(c); row.append(c)
    total.append(sum(row))
    if len(total) >= 12000:
        break
total = np.array(total)

targets = [("TOTAL relation degree", total)]
for m in ["hyponyms", "member_meronyms", "part_meronyms", "hypernyms",
          "member_holonyms", "also_sees"]:
    targets.append((m, np.array(cols[m])))

print(f"corpus {len(total)} synsets\n")
print(f"{'distribution':24s} {'n>=1':>6} {'xmin':>5} {'gamma':>6} {'KS':>6} "
      f"{'ntail':>6} {'p':>5}  stable-alpha  variance")
print("-" * 92)
for name, data in targets:
    n1 = int(np.sum(data >= 1))
    fit = csn_fit(data)
    if fit is None:
        print(f"{name:24s} {n1:6d}   -- too sparse --")
        continue
    xmin, g, ks, ntail = fit
    p = bootstrap_p(data, xmin, g, ks, B=200)
    sa = g - 1.0
    var = "INFINITE (Levy)" if sa <= 2.0 else "finite"
    verdict = "power law OK" if p >= 0.1 else "PL rejected"
    print(f"{name:24s} {n1:6d} {xmin:5.0f} {g:6.2f} {ks:6.3f} {ntail:6d} "
          f"{p:5.2f}  {sa:6.2f}      {var:16s} [{verdict}]")

print("\nstable-alpha = gamma - 1 (tail).  infinite variance iff gamma <= 3.")
print("p >= 0.1: power-law tail not rejected.  p < 0.1: not a clean power law.")
