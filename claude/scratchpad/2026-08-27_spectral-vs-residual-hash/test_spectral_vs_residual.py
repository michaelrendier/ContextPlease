#!/usr/bin/env python3
"""
test_spectral_vs_residual.py

HYPOTHESIS (Cody, 2026-08-27), stated so it can fail:

  "spectral decomposition" was used loosely as a name for A decomposition.
  IF the phonetic/stress side is genuinely SPECTRAL in nature (orthogonal
  modes, conjugate faces: reCORD / REcord differ only by the phase of the
  stress spectrum), THEN the prime SEMANTIC hash should be RESIDUAL in
  nature -- BECAUSE residuals can overlap and an orthogonal spectral basis
  cannot. And the residual can be the Smith diagram's 4D (it is the
  multi-dimensional object the Mobius fold consumes; its effective
  dimension should sit near 4).

Three falsifiable predictions:

  P-A  stress_spec IS spectral:
       - heteronym pairs (same phoneme skeleton, different stress) have
         EQUAL magnitude spectra and DIFFERENT phase  (conjugate faces)
       - stress-vector modes over syllable position are ~orthogonal
  P-B  context_vector IS residual (overlap-permitting), NOT orthogonal:
       - its 19 components are CORRELATED (mean |off-diagonal corr| high)
       - low participation ratio (effective rank << 19)
       - semantically related synset pairs OVERLAP (high cosine, shared
         prime factors in context_code) -- an orthogonal basis would make
         even related items near-orthogonal
  P-C  the residual is the Smith 4D:
       - after removing the dominant shared mode(s), the residual
         subspace has effective dimension ~= 4
       - residual coords fold through mobius_fold without |Gamma|
         saturating (same degeneracy discipline as the primer)

Run with the ValaQuenta venv python:
  ../ValaQuenta/.venv/bin/python3 test_spectral_vs_residual.py
"""

import os
import sys
import math
import struct
import random
from collections import Counter

import numpy as np

VAPMIP = "/home/rendier/Projects/ThePlace/VAPMIP"
PROJ = "/home/rendier/Projects/ThePlace"
sys.path.insert(0, VAPMIP)
sys.path.insert(0, PROJ)

from wordnet_boxkite import context_vector, context_code, RELATION_METHODS, CONTEXT_PRIMES  # noqa
from nltk.corpus import wordnet as wn  # noqa

try:
    from ValaQuenta.modules.scale.maths import mobius_fold  # noqa
except Exception:
    def mobius_fold(Z, Z0):
        return (Z - Z0) / (Z + Z0)

PHON_BIN = os.path.join(VAPMIP, "PtolC", "monad_phonetic.bin")
random.seed(20260827)
np.random.seed(20260827)

LINE = "=" * 74


def hdr(s):
    print("\n" + LINE + "\n" + s + "\n" + LINE)


# ----------------------------------------------------------------------------
# phonetic bin reader (format from tools/make_phonetic_bin.py)
# ----------------------------------------------------------------------------
def read_phon(path):
    with open(path, "rb") as f:
        assert f.read(4) == b"PHON"
        struct.unpack("<I", f.read(4))
        (n_words,) = struct.unpack("<I", f.read(4))
        out = {}
        for _ in range(n_words):
            (wlen,) = struct.unpack("<B", f.read(1))
            word = f.read(wlen).decode("utf-8")
            (n_pron,) = struct.unpack("<B", f.read(1))
            prons = []
            for _ in range(n_pron):
                (n_phon,) = struct.unpack("<B", f.read(1))
                pron = []
                for _ in range(n_phon):
                    (plen,) = struct.unpack("<B", f.read(1))
                    pron.append(f.read(plen).decode("ascii"))
                prons.append(pron)
            out[word] = prons
    return out


def stress_vec(pron):
    """per-syllable stress digits, vowels only: reCORD -> [0,1]"""
    return [int(p[-1]) for p in pron if p[-1] in "012"]


def skeleton(pron):
    """phoneme multiset with stress digits stripped -- the shared face"""
    return tuple(sorted(p.rstrip("012") for p in pron))


