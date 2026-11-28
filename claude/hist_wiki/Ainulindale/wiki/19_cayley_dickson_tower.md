# 19 — The Cayley–Dickson Tower

| | |
|---|---|
| Scope | the algebra tower ℝ → ℂ → ℍ → 𝕆 → 𝕊; what each doubling loses; how the framework reads the loss |
| Code | `ValaQuenta/modules/box_kite` (zero-divisor structure), `modules/tier8_sedenion`, `modules/archimedes_screw`; engine constants in `engine/constants.py` |
| Confidence | ESTABLISHED (the algebra) · THEORETICAL (the SMMIP reading of it) |
| Last verified | 2026-11-13: Listing 1 executed; its results are quoted below |

## 1. The tower

```
ℝ (1)  →  ℂ (2)  →  ℍ (4)  →  𝕆 (8)  →  𝕊 (16, the boundary)
```

Hurwitz's theorem (1898): exactly four normed division algebras exist: ℝ, ℂ,
ℍ, 𝕆. The Cayley–Dickson construction continues the doubling past 𝕆 into
the sedenions 𝕊, where division fails: zero-divisors appear and the norm is no
longer multiplicative. (`ESTABLISHED`.)

The framework's position is that its addressing scheme requires the same
algebras at the same levels as the information network does, and that the tower
was found rather than chosen. That is the author's account of the history; the
mathematics below does not depend on it.

## 2. The doubling, and what it loses

One doubling takes a pair (a₁, a₂) of elements of the smaller algebra to an
element of the next; the product is

```
(a₁, a₂)(b₁, b₂) = ( a₁b₁ − conj(b₂)·a₂ ,  b₂·a₁ + a₂·conj(b₁) )
```

**Listing 1 — the tower, and what each level keeps** (written for this page
from the formula above; not an extract from `ValaQuenta`, whose engines index
the basis by their own box-kite conventions; runs cold; random seed fixed)

```python
import math, random, itertools

def conj(a):
    return [a[0]] + [-x for x in a[1:]] if len(a) > 1 else list(a)

def mul(a, b):
    if len(a) == 1:
        return [a[0] * b[0]]
    h = len(a) // 2
    a1, a2, b1, b2 = a[:h], a[h:], b[:h], b[h:]
    t1, t2 = mul(a1, b1), mul(conj(b2), a2)
    t3, t4 = mul(b2, a1), mul(a2, conj(b1))
    return [x - y for x, y in zip(t1, t2)] + [x + y for x, y in zip(t3, t4)]

norm = lambda a: math.sqrt(sum(x * x for x in a))
rnd = lambda n: [random.uniform(-1, 1) for _ in range(n)]
dev = lambda p, q: max(abs(x - y) for x, y in zip(p, q))

random.seed(1)
for n, name in ((1, 'R'), (2, 'C'), (4, 'H'), (8, 'O'), (16, 'S')):
    x, y, z = rnd(n), rnd(n), rnd(n)
    print(name, n,
          'norm %.0e' % abs(norm(mul(x, y)) - norm(x) * norm(y)),
          'comm %.0e' % dev(mul(x, y), mul(y, x)),
          'assoc %.0e' % dev(mul(mul(x, y), z), mul(x, mul(y, z))),
          'alt %.0e' % dev(mul(x, mul(x, y)), mul(mul(x, x), y)))

def e(i):
    v = [0.0] * 16
    v[i] = 1.0
    return v

add = lambda a, b, s: [x + s * y for x, y in zip(a, b)]
for i, j in itertools.combinations(range(1, 16), 2):
    for k, l in itertools.combinations(range(1, 16), 2):
        for s, t in itertools.product((1, -1), repeat=2):
            if norm(mul(add(e(i), e(j), s), add(e(k), e(l), t))) < 1e-12:
                print('zero divisor: (e%d %+d e%d)(e%d %+d e%d) = 0' % (i, s, j, k, t, l))
                raise SystemExit
```

```
R 1 norm 0e+00 comm 0e+00 assoc 0e+00 alt 0e+00
C 2 norm 3e-17 comm 0e+00 assoc 3e-17 alt 1e-17
H 4 norm 0e+00 comm 6e-01 assoc 4e-16 alt 4e-16
O 8 norm 4e-16 comm 3e+00 assoc 5e+00 alt 4e-16
S 16 norm 8e-02 comm 4e+00 assoc 4e+00 alt 1e+00
zero divisor: (e1 +1 e10)(e4 -1 e15) = 0
```

(The random-draw values vary with the seed; only their order of magnitude matters. Values ≲ 10⁻¹⁵ are zero to rounding. The zero divisor is a property of the
algebra and its position depends on the basis convention.)

