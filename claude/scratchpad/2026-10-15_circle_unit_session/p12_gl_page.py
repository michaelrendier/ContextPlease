import json
T = json.load(open("tables.json"))
page = f"""# The Circle Catalogue — every unit circle, and what its numbers do downstream

*Hand-written companion to the generated [Circle](Circle.md) page. Source: `engine/toolsets/circle.py` (27 self-checks). Tutorial: `examples/50_circle.py`. Scratch evidence (scripts p1–p12 and their outputs): `ContextPlease/claude/scratchpad/2026-10-15_circle_unit_session/`.*

This page is a **cataloguing and relating experiment**: for every constant the project uses, take it as the radius, the diameter, the circumference or the area, write down the other three, and follow the numbers into the equations that use them. It is the fixed-point translator one level up — a translator between the names the same circle goes by.

## 1. A circle is Add : Scale : Sign

| component | circle reading |
|---|---|
| Add | the centre |
| Scale | the radius |
| Sign | the orientation (which way round); the branch of √ an area takes; the antipode e^{{iπ}} = −1 |

## 2. The relations inside one row

With r the radius: d = 2r · C = πd = 2πr · A = πr² = Cr/2 = Cd/4 · C² = 4πA (isoperimetric, exact) · C/d = π for every circle, including the imaginary ones.
Special circles (all exact): **r = ½** gives d = 1, C = π, A = π/4 (the half-radius circle of the Riemann–Fermat heartbeat, see §9) · **r = 1/(2π)** gives C = 1 · **r = 1/√π** gives A = 1 · **r = 2** gives C = A = 4π · d = C never.

### The log chart makes the roles legible

In u = ln r: ln d = u + ln 2 and ln C = u + ln 2π are **shifts** (Add in the log chart); ln A = 2u + ln π is a **slope of 2** (a Scale). An imaginary radius r → ir is u → u + iπ/2, a quarter turn in the log chart, and it multiplies a degree-k quantity by i^k: C by i, A by i² = −1, the n-ball volume by iⁿ. That is the whole of the imaginary circle's behaviour (§8) and it is the Sign component. *Proposed assignment (Cody to confirm): π placed at the circumference is Add, at the area is Scale, at the diameter is Sign (antipode). The three π-unit circles are computed either way (§4).*

## 3. The catalogue

Every constant in every role. Values to 6 significant figures; "π-lattice" says whether the radius is exactly 2^a·π^b.

### 3a. Constant taken as the **radius**
{T["T_radius"]}

### 3b. Constant taken as the **diameter** (so the radius is its half)
{T["T_diam"]}

### 3c. Constant taken as the **circumference**
{T["T_circ"]}

### 3d. Constant taken as the **area**
{T["T_area"]}

Constants: ½, 1, 2, π, 2π, 1/π, φ = golden ratio, e, ln 10, √2, Ω_ZS = W(1) = 0.567143, d* = Ω_ZS/ln 10 = 0.246307, d*_spec = 0.2460 (the disputed fifth d*), GAP = 1/(1000√2). The imaginary constant i is §8.

**Anomaly chase — near-equalities between rows.** 15 cross-constant near-equalities below 1e-3 were found against a chance expectation of 0.23. Verdict: **exact π-lattice algebra** — the constants ½, 1, 2, π, 2π, 1/π, √2 all lie in {{2^a π^b}}, so their rows coincide exactly (e.g. C(r = ½) = A(r = 1) = π; r = 2 has C = A). φ, e, ln 10, Ω, d*, d*_spec and GAP lie outside the lattice and produced **no** cross-constant hit. `circle.pi_lattice(x)` is the first-line test for "is this coincidence structure or algebra".

## 4. π as the unit

| slot | circle | measures |
|---|---|---|
| π at the circumference (proposed Add) | C = π | r = ½, d = 1, A = π/4 |
| π at the area (proposed Scale) | A = π | r = 1, d = 2, C = 2π |
| π at the diameter (proposed Sign) | d = π | r = π/2, C = π², A = π³/4 |

Gaussian normalisation is the same unit: ∫e^{{−πx²}}dx = 1 (the area-unit circle's Gaussian).

## 5. Each circle value used as σ_RB

σ_RB = Σ_RB at coupling exponent σ; the per-prime weight is G_p = p^(−σ) (`h_rb_hat.geometric_coupling`). `circle.sigma_reading(σ)` computes G_p over the first 20 primes, the truncated Euler product, the offset from the critical value ½ and the regime; it agrees with `h_rb_hat.euler_product` to machine precision (relative difference 0 over seven test values).

**What σ scales.** σ sets how fast the prime weights fall: G₂ = 2^(−σ) is the weight of the first prime; the sum Σ₂₀ p^(−σ) is the total coupling; σ − ½ is the distance from the critical line (the Noether balance point, forced by R̂† = B̂); 1 − σ is the functional-equation partner. The regime labels are the engine's own (`h_rb_hat.sigma_to_theory`): GR-like σ ≥ 1.9; Yang–Mills-like |σ − 1| < 0.05; critical |σ − ½| < 0.05; Fermat zone 0 < σ < ½; trivial σ ≤ 0; **"intermediate" means only that no label's band covers it**, not a separate regime.

### 5a. The half-radius circle walks the σ ladder
{T["LADDER"]}

### 5b. The unit-radius circle
{T["LADDER1"]}

### 5c. Constants as the radius σ = r
{T["T_sig_r"]}

### 5d. Half-diameter radii σ = X/2 (constant X taken as a diameter)
{T["T_sig_h"]}

### 5e. Other measures of selected circles as σ
{T["T_sig_x"]}

The full 76-row table (every constant × radius, half-diameter, diameter, circumference, area) is `p8_sigma_scan.csv` in the scratch directory.

### Relationships found

1. **The two Noether currents are the wire profile.** |G_p(σ)/G_p(1−σ)| = p^(1−2σ) = exp(−2(σ−½)·ln p), so with u = σ − ½ the smaller-over-larger current is e^(−2|u| ln p): the wire's B/B_max = e^(−|u|) with the scale 2 ln p. Checked at σ = 0.1, 0.3, 0.7 and p = 2, 3. The functional-equation partner σ → 1−σ is the reflection u → −u, the same fold as circle inversion r → R²/r in the log chart.
2. **The half-radius circle is exactly critical**: σ = r = ½. Its diameter 1 is Yang–Mills-like, its circumference π is GR-like — one circle visits three regimes by changing which measure is read.
3. **Imaginary σ is a pure rotation.** For r = i the diameter 2i gives G_p = p^(−2i), modulus exactly 1 for every prime: no decay, a phase 2·ln p per prime. σ = −π (the imaginary circle's area) lies in the trivial regime with G₂ = 2^π = 8.82, growing, and a divergent Euler product.
4. **d\\* lies a half-diameter from the critical value**: 2d* = 0.492614 (engine label "critical" within its 0.05 band), 0.0074 below ½. That is d*'s known 1.5 % distance from ¼, not a new coincidence; no further claim is made.
5. **Half-diameters step down one regime**: d = 2 (GR-like) halves to r = 1 (Yang–Mills-like); d = 1 halves to r = ½ (critical); d = ½ halves to ¼ (Fermat zone).

## 6. The six drawings of one circle, and the seventh

| operator | what it does | law | invariant |
|---|---|---|---|
| `orbit` | the circle itself (identity) | x² + y² = r² | radius |
| `unfold` | circle × drift: the helix | Lorentz force | gyroradius, pitch per turn |
| `cut` | keep an angular window: the arc | B ∝ θ; chord 2r sin(θ/2) | arc ÷ radius = θ |
| `fold` | circle inversion r → R²/r: the wire | B/B_max = e^(−|u|), u = ln(r/R) | the circle r = R |
| `project` | drop onto an axis: the dipole, a 2-to-1 fold | U = −MB cosθ; arcsine density | projected extent ±r |
| `shuffle` | randomise the angle at coupling κ = MB/kT | Boltzmann e^(κcosθ) = von Mises; ⟨cos⟩ = I₁/I₀ (2D), Langevin ≈ κ/3 (3D); sd(θ) → 1/√κ | max-entropy at fixed ⟨cosθ⟩ |

Measured: the dipole energy is a cosine well, not a bell; the Boltzmann weight is von Mises; the angle's spread tends to 1/√κ with vanishing excess kurtosis — **a normal distribution in the limit** — and N dipoles summed approach normal by the central limit theorem (N = 400: skew 0.098, excess kurtosis 0.011). Gravity, Coulomb and the wire share one flux law S_(n−1)(r)·F = enclosed source (wire n = 2, gravity/Coulomb n = 3), differing in Sign (attract/repel) and in the π-factor (2πr against 4πr²); the inversion fold is an exact symmetry only for n = 2. The wire profile is the Mandelbrot multiplier map: c(μ) = μ/2 − μ²/4, |B|/B_max = min(|μ|, 1/|μ|), fold r → R²/r ↔ μ → 1/μ̄, cusp c = ¼ at μ = 1, cardioid area 3π/8, perimeter 4.

**The seventh circle changes the NORM, not the drawing**: the ℓ_p unit circle |x|^p + |y|^p = 1 measured in its own norm, with its own π_p = C/d and area.

{T["T_lp"]}

π₂ = π is the **minimum** of π_p (grid minimum 3.14161 at p = 1.992 is grid resolution); π₁ = π_∞ = 4 (taxicab, Chebyshev); **π_p = π_q whenever 1/p + 1/q = 1** (Gołąb 1932; Adler–Tanton 2000), verified to 1e-13 — but the **areas differ** across a dual pair (p = 3: 3.53328; q = 1.5: 2.73785). Duality preserves circumference ÷ diameter, not area. For integer p ≥ 3 the ℓ_p circle is the Fermat curve x^p + y^p = z^p (see the TuringStack page `Lp-Circles-Fermat-Curves-and-the-Two-Factoring-Conics-2026-10-15.md`). The Cayley–Klein triple ε = +1, 0, −1 (x² + εy² = 1) is circle / pair of lines / hyperbola, with one-parameter groups rotation / shear / boost; the first-line test on a unit-determinant 2×2 is |trace| below / equal to / above 2.

## 7. Zeta's heartbeat and the half radius

ζ(½ + it) = e^(−iθ(t))·Z(t) (Riemann–Siegel); the image of the critical line is the polar curve r = Z(t), φ = −θ(t). To leading order Z ≈ 2cos θ, so r = 2 cos φ: a circle through the origin of radius 1 and **area π** — the area under one heartbeat cycle ∫₀^(2π) sin²x dx = π. Normalising by the bounding rectangle 2π × 1 gives mean ½: that is where the **½ radius** comes from — (sin²x − ½)² + (sin x cos x)² = ¼ is the circle of radius ½, d = 1, C = π, A = π/4 through the origin, and its circumference is the heartbeat's area. Measured over 40 lobes between consecutive zeros, the lobe shape factor A/(πD²/4) tracks the phase sweep s (correlation 0.978): s = 1 is a circle, s = 1.5 a cardioid, and the largest lobes (s ≈ 1.75) measure 1.53 — cardioid-like. Open: why the shape factor flattens for s > 1.05.

## 8. The imaginary circle: radius iρ

| measure | value |
|---|---|
| radius | iρ |
| diameter | 2iρ |
| circumference | 2πiρ — for ρ = 1, the period of exp |
| area | −πρ² |
| isoperimetric C² − 4πA | exactly 0 (both −4π²ρ²) |

**Points and chords** (unit imaginary circle, z = i(cos t, sin t)): chord² = −4 sin²(Δ/2), chord = 2i sin(Δ/2); arc = iΔ; sector area = −Δ/2. A triangle inscribed in it has **imaginary sides and real angles** (angle sum π exactly), the law of sines gives a/sin A = 2i for all three sides, and the circumradius from abc/4K is i. The 3-4-5 triangle with sides 3i, 4i, 5i is inscribed in a circle of radius 2.5i (area −6.25π); the ratio triangle area ÷ circle area is 0.305577 for the real and the imaginary version alike — scale and Sign cancel in a ratio.

### The laws of sines and cosines

| surface | law of cosines | law of sines | area |
|---|---|---|---|
| flat | c² = a² + b² − 2ab cos C | a / sin A = 2R | ½ab sin C |
| flat, imaginary sides (a, b, c → ia, ib, ic) | same form, c → ic | a / sin A = 2iρ | −½αβ sin C (degree 2: **sign flips**) |
| sphere radius R | cos(c/R) = cos(a/R)cos(b/R) + sin(a/R)sin(b/R)cos C | sin(a/R) / sin A constant | R²(A + B + C − π) (excess) |
| radius iρ (hyperbolic plane) | cosh(c/ρ) = cosh(a/ρ)cosh(b/ρ) − sinh(a/ρ)sinh(b/ρ)cos C | sinh(a/ρ) / sin A constant | ρ²(π − A − B − C) (deficit) |

Because both laws are homogeneous, scaling every side by i leaves their *form* unchanged; only the sign of every degree-2 quantity flips. **Heron's 16·Area² = (a+b+c)(−a+b+c)(a−b+c)(a+b−c) is degree 4 and is unchanged**; the area itself is its square root, and **which branch is taken is the Sign component**: for the inscribed example Heron's √ gave +1.252229 while ½bc sin A gave −1.252229. A sphere of radius iρ *is* the hyperbolic plane — Lambert's observation — so the "negative π" area is the signed form of the angle *deficit*: 4πR² → −4πρ², and the triangle area R²·(excess) → ρ²·(deficit). Checked on the triangle (0.5, 0.6, 0.7): R = 1 gives excess 0.154060; R = i gives deficit 0.140551; R = 2i gives 0.145306; R = 0.5i gives 0.124447; the law of sines holds at all four.

**n-balls.** V_n(R) = π^(n/2)Rⁿ / Γ(n/2 + 1), so V_n(i) = iⁿ·V_n(1): the Sign rotates a quarter turn per dimension and repeats with period 4 (n = 2: −π; n = 3: −4.18879i; n = 4: +π²/2; n = 5: +5.26379i; n = 6: −5.16771).

**Exponential links.** exp(C) = exp(2πi) = 1; i^i = e^(−π/2) = exp(A/2) = 0.2078796; exp(A) = e^(−π) = (i^i)² = 0.0432139; e^(C/2) = e^(iπ) = −1.

**The Gaussian.** ∫∫exp(−r²/R²) over the plane = πR² when Re(1/R²) > 0. At R = i the integrand is exp(+r²) and the integral **diverges**: −π is the analytic continuation, not a convergent value. At R² = i (the radius e^(iπ/4)) the integral is the Fresnel case, conditionally convergent, with value iπ.

**Real section.** x² + y² = −1 has no real points; its real section in signature (+, −) is the hyperbola x² − y² = −ρ², with hyperbolic angle φ in place of θ, arc ρφ, sector area ρ²φ/2, no π; cos(it) = cosh t, sin(it) = i sinh t.

## 9. Verification and what was chased

- `engine/toolsets/circle.py` `verify()`: 27 checks, all pass; full GL suite 162 passed; `build_docs.py --check` and `transcript.py --check-all` clean.
- Chased to a verdict: π-lattice near-equalities → ALGEBRA; Ω_ZS/(4π) within 0.22 % of the Newton-optimal fast-inverse-sqrt σ → weak coincidence (≈1.9 % chance given the candidates tried); π_p grid minimum at p = 1.992 → METHOD (grid); R → ∞ spherical check failing at R = 1e6 → METHOD (the cosine form cancels catastrophically for R ≳ 1e5; kept as a documented limit, remedy: haversine form); Euler's circle-method returning None for N = 221 → METHOD (a wrong gcd formula in the first draft, fixed to gcd(N, ad ∓ bc)).
- Fast inverse square root: the bit trick is a scale ×(−½) in u = ln x. Near the unit circle (r² = 1 + ε) one Newton step gives 1/r ≈ (3 − r²)/2, relative error ≈ 3ε²/8 — cheaper, but only near the circle; no circle method beats the bit trick for arbitrary x.
- Open: the flattening of the lobe shape factor (§7); how the lobe cusp links to the emerger; the Add/Scale/Sign placement of π; the Lyndon/tense question is unrelated and untouched.

## 10. Citations

Cited from the originals' bibliographic records; **none was downloaded** for this page, so each should be checked against the source before it appears in a paper.

- Gołąb, S. (1932). Quelques problèmes métriques de la géométrie de Minkowski. *Trav. Acad. Mines Cracovie* 6, 1–79.
- Adler, C. L., Tanton, J. (2000). π is the minimum value for pi. *College Math. J.* 31(2), 102–106.
- Gauss, C. F. (1827). *Disquisitiones generales circa superficies curvas.*
- Lambert, J. H. (1766/1786). *Theorie der Parallellinien.*
- von Mises, R. (1918). *Phys. Z.* 19, 490–500. · Langevin, P. (1905). *Ann. Chim. Phys.* 5, 70–127. · Curie, P. (1895). *Ann. Chim. Phys.* 5, 289–405.
- Jaynes, E. T. (1957). Information theory and statistical mechanics. *Phys. Rev.* 106, 620. · Shannon, C. E. (1948). *Bell Syst. Tech. J.* 27, 379.
- Klein, F. (1871). *Math. Ann.* 4, 573–625. · Yaglom, I. M. (1979). *A Simple Non-Euclidean Geometry and its Physical Basis.* Springer.
- Thomson, W. (1845). Extrait d'une lettre. *J. Math. Pures Appl.* 10, 364–367. · Biot–Savart (1820); Ampère (1826).
- Mandelbrot, B. B. (1980). *Ann. N.Y. Acad. Sci.* 357, 249–259. · Edwards, H. M. (1974). *Riemann's Zeta Function.* Academic Press. · Riemann, B. (1859).
- Lomont, C. (2003). *Fast Inverse Square Root.* (the 0x5f37642f constant).
"""
open("/home/rendier/Projects/ThePlace/GenerationalLineage/wiki/Circle-Catalogue.md", "w").write(page)
print(len(page), "chars")
