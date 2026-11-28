# 95 — The Scale: Decompositional Analysis, Forwards and Backwards

| | |
|---|---|
| Scope | SCALE (identity 1, gain 1, axis {×, /}) extracted from a quantity in both directions; what stays invariant at each of three levels; the master identity Γ = tanh(½ ln(Z/Z₀)); the ASS datatype; "locally square"; the J_red/J_blue "two rings" pairing that turned out to be one number; the speculative connections |
| Written | 2026-08-25; the author: "this is why it's the primary forensic tool of the generational lineage engine … This is The Scale … the scale invariant/scale blind version of the maths" and, correcting the scope, "the purpose of this engine is for decompositional analysis … so forwards and backwards" |
| Continues | the same-day VAPMIP thread (Vigenère quaternion, Enigma octonion, the two-ring/Smith-chart Möbius fold) and [92](92_ring_theory_spine.md) |
| Code | `ValaQuenta/modules/scale/` (`maths.py`, `tools.py`, `EquationModule` contract); `modules/add_scale_sign/` (`ASS`, `ASSWord`); notebook `17_scale.ipynb`; `ValaQuenta/wiki/scale.md`; `GenerationalLineage/engine/lineage.py` PW13–PW15 (the first proof; the ValaQuenta module is an independent port) |
| Confidence | the identities, the cross-ratio invariance, the derivative and the Möbius/matrix statements: ESTABLISHED (re-run) · the ASS datatype and the "defined twice" defect: a design, `THEORETICAL` · the "witches hat into a galaxy", gravastar and thermal-ceiling remarks: speculative, recorded as such |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The ASS module and the five custom-ring tests of `scale.md` §8 were not re-run |

## 1. Where SCALE already lived

The generational-lineage skill (§1) names three tier-0 irreducibles: ADD, SCALE, SIGN. SCALE was never a new concept; what was missing was an instrument that extracts it from a quantity and names what remains, in both directions.

## 2. One statement, three levels, three different answers

> An object's scale can always be extracted, but what remains invariant depends on the level at which the question is asked, and the levels do not share an answer.

**Level 1: one point, polar decompose/recompose (exact).** Z = r e^{iθ}; r = |Z| is the scale (real, non-negative, ordinal); θ = arg Z is scale-blind under real-positive rescaling, arg(λZ) = arg Z for λ > 0, exactly. The return path is exact: `polar_recompose(*polar_decompose(Z)) == Z` to < 10⁻⁹ over five test points (a near-zero and a near-million magnitude included).

**Level 2: the two-ring/Möbius fold, a different and harder question.** With the Smith-chart fold Γ = (Z − Z₀)/(Z + Z₀), is θ still the scale-blind invariant? **No**, and the rejected candidate is kept: the fold's fixed point is Z₀, not the origin, so rescaling about 0 is not a symmetry of the fold. Listing 1: for Z = λ(1 + i) with anchor Z₀ = 1, arg Γ = 2.0344, 1.1071, 0.2013, 0.0200 at λ = 0.5, 1, 5, 50 while arg(λZ) stays 0.7854. (The page quoted a range 1.054 → 0.007 for a test point it does not state; the pattern, a steep fall with λ, is the same.) The actual invariant at this level is the **cross-ratio** of four points, the classical Möbius invariant: folding the same four points through the fold at four different anchors (one nearly on the pole) leaves the cross-ratio unchanged (differences 0.0 in Listing 1). It is a property of a relationship among four points and not of any one.

**Level 3: a whole process, pathway decomposition.** `pathway_decompose()` runs a dependency graph of named operators, not a forced linear chain. Control case: real RSA CRT-decrypt (p = 61, q = 53): m₁ and m₂ are siblings (each depends only on the ciphertext), h depends on both, and the final message depends on h **and** m₂ again, a fan-out that a linear chain cannot represent. Forwards is running the graph; backwards is whatever the architecture provides, and the module does not manufacture a return path a process does not have.

## 3. Why a caustic was checked, and rejected  `ESTABLISHED`

