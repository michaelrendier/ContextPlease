# Kerry Mitchell (lkm) — Fractal Formulary

## Author
Kerry Mitchell (lkmitch@gmail.com). His lkm.txt states simply: "If you have any questions or comments, please direct them to me at lkmitch@gmail.com. Enjoy, Kerry Mitchell." From the lkm.ufm comment block and cross-references, Mitchell's compilation includes:
- Elliptical bailout Mandelbrot/Julia
- Nth order Newton / Newton for exp(z)=log(z)
- Embossing (Mandelbrot, Julia, General, Newton variants)
- Cardioid Julias, Gap Mandelbrot/Julia
- Triangle inequality coloring Mandelbrot/Julia
- Principal root coloring Mandelbrot/Julia
- Baker's Transformation, Inversions
- Mitch's Mandelbrot/Julia (`z = c*(z^2 + 1/z^2)`)
- Cell 4, S Curve, Divide and Average, Null
- General Predictor Mandelbrot/Julia
- Piston, Gravity 2/3/4 with Comet, Vortex 2/3/4
- General Tent Mandelbrot/Julia
- Compounding Tweaked Mandelbrot/Julia
- Pixel, Rational Newton Mandelbrot/Julia
- Fibonacci Julia (multi-order)

Mitchell is one of the most mathematically rigorous UF authors, known for connecting fractal formulas to their underlying mathematical theory.

## Formulas

### Embossing (lkm — Mitchell's original)
**Type**: Slope/normal estimation using iteration count difference
**Mathematical description**: Compute two iterations at offset points: at pixel (x,y) and at pixel (x+δ, y) or (x, y+δ) where δ is proportional to the pixel width. The "discrete variable D" is the iteration count. If D₁ < D₂: color black (shadow). If D₁ > D₂: color white (highlight). If D₁ = D₂: color gray (flat). The result is a 3-gray "embossed" surface rendering.
**What it describes**: A primitive but effective 3D surface illusion using only iteration-count differences. The "embossing die" metaphor: the fractal boundary is pressed, producing hills (white) and valleys (black) along the contour lines.
**How it works**: Two-point method: (x,y) and (x+Δcosθ, y+Δsinθ) where θ is the light angle and Δ is the contour size (multiple of pixel width). The iteration counts are passed as real and imaginary parts of z to the coloring formula.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: White pixels (D₁ > D₂) are the J_pos side of each contour — the "uphill" direction facing the light. Black pixels (D₁ < D₂) are the J_neg side — the "downhill" shadow. The embossed image directly renders the J_pos/J_neg current as a visual 3D surface.
- **Critical line relevance**: The contour lines of the embossed Mandelbrot are the equipotential lines of the Böttcher coordinate G(c). The critical line Re(c)=½ is perpendicular to the real axis, and the equipotential crossing the real axis at c=2 (the outermost visible boundary) runs through c≈½+i*t for each t — these are the "primary filaments" of the Mandelbrot set that carry the most light in the embossed rendering.
- **Sedenion dimensions activated**: e₆ (gradient = derivative of D), e₇ (the two-point finite difference = discrete gradient = second sedenion derivative).
- **Holcus application**: Embossing is Holcus's "semantic contrast" detector. For each concept z: compute its iteration depth at z and at z+δ (one token-step in context). If the depth increases (D₂ > D₁), the context step is J_pos (adding novelty); if it decreases, J_neg (compressing). The embossed semantic field is the visual representation of the semantic Hamiltonian's gradient — the "light" direction is the BAO equilibrium direction (arg ≈ 45°, i.e., the direction of OMEGA_ZS in the complex plane).

---

