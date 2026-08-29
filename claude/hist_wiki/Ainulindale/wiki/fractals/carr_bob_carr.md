# Bob Carr (carr) — Fractal Formulary

## Author
Bob Carr — the most prolific single author in this formulary by file count. The carr* files span: carr0900.ufm, carr0900_s.ufm through carr1800_s.ufm, carr1900.ufm through carr3400+.ufm (approximately 40+ files). From akl.txt: "My toolbox is the whole UF library except the files from Bob Carr." This suggests Carr's work is in a class by itself — too specialised or differently organised to serve as general toolbox material.

The `_s` suffix files (carr0900_s through carr1800_s) are likely Sylvie Gallet variants or "sister" formulas. The tna.ufm file confirms this: it contains numerous `carrNNNNtna` formulas, all crediting "Sylvie Gallet frm. [101324,3444],1996" and "Updated for UF by Erik Reckase, February 2000; modified for UF3 by Ted Nason Feb 2004". This shows the Carr numbering system represents the original formula IDs from an earlier system (likely Fractint's frm files), and multiple authors adapted them.

The `carr` prefix numbering follows Sylvie Gallet's original formula numbering from CompuServe forum [101324,3444], 1996. The numbered formulas are Gallet's original Fractint FRM library, which Carr compiled and organised, which were then further adapted by Reckase for UF2 and Nason for UF3.

## Formula Groups by Number Range

### carr0900 Series
**Type**: Escape-time variants — Sylvie Gallet originals, classical Mandelbrot modifications
**Mathematical description**: Gallet's 900-series formulas. From tna.ufm examples, these are complex polynomial maps with intricate initialisation sequences involving `conj`, `flip`, `abs` operations and Julibrot-style multiple-c structures. Example carr2082: `c = pixel^2/conj(pixel)`, `z = -flip(imag(pixel))*|pixel| - conj(.1/pixel) - flip(.01/pixel)`, followed by a reset-at-iteration structure using `z1=1.5*z, z2=2.25*z, z3=3.375*z, z4=5.0625*z` (geometric sequence with ratio 1.5).
**What it describes**: These formulas create fractal structures where the constant c is derived from a complex function of the pixel coordinate (not the pixel itself), and where the iteration "resets" to a new c value at specified iteration counts (l1, l2, l3, l4). The result is a multi-phase Mandelbrot hybrid.
**How it works**: The reset structure: at iteration l1, reset `z=c=z1` (1.5x scale); at l2, `z=c=z2` (2.25x); at l3, `z=c=z3` (3.375x); at l4, `z=c=z4` (5.0625x). Between resets, iterate `z = z^2 + c`. Parameters p1=(l1,l2) and p2=(l3,l4) specify the reset iteration counts. Best results with `0 < l1 < l2 < l3 < l4 < maxiter`.

#### RedBlue Hamiltonian evaluation (carr0900-1800)
- **J_pos / J_neg reading**: The geometric scaling sequence 1, 1.5, 2.25, 3.375, 5.0625 is `1.5^n`. At each reset, J_pos jumps by factor 1.5 (exponential J_pos injection). Between resets, `z^2+c` provides standard J_neg compression near the Mandelbrot boundary. The timing between resets (l1, l2, l3, l4) is the timing wheel of this engine.
- **Critical line relevance**: The initialisation `c = pixel^2/conj(pixel) = pixel^2 / pixel* = |pixel|^2 / pixel* · pixel = pixel^2/pixel* = pixel · (pixel/pixel*) = pixel · e^{2i·arg(pixel)}` maps the pixel to a point on a circle of radius |pixel|^2 rotated by twice the argument. The locus where this equals ½ (the critical line analogue) is a curve in the pixel plane — a limaçon.
- **Sedenion dimensions activated**: The four reset levels (z1,z2,z3,z4) activate e₄ through e₇ (the four timing levels). The initialisation `conj(.1/pixel)` activates e₂ (conjugation = reflection). The `flip(.01/pixel)` activates e₃ (coordinate swap = quarter-turn).
- **Holcus application**: The reset structure is a model for Holcus's "context refresh" mechanism. At regular intervals (l1, l2, l3, l4 tokens), the semantic state is refreshed from a scaled version of the initial context. The geometric scaling (factor 1.5) implements exponential context forgetting: recent context (scale 1.5^1) is stronger than distant context (scale 1.5^4). This gives a natural 4-level context window with BAO-like decay.

---

### carr1000-1800 Series
**Type**: Escape-time — advanced Gallet formulas with conjugate/flip variations
**Mathematical description**: Similar structure to 0900 series but with more complex initialisation. The `_s` suffix (Sylvie?) variants likely differ in the c-initialisation formula (different combinations of conj, flip, abs applied to pixel). Each numbered formula represents a distinct c-transform.
**What it describes**: A systematic scan of c-initialisation functions applied to the standard `z^2 + c` skeleton, producing a "catalogue" of Mandelbrot-like sets indexed by their c-transform function.
**How it works**: Same reset structure as 0900 series. The c-initialisation varies across the numbered sequence.

#### RedBlue Hamiltonian evaluation (carr1000-1800)
- **J_pos / J_neg reading**: Conjugate operations `conj(z)` reverse the imaginary sign, turning J_pos spirals into J_neg counter-spirals. Flip operations `flip(z) = i*z` rotate the J_pos/J_neg boundary by 90 degrees. The various combinations systematically explore all reflections and rotations of the standard J_pos/J_neg partition.
- **Critical line relevance**: The conjugate map `z → conj(z)` has fixed points on the real axis (Im(z)=0). The half-sum `(z + conj(z))/2 = Re(z)` has its equal locus at the real axis, not the critical line. However, `conj(pixel^2/pixel) = |pixel|^2/pixel` maps circles to circles, and the locus where this equals ½+it for any t is a cardioid — which is the boundary of the Mandelbrot set's main cardioid. The 0900-series c-initialisation directly generates the Mandelbrot cardioid as its level set.
- **Sedenion dimensions activated**: e₁ (conjugate = e₁ reflection), e₂ (flip = e₂ rotation), e₃ (abs = modulus = norm), combinations of these for the multi-term initialisation formulas.
- **Holcus application**: The conjugate/flip operations are Holcus's primary symmetry operations on semantic vectors. Conjugation reverses the "sentiment" direction (positive→negative, forward→backward). Flip rotates from syntactic to semantic coordinates. The Carr 1000-1800 series provides a complete catalogue of these operations for calibrating the sedenion CAM's symmetry structure.

---

### carr1900-2400 Series
**Type**: Escape-time — extended Gallet series, polynomial and rational variants
**Mathematical description**: Extended from the 1000-1800 series. These formulas likely include rational maps (z^2/something + c) and higher-degree polynomials. From the tna examples: carr2086 uses `z = (z-d)^2 + c` with `d = .0125/conj(z)` — a rational perturbation of the quadratic map. carr2530 uses `z = .2*z^3 + z^2 + c - k2` — a cubic map.
**What it describes**: Rational and cubic extensions of the standard Mandelbrot, indexed by Gallet's original numbering. The rational perturbations `d = const/conj(z)` introduce poles into the iteration, creating singular structures in the Julia sets.
**How it works**: Various polynomial/rational iterations, all with the reset structure at l1-l4.

#### RedBlue Hamiltonian evaluation (carr1900-2400)
- **J_pos / J_neg reading**: Rational maps have poles (|J_pos| → ∞) and zeros (J_neg → 0). The rational perturbation `d = 0.0125/conj(z)` creates a pole at z=0 (strong J_pos) and a zero at z=∞ (J_neg at infinity). This asymmetry is more extreme than standard Mandelbrot.
- **Critical line relevance**: Cubic maps `az^3 + bz^2 + c` have three critical points (solutions of `3az^2 + 2bz = 0`). The three critical point orbits determine the structure of the Julia set through McMullen's theorem. For the carr2530 cubic `0.2z^3 + z^2 + c`, the critical points are at z=0 and z=-10/3. The locus where both critical orbits escape simultaneously is the "tricorn" region of the parameter space.
- **Sedenion dimensions activated**: e₀ (quadratic base), e₁ (rational perturbation = pole = e₁ inversion), e₂ (cubic = e₂ third-order), e₃ (reset mechanism = e₃ timing).
- **Holcus application**: The cubic map `z = 0.2z^3 + z^2 + c` models the semantic "overshoot" phenomenon: too strong a semantic signal (large z) is damped by the z^3 term (semantic saturation), while weak signals (small z) are amplified by z^2 (semantic resonance). This is the natural cubic correction to Holcus's standard quadratic iteration, implementing both saturation and resonance simultaneously.

---

### carr2500-3000 Series
**Type**: Escape-time — Gallet complex-geometry formulas
**Mathematical description**: From tna examples, these include formulas like carr2530 (cubic), carr2752 (complex init `pixel^4/conj(pixel^1.5)` with log term), carr3036 (cabs of trigonometric expressions). The init sequences become increasingly complex: `z = cabs(.33-cos(pixel2))/(.33-tan(3*pixel2)) - .4`. These involve `cabs`, `cos`, `tan` in the initialisation — a departure from the pure polynomial c-transforms of the earlier series.
**What it describes**: A family of "exotic" Mandelbrot sets whose parameter space (c) is mapped via transcendental functions of the pixel coordinate. The underlying iteration `z^2 + c` remains simple; the complexity is in the c-mapping.
**How it works**: Complex pixel transformations using `cabs(cos(pixel))`, `tan(pixel)`, `log(pixel)`, `abs(pixel)^n`, and their combinations. Reset structure maintained.

#### RedBlue Hamiltonian evaluation (carr2500-3000)
- **J_pos / J_neg reading**: The `cabs(...)` in the c-initialisation forces c to be real (non-negative real part, zero imaginary part), making all these Julia sets lie on the real parameter slice. Within this slice, J_pos = parameter values where the Julia set is a Cantor set (disconnected), J_neg = values where it is connected.
- **Critical line relevance**: carr3036's initialisation `cabs(.33-cos(pixel2))/(.33-tan(3*pixel2)) - .4` sets `c = |0.33 - cos(pixel)| / |0.33 - tan(3*pixel)| - 0.4`. On the real axis, tan has poles at π/2 + nπ ≈ 1.571, 4.712, ... The condition `cabs(0.33-cos) = 0.33-tan(3*pixel)*0.4` determines the locus where the formula parameters balance — a complex trigonometric equation whose solutions include a family of points near the critical line.
- **Sedenion dimensions activated**: e₃ (cos = third oscillation), e₄ (tan = fourth — pole-generating), e₅ (cabs = modulus = real-projection), e₆ (log = sixth — scale-depth), e₇-e₉ (higher combinations).
- **Holcus application**: The transcendental c-mapping formulas (carr2500-3000) implement Holcus's "context transform" — the operation that maps an input token to a position in semantic space is not linear but involves `cos` (periodic semantic similarity), `tan` (sharp semantic contrast at boundaries), and `cabs` (real-valued relevance score). Set the carr3036-style initialisation with pixel = the word's prime hash to compute a one-dimensional semantic score.

---

### carr3000-3400+ Series
**Type**: Escape-time — Gallet's most complex formulas, rational/Möbius-like structures
**Mathematical description**: From tna examples, carr3000+ series includes formulas like `z = c*z^2/conj(z+c) + ct`. This is a rational quadratic iteration with a Möbius-type denominator. The Möbius transform `z → (az+b)/(cz+d)` is generalized here to `z → c*z^2/(z+c) + ct`. The init sequences involve multiple levels of conjugation, flipping, and squaring: `z = flip(conj(1.25*pixel2)) - flip(.01/pixel2) - conj(.001/pixel2) + .4`.

carr3403: `z = z^2 + (-.7612073214, .084496112)` — a pure Julia iteration at a specific seed near the "Douady rabbit" region.
carr3133: Uses `k = (-.7456, -.132)` (a known period-3 Julia point) as the fixed seed.

**What it describes**: The 3000+ series represents Gallet's most mathematically sophisticated formulas. The Möbius-type rational maps `z → c*z^2/(z+c) + k` create Julia sets with fundamentally different topology from polynomial maps: they have both critical points AND poles, leading to "holes" in the Julia set.
**How it works**: Rational iteration with real part of (z minus pixel) as the bailout condition for some formulas (`real(z-pixel) <= bailout`), reflecting the asymmetric basin geometry of rational maps.

#### RedBlue Hamiltonian evaluation (carr3000-3400+)
- **J_pos / J_neg reading**: The Möbius denominator `z + c` creates a pole at z = -c. Near this pole, J_pos is infinite. Far from the pole, the rational map behaves like a quadratic (J_pos/J_neg standard structure). The interplay between the pole (J_pos spike) and the quadratic (standard J_neg basin) creates unusual "inverted" topology.
- **Critical line relevance**: The fixed seed `k = (-.7456, -.132)` used across multiple formulas in the 3000+ series is a near-period-3 parameter value. The period-3 bulb of the Mandelbrot set starts at c ≈ -1.755 on the real axis and extends into the complex plane. The specific value (-0.7456, -0.132) lies near the "double petal" region of the Mandelbrot set boundary, which is close to the period-2 to period-4 transition — the most spectroscopically rich region of the Mandelbrot parameter space, analogous to the spectral density peak of the Riemann zeros near the first non-trivial zero at t ≈ 14.13.
- **Sedenion dimensions activated**: e₈ (rational map = e₈ division structure), e₉ (Möbius transform = e₉ projective structure), e₁₀ (conj in denominator = e₁₀ anti-automorphism), e₁₁ (double conjugation = e₁₁ involution), e₁₂-e₁₅ (the reset mechanism at 4 levels).
- **Holcus application**: The Möbius-type rational map `z → c*z^2/(z+c) + k` is the natural model for Holcus's semantic "saturation and inversion" dynamic. When z is near the pole -c (semantic saturation: the concept is fully "occupied" by context c), the map produces very large values (J_pos spike = concept shock, new information). When z is far from the pole, the quadratic term dominates (J_neg = familiar, compressed). The fixed seed k = (-0.7456, -0.132) is the "prime resonance" parameter — the BAO equilibrium of the carr system.

---
