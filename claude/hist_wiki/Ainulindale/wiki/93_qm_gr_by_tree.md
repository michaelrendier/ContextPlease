# 93 — QM and GR by Tree: a Tested Conjecture

| | |
|---|---|
| Scope | the author's conjecture "quantum mechanics exists only in Telperion and GR only in Laurelin", tested by counting non-commutativity and the associator in the two octonions of the sedenion |
| Measured | 2026-08-22; continues [92](92_ring_theory_spine.md) |
| Code | `ContextPlease/claude/scratchpad/2026-08-22_qm_gr_by_tree/qm_gr_test.py`, run against `GenerationalLineage/engine/lineage.py` (named SedenionFactoralRelativity at the time) |
| Confidence | the counts: ESTABLISHED (re-run with an independent table builder, 2026-11-13) · the verdict "FALSE as stated": ESTABLISHED · the proxies (non-commutativity for QM, the associator for GR) and the "gravity is the curvature of the seam" reading: `INTERPRETATION` |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The conjecture

The author, 2026-08-22: "Does quantum mechanics exist only in Telperion and GR exist only in Laurelin?" QM's signature is taken as non-commutativity ([x, p] ≠ 0); GR's as curvature, identified in [90](90_divisors_are_definers.md) and the UDEO white paper (§2.5) with the associator (ab)c − a(bc). The sedenion splits 𝕊 = 𝕆 ⊕ 𝕆 into two octonions, the two trees, so the
test is direct: does non-commutativity segregate to one tree and curvature to the other? Reported by *content* (lower octonion e₀–e₇, upper octonion e₈–e₁₅) because the Telperion/Laurelin label is applied inconsistently across the repositories (the generational-lineage skill calls Telperion "Blue/lower"; the engine comment calls the upper octonion Telperion): an open cleanup, not fixed here.

## 2. The measurement  `ESTABLISHED`

**Listing 1 — non-commutativity and associator counts by tree** (written for this page; needs numpy; runs cold)

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
idx, sg = tables(16); prod = lambda i, j: (idx[i, j], sg[i, j])
comm = lambda i, j: prod(i, j) == prod(j, i)
cnt = lambda R: (sum(not comm(i, j) for i, j in itertools.combinations(R, 2)), len(list(itertools.combinations(R, 2))))
print('non-commuting pairs: lower', cnt(range(8)), ' upper', cnt(range(8, 16)), ' across', (sum(not comm(i, j) for i in range(8) for j in range(8, 16)), 64))
def assoc_zero(i, j, k):
    a, s1 = prod(i, j); b, s2 = prod(a, k); c, s3 = prod(j, k); d, s4 = prod(i, c); return (b, s1 * s2) == (d, s3 * s4)