A crowding of circles near the Smith chart's boundary invites the word "caustic". The exact derivative dΓ/dZ = 2Z₀/(Z + Z₀)² is never zero for finite Z (Listing 1: its minimum over |Z| = 10⁻³ … 10⁶ is 2×10⁻¹², tending to zero only as |Z| → ∞), and diverges only at the isolated pole Z = −Z₀. A caustic needs a vanishing Jacobian (an envelope); crowding toward infinity at one point is a different phenomenon, and the project does not conflate them.

## 4. What this is not claiming

- "Ring" as a family of circles on the Smith chart is not the "ring" of abstract algebra. Möbius transformations under composition form a group, the group of units of the matrix ring M₂(ℂ): composition equals matrix multiplication (Listing 1: difference 0.0), real but one level underneath, and only the multiplicative half is used when chaining folds.
- Not every process has a clean backward pass. RSA and the Vigenère cipher do; the module reports what the dependency graph contains.

## 5. The master identity  `ESTABLISHED`

The author: "The Scale (log and exponents) are unfolding and folding pretty directly right?" Checked, not agreed with on the spot: **Γ = tanh(½ ln(Z/Z₀))**, exactly, for complex Z and Z₀ (Listing 1: maximum difference 2×10⁻¹² over 20,000 random complex pairs with the principal logarithm, so the identity holds up to the branch of the log). Folding is log-then-bound; unfolding is unbound-then-exp, Z = Z₀ exp(2 artanh Γ).

**Listing 1 — the identities of this page and the next** (written for this page; needs numpy; runs cold)

```python
import cmath, math, random, numpy as np
random.seed(5)
rc = lambda: complex(random.uniform(-5, 5), random.uniform(-5, 5))
G = lambda Z, Z0: (Z - Z0) / (Z + Z0)
err = max(abs(G(Z, Z0) - cmath.tanh(0.5 * cmath.log(Z / Z0))) for Z, Z0 in ((rc(), rc()) for _ in range(20000)))
print('max |Gamma - tanh(ln(Z/Z0)/2)| over 20000 random complex pairs: %.2e' % err)
cr = lambda a, b, c, d: ((a - c) * (b - d)) / ((a - d) * (b - c))
pts = [rc() for _ in range(4)]; base = cr(*pts)
print('cross-ratio change under the fold for anchors 0.3, 1, 7+2i, -pts[0]*1.0001:', [round(abs(cr(*[G(p, z0) for p in pts]) - base), 12) for z0 in (0.3, 1, 7 + 2j, -pts[0] * 1.0001)])
d = lambda Z, Z0: abs(2 * Z0 / (Z + Z0) ** 2)
print('min |dGamma/dZ| over |Z| = 1e-3..1e6: %.2e ; near the pole Z -> -Z0: %.3g' % (min(d(m * cmath.exp(0.7j), 1) for m in (1e-3, 1e-1, 1, 1e2, 1e4, 1e6)), d(-1 + 1e-6, 1)))
print('arg Gamma for Z = lam(1+i), anchor 1, lam = 0.5, 1, 5, 50:', [round(cmath.phase(G(l * (1 + 1j), 1)), 4) for l in (0.5, 1, 5, 50)], '; arg(lam Z) =', round(cmath.phase(1 + 1j), 4))
Z, Z0, h = 0.8 + 0.4j, 1.0, 1e-6; gx = (G(Z + h, Z0) - G(Z - h, Z0)) / (2 * h); gy = (G(Z + 1j * h, Z0) - G(Z - 1j * h, Z0)) / (2 * h)
print('tangent vectors |d/dx| = %.6f |d/dy| = %.6f angle %.4f deg' % (abs(gx), abs(gy), math.degrees(abs(cmath.phase(gy / gx)))))
v = np.random.default_rng(1).normal(size=16); v /= np.linalg.norm(v)
print('squared norms of the two halves of a unit vector sum to %.12f (the half-norms themselves sum to %.4f)' % (v[:8] @ v[:8] + v[8:] @ v[8:], np.linalg.norm(v[:8]) + np.linalg.norm(v[8:])))
A = np.array([[1, -1], [1, 1.0]]); B = np.array([[2, 1j], [0, 1.0]]); f = lambda M, z: (M[0, 0] * z + M[0, 1]) / (M[1, 0] * z + M[1, 1])
print('Mobius composition vs matrix product: |f_A(f_B(z)) - f_AB(z)| = %.1e' % abs(f(A, f(B, 0.3 + 0.2j)) - f(A @ B, 0.3 + 0.2j)))
x = np.linspace(0, 2 * np.pi, 2000001)
print('integral of sin^2, cos^2 over [0, 2pi]: %.10f, %.10f ; sin^2 = cos^2 = %.6f at pi/4' % (np.trapezoid(np.sin(x)**2, x), np.trapezoid(np.cos(x)**2, x), math.sin(math.pi / 4)**2))
```

