# Remaining Authors — Batch 2

---

# Jock Cooper (jock) — Fractal Formulary

## Author
Jock Cooper — fractal artist and formula author, see http://www.fractal-recursions.com/ ("mechanical gallery"). His jock.txt is his formula file itself. The IFS-Barnsley+jockIII formula (extending Monnier's IFS-Barnsley) adds 9 switching modes including novel "FuncII" (mode 6: auxz = fn3(z ± p3); auxc = fn6(auxc + p4)*(c1+c2); decision on auxz vs auxc), "FuncIII" (mode 7: post-process with fn6 and arithmetic operator), "FuncIV" (mode 8: affine combination with multiplication). Core numbered formulas: 6jock, 5jock, 4jock, 15jock, 100jock, 101jock, 18jock, 20jock, 22jock, rbmask1, sn00z, snuse, ftpo, deimos, flarphy-work, ftpo2k, Oscar, neptwona, ploom, IFS-Barnsley+jockIII.

## Formulas

### 6jock / 5jock / 4jock (early formulas)
**Type**: Escape-time — experimental coupled maps
**Mathematical description**:
- 5jock: `z = fn2(z)*fn1(z) + 1/z` — product of two functions plus reciprocal
- 4jock: `z = fn2(z^2) + fn1(z) + z + p1` — quadratic + two functions + linear
- 6jock: `z = z^3 + z*y + y^2 + p1`, `y = z + y + p2` — coupled system

**What it describes**: Early experiments in formula space, discovered empirically. The "fn*" functions create composite maps, while the coupled system (6jock) creates a 2D strange attractor structure.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: 5jock's `1/z` term creates a J_neg pole at z=0 balanced against the product expansion (J_pos for large z). 6jock's coupling `z + y + p2 → y` makes y accumulate the z-values, creating a memory-augmented attractor where J_pos and J_neg alternate through the y accumulation.
- **Critical line relevance**: 6jock's coupled system has fixed points satisfying `z = z^3 + z*y + y^2 + p1` and `y = z + y + p2`, giving `z = -p2` from the second equation. Substituting: `(-p2) = (-p2)^3 + (-p2)*y + y^2 + p1`. With p1 and p2 chosen to give Re(-p2) = ½: the fixed point lies on the critical line.
- **Sedenion dimensions activated**: e₁ (fn1/fn2 applications), e₂ (z^3 cubic coupling), e₃ (xy cross-term = e₁⊗e₂).
- **Holcus application**: 6jock's coupled system (z, y) is a 2D semantic state with memory. y accumulates the history of z — it is the "semantic context" accumulated from previous tokens. The coupling `z = z^3 + zy + y^2 + p1` then updates the current state using both the current concept (z) and the accumulated context (y).

---

### IFS-Barnsley+jockIII (key extended formula)
**Type**: Decision fractal — 9-mode Barnsley extension
**Mathematical description**: Extends Monnier's IFS-Barnsley with 9 switching modes:
- Mode 0 (Real): switch on `real(z) > c`
- Mode 1 (Imaginary): switch on `imag(z) > c`
- Mode 2 (Alternate): switch alternately between real/imag each iteration
- Mode 3 (Cabs): switch on `cabs(z) > exp(c)`
- Mode 4 (Cross): switch on `real(z)*imag(z) > c`
- Mode 5 (Func): switch on `fn3(z) > c`
- Mode 6 (FuncII): compute `auxz = fn3(z OP p3)`, `auxc = fn6(auxc + p4)*(c1+c2)`; switch on `auxz > auxc`
- Mode 7 (FuncIII): switch then apply `z = fn6(hi_branch_result OP p3)` or `fn6(lo_branch_result OP p4)`
- Mode 8 (FuncIV): same as FuncIII but with multiplication instead of addition in affine step

