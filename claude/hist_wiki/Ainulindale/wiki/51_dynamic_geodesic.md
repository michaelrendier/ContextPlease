# 51 — The dynamic geodesic: L_FR = 0, the slingshot term, and the primes-as-cavitation reading

| | |
|---|---|
| Status | **THEORETICAL as headed (2026-06-13, cascade from [52b](52b_vortex_quantizing_shear.md)); in this wiki `CONJECTURE`/`INTERPRETATION` with three corrections found by calculation: ζ(s) ≠ Σ p^(−s) (§6), primes are sums of two powers (§2), the generalised Fermat equation has solutions (§2)** |
| Code | Listing 1; the L_(I|O) engine `ValaQuenta/modules/l_io_photon_path` ([82](82_l_io_photon_path.md)); the SVG Bézier renderers |
| Page numbering | one of two pages numbered 51 (the other: [j2 involution](52c_j2_involution_riemann_fermat.md)) |
| Last verified | 2026-11-13: Listing 1 executed |

## 1. L_FR = 0  `interpretation`

Three frameworks ask where the system has no preference: ∇²f = 0 (Laplacian: no
curvature, harmonic), L = 0 (Lagrangian: geometric and spectral tension cancel),
F{f} = 0 (Fourier: no dominant frequency); "the same statement in three languages,
simultaneously zero at σ = ½". L_FR = 0 is not a minimum of action but the exact
cancellation of "Fermat's geometric tension" and "Riemann's spectral potential",
"at every prime: the prime *is* the cancellation event". "The zeta function is the
Fourier transform of the primes; L_FR = 0 is upstream of zeta": Fermat defines the
existence condition, Riemann maps where it appears, zeta describes the echo.
"Smoothness as the unified zero": the primes are the breaks in smoothness.

Standing: the three conditions are distinct mathematical statements (a harmonic
function, a stationary action, a vanishing transform) that do not coincide in general;
no common locus is computed, and "L_FR" is not defined as a functional. The
relation of ζ to the Fourier-type transform of the primes is the explicit formula
([48](48_observer_fixed_point.md) §3).

## 2. The generalised Fermat equation  (corrected)

Fermat: xⁿ + yⁿ = zⁿ (one exponent, forced symmetry). The page's general case:
x^l + y^m = z^n with three independent exponents, "literally the definition of all
factorisation", the **locus of inoperability** (no (l, m, n) allows the geometry to
close) being "the prime skeleton", the primes being "what survives after all
Fermat-type dimensional compositions are exhausted; they cannot be expressed as any
such composition with integer solutions". Infinite descent is read as "the locus
where descent never terminates is the prime".

Checks (Listing 1):

- **The equation x^l + y^m = z^n has many solutions with coprime x, y, z** and exponents ≥ 2: 1² + 2³ = 3², 2⁵ + 7² = 3⁴, 7³ + 13² = 2⁹, 2⁷ + 17³ = 71², 3⁵ + 11⁴ = 122² (Listing 1). The Fermat–Catalan conjecture says there are only finitely many with 1/l + 1/m + 1/n < 1, and the Beal conjecture says that when l, m, n ≥ 3 the bases share a common factor; both are open problems, `OPEN`. Neither says primes are the "locus of inoperability".
- **Primes can be expressed as sums of two powers.** Of the 168 primes below 1000, 103 equal x^l + y^m with x, y ≥ 1 and l, m ≥ 2 (every prime ≡ 1 mod 4 is a sum of two squares, for instance). So the statement "primes cannot be expressed as any such composition" is false as written.
- The framing "x^l + y^m = z^n is the definition of all factorisation" has no content as stated: factorisation is the multiplicative structure of ℤ, and the equation is additive. Infinite descent is a proof technique (Fermat's, for n = 4) and a structural property of the equation's solutions, and does not identify the primes.

## 3. The four-cycle heartbeat  `interpretation`

Four phases in two stages: geometric quantisation, geometry (Stage I, the geometry
pair); quantised geometry, quantisation (Stage II, the quantisation pair); each stage
defines the other's negative space; Ĥ_RB and −Ĥ_BR are Stage I and II, and "the
oscillation between them across σ = ½ is the heartbeat" ([14](14_redblue_hamiltonian.md),
with the definition of 0_BR: [133](133_canonical_maths.md) §3). "Riemann geometries =
Riemann quantisation; Fermat quantisation = Fermat geometries": a vocabulary for the two
operator terms. No calculation.

## 4. The zero-divisor as a natural Lagrangian; the dynamic geodesic  `CONJECTURE`