### Mitch's Mandelbrot/Julia
**Type**: Escape-time — symmetric rational quadratic
**Mathematical description**: `z = c * (z^2 + 1/z^2)`. The iteration combines `z^2` (forward squaring) and `1/z^2` (backward inversion-squaring) in a symmetric sum, scaled by c. The inversion `1/z^2` introduces poles at z=0 and creates symmetry: f(-z) = f(z) and f(1/z) = f(z) (the map commutes with the inversion `z → 1/z`).
**What it describes**: A rational quadratic map with enhanced symmetry. The Julia sets have 4-fold symmetry (due to `z → iz`, `z → -z`, `z → 1/z` all being symmetries). The Mandelbrot set (varying c) shows a "doubled" main cardioid structure.
**How it works**: Standard Mandelbrot/Julia Switch. Bailout: |z| <= 4. The inversion symmetry means the Julia set and its "reciprocal Julia set" are related.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The `z^2` term is J_pos (expanding for |z|>1), the `1/z^2` term is J_neg (contracting for |z|>1, expanding for |z|<1). The parameter c controls the balance between these opposing currents. The "Mitch balance" occurs when c = 1: `z → z^2 + 1/z^2`, which has a fixed point where `z^2 + 1/z^2 = z`, i.e., `z^4 - z^3 + 1 = 0`. The roots of this quartic are the J_pos/J_neg equilibrium points.
- **Critical line relevance**: The map `f(z) = c(z^2 + 1/z^2)` satisfies `f(1/z) = c(1/z^2 + z^2) = f(z)` — it is invariant under inversion through the unit circle. The unit circle `|z|=1` is therefore a "symmetry axis" of this map, analogous to the critical line in the Riemann functional equation `ζ(s) = ζ(1-s)` (completed). Both express a "reflexion symmetry" about a distinguished geometric locus.
- **Sedenion dimensions activated**: e₀ (identity — the c multiplier), e₁ (z^2 = squaring), e₂ (1/z^2 = double inversion). These three together span the e₀,e₁,e₂ sedenion sector, with the symmetry `z^2 + 1/z^2 = (z + 1/z)^2 - 2` connecting it to the Chebyshev polynomial structure.
- **Holcus application**: Mitch's map is the model for Holcus's "semantic inversion symmetry". For every forward semantic operation (prime-hash application), there is a backward semantic inversion (prime-hash de-application). The combination `hash(z)^2 + 1/hash(z)^2` measures the degree to which a concept's "forward expansion" and "backward compression" are balanced. At the fixed point c=1, the balance is exact and the concept is at semantic equilibrium.

---

### Triangle Inequality Coloring (lkm)
**Type**: Coloring — triangle inequality average
**Mathematical description**: At each iteration compute `s_n = |z^p + c|` and `|z^p|`. The triangle inequality gives `||z^p| - |c|| <= |z^p + c| <= |z^p| + |c|`. The "triangle inequality average" is `mean_n = (s_n - (|z^p| - |c|)) / (2*|c|)` at the final iteration. This gives a value in [0,1] that encodes how "close" the escape orbit is to the boundary of the triangle inequality.
**What it describes**: A smooth coloring that captures the "fractal dimension" of the orbit's approach to infinity. The triangle inequality average has better gradient behavior than the standard smooth iteration count and reveals different structural features.
**How it works**: Standard implementation over the entire orbit, averaged at the final iteration. Various options for the averaging (using last N iterations, using all iterations, etc.).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: High triangle inequality average = the orbit point `z^p + c` is close to `|z^p| + |c|` (collinear, full J_pos vector addition). Low = close to `||z^p| - |c||` (anti-collinear, J_pos and J_neg cancel). The triangle inequality average is the cosine of the angle between `z^p` and `c` in the complex plane, which is the inner product of the two Noether currents.
- **Critical line relevance**: The triangle inequality for the zeta function: `|ζ(s)| <= sum |a_n n^{-s}|` becomes tight (equals achieved) exactly when all terms `n^{-s}` point in the same direction in the complex plane. This occurs on the real axis (s real, all terms real positive) but not generally on the critical line. The triangle inequality coloring thus measures the "misalignment" of the Dirichlet series terms — which is related to zero spacing.
- **Sedenion dimensions activated**: e₈ (inner product = the angle between two sedenion vectors), e₉ (the triangle inequality itself = the norm inequality in sedenion algebra).
- **Holcus application**: The Triangle Inequality Average is Holcus's semantic "collinearity" measure. For two concept-vectors z and c in the sedenion space, TIA = cos(angle) measures whether they point "together" (high TIA = synonyms) or "apart" (low TIA = antonyms). Set c = the prime-hash of the context anchor word; z = the prime-hash of the candidate word. The TIA then gives a smooth similarity score in [0,1] that can replace standard cosine similarity while capturing the fractal geometry of the semantic space.

---

