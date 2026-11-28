# 90 — Divisors Are Definers

> **Disambiguation, read first.** Three different objects in this project carry "zero" in their name:
>
> | name | domain | what it is |
> |---|---|---|
> | **zero divisors** | algebraic | a·b = 0 with a, b ≠ 0; the 84 diagonals at dim 16. **This page.** |
> | **Riemann zeta zeros** | analytic | ρ = ½ + iγ: the Zero Tree, the Zero Lattice, Telperion's spectral nodes |
> | **d\*, "The Zero Definer"** | analytic | Ω_ZS/ln 10 = 0.24631, the σ = ½ boundary below which no algebraic definition occurs |
>
> This page concerns the first row only. It argues that zero *divisors* deserve the name *definers* because they are constructive; the phrase "The Zero Definer" is already d\*, so the
> page is titled for the claim and not the noun. Nothing here is about zeta zeros or d\*.

| | |
|---|---|
| Scope | zero divisors as a selection mechanism (7 octonions, 7 quaternions, the Fano plane) out of a continuum; definition impossible from inside the child; reading/writing/speaking as the nesting 𝕊 ⊃ 𝕆 ⊃ ℍ; provenance as geometry; two struts, one point, one bit; the fulcrum; what was refuted |
| Origin | measured 2026-08-16; continues [89](89_the_seven_octonions.md) |
| Code | `ValaQuenta/modules/box_kite/`, `angular_rank/` |
| Confidence | the gain-1 octonions, the determinants, the nested-algebra statistics and the 84 → 12 → 4 → 2 pruning: ESTABLISHED (re-run) · the language correspondence and the provenance model: `INTERPRETATION` (the timings are machine-dependent and were not re-run) · the refutations: kept |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The rename, and why it is not cosmetic

A zero divisor is a pair of non-zero numbers with product zero; it first appears at the sedenions (dimension 16) and the name says what *fails*. The page's claim is that the name is wrong: what happens there is not a failure but the only place
definition happens at all.

```
DIVISOR   names a breakdown   xy = 0            destructive, an exception
DEFINER   names a selection   the 7, the 21, PG(2,2)   constructive, a mechanism
```

(A caution, kept: "The Zero Definer" is d\* in the canonical maths and the two domains are not to be merged because they share an adjective.)

## 2. What the definers define  `ESTABLISHED`

An octonion (an 8-dimensional closed subalgebra) is not rare. For **any** unit sedenion a, the subspace where multiplication by a has gain exactly 1 is 8-dimensional and closed under multiplication to rounding. So octonions are a continuum; what is rare is *which* octonions and how they sit relative to each
other.

**Listing 1 — random unit sedenions against the seven; determinants; the nested algebras; the 84 → 12 → 4 → 2 pruning** (written for this page; needs numpy; runs cold; a few seconds)

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
rng = np.random.default_rng(2)
def Lm(ix, sx, a):
    d = len(a); M = np.zeros((d, d))
    for i in np.flatnonzero(a):
        for k in range(d): M[ix[i, k], k] += a[i] * sx[i, k]
    return M
idx, sg = tables(16); E = np.eye(16)
mul = lambda x, y: Lm(idx, sg, x) @ y
def preserve(a): w, U = np.linalg.eigh(Lm(idx, sg, a).T @ Lm(idx, sg, a)); return U[:, abs(w - 1) < 1e-9]
zd = [(i, j, s) for i in range(1, 8) for j in range(8, 16) for s in (1, -1) if any(np.abs(mul(E[i] + s * E[j], E[k] + t * E[l])).max() < 1e-12 for k in range(1, 8) for l in range(8, 16) for t in (1, -1))]
S7 = {tuple(np.round((lambda U: (U @ U.T).flatten())(preserve((E[i] + s * E[j]) / np.sqrt(2))), 6)) for i, j, s in zd}
S7 = [np.array(k).reshape(16, 16) for k in S7]
inter = lambda A, B: int((np.linalg.eigvalsh(A + B) > 2 - 1e-6).sum())
news, leaks, dims, hits = [], [], [], 0
for _ in range(60):
    a = rng.normal(size=16); a /= np.linalg.norm(a); U = preserve(a); P = U @ U.T; dims.append(U.shape[1])
    leaks.append(max(np.linalg.norm((lambda p: p - U @ (U.T @ p))(mul(U[:, x], U[:, y]))) for x in range(U.shape[1]) for y in range(U.shape[1])))
    hits += any(np.linalg.norm(P - Q) < 1e-6 for Q in S7); news.append(P)
print('60 random unit sedenions: gain-1 subspace dims', sorted(set(dims)), '; max leakage %.1e ; equal to one of THE SEVEN: %d' % (max(leaks), hits))
print('pairwise intersections among 20 of the new ones:', sorted({inter(P, Q) for P, Q in itertools.combinations(news[:20], 2)}), '; among THE SEVEN:', sorted({inter(P, Q) for P, Q in itertools.combinations(S7, 2)}))
for name, d in (('H', 4), ('O', 8)):
    ix, sx = tables(d); dets = []
    for _ in range(500):
        v = rng.normal(size=d); v /= np.linalg.norm(v); dets.append(abs(np.linalg.det(Lm(ix, sx, v))))
    print('%s: min |det L_v| over 500 random unit v = %.10f' % (name, min(dets)))
