# 143 — Relativity as Four Spaces, Each With Its Own Jurisdiction

| | |
|---|---|
| Written | 2026-11-19 |
| Scope | special and general relativity as an engine; why it is organised by space and not by field content; what each space allows and forbids; the crossings; what was measured; where the question "where is GR, F = ma, Navier–Stokes, QM, string theory" lands in this arrangement |
| Requested by | Cody, 2026-11-19: "i need a Full Engine Protocol for Einstein's Relativity, general and special"; and on the first layout: "relativity is a different space isn't it? different jurisdictions...it should not be following a L_SM layout at all" |
| Predecessors | [140](140_length_and_time.md) (the conversion field, the Penrose swap) · [139](139_three_lagrangians.md) · [142](142_units_flattening_and_emergence.md) · the `spatial-simulation` skill, spaces §§1–2, 9 |
| Code | `ValaQuenta/modules/relativity/` · tests `ValaQuenta/Testing/test_relativity.py` (31, all pass) · notebook `ValaQuenta/notebooks/engines/26_relativity.ipynb` · wiki `ValaQuenta/wiki/relativity.md`, toolbox 43 |
| Confidence | the four spaces and every number: `ESTABLISHED:CALCULATED` · §5 (the prime-boost bridge, the conversion field read as a spacetime): `INTERPRETATION` · nothing here derives relativity from the Null Operator |

> **Note from the assistant.** Written by a transformer (Claude Sonnet 5.5, `claude-sonnet-5-5`) working with Cody Allison in Claude Code. Cody does not tell the model what result he wants. My first layout followed the L_SM engine (content, measured numbers); Cody corrected it at once: relativity is a family of spaces. The correction is the structure of the engine, not a detail.

## 1. Why four spaces, and what a jurisdiction is

The Standard Model is one theory in one space (field space), so L_SM is organised by content. Relativity is not: the *same words* mean different things in different spaces, and an operation that is correct in one is an error in another. The engine therefore declares four spaces, each with the eight fields of the spaces skill (points, axes, motions, invariant, views, acceptance test, repo, status) and a **jurisdiction**: the set of operations legal in it. The test of legality is `bracketing_firing_order.jurisdiction_violation`, reused: a violation is a failed set-membership test.

| space | points | what is legal | what is a violation |
|---|---|---|---|
| **Minkowski** (SR) | events, flat | global boosts, translations, adding vectors anywhere, global simultaneity within a frame, global energy-momentum conservation | gravitational potential, curvature, tides |
| **curved** (GR) | events on a Lorentzian manifold | local frames, geodesics, parallel transport, covariant conservation, curvature | global boost, adding vectors at different events, global simultaneity, global energy conservation (without a Killing vector), translation |
| **tangent** | vectors at one event | SR: boosts, velocity addition, invariant mass | removing the curvature, anything beyond second order in distance |
| **metric** | a whole geometry g(x) | varying the action, gauge orbits, linearising, the lapse constraint | evolving in absolute time, a fixed background, a unique coordinate description |

Operations that are legal in one space and illegal in another are the **crossings** (`crossing_table()`): global boost, global simultaneity, global energy-momentum conservation, translation. Using Minkowski's language in curved space on exactly these is the standard error.

## 2. Minkowski: measured

Composed boosts preserve η to 10⁻¹⁶; velocity addition is addition of rapidity (residual 10⁻¹⁶); the Lorentz algebra closes (six generators); the Thomas–Wigner rotation of 0.6c then 0.7c perpendicular boosts is 15.50° and matches (γ₁+γ₂)/(1+γ₁γ₂) to 3×10⁻¹⁶; the p + p → p + p + p + p̄ threshold is 6 mₚc² of kinetic energy; a 1 g trip of 4.37 light years takes about 3.5 years of proper time; E² − c²B² and E·B survive a boost. A boost is a **dilation** of u = ct + x and v = ct − x: u → u/k, v → kv with k = √((1+β)/(1−β)) the Doppler factor.

## 3. Curved: measured

Symbolic from the metric alone: Schwarzschild is vacuum (Ricci = 0) with Kretschmann 48M²/r⁶; static de Sitter has G = −Λg with Λ = 3/L²; flat FLRW has G_tt = 3ȧ²/a²; the contracted Bianchi identity ∇_μG^{μν} = 0 holds for curved FLRW; the tidal component R_{trtr} = −2M/r³, and two nearby radial free-fallers separate with ξ″ = 2M/r³ ξ (ratio 1.00002); a plane TT wave solves the vacuum equations iff ω² = k². Numbers: Mercury 42.98″ per century; light grazing the Sun 1.751″; GPS +38.5 µs per day (45.7 gravitational, −7.2 velocity); Hulse–Taylor Ṗ_b = −2.40×10⁻¹² (orbital elements from memory, to verify); the integrated null geodesic matches 4M/b·(1 + 15πM/16b) to 10⁻⁴ at b = 1000M; the integrated orbit advances 4 % above 6πM/p at p = 200M and tends to the formula as p grows. Horizons: 2.953 km for the Sun, photon sphere 1.5 r_s, ISCO 3 r_s, Hawking T = 6.17×10⁻⁸ K.

