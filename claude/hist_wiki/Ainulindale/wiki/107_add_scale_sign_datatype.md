# 107 — The ADD:SCALE:SIGN Datatype: Formal Specification

| | |
|---|---|
| Scope | the tier-0 floor Aff(1, ℝ) = ADD ⋊ (SCALE × SIGN) as a value type; its generators, word, fold, operations, firing order, `ASSWord`, Smith charts; the fast-inverse-square-root example; the reconstruction claim and its scope; three conjectures (J_green, the Two-Trees containment, string theory as the M ⟂ J residual); SIGN and the Noether-current direction |
| Engines | `ValaQuenta/modules/add_scale_sign/` (value type + `EquationModule`; `ValaQuenta/wiki/add_scale_sign.md`); `GenerationalLineage/engine/add_scale_sign.py` (engine and decomposer tool, formerly under SedenionFactoralRelativity); decomposition maths (four-question test, roll-down) in `VAPMIP/add_scale_sign.py`; reference `.clauderc_canonical_maths` "ADD:SCALE:SIGN — the tier-0 datatype" |
| Related | [95](95_the_scale.md), [92](92_ring_theory_spine.md), [61](61_up_down_not_forward_backward.md), `generational-lineage` skill §§0–3 |
| Confidence | the group, the laws and the identities: ESTABLISHED (re-run, Listing 1) · the "word" u of a composite and the fold of a composite: a definition with a stated defect (§3) · the reconstruction claim: scoped (§9) · §10–§12: `THEORETICAL`, flagged |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The module's own self-tests were not re-run |

## 1. Object

An `ASS` value is an element of the tier-0 floor Aff(1, ℝ) = ℝ ⋊ (ℝ_{>0} × ℤ/2) = ADD ⋊ (SCALE × SIGN), represented by a triple (add a, scale s > 0, sign g ∈ {−1, +1}) acting as T_{(a,s,g)}: x ↦ g·s·x + a. `ASS` is immutable and records the atomic generators that built it (`.steps`, in application order): forward, backward and record-keeping in one type.

## 2. Generators and their equation parts

| generator | map | equation part Δ | cost |
|---|---|---|---|
| `ADD(a)` | x ↦ x + a | a | free (translation; the flow / count) |
| `SCALE(s)` | x ↦ s·x | ln s | **the work** (log-gain; the fold) |
| `SIGN(g)` | x ↦ g·x | g ∈ {−1, +1} | free (one bit; det ±1) |

Identity: (0, 1, +1), the Mingling (off both Two Trees).

## 3. The word and the fold  `ESTABLISHED` with a stated defect

Every element has a word u(a, s, g) = g ln s + a and a position on the Smith/Joukowsky fold Γ = tanh(u/2); for a composite of generators T = ⨟ₖ Tₖ the page defines u(T) = Σₖ [gₖ ln sₖ + aₖ] and Γ(T) = tanh(u(T)/2). The fold is the generating function of Aff(1, ℝ) acting on ln x. Ground state: a → 0, s → 1, g → +1 ⇒ u = 0 ⇒ Γ = 0 ⇒ x = the anchor (the identity / the now / the viewport); the predicate `T.is_ground()`.

**What Listing 1 fixes.** The composition law (a₂, s₂, g₂) ∘ (a₁, s₁, g₁) = (a₂ + s₂ g₂ a₁, s₂ s₁, g₂ g₁) and the inverse (−g a/s, 1/s, g) hold to 3×10⁻¹⁴ over 2000 random elements. The word u of a **composed triple** is not the sum of the words of its factors in general: for A = (0.7, 2, +1) and B = (1.1, 3, +1), u(A∘B) = 4.6918 while u(A) + u(B) = 3.5918, because A scales B's translation. So "u(T) = Σₖ[…]" is the definition of the word *of a list of generators* (the sum over the recorded steps), which is what the engine's `ASSWord` computes, and it is **not** the word of the composed map. The two differ exactly by the non-trivial bracket of the group, which is the only one: [SCALE, ADD] = ADD (Listing 1: SCALE(3)∘ADD(2) = (6, 3, +1) but ADD(2)∘SCALE(3) = (2, 3, +1); they differ by an ADD of (s − 1)a = 4).

