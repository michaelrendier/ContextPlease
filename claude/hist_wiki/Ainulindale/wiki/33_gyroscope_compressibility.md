# 33 — The gyroscope and the compressible / incompressible duality

| | |
|---|---|
| Status | **First capture (2026-06-03), raw insight burst; the proposed spine of the D-P paper. `INTERPRETATION` throughout, built on exact facts about ξ(s) that are stated and checked (§2)** |
| Predecessor | [32](32_superconducting_medium.md) |
| Code | none; Listing 1 checks the facts used |
| Last verified | 2026-11-13: Listing 1 executed (mpmath, 30 digits) |

## 1. The σ-face table and "which way is down"

The earlier page presents, as a derivation, the remark that "down is the
direction in which time runs slower" (the closing postulate of the Vsauce video
*Which Way Is Down?*, a built-against source) as the σ = 2 face:

| σ | Domain | Time behaviour (as read) |
|---|---|---|
| ½ | causality, quantum | reference rate: "the surface" |
| 1 | Yang–Mills | time begins to slow as mass assembles |
| 2 | gravity, the medium | slowest |
| ∞ | black-hole interior | time stops |

"Down" is increasing σ, "up" is decreasing σ, buoyancy points toward causality,
and the semantic buoyancy of words (neutral buoyancy = J_ambient) is the same
orientation device (heavy words sink toward σ = 2, neutral ones float at
σ = ½). `INTERPRETATION`: the physical statement that gravitational time
dilation grows toward a mass is general relativity (`ESTABLISHED`); the
mapping of the σ values to those regions is the framework's, and no calculation
connects σ to a time-dilation factor.

## 2. The exact facts used  (`ESTABLISHED`, checked)

With ξ(s) = ½ s(s−1) π^(−s/2) Γ(s/2) ζ(s):

1. **ξ(s) = ξ(1−s)** for all s, and ξ(s̄) = conj ξ(s). Hence if ρ is a zero, so are 1−ρ, ρ̄ and 1−ρ̄.
2. The map s ↦ 1−s is a **reflection** about Re(s) = ½ (an involution that reverses orientation), not a rotation.
3. Consequently a zero off the critical line comes in a **quadruple** {ρ, 1−ρ, ρ̄, 1−ρ̄}, symmetric about the line and about the real axis.

**Listing 1 — the functional equation and the conjugate symmetry** (written
for this page; runs cold with mpmath)

```python
import mpmath as mp
mp.mp.dps = 30
xi = lambda s: 0.5 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
for s in (mp.mpc(0.3, 2.1), mp.mpc(0.5, 14.134725), mp.mpc(0.8, -5)):
    print(mp.nstr(s, 8), mp.nstr(abs(xi(s) - xi(1 - s)), 3))
s = mp.mpc(0.3, 2.1)
print(mp.nstr(abs(xi(mp.conj(s)) - mp.conj(xi(s))), 3))
```

```
(0.3 + 2.1j) 1.02e-31
(0.5 + 14.1347j) 5.95e-40
(0.8 - 5.0j) 8.01e-32
0.0
```

(Residuals at the working precision.)

## 3. The gyroscope  `analogy`

The earlier page reads ξ(s) = ξ(1−s) as "a rotation — this IS angular
momentum", the critical line as the equatorial plane of a gyroscope with poles
at σ = 0 and σ = 1, "RH = the gyroscope never wobbles", and a zero off the line
as precession that makes "up" locally undefined. Corrections and standing:

- the symmetry is a reflection, not a rotation (fact 2); no angular momentum is attached to it;
- a hypothetical off-line zero does not "tilt" anything in ξ: it enters as a symmetric quadruple (fact 3), and the functional equation continues to hold;
- "causality fails at that point" has no counterpart in the mathematics.

As a picture of why the critical line is a natural axis (the fixed set of the
reflection) the gyroscope is harmless. As an argument for RH it adds nothing
([13](13_omgwtf_rh_proof.md) §3).

**Poles into modular cusps.** Modular forms have cusps at the rational boundary
points of the upper half-plane, and the claim "the north pole locks into the
cusp: that lock IS the Modularity Theorem; the Frey curve's cusp lies where the
pole cannot reach without leaving σ = ½" is a metaphor for the Frey–Ribet–Wiles
argument ([18](18_fermat_lattice.md) §3). In that argument the contradiction
comes from Ribet's theorem (the Frey curve cannot be modular) and Wiles's
modularity of semistable curves; neither uses the Riemann Hypothesis or the
position of the zeros, so "the gyroscope will not leave σ = ½, therefore the Frey
curve cannot exist" is not the proof and is not an additional one.

## 4. Factors and no factors: compressible and incompressible  `analogy`

| | Riemann | Fermat |
|---|---|---|
| Objects | primes | composites |
| Property | no factors | has factors |
| Fluid analogy | incompressible, ∇·u = 0 | compressible, ∇·u ≠ 0 |
| Medium state | non-shear 𝕆 | cavitation void |

A prime has no internal structure to fold; the non-shear medium of
[31](31_cavitation_causality_fermat.md) is "incompressible" in the same
sense. Writing aⁿ + bⁿ = cⁿ with n ≥ 3 is read as "compressing three
incompressible objects into a factored configuration", which the medium
refuses; so FLT "is the incompressibility condition of the prime medium".
That is a way of narrating FLT, not a proof and not an independent
derivation of it. The Euler product ζ(s) = Π_p (1 − p^(−s))^(−1) = Σ n^(−s) (for
Re s > 1; `ESTABLISHED`) is the exact statement that the primes generate every
integer, and the table is a mnemonic for it.

## 5. Black holes and Navier–Stokes, restated  `CONJECTURE`

The model: the medium is incompressible (Riemann side); the event horizon is the
incompressible/compressible boundary; falling through it is entering the
Fermat-forbidden zone. Navier–Stokes: its singularity "is an incompressible
fluid forced into a compressible configuration, the gyroscope collapsing
because the imaginary component (the spin) was removed"; restoring the Blue
channel keeps ∇·u = 0 and removes the singularity. Standing: the claim is the
framework's reading of [106](106_the_navier_stokes_problem.md) and is not a
regularity proof. A standard fact for context: the incompressible
Navier–Stokes equations already enforce ∇·u = 0, so "forcing it into a
compressible configuration" is not a feature of the equations whose global
regularity is the open problem.

## 6. Open threads (as listed, kept)

- Formalise the gyroscope precession → causality failure argument (note §3: as stated it has no counterpart).
- Connect Blue-channel restoration explicitly to the Navier–Stokes problem statement.
- Incompressibility → FLT as a corollary, written up cleanly (the §4 caveat applies).
- Embed the σ-face table as the anchor of the D-P introduction.

## 7. Related pages

[13 RH proof path](13_omgwtf_rh_proof.md) · [18 Fermat lattice](18_fermat_lattice.md) ·
[31 Cavitation, causality, Fermat](31_cavitation_causality_fermat.md) · [32 The superconducting medium](32_superconducting_medium.md) ·
[106 The Navier–Stokes problem](106_the_navier_stokes_problem.md)