| Step | Property lost | Evidence in Listing 1 | What the framework reads it as |
|---|---|---|---|
| ℝ → ℂ | ordering (ℂ is not an ordered field; not tested by the listing) | — | phase: direction becomes meaningful; U(1) |
| ℂ → ℍ | commutativity | `comm` jumps from 0 to order 1 | rotation does not commute; SU(2) |
| ℍ → 𝕆 | associativity | `assoc` jumps from 10⁻¹⁶ to order 1 | the Fano plane governs the valid triples; G₂ / SU(3) |
| 𝕆 → 𝕊 | multiplicative norm and alternativity, hence division (zero-divisors) | `norm` 10⁻¹⁶ → order 10⁻¹; `alt` 10⁻¹⁶ → order 1; a zero divisor is found | the boundary; "training stops" |

The framework's reading is that the lost property is the signal carried by
that level: the impossibility of ordering ℂ is what makes phase meaningful, the
non-commutativity of ℍ is what makes rotation physical, and the
non-associativity of 𝕆 is what makes the Fano plane the geometry of the strong
interaction. The sedenion boundary is read as the correct termination, "the
Noether current's way of saying: no further". (`THEORETICAL`.)

## 3. Gauge groups  (Dixon; Furey)

Dixon (1994) and later Furey obtained U(1) × SU(2) × SU(3), the Standard
Model gauge group, from the tensor product ℝ ⊗ ℂ ⊗ ℍ ⊗ 𝕆. These are published
proposals, not a theorem that the Standard Model follows from the algebras; the
earlier wording "Dixon's theorem" overstated it.

| Algebra | Group | Force (as read) | Note |
|---|---|---|---|
| ℂ | U(1) | electromagnetism | |
| ℍ | SU(2) | weak | |
| 𝕆 | G₂ ⊃ SU(3) | strong | G₂ = Aut(𝕆); SU(3) is the subgroup fixing a complex structure |

The framework reports that the group emerged after the construction was
complete rather than being designed in. The group content is `ESTABLISHED`
as mathematics; its identification with the three forces is the proposal.

## 4. The two currents

Two flows run through the tower in opposite directions.

| Current | Direction | Role | In the code |
|---|---|---|---|
| Noether J^μ (forward) | ℝ → ℂ → ℍ → 𝕆 → (𝕊 boundary) | synthesis, "the Builder"; complexity escalation; the Red channel | `hear` ([15](15_the_monad.md)) |
| Noether information J_info (backward) | 𝕆 → ℍ → ℂ → ℝ | distillation, "the Evaluator"; reduction toward the prime; strips degrees of freedom | `speak` |

Going backward restores the lost properties in turn: associativity at 𝕆 → ℍ,
commutativity at ℍ → ℂ, ordering at ℂ → ℝ. The result at ℝ is cheap, stable
and addressable: the potential stays in the higher dimensions and the meaning
arrives in the reals. J_info is a `CONJECTURE` as a Noether current
([06](06_noether_information_engine.md)).

Where the two meet, the forward current (building) and the backward current
(stripping to the prime) interact; this interaction is read as spontaneous
symmetry breaking, and the crystal that forms is a prime: the Riemann–Fermat
Heartbeat, with inhalation (forward) and exhalation (backward). The code
names the weaving of the two the Topological Loom. How J_red and J_blue relate
to these two currents, and the status of J_red + J_blue = J_green, is in
[133](133_canonical_maths.md) §3.

## 5. σ = 0

At σ = 0 in the RedBlue operator, p⁰ = 1 for every prime and no prime is
distinguished ([14](14_redblue_hamiltonian.md) §4). The framework reads this as
simultaneously the top of the tower (the 𝕊 layer from above, the
infinite-dimensional limit) and the bottom (ℝ from below, undifferentiated):
maximum symmetry before the first distinction. `THEORETICAL`. Moving σ above
zero is where primes acquire different weights. "0 is the quasi-prime":
unusable as a divisor, yet containing the potential of every number.

## 6. The octonion pivot and the Fano plane

The step 𝕆 → 𝕊 is the Octonion Pivot: the forward current first reaches the
loss of associativity-with-division and the backward current first regains it.
The Fano plane (7 points, 7 lines) is the multiplication table of the
octonion imaginary units; the Fano index used in HyperWebster
([09](09_hyperwebster_engine.md)) maps each character to one of the seven
generators. As [09](09_hyperwebster_engine.md) §4 records, that map is
many-to-one: it is a path address, not an invertible encoding.

## 7. Related pages

[03 Inversion](03_inversion_engine.md) · [05 Noether](05_noether_engine.md) ·
[06 Noether information](06_noether_information_engine.md) · [25 Sedenion manual](25_sedenion_manual.md) ·
[84 Box-kite debugger](84_the_box_kite_debugger.md) · [101 The Cayley–Dickson literature](101_the_cayley_dickson_literature.md)
