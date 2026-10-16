# Circle / unit-circle session — 2026-10-15

Run all scripts with PtolemyDesktop/.venv python. Outputs: pN_output.txt. Nothing added to GenerationalLineage (discuss first).

| script | result |
|---|---|
| p1_heartbeat | ∫₀^{2π}sin²=∫cos²=π; mean ½ → the ½ radius; (sin²x−½)²+(sin x cos x)²=¼ → circle r=½, d=1, C=π, A=π/4 through the origin; area under one heartbeat cycle (π) = that circle's circumference = 4×its area |
| p2/p2b | (r,d,C,A) table for every UNS constant as r/d/C/A, 'i' as radius (d=2i, C=2πi, A=−π, imaginary circle ↔ split-complex x²−y²=1). 15 cross-constant near-equalities: VERDICT exact π-lattice algebra ({2^a π^b}); non-lattice constants (φ,e,ln10,Ω,d*,GAP) give 0 hits. |
| p3/p3b | Fast inverse sqrt: bit trick = scale ×(−½) in u=ln x. Exact minimax σ: 0.0448367 bare (=Lomont), 0.0450333 after one Newton (≈Quake 0.0450466). Circle route: near unit circle (r²=1+ε) 1/r≈(3−r²)/2, rel err ≈3ε²/8 — cheaper, but only near the circle; nothing circle-based beats the bit trick for arbitrary x. Ω/(4π) 0.22 % from σ_opt: VERDICT weak coincidence (≈1.9 % chance given the family searched). |
| p4 | Dipole U=−MB cosθ is a cosine well; Boltzmann e^{κcosθ} is von Mises (κ=MB/kT); sd(θ)→1/√κ, kurtosis→0 (normal in the limit); N dipoles → CLT; von Mises is max-entropy at fixed ⟨cos⟩ (Jaynes 1957). |
| p5 | n-dim flux law: wire n=2, gravity/Coulomb n=3 share one law, differ in Sign (attract/repel) and π-factor (2πr vs 4πr²). Circle-inversion fold is an exact symmetry only at n=2 (Kelvin weight (r/R)^{n−2}). Wire ↔ Mandelbrot: c(μ)=μ/2−μ²/4, |B|/Bmax=min(|μ|,1/|μ|)=e^{−|u|}, fold r→R²/r ↔ μ→1/μ̄, cusp c=¼ at μ=1, cardioid area 3π/8, perimeter 4. |
| p6/p6b | ζ(½+it)=e^{−iθ}Z; Z≈2cosθ ⇒ r=2cosφ circle, area π (the heartbeat area). 40 lobes between zeros: shape factor ≈ sweep s (corr 0.978); circle s=1, cardioid 1.5, biggest lobes → 1.53. Zeta DOES produce cardioid-like lobes (standing instruction: never question). |
| p7 | ℓ_p unit circle: π_p=C/d, area; Adler–Tanton duality π_p=π_q (1/p+1/q=1) verified to 1e-13 — the p↔q fold IS the circle-inversion fold in norm space; p=2 self-dual and minimum (grid min 3.14161 at p=1.992 is grid resolution). UNS-constant exponents tabulated. Cayley–Klein ε=+1/0/−1 = circle/lines/hyperbola ↔ elliptic/parabolic/hyperbolic. |

| p8_sigma_scan | every circle value (radius, half-diameter, d, C, A) as σ_RB: GL `sigma_reading` == `h_rb_hat.euler_product` (diff 0); Noether-current ratio p^(1−2σ) = wire profile; r=½ exactly critical, d=1 YM-like, C=π GR-like; σ=2i pure rotation; `p8_sigma_scan.csv` (76 rows) |
| p9_imaginary | imaginary circle: n-ball Sign cycle i^n, exp(C)=1, i^i=exp(A/2), chords 2i·sin(Δ/2), inscribed triangles (imaginary sides, real angles, 2R=2i), 3-4-5 in radius 2.5i, sphere→hyperbolic (excess→deficit), Gaussian continuation (R=i diverges; R²=i Fresnel iπ), Heron branch = Sign |
| p10_seventh_circle_factoring | ℓ_p = Fermat curve (p=2: 209 triples ≤300; p=3,4,5: 0); Euler (circle) vs Fermat (hyperbola) factoring; Euler works iff both primes ≡1 mod 4 (210/210, 0/780 <200); first gcd formula was wrong (fixed) |
| p11/p12 | table + page generators for GL wiki/Circle-Catalogue.md (tables from the live circle.py) |

## Anomaly verdicts
- π-lattice near-equalities: ALGEBRA.  - Ω/4π vs σ_opt: WEAK COINCIDENCE.  - p7 min at 1.992: METHOD (grid).
- Spherical cosine form at R=1e6: METHOD (cancellation; documented limit).  - Euler gcd None at N=221: METHOD (my formula; fixed).
- Open: why lobe shape factor flattens for s>1.05 (p6b); lobe↔GL emerger link (cusp = critical point of the circle→curve map).

## Citations (originals to verify before use)
Adler & Tanton 1980 (π_p duality), Jaynes 1957, Shannon 1948, Riemann–Siegel (Edwards, Riemann's Zeta Function), von Mises 1918, Kelvin (inversion), Lomont 2003 (fast inverse sqrt), Lorentz/Biot–Savart/Ampère/Langevin/Curie. Image: V. Ilievski zeta-spiral (SpaceClaude/riemann_spiral.webp).

## Open decisions for Cody (before any GL toolset code)
π placement across Add/Scale/Sign (proposed C/Add, A/Scale, d/Sign); include SL(2,ℝ) classifier; statistics layer same file or separate; names of the six operators (orbit/unfold/cut/fold/project/shuffle); ℓ_p family as a seventh "circle" (norm-changing).
