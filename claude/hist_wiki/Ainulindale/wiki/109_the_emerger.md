# 109 — The Emerger

| | |
|---|---|
| Scope | the ascent dual of generational lineage: given a 16-vector, which domains does a chosen grouping of the imaginary units expose, and in what order do the variables emerge; the five brackets and the dependency order between them; firing plans |
| Written | 2026-09-01; update 2026-10-21 (firing plans) |
| Engine | `ValaQuenta/modules/emerger/` (`EmergerModule`, v0.1); first-pass prototype `TuringStack/the_emerger.py`; firing plans: `SedenionSpectralRelativity/firing_plan.py` (15 exact checks), `wiki/Bracketing-and-Firing-Plans.md`, standalone port `GenerationalLineage/engine/bracketing_firing_order.py` tool 4 (`wiki/Firing-Plans.md`); `GenerationalLineage/engine/emerger.py` |
| Continues | the sedenion-bracketing thread of [94](94_mathematical_xray_crystallography.md), [95](95_the_scale.md), [107](107_add_scale_sign_datatype.md) and the box-kite work |
| The author | "the emerger is going to be a useful methodology for factoral decomposition and spectroscopy in general. it's directly the Sedenion Bracketing engine … the grouping of what sedenion operators creates what different domains … which by need give the emergence a priority in a particular order." And the mechanism: "a dynamic permutative bracketer that works only in complex domains since the reals are the tilt to the 'i' axis … but we keep the anchor of the Real Numbers in place to view the relationships between the bracketing and the real component … it can also permute between quaternion, octonion … complex …" |
| Confidence | the counts (4 legal orders of 120; separable permutations): ESTABLISHED (re-run, Listing 1) · the reading of each bracket: `INTERPRETATION` · the σ_RB entry-point clock: a design with a recorded illegality (§4) |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The module and the 15 firing-plan checks were not re-run |

## 1. What changed

Generational Lineage answers **descent**: what built this operator, which generators, how deep. The Emerger is its **ascent** dual: given a 16-vector, which *domains* does a chosen grouping of the imaginary units expose, and (because each domain needs the ones under it) in what **order** do the variables emerge.

The real component e₀ is not one of the things grouped. It is the **anchor**, "the tilt to the i axis", held fixed so every imaginary group is read against it. What is permuted is the partition of the 15 imaginary indices; the partition yields a list of sub-domains, each span({e₀} ∪ group), classified by closure as ℂ, ℍ, 𝕆 or a **fragment**: a linear subspace that is not a subalgebra, which is exactly where the zero divisors live.

## 2. The five brackets

