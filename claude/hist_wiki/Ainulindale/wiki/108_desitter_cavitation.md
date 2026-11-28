# 108 — No Singularity: the Abrikosov-Vortex Core and De Sitter Cavitation

| | |
|---|---|
| Scope | the claim that a black-hole interior is a finite, sub-Planckian de Sitter core (gravastar matching), with the closed-form numbers it implies, a pre-registered prediction and falsifiers; the engineering table for four black-hole classes; the honest boundaries |
| Engine | `ValaQuenta/modules/desitter_cavitation/` (`DeSitterCavitationModule`, 8 equations): **calculation, not simulation** |
| Paper | `FourthAgePapers/DeSitterCavitation/` (one claim, one Holcus prediction, notebooks 00–03, `predictions.json`) |
| Related | [75](75_abrikosov_lattice.md), [73](73_why_the_half_line.md), `fixed_point.py` (the inside-out horizon), `AbrikosovTree` (the Two Trees), `generational-lineage` skill §7 (collisions), §8 (provenance) |
| Confidence | **THEORETICAL.** The core-curvature formula is a de Sitter identity (ESTABLISHED, re-run); that a real interior realises it is a consistency argument, not a derivation from a field equation; the matching condition that fixes L = r_s is stated precisely in §2 |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below. The engine's 8 equations were not re-run. References checked against arXiv/Crossref (§5) |

## 1. Origin

> "space can move faster than light — it's allowed — so it wouldn't necessarily get trapped inside of it … it's not a sink, it's a vortex that has the other end a generational lineage of turbulent flow … and the shadow of that flow is frame dragging." — the author, 2026-08-30, working from the river model of space toward the interior.

The Abrikosov identification ([75](75_abrikosov_lattice.md)) says the Riemann zeros are vortex cores of the prime condensate; a superconducting vortex core has no singularity (|Ψ| → 0 is a simple zero of winding number 1, with finite free-energy density, the condensation energy H_c²/8π). If the black-hole interior is the same object one domain over, it too has no singularity: the condensate vanishes and everything else stays finite. As in [75](75_abrikosov_lattice.md), this is an analogy of roles; the physical argument is the gravastar one of §2.

## 2. The claim, and what forces L = r_s

The claim: there is no singularity; the interior is a finite, sub-Planckian de Sitter core. A gravastar matching (Mazur–Mottola) of the interior metric 1 − (r/L)² to the exterior Schwarzschild 1 − r_s/r at a shell at radius R requires continuity of the metric there: 1 − R²/L² = 1 − r_s/R, i.e. **L² = R³/r_s**. The page states L_dS = r_s; that follows when the shell sits at the horizon, R = r_s, and not for a shell at general R (Listing 1 prints the relation). The identity L = r_s is therefore the **horizon-shell** case of the matching, an assumption of the claim and not something the matching alone forces; a shell
at R > r_s gives L > r_s and a correspondingly smaller core curvature, so the numbers below are for the horizon-shell case.

From L = r_s the engine reads off (Listing 1, using 2018 CODATA/IAU constants):

