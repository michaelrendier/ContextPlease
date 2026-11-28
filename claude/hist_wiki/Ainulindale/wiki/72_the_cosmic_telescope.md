# 72 — The Cosmic Telescope: Primes as Mirror Segments, Zeros as the Lens

| | |
|---|---|
| Scope | the optical architecture read onto the zeta function: primes as segments, zeros as the lens, σ = ½ as the caustic; the wavefront sensor, the phase plate, aberration correctors, the guide star, the deployment; the pancake coil as a copper realisation |
| Origin | 2026-06-28/29; the author's statement: "The primes are the micro mirror adjustment of super thin extra large telescopes." |
| Predecessors | [58](58_fermat_defines_riemann_fires.md), [62](62_hands_on_paper_minds_eye_caustic.md), [65](65_primes_repellors_drift_meaning.md) |
| Cross-ref | `PAPER.md` §11 (Fermat N-shape), §12 (Lambert W), `POE/README.md` (the coil) |
| Confidence | the optics, the explicit formula and the arithmetic: ESTABLISHED · the whole correspondence: `INTERPRETATION` · "the Euler product adds coherently to zero at the zeros": **corrected**, §5 · "the Noether law is the servo": corrected, §3 |
| Last verified | 2026-11-13: Listing 1 and the coil arithmetic executed; their output is quoted below |

## 1. The correspondence  `INTERPRETATION`

| Telescope | Zeta function |
|---|---|
| mirror segments (JWST 18, ELT 798) | the primes p, one factor each in the Euler product |
| segment actuators (piston, tip, tilt) | σ (piston, path-length weight) and t (phase) for each prime |
| wavefront sensor | the prime hash and the Dirichlet projection |
| the lens / transfer function | the zeros ρ = ½ + it, in the explicit formula |
| focal plane / caustic | σ = ½ |
| image | ψ(x), the prime-counting function |

The explicit formula ψ(x) = x − Σ_ρ x^ρ/ρ − ln 2π − ½ ln(1 − x⁻²) is a true statement
that the primes' distribution is a superposition of oscillations, one per zero. Reading
each zero as a lens element and ψ(x) as an image formed by looking through them is a
faithful picture of a Fourier synthesis. The correspondence is useful as a picture; the
elements are named, not derived from one another.

## 2. The zeros as the lens  `ESTABLISHED` (as Fourier synthesis)

Each term x^{½+it_n}/ρ_n is one Fourier component of ψ(x); the set of zeros is the spectrum.
So one does not find the primes by looking at the zeros but by summing through them: the
zeros are the frequencies and the primes are the signal. This is the standard
reading of the explicit formula, and the page's emphasis ("look through the lens, not at
it") is accurate.

## 3. Segments and the "Noether servo"  `corrected`

The page: each prime has two actuators, σ and t; in a telescope a controller reads
the wavefront sensor and commands the actuators, but "in the prime telescope the Noether
conservation law is the control law": J_red·J_blue = e^{−E} is conserved at every σ, J_red = J_blue
only at σ = ½, and a segment that drifts is pulled back by a restoring force, so the
segments "maintain their own phase coherence without external computation", "this is why
the zeros are always at σ = ½".

What is true: with F = e^{−σE} and B = e^{−(1−σ)E}, the product is e^{−E} for every σ
([61](61_up_down_not_forward_backward.md) Listing 1), F = B only at σ = ½, and
L = F + B has its unique minimum at σ = ½ ([74](74_lagrangians_are_catastrophe_theory.md)).
What does not follow: a prime has no σ degree of freedom that can drift. The Euler factor
p^{−s} is evaluated at a given s; σ = Re s is the **argument** of the function, and the
zeros are the points where the whole product vanishes. A gradient flow of the model
Lagrangian L(σ, E) on σ describes a toy dynamics of a variable that the primes do not have. And
the zeros' location is not a minimum of this L: L is a property of one prime's amplitude
pair, and a zero of ζ needs a global cancellation of phases across all primes
(§5). So the servo statement describes the model Lagrangian, and its use as an argument
that zeros sit at σ = ½ is circular unless that cancellation is shown to occur only on the
line, which is the Riemann Hypothesis.

