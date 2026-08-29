# 102 — Berry–Keating and the Hilbert–Pólya lineage

[98_provenance_and_citations.md](98_provenance_and_citations.md) §A.5. The
spectral approach to the Riemann Hypothesis — the operator route this framework
takes to `σ = ½`.

---

## The lineage

- **[HilbertPolya]** Hilbert, D. & Pólya, G. — *no publication.* The idea that
  the non-trivial zeros are eigenvalues of a self-adjoint operator (hence real,
  hence on the critical line) is folklore, documented in **Pólya's 1982 letter
  to Andrew Odlyzko** (archived: `dtc.umn.edu/~odlyzko/polya/`).
- **[Montgomery1973]** Montgomery, H. L. (1973). *The pair correlation of zeros
  of the zeta function.* Proc. Sympos. Pure Math. XXIV, AMS, 181–193. — the
  pair-correlation conjecture; the zeros' spacing statistics match the **GUE**
  (Gaussian Unitary Ensemble) of random-matrix theory.
- **[Odlyzko1987]** Odlyzko, A. M. (1987). *On the distribution of spacings
  between zeros of the zeta function.* Math. Comp. 48(177), 273–308. — numerical
  confirmation to high zero height.
- **[BerryKeating1999a]** Berry, M. V. & Keating, J. P. (1999). *H = xp and the
  Riemann zeros.* In *Supersymmetry and Trace Formulae* (Kluwer), 355–367.
- **[BerryKeating1999b]** Berry, M. V. & Keating, J. P. (1999). *The Riemann
  zeros and eigenvalue asymptotics.* SIAM Review 41(2), 236–266.
  DOI:10.1137/S0036144598347497. — the classical Hamiltonian `H = xp`, suitably
  regularised, has a smoothed level count matching Riemann's `N(E)`.
- **[Connes1999]** Connes, A. (1999). *Trace formula in noncommutative geometry
  and the zeros of the Riemann zeta function.* Selecta Math. 5(1), 29–106.
  arXiv:math/9811068. — a trace-formula realisation; RH as a positivity
  statement.
- **[Stone1932]** Stone, M. H. (1932). *On one-parameter unitary groups in
  Hilbert space.* Annals of Mathematics 33(3), 643–648. — self-adjoint
  generators have **real spectrum**. The lemma the argument turns on.

## What Ainulindalë takes

- **The operator route to the critical line.** Ĥ_RB is constructed (D-CS_Memory
  §18; wiki/14) to be self-adjoint, `Ĥ_RB† = Ĥ_RB`. Stone's theorem then forces
  a real spectrum, placing the zeros on `σ = ½`. **Berry–Keating `H = xp` is
  recovered as a *consequence* of Ĥ_RB, not assumed independently** (wiki/07;
  D-CS_Memory §12).
- **The Red channel is `R̂_p = xp`** — Berry–Keating as the "what IS" operator,
  paired with the Blue Fermat–Weierstrass operator `B̂_p = ½p² + ℘(x;g₂,g₃)`.
- **GUE / pair-correlation is the fingerprint the framework's spectrum must
  match** — the Hermite H₁₆ timing wheel (wiki/23) and the "GUE timing wheel"
  in the six-family Ω_ZS table are checked against it.
- The Berry–Keating domain `L²([α_F, Ω_ZS])` — floor at the fine-structure
  constant, ceiling at the Lambert W fixed point — is the interval Ĥ_NN operates
  on (wiki/07, wiki/17).

**What is NOT claimed:** that this proves RH, or that Ĥ_RB has been shown
rigorously self-adjoint on a dense domain with the right spectrum. Both are
stated OPEN (D-CS_Memory §42).

---

## Appears in

wiki/07, wiki/14, wiki/17, wiki/23, wiki/73, wiki/98, wiki/102; D-CS_Memory §12,
§18, §42; VAPMIP_Paper §"Engine 07", §"Engine 14".