# ----------------------------------------------------------------------------
# PART A : is stress_spec spectral?
# ----------------------------------------------------------------------------
def part_a():
    hdr("PART A  --  is stress_spec SPECTRAL (orthogonal modes, conjugate faces)?")
    phon = read_phon(PHON_BIN)
    print(f"  loaded {len(phon):,} words from monad_phonetic.bin")

    # A1: heteronym conjugate-pair test
    conj_hits, conj_total = 0, 0
    mag_err = []
    examples = []
    for word, prons in phon.items():
        if len(prons) < 2:
            continue
        # group prons by skeleton; a heteronym pair = same skeleton, diff stress
        by_skel = {}
        for pr in prons:
            by_skel.setdefault(skeleton(pr), []).append(stress_vec(pr))
        for skel, svs in by_skel.items():
            uniq = [tuple(s) for s in svs]
            seen = set()
            for i in range(len(uniq)):
                for j in range(i + 1, len(uniq)):
                    a, b = uniq[i], uniq[j]
                    if a == b or len(a) != len(b) or len(a) < 2:
                        continue
                    if sorted(a) != sorted(b):
                        continue  # require same stress multiset, moved position
                    conj_total += 1
                    fa = np.fft.rfft(np.array(a, float) - np.mean(a))
                    fb = np.fft.rfft(np.array(b, float) - np.mean(b))
                    ma, mb = np.abs(fa), np.abs(fb)
                    denom = (np.linalg.norm(ma) + np.linalg.norm(mb)) or 1.0
                    merr = np.linalg.norm(ma - mb) / denom
                    mag_err.append(merr)
                    # conjugate face := equal magnitude spectrum, phase differs
                    phase_diff = np.abs(np.angle(fa) - np.angle(fb))
                    phase_moved = np.any(phase_diff[1:] > 1e-6)
                    if merr < 1e-6 and phase_moved:
                        conj_hits += 1
                        if len(examples) < 8:
                            examples.append((word, a, b))
    print(f"\n  A1 heteronym conjugate-pair test:")
    print(f"     stress-moved pairs found      : {conj_total}")
    if conj_total:
        print(f"     equal-magnitude & phase-moved : {conj_hits}"
              f"  ({100*conj_hits/conj_total:.1f}%)")
        print(f"     mean magnitude-spectrum error : {np.mean(mag_err):.2e}")
    for w, a, b in examples:
        print(f"       {w:<16} {a} <-> {b}")
    a1_spectral = conj_total > 0 and conj_hits / conj_total > 0.9

    # A2: orthogonality of syllable-position modes at fixed length
    print(f"\n  A2 syllable-position mode structure (fixed length L):")
    a2_flags = []
    for L in (2, 3, 4):
        rows = []
        for word, prons in phon.items():
            for pr in prons:
                sv = stress_vec(pr)
                if len(sv) == L:
                    rows.append(sv)
        if len(rows) < 50:
            continue
        X = np.array(rows, float)
        Xc = X - X.mean(0)
        C = np.cov(Xc, rowvar=False)
        # compare eigenbasis of C to the DFT basis of length L
        w_, V = np.linalg.eigh(C)
        F = np.fft.fft(np.eye(L), axis=0) / math.sqrt(L)
        # how well DFT basis diagonalises C  (off-diag energy after F^H C F)
        D = np.abs(F.conj().T @ C @ F)
        offd = (D.sum() - np.trace(D).real) / (D.sum() or 1.0)
        pr_C = (w_.sum() ** 2) / (np.sum(w_ ** 2) or 1.0)
        print(f"     L={L}: n={len(rows):5d}  eig(C)={np.round(w_,3)}  "
              f"partic.ratio={pr_C:.2f}  DFT off-diag frac={offd:.3f}")
        a2_flags.append(offd < 0.15)
    a2_spectral = bool(a2_flags) and all(a2_flags)

    verdict = a1_spectral and a2_spectral
    print(f"\n  --> P-A  stress_spec spectral?  "
          f"A1={'YES' if a1_spectral else 'no'}  "
          f"A2={'YES' if a2_spectral else 'no'}  "
          f"==>  {'SUPPORTED' if verdict else 'NOT supported'}")
    return verdict


