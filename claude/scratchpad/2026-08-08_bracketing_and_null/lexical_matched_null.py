"""TEST 4 — LEXICAL-MATCHED NULL.
Is the z=+31 module signal SEMANTIC, or just shared prefixes?
Same-module names share long substrings by construction ('skills.config.Path.').
Control for that and see whether anything survives.
"""
import pickle, numpy as np
from collections import Counter, defaultdict

d = pickle.load(open('/home/rendier/Projects/ThePlace/VAPMIP/monad_sedenion_addresses.pkl','rb'))
book = d['book']
names, vecs = [], []
for nm, ent in book.items():
    v = ent.get('sedenion') if isinstance(ent, dict) else ent
    if v is None or len(v) != 16: continue
    names.append(nm); vecs.append(np.asarray(v, float))
V = np.array(vecs)
Vp = V.copy(); Vp[:, 0] = 0.0                      # e0 projected out
Vp /= np.clip(np.linalg.norm(Vp, axis=1, keepdims=True), 1e-12, None)
N = len(names); print(f"{N} addresses (e0 projected out)\n")

def tri(s):
    s = f"  {s}  "
    return Counter(s[i:i+3] for i in range(len(s)-2))
TRI_FULL = [tri(n) for n in names]
TRI_LEAF = [tri(n.split('.')[-1]) for n in names]
MOD      = ['.'.join(n.split('.')[:2]) for n in names]

def tsim(a, b):
    if not a or not b: return 0.0
    inter = sum((a & b).values())
    return inter / np.sqrt(sum(a.values())*sum(b.values()))

rng = np.random.default_rng(1)
M = 200_000
I = rng.integers(0, N, M); J = rng.integers(0, N, M)
keep = I != J; I, J = I[keep], J[keep]

addr = (Vp[I]*Vp[J]).sum(1)
lex_full = np.array([tsim(TRI_FULL[i], TRI_FULL[j]) for i, j in zip(I, J)])
lex_leaf = np.array([tsim(TRI_LEAF[i], TRI_LEAF[j]) for i, j in zip(I, J)])
same = np.array([MOD[i] == MOD[j] for i, j in zip(I, J)])
print(f"sampled {len(I):,} pairs | same-module {same.sum():,}\n")

print("=== A. how much of the ADDRESS is spelling? ===")
for lab, L in (("full name", lex_full), ("leaf name only", lex_leaf)):
    r = np.corrcoef(L, addr)[0,1]
    print(f"  corr(lexical_sim[{lab}], address_cos) = {r:+.4f}")
print()

print("=== B. LEXICAL-MATCHED comparison: bin by full-name similarity ===")
print(f"  {'lex bin':>14s} {'n_same':>8s} {'n_diff':>9s} {'same-mod cos':>13s} {'diff-mod cos':>13s} {'gap':>8s}")
edges = np.quantile(lex_full, np.linspace(0, 1, 9))
gaps, ws = [], []
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (lex_full >= lo) & (lex_full < hi)
    s, dd = m & same, m & ~same
    if s.sum() < 30 or dd.sum() < 30: continue
    a, b = addr[s].mean(), addr[dd].mean()
    gaps.append(a-b); ws.append(s.sum())
    print(f"  [{lo:.3f},{hi:.3f}) {s.sum():8d} {dd.sum():9d} {a:13.4f} {b:13.4f} {a-b:8.4f}")
if gaps:
    gaps, ws = np.array(gaps), np.array(ws)
    print(f"\n  weighted mean within-bin gap: {np.average(gaps, weights=ws):+.4f}")
    print(f"  raw (unmatched) gap          : {addr[same].mean()-addr[~same].mean():+.4f}")
