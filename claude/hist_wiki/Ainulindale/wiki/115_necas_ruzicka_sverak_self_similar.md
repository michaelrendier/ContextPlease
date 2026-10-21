# 115 — Nečas–Růžička–Šverák: no self-similar Navier–Stokes blow-up

[98_provenance_and_citations.md](98_provenance_and_citations.md). Citation-pass
intake, 2026-09-04 session. Independent parallel — the "clean spiral vs
frustrated spiral" distinction was reached geometrically; it maps exactly onto
the continuous-vs-discrete self-similarity result.

---

- **[Leray1934]** Leray, J. (1934). *Sur le mouvement d'un liquide visqueux
  emplissant l'espace.* Acta Math. 63, 193–248. — weak solutions; and the
  proposed **exactly self-similar** finite-time blow-up ansatz `u(x,t) =
  (T−t)^{−1/2} U(x/√(T−t))` (continuous scale invariance).
- **[NecasRuzickaSverak1996]** Nečas, J., Růžička, M. & Šverák, V. (1996).
  *On Leray's self-similar solutions of the Navier–Stokes equations.* Acta
  Math. 176(2), 283–294. — **no nontrivial Leray self-similar solution in
  L³(ℝ³)**. Continuous self-similar blow-up is ruled out.
- **[Tsai1998]** Tsai, T.-P. (1998). *On Leray's self-similar solutions of
  the Navier–Stokes equations satisfying local energy estimates.* Arch.
  Ration. Mech. Anal. 143, 29–51. — extension under a local energy bound.
- **[JiaSverak2014]** Jia, H. & Šverák, V. (2014). *Local-in-space estimates
  near initial time for weak solutions … and forward self-similar solutions.*
  Invent. Math. 196, 233–265. — **discretely** self-similar solutions
  (invariance under one fixed zoom factor) *are* constructed. The surviving
  case.
- **[ConstantinFefferman1993]** Constantin, P. & Fefferman, C. (1993).
  *Direction of vorticity and the problem of global regularity for the
  Navier–Stokes equations.* Indiana Univ. Math. J. 42(3), 775–789. —
  regularity if the vorticity *direction* stays Lipschitz where vorticity is
  large (a direction-field index singularity = a saddle/cusp defect would be
  needed to blow up).

## What it anchors

- **Clean spiral = continuous self-similarity** (Smith-chart symmetry) — ruled
  out. **Frustrated spiral = discrete self-similarity** (Apollonian symmetry,
  one fixed zoom, recursive) — survives.
- The frustrated spiral **threads the σ = ½ hub saddle** (stable⊥unstable
  manifold cross); its return step interdigitates the outbound step — the
  vorticity-direction defect Constantin–Fefferman rules against.

## Cite in

`Ainulindale/wiki/106_the_navier_stokes_problem.md`;
`VAPMIP/docs/wiki/Tuning-the-Engine/35`; the frustrated-spiral discussion notes;
`FourthAgePapers/Crawford_NavierStokes`.
