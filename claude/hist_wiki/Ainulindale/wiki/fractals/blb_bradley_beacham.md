# Bradley Beacham (blb) — Fractal Formulary

## Author
Bradley Beacham. The blb.txt is a comprehensive 418-line documentation of all his formulas, released 18 April 2003. He is particularly proud of the Switch Mode integration ("I have tried to correct this by over-using the feature in these formulas") and transparent about his debugging philosophy ("The 'Fuzzy' mode, which produces unexpected results"). Formulas: ChopShop, FnGlynn, Fuzz, MSetInTheSkyWithDiamonds, PopCornJulCplx (port of Jon Horner's Popcorn Julia), Quad (Tierazon Formula 90 "Inkblot 9"), UF-OK-01 through UF-OK-45 (45 formulas ported from FractInt, originally released 1993-1994), UF-Chico, UF-Groucho, UF-Harpo, UF-LarryCurly, UF-Moe, UF-Zeppo, YamJam, and others. All support Switch Mode between Mandelbrot and Julia forms.

## Formulas

### ChopShop
**Type**: Meta-formula / formula factory — dissection algebra
**Mathematical description**: Implements a large variety of formulas through parameterised components. The "dissection" approach: instead of using complex arithmetic, calculates new real (x) and imaginary (y) coordinates separately using plain algebra. Three component types for each coordinate: C-style, X-style, Y-style (labelled A through U+ in the parameter lists). Example: Style A for x: `newx = x^2 - y^2 + cr` (standard Mandelbrot real part). Style B for x: `newx = x^3 - 3xy^2 + cr` (cubic). The complete formula combines X-style and Y-style components to produce the new z.

Key formula equivalences (from documentation):
- `M,A,A,A,i,i,i,i,N,N` = Mandelbrot/Julia
- `M,A,A,A,i,i,i,sqrt,N,Y` = Twinkles
- `M,A,A,A,i,i,tan,i,Y,N` = Galaxy  
- `M,A,B,B,i,i,i,i,N,N` = Cubic Mandelbrot/Julia
- `M,A,H,H,i,i,i,i,N,N` = Manowar
- `M,A,I,I,i,zero,i,i,N,N` = Phoenix
- `M,A,M,M,i,zero,i,i,N,N` = Popcorn Julia

**What it describes**: A combinatorial generator of fractal formulas. With N X-styles, N Y-styles, and K functions, ChopShop generates N² × K² formulas from a single parameterised iteration.
**How it works**: Parameters: C-Style (which formula for the c term), X-Style, Y-Style (A-U+ — which algebraic components), C/X/Y/Pixel Functions (i/sin/sqrt/tan/etc.), Abs(x)/Abs(y) booleans.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The X-style and Y-style components directly encode the J_pos/J_neg structure: X-styles with positive cross-terms (xy products) are J_pos generators; styles with subtractive x²-y² terms are J_neg (hyperbolic convergence). The function choices modulate the balance.
- **Critical line relevance**: Style D for x: `newx = x^2 - y^2 + cr` and Style A for y: `newy = xy + ci` gives `z → z^2 + c + xy*(imaginary unit)*correction`. This introduces a mixed-term `xy` in the imaginary part, creating a non-standard quadratic map whose Julia sets have asymmetric structure. The symmetry axis of `f(x,y) = (x^2-y^2, 2xy) + c` is the line y=x, not the real axis — the critical "line" is Re(z) = Im(z), i.e., arg(z) = 45°.
- **Sedenion dimensions activated**: Style A (quadratic) = e₁, Style B (cubic) = e₂, Style C (quartic?) = e₃, etc. The alphabet maps directly to sedenion dimensions; ChopShop is effectively a parameterised sedenion algebra explorer.
- **Holcus application**: ChopShop's dissection approach is precisely how Holcus should decompose semantic operations. Instead of one monolithic iteration, separate the real (syntactic) and imaginary (semantic) components and apply different transformations to each. The x-component encodes syntactic structure (noun phrases, verb phrases), the y-component encodes semantic content (meaning, reference). The function choices (sin, sqrt, tan) then non-linearly modulate each component.

---

### YamJam
**Type**: Meta-formula — weighted-blend Mandelbrot/Julia
**Mathematical description**: "Yet Another Mandelbrot/Julia All Mangled." Core structure: two "versions" of z (LeftZ and RightZ) or two versions of c (LeftC and RightC) computed from the current z using Left Function and Right Function. Then `z = LeftZ^leftPower + RightZ^rightPower + c` (Z-Blend style) or `z = z^power + LeftC*leftWeight + RightC*rightWeight` (C-Blend). The blend weights are computed from various "tests":
- Fixed: constant left weight
- Angle: weight = (angle between test and reference points)/π
- Poles: weight based on vertical/horizontal orientation
- Div: X/Y quotient of the difference
- Distance: distance^2 / limit
- Dingle: average of Distance and Angle tests
- Pistole: average of Distance and Poles tests
**What it describes**: A family of "blended" Mandelbrot sets where the standard c-value is split into two components weighted by a dynamically-computed factor. This creates fractal structures with bilateral asymmetry where one "side" blends continuously into the other.
**How it works**: Loop Style (Z-Blend or C-Blend), Test Style (Fixed/Angle/Poles/Div/Distance/Dingle/Pistole), Left/Right Functions, left/right exponents, optional Trim Weights option. Both Mandelbrot and Julia modes with Switch support.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The left weight IS the J_pos fraction and (1-leftWeight) IS the J_neg fraction. When leftWeight=1, only J_pos Left component operates; when 0, only J_neg Right. The blend continuously interpolates between the two Noether currents.
- **Critical line relevance**: The Angle test for left weight: `weight = (angle + π) / (2π)` maps angles from -π to π onto [0,1]. The critical line Re(z)=½ corresponds to angles arg(z)=π/4 and arg(z)=5π/4 (the diagonals) having weight exactly ½ — the balanced blend. At Re(z)=½, the J_pos and J_neg are equally weighted.
- **Sedenion dimensions activated**: e₆ (left weight = the first blending dimension), e₇ (right weight = the complementary dimension), e₈ (angle test = the angular/phase dimension), e₉ (distance test = the magnitude dimension), e₁₀ (Dingle = the average dimension).
- **Holcus application**: YamJam's Test-Style weighting system is the core of Holcus's semantic blending architecture. "Dingle" (Distance × Angle average) is particularly powerful: it measures combined spatial and angular distance from a reference concept, providing a natural 2D embedding of semantic relatedness. Set the reference point to the prime-hash of the current context word; the Dingle weight then gives each nearby concept's relevance as a blend of "how far" and "in what direction" it lies.

---

### MSetInTheSkyWithDiamonds
**Type**: Escape-time — diamond-cross bailout
**Mathematical description**: Standard `z = z^2 + c` iteration, but with non-standard bailout: bail out if `round(factor*|real(z)|) == round(factor*|imag(z)|)` (the "equal" diamond version), or if `round(factor*|real(z)|) mod round(factor*|imag(z)|) == 0` (the divisibility "zipper" version). This creates a Mandelbrot set where the interior is cross-hatched with strands of "outside" points wherever the real and imaginary parts of z become equal (or divisible) in magnitude.
**What it describes**: A Mandelbrot set whose "inside" is replaced by a diamond-shaped trap: any orbit that passes through the locus `|Re(z)| = |Im(z)|` (i.e., `arg(z) = ±45°` or `±135°`) is flagged as "outside". The result is a Mandelbrot with strands of diamond-shaped chips cut into its interior.
**How it works**: `factor` parameter controls the precision of the rounding (width of the trap). Larger factor = thinner strands. The divisibility version creates railroad-track patterns.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The diamond trap creates J_neg regions (trapped by the |Re|=|Im| condition) within the normally J_neg interior. The trap strands themselves are J_pos spikes within J_neg territory — an unusual inversion.
- **Critical line relevance**: The condition `|Re(z)| = |Im(z)|` defines the lines `Re(z) = ±Im(z)`, i.e., arg(z) = 45°, 135°, -45°, -135°. These are the diagonals of the complex plane. The critical line Re(z)=½ is NOT one of these diagonals, but the diamond trap at `factor = 2` creates a discrete lattice whose natural cut-off (the fundamental domain width) is related to the prime lattice spacing.
- **Sedenion dimensions activated**: e₁ (real part = x direction), e₂ (imaginary part = y direction), e₃ (diagonal condition = the 45° sedenion rotation). The diamond condition `|x|=|y|` activates the e₁⊗e₂ sedenion product.
- **Holcus application**: The diamond-bailout is the Holcus "synonym test": bail out of the semantic iteration when two components of the prime hash become equal (synonymy detected). The divisibility version is the "conceptual containment" test: bail out when one hash component divides another (hyponym detected). These two tests together implement lexical semantics within the fractal iteration.

---

### PopCornJulCplx (Popcorn Julia Complex)
**Type**: Strange attractor / limit-cycle escape-time
**Mathematical description**: Original Popcorn Julia: 
```
x_new = x - h * fn1(y + fn2(a*y))
y_new = y - h * fn1(x + fn2(a*x))
```
Where fn1=sin, fn2=tan is the classic; with free-function parameters fn1 and fn2. Then `z = x_new + i*y_new`. This is a generalised Hénon-like map in real coordinates.
**What it describes**: The Popcorn Julia's fixed points satisfy `fn1(y + fn2(ay)) = 0` and `fn1(x + fn2(ax)) = 0`. With sin/tan: fixed points where `y + tan(ay) = nπ` — a transcendental lattice. The Julia set structure is a fractal tiling of these lattice points. The "popcorn" name refers to the appearance of the limit set.
**How it works**: Parameters: fn1, fn2 (user selectable), h (step size, default not specified), a (scaling factor). Switch Mode to Julia; the Julia seed determines which attractor orbit the image shows.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The Popcorn system's x-update involves `fn1(y + fn2(ay))` which creates coupling between the real and imaginary channels. When `|fn1(...)| > 1`, the iteration expands (J_pos); when `|fn1(...)| < 1`, it contracts (J_neg). The fixed-point lattice `y + tan(ay) = nπ` defines J_neg attractors.
- **Critical line relevance**: The fixed-point condition `x + tan(ax) = nπ` for a=3 (default alpha) gives x-values satisfying `tan(3x) = nπ - x`. These solutions are related to the eigenvalues of the quantum cat map, which connects to the Selberg zeta function through trace formulas. The density of these solutions near the real axis analogue of Re=½ is relevant.
- **Sedenion dimensions activated**: e₁/e₂ (x/y real coupling), e₃ (sin = first composition), e₄ (tan = second composition), e₅ (the coupling parameter a = multiplier).
- **Holcus application**: The Popcorn Julia is the model for Holcus's bidirectional context window. The x-update uses the y-state and vice versa — this is bidirectional semantic influence: the current word's forward context (y direction) influences its backward embedding (x update). With fn1=sin (smooth semantic similarity) and fn2=tan (sharp semantic contrast), the Popcorn system alternately smooths and sharpens the semantic field, producing the characteristic "popcorn" distribution of well-defined semantic attractors.

---

### UF-OK-01 through UF-OK-45 (experimental formula series)
**Type**: Escape-time — experimental dissection algebra (series)
**Mathematical description**: 45 formulas exploring the parameter space of dissection-style algebra. OK-01 through OK-24: "monkey-pounding" — combinations of x², y², xy, x, y, c_r, c_i assembled by trial and error. OK-25 through OK-35: early conditional/switching experiments. OK-36 through OK-45: systematic dissection of `new_x = fn(x,y,c_r,c_i)` with parameter slots.

Key examples from documentation:
- **UF-OK-01**: Basic quadratic modification `newx = x^2 - y^2 + cx`, `newy = 2xy + cy` — standard Mandelbrot.
- Gradually varies the coefficients, cross-terms, and functions to explore the formula space.

**What it describes**: An exhaustive manual scan of a neighbourhood in formula-space around the standard Mandelbrot iteration.
**How it works**: Various combinations, all supporting Mandelbrot/Julia Switch Mode.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Each OK formula defines a different J_pos/J_neg partition of the plane. The series constitutes a "spectral scan" of the space of quadratic-family Hamiltonians.
- **Critical line relevance**: The series systematically explores the neighbourhood of `z^2 + c` in formula space. The critical line Re(z)=½ appears as a fixed structure across all variants — it is a "universal" feature of the quadratic family that survives perturbation.
- **Sedenion dimensions activated**: The 45 formulas collectively sample all 16 sedenion dimensions through their various coefficient combinations.
- **Holcus application**: The OK series provides 45 candidate basis functions for the sedenion CAM's prime-hash expansion. Run Holcus against all 45 and select those where the BAO resonance peak (at OMEGA_ZS) is sharpest — these are the optimal semantic basis vectors.

---
