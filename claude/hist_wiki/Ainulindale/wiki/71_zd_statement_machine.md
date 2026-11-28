# 71 — The Sedenion Statement Machine

| | |
|---|---|
| Scope | zero-divisors as a lookup that replaces a full product; the relations a zero-divisor pair imposes; the prime "leaves"; the sphere/n-ball crossing; emergence and immergence |
| Origin | 2026-06-26, stated by the author |
| Predecessors | [70](70_precession_stroke_oblique_crank_trine.md), `zero_lattice.py` v0.100, `fixed_point.py` v0.100 |
| Code | `ValaQuenta/zero_lattice.py` (`find_zd_pairs`, `classify_zd_pairs`, `build_tree`), `fixed_point.py` |
| Paper | "How an Addition EQUALS a Subtraction"; FourthAgePapers `ZeroTree/` |
| Confidence | counts, the two relations and the n-ball crossing: ESTABLISHED (Listing 1) · the "statement machine / production rules" reading: `INTERPRETATION` · the prime-leaf table: recorded, **not reproduced** (§4) · the page's original status line, "ESTABLISHED (zero free parameters, verified)", applies to the first row only |
| Last verified | 2026-11-13: Listing 1 and the engine run in §2 executed; their output is quoted below |

## 1. The claim and the cost argument  `INTERPRETATION`

