# 73 — Why σ = ½: Six Derivations, What Each Shows, and the Dependency Order

| | |
|---|---|
| Scope | the six derivations of σ = ½ that the framework collects (symmetry, Lagrangian minimum, N-shape/AM-GM, the spiral, LC resonance, the factorisation tree); what each establishes; the 2026-08-25 dependency analysis; the Abrikosov-lattice corollary |
| Origin | 2026-06-29 cascade capture; addendum 2026-08-25 (§9, kept) |
| Predecessors | [72](72_the_cosmic_telescope.md), [58](58_fermat_defines_riemann_fires.md), [52b](52b_vortex_quantizing_shear.md), [52c](52c_j2_involution_riemann_fermat.md) |
| Code | `engines/noether_derivation.py` (archived at `RiemannHypothesisProof/archive/2026-11-03_pre-rewrite/engines/`), `FermatMonster/engine/fermat_monster_engine.py` |
| Confidence | each derivation's own algebra: ESTABLISHED · the page's conclusion "σ = ½ is not a conjecture": **withdrawn**: the derivations locate the symmetric point of the model, not the zeros · the Riemann Hypothesis: OPEN |
| Last verified | 2026-11-13: Listing 1 (zeta spiral facts) and the symbolic checks of [74](74_lagrangians_are_catastrophe_theory.md) executed; their output is quoted below |

## 1. The question

Why σ = ½? The statement of the Riemann Hypothesis is that every non-trivial zero of ζ lies on
Re s = ½. The page's question is why ½ is the algebraically, variationally and physically
natural address, and its answer is "six engines, one answer". Each of the six is
assessed below for what it proves.

## 2. Engine 1: the symmetry fixed point  `ESTABLISHED`, conclusion corrected

The functional equation ξ(s) = ξ(1 − s) makes the zero set symmetric under s → 1 − s and
under complex conjugation, so under s → 1 − s̄ as well. The line fixed by s → 1 − s̄ is
σ = ½: σ + it = 1 − σ + it gives σ = ½ for every t. A zero ρ off the line forces its
mirror partners 1 − ρ̄, 1 − ρ and ρ̄, a quadruple; a zero on the line is its own mirror
under that map.

What this shows: σ = ½ is the symmetry axis of the zero set. What it does not show:
that every zero is on the axis. The symmetry is satisfied equally by a zero set that
contains quadruples off the line; that possibility is what the open problem is about.
The page's wording "the symmetry argument says σ = ½ is the only line that is
self-consistent" is correct as "the only line fixed by the involution"; it does not
exclude off-line pairs.

## 3. Engine 2: the Lagrangian minimum  `ESTABLISHED` (algebra), scope stated

L(σ, E) = e^{−σE} + e^{−(1−σ)E} with E = ln p. ∂L/∂σ = 0 gives σ = ½ (E ≠ 0), and
∂²L/∂σ² = E²L > 0, so the critical point is the unique global minimum
([74](74_lagrangians_are_catastrophe_theory.md) Listing 1 gives the symbolic derivation).
The current J = −∂L/∂σ = E(e^{−σE} − e^{−(1−σ)E}) is positive for σ < ½ and negative
for σ > ½, so the gradient flow σ̇ = J drives σ to ½. All correct.

Scope: this is a statement about the amplitude pair of **one prime** at a
hypothetical σ. It is not an equation whose solutions are zeros of ζ, and σ is not a
dynamical variable of the primes ([72](72_the_cosmic_telescope.md) §3). So it supports "½ is the
balance point of the model" and not "the zeros are at ½".

## 4. Engine 3: the N-shape and AM-GM  `ESTABLISHED` (algebra)

F = e^{−σE}, B = e^{−(1−σ)E}: FB = e^{−E} for all σ ([61](61_up_down_not_forward_backward.md)
Listing 1), and F = B ⇔ σ = ½. By AM-GM, F + B ≥ 2√(FB) = 2e^{−E/2} with equality
exactly at F = B. This is the same fact as Engine 2 (§9 below): a minimum of the sum at a
fixed product. The page's further claims, that a crossing off σ = ½ "would violate the
Wiles–Noether conservation law" and that off the line "the dominant current generates a
non-zero winding number which, at dimension ≥ 16, hits a zero-divisor and is annihilated",
are statements about the FermatMonster model; the winding-number argument is not
derived in this wiki and is `CONJECTURE`. The statement "primes are leaves, ZD-free" is the
framework's reading of irreducibility.

## 5. Engine 4: the spiral  `ESTABLISHED` facts, claims corrected

**Listing 1 — facts about ζ(½ + it)** (written for this page; needs numpy, mpmath; runs cold)

