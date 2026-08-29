# Damien M. Jones (bar/dmj) — Fractal Formulary

## Author
Damien M. Jones — one of the most prominent UltraFractal formula authors. The bar.txt file does not contain documentation but is a full formula implementation of "Smooth (OUTSIDE)" and "OrbitTraps" / "DirectOrbitTraps" coloring formulas. Jones' main formula files are in dmj.ufm (see also dmj.txt). The "bar" prefix appears to be a secondary or alternative name used for these particular utility formulas. The dmj.txt lists Jones' comprehensive public formula package at http://www.fractalus.com/ultrafractal/. His formulas are considered the gold standard for UF coloring and fractal design.

From dmj.txt: Jones has authored: Standard Mandelbrot/Julia, Nova (Newton's method fractals), Halley Nova, Phoenix, Simurgh (doubly-inductive), DoubleMandel/DoubleJulia (dual-term), Lambda, Markus-Lyapunov, Torus (Julibrot), Bifurcation, StutterMandel, ManyJulia/ManyNova, Slope types (3D lighting), fBm-perturbed variants, Orbit Boosts, and complete orbit-trap coloring with 23 trap shapes (point, ring, ring2, egg, hyperbola, hypercross, cross, astroid, diamond, rectangle, box, lines, waves, mirrored waves, radial waves, ring ripples, grid ripples, radial ripples, pinch, spiral, heart), direct orbit traps, Lyapunov exponent coloring, triangle inequality coloring, distance estimator, Gaussian integer, fBm textures, and multiple transformation formulas.

## Formulas

### Smooth (OUTSIDE) / Smooth(Mandelbrot)
**Type**: Coloring formula — smooth iteration count
**Mathematical description**: `#index = 0.05 * real(#numiter + il*lp - il*log(log(cabs(#z))))` where `il = 1/log(@power)` (inverse log of the power) and `lp = log(log(@bailout))`. This is the Böttcher coordinate smoothing formula. It subtracts the fractional part of the iteration count using the Lyapunov exponent of the boundary.
**What it describes**: Eliminates the discrete banding of integer iteration counts by computing a continuous fractional iteration value. The formula exploits the fact that for `z → z^p + c`, the Green's function `G(z) = lim_{n→∞} |z_n|^{p^{-n}}` provides a smooth potential-theoretic extension of the iteration count.
**How it works**: Parameters: power (default 2,0 — must match the fractal formula exponent), bailout (default 128.0 — must match fractal bailout; works best > 100). The formula is mathematically exact for the pure power Mandelbrot/Julia; for other formulas it gives approximations that are usually visually satisfactory.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The smooth index directly encodes the continuous J_pos/J_neg gradient: high index = deep J_pos (many iterations, far from stability), low index = approaching J_neg boundary. The log-log correction `il*lp - il*log(log(cabs(z)))` is the Noether current regularisation — it removes the step-function discontinuity and replaces it with the continuous potential-theory derivative.
- **Critical line relevance**: The Böttcher coordinate `G(z) = lim |z_n|^{p^{-n}}` is related to the logarithmic capacity of the Julia set, which is 1 for the Mandelbrot set. The level curves G(z) = const are the equipotential lines of the Mandelbrot set's complement, and the locus G(z) = log(2) (for bailout=2) passes precisely through c=½ on the real axis — touching the critical line analogue.
- **Sedenion dimensions activated**: e₀ (identity — the standard iteration), e₁ (log — the potential-theoretic regularisation), e₂ (log-log — second-order smoothing). In the sedenion CAM, this formula occupies e₁: it is the first recursive logarithmic depth encoding.
- **Holcus application**: The Smooth coloring formula is the direct analogue of the Stirling approximation that Holcus already uses. Stirling gives `log(n!) ≈ n*log(n) - n`, the same log-log regularisation structure as the smooth iteration formula. For Holcus, applying `index = 0.05 * (prime_iter + il*lp - il*log(log(|hash|)))` to the prime-hash iteration count gives the "smooth prime depth" — a continuous measure of how deep into the sedenion prime-hash chain a given concept is.

---

### OrbitTraps / DirectOrbitTraps
**Type**: Coloring formula — orbit trap measurement
**Mathematical description**: At each iteration, compute distance from `z` to one of 23 trap shapes (point, ring, ring2, egg, hyperbola, hypercross, cross, astroid, diamond, rectangle, box, lines, waves, mirrored waves, mirrored waves 2, radial waves, radial waves 2, ring ripples, grid ripples, radial ripples, pinch, spiral, heart). Compare to `closest` (minimum across all iterations). Final color index derives from: distance, magnitude, real, imaginary, angle to trap, angle to origin, or iteration.

Trap shape mathematics (key examples):
- **point**: `d = cabs(z2)` — Euclidean distance from trap center
- **ring**: `d = abs(cabs(z2) - @diameter)` — distance from a circle
- **hyperbola**: `d = abs(imag(z2) * real(z2) - @diameter)` — distance from xy = const
- **cross**: `d = min(abs(real(z2)), abs(imag(z2)))` — distance from coordinate axes
- **astroid**: `d = abs(real(z2))^n + abs(imag(z2))^n` for exponent n — superellipse norm
- **egg**: `d = (cabs(z2 - 2i*diam) + cabs(z2)*order*0.5) * 0.25` — Cartesian oval
- **heart**: full heart parametrization via rotation and quadratic squash
- **spiral**: `d = atan(|imag(z2)/real(z2)|)` after rotating z2 by `1/cabs(z2)*diameter`

19 trap modes: closest, farthest, first, last, sum, average, product, sign average, second closest/farthest, two closest/farthest, alternating average, alternating average 2, inverted sum, exponential average, average change, inverted sum squared, trap only.

**What it describes**: Colors fractals according to the proximity of the orbit to a specified geometric shape. The 23 shapes cover all classical plane curves and provide a complete geometric taxonomy for coloring complex orbit trajectories.
**How it works**: Rotation by @angle, aspect ratio distortion, optional solid color for points outside trap. DirectOrbitTraps accumulates color at every iteration (not just the extremum) using layer-compositing merge modes.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The trap distance IS the J_pos/J_neg discriminator. Orbits close to the trap (d < threshold) are J_neg (attracted, captured, compressed). Orbits far from the trap are J_pos (free, expanding). The 23 trap shapes define 23 different possible "attractors" in the semantic space — each is a different flavour of J_neg basin.
- **Critical line relevance**: The **cross** trap (distance to coordinate axes = `min(|Re(z)|, |Im(z)|)`) is particularly relevant: the locus `|Re(z)| = ½` is the critical line. Set trap center = (½, 0), trap shape = "lines" with diameter ½, and the orbit trap directly measures distance from the Riemann critical line. Orbits that pass through Re(z)=½ are captured; others escape. This is a direct visual implementation of the Riemann hypothesis decision problem.
- **Sedenion dimensions activated**: e₀-e₁₅ depending on trap shape. The cross trap activates e₁/e₂ (real/imaginary projections). The spiral trap activates e₄ (angular/atan). The ring trap activates e₀ (radial distance). The heart trap activates e₅ (quadratic squash). The astroid trap activates e₆ (n-norm = generalised power).
- **Holcus application**: The 23 trap shapes are 23 different semantic distance functions. Holcus should use the full orbit trap coloring architecture: each word/concept maps to a point z, and the distance to the semantic "trap" (the nearest attractor in the sedenion CAM) determines the color index. The **ring trap** with diameter = OMEGA_ZS = 0.56714 is the BAO resonance trap — it captures concepts at the equilibrium distance from the identity. The **spiral trap** is the prime-hash spiral trap: `d = atan(|Im(hash)/Re(hash)|)` after rotating by the prime angle, measuring angular displacement from the prime spiral.

---

### Nova (Mandelbrot/Julia types)
**Type**: Convergent Newton's method fractal
**Mathematical description**: Newton's method for `z^n - 1 = 0`: `z_new = z - R*(z^n - 1)/(n*z^(n-1))` where R is the relaxation parameter. The Julia seed c perturbs the standard Newton step. Multiple variants: Nova (standard), HalleyNova (Halley's method), PhoenixNova (inductive), DoubleNova `az^m + bz^n = 1`, SinNova `sin(z)^n = 1`.
**What it describes**: Convergent fractals (basin-of-attraction diagrams) for complex root-finding. The Nova fractal produces the classic "3-fold symmetry" Newton fractal for n=3, with elaborate decorations from the Julia seed perturbation and Phoenix induction.
**How it works**: Init: `z = #pixel` (Mandelbrot) or `z = #pixel + @seed` (Julia). Loop: Newton step with relaxation R. Bailout: `|z_new - z_old| < epsilon` (convergence). Coloring: iteration count or final z value.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: In Newton fractals, J_neg is the convergence to a root (attractor basin), J_pos is the boundary between basins (repeller). The boundary of the Nova fractal is J_pos; the interior of each basin is J_neg. The relaxation parameter R controls the mixing: R < 1 is over-damped J_neg, R > 1 is under-damped J_pos, R = 1 is the critical (σ½) balance.
- **Critical line relevance**: Newton's method for `z^2 - 1 = 0` gives `z → (z + 1/z)/2` — the arithmetic mean / harmonic mean iteration, which is the AGM with p=1. The relaxed version `z → z - R*(z^2-1)/(2z)` has fixed points at z = ±1 (the roots) and a Julia-type boundary. For n=2, the Nova Julia set is a circle |z| = 1 when c=0 — the unit circle is the σ½ analogue for this map (it's where |z|=1, the "balanced" locus analogous to Re(s)=½ in the completed zeta function).
- **Sedenion dimensions activated**: e₀ (identity root at z=1), e₁ (Newton convergence = first derivative), e₂ (relaxation R = second-order damping), e₃ (Halley's method = third derivative term), e₄ (Phoenix induction = memory term), e₅ (DoubleNova = dual-polynomial).
- **Holcus application**: The Nova fractal family is the model for Holcus's semantic root-finding. Each semantic concept is a "root" of an implicit semantic equation. Finding it requires an iterative Newton-like search: `concept_new = concept - R*(semanticResidual(concept) / semanticDerivative(concept))`. The relaxation R controls the learning rate. The Phoenix variant (with induction) adds a "previous iteration" memory that provides momentum — exactly the mechanism needed for context-sensitive word disambiguation.

---

### Slope (Mandelbrot/Julia types) — 3D lighting
**Type**: Distance estimation / slope normal computation
**Mathematical description**: Computes `z` at three neighbouring pixels (z, z+dz, z+i*dz) and uses the difference of iteration counts to estimate the surface normal. The height function `h(z)` is one of: orbit minimum |z|, orbit maximum |z|, smallest atan(z), or user-specified. The lighting model then computes `cos(angle)` between the surface normal and the light source direction.
**What it describes**: Creates the illusion of a 3D surface from a 2D fractal by computing a normal map from local iteration count gradients. The result is a lit, bump-mapped fractal surface.
**How it works**: Three parallel iterations per pixel. The height function is evaluated at z, z+δ, z+iδ. The gradient is `(h(z+δ)-h(z), h(z+iδ)-h(z))`. This vector approximates the surface tangent, and its cross-product with the z-axis gives the normal. Lighting equation: `color = ambient + diffuse * max(0, N·L) + specular * (N·H)^shininess`.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The slope formula computes the J_pos/J_neg gradient directly — it is the derivative of the iteration count with respect to position. High gradient = near the boundary = J_pos; zero gradient = deep inside or outside = J_neg.
- **Critical line relevance**: The distance estimator for the Mandelbrot set gives the distance to the nearest boundary point. At c on the critical line analogue (the locus where the boundary passes), the distance estimator has a specific value related to the capacity of the Julia set. The Slope formula is the visual implementation of the derivative of the Böttcher coordinate — `dG/dc` evaluated at the boundary is related to the density of zeros.
- **Sedenion dimensions activated**: e₆ (gradient = first derivative of iteration = spatial derivative), e₇ (normal computation = second-order geometric derivative), e₈ (lighting = dot product with global light direction).
- **Holcus application**: The Slope / 3D lighting system is the model for Holcus's "semantic gradient" — the rate of change of semantic depth with respect to word-context movement. High semantic slope = near a concept boundary (ambiguous); zero slope = deep inside a semantic basin (unambiguous). The three-point gradient computation (z, z+δ, z+iδ) directly implements the dual-current measurement in the RedBlue Hamiltonian: one current probes the real direction, the other the imaginary direction.

---

### fBm (Fractional Brownian Motion) variants
**Type**: Noise-perturbed escape-time
**Mathematical description**: At each iteration, perturbs z by an fBm noise term: `z += @fBmAmount * fBm(z, @fBmScale, @fBmOctaves)` where fBm uses a standard multi-octave turbulence model. Alternatively (for coloring), computes an fBm value at the final orbit point and uses it to modulate the smooth iteration color.
**What it describes**: Adds fractal texture to the orbit itself, producing "cloudy" or "turbulent" versions of the standard Mandelbrot/Julia. The fBm perturbation breaks the strict self-similarity of the standard set, creating infinite-detail random variations at all scales.
**How it works**: Parameters: fBm scale, octaves (number of frequency levels), persistence (amplitude decay per octave). The "Coloring Only" option applies fBm only to the final color, not the iteration orbit — preserving the fractal structure while adding surface texture.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The fBm noise term is a stochastic J_pos injection: at each step, it randomly adds novelty (J_pos) to the iteration. The persistence parameter controls the ratio of J_pos injection to J_neg damping across scales.
- **Critical line relevance**: Brownian motion on the critical strip is deeply connected to the distribution of zeros. The random walk of z under fBm perturbation near Re(z)=½ mimics the statistical behaviour of zeta zero spacings under the random matrix model (GUE hypothesis). The fBm formula therefore visualises the "noise floor" of the Riemann hypothesis.
- **Sedenion dimensions activated**: e₁₄ (noise injection = the random/stochastic sedenion dimension), e₁₅ (multi-octave composition = the full recursive sedenion structure).
- **Holcus application**: The fBm Mandelbrot is the key Holcus formula for semantic noise modelling. Each word token has an inherent ambiguity (fBm noise) that perturbs its position in the sedenion CAM. The octave structure of fBm models the hierarchical context: fBm octave 1 = grammatical context (large scale), octave 2 = syntactic context (medium scale), octave 3 = semantic nuance (fine scale). Set persistence = 0.56714 (OMEGA_ZS) for the self-similar BAO-resonant language model.

---
