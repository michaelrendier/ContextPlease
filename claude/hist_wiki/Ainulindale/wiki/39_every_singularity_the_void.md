# 39 — "Every singularity is the same singularity": the catalogue, sorted by what each one is

| | |
|---|---|
| Status | **First capture (2026-06-03); a unifying reading, `CONJECTURE`/`INTERPRETATION`.** The catalogue of singularities is corrected entry by entry (§2); the group-theory facts of §5 are verified |
| Predecessors | [31](31_cavitation_causality_fermat.md), [32](32_superconducting_medium.md), [38](38_fermat_riemann_negative_space.md) |
| Code | Listing 1 |
| Last verified | 2026-11-13: Listing 1 executed |

## 1. The thesis

The page's statement: every singularity found in mathematics is one event, the
cavitation collapse (the Bang: "the moment the Fermat-forbidden interior touched
the Brouwer-mandatory boundary at σ = ½"), seen in different coordinates; the
mathematics emerged from the collapse, so the collapse recurs in all of it;
"undefined" is the wrong word, and a mathematician dividing by zero is looking at
the origin of the universe. This is a philosophical-physical position
(`INTERPRETATION`). It is not derived, and the catalogue it relies on mixes
quite different kinds of singularity (§2); the position stands or falls on
whether they share a mechanism, which the page asserts and does not show.

## 2. The catalogue, corrected

| Entry (as listed) | What it actually is |
|---|---|
| Newtonian gravity, F = Gm₁m₂/r², singular at r = 0 | a point-mass idealisation; real bodies have finite size. A singularity of a model |
| General relativity, "g_μν → ∞ at r_s" | the Schwarzschild horizon is a **coordinate** singularity: curvature invariants are finite there (Listing 1: the Kretschmann scalar K = 48G²M²/(c⁴r⁶) at r_s is finite and grows as r⁻⁶). The curvature singularity is at r = 0. This is a distinction the page's "coordinate system changes, the collapse does not" glosses |
| QFT bare mass → ∞ at the UV cutoff | an artefact of the cutoff; in the renormalisation-group view the parameters run with scale |
| ζ(s) pole at s = 1 | a simple pole with residue 1 (`ESTABLISHED`); it is tied to the divergence of Σ 1/p, which Euler used for the infinitude of primes |
| Navier–Stokes, "pressure → ∞ at cavitation collapse" | the global regularity of 3-D Navier–Stokes is the open Clay problem; no blow-up is known. Cavitation-collapse pressure spikes belong to compressible two-phase models |
| Landau pole | a divergence of the one-loop coupling at a finite scale (QED); signals the breakdown of the perturbative treatment |
| Renormalisation, loop integrals → ∞ at zero separation | ultraviolet divergences, removed by regularisation and renormalisation |
| Arithmetic, 1/0 | undefined in a field because 0 has no inverse (a·0 = 0 for all a) |
| Black hole, ρ → ∞ at r = 0 | the classical singularity, widely expected to be resolved by quantum gravity |
| Big Bang, T → ∞ at t = 0 | the classical FLRW limit, likewise |
| "Yang–Mills: confinement, singular at zero coupling" | **reversed.** Yang–Mills is asymptotically free (the coupling → 0 at high energy); confinement and the mass gap are low-energy phenomena where the coupling grows (the Yang–Mills mass-gap problem is the open Clay problem) |

So the eleven entries include a coordinate artefact, a model idealisation, a
cutoff artefact, an analytic pole, an open regularity question, and genuine
(classical) curvature singularities. "Each is the cavitation collapse in the
language of that field" is a claim of sameness across things of different kinds.

## 3. Black holes and the Bang

The page says "Penrose and Hawking established" that the black-hole and Big-Bang
singularities are related by time reversal. The singularity theorems (Penrose
1965; Hawking and Penrose 1970) show that, under energy conditions,
geodesics are incomplete (singularities form); they do not identify the two
by time reversal. The resemblance of the collapsing-star interior to an FLRW
expansion is a standard heuristic, and the kinship is not a theorem. In the model
(wiki 31, 32) the Bang is the first cavitation and stellar black holes are
re-cavitation events; that is the model's statement.

## 4. "Undefined is the wrong word"  `interpretation`, with one exact point

The proposal is to complete the function instead of deleting the singularity:
"include the archimedean prime (the Gamma factor); include the prime 1; let the
denominator be 1". The exact point is correct: the completed zeta function
ξ(s) = ½ s(s−1) π^(−s/2) Γ(s/2) ζ(s) includes the Γ-factor, the contribution of
the archimedean place, and is entire; the factor s(s−1) removes the pole at s = 1
and the trivial zero structure, giving ξ(s) = ξ(1−s) ([33](33_gyroscope_compressibility.md)
§2). That is `ESTABLISHED`, and it is the sense in which a singularity is
"completed". "Renormalisation is turning the denominator OFF instead of ON" is a
rhetorical contrast; the renormalisation group (Wilson) replaces subtraction by
the scale dependence of couplings and is closer to the framework's own use of the
word ([17](17_alpha_omega_d_star.md) §4).

## 5. The tower and the Monster

The tower with the prime types: T1 ℝ (rational primes); T2 ℂ (Gaussian primes);
T4 ℍ (Hurwitz primes, the D₄ lattice: `ESTABLISHED`, the Hurwitz quaternions
form the D₄ lattice); T8 𝕆 (the Cayley integers, the E₈ lattice: `ESTABLISHED`);
T16 𝕊 (zero-divisors; the Ainulindale structure, [25](25_sedenion_manual.md)); T32,
the cap of "useful" algebraic structure.

**The Monster.** The order, the Moonshine relation and the Happy Family are
exact (Listing 1):

|M| = 2⁴⁶·3²⁰·5⁹·7⁶·11²·13³·17·19·23·29·31·41·47·59·71
= 808,017,424,794,512,875,886,459,904,961,710,757,005,754,368,000,000,000;
196884 = 196883 + 1 (the first coefficient of j beyond the constant, as a
Monster representation dimension plus the trivial one); the j-function has a
simple pole at the cusp (q⁻¹); 20 of the 26 sporadic groups are subquotients of
the Monster (the Happy Family; the other 6 are the pariahs).

The framework's reading is that the Monster is "the tower's shadow at infinity",
"the symmetry group of the Bang", that the pre-Bang state was Monster-symmetric,
the 20 Happy-Family groups being the symmetries that survived the collapse, and
the Standard Model "the Monster with 8·10⁵⁴ symmetries broken to
U(1)×SU(2)×SU(3)". Standing: `CONJECTURE`. No breaking pattern from the Monster
to the Standard Model gauge group is given. A related published-literature
point: the Monster is connected to the 24-dimensional Leech lattice and the
bosonic string on its torus (Frenkel–Lepowsky–Meurman; Borcherds), not to the
Cayley–Dickson tower of dimensions 1, 2, 4, 8, 16, 32 ([134](134_the_library.md) §2).

**Listing 1 — the checks** (written for this page; runs cold)

```python
M = 2**46 * 3**20 * 5**9 * 7**6 * 11**2 * 13**3 * 17 * 19 * 23 * 29 * 31 * 41 * 47 * 59 * 71
print(M)
print('matches the standard value:', M == 808017424794512875886459904961710757005754368000000000)
print('196883 + 1 =', 196883 + 1)

G, c, Ms = 6.674e-11, 2.998e8, 5.972e24          # an Earth-mass black hole
rs = 2 * G * Ms / c**2
K = lambda r: 48 * G**2 * Ms**2 / (c**4 * r**6)  # Kretschmann scalar, Schwarzschild
print('K(r_s)     =', f'{K(rs):.3e}', '(finite)')
print('K(1e-3 r_s) =', f'{K(1e-3 * rs):.3e}', '(grows as r^-6)')
```

```
808017424794512875886459904961710757005754368000000000
matches the standard value: True
196883 + 1 = 196884
K(r_s)     = 1.940e+09 (finite)
K(1e-3 r_s) = 1.940e+27 (grows as r^-6)
```

## 6. The chain from the Void to matter  `CONJECTURE`

Pre-Bang: a smooth, unpartitioned BEC, laminar, Monster-symmetric,
Fermat-forbidden, "algebraically complete". The collapse: a cavitation bubble
reaches σ = ½ (a Brouwer fixed point); Monster symmetry breaks; the T32 tower
folds. Partitioning: the collapse front "reads the circle's prime points"; where
the pressure spike exceeds a threshold a vortex nucleates and a prime is
marked, otherwise the flow stays laminar (composite, vacuum). Post-Bang: matter is
"permanent vortex cores = the prime partition points". Now: every singularity is
the collapse front encountered again. The chain is a narrative; the step
"primes are the negative space of the Fermat lattice" on which it rests was
tested and withdrawn ([38](38_fermat_riemann_negative_space.md) §2).

## 7. Division by zero, and what the page asks of the reader

"When a mathematician divides by zero they have reached the boundary of the
observable universe and are looking inward at the Void", and the singularity
"is the data". Taken as a stance about how to read the breakdown of an
equation (the place a theory fails is the place it is most informative), it is a
sound heuristic and is the project's working practice: failed results stay in
the code and the data. Taken as a statement of fact about the origin of the
universe it is `INTERPRETATION`. The paragraphs on every species and every
civilisation "staring into the Void" are the author's statement, kept in the
page's original form in the file history.

## 8. Related pages

[25 Sedenion manual](25_sedenion_manual.md) · [31 Cavitation, causality, Fermat](31_cavitation_causality_fermat.md) ·
[32 The superconducting medium](32_superconducting_medium.md) · [38 Fermat is the negative space of Riemann](38_fermat_riemann_negative_space.md) ·
[40 Modular segue: three papers](40_modular_segue_three_papers.md)