print('S: singular L_a among the 84 diagonals:', len(zd), 'of', len(zd))
def stats(d):
    ix, sx = tables(d); m = lambda x, y: Lm(ix, sx, x) @ y; A, N, C = [], [], []
    for _ in range(300):
        x, y, z = [(lambda v: v / np.linalg.norm(v))(rng.normal(size=d)) for _ in range(3)]
        A.append(np.linalg.norm(m(m(x, y), z) - m(x, m(y, z)))); N.append(abs(np.linalg.norm(m(x, y)) - 1)); C.append(np.linalg.norm(m(x, y) - m(y, x)))
    return np.mean(A), np.mean(N), np.mean(C)
for name, d in (('H (4)', 4), ('O (8)', 8), ('S (16)', 16)):
    a, n, c = stats(d); print('%-7s mean associator %.2e  mean | |xy| - 1 | %.2e  mean commutator %.3f' % (name, a, n, c))
st = {}
for i, j, s in zd: st.setdefault(i ^ j, []).append((i, j, s))
print('84 diagonals; per strut', sorted({len(v) for v in st.values()}), '; inside one octonion, per strut:', sorted({len([z for z in zd if (z[0] ^ z[1]) == t and np.linalg.norm(S7[0] @ (E[z[0]] + z[2] * E[z[1]]) - (E[z[0]] + z[2] * E[z[1]])) < 1e-9]) for t in st}))
```

```
60 random unit sedenions: gain-1 subspace dims [8] ; max leakage 7.0e-15 ; equal to one of THE SEVEN: 0
pairwise intersections among 20 of the new ones: [2] ; among THE SEVEN: [4]
H: min |det L_v| over 500 random unit v = 1.0000000000
O: min |det L_v| over 500 random unit v = 1.0000000000
S: singular L_a among the 84 diagonals: 84 of 84
H (4)   mean associator 1.57e-16  mean | |xy| - 1 | 6.70e-17  mean commutator 1.126
O (8)   mean associator 1.11e+00  mean | |xy| - 1 | 7.03e-17  mean commutator 1.607
S (16)  mean associator 1.29e+00  mean | |xy| - 1 | 7.29e-02  mean commutator 1.791
84 diagonals; per strut [12] ; inside one octonion, per strut: [0, 4]
```

(The last line of the listing counts, for the first of the seven octonions, the diagonals that lie inside it, by strut: 4 on each of its three struts and 0 on the other four; the page's "84 → 12 → 4 → 2" is derived in §6.)

Reproduced: every one of 60 random unit sedenions has an 8-dimensional gain-1 subspace closed to 7×10⁻¹⁵, none of them is one of **the seven**, and the new ones meet pairwise in dimension 2 (just ℂ); the seven meet in dimension 4 (ℍ). The page's counts were 200 samples, 0 equal to
one of the seven, pairwise dimension 2. Without the definers there is no geometry: an uncountable family of octonions meeting only in ℂ with no incidence and no lines; with them, exactly 7 points, 7 quaternions and the Fano plane ([89](89_the_seven_octonions.md)). "The definers do not create the algebra below; they select the finite geometry out
of a continuum."

## 3. Definition is not possible from inside the child  `ESTABLISHED` (the determinants)

To define a structure you need something that annihilates, picking a proper subspace by sending the rest to zero. In a normed division algebra |det L_v| = |v|^dim, so for a unit element it is 1 always: min |det L_v| = 1.0000000000 over 500 random units in ℍ and in 𝕆 (Listing 1; the page tested 2000 each), with no partial degeneracy and no
near-singularity anywhere. In 𝕊 the 84 diagonals are singular (det exactly 0). So the instrument cannot exist in the child. The chain: to define you must annihilate; to annihilate you need zero divisors; they first appear at 𝕊; therefore 𝕆's geometry is visible only from 𝕊, and the 7 quaternions
exist as 𝕆's intersections selected only by 𝕊's definers. "A scope cannot define its own boundary" is the page's general reading (`INTERPRETATION`).

## 4. Reading, writing, speaking  `INTERPRETATION` over measured properties

The nesting 𝕊 ⊃ 𝕆 ⊃ ℍ carries three algebraic properties which the page matches to three modes of language (the properties are measured; the correspondence is proposed):

| | closed | bracketing (associator) | norm multiplicativity | mean commutator (Listing 1) |
|---|---|---|---|---|
| READING 𝕊 (16) | trivial | 1.29 | 7.3×10⁻² | 1.79 |
| WRITING 𝕆 (8) | rounding | 1.11 | 7×10⁻¹⁷ | 1.61 |
| SPEAKING ℍ (4) | rounding | 1.6×10⁻¹⁶ | 7×10⁻¹⁷ | 1.13 |

(The earlier page's numbers, 2.4 / 1.9 / 2.6×10⁻¹⁵ for the associator and 0.34 / 3×10⁻¹⁶ for the norm, are of the same orders and come from a different sampling or norm convention; the pattern is the same: ℍ associative to rounding, 𝕆 and 𝕊 not, only 𝕊 failing the multiplicative norm.) Speaking is a **subgroup**, writing a **subalgebra**: 𝕆's units fail
associativity (the unit octonions form a Moufang loop, not a group) while ℍ's form a genuine group (S³).

The page's "order dependence" column (ℍ: exactly 0, three bracketings agreeing to 2.77×10⁻¹⁶) is about **bracketing**, not about the order of the factors: ℍ is non-commutative (mean commutator 1.13, Listing 1), so xy ≠ yx there. What is exactly zero in ℍ is dependence on parenthesisation; grammar read as the bracketing is
what a group does not record, which is why "it aint not got to aks whudup" and "you should ask someone's name when you speak to them" can land in the same place. Reading and writing sit only about 8 % apart (1.909 and 1.766 on the earlier page) while speaking is a cliff to zero: the hierarchy is the associative one and everything else. And only the widest layer has zero divisors:
"you cannot say two things that cancel to nothing, and you cannot write them either, but you can read them" (`INTERPRETATION`).

## 5. Provenance is compiled, not discarded  `INTERPRETATION`, timings recorded

The obvious model of long-term memory strips the source and keeps the lesson; the page argues the history is still present, changed from something you replay into something you are. Recorded timings (this machine, 2026-08-16, **not re-run**):

```
build the geometry once   19.2 ms     query WITH geometry   19.2 µs     query WITHOUT (scan)   5.1 ms
speedup per query   265×             queries to amortise   3.8
```

Pays for itself in under four uses and then runs 265× faster, "muscle memory's exact economics". The geometry is the construction record: the strut label is i XOR j (the doubling operation itself) and generation depth is a difference of 2-adic valuations (which doubling a thing was born at). Mind's Eye keeps provenance as episodes
(explicit path, replayed, 5.1 ms), Paper's Hands as geometry (implicit shape, read off, 19.2 µs); the older canonical split reads Mind's Eye as additive (a cache accumulates) and Paper's Hands as subtractive (a skill is what survives pruning). Landauer's bound (erasing a bit costs kT ln 2; keeping one costs nothing) is the
standard footnote: a cache does not cheat entropy, it declines to pay until consolidation.

## 6. Two struts, one point, one bit that is yours  `ESTABLISHED`

Any two Fano lines meet in exactly one point, so naming a context line and a content line names one octonion and prunes the space (Listing 1: 12 diagonals per strut; 4 per strut inside one octonion):

```
84 → 12   fix one strut                    7×
   →  4   intersect the two                21×     95.24 % discarded
   →  2   add an orientation               42×     97.62 % discarded
