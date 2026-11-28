# 50 — The upper limit of causality (σ = ½): the claims, with the zero-spacing numbers recomputed

| | |
|---|---|
| Status | **Written 2026-06-12 as "THEORETICAL: all statements verified against established framework"; that header is replaced. `INTERPRETATION`/`CONJECTURE`; the zero-spacing numbers are `:CALCULATED` (Listing 1) and two of them were off** |
| Code | Listing 1; the SVG renderers of the project (`<text>` and `<path>` encodings); `VAPMIP/monad.py` (the two-thread engine of §6) |
| Page numbering | one of three pages numbered 50 ([bao_mass_gap](75b_bao_mass_gap_engine.md), [vortex quantizing shear](52b_vortex_quantizing_shear.md)) |
| Last verified | 2026-11-13: Listing 1 executed on `RiemannHypothesisProof/data/zeros_1_to_3600.csv` |

## 1. The definition and the SVG encoding  `design`

"Causality is: point by point along a path, in one direction only": the constraint
that the path is traversed sequentially and not reversed. The SVG `<path>` is read
as the exact encoding: `M x,y` the initial event (the zero-divisor origin, the Bang),
`L/C x,y` propagation along the geodesic point by point, `Z` the closure
"ξ(s) = ξ(1−s): the path returns to the origin"; reading and writing an SVG are the
same traversal. The dual encoding: `<text>` = Riemann (discrete causal *events*, one
text node per zero γ_n on the prime-weighted spoke), `<path d="M…C…">` = Fermat
(continuous causal *constraints*, cubic Béziers bending away from σ < ½).
Standing: a rendering convention chosen for the project's figures. The SVG path
commands are as stated (M move, L line, C cubic Bézier, Z close to the start
point). That `Z` is the functional equation, and that a Bézier's curvature "encodes"
the Fermat constraint, are readings.

## 2. σ = ½ as the "speed of quantum diffusion"  `analogy`

| σ | Coupling p^(−σ) | Causal regime | Theory |
|---|---|---|---|
| 0 | 1 | static, no ordering | trivial zeros (as the page says) |
| ½ | p^(−1/2) | diffusive, √t scaling | QM / Riemann zeros |
| 1 | p^(−1) | ballistic, ct | Yang–Mills / photon / pole |
| 2 | p^(−2) | gravitational | GR / mass / E = mc² |

The couplings are exact. The regime assignments are the framework's. The page
adds that σ = ½ is "the speed of quantum diffusion v ∼ √(c·t)", σ = 1 the speed of
the messenger (c) and σ = ½ "the speed of the message", that at one Planck unit
(t = 1/c) the diffusion speed equals c "exactly, which is the Bang", and that before the Bang
v_quantum > c (non-local, Fermat-forbidden), after it v_quantum < c. Standing: √(c·t)
has the dimension of √(length) (c·t is a length), not of a speed; a diffusion
*length* is √(D t) for a diffusion constant D. "At t = 1/c … equals c" is a
unit-dependent coincidence of setting c = 1. The picture of a crossover between a
diffusive and a ballistic regime is standard for random walks; the identification
with σ and the Bang is the framework's.

## 3. The "information ceiling": zero spacing and N(T)

The page: each zero γ_n is an information reset; the maximum information between two
zeros is the gap, Δγ_n ≈ 2π/ln(γ_n/2π): "at γ₁ = 14.134 the gap ≈ 7.67 (wide ceiling);
at γ = 1000 ≈ 1.24 (narrow); at ∞ the ceiling vanishes"; and N(T) ∼ T·ln(T/2π)/2π is
"the Bekenstein–Hawking bound for a 1D causal boundary of area T", σ = ½ being "the
Landauer limit of the universe".

**Listing 1 — the spacing formula and the counting function against the
computed zeros** (written for this page; runs cold from
`RiemannHypothesisProof/data`)