A full sedenion product costs 256 basis multiplications (a 16 × 16 table of sign and
index). A zero-divisor pair check is a table lookup: if the pair (eᵢ + eⱼ, eₖ + eₗ)
belongs to a known zero-product class the product is exactly zero and the computation can
stop. So 256 operations become one lookup. The page calls the algebra a statement machine:
a product question ("what is this product?") becomes a logical proposition ("is this a
zero-divisor pair?") that answers true and terminates.

The cost statement is correct for inputs that are already given as sums of two basis
elements, where the lookup applies. A general element is a sum of sixteen terms and is
not a zero-divisor unless it lies in the set; the lookup does not replace the product for
those. The reading as a formal grammar (input a pair, check the classes, fire or
compute) is the framework's way of describing the engine's shortcut.

## 2. The counts and the relations  `ESTABLISHED`

The two polynomial relations the page gives, for (eᵢ + eⱼ)(eₖ + eₗ) = 0:

```
eᵢeₖ = −(eⱼeₗ)   and   eᵢeₗ = −(eⱼeₖ)
```

**Listing 1 — the counts, the relations, and the sphere/n-ball crossing** (written for this page; needs scipy; basis convention of [19](19_cayley_dickson_tower.md) Listing 1; runs cold)

```python
import math, itertools
from scipy.special import gamma
from scipy.optimize import brentq, minimize_scalar
def conj(a): return [a[0]] + [-x for x in a[1:]] if len(a) > 1 else list(a)
def mul(a, b):
    if len(a) == 1: return [a[0] * b[0]]
    h = len(a) // 2; a1, a2, b1, b2 = a[:h], a[h:], b[:h], b[h:]
    t1, t2, t3, t4 = mul(a1, b1), mul(conj(b2), a2), mul(b2, a1), mul(a2, conj(b1))
    return [x - y for x, y in zip(t1, t2)] + [x + y for x, y in zip(t3, t4)]
def e(i): v = [0.0] * 16; v[i] = 1.0; return v
zd = [(i, j, s) for i in range(1, 8) for j in range(8, 16) for s in (1, -1)]
pairs = []
for a, b in itertools.combinations(zd, 2):
    x = [p + a[2] * q for p, q in zip(e(a[0]), e(a[1]))]; y = [p + b[2] * q for p, q in zip(e(b[0]), e(b[1]))]
    if max(abs(v) for v in mul(x, y)) < 1e-12 and max(abs(v) for v in mul(y, x)) < 1e-12: pairs.append((a, b))
zds = {z for p in pairs for z in p}
print('candidates', len(zd), '| zero-divisors with a partner', len(zds), '| unordered zero-product pairs', len(pairs),
      '| index pairs {i,j}', len({(z[0], z[1]) for z in zds}))
def pi_(i, k):
    p = mul(e(i), e(k)); m = max(range(16), key=lambda t: abs(p[t])); return m, p[m]
ok = tot = 0
for a, b in pairs:
    if a[2] == 1 and b[2] == 1:
        tot += 1; (m1, s1), (m2, s2), (m3, s3), (m4, s4) = pi_(a[0], b[0]), pi_(a[1], b[1]), pi_(a[0], b[1]), pi_(a[1], b[0])
        ok += (m1 == m2 and s1 == -s2) and (m3 == m4 and s3 == -s4)
print('(++) pairs satisfying both relations:', ok, '/', tot)
V = lambda n: math.pi ** (n / 2) / gamma(n / 2 + 1)
pk = minimize_scalar(lambda n: -V(n), bounds=(3, 8), method='bounded')
kx = brentq(lambda k: math.sin(math.pi * k / 8) - V(2 ** k) / V(pk.x), 2.2, 3.4)
print('n-ball peak n=%.4f V=%.4f ; crossing of sin(pi k/8) and V(2^k)/Vpeak: k=%.3f n=%.3f sigma=1-k/4=%.3f value=%.3f'
      % (pk.x, V(pk.x), kx, 2 ** kx, 1 - kx / 4, math.sin(math.pi * kx / 8)))
for k in (0, 2, 4, 8): print('  k=%d sin=%.3f  V(2^k)/Vpeak=%.4f  V(2^k)=%.4f' % (k, math.sin(math.pi * k / 8), V(2 ** k) / V(pk.x), V(2 ** k)))
```

```
candidates 112 | zero-divisors with a partner 84 | unordered zero-product pairs 168 | index pairs {i,j} 42
(++) pairs satisfying both relations: 42 / 42
n-ball peak n=5.2569 V=5.2778 ; crossing of sin(pi k/8) and V(2^k)/Vpeak: k=2.811 n=7.020 sigma=1-k/4=0.297 value=0.893
  k=0 sin=0.000  V(2^k)/Vpeak=0.3789  V(2^k)=2.0000
  k=2 sin=0.707  V(2^k)/Vpeak=0.9350  V(2^k)=4.9348
  k=4 sin=1.000  V(2^k)/Vpeak=0.0446  V(2^k)=0.2353
  k=8 sin=0.000  V(2^k)/Vpeak=0.0000  V(2^k)=0.0000
```

What it fixes:

- Of the 112 sums eᵢ ± eⱼ (i in 1–7, j in 8–15), 84 are zero-divisors with a partner,
  on 42 index pairs {i, j}. Counting every sign combination there are 168 unordered
  zero-product pairs. The page's "42 unordered classes, 84 directed pairs, the complete
  statement set" is therefore a count of classes and of zero-divisors, and the
  number of zero-product *pairs* is 168 (336 ordered) when all sign patterns are included.
- Both polynomial relations hold for all 42 (++) pairs: the page's statement is correct.
  The absorbing of non-commutativity and non-associativity is accurate in the
  sense that the two relations hold for each pair; "collapses to a polynomial ring with 42
  relations" is a framing and no ring is constructed.
- The sphere/n-ball crossing reproduces exactly: k = 2.811, n = 7.020, σ = 0.297, value
  0.893. The page's table entry "k = 2: N-ball 0.935" is correct (0.9350); the n-ball
  at the sedenion level is V(16) = 0.2353, which is 4.5 % below d* = 0.24631 (relevant to
  [72](72_the_cosmic_telescope.md) §11, where V(16) ≈ d* is written).
  The sphere cross-section used is sin(πk/8) (the page does not state its form; this
  is the form that gives the page's values 0, 0.707, 1, 0). That the crossing
  falls at n ≈ 7, the number of imaginary octonion units, is a numerical observation.

**The engine's own count** (`ValaQuenta/zero_lattice.py`, run 2026-11-13): `find_zd_pairs()`
returns 84 pairs on 42 distinct index quadruples; `classify_zd_pairs` splits them into 12
`odd_sector`, 72 `mixed`, 0 `even_sector`. (This engine labels its basis by its own
convention, so a quadruple such as (1, 10)(5, 14) has different labels from the Cayley–Dickson
basis of Listing 1; the counts agree.)

## 3. Emergence and immergence  `INTERPRETATION`

| Direction | Through the tower | What the page says happens |
|---|---|---|
| Emergence | root → leaf, T₂₅₆ → ℝ | zero-divisor crossings, non-associativity and non-commutativity clear; the Vector appears; subtraction and division become distinct; primes fall off as leaves; the machine outputs |
| Immergence | leaf → root, ℝ → T₂₅₆ | subtraction and division dissolve into each other; at k = 4, eᵢeₖ = −(eⱼeₗ), addition becomes subtraction; by T₂₅₆ division has failed completely (255 imaginary units, 32 Fano planes) |

"Addition becomes subtraction" at k = 4 is the relation of §2: a sum of products equals a
negated sum of products, which is impossible in the division algebras ℝ, ℂ, ℍ, 𝕆 and is the
content of the paper's title. The crossing at n ≈ 7 is the page's handoff: below it the
geometry (the sphere cross-section) dominates; above it the volume (the n-ball, "the
Vector"). Both functions are non-zero where the other peaks (at the n-ball peak the sphere
term is 0.809; at the sphere maximum the n-ball is 0.045).

## 4. The prime leaves  recorded, not reproduced

The page states that each odd-sector constellation carries a minimum prime (the leaf
weight), e.g. (e₁+e₁₁)(e₅+e₁₅) = 0 with primes {2, 13, 5, 19} and leaf 2; that the leaves
are exactly the real primes {2, 3, 5, 7, 11, 13, 17}; and that the Euler product of the
Zero Lattice is the first seven primes exactly. With the assignment eₖ ↔ the k-th
prime used elsewhere in the project (e₀ = 2, e₁ = 3, … e₁₅ = 53) the engine's six all-odd-index
quadruples have primes

```
(1, 3, 13, 15) → {3, 7, 43, 53}   min 3      (3, 5, 9, 15) → {7, 13, 29, 53}   min 7
(1, 5, 11, 15) → {3, 13, 37, 53}  min 3      (3, 7, 9, 13) → {7, 19, 29, 43}   min 7
(1, 7, 11, 13) → {3, 19, 37, 43}  min 3      (5, 7, 9, 11) → {13, 19, 29, 37}  min 13
```

so the minima are 3, 7 and 13, not the sequence 2, 3, 5, …, and the prime 2 (index 0)
does not appear in an odd-index quadruple. The page's prime table uses a different
prime assignment from the one that can be reconstructed from the engine's quadruples;
that assignment is not in the cells read for this page. Until it is located, the
statements "leaves are exactly the first seven primes" and "ζ_T(s) is the first seven
primes' Euler product" are recorded results (`CONJECTURE`), and the e₁₅ ("Monster gap,
prime 19, always shadowed") statement likewise. The number 12 of odd-sector constellations
appears in the engine's classification (§2); the page's "12 odd-sector" counts
quadruple-with-sign-pattern, not the six distinct index sets.

## 5. Zork provenance

"go north" is a pattern match to an action with no arithmetic; a zero-divisor
crossing (eₐ + e_b)(e_c + e_d) = 0 is a pattern match to zero with no arithmetic. The page
reads the LSHS speaking model as a statement machine built on the same principle:
pattern → statement → terminate expensive computation. The parser is prior work the
author engineered with, and the comparison is the author's.

## 6. Key numbers (current)

| Quantity | Value | Source |
|---|---|---|
| zero-divisors eᵢ ± eⱼ | 84 | Listing 1 |
| index pairs | 42 | Listing 1 |
| unordered zero-product pairs, all signs | 168 | Listing 1 |
| engine `find_zd_pairs` | 84 pairs on 42 quadruples; 12 odd-sector, 72 mixed | engine run |
| yin-yang crossing | k = 2.811, n = 7.020, σ = 0.297, value 0.893 | Listing 1 |
| full product cost | 256 | the 16 × 16 table |
| leaf-prime table, Euler product of 7 primes | not reproduced | §4 |

## 7. Related pages

[19 the Cayley–Dickson tower](19_cayley_dickson_tower.md) · [25 the sedenion manual](25_sedenion_manual.md) ·
[31 cavitation, causality and Fermat](31_cavitation_causality_fermat.md) · [70](70_precession_stroke_oblique_crank_trine.md) ·
[72 the cosmic telescope](72_the_cosmic_telescope.md)
