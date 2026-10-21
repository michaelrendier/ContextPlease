# 126 — The Circle Catalogue: every unit circle, six drawings and a seventh

**Built 2026-10-15.** Engine: `GenerationalLineage/engine/toolsets/circle.py` (one file, `LINE = "both"`, 27 self-checks). Full tables and proofs-by-code: `GenerationalLineage/wiki/Circle-Catalogue.md`. The ℓ_p / factoring half: `TuringStack/wiki/Lp-Circles-Fermat-Curves-and-the-Two-Factoring-Conics-2026-10-15.md`. Scratch evidence p1–p12: `ContextPlease/claude/scratchpad/2026-10-15_circle_unit_session/`. Follows [[96_the_riemann_fermat_horizon]] (the heartbeat integral), [[22_constant_facets]] (π, φ, i, e as facets) and [[121_fast_inverse_square_root_of_the_two_trees]].

---

## Origin

Cody, 2026-10-15, looking at a card of six magnetism graphs: the six are **six different ways of drawing a circle** — partitions, foldings, permutations — each the circle plus a transform that reduces it to one pathway. "Everything is circles"; 0_RB is how to partition, permute, fold, disambiguate, cavitate, measure and show circles in action. The area under the Riemann–Fermat heartbeat (∫₀^(2π) sin² = π) is where the ½ radius comes from. Then: use every constant of the UNS as a unit and build every kind of unit circle, listing circumference, diameter/radius and area; use the half-diameter radii too; use each as σ_RB; say a lot more about the negative-π area of the imaginary circle and the laws of sines and cosines in imaginary terms; cataloguing and relating, one file, "one level up from the fixed-point translator". The six names (orbit, unfold, cut, fold, project, shuffle) were approved; the seventh circle (ℓ_p) goes in.

## What was found

- **The half radius.** (sin²x − ½)² + (sin x cos x)² = ¼: a circle of radius ½ through the origin; d = 1, C = π, A = π/4. The area under the heartbeat over one cycle (π) is that circle's circumference. ζ(½+it) ≈ 2cosθ·e^(−iθ) is a circle of area π; measured lobes between zeros have shape factor equal to the phase sweep (corr 0.978): circle at 1, cardioid at 1.5, the largest lobes 1.53.
- **Constants × roles.** The catalogue (GL wiki §3) covers 14 constants in 4 roles. Near-equalities between rows are exact π-lattice algebra (constants in {2^a π^b}); φ, e, ln 10, Ω, d*, GAP gave no cross hit.
- **Add : Scale : Sign.** In u = ln r the diameter and circumference are shifts (Add), the area is a slope of 2 (Scale), and an imaginary radius is a quarter turn u → u + iπ/2 (Sign): C×i, A×(−1), V_n×iⁿ.
- **σ_RB readings.** r = ½ is exactly critical; its diameter 1 is Yang–Mills-like, its circumference π GR-like. The Noether-current ratio is p^(1−2σ), so the smaller/larger current is the wire profile e^(−2|σ−½| ln p). Imaginary σ = 2i is a pure rotation per prime.
- **Imaginary circle.** d = 2iρ, C = 2πiρ, A = −πρ², C² = 4πA exactly. The laws of sines and cosines keep their form (homogeneous); every degree-2 quantity flips sign; Heron's 16A² is unchanged and its square-root branch is the Sign. A sphere of radius iρ is the hyperbolic plane: area ρ²(π − A − B − C), the angle deficit. The Gaussian ∫exp(−r²/R²) = πR² diverges at R = i (−π is the continuation); at R² = i it is Fresnel, value iπ.
- **Dipole → normal.** U = −MB cosθ is a cosine well; e^(κcosθ) is von Mises; sd(θ) → 1/√κ, kurtosis → 0 — a normal distribution in the limit; many dipoles → CLT; von Mises is max-entropy at fixed ⟨cos⟩.
- **Wire ↔ Mandelbrot ↔ gravity.** One flux law in n dimensions; the inversion fold is exact only at n = 2; the wire profile is the multiplier map c(μ) = μ/2 − μ²/4 with fold μ → 1/μ̄; the cardioid has area 3π/8 and perimeter 4.
- **Fast inverse square root.** The bit trick is a scale ×(−½) in u = ln x; near the unit circle one Newton step 1/r ≈ (3 − r²)/2 is cheaper (error ≈ 3ε²/8) but only there. Ω/(4π) matching the optimal magic σ to 0.22 % is a weak coincidence.
- **The seventh circle.** ℓ_p: π_p = π_q for 1/p + 1/q = 1; π₂ = π is the minimum; π₁ = π_∞ = 4; areas differ across a dual pair. Integer p ≥ 3 is the Fermat curve.

## Honest boundaries

- Nothing here moves a Clay problem or any established open programme; the cross-domain readings (σ regimes, wire ↔ Mandelbrot) are intuition aids that the code checks numerically, no more.
- The Add/Scale/Sign placement of π (C → Add, A → Scale, d → Sign) is a proposal derived from the log chart; the three circles are computed either way.
- The cosine form of the spherical law of cosines fails numerically for R ≳ 1e5 (kept as a recorded limit).
- Citations were written from the originals' bibliographic records; none was downloaded.
