# 115 — Nečas–Růžička–Šverák: no Self-Similar Navier–Stokes Blow-Up (of the Leray Kind)

| | |
|---|---|
| Scope | the literature on Leray's self-similar blow-up ansatz for Navier–Stokes, as the precedent for the "clean spiral against frustrated spiral" distinction (continuous against discrete self-similarity) |
| Intake | citation pass, 2026-09-04 session; [98](98_provenance_and_citations.md). **Independent parallel**: the distinction was reached geometrically and maps onto the continuous-versus-discrete self-similarity results |
| Verification (2026-11-13) | Nečas–Růžička–Šverák (*Acta Math.* 176(2), 283–294, 1996), Tsai (*Arch. Ration. Mech. Anal.* 143(1), 29–51, 1998) and Jia–Šverák (*Invent. Math.* 196(1), 233–265; online 2013) were resolved against Crossref. **Not located:** Constantin–Fefferman 1993 (*Indiana Univ. Math. J.* 42(3), 775–789; the search returned a 2023 *Nonlinearity* paper on the same topic, not the 1993 paper) and Leray 1934 (no identifier) |
| Confidence | the citations and the theorem statements marked ESTABLISHED: as published · the mapping onto the "frustrated spiral": `INTERPRETATION` · the statement that discrete self-similarity "survives": see §2 |

## 1. The references

- **[Leray1934]** J. Leray, *Sur le mouvement d'un liquide visqueux emplissant l'espace*, *Acta Math.* 63, 193–248: weak solutions; and the proposed **exactly self-similar** finite-time blow-up ansatz u(x, t) = (T − t)^(−1/2) U(x/√(T − t)) (continuous scale invariance).
- **[NecasRuzickaSverak1996]** J. Nečas, M. Růžička & V. Šverák, *On Leray's self-similar solutions of the Navier–Stokes equations*, *Acta Math.* 176(2), 283–294: **no non-trivial Leray self-similar solution in L³(ℝ³)**; continuous self-similar blow-up of that form is ruled out.
- **[Tsai1998]** T.-P. Tsai, *On Leray's self-similar solutions of the Navier–Stokes equations satisfying local energy estimates*, *Arch. Ration. Mech. Anal.* 143, 29–51: the extension to solutions satisfying a local energy bound.
- **[JiaSverak2014]** H. Jia & V. Šverák, *Local-in-space estimates near initial time for weak solutions of the Navier–Stokes equations and forward self-similar solutions*, *Invent. Math.* 196, 233–265: constructs **forward** self-similar (and, in the programme that follows, discretely self-similar) solutions for scale-invariant initial data. These are solutions *starting* from singular, scale-invariant data, which is a different object from a smooth-data blow-up.
- **[ConstantinFefferman1993]** P. Constantin & C. Fefferman, *Direction of vorticity and the problem of global regularity for the Navier–Stokes equations*, *Indiana Univ. Math. J.* 42(3), 775–789: regularity if the vorticity direction stays Lipschitz in regions of large vorticity (so a blow-up would need a direction-field defect, a saddle or cusp). Quoted as recorded; not located in the checks.

## 2. What it anchors, and a caution on "survives"

- **Clean spiral = continuous self-similarity** (the Smith-chart symmetry, a one-parameter scaling): ruled out for the Leray ansatz. **Frustrated spiral = discrete self-similarity** (the Apollonian symmetry: invariance under one fixed zoom factor, recursively): the framework's candidate that survives.
- The frustrated spiral **threads the σ = ½ hub saddle** (the stable ⊥ unstable manifold cross); its return step interdigitates the outbound step, which is the vorticity-direction defect the Constantin–Fefferman criterion rules against.

**Caution.** The theorems above exclude the *continuous* Leray ansatz for finite-energy solutions; they do not establish that a *discretely* self-similar finite-time blow-up exists, and the question of whether the three-dimensional Navier–Stokes equations blow up in finite time is the open Clay problem ([106](106_the_navier_stokes_problem.md), [105](105_the_millennium_problems_in_ainulindale.md)). That discrete self-similarity "survives" means only that the published exclusion does not cover it; whether the literature has since excluded or constructed
backward discretely self-similar solutions was not checked in this pass, and the Jia–Šverák construction concerns forward solutions from singular data. The page's mapping (clean ↔ continuous, frustrated ↔ discrete) is the framework's geometric reading and is not a theorem.

## 3. Cite in

[106](106_the_navier_stokes_problem.md); `VAPMIP/docs/wiki/Tuning-the-Engine/35`; the frustrated-spiral discussion notes; `FourthAgePapers/Crawford_NavierStokes`.

## 4. Related pages

[98](98_provenance_and_citations.md) · [106](106_the_navier_stokes_problem.md) · [112](112_sullivan_dictionary.md) · [114](114_herrmann_apollonian_bearings_turbulence.md)