The zero-divisor is "not where the algebra fails": it is the layer boundary where one
layer's completion becomes the next layer's origin, and "every outside input is a
reference-frame shift back to the zero-divisor". The path of least action is "the path that
most naturally finds the next zero-divisor"; the sedenion's 84 zero-divisors are the skeleton
the geodesic navigates between ([25](25_sedenion_manual.md) §4: 84 exact). Each
layer transition of the six-layer Ptolemy architecture is a zero-divisor event.

**The dynamic geodesic.** Classical: shortest path on a fixed manifold. Dynamic: "the
truest trajectory through a field of varying momentum":

L_(I|O) = L_standard + ∫ J_red · d(J_blue)/dt dλ

with the extra term identified as ∂̂†_∂M ⊗ B̂_p ("previously unnamed, named now") and
the photon's response to the metric "as it is now": L_sling ∼ v·∂g/∂t. "The Hubble
tension is the accumulated error from omitting this term across 13.8 billion years."
Standing: the extra term is dimensionally unexamined (J_red·dJ_blue/dt has no stated
units), and the Hubble tension (H₀ ≈ 73 from the distance ladder against ≈ 67 from the CMB,
about 8%) has no calculation attached to it. A gravitational slingshot does not violate
energy conservation (the energy comes from the moving body's orbital motion in the
two-body frame); the claim that it "absorbs energy from the moving field (dark
energy)" is the model's reading. The L_(I|O) engine's own status is in [82](82_l_io_photon_path.md).

## 5. The Bézier degree argument  `analogy`