## 4. Operations (the manipulation surface, the `str` analogy)

| category | method | semantics |
|---|---|---|
| apply | `T(x)` | g·s·x + a |
| **forward** | `A @ B` / `A.then(B)` | composition; (A @ B)(x) = A(B(x)), B fires first |
| **backward** | `~T` | inverse (−g a/s, 1/s, g); reverses and inverts the record |
| **residual** (`str.strip`) | `T.residual('SIGN')` | reset one generator to its identity, keep the rest |
| complement | `T.only('SCALE')` | keep one generator, drop the other two |
| split | `T.parts()` | (SIGN(g), SCALE(s), ADD(a)), camshaft order |
| **decompose** | `T.lineage(order)` | → `ASSWord` (§6) |
| chart | `T.to_smith()` | §7 |
| record | `T.steps`, `T.record()` | the immutable (a, s, g) log: Paper's Hands / the Long Path |

## 5. Firing order: the three-phase camshaft

`CAMSHAFT = (SIGN, SCALE, ADD)`, SIGN innermost: x ↦ ADD(SCALE(SIGN(x))), T = ADD(a) @ SCALE(s) @ SIGN(g). **Firing defect:** u(T) − (a + ln s) = (g − 1) ln s (verified exact, Listing 1: −2.772589 for g = −1, s = 4); zero iff g = +1 or s = 1, otherwise −2 ln s. Non-zero ⇔ the SIGN flipped a non-trivial SCALE ⇔ "the same quantity was defined twice", the page's reading of it as structurally the Bell composed-rotation defect (an analogy: the algebraic fact is the formula above). Concurrency model: three threads, one per phase, rotating independently; "the interference pattern of the three phases is the pathway".

## 6. `ASSWord`: the datatype's own decomposition type

`T.lineage(order)` returns an ordered word of the recorded generators: `order='chrono'` is application order (when each fired; the record); `order='zeta'` is by spectral weight |uₖ| descending (how much each moves the fold). The departure between the two orderings is this datatype's ψ(x) − x ([103](103_riemann_and_the_prime_number_theorem.md)): the generational-lineage-as-chronology against lineage-as-ζ-order. `ASSWord.firing_defect()`, `.additive()`, `.as_equation()`, iteration.

## 7. The orthogonal Smith charts

`T.to_smith()` reads the element in the language it was built on: Γ_SCALE = tanh(½ ln s) (multiplicative, the E–W ring), Γ_ADD = tanh(½ a) (additive, the N–S ring), parity = g (the quadrant sheet). Ground state → (0, 0, +1), the centre. The two rings are conformally orthogonal ([95](95_the_scale.md) §7), and SIGN selects the sheet.

## 8. Worked example: the fast inverse square root  `ESTABLISHED`

1/√x = exp(−½ ln x) is the `ASS` word SIGN(−1) ∘ SCALE(½) applied to ln x. The Quake III routine (`0x5f3759df`) computes this in the IEEE-754 exponent field, the hardware's native log₂: `i >> 1` is SCALE by ½ done as a shift (the multiply is skipped); `MAGIC − …` is the ADD (the bias/offset); the sign bit is untouched. The mantissa makes the map piecewise-linear, "good enough"; one Newton step is the residual. Listing 1: maximum relative error **3.44 %** raw and **0.175 %** after one Newton step over 200,000 values spanning 10⁻⁶–10⁶, matching the page's ≈ 3.4 % and ≈ 0.17 %. (`GenerationalLineage/engine/add_scale_sign.py` `fisr_word(x)`.)

**Listing 1 — the group laws, the firing defect, the SIGN/Noether identity and the fast inverse square root** (written for this page; python3 standard library; runs cold)