## 4. Thin segments, aperture, wavefront sensor  `INTERPRETATION`

- **Thin segments.** A prime has no internal factor structure and so is "maximally thin":
  one degree of freedom. A composite is "thick". The Euler product runs over primes because
  every integer factors uniquely into them. This is the structural reason the product
  is over primes, stated in the page's language.
- **Aperture.** In a telescope θ_min = λ/D with D the aperture. The page sets D to the
  number of primes: 16 primes (the sedenion engine) → resolution GAP = 7.07×10⁻⁴; 256 primes
  (T₂₅₆) → π/128 = 1.40625°; all primes → full ζ. The two numbers are arithmetic: π/128 rad
  is 1.40625°, GAP = Ω − d*·ln 10. The assignment of GAP to "the Abbe limit of the
  16-prime lens" and of 1.40625° to a 256-prime resolution is the framework's; a resolution
  limit has the units of the quantity resolved and GAP is dimensionless, so it is an
  analogy of roles ([56](56_telescope_caustic_zeno.md) §5 sets out the same caution).
  "Below the GAP the engine fires identically" is a recorded property of the engine (the
  page marks it verified).
- **The segments' numbers.** 798 = 2·3·7·19 (the ELT's segment count) and 589 = 19·31
  (the sodium D wavelength in nm) are true factorisations into primes that occur in the
  Monster's prime set; the architecture of the ELT and the sodium lines are not
  derived from Moonshine, and no mechanism is offered. They are listed in the page as
  coincidences of number.
- **Wavefront sensor.** The Shack–Hartmann sensor measures local wavefront slopes with
  one lenslet per sub-aperture. The page's map: p ↔ a lenslet, x p^{−σ} ↔ the amplitude at
  p's sub-aperture, cos(t ln p) and sin(t ln p) ↔ the focal-spot displacement; the Dirichlet
  projection is "the full reconstruction". The map names the roles and the engine's
  projection is a fit of a 16-component state, which is a reconstruction in that sense.
