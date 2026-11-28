# 43 — The Emmy Noether Sedenion: the naming, and what the name rests on

| | |
|---|---|
| Status | **A naming decision (2026-06-03), in force across the papers: the 16-dimensional Cayley–Dickson algebra is called the *Emmy Noether Sedenion*, 𝕊_EN** (also "EN-Sedenion", "Noether Sedenion"). The mathematical justification offered on the earlier page is corrected below; the prize table is superseded |
| Author's account (2026-11-13) | the sedenion is named for her because *her mathematics had this shape in 1915, though not in this form* ([25](25_sedenion_manual.md) §4): the conserved-current balance. This is the operative reason |
| Code | `VAPMIP/monad.py` (the sedenion is "the CAM, Emmy Noether Sedenion"; the CRANK is the Ĥ_RB field engine); Listing 1 |
| Last verified | 2026-11-13: Listing 1 executed; biographical statements checked against the standard accounts |

## 1. The decision

Notation 𝕊_EN in formal contexts; "the Emmy Noether Sedenion" in text. It names the
algebra; it makes no claim that Noether wrote about sedenions (she did not).

## 2. What the name rests on  (corrected)

The earlier page said the naming is "mathematically exact" because every
structural result about the algebra derives from her mathematics. Item by item:

| Claim | Assessment |
|---|---|
| **The isomorphism theorems** govern the algebra's subalgebras, ideals and quotients | They are stated for rings and modules, and are due to Noether's formulation (`ESTABLISHED`). 𝕊 is a **non-associative** algebra, not a ring in her sense; the theorems apply to its associative structure (and to its linear-space quotients), not to the algebra as a whole |
| **Noetherian**: the algebra satisfies the ascending chain condition on ideals, "so its ideal structure is finite and tractable" | True but trivial: 𝕊 is a 16-dimensional real vector space, so every ascending chain of subspaces, and so of ideals, stabilises. Its "tractability" is not a property of Noetherianity beyond finite dimension |
| **Zero-divisors are ideals** in the Noetherian sense; "the zero-divisor manifold (S⁷ within 𝕊_EN) is a Noetherian ideal structure made geometric" | **False as written.** The set of zero-divisors of 𝕊 is not closed under addition and is not an ideal (a sum of zero-divisors need not be one). Nor is it S⁷: S⁷ is 7-dimensional. The structure that is known: 84 zero-divisors of the form e_i ± e_j ([25](25_sedenion_manual.md) §4; Listing 1), organised in box-kites ([84](84_the_box_kite_debugger.md)); the unit zero-divisors of the sedenions are reported (Moreno, 1998, to be verified) to form a space related to G₂ |
| **Representation theory**: her founding work on how algebras act on vector spaces; the σ-face map, the HSR metric and Ĥ_RB are "representations in her sense" | She did lay foundations of the representation theory of algebras (`ESTABLISHED`). Calling the framework's maps representations is a reading: no representation of 𝕊 on a vector space is written down on this page |
| **Conservation laws**: "σ = ½ is the conserved charge of the Fermat–Riemann symmetry, a direct application of her theorem to the algebra's automorphism group" | Noether's theorem concerns continuous symmetries of an action ([38](38_fermat_riemann_negative_space.md) §6: the application to the Fermat–Riemann duality is `CONJECTURE`). The automorphism group of 𝕊 is not the symmetry group of a stated action here |

What survives as an accurate reason: the **conserved-current balance** that the
framework carries in the sedenion's three octonion slots has the form of her
theorem ([25](25_sedenion_manual.md) §4; [05](05_noether_engine.md)), and the
naming honours that. The name is a dedication and a statement of lineage, and the
page's earlier claim that it is mathematically exact is withdrawn.

**Listing 1 — the algebra the name is given to** (written for this page; runs
cold; the doubling of [19](19_cayley_dickson_tower.md))

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