# ----------------------------------------------------------------------------
# sample synsets + build the context_vector matrix
# ----------------------------------------------------------------------------
def sample_matrix(n=2500):
    all_s = list(wn.all_synsets())
    random.shuffle(all_s)
    picks, rows, codes, labels = [], [], [], []
    for s in all_s:
        v = context_vector(s)
        if sum(v) == 0:
            continue
        picks.append(s)
        rows.append(v)
        codes.append(context_code(s))
        labels.append(s.lexname())          # 45 WordNet supersenses = free label
        if len(picks) >= n:
            break
    return picks, np.array(rows, float), codes, labels


# ----------------------------------------------------------------------------
# PART B : is context_vector residual (overlap-permitting), not orthogonal?
# ----------------------------------------------------------------------------
def part_b(picks, M, codes, labels):
    hdr("PART B  --  is context_vector RESIDUAL (overlaps), not an orthogonal basis?")
    n, d = M.shape
    Mc = M - M.mean(0)
    print(f"  {n} synsets x {d} relation dims")

    # B1: component correlation
    R = np.corrcoef(Mc, rowvar=False)
    R = np.nan_to_num(R)
    offdiag = R[~np.eye(d, dtype=bool)]
    print(f"\n  B1 component correlation (orthogonal basis => ~0):")
    print(f"     mean |off-diag corr| = {np.mean(np.abs(offdiag)):.3f}")
    print(f"     max  |off-diag corr| = {np.max(np.abs(offdiag)):.3f}")
    print(f"     frac |corr|>0.3      = {np.mean(np.abs(offdiag)>0.3):.3f}")
    b1_residual = np.mean(np.abs(offdiag)) > 0.15

    # B2: participation ratio / effective rank
    U, S, Vt = np.linalg.svd(Mc, full_matrices=False)
    ev = S ** 2
    pr = (ev.sum() ** 2) / (np.sum(ev ** 2) or 1.0)
    frac = ev / ev.sum()
    print(f"\n  B2 spectrum of context_vector (flat => orthogonal/independent):")
    print(f"     singular-value energy frac (top 8): "
          f"{np.round(frac[:8],3)}")
    print(f"     participation ratio (eff. rank)   : {pr:.2f}  / {d}")
    b2_residual = pr < d * 0.6

    # B3: overlap of semantically RELATED pairs vs random pairs
    def cos(a, b):
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        return float(a @ b / (na * nb)) if na and nb else 0.0

    def factor_overlap(ca, cb):
        g = math.gcd(ca, cb)
        return math.log(g + 1) / math.log(min(ca, cb) + 1)

    idx = {s: i for i, s in enumerate(picks)}
    rel_cos, rel_fac, rnd_cos, rnd_fac = [], [], [], []
    for s in picks:
        i = idx[s]
        rels = []
        for m in ("hypernyms", "hyponyms", "similar_tos", "also_sees", "verb_groups"):
            try:
                rels += getattr(s, m)()
            except Exception:
                pass
        for r in rels:
            j = idx.get(r)
            if j is None or j == i:
                continue
            rel_cos.append(cos(M[i], M[j]))
            rel_fac.append(factor_overlap(codes[i], codes[j]))
    for _ in range(len(rel_cos) or 500):
        i, j = random.randrange(n), random.randrange(n)
        if i == j:
            continue
        rnd_cos.append(cos(M[i], M[j]))
        rnd_fac.append(factor_overlap(codes[i], codes[j]))
    print(f"\n  B3 overlap: related pairs vs random pairs "
          f"(n_rel={len(rel_cos)}):")
    print(f"     cosine   related={np.mean(rel_cos):.3f}   random={np.mean(rnd_cos):.3f}")
    print(f"     factor   related={np.mean(rel_fac):.3f}   random={np.mean(rnd_fac):.3f}")
    b3_overlap = np.mean(rel_cos) > np.mean(rnd_cos) + 0.05

    verdict = sum([b1_residual, b2_residual, b3_overlap]) >= 2
    print(f"\n  --> P-B  context_vector residual?  "
          f"B1={'YES' if b1_residual else 'no'} "
          f"B2={'YES' if b2_residual else 'no'} "
          f"B3={'YES' if b3_overlap else 'no'}  ==>  "
          f"{'SUPPORTED' if verdict else 'NOT supported'}")
    return verdict, (U, S, Vt, Mc)