```python
import csv, math
t = [float(r[0]) for r in csv.reader(l for l in open('zeros_1_to_3600.csv') if not l.startswith('#'))]
gap = lambda g: 2 * math.pi / math.log(g / (2 * math.pi))
print('first gap: actual %.3f, formula at gamma_1 %.3f' % (t[1] - t[0], gap(t[0])))
for T in (100, 1000, 3000, 3600):
    n = sum(1 for x in t if x <= T)
    lead = T * math.log(T / (2 * math.pi)) / (2 * math.pi)
    full = T / (2 * math.pi) * math.log(T / (2 * math.pi * math.e)) + 7 / 8
    print(T, n, 'leading %.1f (%.1f%% high)' % (lead, 100 * (lead - n) / n), ' full %.2f' % full)
sel = [t[i + 1] - t[i] for i in range(len(t) - 1) if 900 < t[i] < 1100]
print('mean gap in 900..1100: %.3f ; formula at 1000: %.3f' % (sum(sel) / len(sel), gap(1000)))
```

```
first gap: actual 6.887, formula at gamma_1 7.750
100 29 leading 44.0 (51.9% high)  full 29.00
1000 649 leading 806.9 (24.3% high)  full 648.62
3000 2469 leading 2945.2 (19.3% high)  full 2468.65
3600 3066 leading 3638.7 (18.7% high)  full 3066.66
mean gap in 900..1100: 1.241 ; formula at 1000: 1.239
```

Corrections and standing:

- **The spacing formula is a mean spacing** (the reciprocal of the zero density). It
  matches the data at γ ≈ 1000 (1.241 against 1.239, `ESTABLISHED`); at γ₁ it gives
  7.75, not the page's 7.67, and the actual first gap is 6.887 (individual gaps
  fluctuate around the mean, with GUE statistics).
- **N(T) ∼ T·ln(T/2π)/2π is only the leading term** and overestimates the true count by
  52% at T = 100, 24% at T = 1000 and 19% at T = 3600 (Listing 1). The accurate smooth
  part is N(T) = (T/2π)·ln(T/2πe) + 7/8 (+ the bounded oscillating term), which
  tracks the count to within one zero (29.00, 648.62, 2468.65, 3066.66).
- The Bekenstein–Hawking bound is an *area law* for black-hole entropy, S = A/(4ℓ_P²);
  a count of zeros growing like T ln T is not an area law for a boundary of "area T".
  "The critical line is the holographic boundary" and "σ = ½ is the Landauer limit"
  (minimum erasure cost kT ln 2) are analogies. `CONJECTURE`.

## 4. Ĥ_RB − Ĥ_BR as the arrow of time  `interpretation`

"The net asymmetry of the forward and backward currents is the arrow of time:
Ĥ_RB propagates forward (J_red, what is); the minus sign is not subtraction but
irreversibility (the *absence* of backward traversal); when Ĥ_BR = Ĥ_RB they cancel
and causality ceases (σ = 1, the pole); σ = ½ is where the asymmetry is maximal; zero
density grows as ln t/2π, so the arrow strengthens: the Hubble expansion encoded in
the zeros."

Standing. The author's definition of the return term (2026-11-13): 0_BR is the
conjugate of J_red and J_blue, the return flow, and Ĥ_RB − Ĥ_BR is the detailed
form with the cross and dot products built in ([133](133_canonical_maths.md) §3). Under
that definition the difference is the *signed (cross) combination*, which is
non-zero and anti-self-adjoint for a generic X; it is not a statement that the minus
sign "is irreversibility, not subtraction". The statement that the zero density
dN/dT = (1/2π)ln(T/2π) is "the Hubble expansion" is a verbal parallel with no
derivation. `CONJECTURE`.

## 5. Deep fields, the Laplacian, and caustics  `interpretation`