```

(84/12 = 7, 84/4 = 21, 84/2 = 42; the "4 → 2" step is the choice of orientation, the sN = sA·sC bit of [89](89_the_seven_octonions.md) §5.) Uniform across all 21 strut pairs and both orientations: a guaranteed constant reached by index lookup. Three properties: the meet is neither input (the unique thing determined by the pair); the
prune is one-way (21 pairs land on 7 points, three pairs per point, so which pair produced a result is unrecoverable: a reduction you could invert would have discarded nothing); and the orientation cannot be inferred (it is the sN bit, invisible to every annihilation test) and must be declared: one bit, the only quantity in the structure that no input determines.

## 7. The fulcrum does no work  `INTERPRETATION` over an identity

A fulcrum is where chirality comes from, not where the work comes from. The orphan elements lie in no Assessor and carry no force ([87](87_the_boundary_lever.md)); the antisymmetric generator Σ has tr Σ = 0, so det exp(tΣ) = exp(t·tr Σ) = 1 at every t: the flow is volume-preserving by identity, not by tuning (an identity of the determinant and the trace; the measured statement is that
the generator used has zero trace). So leverage is a fictitious quantity in the sense that the centrifugal force is: a book-keeping term from describing real inertia in a rotating frame; the fulcrum supplies orientation, the inertia supplies the work.

## 8. Refuted along the way  `kept` (recorded; not re-run)

- Octonions are defined by zero divisors: false (every unit sedenion has one, Listing 1).
- A closed 8-dimensional subalgebra is rare: false.
- The V₄ orbit's 4 dimensions form a quaternion: false (leakage 1.000).
- That orbit carries a Klein-bottle involution: false: det = +1 (orientation-preserving) with two fixed directions; it is a torus involution.
- Grade agreement holds inside every box-kite: false: 12/12 for strut 9 only, 4–8/12 elsewhere, 47/84 overall; strut 9's distinction is confounded with construction order and untested.
- The defect field recovers the Fano lines: false (0/84, below chance).

## 9. Related pages

[89 the seven octonions](89_the_seven_octonions.md) · [87 the boundary lever](87_the_boundary_lever.md) · [88 the paper trail](88_the_paper_trail.md) · [17 α, Ω and d\*](17_alpha_omega_d_star.md)