| quantity | value | reading |
|---|---|---|
| interior BANG time | τ = 1/H_dS = r_s/c = 2GM/c³ | one e-fold; the core cannot rest |
| **core curvature (HOLCUS)** | K_core = 24/L_dS⁴ = (3/2) c⁸/(G⁴M⁴) | finite, ∝ M⁻⁴, sub-Planckian for M > (3/2)^{1/4} m_Pl = 2.41×10⁻⁸ kg |
| Schwarzschild contrast | K(r) = 48 G²M²/(c⁴r⁶) → ∞ as r → 0 | the artefact the claim denies |
| core / Hawking temperature | T_dS = ħH_dS/2πk_B = 2·T_H(M) | the core inherits the hole's scale, doubled (Listing 1: ratio 2.0000) |
| two release channels | stiff space p = −ρc² (Λ-signed) · stiff matter p = ρc² (Zel'dovich ceiling) | metric vs radiative |
| unwrapping | the horizon recedes below the core as M evaporates | decompression → the De Sitter Cavitation |

The Kretschmann scalar of de Sitter is 24/L⁴ and of Schwarzschild 48G²M²/(c⁴r⁶): standard.

**Holcus prediction (pre-registered):** K_core(M) = (3/2) c⁸/(G⁴M⁴), with a gravitational-wave ringdown echo at delay ≈ (2r_s/c) ln(r_s/ℓ_Pl) as its observational shadow. **Falsifier:** a core curvature that diverges (a classical GR singularity), or pins to K_Planck independent of M (limiting-curvature / Planck-star), or no ringdown echoes down to the reflectivity bound a finite core requires.

## 3. The engineering table  `ESTABLISHED` (closed forms)

**Listing 1 — the four classes, the temperature ratio, the junction condition, and the cavitation budget** (written for this page; needs sympy; runs cold)

```python
import math, sympy as sp
G, c, hbar, kB, Msun = 6.67430e-11, 2.99792458e8, 1.054571817e-34, 1.380649e-23, 1.98847e30
mP = math.sqrt(hbar * c / G); lP = math.sqrt(hbar * G / c**3); KP = 1 / lP**4
print('m_Planck = %.3e kg ; l_Planck = %.3e m' % (mP, lP))
for name, M in (('kugelblitz 1e12 kg', 1e12), ('stellar 10 Msun', 10 * Msun), ('intermediate 1e4 Msun', 1e4 * Msun), ('supermassive 1e9 Msun', 1e9 * Msun)):
    rs = 2 * G * M / c**2; Kc = 1.5 * c**8 / (G**4 * M**4); TdS = hbar * c / (2 * math.pi * kB * rs); TH = hbar * c**3 / (8 * math.pi * G * M * kB)
    print('%-22s r_s = %.3e m  tau = %.2e s  K_core/K_Planck = %.1e  (1.5 (mP/M)^4 = %.1e)  T_dS/T_H = %.4f' % (name, rs, rs / c, Kc / KP, 1.5 * (mP / M)**4, TdS / TH))
print('sub-Planckian iff M > (3/2)^(1/4) m_P = %.3e kg' % (1.5 ** .25 * mP))
R, L, rs_ = sp.symbols('R L r_s', positive=True)
print('junction: 1 - R^2/L^2 = 1 - r_s/R  =>  L^2 =', sp.simplify(R**3 / rs_), ' (L = r_s only if R = r_s)')
print('Omega_cav = Omega_BH (1 - d*) with Omega_BH = 1e-5, d* = 0.24631: %.2e against Omega_Lambda 0.685' % (1e-5 * (1 - 0.24631)))
```

```
m_Planck = 2.176e-08 kg ; l_Planck = 1.616e-35 m
kugelblitz 1e12 kg     r_s = 1.485e-15 m  tau = 4.95e-24 s  K_core/K_Planck = 3.4e-79  (1.5 (mP/M)^4 = 3.4e-79)  T_dS/T_H = 2.0000
stellar 10 Msun        r_s = 2.953e+04 m  tau = 9.85e-05 s  K_core/K_Planck = 2.2e-156  (1.5 (mP/M)^4 = 2.2e-156)  T_dS/T_H = 2.0000
intermediate 1e4 Msun  r_s = 2.953e+07 m  tau = 9.85e-02 s  K_core/K_Planck = 2.2e-168  (1.5 (mP/M)^4 = 2.2e-168)  T_dS/T_H = 2.0000
supermassive 1e9 Msun  r_s = 2.953e+12 m  tau = 9.85e+03 s  K_core/K_Planck = 2.2e-188  (1.5 (mP/M)^4 = 2.2e-188)  T_dS/T_H = 2.0000
sub-Planckian iff M > (3/2)^(1/4) m_P = 2.409e-08 kg
junction: 1 - R^2/L^2 = 1 - r_s/R  =>  L^2 = R**3/r_s  (L = r_s only if R = r_s)
Omega_cav = Omega_BH (1 - d*) with Omega_BH = 1e-5, d* = 0.24631: 7.54e-06 against Omega_Lambda 0.685
```

| class | r_s | τ = r_s/c | K_core/K_Planck | QGP at the core? |
|---|---|---|---|---|
| kugelblitz / primordial (10¹² kg) | 1.5 fm | 5×10⁻²⁴ s | 3×10⁻⁷⁹ | yes (the page's statement) |
| stellar (10 M☉) | 30 km | 10⁻⁴ s | 2×10⁻¹⁵⁶ | no (yes for M ≲ 3 M☉, the page's statement) |
| intermediate (10⁴ M☉) | 3×10⁴ km | 0.1 s | 2×10⁻¹⁶⁸ | no |
| supermassive (10⁹ M☉) | 20 AU (19.7 AU) | hours (2.7 h) | 2×10⁻¹⁸⁸ | no |

The r_s, τ and K_core/K_Planck columns reproduce (Listing 1; the page's 2×10⁻¹⁵⁶ for the stellar class is 2.2×10⁻¹⁵⁶). The quark–gluon-plasma column is the page's statement and was not recomputed. ρ_core ∝ M⁻² makes the small holes the hot ones. Every class is sub-Planckian in core curvature by at least 78 orders of magnitude (the kugelblitz is the smallest margin, 3×10⁻⁷⁹); Planck-scale curvature appears only for Planck-mass holes. These are statements about the *assumed* core.

## 4. Honest boundaries (kept, with one addition)

- **No derivation that nature picks this interior.** The engine verifies *if gravastar, then* K_core is the de Sitter value; it does not solve a field equation for the interior. The singularity theorems of general relativity (Penrose, Hawking) assume energy conditions; gravastar-type interiors evade them with exotic equations of state (the p = −ρc² core), so this proposal sits outside classical GR's assumptions and is not a result of it.
- The bounce-time and echo-delay coefficients are O(1) and model-dependent (Haggard–Rovelli; Cardoso–Pani); only the scalings are firm.
- The d\* energy split (E_space/E_tot = 1 − d\*) is **asserted**, a secondary prediction. `cosmic_cavitation_budget` gives Ω_cav ≈ Ω_BH(1 − d\*) ≈ 7.5×10⁻⁶ against Ω_Λ ≈ 0.685 (Listing 1: 7.54×10⁻⁶, using Ω_BH = 10⁻⁵): it **fails as a magnitude** and stays in the data. If the mechanism leaves any trace it is dark flow (directional, cumulative along the hole's spin axis), not a dark-energy density.
- **Addition (the matching, §2):** L = r_s is the horizon-shell case of the junction condition L² = R³/r_s, an assumption of the claim.
- Labelled-ZD note: the box-kite object is PSL(2, 7) (order 168, Aut Fano); Moreno's G₂ is the blow-up that forgets the labelling ([84](84_the_box_kite_debugger.md)). The AbrikosovTree README's "ZD(𝕊) ≅ G₂" is the topological statement; this paper uses the labelled one.

## 5. Predecessors and references (checked 2026-11-13)

- [75](75_abrikosov_lattice.md) (the identification; see its §4 for the limits of the "lock"); [73](73_why_the_half_line.md) §6; `fixed_point.py` (the Bang as an inside-out event horizon; the Schwarzschild → de Sitter orientation flip; the GAP as "the mass that cannot be made virtual"); the Two Trees (`AbrikosovTree`).
- **Mazur & Mottola**, *Gravitational condensate stars: an alternative to black holes*, arXiv:gr-qc/0109035 (2001) (the page's "Mazur & Mottola (2001)" is this arXiv preprint; the title *Gravitational vacuum condensate stars* belongs to later write-ups, whose journal details were not confirmed here). **Visser & Wiltshire**, *Stable gravastars — an alternative to black holes?*, *Class. Quantum Grav.* 21(4), 1135–1151 (2004). **Chirenti & Rezzolla**, *How to tell a gravastar from a black hole*, *Class. Quantum Grav.* 24(16), 4191–4206 (2007) (the 2016 paper cited on the earlier page was not checked). **Cardoso, Pani, Cavalcanti, Berti**, *Ergoregion instability of ultracompact astrophysical objects*, *Phys. Rev. D* 77, 124044 (2008). **Haggard & Rovelli**, *Black hole fireworks: quantum-gravity effects outside the horizon spark black to white hole tunneling*, arXiv:1407.0989 (2014), *Phys. Rev. D* 92, 104020 (2015). **Rovelli & Vidotto**, *Planck stars*, arXiv:1401.6562 (2014), *Int. J. Mod. Phys. D* 23(12), 1442026. (All identifiers and titles resolved against arXiv and Crossref, 2026-11-13.)

## 6. Related pages

[75](75_abrikosov_lattice.md) · [73](73_why_the_half_line.md) · [110](110_qm_in_gr_gr_in_qm.md) · [84](84_the_box_kite_debugger.md) · [93](93_qm_gr_by_tree.md)