```python
import math, random, struct
random.seed(3)
class T:
    def __init__(s, a=0.0, sc=1.0, g=1): s.a, s.s, s.g = a, sc, g
    def __call__(s, x): return s.g * s.s * x + s.a
    def then(A, B): return T(A.a + A.s * A.g * B.a, A.s * B.s, A.g * B.g)       # A @ B : B fires first
    def inv(s): return T(-s.g * s.a / s.s, 1 / s.s, s.g)
    def word(s): return s.g * math.log(s.s) + s.a
rnd = lambda: T(random.uniform(-3, 3), math.exp(random.uniform(-2, 2)), random.choice((-1, 1)))
err = 0
for _ in range(2000):
    A, B, x = rnd(), rnd(), random.uniform(-5, 5); err = max(err, abs(A.then(B)(x) - A(B(x))), abs(A.inv()(A(x)) - x), abs(A.then(A.inv())(x) - x))
print('composition law, inverse and round trip over 2000 random elements: max error %.1e' % err)
a, s, g = 1.3, 4.0, -1
Tt = T(a, 1, 1).then(T(0, s, 1)).then(T(0, 1, g))
print('ADD@SCALE@SIGN triple =', (round(Tt.a, 6), round(Tt.s, 6), Tt.g), '; u = %.6f ; a + ln s = %.6f ; (g-1) ln s = %.6f ; u - (a + ln s) = %.6f' % (Tt.word(), a + math.log(s), (g - 1) * math.log(s), Tt.word() - (a + math.log(s))))
A, B = T(0.7, 2.0, 1), T(1.1, 3.0, 1)
print('u(A@B) = %.6f vs u(A) + u(B) = %.6f' % (A.then(B).word(), A.word() + B.word()))
x1 = T(0, 3, 1).then(T(2, 1, 1)); x2 = T(2, 1, 1).then(T(0, 3, 1))
print('SCALE(3)@ADD(2) = %s ; ADD(2)@SCALE(3) = %s ; difference in a: %s' % ((x1.a, x1.s, x1.g), (x2.a, x2.s, x2.g), x1.a - x2.a))
E = 1.7
print('ln F - ln B = E(1 - 2 sigma) vs ASS(0, 2E, -1)(sigma - 1/2): max difference', max(abs(math.log(math.exp(-sg * E)) - math.log(math.exp(-(1 - sg) * E)) - T(0, 2 * E, -1)(sg - .5)) for sg in (0.1, 0.3, 0.5, 0.8)))
def fisr(x, newton=False):
    i = struct.unpack('>I', struct.pack('>f', x))[0]; i = 0x5f3759df - (i >> 1); y = struct.unpack('>f', struct.pack('>I', i))[0]
    return y * (1.5 - 0.5 * x * y * y) if newton else y
xs = [10 ** random.uniform(-6, 6) for _ in range(200000)]
print('Quake III 0x5f3759df: max relative error raw %.2f%% ; after one Newton step %.3f%%' % (100 * max(abs(fisr(x) * math.sqrt(x) - 1) for x in xs), 100 * max(abs(fisr(x, True) * math.sqrt(x) - 1) for x in xs)))
```

```
composition law, inverse and round trip over 2000 random elements: max error 2.8e-14
ADD@SCALE@SIGN triple = (1.3, 4.0, -1) ; u = -0.086294 ; a + ln s = 2.686294 ; (g-1) ln s = -2.772589 ; u - (a + ln s) = -2.772589
u(A@B) = 4.691759 vs u(A) + u(B) = 3.591759
SCALE(3)@ADD(2) = (6, 3, 1) ; ADD(2)@SCALE(3) = (2, 3, 1) ; difference in a: 4
ln F - ln B = E(1 - 2 sigma) vs ASS(0, 2E, -1)(sigma - 1/2): max difference 2.220446049250313e-16
Quake III 0x5f3759df: max relative error raw 3.44% ; after one Newton step 0.175%
```

## 9. Reconstruction claim, stated with its scope

The three generators span Aff(1, ℝ), the one-dimensional similarity group. Every operation the generational-lineage roll-down reaches (`root_irreducible`, `ROOT_OF`, `AFF1`; tiers 0–3) terminates on a word in {ADD, SCALE, SIGN}, and within that domain the (ADD, SCALE, SIGN) axes are a 3-D field with every operation a point/word in it. This is the concrete content of "this reduces everything"; it is **not** a claim about mathematics outside the decomposition domain.