```python
import numpy as np, mpmath as mp, math
mp.mp.dps = 20
ts = np.linspace(10, 60, 2001)
z = np.array([complex(mp.zeta(mp.mpc(0.5, t))) for t in ts])
th = np.array([float(mp.siegeltheta(t)) for t in ts]); Z = np.array([float(mp.siegelz(t)) for t in ts])
print('zeta(1/2+it) = exp(-i theta) Z(t), Z real: max|Im(zeta e^{i theta})| = %.1e ; max|Z - Re(zeta e^{i theta})| = %.1e'
      % (np.abs((z * np.exp(1j * th)).imag).max(), np.abs(Z - (z * np.exp(1j * th)).real).max()))
print('d theta/dt at t=50: %.4f ; 0.5 ln(t/2pi) = %.4f' % (np.gradient(th, ts)[1600], 0.5 * math.log(ts[1600] / (2 * math.pi))))
print('sign changes of Z on [10,60]:', int(sum(Z[k] * Z[k + 1] < 0 for k in range(len(ts) - 1))))
zs = [float(mp.zetazero(k).imag) for k in range(1, 31)]
print('theta(gamma_n)/pi, n=1..8:', [round(float(mp.siegeltheta(t)) / math.pi, 3) for t in zs[:8]])
print('arg zeta at t=20,30,40,50:', [round(float(np.angle(complex(mp.zeta(mp.mpc(.5, t))))), 3) for t in (20, 30, 40, 50)])
mx = max(abs(complex(mp.zeta(0.5 + 1j * t))) for t in np.linspace(14, 2000, 4000)); print('max |zeta(1/2+it)|, 4000 samples in [14,2000]: %.3f' % mx)
print('mean spacing, zeros 21-30: %.3f ; 2pi/ln(t/2pi) at gamma_26: %.3f' % (np.mean(np.diff(zs[20:])), 2 * math.pi / math.log(zs[25] / (2 * math.pi))))
```

```
zeta(1/2+it) = exp(-i theta) Z(t), Z real: max|Im(zeta e^{i theta})| = 7.8e-15 ; max|Z - Re(zeta e^{i theta})| = 4.4e-16
d theta/dt at t=50: 1.0371 ; 0.5 ln(t/2pi) = 1.0371
sign changes of Z on [10,60]: 13
theta(gamma_n)/pi, n=1..8: [-0.55, 0.57, 1.394, 2.671, 3.317, 4.594, 5.565, 6.294]
arg zeta at t=20,30,40,50: [-1.187, -1.775, -0.92, 1.813]
max |zeta(1/2+it)|, 4000 samples in [14,2000]: 11.238
mean spacing, zeros 21-30: 2.442 ; 2pi/ln(t/2pi) at gamma_26: 2.336
```

What holds:

- ζ(½ + it) = e^{−iθ(t)}·Z(t) with Z real (the Riemann–Siegel form; residuals at rounding).
  The phase rotates at dθ/dt ≈ ½ ln(t/2π) (1.0371 at t = 50), increasing with t, so the
  winding tightens. The "½" in (t/2) ln(t/2π) comes from Γ(s/2) at s = ½ + it, as the page
  says. The Stirling form θ(t) ≈ (t/2) ln(t/2π) − t/2 − π/8 is the right asymptotic.
- The zeros are the sign changes of Z (13 on [10, 60]): the curve passes through the
  origin and re-emerges turned by π.
- N(T) ≈ (T/2π) ln(T/2πe) + 7/8, and the mean spacing 2π/ln(t/2π): 2.44 measured
  against 2.34 from the formula for zeros 21–30 (a 4 % difference for the first few tens).

What is corrected:

- **"A logarithmic spiral."** The path of ζ(½ + it) is a quasi-periodic curve that loops
  through the origin at every zero; it is not a logarithmic spiral (a curve of constant
  angle to the radius). The winding rate increasing as ½ ln(t/2π) is the accurate
  statement.
- **"Bounded, conditionally (Lindelöf)."** The Lindelöf hypothesis says |ζ(½ + it)| ≪ t^ε.
  That is a growth bound and not boundedness; ζ on the critical line is unbounded (it
  reaches 11.2 in the sampled range and grows slowly). The page's "bounded" is withdrawn.
- **"θ(t_n) ≈ nπ, so e^{iθ} = (−Δx)^n."** The values are θ(γ_n)/π = −0.55, 0.57, 1.39, 2.67, 3.32,
  4.59, 5.57, 6.29: close to n − 1 plus the fluctuation S(T) of the zero count
  (N(T) = θ(T)/π + 1 + S(T)), not to n. The relation e^{πi} = −1 is Euler's identity; the
  framework's reading e^{πi} = −Δx adds a displacement and belongs to
  [52b](52b_vortex_quantizing_shear.md) as an operator-form statement, not to an
  identity of ζ.
- **"L_(I|O) = Q/I = e^{(2σ−1)E}-type, equal to 1 at σ = ½, phase π/4."** The page defines
  I = Re ζ and Q = Im ζ and then evaluates Q/I as the ratio of the two exponentials F and B.
  These are different objects. The ratio of the exponential amplitudes is exactly 1 at
  σ = ½ (so arctan = π/4 for them); the phase of ζ(½ + it) itself is −θ(t) + (0 or π)
  and varies (−1.19, −1.78, −0.92, 1.81 rad at t = 20, 30, 40, 50), not the constant π/4.
  The "π/4 = half the quadrature offset" statement is about the F/B ratio.
