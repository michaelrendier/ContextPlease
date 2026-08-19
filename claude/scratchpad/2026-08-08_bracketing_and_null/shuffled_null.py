"""TEST 2 — SHUFFLED NULL, two arms (raw vs e0-projected).

Ground truth grouping: symbols sharing a parent module (e.g. skills.config.*)
should be more similar than random pairs IF the addresses carry structure.
Null: shuffle the name->vector assignment, destroying association only.
"""
import pickle, numpy as np
from collections import defaultdict

d = pickle.load(open('/home/rendier/Projects/ThePlace/VAPMIP/monad_sedenion_addresses.pkl','rb'))
book = d['book']
k0 = next(iter(book)); print("entry fields:", list(book[k0].keys()) if isinstance(book[k0],dict) else type(book[k0]))

names, vecs = [], []
for name, ent in book.items():
    v = ent.get('sedenion') if isinstance(ent, dict) else ent
    if v is None or len(v) != 16: continue
    names.append(name); vecs.append(np.asarray(v, float))
V = np.array(vecs); print(f"loaded {len(names)} addresses, shape {V.shape}")

groups = defaultdict(list)
for i, nm in enumerate(names):
    parts = nm.split('.')
    if len(parts) >= 2: groups['.'.join(parts[:2])].append(i)
groups = {g: ix for g, ix in groups.items() if len(ix) >= 4}
print(f"{len(groups)} parent modules with >=4 members "
      f"({sum(len(v) for v in groups.values())} symbols)\n")

def cos_stats(M, groups, rng=None):
    M = M / np.clip(np.linalg.norm(M, axis=1, keepdims=True), 1e-12, None)
    idx = np.arange(len(M))
    if rng is not None: idx = rng.permutation(len(M))
    within = []
    for g, ix in groups.items():
        jx = idx[ix]
        S = M[jx] @ M[jx].T
        iu = np.triu_indices(len(jx), 1)
        within.append(S[iu].mean())
    r = np.random.default_rng(0)
    a, b = r.integers(0, len(M), 20000), r.integers(0, len(M), 20000)
    m = a != b
    return float(np.mean(within)), float((M[a[m]] * M[b[m]]).sum(1).mean())

for arm, M in (("RAW 16D", V.copy()),
               ("e0 PROJECTED OUT", np.where(np.arange(16)==0, 0, V)),
               ("e0+e8 PROJECTED OUT", np.where((np.arange(16)==0)|(np.arange(16)==8), 0, V))):
    w, b = cos_stats(M, groups)
    nulls = [cos_stats(M, groups, np.random.default_rng(s))[0] for s in range(200)]
    mu, sd = np.mean(nulls), np.std(nulls)
    z = (w - mu)/sd if sd > 0 else float('nan')
    print(f"{arm:22s} within-module cos {w:.4f} | random-pair cos {b:.4f}")
    print(f"{'':22s} shuffled null {mu:.4f} +/- {sd:.4f}  ->  z = {z:+.2f}"
          f"   {'SIGNAL' if abs(z)>3 else 'no signal'}\n")