# ----------------------------------------------------------------------------
# PART C : is the residual the Smith diagram's 4D?
# ----------------------------------------------------------------------------
def part_c(svd, labels):
    hdr("PART C  --  is the RESIDUAL the Smith diagram's 4D?")
    U, S, Vt, Mc = svd
    d = Mc.shape[1]
    lab = np.array(labels)

    def fisher(X, lab):
        mu = X.mean(0)
        sw = sb = 0.0
        for c in np.unique(lab):
            Xi = X[lab == c]
            if len(Xi) < 2:
                continue
            mi = Xi.mean(0)
            sw += ((Xi - mi) ** 2).sum()
            sb += len(Xi) * ((mi - mu) ** 2).sum()
        return sb / (sw or 1.0)

    print(f"  C1 effective dimension of the residual after removing top-k modes:")
    print(f"     (participation ratio of the leftover singular spectrum)")
    for k in range(0, 6):
        Sres = S.copy()
        Sres[:k] = 0.0
        ev = Sres ** 2
        pr = (ev.sum() ** 2) / (np.sum(ev ** 2) or 1.0)
        Xk = (U * S) @ Vt
        Xres = Xk - (U[:, :k] * S[:k]) @ Vt[:k]
        j_full = fisher(Xk, lab)
        j_res = fisher(Xres, lab)
        tag = "  <== near 4" if abs(pr - 4.0) < 0.75 else ""
        print(f"     k={k}: residual particip.ratio={pr:5.2f}"
              f"   Fisher(full)={j_full:.3f}  Fisher(residual)={j_res:.3f}{tag}")

    # C2: does the residual fold through the Mobius map without saturating?
    print(f"\n  C2 residual coords through mobius_fold (|Gamma| must not saturate):")
    Xres1 = ((U * S) @ Vt) - (U[:, :1] * S[:1]) @ Vt[:1]
    # min-max normalise each residual dim to [0,1] (primer's own recipe)
    lo, hi = Xres1.min(0), Xres1.max(0)
    Xn = (Xres1 - lo) / np.where(hi - lo == 0, 1, hi - lo)
    # pair the 19 dims into complex Z's, fold each vs Z0=0.5+0.5j
    Z0 = complex(0.5, 0.5)
    gammas = []
    for row in Xn:
        for a in range(0, d - 1, 2):
            Z = complex(row[a], row[a + 1])
            gammas.append(abs(mobius_fold(Z, Z0)))
    g = np.array(gammas)
    print(f"     |Gamma|  mean={g.mean():.3f}  std={g.std():.3f}  "
          f"min={g.min():.3f}  max={g.max():.3f}")
    print(f"     frac |Gamma|>0.99 (saturated) = {np.mean(g>0.99):.3f}"
          f"   frac in (0.05,0.95) = {np.mean((g>0.05)&(g<0.95)):.3f}")
    healthy = np.mean(g > 0.99) < 0.05 and 0.1 < g.std() < 0.5

    print(f"\n  --> P-C  residual ~ Smith 4D?  "
          f"(read C1 for a participation ratio near 4; "
          f"fold {'HEALTHY' if healthy else 'saturated/degenerate'})")


# ----------------------------------------------------------------------------
def main():
    a = part_a()
    picks, M, codes, labels = sample_matrix(2500)
    b, svd = part_b(picks, M, codes, labels)
    part_c(svd, labels)

    hdr("SUMMARY")
    print(f"  P-A  stress_spec is spectral (conjugate faces)   : "
          f"{'SUPPORTED' if a else 'NOT supported'}")
    print(f"  P-B  semantic hash is residual (overlaps)         : "
          f"{'SUPPORTED' if b else 'NOT supported'}")
    print(f"  P-C  residual dimensionality / Smith fold         :  see PART C")
    print()
    if a and b:
        print("  => the inference holds on the data: phonetic side carries the")
        print("     orthogonal/spectral structure, the prime semantic hash")
        print("     carries the overlap-permitting residual.")
    else:
        print("  => the inference does NOT hold cleanly; see which P failed.")


if __name__ == "__main__":
    main()