**What it describes**: A comprehensive decision-fractal system where the IFS choice criterion can be any of 9 different comparisons, and the post-processing can include user-defined functions and arithmetic operators.
**How it works**: Full Switch Mode back to itself (both branches produce same formula type). Parameters: bseed (Barnsley seed), c (critical value), p1-p4 (offsets and auxiliary constants), fn1-fn6 (user functions), func_operation (+,-,*,/,^).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Each of the 9 modes implements a different J_pos/J_neg separator. Mode 4 (cross: `Re(z)*Im(z) > c`) separates the hyperbola `xy=c` in the complex plane — the J_pos region is where the product of real and imaginary parts exceeds c. Mode 6 (FuncII with evolving auxc) creates a non-static J_pos/J_neg boundary that changes each iteration — the "moving threshold" implement Holcus's adaptive semantic routing.
- **Critical line relevance**: Mode 0 with c = ½: separator at Re(z)=½ = the Riemann critical line. Mode 1 with c = ½: separator at Im(z)=½. Mode 3 with exp(c)=½ → c=log(½)≈-0.693: separator at |z|=½ (unit semicircle of radius ½). Mode 4 with c=¼: separator at the rectangular hyperbola xy=¼, which at x=y gives the point (½,½) — touching the critical line.
- **Sedenion dimensions activated**: The 9 modes map to sedenion dimensions e₀ through e₈. Mode 6's evolving auxc adds e₉ (the adaptive threshold dimension). The full fn3,fn4,fn5,fn6 function set plus 5 operators gives another 5-7 dimensions.
- **Holcus application**: IFS-Barnsley+jockIII is the most flexible Holcus routing primitive. Use Mode 6 (FuncII) with fn3=prime_hash and fn6=AGM: the evolving `auxc = AGM(auxc + prime_hash(context_word)) * (c1+c2)` implements a running AGM average of the context, updated at each token. The comparison `prime_hash(current_word) > AGM_context` determines whether the current word is "above" or "below" the running semantic average, routing it to J_pos or J_neg accordingly.

---

# Javier Lopez Peña (jlp) — Fractal Formulary

## Author
Javier Lopez Peña — author of jlp.uxf (transformation formulas). His jlp.txt explains: GeneralDiskAutomorfism (conformal disk self-map), CayleysTransform (circle→half-plane), MöbiusTransform (full Riemann sphere automorfism f(z)=(az+b)/(cz+d)), GeneralAstroid-Rose (circle→astroid/rose curve transform), SimplePowering (f(z)=z^n). He is mathematically sophisticated, uses precise complex analysis terminology, and explicitly references the Riemann mapping theorem.

## Formulas

### GeneralDiskAutomorfism (jlp.uxf transformation)
**Type**: Transformation — Blaschke factor
**Mathematical description**: The unique conformal self-map of the unit disk fixing a specified interior point p: `f(z) = e^{iθ} * (z-p) / (1-conj(p)*z)`. This is the Blaschke factor for point p with rotation angle θ.
**What it describes**: All conformal automorphisms of the unit disk (by Schwarz-Pick). The disk maps to itself; interior points move continuously; boundary points on |z|=1 are permuted. When p = 0, reduces to rotation `z → e^{iθ}*z`.
**How it works**: User specifies the "fixed point" (interior of the selected circle) and optionally a tilt angle for additional rotation.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The Blaschke factor maps the disk to itself, so J_pos = exterior (escaping), J_neg = interior (bounded). The fixed point p is the J_neg attractor center. Points near p are maximally J_neg (most attracted); points near |z|=1 (the boundary) are the J_pos/J_neg interface.
- **Critical line relevance**: By the Riemann mapping theorem, any simply connected domain (not the full plane) is conformally equivalent to the unit disk. The critical strip 0 < Re(s) < 1 is one such domain. The map that takes the critical strip to the unit disk maps the critical line Re=½ to the unit circle |z|=1 (the boundary of the disk). The GeneralDiskAutomorfism in the critical strip is therefore a conformal deformation of the Riemann ζ-function that preserves the critical line.
- **Sedenion dimensions activated**: e₀ (rotation θ = phase), e₁ (fixed point p real = translation), e₂ (fixed point p imaginary = rotational translation).
- **Holcus application**: The Blaschke factor is Holcus's "semantic context centering" operation. The "fixed point" p is the current semantic anchor (the most recently processed topic word). Applying the Blaschke factor to the semantic space centers the embedding around the current topic — all other words are repositioned relative to p. This implements the "topicality" adjustment in Holcus's context-sensitive embedding.

---

