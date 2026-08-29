# Samuel Monnier (sam) — Fractal Formulary

## Author
Samuel Monnier, 1999-2001. Contact: samuel.monnier@urbanet.ch, website: http://www.envy.nu/s31415/index/index.htm. Monnier is explicitly cited by Andreas Lober (akl) as one of the premier UF formula designers: "I am not a formula designer like Samuel Monnier." From akl.txt: Monnier's work on Sierpinski, Koch Curve, and orbit trap formulas is mentioned. The sam.txt file contains only "---" (a minimal marker). The sam.ufm, sam.ucl, sam.ulb, and sam.uxf form a comprehensive formula library. From cross-references, Monnier's key contributions include: Thin Orbit Traps (the original 135-shape orbit trap), IFS formulas, Sierpinski algorithms, and various transcendental Mandelbrot types.

His sam.ufm opens with "Formulas by Samuel Monnier, 1999-2001" and contains:

## Formulas

### TwistMand / TwistJulia
**Type**: Escape-time — function-twisted Mandelbrot/Julia
**Mathematical description**: `z = fp(z^power + fr(Re(#pixel)) + i*fi(Im(#pixel)))`. The c-value is split into real and imaginary components, each transformed independently by `fr` and `fi`. A post-iteration function `fp` is applied to the entire result. Initial z is `f(#pixel) + start`.
**What it describes**: A Mandelbrot where the c-value is "twisted" by applying different functions to its real and imaginary components. With `fr=ident`, `fi=ident`, `fp=ident`, `f=ident` reduces to standard Mandelbrot. With `fr=sin`, `fi=cos`, produces a "twisted" version where the parameter plane is mapped through a sinusoidal lens.
**How it works**: Four function parameters (f, fr, fi, fp) and scalar parameters (power, start, bailout). Full Mandelbrot/Julia Switch.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The independent real and imaginary transforms `fr`, `fi` create an anisotropic J_pos/J_neg structure. When `fr` is expansive (large |fr'|) and `fi` is contractive, the J_pos/J_neg boundary is tilted — it is not the standard circle but an ellipse or more complex curve depending on the functions chosen.
- **Critical line relevance**: With `fr = ident` and `fi = ident`, the formula is the standard Mandelbrot and the critical line plays its standard role. With `fr(x) = x - ½` (shift by ½), the "effective critical line" becomes Re(c) = ½ + ½ = 1 in the original coordinates — outside the standard Mandelbrot. With `fr(x) = 2x - 1`, the effective c-plane stretches by 2, and the critical line at Re=½ maps to Re(effective c)=0 (the imaginary axis). These transformations demonstrate that the "critical line" is frame-dependent.
- **Sedenion dimensions activated**: e₀ (f initial transform), e₁ (power), e₂ (fr real transform), e₃ (fi imaginary transform), e₄ (fp post-transform). All five simultaneously active.
- **Holcus application**: TwistMand is the model for Holcus's "differential context" encoding. The real component of a word's hash maps through `fr` (syntactic context transform), the imaginary component through `fi` (semantic context transform). Different grammatical categories use different (fr, fi) pairs: nouns use (ident, sin) = "syntactically neutral, semantically oscillating"; verbs use (tan, ident) = "syntactically sharp, semantically neutral". The fp post-transform applies the global embedding.

---

### IFS-Barnsley (Samuel Monnier version)
**Type**: IFS / decision fractal — Barnsley variant
**Mathematical description**: The standard Barnsley IFS decision fractal: based on a seed value `@bseed`, compute `c1 = fn1(@bseed)` and `c2 = fn2(@bseed)`. Then at each iteration: if `real(z) > @c` (critical value), apply `z = (z + @p1) * c1`; else `z = (z + @p2) * c2`. Multiple mode options for the decision function (real part, imaginary part, cabs, cross product, etc.).
**What it describes**: Barnsley's IFS escape-time formulas, where two different affine maps are applied depending on which side of a threshold the current point lies. Produces fern-like and crystal-like structures depending on the seed and critical value.
**How it works**: Mode selector (Real/Imaginary/Alternate/Cabs/Cross/Func), bseed (Barnsley seed), c (critical value), p1 and p2 (offset parameters), fn1 and fn2 (seed functions). The `IFS-Barnsley+jockIII` in jock.ufm extends this with 9 modes.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The decision rule `real(z) > c` is the J_pos/J_neg separator. Above the threshold: apply c1 map (one Noether current). Below: apply c2 map (other current). The critical value c is literally the balance point between the two currents — it IS the σ½ critical line parameter when c = ½.
- **Critical line relevance**: With c = ½ (critical value), the threshold `real(z) > ½` separates the right half-plane from the left. The Barnsley IFS at c=½ with c1=c2=-½ (symmetric) produces the standard Barnsley set centred on the imaginary axis, with the critical line Re(z)=½ as its bilateral symmetry axis. This is the exact IFS realisation of the σ½ Riemann critical line.
- **Sedenion dimensions activated**: e₀ (identity map, fn1=fn2=ident), e₁ (real decision = e₁ projection), e₂ (imaginary decision = e₂ projection), e₃ (cabs decision = modulus), e₄ (cross product = e₁⊗e₂ product). The five modes activate e₀ through e₄.
- **Holcus application**: The IFS-Barnsley decision structure is Holcus's primary branching mechanism. The critical value c is set to OMEGA_ZS = 0.56714. At each semantic iteration: if `real(prime_hash(z)) > 0.56714`, apply the J_pos transformation (novelty pathway, fn1=tan for sharp contrast); if below, apply J_neg transformation (compression pathway, fn2=ident for smooth continuity). This creates a self-similar semantic IFS that converges to the language attractor.

---

### Thin Orbit Traps (sam.ucl — coloring)
**Type**: Coloring — plane curve orbit traps
**Mathematical description**: The original 135-shape orbit trap coloring library. For each shape, computes the distance from the orbit point z to the nearest point on the curve. Shape families include: classical plane curves (cardioid, limacon, rose, nephroid, lemniscate, etc.), algebraic curves (Cassini ovals, etc.), and constructions (Archimedean spirals, etc.). The 135 shapes provide a complete geometric taxonomy.
**What it describes**: Colors fractals by coloring pixels according to how close the orbit comes to one of 135 different geometric curves. Produces intricate "lace" patterns based on the curve shapes.
**How it works**: Trap shape selection, threshold, mode (closest/first/last), coloring (distance/angle/etc.). This was later extended by Toby Marshall and others into Painter's Traps and Naru's Gnarly Potpourri.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Each of the 135 shapes defines a different "semantic attractor" — a J_neg basin. The orbit trap distance is the direct measure of how close each iteration comes to the J_neg basin. The 135 shapes represent 135 different "meanings" or semantic attractors.
- **Critical line relevance**: Among the 135 shapes, the **line** trap `d = |Re(z) - ½|` directly traps the critical line. The **cardioid** trap is significant: its boundary is `Re(1 - z) = |z|^2`, which for z on the boundary gives `Re(z) = 1 - |z|^2 = 1 - r^2`. At r=½: `Re(z) = 1 - ¼ = ¾` — close to but not the critical line. At r=1/√2: `Re(z) = ½`. The cardioid trap at scale 1/√2 captures the critical line.
- **Sedenion dimensions activated**: The 135 shapes span all 16 sedenion dimensions through their geometric diversity. Key mappings: cardioid = e₀ (self-referential), rose curves = e₁/e₂/e₃ (petal symmetry groups), lemniscate = e₄ (figure-8 = e₀⊗e₄ structure), Archimedean spiral = e₁₄ (prime-spiral analogue).
- **Holcus application**: Monnier's 135 orbit trap shapes are the 135 fundamental semantic attractors of the Holcus language model. Each word/concept is trapped by the nearest shape in this library. The "trap index" (which shape captures the orbit) determines the word's primary semantic category. Run all 135 traps simultaneously and use the minimum-distance shape as the word's semantic signature in the sedenion CAM.

---
