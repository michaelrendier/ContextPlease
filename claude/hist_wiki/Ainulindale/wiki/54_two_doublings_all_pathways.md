# 54 — "Two doublings expose all pathways": the pathway count, and why the theorem has no content yet

| | |
|---|---|
| Status | **Cascade capture (2026-06-13), "general theorem; [53](53_t256_cryptographic_transparency.md) is one instance". `CONJECTURE`. The engine written to test it (e11) passes its checks, and the pathway count it measures is the combinatorial n(n−1), which grows with every doubling and does not saturate after two (§2)** |
| Code | `VAPMIP/engines/e11_two_doublings.py` (run 2026-11-13); Listing 1 |
| Last verified | 2026-11-13: e11 run; Listing 1 executed |

> *"Two Cayley–Dickson tower doublings expose all pathways. It's all watching a point-by-point along a path: evolution … involution …"*

## 1. The statement

Two Cayley–Dickson doublings from any level expose all pathways at that level: from ℝ
to ℍ (all 3-D rotational pathways), from ℂ to 𝕆 (all G₂ pathways), from ℍ to 𝕊 (all
zero-divisor pathways), from 𝕊 to T₆₄, from T₆₄ to T₂₅₆ (all 256-bit cryptographic
pathways). Why two and not one or three: one doubling shows one face of the "coin" (the
forward pathway and its conjugate) but not the cross-term between two doubled units,
which "is what J₂ requires"; the second doubling introduces the second pair with its own
conjugation and the cross-term, "both faces visible, the whole coin"; a third doubling
adds more zero-divisors but "no new faces", "same two faces, exponentially finer
resolution". With the product (a, b)(c, d) = (ac − d*b, da + bc*).

## 2. The measurement

`e11` defines a *pathway* as a distinct non-zero basis product: a quadruple (i, j, k, sign)
with e_i·e_j = sign·e_k, for i ≠ j, at level n. Its output (2026-11-13):

| Level (n) | paths | new at this level | lower |
|---|---|---|---|
| 1 (n = 2) | 2 | 2 | 0 |
| 2 (n = 4) | 12 | 10 | 2 |
| 3 (n = 8) | 56 | 44 | 12 |
| 4 (n = 16) | 240 | 184 | 56 |

and, growth from each base: from ℂ: 2 → 12 → 56 (ratios 6.000 → 4.667); from ℍ:
12 → 56 → 240 (4.667 → 4.286); from 𝕆: 56 → 240 → 992 (4.286 → 4.133). The engine also
reports "J₂ = the 4th-doubling cross-term: PASS (the upper half maps to the lower: True)".

**Listing 1 — what the count is** (written for this page; runs cold)

```python
def conj(a):
    return [a[0]] + [-x for x in a[1:]] if len(a) > 1 else list(a)

def mul(a, b):
    if len(a) == 1:
        return [a[0] * b[0]]
    h = len(a) // 2
    a1, a2, b1, b2 = a[:h], a[h:], b[:h], b[h:]
    t1, t2, t3, t4 = mul(a1, b1), mul(conj(b2), a2), mul(b2, a1), mul(a2, conj(b1))
    return [x - y for x, y in zip(t1, t2)] + [x + y for x, y in zip(t3, t4)]

e = lambda i, n: [1.0 if k == i else 0.0 for k in range(n)]

def pathways(n):
    """e11's definition: distinct (i, j, k, sign) with e_i * e_j = sign * e_k, i != j"""
    out = set()
    for i in range(n):
        for j in range(n):
            if i != j:
                p = mul(e(i, n), e(j, n))
                for k, v in enumerate(p):
                    if abs(v) > 1e-12:
                        out.add((i, j, k, round(v)))
    return out

counts = {n: len(pathways(n)) for n in (2, 4, 8, 16, 32)}
print('pathways(n)       :', counts)
print('n*(n-1)           :', {n: n * (n - 1) for n in counts})
ns = sorted(counts)
print('ratios of successive levels:', [round(counts[b] / counts[a], 3) for a, b in zip(ns, ns[1:])], '-> 4')
```

```
pathways(n)       : {2: 2, 4: 12, 8: 56, 16: 240, 32: 992}
n*(n-1)           : {2: 2, 4: 12, 8: 56, 16: 240, 32: 992}
ratios of successive levels: [6.0, 4.667, 4.286, 4.133] -> 4
```