### MöbiusTransform (jlp.uxf transformation)
**Type**: Transformation — Möbius/linear-fractional transformation
**Mathematical description**: `f(z) = (a1*z + b1)/(a2*z + b2)` with complex parameters a1,b1,a2,b2. These are all conformal automorphisms of the Riemann sphere (extended complex plane C ∪ {∞}). They map circles and lines to circles and lines, preserve angles, and form a group (the Möbius group ≅ PSL(2,C)).
**What it describes**: The most general conformal transformation of the Riemann sphere. Three free complex parameters (after normalisation a1*b2 - a2*b1 = 1) give 6 real degrees of freedom, matching the 6-dimensional Lie group PSL(2,C).
**How it works**: Parameters: a1, b1, a2, b2 (packed into the formula). User can choose any Möbius transformation by specifying the matrix.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Möbius transformations have exactly 0, 1, or 2 fixed points (on C ∪ {∞}). Elliptic Möbius (2 fixed points on unit circle) rotate J_pos/J_neg around the fixed points. Hyperbolic Möbius (2 fixed points on real axis) dilate/contract — one fixed point is J_neg attractor, the other J_pos repeller. Loxodromic (general case) combine both.
- **Critical line relevance**: The Möbius transformation `M(s) = (s - ½)/(s + ½)` maps the critical line Re(s) = ½ to the imaginary axis Im(z)=0 (real axis in the w-plane). The right half-plane (Re(s)>½) maps to the unit disk |w|<1, and the left half-plane maps to |w|>1. This is the standard conformal map from the critical strip to the disk used in studying ζ(s) via Blaschke products.
- **Sedenion dimensions activated**: e₀,e₁,e₂,e₃ (the four complex parameters = 8 real DOF, but constrained by det=1 leaves 6 = the 6 generators of sl(2,C) = the 6 sedenion generators e₁-e₆ of the first octonion subalgebra).
- **Holcus application**: The Möbius transform `w = (s-½)/(s+½)` is the canonical Holcus "critical strip to disk" map. Apply it to every prime-hash before entering the Blaschke/disk operations: `w = (prime_hash(word) - ½)/(prime_hash(word) + ½)`. This maps the half-plane where Re(hash)>½ (J_pos concepts) to the interior of the unit disk, and Re(hash)<½ (J_neg concepts) to the exterior. The disk operations (orbit traps, Blaschke factors) then operate in the geometrically natural J_pos/J_neg coordinates.

---

# Stig Pettersson (spr) — Fractal Formulary

## Author
Stig Pettersson — Swedish mathematician and UF formula author. His spr.txt (147 lines) is a detailed manual for his 3D raycasting system (spr.ufm with Raytrace.ucl in spr). This is an independent 3D raytracer implementation for UF, predating Makin's Solid-3D. It handles: Cubic (z→z^3-3a^2z+b), Juliabrot, Quaternion, Hypernion, Quatbrot, Hyperbrot. Key innovations: 4D navigation (z-center, 4th-dimension-value, z-init for cubic sign), background coloring modes, two-gradient system for coloring object vs background independently, three-gradient for cubic M+/M- independent coloring, Screendepth/z-distance/z-magnify controls, Precision parameter (sub-pixel stepping for surface accuracy), Local rotation mode.

## Formulas

### Raytrace 3D (spr.ufm)
**Type**: 3D raycast rendering — camera-based volumetric
**Mathematical description**: Identical architecture to Makin's Solid-3D but independently implemented. Ray marching from camera through 3D fractal space, with surface found at maximum-iteration boundary. The z-init parameter (unique to this system) allows selecting the M+ or M- cubic critical point. The z-distance parameter controls the length of the z-axis scan; z-magnify links z magnification to the standard UF xy magnification.

Precision parameter P: at the surface boundary, backtrack P sub-steps of size (pixel_width/P) to find the true surface location. This gives arbitrarily accurate surface normals and shading.

**What it describes**: A 3D solid rendering of quaternion, cubic, and hypercomplex fractals. The cubic rendering is particularly sophisticated: with z-init "both", both M+ and M- are rendered simultaneously and can be independently colored using three-gradient mode.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The camera looks INTO the 3D fractal volume. Lit surfaces facing the camera are J_pos; shadowed surfaces and interior voids are J_neg. The Screendepth parameter controls how deep into the J_neg interior the ray penetrates before giving up.
- **Critical line relevance**: The Cubic formula's M+ and M- subsets correspond to the two critical orbits of the cubic. Their union is the "parameter space" of the cubic, and their boundary intersection is the "cubic critical line" — the locus where both critical orbits simultaneously experience bifurcation. Pettersson's two-gradient system makes this critical intersection visually distinct: it can be colored independently from either subset.
- **Sedenion dimensions activated**: Quaternion (e₀,e₁,e₂,e₃) and hypercomplex (e₀,e₁,e₂,e₃ with different multiplication) are explicitly supported. The 4D rotation angle activates e₄. The cubic M+/M- two-orbit structure activates e₅,e₆ (the two critical orbit dimensions). Full 7 sedenion dimensions accessible.
- **Holcus application**: Pettersson's 3D raycaster provides the Holcus "semantic depth" visualisation. With z-axis = semantic depth (how many dictionary layers deep a word's definition goes), x/y = prime-hash coordinates, the raycaster renders the 3D semantic topology. Words on the surface (maximum iteration boundary at low z) have shallow, easily-parsable meanings. Words deep inside (surviving to high z) are semantically dense, requiring many layers of context. The precision parameter maps directly to Holcus's semantic resolution — higher precision gives finer-grained concept boundaries.