## 10. J_green  `CONJECTURE` (author, 2026-08-28)

J_red and J_blue are the two octonion halves ([14](14_redblue_hamiltonian.md) §3); their coupling is the sedenion = 0_RB. Read in the (ADD, SCALE, SIGN) basis that coupling is a single 3-vector field, **J_green** (green = red + blue, additively). Proposed: J_red ⊕ J_blue = (ADD: x, SCALE: y, SIGN: z) = J_green = 0_RB. The ⊕ is the coupling (a per-channel product, s_rb[k] = J_red[k]·J_blue[k], not a scalar sum), consistent with `decompose_h_rb_hat` finding that Σ_RB decomposes as 2·ADD / 3·SCALE / 4·SIGN. (Relation to the J_red/J_blue record and its sign conventions: [14](14_redblue_hamiltonian.md) §2, [133](133_canonical_maths.md) §3.)

## 11. The Two Trees containment  `INTERPRETATION` (author, 2026-08-28)

LAURELIN (composite, "what is") is all around TELPERION (irreducible, "what cannot be"): the derived operations are dense, the three irreducibles sparse; yet TELPERION hugs LAURELIN, because every composite is built from the irreducibles, so the three are inside each. `T.parts()` extracts the three generators every element hugs. Mutual embedding, "the same self-similar containment the Mandelbrot interior/exterior relation shows" (a picture).

## 12. String theory as the M ⟂ J residual  `CONJECTURE`, no engine

The Mandelbrot set (parameter space, z₀ = 0, c varies) and the Julia sets (dynamical space, c fixed, z₀ varies) are the two orthogonal viewpoints of z ↦ z² + c. The author's conjecture: string theory is the residual of that orthogonal pair, the same "residual" as the error check ([98](98_provenance_and_citations.md) §B; `~/.clauderc_user_provenance` §1.20) and the BAO spectral residue ([75b](75b_bao_mass_gap_engine.md)). THEORETICAL; no engine; recorded as the natural next probe.

## 13. SIGN and the Noether-current direction (2026-09-28)  `ESTABLISHED` (the identity)

The spec's SIGN (g = ±1, the direction bit) is necessary but not sufficient for the direction of the Noether currents. Exact identity (Listing 1, difference 2×10⁻¹⁶): ln F − ln B = E(1 − 2σ) = ASS(0, 2E, −1)(σ − ½): SCALE 2E is the strength, the ADD offset σ − ½ picks the side, SIGN is the orientation. On this floor SIGN∘SCALE = SCALE∘SIGN, while SIGN and ADD differ by a translation (the reflection of the offset); flipping SIGN moves the fold by (g − 1) ln s, zero at s = 1 (§5). The up/down orientation of the currents ([61](61_up_down_not_forward_backward.md)) is a Cayley–Dickson-tower fact that the tier-0 bit only traces. Caveats (kept): backward = −forward is a definition; F + B is not conserved in σ (only the product FB = e^{−E} is, [61](61_up_down_not_forward_backward.md) Listing 1). Tables and script: `ValaQuenta/wiki/add_scale_sign.md`, `ContextPlease/claude/scratchpad/2026-09-28_sign_noether_direction/`.

## 14. Related pages

[95 the Scale](95_the_scale.md) · [92 the ring-theory spine](92_ring_theory_spine.md) · [61 up/down](61_up_down_not_forward_backward.md) · [109 the Emerger](109_the_emerger.md)


## Interactive pages (2026-11-27)

`ValaQuenta/gallery/add_scale_sign/`: five pages (two maps and their composites, the bracket `[SCALE, ADD] = ADD` walked on a number line, the fold and the two Smith charts, the Long Path with the flip test, an exact 18-element grid), each checked against the Python engine on load. Writing them found that the quadrant letters of `to_smith()` were swapped against the rings described above (ledger X-71, fixed at 0.3).