```
max |Gamma - tanh(ln(Z/Z0)/2)| over 20000 random complex pairs: 2.03e-12
cross-ratio change under the fold for anchors 0.3, 1, 7+2i, -pts[0]*1.0001: [0.0, 0.0, 0.0, 0.0]
min |dGamma/dZ| over |Z| = 1e-3..1e6: 2.00e-12 ; near the pole Z -> -Z0: 2e+12
arg Gamma for Z = lam(1+i), anchor 1, lam = 0.5, 1, 5, 50: [2.0344, 1.1071, 0.2013, 0.02] ; arg(lam Z) = 0.7854
tangent vectors |d/dx| = 0.588235 |d/dy| = 0.588235 angle 90.0000 deg
squared norms of the two halves of a unit vector sum to 1.000000000000 (the half-norms themselves sum to 1.3789)
Mobius composition vs matrix product: |f_A(f_B(z)) - f_AB(z)| = 0.0e+00
integral of sin^2, cos^2 over [0, 2pi]: 3.1415926536, 3.1415926536 ; sin^2 = cos^2 = 0.500000 at pi/4
```

## 6. The datatype and the generalised equation (2026-08-28)  `THEORETICAL`

The fold Γ = tanh(½u) is the generating function of Aff(1, ℝ) acting on ln x. Every framework quantity is a **word** in the tier-0 generators {ADD, SCALE, SIGN}, anchored on a d\* face:

```
u = Σₖ [ gₖ ln sₖ + aₖ ]      Γ = tanh(u/2)
          SIGN  SCALE   ADD
GROUND STATE   aₖ → 0, sₖ → 1, gₖ → +1  ⇒  u = 0  ⇒  Γ = 0  ⇒  x = the anchor
               = the now / the viewport / SCALE at identity = "readiness = ground state = only ADD:SCALE:SIGN"
```

It is said to cover the constant placements, Σ_RB (the composite ADD:SCALE:SIGN lineage, 2·ADD / 3·SCALE / 4·SIGN), the Penrose {4:8:4} (past/now/future = ADD/SCALE/SIGN), the curriculum (one word, out and back) and the error check (the residual between two anchor faces); it **closes** iff d\*_RG (the Stability face) gets a closed form, the depth → ∞ fixed point of "fold the fold", currently OPEN ([17](17_alpha_omega_d_star.md)). Built as a value type, `ValaQuenta/modules/add_scale_sign/` (`ASS`, `ASSWord`): compose with `@`, invert with `~`, take
residuals, decompose into an `ASSWord` in two orderings (chrono / zeta), read out on orthogonal Smith charts; firing order is the three-phase camshaft SIGN → SCALE → ADD, and the firing defect (g − 1) ln s is non-zero exactly when the SIGN flips a non-trivial SCALE ("defined twice", the same shape as the Bell composed-rotation defect). Whether the listed quantities all *are* words of this form is the design claim; the identity of §5 is what is established.

## 7. "Locally square"  `ESTABLISHED`

At any point the two ring-directions' tangent vectors are equal in length and 90° apart (Listing 1: 0.588235 and 0.588235 at 90.0000°), for any choice of what the two rings mean: a consequence of the fold being holomorphic in Z (conformal), independent of what the caller assigned to ring₁ and ring₂. Every curvilinear cell of the chart is locally a square by construction, before any physical interpretation.

## 8. User-defined rings, and the pairing that turned out to be fake