e = lambda i: [1.0 if k == i else 0.0 for k in range(16)]
add = lambda a, b, s: [x + s * y for x, y in zip(a, b)]
nrm = lambda a: sum(x * x for x in a) ** 0.5
a = add(e(1), e(10), 1)      # e1 + e10
b = add(e(4), e(15), -1)     # e4 - e15
print('(e1+e10)(e4-e15) =', nrm(mul(a, b)) < 1e-12, '  (a zero product of non-zero elements)')
s = add(a, add(e(2), e(9), 1), 1)    # a + (e2 + e9): is the sum of two zero-divisors a zero-divisor?
partners = [(k, l, t) for k in range(1, 8) for l in range(8, 16) for t in (1, -1)
            if nrm(mul(s, add(e(k), e(l), t))) < 1e-12]
print('a + (e2+e9) has a zero-product partner among the e_k +/- e_l forms:', bool(partners))
```

```
(e1+e10)(e4-e15) = True   (a zero product of non-zero elements)
a + (e2+e9) has a zero-product partner among the e_k +/- e_l forms: False
```

The second line is a witness (not a proof) that the zero-divisors are not
closed under addition: the sum of two zero-divisors, e₁+e₁₀ and e₂+e₉, has no
partner among the 84 forms. (A full test would search all of 𝕊 for a partner.)

## 3. The history, as it is told

Emmy Noether (1882–1935) proved the theorem relating continuous symmetries to
conserved currents in 1915 (published 1918, *Invariante Variationsprobleme*; the
dates as given in the standard accounts); built the abstract algebra of the 1920s
(ideal theory, the ascending chain condition, the "Noetherian" rings); lectured
for years under David Hilbert's name because the faculty would not allow her to
lecture under her own; was dismissed from Göttingen in 1933 under the Nazi
government's civil-service law; took a position at Bryn Mawr College and died
there in 1935, aged 53, following surgery; her ashes were placed beneath the
cloister walkway of the Bryn Mawr library. (Details, including the cause of
death and the exact placement of the ashes, are from the standard biographies and
are to be cited in [99](99_emmy_noether.md).)

## 4. Hilbert's remark

The words quoted in every paper of the series are attributed to Hilbert at the
1915 Göttingen faculty debate on her Habilitation: *"I do not see that the sex of
the candidate is an argument against her admission as Privatdozent. After all, we
are a university, not a bathing establishment."* The wording is as it is widely
quoted; the exact original (the German, and the wording of the record) is to be
checked at a source before it is cited as a quotation. "He lost the formal battle":
she was habilitated in 1919.

## 5. The prize table (2026-06-03): superseded

The earlier page distributed hypothetical Clay Millennium prize money among Bryn
Mawr College, Göttingen, the Riemann Institute, the Institute for Advanced Study
and the author, on the premise that the framework resolves the Clay problems and that
the algebra's results are "her theorem is Yang–Mills", "Noether–Lefschetz is Hodge",
"her algebra is BSD's language". That table is **withdrawn**: (i) none of the problems
is solved here ([13](13_omgwtf_rh_proof.md), [42](42_rh_proof_no_primes.md),
[105](105_the_millennium_problems_in_ainulindale.md): the Clay modules are built to
probe the operator's reach and are not prize claims, and their statuses are
facets, not solutions); (ii) the identifications are not accurate (the
Noether–Lefschetz theorem concerns the Picard group of a surface in ℙ³ and is a
relative of the Hodge conjecture, not the conjecture; Yang–Mills existence and mass gap
is not Noether's theorem); (iii) the Clay rules require publication and a waiting
period. What stands from that section is the author's intent of the ordering of
credit: the naming of the algebra for Emmy Noether is the lasting honour the
page values over any money.

## 6. Related pages

[05 Noether engine](05_noether_engine.md) · [19 Cayley–Dickson tower](19_cayley_dickson_tower.md) ·
[25 Sedenion manual](25_sedenion_manual.md) · [99 Emmy Noether](99_emmy_noether.md) ·
[105 The Millennium Problems](105_the_millennium_problems_in_ainulindale.md)