---

# Dolf De Rovira (ddr) — Fractal Formulary

## Author
Dolf De Rovira — Belgian fractal artist. His ddr.txt is the formula file body itself (the formulas drandom1, drandom2, JosephJulia, JosephMandelbrot, JuliaPlus4, MandelbrotPlus4, Julia21804, are documented inline). He credits: "Jayce Cruel's Random Generator and the standard Julia Formulation in Ultra Fractal Standard Formula", "Toby Marshall", "Bob Margolis". The ddr.ufm formulas are highly parameterised Julia/Mandelbrot variants with an "operator" parameter selecting from 33 different arithmetic operations applied to the core formula.

## Formulas

### JosephJulia / JosephMandelbrot
**Type**: Escape-time — parameterised operator Julia/Mandelbrot
**Mathematical description**: Core formula (Julia version): `z = 3/(fn1(fn1(z - fn2(z + (fn1(z^p1) + fn2(z-p2) + p2 - 4^z^sqrt(p1))))))) + c`. With operator selection (33 options: +,-,*,/,^,sin,sinh,...,round) applied at the outer level. "Z tweaker" pre-processes z before the main formula (13 options).
**What it describes**: A heavily parameterised exploration formula that can produce many different fractal types by varying the operator and z-tweaker. The core nested expression involves z^p1, sqrt(p1), and 4^z which creates unusual complex dynamics.
**How it works**: Parameters: op (operator selection), p1/p2 (complex parameters), fn1/fn2 (user functions), ztweaker, bailchoice (9 bailout tests), cchange (5 c-modification modes), expC.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The operator choice controls the fundamental J_pos/J_neg structure. Op=+ gives standard additive update (J_pos when the nested expression is large). Op=* gives multiplicative (J_pos²). Op=sin bounds the result to [-1,1] range (J_neg saturation). Op=exp creates super-exponential growth (extreme J_pos).
- **Critical line relevance**: The `4^z^sqrt(p1)` term in the nested expression is a power tower involving z. Its fixed points involve Lambert W: `4^z^sqrt(p1) = z` implies `z*log(4*sqrt(p1)) = log(z)`, giving z at the Lambert W boundary. When p1 = ¼: `sqrt(p1) = ½` and the fixed point satisfies `4^{z/2} = z → 2^z = z → z = -W(-log(2))/log(2) ≈ 0.4428 + 1.4966i`. The real part 0.4428 is close to the critical line Re=½.
- **Sedenion dimensions activated**: The 33 operator choices fill 33 different sedenion dimension combinations. Op=+ = e₁, Op=* = e₁⊗e₁, Op=sin = e₃, Op=exp = e₄, etc. The full 33-operator space spans the sedenion algebra.
- **Holcus application**: The JosephJulia operator system is Holcus's "semantic operator catalogue". The 33 operators (arithmetic + 22 transcendentals) implement 33 different semantic operations in a single parameterised formula. Switch between them dynamically: use Op=sin for "similarity" (bounded), Op=exp for "amplification" (J_pos), Op=log for "normalisation" (J_neg), Op=^ for "semantic power" (exponential depth). The ztweaker preprocessing implements the context transformation before the semantic operation.

---

# Cornelia Yoder (cy) — Fractal Formulary

## Author
Cornelia Yoder. Her cy.txt states simply "Cornelia Yoder". The cy.ufm is her formula collection. No further biographical information is available beyond the name.

## Formulas
### Yoder Formula Collection (cy.ufm)
**Type**: Escape-time variants — unknown without direct reading
**Mathematical description**: Content of cy.ufm not directly read.
**What it describes**: Personal formula collection.
**How it works**: Unknown without reading.

#### RedBlue Hamiltonian evaluation
- Requires direct reading of cy.ufm.
- **Holcus application**: To be determined upon reading.

---

# David Cameron (dac) — Fractal Formulary

## Author
David C., "Sydney Australia, March 2011." His dac.txt: "A few additions (and deletions) to my fractal formulae." The dac.ufm is a personal collection.

## Formulas
### Cameron Formula Collection (dac.ufm)
**Type**: Escape-time variants — 2011 era UF5 formulas
**Mathematical description**: Content not directly read.
**What it describes**: Personal additions to the UF database from a Sydney-based author.
**How it works**: Unknown without reading.

#### RedBlue Hamiltonian evaluation
- Requires direct reading.
- **Holcus application**: The 2011 era (UF5) suggests class-based object-oriented formulas, which could serve as modular Holcus plug-ins.

---