`custom_ring_chart` takes any two functions of any object. Five proposed pairs were tested on real data (numbers in `ValaQuenta/wiki/scale.md` §8; not re-run). The one worth repeating: **J_red and J_blue are not two independent rings.** The recorded finding is "J_red + J_blue = 1.0000000000 on every real sentence tried", because the encoder returns a unit-normalised vector split into two non-overlapping halves. Precisely, it is the **squared** norms of the two halves that sum to 1 (Listing 1: 1.000000000000, while the half-norms sum to 1.3789): what looked like two rings is
one number (σ_self) under two labels. The two-independent-ring version pairs σ_self against J_green (the su(2) bracket quantity, [J_blue, J_red] = J_green); note the sign/bracket issues of [70](70_precession_stroke_oblique_crank_trine.md) §4 before building it. This is what testing a "what if" is for: catching the one pairing that looked plausible and was not.

## 8b. The Broca–Wernicke Rings Scale (2026-11-21)  `ESTABLISHED` (the identities) · `THEORETICAL` (the reading)

The Scale has taken a pair of rings from the beginning: any two readings of one object, laid out as the two axes of a plane and folded. The author's next pair is the one the sentence engine needs. The vertical rings are **Broca** and the horizontal rings are **Wernicke**. Broca is the discrete reading of an object's context (the scalar boxkite: one word, seven ordered pairs, a count that is either this or that). Wernicke is the continuous reading (the scaled boxkite: a field the sentence moves through). The point Z = Wernicke + i·Broca is then folded as before, so everything the engine already proves about the fold holds for it: the cross-ratio of any four such points survives every anchor, and the cells are locally square.

Two things come with it. First, **two pathways**: one to the centre and one from it. The fold's inversion (impedance ↔ admittance, Γ → −Γ) turns the first into the second, and the two Γ cancel at the matched load. That is the same shape as the pair the project already carries as J_red and J_blue, the Noether current and the reversed Noether information current, and the same shape as an orb web's two kinds of thread (the radial ones that carry, the spiral ones that catch). Whether the pairing is more than a resemblance is **not established**; the engine only proves the inversion. Second, **the spiral similarity**: scaling and rotating at once is one addition in the log chart (scale on the real axis, rotation on the imaginary axis, the same r and θ as the polar decomposition on page 1), and a fixed scale and angle trace a logarithmic spiral, the curve that keeps its shape under both. A sentence that contracts to its next word and grows back with the word in place is that move with a changing scale at each step.

Where it lives: `ValaQuenta/modules/scale` v0.2 (`broca_wernicke_ring_chart`, `broca_wernicke_ring_series`, `two_pathways`, `spiral_similarity`); the theory page is `ValaQuenta/wiki/scale.md` §9.

## 9. What is speculative, stated as speculative

- **"Witches hat into a galaxy."** The Higgs/Mexican-hat potential (an unstable symmetric maximum ringed by a trough of degenerate vacua) resembles the fold's singular centre Z₀ surrounded by a continuum; inflationary models do use a hat-shaped scalar potential to seed density fluctuations. The shape resemblance is real; the identification of the two objects is not shown.
- **"Black hole unwrapping into a white-hole gravastar before evaporation and BANG."** Gravastars and black-hole-to-white-hole bounce models are published, non-mainstream proposals; the fold's isolated pole (Z = −Z₀, verified in Listing 1) is a mathematical fact the image evokes, not evidence that the physics is right.
- **"Between causality and the informational thermal ceiling, even this tool loses resolution"** is a closing limit, not a new claim: the project's named boundary for that idea is d\* ([17](17_alpha_omega_d_star.md)), and any instrument built on the fold inherits it.

## 10. Related pages

[92 the ring-theory spine](92_ring_theory_spine.md) · [96 the Riemann–Fermat Horizon](96_the_riemann_fermat_horizon.md) · [97 units as the equation index](97_units_as_the_equation_index.md) · [17 α, Ω and d\*](17_alpha_omega_d_star.md) · `PtolemyDesktop/Kryptos/Ciphers/` (Vigenère, Enigma, RSA: the ciphers the instrument was tested against)
