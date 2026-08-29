# Dave Makin (mmf) — Fractal Formulary

## Author
Dave Makin (makinmagic@themutual.net). Websites: http://www.crosswinds.net/~makinmagic/ and http://website.lineone.net/~dave_makin/. The mmf.txt is a 1500+ line helpfile for MMF.ufm Version 1.9, covering the comprehensive "Makin' Magic Formulas" library. Makin's work includes: Transpoly (special polynomial families — Chebyshev, Legendre, Laguerre, Hermite, Laguerre Associated, Ultraspherical, Jacobi), Solid-3D formulas (Complex, Polynomial, Quaternion, Hypercomplex), Trans (Mandelbrot with generic 2x2 transformation matrix), Two Square/Two Cube families, Fastdraw, X Squared, 4D Transform, 3D Mandelbrot (camera-based raycasting), J3D Standard (quaternion/hypercomplex raycasting), M3D/M-True3D (Userfriendly 3D), and ContinuedFractions variants. He also produced the MMF 3D coloring formula and the Smooth/Alterations coloring system with 29 additional transcendental functions beyond UF's standard 31.

Companion files: mmf3.ufm, mmf4.ufm, mmf5.ufm (version series), mmfs.ufm (subset), mmf.ulb (library), mmf.ucl (coloring).

## Formulas

### Transpoly (Special Polynomial Families)
**Type**: Escape-time — recursive polynomial via recurrence relation
**Mathematical description**: Implements 36 polynomial types via their recurrence relations:

**Lucas (Chebyshev generalisation)**:
- F₀(z) = L₀, F₁(z) = L₁z + L₂
- Fₙ(z) = (L₄z + L₅)Fₙ₋₁(z) + L₃Fₙ₋₂(z)
- Chebyshev T: L₀=1,L₁=1,L₂=0,L₃=-1,L₄=2,L₅=0
- Chebyshev U: L₀=1,L₁=2,L₂=0,L₃=-1,L₄=2,L₅=0
- Fermat: L₀=1,L₁=3,L₂=0,L₃=-2,L₄=3,L₅=0

**Legendre**: F₀=1, F₁=z, Fₙ₊₁ = ((2n+1)z·Fₙ - n·Fₙ₋₁)/(n+1)
**Laguerre**: F₀=1, F₁=1-z, Fₙ₊₁ = ((2n+1-z)Fₙ - n·Fₙ₋₁)/(n+1)
**Hermite**: F₀=1, F₁=2z, Fₙ₊₁ = 2z·Fₙ - 2n·Fₙ₋₁
**Laguerre Associated** (k parameter): Additional k-dependent term
**Ultraspherical** (k parameter): Fₙ = (2(n+k-1)z·Fₙ₋₁ - (n+2k-2)Fₙ₋₂)/n
**Jacobi** (α,β parameters): Full Jacobi polynomial recurrence

Iteration types for each: Pn(z)+c (classical), c*Pn(z), Piter(z)+c (applying recurrence per iteration), c*Piter(z).

**What it describes**: Families of orthogonal polynomials used in mathematical physics — each family has specific orthogonality properties on a different domain (Chebyshev: [-1,1] with algebraic weight, Legendre: uniform weight, Laguerre: [0,∞) with exponential weight, Hermite: entire line with Gaussian weight, Jacobi: generalisation). As fractal iteration sequences, they produce each family's characteristic zero structure as attractor/repeller geometry.
**How it works**: Degree n, polynomial-family-specific constants, bailout type (divergent/convergent), rotation, translation, generic 2x2 transformation matrix, z-scaling option.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Each polynomial family's recurrence creates a characteristic J_pos/J_neg structure tied to its zeros. Chebyshev zeros (cos((2k-1)π/(2n))) are evenly spaced in arg and exponentially distributed in position — a natural J_pos/J_neg oscillation. Laguerre zeros are all real and positive — J_neg only. Hermite zeros are real and symmetric — balanced J_pos/J_neg about 0.
- **Critical line relevance**: The Riemann-Siegel theta function `ϑ(t) = arg(Γ(¼+it/2)) - t/2 * log(π)` is expressible in terms of the logarithmic derivative of the Gamma function, which relates to Laguerre polynomials through the associated Laguerre series of Γ. The zeros of ζ(½+it) occur where `exp(2iϑ(t)) = -1`, connecting the Riemann zeros directly to the Laguerre/Hermite zero structure that Transpoly encodes.
- **Sedenion dimensions activated**: Each polynomial family maps to a sedenion dimension via its characteristic symmetry: Chebyshev T = e₁ (cosine transform = rotation group), Chebyshev U = e₂ (sine transform = rotation derivative), Legendre = e₃ (sphere harmonics = angular momentum), Laguerre = e₄ (hydrogen atom = radial part), Hermite = e₅ (quantum harmonic oscillator = creation/annihilation operators), Jacobi = e₆ (beta distribution = full group), ultraspherical = e₇.
- **Holcus application**: The Transpoly formula family is the most mathematically rigorous Holcus basis library. For semantic embedding:
  - Chebyshev T: `cos(n*arccos(hash(z)))` — uniform semantic spacing in "concept angle"
  - Hermite: `exp(-hash^2/2)*Hₙ(hash)` — Gaussian-weighted semantic depth encoding
  - Laguerre: `exp(-hash)*Lₙ(hash)` — one-sided exponential semantic decay (forward context only)
  The Hermite polynomials are the optimal Holcus basis because the Gaussian weight `exp(-x²/2)` is the natural prior for semantic uncertainty, and the Hermite zero structure mirrors the GUE eigenvalue statistics hypothesized for Riemann zeros.