- The conventions: here J_blue = B = e^{−(1−σ)E} and J_red = F = e^{−σE}, the reverse of
  [64](64_l_dynamic.md) (which has J_red = B). See the convention table in
  [61](61_up_down_not_forward_backward.md) §1 and the ledger row X-11.

## 6. The Abrikosov lattice and the zero spacing  `corollary`, status stated

N(T) ≈ (T/2π) ln(T/2πe) and the mean spacing 2π/ln(t/2π) are correct (Listing 1; the
N(T) check against the 3,066 zeros is in [50](50_causality_upper_limit.md)). The zero
set therefore has logarithmic density, echoing π(x) ~ x/ln x; the explicit formula
reconstructs the primes from the zeros and the zeros from the primes, which is the
page's "Fourier dual" statement.

The N-shape theorem (Engine 3) is said to fix **where** (σ = ½) and the logarithmic
lattice **when** (the positions), so that together "the complete zero set is determined".
The lattice gives the *mean* density only; the individual positions are not determined by
2π/ln t (they have GUE-type fluctuations and the actual γ_n are computed numerically).
The "where" is the Riemann Hypothesis. The identification with Abrikosov's vortex lattice
(Nobel 2003) is developed, with its limits, in [75](75_abrikosov_lattice.md).

## 7. Engine 5: the LC resonance  `ESTABLISHED` radio engineering

XL = XC gives tan(phase) = 1, sin = cos, which the page calls σ = ½, and the half-wave
self-resonance l_wire = λ/2 as the "electromagnetic σ = ½". These are real
equalities in the coil ([72](72_the_cosmic_telescope.md) §7). They show that a balance
between two opposing quantities occurs there. They are not a derivation of anything about
ζ; §9 places Engine 5 accordingly.

## 8. Engine 6: the leaves  `ESTABLISHED`

The integers form a tree under prime factorisation; primes are the irreducibles, the
"leaves" with one edge from the root 1. A prime cannot be written as a product of integers
> 1, and the Euler product needs every prime (remove p and the product no longer equals
ζ(s)). Correct. The "stability argument" (the prime sits at J = 0, the attractor, and cannot be
displaced) repeats Engine 2 with the scope noted in §3.

## 9. Addendum 2026-08-25: the six are not six emergences  `kept`

The author's observation: "if it emerges in different places … those are all the same
emergent object emerging the same ½". Checked, with the following dependency order.

- **Engines 2 and 3 are one fact.** For a, b > 0 with ab = c fixed, a + b is minimal exactly when
  a = b. With a = e^{−σE}, b = e^{−(1−σ)E} the product e^{−E} is constant by construction, so
  Engine 2's calculus minimum and Engine 3's AM-GM closure are the same elementary fact once
  with a derivative and once with an inequality.
- **Dependency order.** (1) Engine 6, truly prior: purely discrete, no σ yet; it makes
  E = ln p well defined. (2) Engines 2 ≡ 3: the single emergence, forced when the Euler
  factor p^{−s} is paired with its reflection under a σ-independent conserved product.
  (3) Engine 1: the global upgrade of the same local symmetry σ ↔ 1 − σ for the whole ξ.
  (4) Engine 4: descriptive, shows ζ(½ + it) given σ = ½. (5) Engine 5: a physical
  instance of the same a = b balance.
- **The statement.** None of them defines a second ½: it "emerges exactly once, at the AM-GM
  equality of the Euler-factor amplitude with its own reflection", and everywhere else in the
  project it propagates through what is built on top.

This dependency analysis is accurate as an account of the six derivations. It also settles
what their combined force is: they are one local symmetry fact (σ ↔ 1 − σ with a
conserved product) in different clothes, plus a physical instance of it. That is why, after
§§2–8, the page's closing statements, "σ = ½ is not a conjecture; it is the only
algebraically consistent address for anything that cannot be divided further" and "the
engines prove that σ = ½ is the unique attractor", are withdrawn as statements about the
zeros, and kept as statements about the symmetric point of the amplitude model. The
open question the page itself names (whether the spectral argument excludes off-line zeros or
only attracts on-line ones) is the Riemann Hypothesis, and this page does not resolve it.

## 10. Related pages

[13 the RH proof path](13_omgwtf_rh_proof.md) · [50 vortex shear](52b_vortex_quantizing_shear.md) ·
[61 up/down](61_up_down_not_forward_backward.md) · [72](72_the_cosmic_telescope.md) ·
[74 Lagrangians and catastrophe theory](74_lagrangians_are_catastrophe_theory.md) · [75 the Abrikosov lattice](75_abrikosov_lattice.md)