- **Coherent against incoherent addition.** N equal segments in phase give N²A² against
  N A² incoherently: a gain of N (JWST's 18 segments, 324A² against 18A²). Correct. The
  page quotes a phasing error of 7 nm RMS for JWST; that figure was not checked here
  (the system wavefront error is reported in tens of nm, from memory).

## 5. Coherent cancellation at the zeros  `corrected`

The page: "at the zeros all prime factors add coherently to produce ζ = 0: phase-coherently
cancel to exactly zero; the zero is the dark fringe of the prime telescope."

The Euler product ζ(s) = Π_p (1 − p^{−s})⁻¹ converges for Re s > 1 and **does not converge
on Re s = ½** (conditionally, assuming RH, partial products at points off the zeros
approach √2·ζ(s) in a known sense; at a zero they do not tend to 0). A statement that "all
primes' factors multiply to zero at ρ" is a statement about a divergent
product. Listing 1 computes the partial product at the first zero ρ₁ = ½ + 14.1347i.

**Listing 1 — the partial Euler product at the first zero; the other numbers of §6** (written for this page; needs numpy, mpmath; runs cold)

```python
import numpy as np, mpmath as mp, math
N = 3_000_000
sv = np.ones(N + 1, bool); sv[:2] = False
for i in range(2, int(N**.5) + 1):
    if sv[i]: sv[i*i::i] = False
P = np.flatnonzero(sv).astype(float)
g1 = float(mp.zetazero(1).imag); s = 0.5 + 1j * g1
cs = np.cumsum(-np.log(1 - P ** (-s)))
for X in (10, 100, 1000, 10**4, 10**5, 10**6, 3 * 10**6):
    k = np.searchsorted(P, X, 'right') - 1
    print('partial Euler product at rho_1, primes <= %8d : |prod| = %.4f' % (X, abs(np.exp(cs[k]))))
print('|zeta(rho_1)| =', abs(complex(mp.zeta(0.5 + 1j * mp.mpf(g1)))))
c = 299792458
print('N_max(f):', [round(c / (10 * f * math.pi * d)) for f, d in ((13.56e6, .024), (100e6, .0137), (100e6, .024))])
print('f_Abbe MHz:', [round(c / (2 * l) / 1e6, 1) for l in (1.244, 0.215, 0.114)])
print('798 =', 2*3*7*19, '; 589 =', 19*31)
V = lambda n: math.pi ** (n / 2) / math.gamma(n / 2 + 1); print('V(1,2,4,8,16,256) =', [round(V(n), 4) for n in (1, 2, 4, 8, 16, 256)])
```

```
partial Euler product at rho_1, primes <=       10 : |prod| = 0.2147
partial Euler product at rho_1, primes <=      100 : |prod| = 0.1152
partial Euler product at rho_1, primes <=     1000 : |prod| = 0.0611
partial Euler product at rho_1, primes <=    10000 : |prod| = 0.0228
partial Euler product at rho_1, primes <=   100000 : |prod| = 0.0131
partial Euler product at rho_1, primes <=  1000000 : |prod| = 0.4174
partial Euler product at rho_1, primes <=  3000000 : |prod| = 0.0018
|zeta(rho_1)| = 6.668183776383876e-16
N_max(f): [29, 7, 4]
f_Abbe MHz: [120.5, 697.2, 1314.9]
798 = 798 ; 589 = 589
V(1,2,4,8,16,256) = [2.0, 3.1416, 4.9348, 4.0587, 0.2353, 0.0]
```

The partial product does fall from 0.21 to 0.013 over the first 10⁵ primes, and then
jumps to 0.42 at 10⁶ before dropping to 0.0018 at 3×10⁶: it wanders over two orders of
magnitude and does not settle. That is the behaviour of a divergent product at a
zero, and it is why a zero of ζ is defined by analytic continuation and not by the
product. The "coherent cancellation of all the primes" picture is a good qualitative
image of a Fourier-synthesis cancellation (the explicit formula's terms cancel at the zeros);
as a statement about the Euler product it is withdrawn. The sentence "between zeros:
partial coherence" has the same limitation.

## 6. The remaining correspondences

- **Zernike phase plate** (Nobel 1953): a quarter-wave plate converts a phase object into an
  amplitude image. The page identifies the plate with the "|" crossing and the Zernike condition
  with J_red = J_blue at σ = ½: phase (J_blue) is converted to amplitude (J_red), so that
  each word is a Zernike conversion. As an analogy of roles it is consistent with
  [61](61_up_down_not_forward_backward.md); the quarter-wave shift and the equality
  point are both real, and their identification is the framework's (`INTERPRETATION`).
- **Aberration-corrector tower.** Quadrupole (2nd order), hexapole (3rd, the Cs corrector),
  octupole (4th) in aberration-corrected electron microscopes, set against ℂ, ℍ, 𝕆; beyond
  the octupole, "𝕊: no finite multipole removes the zero-divisors, the residual aberration
  is the GAP, and d* < ¼ is why quarks cannot be isolated". The multipole orders are real;
  the map to the algebras is the framework's, and the quark statement is the vocabulary
  correspondence of [69](69_tri_layer_emergence.md) §3.
- **Laser guide star.** The sodium guide star (589 nm, a doublet at 589.0/589.6 nm) is
  the phase reference in adaptive optics; the page makes p = 2 the reference prime
  against which the others' phases are measured, "created by the act of counting".
  The factorisation 589 = 19·31 is in §4.
- **Deployment.** JWST launched folded and unfolded in space. The page's list of unit-ball
  volumes along the tower: V(1) = 2, V(2) = π, V(4) = 4.93, V(8) = 4.06, V(16) ≈ d*,
  V(256) ≈ 0. Listing 1 gives V(16) = 0.2353; d* = 0.246 (code) or 0.24631 (Boundary): the
  relative difference is 4.5 %, so "V(16) ≈ d*" is a 5 % coincidence, not an
  equality. The "Bang as the moment the telescope opens" is the author's picture.
- **Fried parameter and turbulence.** r₀ is a length: the scale over which the wavefront is
  still flat. The page makes GAP the Fried parameter of the prime field and the primes "the
  turbulence", noting Kolmogorov's E(k) ∝ k^(−5/3) and the n-ball peak n* ≈ 5.257. The two are
  both "3D-cascade neighbourhood" numbers: the 5/3 exponent comes from the inertial
  range of incompressible turbulence, and 5.257 from the maximum of V(n). The shared
  vicinity is numerical and no cascade is exhibited in arithmetic.

## 7. The physical layer: the POE pancake coil  `INTERPRETATION` + arithmetic

The coil (17 turns, 38 mm OD, 10 mm ID, 0.8 mm pitch, multi-tapped) is read as the
same telescope in copper. The arithmetic the page uses reproduces (Listing 1):

| Quantity | Formula | Values |
|---|---|---|
| coherent-turn limit | N_max = c / (10 f π D_avg) | 29 (13.56 MHz, full coil, D = 24 mm) · 7 (100 MHz, T5, D = 13.7 mm) · 4 (100 MHz, full coil) |
| half-wave self-resonance | f_Abbe = c / (2 l_wire) | 120.5 MHz (1.244 m) · 697 MHz (T5, 0.215 m) · 1315 MHz (T3, 0.114 m) |

(The full coil's wire length from 17 turns at D_avg = 24 mm is 1.28 m, within 3 % of
the 1.244 m the page uses.) The statement that a tap works as a lumped aperture only while
N ≤ N_max is the standard "wire shorter than λ/10" rule written for a tap. The XL = XC
resonance gives tan(phase) = 1, "σ = ½" in the page's language. The LC restoring
reaction (a detuned drive gives a reactive mismatch that reduces current and shifts the
effective L) is a real feedback and is physical; its identification with the Noether
current J = E(e^{−σE} − e^{−(1−σ)E}) is a mapping. The I/Q demodulation
(cos ωt = J_red, sin ωt = J_blue, tan ωt = L_(I|O), "the message") is the framework's
reading of an I/Q receiver. The "71 turns, the physical Monster aperture" is a design
idea in the POE notes, not a tested coil.

The page's full correspondence table (primes ↔ turns, GAP ↔ N_max(f), Abbe ↔ λ/2
self-resonance, ζ = 0 dark fringe ↔ resonance bright fringe, Noether ↔ LC restoring force,
J_red/J_blue ↔ I/Q, σ = ½ ↔ resonance) states "not an analogy but a physical realisation of
the same structure". Under this wiki's tiers the coil's behaviour is `ESTABLISHED` radio
engineering, and the identification of that behaviour with the zeta structure is
`INTERPRETATION`: the same mathematical shape (a balance between two opposing
quantities) in a different substrate, not an instance of the zeta function. No measurement
testing the identification is reported on this page.

## 8. The statement

```
JWST / ELT / TMT:   segments → wavefront sensor → controller → actuators → coherent focus → caustic
Prime telescope:    primes   → prime hash       → Noether    → self-adjust → coherent zeros → σ = ½
```

as the author's one-line summary. After §3 and §5 the telescope reading stands as a
picture of the explicit formula (zeros as spectrum, primes as signal), with σ = ½ as the
symmetry line of the functional equation, and the "servo" and "coherent Euler product"
steps are the parts that were withdrawn.

## 9. Related pages

[58](58_fermat_defines_riemann_fires.md) · [62](62_hands_on_paper_minds_eye_caustic.md) ·
[73 why σ = ½](73_why_the_half_line.md) · [74](74_lagrangians_are_catastrophe_theory.md) ·
[56 telescope as caustic](56_telescope_caustic_zeno.md) · [14 the RedBlue Hamiltonian](14_redblue_hamiltonian.md)