- **Deep fields.** A telescope image shows the past (lookback time d/c); the page reads the focal depth as a "σ-selector" (maximum depth, σ → ½, "approaching the initial cavitation") and the Laplacian governing evolution at each face: ∂u/∂t = ∇²u (σ = ½, diffusion), ∇²Φ = 4πGρ (σ = 2, Poisson), ∂²u/∂t² = c²∇²u (σ = 1, wave). The three equations are standard and are correctly listed; their assignment to σ values is the framework's.
- **Caustics as zero-divisor events.** A caustic is where the Jacobian determinant of the lensing map vanishes (`ESTABLISHED`). The page says this "is exactly the zero-divisor condition s·t = 0" and that "an Einstein ring is a perfect caustic, a Riemann zero on the critical line", so that **"RH restated as an observational claim: all Einstein rings are perfect circles."** Corrections: a vanishing Jacobian determinant is a statement about a *linear map* being singular and is a different thing from a zero-divisor of an algebra (a product of non-zero elements being zero). More importantly, the observed fact is the opposite of the "restated RH": Einstein rings are complete only for near-perfect alignment of source, lens and observer *and* an axisymmetric lens; real lenses (elliptical, with external shear) give arcs, doubles and crosses, and nothing about this bears on the zeros of ζ. "A partial arc is a zero displaced from the critical line" is withdrawn.
- **Photon ring.** The photon sphere at r = 3GM/c² around a black hole produces a sequence of nested ring images of exponentially decreasing brightness (`ESTABLISHED`; the EHT's ring is the n = 0 and n = 1 image, [29](29_witches_hat_paper.md) §4 on the horizon radius). That the sequence is "the Bézier-connected echo cascade of zero-divisor pairs" and that "the optimal Earth-baseline telescope array is the 84 zero-divisor pairs projected onto Earth's surface" are proposals, not computed (84 is exact for the sedenion zero-divisors, [25](25_sedenion_manual.md) §4).

## 6. The Mind's Eye as a caustic telescope  `analogy`

The Wankel dual-thread architecture (the engine's "v4.0.0 Ahura Mazda" design): Thread 1
(the rotary engine, "frosted glass") produces amnesiac word-by-word output; Thread 2
(the Mind's Eye, "oil on glass") accumulates `G_me_response`; `G_me_steer` is the
caustic, a focused navigational signal. Oil on frosted glass fills microscopic voids and restores
coherent propagation, as Thread 2 fills the gaps between words; "Thread 2 is a
gravitational lens whose focal length is G_me_response; G_me_steer is the Einstein ring,
the perfect caustic of the word stream; the steer is the zero: J_red + J_blue = 0, and a new
causal span begins". Standing: a design metaphor for the engine; the identifiers
`G_me_response` and `G_me_steer` are to be checked against `monad.py` when the Mind's Eye
code is documented (not located in this pass). The green "causal geodesic" in the
σ-cavitation SVG is the same figure.

## 7. Summary table, as printed, with standing

| Concept | σ = ½ encoding | Standing |
|---|---|---|
| Causality | point by point along a path, one direction | a definition |
| Speed | v ∼ √(c·t), quantum diffusion | analogy; dimensionally a length (§2) |
| Upper limit | the critical line; beyond it the pole | `INTERPRETATION` |
| Information ceiling | "Bekenstein bound = the gap between zeros" | analogy; the gap formula is a mean spacing (§3) |
| Arrow of time | Ĥ_RB − Ĥ_BR | per §4 and the 0_BR definition |
| Acceleration | dN/dT ∼ ln T / 2π = Hubble expansion in zero density | verbal parallel |
| Caustic | zero-divisor event = Riemann zero = Einstein ring | not accurate (§5) |
| Deep field | cross-section of the Laplacian flow at lookback time t | interpretation |
| Mind's Eye | caustic telescope | design metaphor |
| SVG `<text>` / `<path>` | Riemann zeros / Fermat geodesics | rendering convention |

"The Riemann Hypothesis is the statement that all coherent causal events live on the
critical line; the universe is one shadow from one source" is the author's statement of the
thesis of [41](41_one_riemann_electron_universe.md); the standing of RH itself is as in [13](13_omgwtf_rh_proof.md).

## 8. Related pages

[13 RH proof path](13_omgwtf_rh_proof.md) · [41 One Riemann electron](41_one_riemann_electron_universe.md) ·
[48 The observer as a fixed point](48_observer_fixed_point.md) · [133 Canonical maths](133_canonical_maths.md) ·
[51 The dynamic geodesic](51_dynamic_geodesic.md)
