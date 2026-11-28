# 110 — QM in GR, GR in QM: Two Jurisdictions and the Current Between Them

| | |
|---|---|
| Scope | a jurisdiction/projection reading of the QM–GR seam: what each theory loses when read in the other's instruments, the asymmetry of the floors, the shear current between them, and recombination as the ignition point |
| Written | 2026-09-01. A side note; continues [93](93_qm_gr_by_tree.md) (the QM↔GR distinction as radial, a tower-rung gap) and leaves the VAPMIP UFT for its own treatment |
| The author | "i want my UFT used to show me what QM looks like in GR, and what GR looks like in QM … QM in GR is going to be a hard resolution floor much higher … but GR in QM shaped the actual universe … the current between them sliding past each other … what does the 'metric energy tensor' say about QM and what does Schrödinger and SMPP say about GR … different jurisdictions … it's where the first ripples from hydrogen becoming stable ignited the fuel of decomposition." |
| Related | [92](92_ring_theory_spine.md), [90](90_divisors_are_definers.md), [17](17_alpha_omega_d_star.md), [75b](75b_bao_mass_gap_engine.md) (`ValaQuenta/modules/bao_mass_gap`), [73](73_why_the_half_line.md), [52](52_l_dynamic_avoided_collaborator.md), [82](82_l_io_photon_path.md), [47](47_the_two_trees.md), [108](108_desitter_cavitation.md); `project-oblique-gear`, `project-flattening-syndrome`, generational-lineage skill §7b |
| Confidence | **THEORETICAL**: a reading, not a quantum-gravity theory. The standard-physics statements (§§2–3, recombination) are ESTABLISHED; one sentence of the earlier text is corrected in §3 |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. Jurisdiction

The UFT's standing claim: **scale gives a law its jurisdiction**, and the jurisdiction changes with scale. The native coordinate is u = ln x (the anti-flattening axis), so a jurisdiction is a **band in u**, not a point. QM and GR are two such bands: they do not contradict, and they do not overlap cleanly; between them is a **seam**. Reading one theory in the other's jurisdiction is a projection across the seam, and every projection through a flat view loses a coordinate (the spiral seen as a circle). The question: which coordinate does each direction lose, and how
expensive is the loss?

## 2. GR ⟶ QM: a soft, low floor  `INTERPRETATION` over standard physics

Read GR with QM's instruments (a fixed background, a chosen vacuum). Curvature becomes a potential term, V(x) = mΦ(x), in the Schrödinger equation; the metric perturbation h_μν becomes a spin-2 field on flat space (gravitons); gravity enters as a slowly varying external parameter, exactly as in the Schrödinger equation on a curved background and in quantum field theory in curved spacetime. The lost coordinate is **back-reaction** (the field's own weight on the geometry), and the loss is cheap
because the background barely moves: the GR-in-QM floor is low and soft, so the projection carries far.

This projection is what built the universe's initial conditions in the standard account: primordial density perturbations are a quantum field read through a metric, and their spectrum set the CMB anisotropies, the acoustic (BAO) scale and the seed of every halo. The `bao_mass_gap` engine measures the residue it leaves: Δ = Ω_ZS − d\*·ln 10 > 0, invariant in the mode number ([75b](75b_bao_mass_gap_engine.md)). *The stronger reading "Δ = 1/(1000√2) exactly = the Yang–Mills mass gap" was disproven as stated (2026-08-30); Δ > 0 and Δ ≈ Ω_ZS − d\*·ln 10 stand* (0.000707358 against 0.000707107, [56](56_telescope_caustic_zeno.md) Listing 1).

## 3. QM ⟶ GR: a hard, much higher floor  `INTERPRETATION`, one correction

