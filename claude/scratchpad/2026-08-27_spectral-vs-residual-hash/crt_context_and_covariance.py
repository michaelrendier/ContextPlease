#!/usr/bin/env python3
"""
crt_context_and_covariance.py

TWO things:

J1  CRT split of context_code  --  context_code = prod CONTEXT_PRIMES[i]^v_i,
    so the "CRT decomposition" is literally the exponent vector v_i, one per
    relation-prime.  Information location over that semantic spectrum:
      MI( lexname ; v_i )        per relation-prime   (magnitude / depth)
      MI( lexname ; 1[v_i>0] )   per relation-prime   (presence only)
    -> where in the relation spectrum does supersense info LIVE, and does
       exponent DEPTH (hub-ness) carry more than mere presence?

J2  Cody's design claims, measured on 3 distance matrices over words that
    have phonetic coverage:
      d_phon = stress-spectrum distance   (from monad_phonetic.bin)
      d_sem  = context_vector distance    (the synset itself)
      d_ctx  = summed-neighbourhood context distance (its related synsets)
    claim A: "semantic and contextual are roughly co-variant" -> corr(d_sem,d_ctx) high
    claim B: "phonetic is the origin of the construction"     -> d_phon ~independent
             of both (corr ~ 0) => a valid independent origin, not another axis
"""
import os, sys, math, struct, random
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP")
sys.path.insert(0, "/home/rendier/Projects/ThePlace")
import numpy as np
from wordnet_boxkite import context_vector, RELATION_METHODS
from nltk.corpus import wordnet as wn

random.seed(20260827); np.random.seed(20260827)
PHON = os.path.join("/home/rendier/Projects/ThePlace/VAPMIP", "PtolC", "monad_phonetic.bin")


def read_phon(path):
    with open(path, "rb") as f:
        assert f.read(4) == b"PHON"; struct.unpack("<I", f.read(4))
        (nw,) = struct.unpack("<I", f.read(4)); out = {}
        for _ in range(nw):
            (wl,) = struct.unpack("<B", f.read(1)); w = f.read(wl).decode()
            (npr,) = struct.unpack("<B", f.read(1)); pr = []
            for _ in range(npr):
                (nph,) = struct.unpack("<B", f.read(1)); ph = []
                for _ in range(nph):
                    (pl,) = struct.unpack("<B", f.read(1)); ph.append(f.read(pl).decode())
                pr.append(ph)
            out[w] = pr
    return out


def stress_vec(pron):
    return [int(p[-1]) for p in pron if p[-1] in "012"]


def Hd(c):
    p = c / c.sum(); p = p[p > 0]; return -np.sum(p * np.log2(p))


def mi_norm(feat, tgt):
    fv, fc = np.unique(feat, return_inverse=True)
    tv, tc = np.unique(tgt, return_inverse=True)
    F, T = len(fv), len(tv)
    if F < 2 or T < 2:
        return 0.0
    tot = np.bincount(tc, minlength=T); Ht = Hd(tot)
    j = np.bincount(fc * T + tc, minlength=F * T).reshape(F, T)
    n = len(feat); Hc = 0.0
    for r in range(F):
        s = j[r].sum()
        if s:
            Hc += (s / n) * Hd(j[r])
    return (Ht - Hc) / Ht


# ======================= J1  CRT split / info location ====================
print("=" * 74)
print("J1  information location over the context_code prime spectrum")
print("=" * 74)
S = list(wn.all_synsets()); random.shuffle(S)
vecs, lex = [], []
for syn in S:
    v = context_vector(syn)
    if sum(v) == 0:
        continue
    vecs.append(v); lex.append(syn.lexname())
    if len(vecs) >= 5000:
        break