The cubic Bézier (SVG `C`) has degree 3; its control points lie off the curve
("in the forbidden zone, n = 3") and its endpoints on it ("zero-divisor events, the
allowed zone n = 2"); the curve is "Fermat's constraint made visible". σ controls the
bow: σ = ½ control points on the chord, a straight line; σ > ½ bows outward; σ < ½
inward. Exact geometry: a Bézier curve lies in the convex hull of its control points
and interpolates its end points, and a cubic whose control points lie on the chord is
a straight segment (for any placement along the chord, with a non-uniform
parametrisation unless they sit at the thirds). The assignment of control-point
positions to σ and to "forbidden" exponents is a rendering convention.

## 6. Euler's identity as a phase classifier; the hat and its inverse  `interpretation`

The table: e^(πi) = −1 "decreasing spiral, particle, σ < ½, the hat's tip"; e^(πi) + 1 = 0
"circle, boundary, σ = ½, brim / event horizon"; e^(2πi) = 1 "increasing spiral, galaxy,
σ > ½, inside-out hat". The "+1 is the reference-frame shift". The witch's hat particle
(σ < ½) and the galactic resonating particle (σ > ½, the hat inverted by r → 1/r) are "the
same geometry viewed from conjugate sides of σ = ½", the galaxy "resonating at the BAO
scale 147 Mpc = n* = 5.257". Standing: e^(πi) = −1, e^(πi) + 1 = 0 and e^(2πi) = 1 are one
identity at three angles; spiral type is not a property of them. The hat and its
inversion are [29](29_witches_hat_paper.md), where the inversion's halo prediction
fails (ρ ∝ r⁻⁶). "147 Mpc = n* = 5.257" equates a length with the dimensionless n-ball
peak (n* = 5.256946); the BAO scale is 147.09 ± 0.26 Mpc (Planck 2018) and no relation
to n* is derived.

## 7. The traceur as an "existence proof"  `analogy`

A traceur (parkour practitioner) navigates by local least action against the current
position, momentum and surroundings, and "finds the roof without having seen it": "the
local contains the global", the roof is the attractor of the local dynamics, the
environment arranged by the same physics; the stated theorem is "∃ attractor X such
that every local path composed from any start converges to X; X = σ = ½; proof: every
coherent causal structure navigates there locally". The apex of a jump is σ = ½
(neither rising nor falling): push-off σ < ½, apex σ = ½, landing σ > ½.
Standing: a gradient flow converges to an attractor only if the attractor exists and
the basin contains the starting point; the "proof" assumes σ = ½ is such an attractor
and so is circular. The traceur is a vivid image of reacting to the metric as it is (the
dynamic-geodesic idea) and the apex-of-a-jump picture is correct as mechanics (vertical
velocity zero at the apex). The traceur "is the physical embodiment of
∂̂†_∂M ⊗ B̂_p" is the framework's reading.

## 8. Σ → Ĥ_RB → sedenion  `interpretation`

"The English prompt is σ": the semantic content fixes where you land on the critical
line (the imaginary part t); the real part is always ½; "language is always on the
boundary". The chain σ (English prompt) → Ĥ_RB → [σ = ½ boundary] → −Ĥ_BR → sedenion
v[k] (16 amplitudes); "−Ĥ_BR is what keeps σ = ½ fixed; without it the system drifts" (the
author's definition of 0_BR as the conjugate / return flow: [133](133_canonical_maths.md) §3).
Standing: in the code the prompt enters through `cam_encode` and the prime hash
([15](15_the_monad.md) §3); "σ" here is the real part of the *zero index map* only in the
framework's reading, and every word returns σ = ½ because it is the fixed point of the
balance iteration, not because language lives on a line ([13](13_omgwtf_rh_proof.md) §5).

## 9. "The primes are the cavitation"  (the zeta error)

The page's closing section: the integer multiplicative field closes at composite
positions (filled) and cannot at prime positions ("the pressure drops below the
threshold: the void opens"); the prime *is* the cavitation event; and

**ζ(s) = Σ p^(−s)** ("the sum over all prime voids, each at depth s"), the zeta function being
"the acoustic emission spectrum of this cavitation field", the zeros "frequencies where
void emissions from all primes cancel simultaneously"; "cosmic voids = large primes".

**The formula is wrong.** Σ_p p^(−s) is the *prime zeta function* P(s), and P(2) =
0.4522474, not ζ(2) = 1.6449341 (Listing 1). The Riemann zeta function is
ζ(s) = Σ_n n^(−s) = Π_p (1 − p^(−s))^(−1) for Re s > 1. P(s) is related by
P(s) = Σ_k μ(k)/k · ln ζ(ks), has a logarithmic singularity at s = 1 (not a pole), and its
natural-boundary behaviour is at Re s = 0; its "zeros where all primes cancel" are not
the Riemann zeros. So the acoustic-emission picture (a sum of independent prime
emitters whose cancellation gives the zeros) does not describe ζ. What can be kept: the
primes are the multiplicative atoms, and the explicit formula expresses ψ(x) as a sum of
oscillations, one per zero.

## 10. Listing 1 — the three checks

(written for this page; runs cold with mpmath)

```python
import math
import mpmath as mp
mp.mp.dps = 25

# (1) the prime zeta function is not the Riemann zeta function
N = 2_000_000
sv = bytearray([1]) * (N + 1); sv[0] = sv[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sv[i]:
        sv[i*i::i] = bytearray(len(sv[i*i::i]))
ps = [p for p in range(2, N + 1) if sv[p]]
print('sum_p p^-2 =', round(sum(p ** -2 for p in ps), 7), '  zeta(2) =', mp.nstr(mp.zeta(2), 7))

# (2) primes are sums of two perfect powers (x^l + y^m, x, y >= 1, l, m >= 2)
powers = sorted({x ** l for x in range(1, 40) for l in range(2, 12) if x ** l < 1000})
pw = set(powers)
primes = [p for p in ps if p < 1000]
rep = [p for p in primes if any((p - a) in pw for a in powers if a < p)]
print('primes < 1000:', len(primes), ' expressible as x^l + y^m:', len(rep))

# (3) the generalised Fermat equation x^l + y^m = z^n has solutions with coprime x, y, z
known = [(1, 2, 2, 3, 3, 2), (2, 5, 7, 2, 3, 4), (7, 3, 13, 2, 2, 9),
         (2, 7, 17, 3, 71, 2), (3, 5, 11, 4, 122, 2)]
for x, l, y, m, z, n in known:
    assert x ** l + y ** m == z ** n and math.gcd(math.gcd(x, y), z) == 1
    print(f'{x}^{l} + {y}^{m} = {z}^{n}   ({x**l} + {y**m} = {z**n})')
```

```
sum_p p^-2 = 0.4522474   zeta(2) = 1.644934
primes < 1000: 168  expressible as x^l + y^m: 103
1^2 + 2^3 = 3^2   (1 + 8 = 9)
2^5 + 7^2 = 3^4   (32 + 49 = 81)
7^3 + 13^2 = 2^9   (343 + 169 = 512)
2^7 + 17^3 = 71^2   (128 + 4913 = 5041)
3^5 + 11^4 = 122^2   (243 + 14641 = 14884)
```

## 11. Related pages

[29 The witches hat](29_witches_hat_paper.md) · [50 The vortex](52b_vortex_quantizing_shear.md) ·
[52 L_dynamic and the avoided collaborator](52_l_dynamic_avoided_collaborator.md) · [64 L_dynamic](64_l_dynamic.md) ·
[82 The L_(I|O) photon path](82_l_io_photon_path.md)