Read QM with GR's instruments. GR's only handle on matter is the stress–energy tensor T_μν (the author's "metric energy tensor"), and its verdict is G_μν = 8πT_μν. A quantum state enters semiclassically as an expectation value, T_μν → ⟨ψ|T̂_μν|ψ⟩, and what remains is a decohered, coarse-grained fluid. Semiclassical gravity has no consistent sub-seam limit and no resolved back-reaction (the known breakdown), so the QM-in-GR floor is hard and sits much higher: the page's estimate is "roughly d\* lifted across the rung
gap ℍ → 𝕆", one Cayley–Dickson generation ([93](93_qm_gr_by_tree.md): QM first at dim 4, GR first at dim 8; the facet ladder puts QM/Riemann at σ = ½ and GR at σ = 2), "i.e. multiplied by ln 10 per decade of seam separation". The exact lifted value is **not calculated** (flagged for the VAPMIP UFT pass).

**Correction.** The earlier text says that on this projection "the phase is gone": "superposition, interference, the discrete spectrum: none of it sources geometry". An expectation value is quadratic in ψ and **retains the relative phases between components of a superposition**: for two lumps ψ₁ + e^{iφ}ψ₂ the density |ψ|², and so ⟨x²⟩ and the energy density, depend on φ through the cross term 2 Re(ψ₁*ψ₂ e^{iφ}). What is lost is the overall phase and everything not captured by the expectation (higher moments, the entanglement structure beyond ρ). Listing 1 shows the dependence.

**Listing 1 — the relative phase survives in an expectation value; the recombination temperature** (written for this page; needs numpy; runs cold)

```python
import numpy as np
x = np.linspace(-12, 12, 4001); dx = x[1] - x[0]
g = lambda x0, k: np.exp(-(x - x0)**2 / 2) * np.exp(1j * k * x)
for phi in (0.0, np.pi / 2, np.pi):
    psi = g(-2, 0.0) + np.exp(1j * phi) * g(2, 0.0); rho = np.abs(psi)**2; rho /= rho.sum() * dx
    print('relative phase %.2f rad between two Gaussian lumps: density at the midpoint %.4f ; <x^2> = %.4f' % (phi, rho[np.argmin(abs(x))], (x**2 * rho).sum() * dx))
for phi in (0.0, np.pi):
    psi = g(-0.5, 1.0) + np.exp(1j * phi) * g(0.5, 1.0); rho = np.abs(psi)**2; rho /= rho.sum() * dx
    print('overlapping lumps, phase %.2f: peak density %.4f' % (phi, rho.max()))
T0 = 2.725
for z in (1100, 1090): print('recombination at z = %d: T = %.0f K = %.2f eV (kB T)' % (z, T0 * (1 + z), T0 * (1 + z) * 8.617333e-5))
```

```
relative phase 0.00 rad between two Gaussian lumps: density at the midpoint 0.0203 ; <x^2> = 4.4281
relative phase 1.57 rad between two Gaussian lumps: density at the midpoint 0.0103 ; <x^2> = 4.5000
relative phase 3.14 rad between two Gaussian lumps: density at the midpoint 0.0000 ; <x^2> = 4.5746
overlapping lumps, phase 0.00: peak density 0.4940
overlapping lumps, phase 3.14: peak density 0.3983
recombination at z = 1100: T = 3000 K = 0.26 eV (kB T)
recombination at z = 1090: T = 2973 K = 0.26 eV (kB T)
```

So the statement that the amplitude/phase "is the lost coordinate" is true of the **overall** phase and of the decohered mixture GR actually uses once the state has decohered; for a coherent superposition the relative phase does source a different T_μν. The "|z|² step, no adjoint" reading ([90](90_divisors_are_definers.md); generational-lineage §7b) therefore describes the loss at the level of the one-point density, not of ⟨T⟩ in general. The asymmetry of the floors (GR can hold a smeared copy of matter, matter can hold only a frozen copy of geometry) is kept as the framework's reading.

## 4. What each instrument says about the other theory

| instrument | verdict |
|---|---|
| **T_μν**, the stress–energy tensor | "I see QM's census, not its ballots": gravity is sourced from ⟨ψ\|T̂\|ψ⟩, a decohered shadow (the flashlight-shadow of `project-scalar-context-paper`); per §3 the census keeps the *relative* phases within a coherent superposition |
| **Schrödinger equation** | "GR is a slowly varying background I diagonalise against": the metric is an external parameter and a vacuum choice, nothing dynamical |
| **Standard Model (SMPP)** | has no dynamical gravity at all; GR appears as a boundary condition on the fields, never as a field among them |

The asymmetry is the content: G_μν = 8πT_μν is a **jurisdiction-boundary equation**: the left side is geometry (GR: forward, inertial, Laurelin, "what is"), the right side is source (the QM expectation: Telperion, "what is allowed"), and the "=" is the intertwiner L_(I|O) ([52](52_l_dynamic_avoided_collaborator.md), [82](82_l_io_photon_path.md)). It does not read the same both ways.

## 5. The current between them: sliding past each other

The two jurisdictions are not stacked; they **shear**. The shear along their seam is the **Oblique Gear** (`project-oblique-gear`): σ_RB as tilt (Re) + axis (Im); Scale ⟂ Flow is a Helmholtz split; σ_RB is the Riemann–Silberstein vector (F = E + iB, the compact form of Maxwell's equations), "the Oblique Gear *is* Maxwell" (the author's statement; the identification of the QM↔GR current with σ_RB is by analogy and not computed for this pair). The QM↔GR current is tangential to the seam: neither normal to GR nor to QM, "a genuine third thing". At σ = ½ (the Mingling, the hyperbolic saddle, λ ≈ 6) the two are in
balance and the shear is maximal: a saddle has maximum tangential flow and zero normal force; off σ = ½ one jurisdiction dominates and the current slackens.

## 6. The ignition point: hydrogen becomes stable  `ESTABLISHED` (standard cosmology) + `INTERPRETATION`

The seam has a moment in cosmic time where the current does real work: **recombination**, z ≈ 1100 (T ≈ 3000 K, Listing 1; kBT ≈ 0.26 eV, below the 13.6 eV hydrogen binding energy because of the high photon-to-baryon ratio): the electron binds the proton, hydrogen goes neutral, photons decouple, and the CMB is released. **Before:** radiation rules; photon pressure is a QM-pressure term; the perturbations are frozen standing sound (the acoustic peaks; the BAO scale, about 147 Mpc, [56](56_telescope_caustic_zeno.md)). **After:** the matter/gravity
jurisdiction takes over; gravitational collapse, "the fuel of decomposition", ignites, structure forms, the composite tree (Laurelin) begins to grow, and with it entropy production. The hand-off from GR-in-QM (the quantum seed spectrum) to GR proper (non-linear collapse) is read as the current sliding across the seam, and the `bao_mass_gap` residue Δ as the scar it leaves in the spectrum.

## 7. Honest boundaries

- **Calculated:** Ω_ZS = W(1) = 0.56714… and d\* = Ω_ZS/ln 10 ≈ 0.246 ([17](17_alpha_omega_d_star.md)); the dim-4/dim-8 rung gap ([93](93_qm_gr_by_tree.md)); the BAO residue Δ > 0, invariant in mode number (`bao_mass_gap`). **Correction to the earlier cross-reference:** "73 % of curvature is a boundary phenomenon" is an unenriched count (crossing triples are 80 % of all triples, [93](93_qm_gr_by_tree.md) §3); it is not used as evidence here.
- **Asserted, not yet calculated:** the exact height of the QM-in-GR floor; the identification of the QM↔GR shear current with σ_RB specifically; "GR-in-QM shaped the universe" as a strong claim against the standard inflationary-perturbation account it rephrases.
- This is a reading of the seam, not a theory of it. The VAPMIP UFT gets its own treatment.

## 8. Summary

| direction | instrument | lost coordinate | floor |
|---|---|---|---|
| **GR in QM** | Schrödinger V = mΦ; gravitons on flat space | back-reaction | low, soft: carries far; set the initial conditions |
| **QM in GR** | T_μν → ⟨ψ\|T̂\|ψ⟩ (semiclassical) | the overall phase and everything beyond the expectation (relative phases within a coherent state survive, §3) | hard, much higher: ≈ d\* lifted across ℍ → 𝕆 (not calculated) |
| **between** | σ_RB / Oblique Gear shear | (this is the seam) | maximal at σ = ½; does its work at recombination |

**QM in GR is a census with the overall ballots burned; GR in QM is a background you diagonalise against. The "=" in Einstein's equation is the seam, it reads asymmetrically, and the current along it lit the fire of structure when hydrogen went quiet.**

## 9. Related pages

[93](93_qm_gr_by_tree.md) · [108](108_desitter_cavitation.md) · [75b](75b_bao_mass_gap_engine.md) · [111](111_alcubierre_reverse_gr.md) · [112](112_sullivan_dictionary.md)