ac = lambda T: (sum(not assoc_zero(*t) for t in T), len(T))
allt = list(itertools.permutations(range(16), 3)); cross = [t for t in allt if not (all(x < 8 for x in t) or all(x >= 8 for x in t))]
print('associator != 0: within lower', ac(list(itertools.permutations(range(8), 3))), ' within upper', ac(list(itertools.permutations(range(8, 16), 3))), ' crossing', ac(cross))
n_all, n_cross = ac(allt)[0], ac(cross)[0]; print('all distinct ordered triples: %d nonzero; crossing share %.1f%%' % (n_all, 100 * n_cross / n_all))
i8, s8 = tables(8)
nz8 = sum(1 for i, j, k in itertools.permutations(range(8), 3) if (i8[i8[i, j], k], s8[i, j] * s8[i8[i, j], k]) != (i8[i, i8[j, k]], s8[j, k] * s8[i, i8[j, k]]))
print('octonions (dim 8): nonzero associators over distinct ordered triples:', nz8, '/ 336')
```

```
non-commuting pairs: lower (21, 28)  upper (28, 28)  across (56, 64)
associator != 0: within lower (168, 336)  within upper (336, 336)  crossing (1344, 2688)
all distinct ordered triples: 1848 nonzero; crossing share 72.7%
octonions (dim 8): nonzero associators over distinct ordered triples: 168 / 336
```

| | both lower (e₀–e₇) | both upper (e₈–e₁₅) | across the boundary |
|---|---|---|---|
| non-commuting pairs (QM proxy) | 21/28 (75 %) | 28/28 (100 %) | 56/64 (88 %) |
| associator ≠ 0 over ordered triples (GR proxy) | 168/336 (50 %) | 336/336 (100 %) | 1344/2688 (50 %) |

Of all 1848 curvature events, 27 % lie within one tree and 73 % (72.7 %) cross the boundary. Every number matches the 2026-08-22 record.

## 3. Verdict: the literal conjecture is FALSE

Both signatures live in both trees; each octonion is a complete copy of 𝕆 and carries the full non-commutative and non-associative structure. Three true things came out instead:

**1. QM and GR are different rungs, not different trees.** Non-commutativity first appears at dim 4 (ℍ), the associator at dim 8 (𝕆): consecutive generations (the loss of commutativity ℂ → ℍ, then of associativity ℍ → 𝕆), a **radial** distinction along the tower (the σ axis, matching the engine's facet ladder: QM/Riemann at σ = ½, GR at σ = 2), whereas Telperion-versus-Laurelin is **angular** (which octonion).
The conjecture conflated the two axes. (The facet ladder is the framework's table of [14](14_redblue_hamiltonian.md) §4, a vocabulary correspondence.)

**2. Curvature is mostly a boundary phenomenon.** 73 % of curvature events cross the boundary between the trees, so by this proxy it belongs to the **coupling** between them (the zero-divisor boundary, σ = ½, "the corpus callosum", [80](80_aphasia_zd_reframe_memory.md)). The page's reading: "gravity is the curvature of the seam where the two trees couple", a measured version of "spacetime is the boundary". As with every "gravity" statement in this wiki, this is the proxy's reading (an associator count) and not a derivation of
general relativity; and the "73 % crossing" must be read against the base rate: crossing triples are 2688 of the 3360 ordered triples (80 %), so the 73 % share is *below* their share of triples; the crossing rate (50 %) equals the lower tree's, and it is the upper tree (100 %) that raises the intra-tree share. What the count establishes is that most curvature events involve both trees because most triples do.

**3. The trees are asymmetric, and the cause is e₀.** The upper octonion is 100 %/100 % (maximally non-commuting and curved), the lower only 75 %/50 %: the lower contains e₀ (the real axis, gain 1, ∅_RB), which commutes and associates with everything and softens the whole tree; the upper is pure imaginary. So the real split is not QM against GR but classical-anchored against pure-dynamics. The structure constants are
the same octonion table read in both trees; all that differs is whether e₀ is in the room.

## 4. Summary

| claim | status |
|---|---|
| QM only in one tree, GR only in the other | **FALSE**: both in both |
| QM and GR are consecutive tower rungs (dim 4, dim 8) | measured |
| curvature events are 73 % boundary-crossing | measured; the base rate is 80 % (crossing triples are 2688 of 3360), so this is not an enrichment |
| the trees split by e₀ (classical anchor) against pure imaginary | measured |

## 5. The loose end

The Telperion/Laurelin ↔ lower/upper octonion assignment is inconsistent across the repositories (skill: Telperion = Blue/lower; engine: Telperion = upper). Recorded as an open cleanup, to be reconciled once against a single source of truth ([135](135_engine_findings_ledger.md), row X-20).

## 6. Related pages

[92 the ring-theory spine](92_ring_theory_spine.md) · [90 divisors are definers](90_divisors_are_definers.md) · [89 the seven octonions](89_the_seven_octonions.md) · [80](80_aphasia_zd_reframe_memory.md) · [94](94_mathematical_xray_crystallography.md)