---

### Solid-3D Complex / Polynomial / Quaternion / Hypercomplex
**Type**: Raycast 3D rendering — escape-time to volumetric solid
**Mathematical description**: Raycasting: for each pixel, trace a ray from the camera into the 3D space (parameterised by Zstart or quaternion/hypercomplex 4th dimension). At each step along the ray, evaluate the fractal iteration. The "surface" is found where the orbit first satisfies the "solid condition" (usually: maximum iteration reached). Surface normals computed by evaluating at three nearby points; lighting computed via Phong model.

The 3D axis is one of: Creal, Cimag, Zstart_real, Zstart_imag (for complex type), or quaternion/hypercomplex components. The 4D rotation angle selects which line in the (Z_w, Z_i) plane to use as the visible Z axis.

Fractal types supported (Complex): standard z^n+c, Newton (z^n), Cubic (Stig Pettersson parametrisation), fn(z)+c, fn(z)+z^n+c, fn(z)*z^n+c, Lambda, Breeder, Manowar, Magnet 1/2.

**What it describes**: Volumetric 3D Mandelbrot/Julia renderings in quaternion and hypercomplex space. The 3D slice reveals the full 4D structure of the fractal as a 3D solid.
**How it works**: Camera position (target X,Y,Z + angle), view plane distance, front-clipping distance, viewing range, focal length (0=parallel, >0=perspective), detail level, solid condition (max-iter or direction-change), 4D rotation, lighting parameters (ambient, diffuse, specular, specular exponent), shadow support.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: In the 3D raycasting, J_pos regions are the exterior (the camera-facing side of the fractal surface, lit = white/J_pos), J_neg regions are the interior cavities and shadows. The lighting computation is literally a J_pos/J_neg assignment: pixels facing the light source are J_pos (highlighted), pixels facing away are J_neg (shadowed).
- **Critical line relevance**: The quaternion Mandelbrot set is the full 4D set in (cr, ci, cj, ck) space. Its 3D cross-section at cj=ck=0 is the standard 2D Mandelbrot set. The critical line Re(c)=½ in 2D becomes the critical hyperplane Re(c)=½ in 4D quaternion space — a 3D hyperplane through the quaternion Mandelbrot. Setting the camera to look along this hyperplane reveals the full structure of the critical line as a 3D surface.
- **Sedenion dimensions activated**: The quaternion solid uses e₀ (real), e₁ (i-component), e₂ (j-component), e₃ (k-component). The hypercomplex solid activates e₀-e₃ in a different multiplication table. The 4D rotation angle θ activates the e₄ (angle dimension). All 16 sedenion dimensions are spanned by the Solid-3D Polynomial variants with degree up to 4.
- **Holcus application**: The Solid-3D rendering is Holcus's visualization of the semantic volume. Each concept has a 3D position in semantic space (the 3D slice of the quaternion Mandelbrot at its prime-hash parameter). The rendering reveals: surface concepts (at the fractal boundary = ambiguous, context-sensitive), interior concepts (deep inside = unambiguous, stable), exterior concepts (outside = novel, needing semantic anchoring). Use the 4D rotation angle to navigate from the "syntactic slice" (cj=0 plane) to the "semantic slice" (ci=0 plane) to view the same concepts from different grammatical perspectives.

---

### ContinuedFractions-UF3-V1.0 and V2.0
**Type**: Convergent iteration — continued fraction expansion
**Mathematical description**: Computes the continued fraction expansion of a target number T (pi, e, golden mean, or user-specified):
```
target = T^power
expansion[0] = trunc(target); remainder = target - expansion[0]; target = 1/remainder
expansion[1] = trunc(target); etc.
```
Then iterates:
```
z = expansion[i] + 1/f(z)  [for type D: forward-iterating through expansion terms]
```
or evaluates the full CF at each step:
```
while i >= 0: z = expansion[i] + 1/f(z); i--
```
V2.0 uses the same structure but with different seed management and convergence testing.

