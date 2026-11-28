# 31 — Cavitation, causality and Fermat: the sedenion hole punch

| | |
|---|---|
| Status | **First capture (2026-06-03, an eight-hour session), now with each checkable number verified.** The thesis is `THEORETICAL`; "E = mc² is Fermat's theorem" is `CONJECTURE`, which is the tier the code itself assigns (§6) |
| Code | `ValaQuenta/modules/tier7_cosmos/maths.py`: `sedenion_hole_punch()` (line 3024; returned inside `full_cosmos`), `black_hole_crossing()` (line 788); `VAPMIP/engines/e05_nball_transformer.py` (the pulley ratios) |
| Registry note | `sedenion_hole_punch` is **not** registered as its own equation (`tier7_cosmos` registers 15; `registry.run('tier7_cosmos.sedenion_hole_punch', …)` raises `KeyError`). Author, 2026-11-13: it is part of the eventual **Sedenion Hyperindexing Frame of Reference**, so it is deliberately left unregistered until that engine is built; the earlier page's "Engine 20: TODO" meant that |
| Last verified | 2026-11-13: Listing 1 executed; `sedenion_hole_punch()` run and its keys read |

## 1. The thesis

> Black holes are the scar of an event: the instant cavitation, experienced
> slowly over billions of years.

Stated as a model (`THEORETICAL`): spacetime is a *non-shear* medium; a
sufficient concentration of energy makes the medium cavitate; the void
nucleates and collapses in about one Planck time (5.391·10⁻⁴⁴ s); the event
horizon is the boundary of the *scar* that persists, and Hawking radiation is
the medium re-equilibrating around it. Everything below is a reading of that
model. The code's own timing figures: punch duration 5.391·10⁻⁴⁴ s, scar
duration 2.1·10⁶⁷ yr, ratio 1.2·10¹¹⁸ (the code and the earlier page say
"Planck second"; the quantity is the Planck *time*).

## 2. Space as a medium  `interpretation`

