#!/usr/bin/env python3
"""
lineage_anomaly.py -- generational-lineage trace of THE ANOMALY.

Question: which operation in the word-construction pipeline BIRTHS the
alpha < 2 (Levy-class, infinite-variance) heavy tail?  Genuine emergent
operator (leave it in) or artifact of one arbitrary step (take it out)?

Generations traced, alpha (Hill tail index) measured at each:
  G0  raw WordNet relation-target counts        len(getattr(syn,method)())
  G1  compress_count exponents                  round(log2(n+1))
  G2  prime hash  context_code / log(code)      prod p_i^v_i  /  sum v_i ln p_i
  G3  mean-centre the 19-vectors
  G4  SVD
  G5  residual after mode0                       Mc - rank1

alpha < 2  => infinite variance, Levy class, chaos-math object
alpha >= ~4 => effectively light / Gaussian-domain
"""
import sys, math, random
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP")
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
import numpy as np
from wordnet_boxkite import (context_vector, context_code, RELATION_METHODS,
                             CONTEXT_PRIMES, compress_count)
from nltk.corpus import wordnet as wn

random.seed(20260827); np.random.seed(20260827)


def hill(x, frac=0.05):
    x = np.sort(np.abs(np.asarray(x, float)))[::-1]
    x = x[x > 0]
    if len(x) < 30:
        return float("nan")
    k = max(15, int(len(x) * frac)); k = min(k, len(x) - 1)
    return 1.0 / np.mean(np.log(x[:k] / x[k]))


def col_alphas(M):
    return [hill(M[:, j]) for j in range(M.shape[1])]


def summarise(tag, alphas, extra=""):
    a = np.array([x for x in alphas if not math.isnan(x)])
    n_levy = int(np.sum(a < 2.0))
    print(f"  {tag:34s} min={a.min():5.2f}  median={np.median(a):5.2f}  "
          f"max={a.max():6.2f}  #(alpha<2)={n_levy}/{len(a)}   {extra}")
    return a


# ---- build raw counts + compressed vectors together, same synset order ----
S = list(wn.all_synsets()); random.shuffle(S)
raw_rows, cmp_rows, codes, logcodes = [], [], [], []
for syn in S:
    counts = []
    for m in RELATION_METHODS:
        try:
            counts.append(len(getattr(syn, m)()))
        except Exception:
            counts.append(0)
    if sum(counts) == 0:
        continue
    raw_rows.append(counts)
    cv = [compress_count(c) for c in counts]
    cmp_rows.append(cv)
    lc = sum(v * math.log(p) for v, p in zip(cv, CONTEXT_PRIMES))
    logcodes.append(lc)
    codes.append(sum(v * math.log10(p) for v, p in zip(cv, CONTEXT_PRIMES)))  # log10 for size only
    if len(raw_rows) >= 4000:
        break

R = np.array(raw_rows, float)     # G0
C = np.array(cmp_rows, float)     # G1
n, d = C.shape
print(f"\nsynsets={n}  relation-dims={d}\n")
print("GENERATIONAL LINEAGE OF THE TAIL INDEX  (alpha via Hill, top 5%)")
print("-" * 78)

# G0
summarise("G0 raw counts (per relation)", col_alphas(R))
summarise("G0 raw counts (row total degree)", [hill(R.sum(1))], "<- WordNet's own graph")

# G1
summarise("G1 compress_count exponents", col_alphas(C))
summarise("G1 compress_count (row sum)", [hill(C.sum(1))])

# G2  prime hash
print(f"  G2 log(context_code)=sum v_i ln p_i    "
      f"alpha={hill(np.array(logcodes)):.2f}   "
      f"(raw context_code spans ~10^{max(codes):.0f}, min|max/median| meaningless)")

# G3 centre
Mc = C - C.mean(0)
summarise("G3 mean-centred (per relation)", col_alphas(Mc))

# G4/G5 SVD + residual after mode0
U, sv, Vt = np.linalg.svd(Mc, full_matrices=False)
res1 = Mc - (U[:, :1] * sv[:1]) @ Vt[:1]
summarise("G5 residual after mode0 (per relation)", col_alphas(res1),
          f"energy mode0={sv[0]**2/np.sum(sv**2):.2f}")
summarise("G5 residual after mode0 (magnitude)", [hill(np.linalg.norm(res1, axis=1))])

# which relation carries the Levy tail, and is it a WordNet hub relation?
print("-" * 78)
ra = col_alphas(res1)
order = np.argsort(ra)
print("  relations ranked by residual tail weight (lowest alpha = heaviest):")
for j in order[:6]:
    nzrate = float((R[:, j] > 0).mean())
    print(f"    {RELATION_METHODS[j]:20s} alpha={ra[j]:5.2f}   "
          f"raw-count max={int(R[:,j].max()):4d}  fires on {nzrate:5.1%} of synsets")

# control: shuffle each column independently (kills cross-relation structure,
# keeps each marginal) -> does the residual tail survive?
Cs = np.column_stack([np.random.permutation(C[:, j]) for j in range(d)])
Mcs = Cs - Cs.mean(0)
Us, svs, Vts = np.linalg.svd(Mcs, full_matrices=False)
res1s = Mcs - (Us[:, :1] * svs[:1]) @ Vts[:1]
print("-" * 78)
print("  CONTROL (per-column shuffle: marginals kept, joint structure destroyed)")
summarise("   shuffled G5 residual (per relation)", col_alphas(res1s))
summarise("   shuffled G5 residual (magnitude)", [hill(np.linalg.norm(res1s, axis=1))])
