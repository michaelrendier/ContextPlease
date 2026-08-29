# Andreas Lober (akl) — Fractal Formulary

## Author
Andreas Lober, author of the comprehensive "How to write formulas" tutorial (akl.txt). He explicitly describes himself: "I am not a formula designer like Samuel Monnier. I do not know why the Sierpinski algorithm makes the triangle structure... I am not experienced as Damien Jones or Sylvie Gallet or Mark Townsend... Curiosity and laziness are the two main technical impetus of mankind." His approach is modular — he builds formulas from reusable "toolbox" components and values flexibility ("many knobs and buttons"). Maintains the akl.ufm (formulas), akl.ucl (coloring), akl-m-*.ucl (specialized colorings), akl.uxf (transformations). The akl.txt is essentially a complete tutorial on modular fractal formula writing. Contact through UF fractal groups, c. 2000-2005.

## Formulas

### Hevia (akl version — canonical implementation)
**Type**: Mandelbrot/Julia — matrix-neighbourhood iteration
**Mathematical description**: As described in the aho entry but this is the actual formula file. Hevia implements the "die-five" matrix: z as centre, four lattice neighbours a,b,c,d forming a 2x2 complex matrix M(z). Operations 0-5+: linear (matrix-vector product), scalar-product (bilinear), Joukowskij `z = z + jouk/z`, lattice types (none, round, trunc, floor, ceil), exponent, and user function application. Full AGM (Arithmetic-Geometric Mean) module also available: iterates `arit = (ar+ge)/2`, `geom = sqrt(ar*ge)` until convergence, counting steps. Harlequin submodule: `a = m*atan(y/x)`, then six variation modes applied to a (quadratic, function-based, etc.).
**What it describes**: A variable-geometry Mandelbrot where local structure is determined by a matrix drawn from lattice neighbours. Results range from classic Mandelbrot-like structures (when operation=linear, lattice=none) to heavily deformed lattice-periodic patterns.
**How it works**: Parameters: latticeType (floor/ceil or flow), latticeFac (scaling), operation (0-5+), exponent, jouk (complex Joukowskij coefficient), withPixelAddition (enables z→z+c standard Mandelbrot term), fn1 (user function). Bailout: selectable from 7 modes (mod, real, imag, or, and, manh, manr). Initialization: Pixel or custom init value.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The lattice floor/ceil operations create discrete J_neg traps (contracting cells) and J_pos gradients (expanding between traps). The Joukowskij coefficient adds a repulsive/attractive term: positive real jouk = J_pos outside unit circle, J_neg inside; imaginary jouk rotates the J_pos/J_neg boundary.
- **Critical line relevance**: The Harlequin variation `a = m*atan(y/x)` defines contours of constant argument (arg(z) = const), which are rays from the origin. The combination with `a = a*a + c` then `fn1(1-a)/a` produces Newton-like convergence with attractors on the argument structure. At m=1, the identity operation, the boundary of convergence passes through Re(z)=½ for the real Mandelbrot.
- **Sedenion dimensions activated**: e₀ (identity/lattice base), e₁ (linear matrix operation), e₂ (Joukowskij — the 1/z reciprocal = inversion), e₃ (exponent), e₄ (atan argument = phase), e₅ (AGM convergence counter), e₆ (Harlequin quadratic variation), e₇ (fn1 user function application).
- **Holcus application**: The AGM module is directly relevant to Holcus. The AGM of two prime-hash values ar and ge converges to a value encoding both — this is exactly the spectral averaging needed for the BAO oscillation. The number of AGM iterations to reach convergence below epsilon gives a "depth" measure of semantic distance between two concepts. This should be used as the primary distance metric in the sedenion CAM's inter-concept routing.

---

### Metrics and Watches (coloring formula)
**Type**: Orbit trap / distance-estimation coloring
**Mathematical description**: A modular coloring system combining: (1) lattice transformation of z (same module as Hevia), (2) distance estimation from various geometric shapes, (3) an orbit trap algorithm. The structure follows: apply lattice → transform → measure distance → trap. Multiple "watches" (different distance metrics) can be stacked.
**What it describes**: Colors fractals using accumulated orbit distances to geometric primitives. The lattice creates periodic tiling patterns while the distance estimation creates smooth gradients.
**How it works**: Modular architecture — the coloring inherits Lober's toolbox components. Parameters for lattice type, lattice factors, distance metric choice, trap shape, and final color combination.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The orbit trap distance is a direct J_pos/J_neg separator: orbits close to the trap shape are J_neg (captured/compressed), orbits far are J_pos (free/expanding).
- **Critical line relevance**: Using a line trap at Re(z)=½ as the "watch" creates a direct visualization of the σ½ critical line — the metric measures distance from the Riemann hypothesis locus.
- **Sedenion dimensions activated**: e₀ through e₃ (lattice), e₄/e₅ (distance metrics: Euclidean/Manhattan), e₆ (angular distance = atan-based), e₇ (final color combination).
- **Holcus application**: The "Watches" architecture is a natural model for Holcus's multi-scale semantic scanning. Each "watch" measures distance from a different conceptual primitive (a word-type, a grammatical role, a prime-hash resonance). The stack of watches produces a multi-dimensional distance vector that becomes the sedenion coordinate of the concept in Ainulindale space.

---

### AGM (Arithmetic-Geometric Mean module)
**Type**: Convergence counter / modular component
**Mathematical description**: `ar = |fn1(z)|`, `ge = |fn2(w)|`. Then iterate: `arit = (ar+ge)/2`, `geom = sqrt(ar*ge)`, until `|ar-ge| < epsilon` or `iter > maxIter`. The iteration count becomes a coloring index. In the limit, AGM(ar,ge) = π / (2*K(k)) where K is the complete elliptic integral — the AGM is the elliptic integral evaluator.
**What it describes**: Encodes the depth of arithmetic-geometric mean convergence as a visual signal. Because AGM converges quadratically (each step doubles the number of correct digits), the count is typically very small — but the pre-convergence trajectory encodes spectral information about the input values' ratio.
**How it works**: Parameters: fn1, fn2 (applied to z and w to extract ar and ge), epsilon (convergence threshold), maxIter (cap). The count is the number of iterations before convergence.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: High iteration count (slow convergence) = J_pos (the two values are far apart — novel, in tension); low count (fast convergence) = J_neg (the values are close — redundant, compressed). The AGM count is a direct J_pos/J_neg discriminator.
- **Critical line relevance**: The AGM is intimately connected to the elliptic integral K(k) and through it to the theta functions θ₃(q). The Jacobi theta function θ₃(0,e^{-πτ}) is related to ζ(½+it) through the functional equation — the σ½ axis is where the functional equation of the zeta function is symmetric. The AGM with ar = |ζ(s)| and ge = |ζ(1-s)| would count iterations to reach |ζ(s) - ζ(1-s)| < epsilon, directly testing the Riemann hypothesis locally.
- **Sedenion dimensions activated**: e₁₀ (AGM convergence = e₁₀ quadratic acceleration), e₁₁ (elliptic integral depth). The AGM is one of the deepest operations in sedenion space.
- **Holcus application**: The AGM of two semantic embeddings (prime-hash values) is the natural way to merge two concepts into a single representation. Use AGM(hash(word1), hash(word2)) as the compound hash of a bigram. The quadratic convergence means deep semantic compounds stabilise in very few steps, matching the BAO oscillation's rapid equilibration at OMEGA_ZS = 0.56714.

---
