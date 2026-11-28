# 89 — The Seven Octonions: What Shape the 84 Zero Divisors Make

| | |
|---|---|
| Scope | the gain spectrum {0 ×4, 1 ×8, √2 ×4} of a zero-divisor multiplier; the 7 PRESERVE octonions and 7 quaternions; the Fano plane of struts; the Klein four-group of valves; what was refuted |
| Origin | measured 2026-08-15/16 (the page's own statement: "every result on this page was computed, not asserted; where something failed, the failure is recorded too") |
| Code | `ValaQuenta/modules/box_kite/`, `modules/angular_rank/`; notes `Null-Space-of-the-Zero-Divisor.md` |
| Confidence | the gain spectrum, the seven octonions, the quaternion count, the Fano incidence and the V₄ valve group: ESTABLISHED (re-run 2026-11-13) · the clathrate picture and "E₈³ unreachable": the algebra is measured, the picture is `INTERPRETATION` · the 2026-08-16 correction (21 → 7 quaternions) is reproduced and kept |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The question

The doublings ℝ → ℂ → ℍ → 𝕆 → 𝕊 (1, 2, 4, 8, 16) each cost a property: ordering, commutativity, associativity, and at 𝕊 division, so that two non-zero numbers can
have product zero. At dimension 16 there are exactly **84** zero divisors (as normalised diagonals eᵢ ± eⱼ). What shape do they make?

## 2. The three channels  `ESTABLISHED`

For a zero divisor a, the matrix L_a of "multiply by a" has exactly three distinct gains:

```
gain 0    4 dimensions   CONTRACT   the kernel
gain 1    8 dimensions   PRESERVE   in equals out
gain √2   4 dimensions   DILATE     amplified
0²·4 + 1²·8 + (√2)²·4 = 16 = the dimension
```

The counting law Σ gain² = dimension admits no other split with these gains: {4, 8, 4} is forced given the three-gain structure.

**Listing 1 — the gains, the seven octonions, the quaternions, the Fano incidence and the valve group** (written for this page; needs numpy; runs cold; a few seconds)

```python
import numpy as np, itertools
def tables(d):
    idx = np.zeros((1, 1), int); sg = np.ones((1, 1), int); h = 1
    while h < d:
        I = np.zeros((2*h, 2*h), int); S = np.zeros((2*h, 2*h), int); I[:h, :h], S[:h, :h] = idx, sg
        for i in range(h):
            for j in range(h):
                I[i, h+j], S[i, h+j] = h + idx[j, i], sg[j, i]
                I[h+i, j], S[h+i, j] = h + idx[i, j], sg[i, j] * (1 if j == 0 else -1)
                I[h+i, h+j], S[h+i, h+j] = idx[j, i], -(1 if j == 0 else -1) * sg[j, i]
        idx, sg, h = I, S, 2*h
    return idx, sg
idx, sg = tables(16); E = np.eye(16)
def L(a):
    M = np.zeros((16, 16))
    for i in np.flatnonzero(a):
        for k in range(16): M[idx[i, k], k] += a[i] * sg[i, k]
    return M
mul = lambda x, y: L(x) @ y
zds = [(i, j, s) for i in range(1, 8) for j in range(8, 16) for s in (1, -1)]
vec = lambda z: E[z[0]] + z[2] * E[z[1]]
zd = [z for z in zds if any(np.abs(mul(vec(z), vec(w))).max() < 1e-12 for w in zds)]
print('zero divisors e_i +- e_j (i<8<=j):', len(zd))
def spaces(z):
    a = vec(z) / np.sqrt(2); w, U = np.linalg.eigh(L(a).T @ L(a)); return [U[:, abs(w - g * g) < 1e-9] for g in (0, 1, 2 ** .5)]
def leak(B): return max(np.linalg.norm((lambda p: p - B @ (B.T @ p))(mul(B[:, x], B[:, y]))) for x in range(B.shape[1]) for y in range(B.shape[1]))
K, P, D = spaces((1, 10, 1))
print('gain 0 / 1 / sqrt2 dims:', K.shape[1], P.shape[1], D.shape[1], '; leakage of products out of CONTRACT %.2f, PRESERVE %.1e, DILATE %.2f' % (leak(K), leak(P), leak(D)), '; PRESERVE contains e0:', abs((P @ P.T)[0, 0] - 1) < 1e-9)
subs = {}
for z in zd:
    B = spaces(z)[1]; subs.setdefault(tuple(np.round((B @ B.T).flatten(), 6)), []).append(z)
projs = [np.array(k).reshape(16, 16) for k in subs]
inter = lambda A, B: int((np.linalg.eigvalsh(A + B) > 2 - 1e-6).sum())
print('distinct PRESERVE octonions:', len(subs), '; diagonals each:', sorted(len(v) for v in subs.values()), '; pairwise intersection dims:', sorted({inter(A, B) for A, B in itertools.combinations(projs, 2)}))
names = {k: n for n, k in enumerate(subs)}; on = {n: sorted({z[0] ^ z[1] for z in subs[k]}) for k, n in names.items()}
for n in sorted(on): print('  octonion', n, 'lies on struts', on[n])
print('3 struts per octonion:', {len(v) for v in on.values()}, '; each strut on', sorted({sum(s in v for v in on.values()) for s in range(9, 16)}), 'octonions; two octonions share', sorted({len(set(on[a]) & set(on[b])) for a, b in itertools.combinations(on, 2)}), 'strut; two struts share', sorted({sum(s in v and t in v for v in on.values()) for s, t in itertools.combinations(range(9, 16), 2)}), 'octonion')
spaces4 = set()
for A, B in itertools.combinations(projs, 2):
    w, U = np.linalg.eigh(A + B); Q = U[:, w > 2 - 1e-6]; spaces4.add(tuple(np.round((Q @ Q.T).flatten(), 5)))
print('distinct pairwise-intersection 4-spaces (quaternions):', len(spaces4), 'from', len(list(itertools.combinations(projs, 2))), 'pairs')
ann = {z: frozenset(w for w in zd if np.abs(mul(vec(z), vec(w))).max() < 1e-12) for z in zd}; ann_r = {z: frozenset(w for w in zd if np.abs(mul(vec(w), vec(z))).max() < 1e-12) for z in zd}
grp = {}
for z in zd: grp.setdefault((ann[z], ann_r[z]), []).append(z)
sA = lambda z: (z[0], z[1], -z[2]); sN = {}
for g in grp.values(): sN[g[0]], sN[g[1]] = g[1], g[0]
sC = {z: sN[sA(z)] for z in zd}
print('annihilator-signature classes (resolved by probing):', len(grp), 'of', len(zd), '; sA, sN commute:', all(sN[sA(z)] == sA(sN[z]) for z in zd), '; all free involutions:', all(sA(z) != z and sN[z] != z and sC[z] != z and sC[sC[z]] == z for z in zd))
print('V4 orbits:', len({frozenset({z, sA(z), sN[z], sC[z]}) for z in zd}), 'of size 4 ; sN(e1+e10) =', sN[(1, 10, 1)], ', sC(e2+e11) =', sC[(2, 11, 1)])
```

```
zero divisors e_i +- e_j (i<8<=j): 84
gain 0 / 1 / sqrt2 dims: 4 8 4 ; leakage of products out of CONTRACT 1.41, PRESERVE 0.0e+00, DILATE 1.41 ; PRESERVE contains e0: True
distinct PRESERVE octonions: 7 ; diagonals each: [12, 12, 12, 12, 12, 12, 12] ; pairwise intersection dims: [4]
  octonion 0 lies on struts [9, 10, 11]
  octonion 1 lies on struts [9, 12, 13]
  octonion 2 lies on struts [9, 14, 15]
  octonion 3 lies on struts [10, 12, 14]
  octonion 4 lies on struts [10, 13, 15]
  octonion 5 lies on struts [11, 12, 15]
  octonion 6 lies on struts [11, 13, 14]
3 struts per octonion: {3} ; each strut on [3] octonions; two octonions share [1] strut; two struts share [1] octonion
distinct pairwise-intersection 4-spaces (quaternions): 7 from 21 pairs
annihilator-signature classes (resolved by probing): 42 of 84 ; sA, sN commute: True ; all free involutions: True
V4 orbits: 21 of size 4 ; sN(e1+e10) = (2, 9, -1) , sC(e2+e11) = (3, 10, 1)
```

(The octonion labels 0–6 are the order found; the strut table below is the one of the 2026-08 page and matches the listing's output.)

### PRESERVE is the octonions

The middle eight dimensions are closed under multiplication (leakage 0 to rounding in Listing 1; the page's 9.5×10⁻¹⁶), contain 1 (e₀), have a multiplicative norm, and are alternative but not associative, and no zero divisors lie in them. By Hurwitz's theorem (the only
composition algebras over ℝ are ℝ, ℂ, ℍ, 𝕆 in dimensions 1, 2, 4, 8) an 8-dimensional closed subalgebra with a multiplicative norm must be 𝕆. So this is measured, not assumed.

### The wings are not algebras

An earlier reading called {4; 8; 4} "an octonion wrapped by its constituent quaternions". Half of it is wrong: CONTRACT and DILATE leak badly (1.41 each in Listing 1; the page recorded 1.39 and 1.41, a sample-level
difference) and are not closed, so they cannot be constituent algebras. The picture is a **clathrate**: a cage that is not itself the guest, holding something complete on its own.

## 3. Where the quaternions are  `ESTABLISHED`, corrected 2026-08-16

There are **7 distinct PRESERVE octonions** among the 84 diagonals, 12 diagonals each; every pair of them intersects in exactly 4 dimensions, all 21 pairs. Each intersection is closed, contains 1 and is
4-dimensional, hence the quaternions ℍ (Hurwitz again). But the 21 pairs give only **7** distinct 4-spaces (Listing 1: 7 from 21): the three pairs on a Fano line all intersect in the same 4-space. The structure is **7–7–7**: 7
octonions, 7 struts, 7 quaternions. The earlier text's "21 quaternions, 21 = C(7,2)" is withdrawn; 21 is the number of octonion *pairs*.

## 4. The Fano plane  `ESTABLISHED`

Each zero divisor lies on a strut, the label i XOR j of its indices (9–15, seven struts, the seven box-kites of [84](84_the_box_kite_debugger.md)). Cross-tabulating struts against octonions (Listing 1, reproducing the 2026-08 table exactly):

| strut | octonions present |
|---|---|
| 9 | 0, 1, 2 |
| 10 | 0, 3, 4 |
| 11 | 0, 5, 6 |
| 12 | 1, 3, 5 |
| 13 | 1, 4, 6 |
| 14 | 2, 3, 6 |
| 15 | 2, 4, 5 |

Seven struts, seven octonions, three per strut and three struts per octonion, any two struts sharing exactly one octonion and any two octonions lying on exactly one strut (Listing 1): that is the Fano plane PG(2, 2), the Steiner system S(2, 3, 7)
(the same design theory that builds the Golay code, the Leech lattice and the Mathieu groups). Octonions are the 7 points, struts the 7 lines, quaternions the 7 line-cores, and the 21 flags the point-on-line incidences. The earlier page states that the lines extracted from the octonion multiplication
table are identical entry for entry to this table; that comparison needs a labelling map between the two and was not repeated here (recorded).

## 5. The valve group  `ESTABLISHED`

The 84 diagonals carry three pairings, each splitting them into 42 pairs: **sA** (flip the sign, e₁+e₁₀ ↔ e₁−e₁₀), **sC** (XOR-translate both indices keeping the sign, e₂+e₁₁ ↔ e₃+e₁₀) and **sN** (same annihilation behaviour, e₁+e₁₀ ↔ e₂−e₉). In Listing 1 sN is *defined* as the pairing of divisors with identical left and right
annihilator sets (42 classes, each of size 2) and sC as sA·sN; both of the page's examples then come out as stated. All three are free involutions (no fixed points), they commute, sA·sC = sN, sA·sN = sC, sC·sN = sA: they are the three non-identity elements of the **Klein four-group V₄** (order 4, not 8:
there is no third independent binary choice), acting freely on 84 so that the 21 orbits all have size 4 (Listing 1).

**The blind spot.** Probing which diagonals annihilate each other resolves the 84 down to 42 signatures and stops, permanently, because sN is a symmetry of annihilation and not a limitation of probing; and sN = sA·sC: the invisible thing is exactly the two visible things done together. So one bit of
the address is unreachable from inside the algebra: an orientation, like the choice of i against −i in ℂ (conjugation is an automorphism). It must come from outside and be made once, globally. The counting closes: 84/4 = 21, which is the number of Fano flags (7 lines × 3 points); "one rotor face per flag, two valves per face, three faces per strut".

## 6. What was refuted  `kept`

- **E₈³ is unreachable.** Three octonions × 8 = 24 = the rank of the Niemeier lattices, and E₈³ is one of them. But every PRESERVE octonion contains the number 1 (Listing 1: `PRESERVE contains e0: True`), so no two can be orthogonal (two subspaces sharing a non-zero vector are not orthogonal). The page records, at dimension 32, 35 octonions and 595 pairs with zero orthogonal pairs and minimum intersection 2 (not re-run). Adding sedenions adds octonions but never separates them.
- **E₈ does not require 48 dimensions:** the octonion is whole inside one sedenion.
- **Orientation cannot be made an independent invariant:** the sign is locked to the XOR translation (the sN = sA·sC statement above); worst-case search stays at 11 probes either way. The invariant that works is the strut, which survives all 42 degeneracies.
- **The strut/octonion structure is PG(2, 2) only at dimension 16:** at dimension 32 it is 35 octonions on 15 struts with skew pairs (a projective space, not a plane); recorded, not re-run.

## 7. Related pages

[84 the box-kite debugger](84_the_box_kite_debugger.md) · [86 the 16D oscilloscope](86_the_16d_oscilloscope.md) · [87 the boundary lever](87_the_boundary_lever.md) · [90 divisors are definers](90_divisors_are_definers.md)