c = 1/√(ε₀μ₀) is exact (`ESTABLISHED`). The page's reading: ε₀ and μ₀ are
properties of the spacetime medium, "free space is not free", so the speed of
light is a propagation speed through the gravitational medium; "gravity is not a
force in the medium; gravity is the medium", at the level of the tower σ = 2
(𝕆, n = 8) with the electromagnetic field at σ = ½ (ℂ, n = 2); and the
Standard Model Lagrangian correctly excludes gravity because gravity is the
medium. Shapiro delay and lensing are offered as evidence. They are
predictions of general relativity in which the *coordinate* speed of light
changes near mass; they are consistent with a medium picture (the "analogue
gravity" programme) and do not distinguish it from the geometric one, so
they are not proof of it. Gravity as a push (Archimedes in the medium: matter
displaces the unindexed permutation universe and the restoring pressure is
gravity) is the same reading.

## 3. Cavitation and the hole punch  `THEORETICAL`

A non-shear fluid (inviscid, the Euler equations, the 𝕆 level being an
alternative algebra with no off-diagonal stress) cavitates sharply: with no
viscosity nothing smooths the void's boundary, so the event horizon is a
sharp surface. (In general relativity the horizon's sharpness is a statement
about causal structure and does not need a viscosity argument; the page's
reading is a model, not a derivation.) The void's interior is the 𝕊 level.

The hole-punch table: die = concentrated energy ("block and tackle"); paper =
the non-shear 𝕆 medium; the punch-through = the 𝕆 → 𝕊 transition; the hole =
the black hole; the chad = white-hole emission; punch duration = one Planck
time; hole persistence = Hawking evaporation time.

**The punch edge.** The edge is said to have the topology of the **168**
composite zero-divisor pairs of 𝕊. This number is exact and checked
(Listing 1): the 84 zero-divisors e_i ± e_j of [25](25_sedenion_manual.md) §4
have 4 partners each, giving 336 ordered and **168 unordered pairs**. That the
horizon has this structure is the framework's reading.

## 4. The block and tackle  (verified numbers)

Each Cayley–Dickson doubling is read as a pulley whose gear ratio is the
ratio of unit-ball volumes, V(2n)/V(n) with V(n) = π^{n/2}/Γ(n/2 + 1):

| Pulley | Ratio (computed) | Earlier page |
|---|---|---|
| ℝ → ℂ | π/2 = 1.5707963 | 1.571 |
| ℂ → ℍ | π/2 = 1.5707963 | 1.571 |
| ℍ → 𝕆 | 0.8224670 | 0.822 |
| 𝕆 → 𝕊 | 0.0579816 | 0.058 |
| 𝕊 → 𝕋 (V(32)/V(16)) | 1.8285·10⁻⁵ | 0.00002 |

The two π/2 ratios are exact; the later ones fall below 1 once the peak of
V(n) is passed, at n* = 5.256946 (V(n*) = 5.277768). The product of the
ratios as a "mechanical advantage" is arithmetic; calling the sequence
a block and tackle (force traded for distance, no change of total energy) is
the analogy. "A quantum fluctuation at ℝ run through the full chain becomes a
black hole" is not computed.

*Corrections found while checking.*
- V(n) = n has its root at **n = 5.2777**, not 5.24 as the page said (it lies next to the peak, where V ≈ 5.2778).
- The descent to n = 16 is said to reach d*. V(16) = **0.235331**, which is 0.0107 below d*_spec = 0.24600 and 0.0110 below d* = 0.24631 (engine e05 reports the same; [26](26_TODO_and_roadmap.md) §3). The identification V(16) ≈ d* is not exact and is recorded as a failed match.

## 5. Mass is local, causality is non-local  (the prime-weight facts)

Weights G_p(σ) = p^(−σ). At σ = 2 (gravity, mass) the prime sum converges:
Σ_p p⁻² = 0.4522474 (the prime zeta value P(2)). At σ = ½ (causality) it
diverges: Σ_{p≤x} p^(−1/2) is 12.65, 29.14, 70.05, 176.35 for
x = 10³, 10⁴, 10⁵, 10⁶ (growth ≈ 2√x/ln x). These two facts are exact
(Listing 1). The framework's reading: mass is assembled from the small primes
(local), causality from all primes including the largest (non-local); the
difference of the two sums *is* the light cone; entanglement lives in the σ = ½
face and so is non-local without transmitting information. That reading is
`THEORETICAL`; the convergence/divergence contrast is mathematics.

The table the code prints (`mass_vs_causality`) gives, for p = 2, w_mass = 0.25,
w_causality = 0.707107 and a ratio of 2.83, and the ratio grows with p
(p^{3/2}).

## 6. "E = mc² is Fermat's theorem"  `CONJECTURE`

The page's argument: FLT says aⁿ + bⁿ ≠ cⁿ for n ≥ 3; the σ-faces correspond
to Fermat powers n = σ; σ = 2 is the only allowed structure; so mass is
assembled at σ = 2; E = mc² has exponent 2 and "the universe cannot write E = mc³
because Wiles proved it cannot exist".

Assessment. The code labels this *CONJECTURE (structurally compelling)* and its
own result dictionary says "E = mc³ cannot exist — Wiles proved it (FLT)".
That last sentence does not follow: FLT is a statement about integer solutions
of aⁿ + bⁿ = cⁿ and says nothing about the exponent of c in a physical law.
The exponent in E = mc² is fixed by dimensional analysis and Lorentz
invariance (E² = (pc)² + (mc²)²; the rest energy of a body of mass m has the
dimension kg·m²/s², which no cube of a speed supplies). The parallel "σ = 2
with Fermat n = 2" is a structural coincidence of the exponent 2 with the
quadratic case; it is a suggestive pattern and not an argument. Status:
`CONJECTURE`, with the unsupported sentence withdrawn.

The "Fermat-forbidden zone" reading: at σ → ∞ every prime weight p^(−σ) → 0, so
nothing assembles; that is read as the interior, with the horizon as the boundary
of the Fermat-allowed zone and the singularity where Fermat's theorem "has the
last word". Interpretation.

## 7. The network hole punch  `analogy`

The correspondence: NAT firewall ↔ event horizon; NAT table entry ↔ horizon
geometry; hole punch ↔ the cavitation event; persistent connection ↔ the
Einstein–Rosen bridge; the peer ↔ a white hole; keep-alive packets ↔ Hawking
radiation; timeout ↔ evaporation. ER = EPR (Maldacena–Susskind, 2013) is a
published conjecture relating wormholes and entanglement; the framework
names its mechanism "the sedenion hole punch". "Information doesn't fall
in, it is routed through; the paradox is a non-issue" is the model's
resolution of the information paradox. The paradox is an open problem in the
literature, and no calculation here resolves it.

## 8. White holes, the gravastar and the Big Bang  `CONJECTURE`

In the model the white hole is the immediate bounce of the punch (one Planck
time), not the end of evaporation; the gravastar (Mazur–Mottola: a de Sitter
interior and a shell) is read as the permanent scar of a completed event; the
Big Bang is the same structure at cosmological scale, the 13.8 Gyr of
expansion being the scar spreading. The code cites consistency with Rovelli's
bounce. None of this is derived here.

## 9. Open problems from the session (still open)

1. The Planck threshold: what energy or information density triggers the punch, in terms of V(n) and d*.
2. The punch geometry: the topology of the edge defined by the 168 pairs and which catastrophe (fold, cusp, swallowtail) it is.
3. The scar lifetime: Hawking time as a function of the pulley ratios and the Planck time.
4. The "STUN server": what coordinates the black-hole/white-hole punch (candidate: the σ = ½ face).
5. The Big Bang as a white hole: does the Hubble constant encode the scar's expansion rate?
6. The prime threshold: at what digit count does the σ = 2 contribution fall below the σ = ½ one. (From §5, the ratio p^{3/2} already exceeds 1 for every prime p ≥ 2, so the crossing is at the smallest primes and the question needs restating.)

## 10. Verification

**Listing 1 — the numbers of this page** (written for this page; runs cold with SciPy)

```python
import math
from scipy.optimize import brentq, minimize_scalar

V = lambda n: math.pi ** (n / 2) / math.gamma(n / 2 + 1)
print('ratios', [round(V(b) / V(a), 7) for a, b in ((1, 2), (2, 4), (4, 8), (8, 16), (16, 32))])
print('peak n* =', round(minimize_scalar(lambda n: -V(n), bounds=(3, 8), method='bounded').x, 6))
print('V(n)=n at', round(brentq(lambda n: V(n) - n, 3, 6), 4), '  V(16) =', round(V(16), 6))

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
forms = [(i, j, s) for i in range(1, 8) for j in range(8, 16) for s in (1, -1)]
vec = {f: add(e(f[0]), e(f[1]), f[2]) for f in forms}
zero = lambda f, g: nrm(mul(vec[f], vec[g])) < 1e-12
zd = [f for f in forms if any(zero(f, g) for g in forms)]
pairs = {frozenset((f, g)) for f in zd for g in zd if zero(f, g)}
print('zero divisors', len(zd), ' unordered pairs', len(pairs))

N = 2_000_000
sv = bytearray([1]) * (N + 1); sv[0] = sv[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sv[i]:
        sv[i*i::i] = bytearray(len(sv[i*i::i]))
ps = [p for p in range(2, N + 1) if sv[p]]
print('sum p^-2 =', round(sum(p ** -2 for p in ps), 7))
print([round(sum(p ** -0.5 for p in ps if p <= x), 2) for x in (10**3, 10**4, 10**5, 10**6)])
```

```
ratios [1.5707963, 1.5707963, 0.822467, 0.0579816, 1.83e-05]
peak n* = 5.256946
V(n)=n at 5.2777   V(16) = 0.235331
zero divisors 84  unordered pairs 168
sum p^-2 = 0.4522474
[12.65, 29.14, 70.05, 176.35]
```

## 11. Related pages

[18 Fermat lattice](18_fermat_lattice.md) · [25 Sedenion manual](25_sedenion_manual.md) ·
[29 The witches hat](29_witches_hat_paper.md) · [30 Lambda paper](30_lambda_paper.md) ·
[32 Superconducting medium](32_superconducting_medium.md) · [108 De Sitter cavitation](108_desitter_cavitation.md)