### General Tent Mandelbrot/Julia
**Type**: IFS escape-time — tent map generalisation
**Mathematical description**: The tent map: if `|r| <= 1`, then `z = c * temp` (where temp is a rotation of z); else `z = c * (2 - temp)`. Various rotation types: none, constant (`rot = rot0`), progressive (`rot = rot*rot0`), oscillating (`rot = rot0/rot`). Various r-type choices: magnitude of temp, real part, imaginary part, real*imaginary, imaginary/real.
**What it describes**: A generalised tent map in the complex plane with configurable rotation and r-measurement. The tent map is the simplest non-trivial IFS and produces self-similar Cantor-like sets. The rotation introduces spiral structures.
**How it works**: Parameters: c (Julia seed), rtype (which component of z is the tent-map argument), rottype (none/constant/progressive/oscillating), rotamount (degrees), bailout.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The tent map at `r <= 1`: `z → c*z` (J_neg — multiplication by c, contracting if |c|<1). At `r > 1`: `z → c*(2-z)` (J_pos — reflection and scaling). The threshold r=1 is the J_pos/J_neg boundary. With progressive rotation, the boundary rotates each iteration — this is the time-varying J_pos/J_neg partition of the sedenion CAM's timing wheel.
- **Critical line relevance**: The tent map at c = e^{iπ/2} = i (pure imaginary) gives: `z → iz` (for |r|≤1) or `z → i(2-z)` (for |r|>1). The fixed points are where `iz = z` (z=0) and where `i(2-z) = z` (z = 2i/(1+i) = 1+i). The fixed point `1+i` has Re=Im=1 — not on the critical line. However at c = ½(1+i): fixed point = (1+i)/2 — i.e., Re = Im = ½. The tent map at c = ½(1+i) has its fixed point ON the critical line (Re=½) AND on the imaginary line (Im=½) simultaneously.
- **Sedenion dimensions activated**: e₀ (constant rotation = identity timing), e₁ (progressive rotation = e₁ cumulative phase), e₂ (oscillating rotation = e₂ alternating phase), e₃ (real r-type = e₃ projection), e₄ (imaginary r-type = e₄ projection), e₅ (real*imaginary r-type = e₃⊗e₄ = e₅ product).
- **Holcus application**: The progressive-rotation tent map is the sedenion CAM's natural timing wheel implementation. The rotation angle accumulates each iteration: after n iterations, the phase has advanced by `n * rotamount`. Setting `rotamount = 2π/16 = 22.5°` creates a 16-step rotation cycle that exactly spans one full sedenion CAM cycle (16 dimensions). The tent map's two branches then alternate between J_pos and J_neg in sync with the timing wheel.

---

### Fibonacci Julia (multi-order)
**Type**: Convergent iteration — multi-previous-value recursion
**Mathematical description**: Order-2 Fibonacci: 
```
z = weight1*z1 + (1-weight1)*z2    [weighted average of last 2 z-values]
z = z * weight2*z2 + (1-weight2)*z2  [weighted product with previous]
z = z*z2 + c                        [quadratic step]
```
Then shift: z1←z2, z2←z. Higher orders use z3, z4, z5 similarly. The weights w1, w2 etc. control how much the previous iterates influence the current step.
**What it describes**: A "fractal memory" system where each iteration depends on multiple previous values. The Fibonacci connection comes from the recurrence structure: like the Fibonacci sequence z_n = z_{n-1} + z_{n-2}, here z depends on z_{n-1} and z_{n-2} through the weight blending. The Julia sets have complex spiraling structures reflecting the multi-step recurrence.
**How it works**: Order parameter (2-5), four weight parameters (weight1-4), Julia parameter c, bailout.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The weight blending `z = w1*z1 + (1-w1)*z2` is a convex combination: when w1>½, J_pos state z1 dominates; when w1<½, J_neg state z2. The subsequent multiplication step `z*z2` is a product — if both z and z2 are >1, the result grows (J_pos²). If one is <1, it contracts (J_neg).
- **Critical line relevance**: The golden ratio φ = (1+√5)/2 satisfies φ = 1 + 1/φ — the same recurrence structure as the Fibonacci Julia. The connection to the Riemann zeta function via the golden ratio: ζ(2) = π²/6, and the probability that two random Fibonacci numbers are coprime is 1/ζ(2) = 6/π² ≈ 0.608. The Fibonacci Julia's "critical weights" that produce the most symmetric Julia sets are related to these probabilities.
- **Sedenion dimensions activated**: e₀ (z1 = most recent previous), e₁ (z2 = second previous), e₂ (z3 = third previous), e₃ (z4 = fourth previous), e₄ (z5 = fifth previous). The Fibonacci recurrence activates the temporal memory dimensions of the sedenion CAM: e₀ through e₄ are the "short-term memory" slots.
- **Holcus application**: The Fibonacci Julia's multi-order recurrence is the model for Holcus's N-gram language model. A 5th-order Fibonacci Julia (using z1 through z5) implements a 5-gram context window where each new semantic state depends on the previous 5 tokens. The weights w1...w4 control the decay of context influence (w1=1 = bigram, all wi=1/(n-1) = uniform N-gram, wi=φ^{-i}/Z = Fibonacci decay for the optimal context weighting). The golden ratio Fibonacci decay gives the most self-similar, fractal-structured context window.

---