## 4. The tangent and metric spaces, and the crossings

**Tangent:** at one event the connection can be removed by a coordinate change (Γ: 10.04 → 0) and the curvature cannot (Kretschmann 4.8×10⁻⁵ at r = 10M, unchanged): the equivalence principle is exactly this statement. Special relativity is legal there and only there inside general relativity. **Metric:** on the (a, N) slice of the space of metrics the Einstein–Hilbert action varied with respect to the lapse N gives 3aȧ²/8πG − a³ρ = 0, the first Friedmann equation, as a constraint (N is a Lagrange multiplier; its equation has no derivative of N); the linearised Riemann of a pure-gauge h = ∂ξ + ∂ξ vanishes identically. **Crossings:** weak field gives R₀₀ = ∇²Φ (Poisson); smoothness of the Euclidean horizon fixes the period 8πM and so T = 1/8πM; M → 0 sends K = 48M²/r⁶ to 0 (the way back to Minkowski).

## 5. Where the project's own structures meet it (`INTERPRETATION`)

- **The conversion field of wiki 140 is a 1+1 spacetime.** Read length = v · time as ds² = −v(x)²dt² + dx²; its curvature is R = −2v″/v. The hat at E = 0 has v = x√(1 − x²/2): a simple zero at the hilltop with surface gravity κ = 1 (horizon-like: infinite transit time) and a square-root zero at x = √2 (a mirror). This is the same classification wiki 140 reached from the transit integral, now arrived at from the curvature side. Where the Rindler case v = κx is flat, the hilltop is curved (R(0) = 3).
- **Prime boosts.** A boost with Doppler factor p (integer) has β = (p²−1)/(p²+1), γ = (p²+1)/2p and the Pythagorean triple (p²−1, 2p, p²+1): p = 2 gives 3-4-5 and β = 3/5, p = 3 gives 8-6-10 → 4/5. Composing the boosts p and q is the boost pq (exact in Fractions), so the boosts of a line with rational Doppler factor form the multiplicative group of the positive rationals, and the rapidity of any of them is Σ e_p ln p over a unique prime factorisation (e.g. 12/5 → 2²·3·5⁻¹). ESTABLISHED arithmetic. The reading that follows, **Lorentz composition along a line is prime factorisation of the Doppler factor**, is an interpretation; whether the Null Operator's shifts R_p are such boosts depends on the definition of R_p, which this engine does not use. Nothing is claimed.

## 6. Where is GR, F = ma, Navier–Stokes, QM, string theory

In this engine's arrangement: **GR** is the curved space plus the space of metrics (built, measured above). **Special relativity** is Minkowski and, locally, the tangent space. **F = ma** is a crossing: Newton is the weak-field, low-velocity limit of the curved space (R₀₀ = ∇²Φ, the field-equation half, is computed here; the low-velocity limit of the geodesic equation is not derived separately: the integrated orbits show the relativistic correction shrinking as M/p → 0, which is consistent with it but is not that derivation). **Navier–Stokes**, **quantum mechanics** and **string theory** are not spaces of this engine: they would be separate jurisdictions (a continuum-fluid space, Hilbert space, a worldsheet space) with their own legal operations and their own crossings to these. That arrangement, not a single containing operator, is what the engine shows; whether the Null Operator reaches each is the Equation Space question (`FourthAgePapers/EquationSpace`).

## 7. Not shown

No derivation of relativity from the Null Operator; the prime-boost reading is arithmetic plus interpretation. Kerr beyond the horizons, black-hole thermodynamics beyond T_H, cosmological perturbations, numerical relativity, the Penrose–Carter diagram and the full ADM decomposition are not built. The Hulse–Taylor elements and the observed Ṗ_b are from memory and are to be verified under the Literature Download Protocol.

## Appendix — what in ContextPlease was used

ContextPlease is the project's public archive of the context a session needs to come up to speed: primers, scratchpads, skills, wiki mirrors and the `.clauderc*` context files. Used here: the `spatial-simulation` skill (the eight-field description of a space and the Minkowski section), `~/.clauderc_ValaQuenta` (the `bracketing_firing_order` jurisdiction record), Ainulindale wiki 140 and 142, and the scratchpad `2026-11-19_lagrangian_sm/` (the hat's conversion-field results).