V = np.array(vecs); lex = np.array(lex)
print(f"  {len(V)} synsets, {len(set(lex))} lexnames (supersenses)\n")
print(f"  {'relation-prime':20s}  MI(lex; v_i)  MI(lex; v_i>0)  depth-gain  nz-rate")
print("  " + "-" * 70)
rows = []
for i, rel in enumerate(RELATION_METHODS):
    mi_mag = mi_norm(V[:, i], lex)
    mi_pres = mi_norm((V[:, i] > 0).astype(int), lex)
    nz = float((V[:, i] > 0).mean())
    rows.append((rel, mi_mag, mi_pres, mi_mag - mi_pres, nz))
for rel, a, b, g, nz in sorted(rows, key=lambda r: -r[1]):
    print(f"  {rel:20s}    {a:.4f}       {b:.4f}       {g:+.4f}     {nz:.3f}")
tot_mag = sum(r[1] for r in rows)
print(f"\n  total MI mass (sum over primes): {tot_mag:.3f}   "
      f"top-1 share {max(r[1] for r in rows)/tot_mag:.2f}   "
      f"top-4 share {sum(sorted((r[1] for r in rows),reverse=True)[:4])/tot_mag:.2f}")

# ======================= J2  covariance of the 3 axes =====================
print("\n" + "=" * 74)
print("J2  d_phon / d_sem / d_ctx  --  co-variance and independence")
print("=" * 74)
phon = read_phon(PHON)
items = []          # (synset, word, stress_vec, context_vector, ctx_sum)
seen = set()
for syn in S:
    for lname in syn.lemma_names():
        w = lname.replace("_", " ").lower()
        if w in seen or w not in phon:
            continue
        cv = np.array(context_vector(syn), float)
        if cv.sum() == 0:
            continue
        # neighbourhood context = sum of related synsets' context_vectors
        cs = np.zeros(len(RELATION_METHODS))
        cnt = 0
        for m in RELATION_METHODS:
            try:
                for r in getattr(syn, m)():
                    cs += np.array(context_vector(r), float); cnt += 1
            except Exception:
                pass
        if cnt == 0:
            continue
        seen.add(w)
        items.append((w, np.array(stress_vec(phon[w][0]), float), cv, cs))
    if len(items) >= 700:
        break
print(f"  {len(items)} words with phonetic + semantic + contextual data")

M = len(items)
maxL = max(len(it[1]) for it in items) or 1


def spad(v):
    z = np.zeros(maxL); z[:len(v)] = v; return z


SP = np.array([spad(it[1]) for it in items])
CV = np.array([it[2] for it in items])
CS = np.array([it[3] for it in items])

# pairwise distances (upper triangle)
iu = np.triu_indices(M, 1)


def pdist(X):
    d = np.abs(X[:, None, :] - X[None, :, :]).sum(-1)
    return d[iu]


dphon = pdist(SP)
dsem = pdist(CV)
dctx = pdist(CS)


def pear(a, b):
    a = a - a.mean(); b = b - b.mean()
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


print(f"\n  Pearson r over {len(dphon):,} pairs:")
print(f"    corr(d_sem , d_ctx) = {pear(dsem, dctx):+.3f}   <- claim A: co-variant?")
print(f"    corr(d_phon, d_sem) = {pear(dphon, dsem):+.3f}   <- claim B: phon independent?")
print(f"    corr(d_phon, d_ctx) = {pear(dphon, dctx):+.3f}   <- claim B: phon independent?")
# partial: semantic vs contextual controlling for phonetic
def partial(a, b, c):
    ra, rb = a - np.polyval(np.polyfit(c, a, 1), c), b - np.polyval(np.polyfit(c, b, 1), c)
    return pear(ra, rb)
print(f"    partial corr(d_sem, d_ctx | d_phon) = {partial(dsem, dctx, dphon):+.3f}")
print(f"\n  reading:")
print(f"    A holds if corr(d_sem,d_ctx) is high and survives partialling phon")
print(f"    B holds if corr(d_phon,*) ~ 0  (phon is an independent origin, not")
print(f"      a third co-variant axis)")