The "pathway count" is exactly **n(n − 1)**, the number of ordered pairs of distinct basis
elements: every product of two distinct basis elements of a Cayley–Dickson algebra lands
on a single basis element (e_i·e_j = ±e_{i⊕j}), so each ordered pair is one pathway. It is
purely combinatorial: it grows by a factor tending to 4 at every doubling (6.0, 4.667,
4.286, 4.133, … → 4) and **does not stabilise after two doublings**, so the
measurement does not show that "two doublings expose all pathways". The "growth after
two doublings" in the engine's table is the same growth after one.

## 3. What the theorem can be made to say, and what it cannot

- **True and trivial:** 𝕆 is two doublings above ℂ, 𝕊 two above ℍ, T₆₄ two above 𝕊, T₂₅₆ two above T₆₄; the examples of §1 are the statement "N is two doublings above N/4". The first zero-divisors appear at 𝕊, which is two doublings above ℍ (and one above 𝕆) (`ESTABLISHED`; [19](19_cayley_dickson_tower.md), [25](25_sedenion_manual.md) §4).
- **The cross-term argument** (the second doubling "introduces the cross-term between two independently conjugated units, which is J₂"): J₂ as the swap of the two halves is not an automorphism of the product ([52c](52c_j2_involution_riemann_fermat.md) §2); the cross-terms of a doubling (−d*b and bc* in the formula) are present after *one* doubling (the first doubling, ℝ → ℂ, already contains the conjugation and cross-terms in its own degenerate form), so the asymmetry "one doubling half-expressed, two fully" has no basis in the formula. The e11 "PASS" is that the upper half maps to the lower under the swap, a statement about the indexing of the halves.
- **"The Cayley–Dickson doubling is an involution, its own inverse":** it is not. Doubling constructs a larger algebra from a smaller one; doubling twice gives the algebra of four times the dimension, not the original. (The *conjugation* is an involution; so is the grading (a, b) ↦ (a, −b), [52c](52c_j2_involution_riemann_fermat.md) §2.) "Point n + 2 contains the involution of point n" is a restatement that 𝔸_n sits inside 𝔸_{n+2} as a subalgebra.
- **The per-level table** (J₂ = quaternion conjugation at ℝ → ℍ; "octonion conjugation plus a cross-term" at ℂ → 𝕆; "the sedenion involution that maps each zero-divisor pair to its partner" at ℍ → 𝕊): quaternion and octonion conjugation are involutions (`ESTABLISHED`); the statement about zero-divisor partners is not computed here; the "J₂" of each row is a different map.

## 4. "Evolution and involution": the Mind's Eye two levels up  `interpretation`

Evolution: climbing the tower point by point, "each step an irreversible change" (the
record of the tower, L_(I|O), [52](52_l_dynamic_avoided_collaborator.md)). Involution: looking two steps
ahead, where both faces are visible; the Mind's Eye is "two levels up", the position from
which one watches both. "The path contains its own inversion", "the same structure as
prompt + response = 0". These are the author's images for the observer-above-the-system
position ([48](48_observer_fixed_point.md)). No calculation attaches to them.

## 5. "No hardness is fundamental"  (withdrawn as a statement of fact)

The page's consequence: "any hardness claim lives at some level of the tower; two
doublings above that level it is transparent; no hardness survives two doublings; T₂₅₆
cryptography is one instance". As in [53](53_t256_cryptographic_transparency.md) §2, this
confuses *the existence of an inverse in a larger algebra* with *an efficient way to
compute it*. Embedding a problem in a larger algebra gives no algorithm; and the
statement is self-defeating on its own terms: the 256-bit primitives of §1 live inside
T₂₅₆, which is itself two doublings below T₁₀₂₄, so "hardness at level n is transparent at
n + 2" would make *transparency* itself level-dependent, never absolute. Computational
hardness classes (P, NP, PSPACE, …) are not statements about an algebra's level, so a
theorem about doublings does not move them ([44](44_halting_problem_uns.md) §4–5).

## 6. Related pages

[19 Cayley–Dickson tower](19_cayley_dickson_tower.md) · [51 The J₂ involution](52c_j2_involution_riemann_fermat.md) ·
[53 T_256 and cryptographic transparency](53_t256_cryptographic_transparency.md) · [26 Roadmap and engine status](26_TODO_and_roadmap.md) ·
[55 Index, not value](55_index_not_value.md)