- **{1:15}**: the scalar against the fifteen relational edges; the grading that makes conjugation, norm and inverse well defined. Everything else needs it first.
- **{2:14}**: the (e₀, e₈) doubling plane against the rest. 16 − dim G₂ = 2: G₂ (the continuous shape of the zero-divisor locus, per Moreno) is "free"; the leftover complex number z = x₀ + i·x₈ is the **pointer**, where you are in the Cayley–Dickson ladder, and "the line on which W(1)·e^{W(1)} = 1 sits, so it carries Ω_ZS" (the page's reading).
- **{8:8}**: 𝕆 ⊕ 𝕆·e₈: J_red and J_blue, the two trees, forward and backward. The signed distance |a| − |b| is the distance from the zero-divisor equator; L_x − R_x is the J₂ asymmetry.
- **{4:4:4:4}**: four quaternion blocks, four SU(2) phases (the d\* faces), and σ_RB's tilt and axis. Σ tilt is the deviation from σ = ½, read here as the **net work** to go once round the 0 → p → q → N loop and back, the frequency difference between the "to" and "from" arcs ([94](94_mathematical_xray_crystallography.md)).
- **{4:8:4}**: the gain spectrum: annihilator (gain 0), unit (gain 1, NOW), amplifier (gain √2): the multiplicative role of the element ([89](89_the_seven_octonions.md) §2 for the measured spectrum).

## 3. The firing order  `ESTABLISHED` (the counts)

The order is load-bearing: {1:15} must precede {2:14}, {8:8} and {4:8:4}; {8:8} precedes {4:4:4:4}, which precedes {4:8:4}. **Listing 1** counts the orders of the five brackets that respect this: **4 of 120**, namely

```
{1:15} {2:14} {8:8} {4:4:4:4} {4:8:4}        {1:15} {8:8} {2:14} {4:4:4:4} {4:8:4}
{1:15} {8:8} {4:4:4:4} {2:14} {4:8:4}        {1:15} {8:8} {4:4:4:4} {4:8:4} {2:14}
```

so {2:14} is free to fire anywhere after {1:15}, and the canonical order is one of the four. σ_RB picks the entry point: Σ tilt is squashed rationally into a phase, ⌊12·phase⌋ mod 5 names the bracket that fires first. The 12 comes from the four d\* faces against the three Lambert-W rotor faces, lcm(4, 3) = 12 (Listing 1; the same "no camshaft" clock as the firing defect of [107](107_add_scale_sign_datatype.md) §5, at sedenion scale).

## 4. Honest boundaries (kept)

- The engine **found** that a σ_RB phase can select a firing order that is *not* dependency-legal (e₁ + e₁₀ phases into {2:14} before {1:15}). The clock names the entry; the engine reports the illegality instead of snapping to the nearest legal order. A real open item, not a bug hidden. (Consistent with §3: only 4 of the 120 orders are legal, so a clock mod 5 that is uniform over entry points selects an illegal first bracket 4 times in 5, since the only legal first bracket is {1:15}.)
- The {4:8:4} gain-index assignment is a reading of the canonical-maths {4:8:4} note, not derived in this module.
- `on_zd_equator` is the sufficient basis-pair condition; the exact zero-divisor locus is `box_kite`'s 42 assessors / PSL(2, 7) ([84](84_the_box_kite_debugger.md)); G₂ is the blow-up that forgets the labelling.
- The RSA/semiprime embedding used for demonstration is illustrative only (`TuringStack/the_emerger.py`).

## 5. Update 2026-10-21: firing plans

Brackets now carry firing orders: `(R I | 2 1)` fires the second child (the imaginary octonion of the two-octonion sedenion) first and the real octonion second, and a bracket runs as one operation inside its parent in its own order (`((A B | 2 1) C | 2 1)` fires C B A). The operator reading (matrix composition) is associative, so only the order changes the result; the element reading (the sedenion product) is not, so the bracketing changes it too. The earlier record: written-order binary plans reach 6, 22, 90 of 3!, 4!, 5! orders. This module (`ValaQuenta/modules/bracketing_firing_order`) does not yet carry plans.

**Listing 1 — the legal orders, and the orders reachable by binary bracketings** (written for this page; python3 standard library; runs cold)

```python
import itertools, math
from functools import lru_cache
B = ['{1:15}', '{2:14}', '{8:8}', '{4:4:4:4}', '{4:8:4}']
before = [(0, 1), (0, 2), (0, 4), (2, 3), (3, 4)]          # {1:15} < {2:14}, {8:8}, {4:8:4} ; {8:8} < {4:4:4:4} < {4:8:4}
legal = [p for p in itertools.permutations(range(5)) if all(p.index(a) < p.index(b) for a, b in before)]
print('legal orders of the 5 brackets:', len(legal), 'of', math.factorial(5))
for p in legal: print('  ', ' '.join(B[i] for i in p))
@lru_cache(None)
def orders(i, j):                                           # firing orders of leaves i..j-1, written in order, each node choosing which child fires first
    if j - i == 1: return frozenset([(i,)])
    out = set()
    for k in range(i + 1, j):
        for L in orders(i, k):
            for R in orders(k, j): out.add(L + R); out.add(R + L)
    return frozenset(out)
def avoids(p, pat):
    for idx in itertools.combinations(range(len(p)), len(pat)):
        vals = [p[i] for i in idx]; srt = sorted(vals)
        if tuple(srt.index(v) for v in vals) == pat: return False
    return True
for n in (3, 4, 5, 6):
    reach = orders(0, n); sep = {p for p in itertools.permutations(range(n)) if avoids(p, (1, 3, 0, 2)) and avoids(p, (2, 0, 3, 1))}
    print('n=%d leaves: reachable firing orders %d of %d! = %d ; separable permutations (avoid 2413, 3142) %d ; equal: %s' % (n, len(reach), n, math.factorial(n), len(sep), set(reach) == sep))
print('unreachable at n=4:', sorted(set(itertools.permutations(range(4))) - set(orders(0, 4))))
print('16 - dim G2 =', 16 - 14, '; lcm(4,3) =', math.lcm(4, 3), '; gcd(4,3) =', math.gcd(4, 3))
```

```
legal orders of the 5 brackets: 4 of 120
   {1:15} {2:14} {8:8} {4:4:4:4} {4:8:4}
   {1:15} {8:8} {2:14} {4:4:4:4} {4:8:4}
   {1:15} {8:8} {4:4:4:4} {2:14} {4:8:4}
   {1:15} {8:8} {4:4:4:4} {4:8:4} {2:14}
n=3 leaves: reachable firing orders 6 of 3! = 6 ; separable permutations (avoid 2413, 3142) 6 ; equal: True
n=4 leaves: reachable firing orders 22 of 4! = 24 ; separable permutations (avoid 2413, 3142) 22 ; equal: True
n=5 leaves: reachable firing orders 90 of 5! = 120 ; separable permutations (avoid 2413, 3142) 90 ; equal: True
n=6 leaves: reachable firing orders 394 of 6! = 720 ; separable permutations (avoid 2413, 3142) 394 ; equal: True
unreachable at n=4: [(1, 3, 0, 2), (2, 0, 3, 1)]
16 - dim G2 = 2 ; lcm(4,3) = 12 ; gcd(4,3) = 1
```

The recorded 6, 22, 90 reproduce, and the pattern has a name: the firing orders reachable by binary bracketings of n leaves written in order are exactly the **separable permutations**, those avoiding the patterns 2413 and 3142 (equal sets for n = 3 to 6: 6, 22, 90, 394, the large Schröder numbers). At four leaves the two unreachable orders are 2413 and 3142 (in the listing's 0-based labels (1, 3, 0, 2) and (2, 0, 3, 1)): "interleaved" firings that no nested bracketing can produce. This is a measured fact of the plans (the separable-permutation fact is standard combinatorics; its application to these plans is noted here); it
bounds what a bracket-plus-firing-order can express.

## 6. Predecessor links

[94](94_mathematical_xray_crystallography.md) · [95](95_the_scale.md) · [100](100_division_algebras_and_physics.md) · [101](101_the_cayley_dickson_literature.md) · [107](107_add_scale_sign_datatype.md) · [89](89_the_seven_octonions.md), [84](84_the_box_kite_debugger.md) (box-kite / zero-lattice engines in ValaQuenta)