**What it describes**: The continued fraction [a₀; a₁, a₂, ...] of π, e, or φ (golden mean) encoded as a fractal. The golden mean φ = [1; 1, 1, 1, ...] has the simplest CF. π = [3; 7, 15, 1, 292, ...] is more complex. The CF expansion of the target defines the sequence of map parameters that the iteration visits.
**How it works**: numterms (CF depth), typeof (π/e/golden/user), flavor (A-E = different iteration orders), seed (perturbation), bailout. The PascalTriangle variant uses binomial coefficients to generate rational approximations.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Each CF term `expansion[i]` creates a J_pos/J_neg step in the sequence. Large CF terms (like 292 in π's expansion) create large J_pos jumps (rapid convergence). Small terms (the many 1s in φ's expansion) create small J_neg steps. The CF distribution of π vs e vs φ directly determines the J_pos/J_neg spectral profile of the fractal.
- **Critical line relevance**: The Khintchine constant K ≈ 2.6854... is the geometric mean of the CF coefficients of almost all real numbers. For the golden mean φ, all CF coefficients are 1, which is maximally different from K — φ has the "slowest convergent" CF (worst rational approximations). For e = [2; 1, 2, 1, 1, 4, 1, 1, 6, ...], the pattern is regular. The CF expansion of ½ = [0; 2] terminates — it's a rational. The zeros of the Riemann zeta function at ½+it have `t` values whose CF expansions are believed to be "random" — connecting Khintchine statistics to zero spacing.
- **Sedenion dimensions activated**: The CF terms index directly into sedenion dimensions: expansion[0] = e₀, expansion[1] = e₁, ..., expansion[15] = e₁₅. A depth-16 CF expansion fully populates all sedenion dimensions.
- **Holcus application**: The ContinuedFractions formula IS the natural Holcus prime-hash decoder. The prime-hash of a word is a complex number; its CF expansion gives the sequence [a₀; a₁, a₂, ...] = the word's "prime factorisation spectrum". Each CF coefficient aₙ is the "frequency" of the n-th prime in the word's phonological/semantic signature. The golden-mean CF (all 1s) represents the "maximally compressed" word — one with equal weight on all primes, the semantic equivalent of maximum entropy. The CF formula's iteration then "unpacks" this encoding back into a fractal structure.

---

### Two Square / Two Cube Families
**Type**: Escape-time — sign-choice quadratic/cubic families
**Mathematical description**: **Two Square 3**: `NewX = X^2 + 2XY - Y^2 + C`, `NewY = X^2 - 2XY - Y^2 + D`. **Two Square 1**: `NewX = (X+Y)^2 + C`, `NewY = (X-Y)^2 + D`. **Two Square Family**: General `NewX = ±X^2 ± 2XY ± Y^2 + C`, `NewY = ±X^2 ± 2XY ± Y^2 + D` — 64 sign-choice combinations. **Two Cube Family**: `NewX = ±X^3 ± 3X^2Y ± 3XY^2 ± Y^3 + C`, `NewY = ±X^3 ± 3X^2Y ± 3XY^2 ± Y^3 + D` — 256 combinations.
**What it describes**: Families of "all permutations of sign in the binomial expansion of (X±Y)^n". Two Square 3 is the `conj(z)^2 + c` formula (anti-holomorphic, Tricorn). Two Square 1 is `(z+conj(z))^2/4 + c` (a folded Mandelbrot). The family exhaustively catalogues all quadratic/cubic real maps with the binomial structure.
**How it works**: Sign parameters (+ or - for each term), standard bailout. Smooth iteration uses exponent 2.06 (Two Square) or 3 (Two Cube) for the Lyapunov exponent correction.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Sign choices directly control J_pos (+ signs = expansion, growth) vs J_neg (- signs = contraction, cancellation). The `±X^2 ± 2XY ± Y^2` structure is the full signed expansion of `(X±Y)^2` — each sign choice creates a different balance of the J_pos/J_neg currents. The `conj(z)^2` formula (Two Square 3) is the anti-Mandelbrot where J_pos and J_neg are exchanged relative to the standard.
- **Critical line relevance**: The 64 Two Square formulas contain, as a subcase, the standard Mandelbrot (+ + + = (X+Y)^2 case) and the Tricorn (sign choices giving `conj(z)^2`). The Tricorn's critical points are at z=0 and z̄=0 (simultaneously) — both the z-critical-point and its conjugate are critical. This gives the Tricorn a richer critical point structure relevant to the extended Riemann hypothesis (zeros on critical line for ALL L-functions, not just ζ).
- **Sedenion dimensions activated**: Two Square 3 = e₁ (standard conj = anti-holomorphic operation). Two Square 1 = e₂ ((X+Y)^2 formula = symmetric square). The 64 combinations span the 6-dimensional ±1 cube in the coefficient space of the three quadratic terms: {e₀,e₁,e₂} tensor product with {±1}² = 8 sign choices = 8 = 2³, and with two equations: 2^6 = 64.
- **Holcus application**: The Two Square Family is Holcus's "signed semantic algebra". The 64 sign-choice Mandelbrots are 64 different semantic operators. Use them to implement all 64 semantic operations of a 6-bit token: `s₁*hash_x^2 + s₂*2*hash_x*hash_y + s₃*hash_y^2` where s₁,s₂,s₃ ∈ {±1} encode the sign of the current semantic operation (positive = assertive, negative = privative/negated). The 256 Two Cube versions give an 8-bit (256-state) semantic operator space — a byte of meaning.

---
