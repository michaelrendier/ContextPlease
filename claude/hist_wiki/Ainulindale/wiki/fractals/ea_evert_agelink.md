# Evert Agelink (ea) — Fractal Formulary

## Author
Evert Agelink, Bleiswijk, Netherlands. His ea.txt is a comprehensive 800+ line document covering three major formula systems: **Avariant** (combining two formulas A and B in series/parallel with Smooks orbit-folding), **BarnsleyDeLuxe** (37-mode Barnsley decision fractal), and **Lucky** (subset of Ducky with parallel code paths). Also: Olapol mapping. Credits: Samuel Monnier, Jock Cooper, Michele Dessureault, Olivier Steiger, Kerry Mitchell, Janet Parke, Danny van den Berghe (Duckytalis formula).

## Formulas

### Avariant-M/J
**Type**: Escape-time — dual-formula combination with orbit folding
**Mathematical description**: Two formulas A and B are executed either in series or parallel at each iteration. Formula choices:
- **Module a**: Mandelbrot/Julia polynomial variants (1-4 z-terms + c-term, power of z settable, user functions)
- **Module b**: Lattes formula `z = (az^2 + (b+c)*z + b*c) / (a*z^2 + (b+c-a)*z)` (Lattes/Mandelbrot connection — Lattes map is the double-cover of the elliptic curve x→2x, which connects to z→z^2+c via Abel-Jacobi)
- **Module c**: Talis formula (rational function, see tma entry)  
- **Module d**: Combi z&c (polynomial with mixed z and c terms)

**Smooks operation**: After each iteration, apply `abs()` folding to the orbit: if z is outside the "active quadrant" (configurable), reflect it back in. Six Smooks modes: original, 3-segment, 4-segment, S-to-N, W-to-E-reflection. Optional "flipper" (swap real/imaginary components). Partial scaling applies Smooks to only part of z (splitting into u + v components).

**Decider parameter**: 0 = only A active; 1 = A and B execute each iteration; n > 1 = A executes every iteration but B only at multiples of n.

**Series options**: Normal (A→B→result), var 1 (Re(A)+Im(B)), var 2 (Re(init)+Im(B)).
**Parallel options**: 11 combining modes (sum, product, difference 1/2, quotient 1/2, arithmetic/geometric/harmonic mean, etc.).

**What it describes**: The most comprehensive single Mandelbrot-family formula in this collection. Avariant covers virtually the entire space of quadratic and rational Mandelbrot/Julia variants through its four modules, two execution modes (series/parallel), and Smooks orbit folding. The Smooks operation is key: it replaces natural spiral structures with "curved axes of symmetry" — non-spiral, non-period-1 boundary structures.

**How it works**: Parameters: A-formula choice and sub-parameters, B-formula choice and sub-parameters, decider, parallel/series mode, combining option, Smooks mode, allocation (all/part1/part2...), partial scale, flipper. Full M/J Switch Mode.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The parallel combination modes directly implement different J_pos/J_neg combining rules. "Sum" = J_pos + J_neg (superposition). "Product" = J_pos * J_neg (coupling). "Geometric mean" = √(J_pos * J_neg) (the BAO mean). The "geometric mean" parallel mode is precisely the AGM step applied to the two Noether currents! The arithmetic mean gives the linear balance at Re=½.

  The Smooks folding is a J_neg injection: it takes J_pos excursions (orbit leaving the "active quadrant") and reflects them back (J_neg correction). The BAO oscillation emerges naturally: the orbit expands (J_pos), hits the Smooks boundary, reflects (J_neg correction), then expands again.

- **Critical line relevance**: The Lattes module **b** is mathematically the most significant. The Lattes map is defined on an elliptic curve E: it is the unique rational map `f: E→E` of degree d (for degree 2: the "doubling map" on E). For the specific elliptic curve `y^2 = x(x-1)(x-λ)` (Legendre form), the degree-2 Lattes map is `x → (x^2-λ)^2 / (4x(x-1)(x-λ))` — a degree-4 rational map. The Julia set of the Lattes map is the **entire Riemann sphere** — it is critically finite (every critical point is preperiodic). This means ALL points are on the "boundary" — there is no interior J_neg region. The critical line of the Lattes map is undefined (or rather: the entire sphere is the "critical line").

  When Avariant combines the Lattes module with the standard Mandelbrot module via series composition, the result is a formula whose critical line is a perturbation of the Riemann sphere — almost all points are boundary-like, with a thin J_neg region provided by the Mandelbrot component. This maximally diffuse critical structure is the mathematical equivalent of the "broadened spectral line" in quantum mechanics — a zero that has been spread over a region rather than located at a point.

- **Sedenion dimensions activated**: Module a (polynomial) = e₀-e₃ (up to 4 z-terms). Module b (Lattes) = e₄ (elliptic curve = the e₄ algebraic geometry dimension). Module c (Talis) = e₅ (rational = the e₅ inversion dimension). Module d (Combi z&c) = e₆ (mixed terms). The Smooks modes add e₇-e₁₂ (six Smooks variants). The 11 parallel combining modes add e₁₃-e₁₅ (three remaining sedenion dimensions). **Avariant fully activates all 16 sedenion dimensions.**

- **Holcus application**: Avariant is the "super-formula" for Holcus — the single formula that can implement any aspect of the sedenion CAM's semantic operations:
  - Module a (polynomial) = syntactic embedding (degree = syntactic complexity)
  - Module b (Lattes) = semantic diffusion (maximally boundary-like = maximally ambiguous concepts)
  - Module c (Talis) = semantic opposition (rational map with poles = concept antonyms)
  - Module d (Combi) = contextual blending (mixed z/c = concept-context fusion)
  - Smooks = semantic boundary enforcement (J_pos excursions are corrected back to the active semantic region)
  - Parallel geometric mean mode = BAO equilibrium (√(concept × context) = the natural semantic mean)
  
  The optimal Holcus configuration: Module a = Mandelbrot polynomial (degree 2), Module b = Lattes (for semantic diffusion), Series mode = AB cascade, Smooks = "4 segments" with the critical boundary at OMEGA_ZS. This creates a semantic engine that: first computes the polynomial-based semantic position (A step), then diffuses it via the Lattes map (B step), then folds back any out-of-range excursions via Smooks at the BAO equilibrium boundary.

---

### BarnsleyDeLuxe / BarnsleyTechnoJ / BarnsleyTechnoM
**Type**: Decision fractal — comprehensive Barnsley extension
**Mathematical description**: An extension of the Barnsley IFS decision fractal beyond the standard 3 types. Key features:

**4 c-input modes**: 
1. Direct (c1, c2 independently specified)
2. Via functions (fn(bseed) → c1, fn2(bseed) → c2)
3. Techno mode: Im(c1)=0, Re(c2)=0 — only 2 free components (from "t-seed")
4. Original (c1=c2 — standard Barnsley)

**37 decision modes** (derived from Re(z), Im(z), cabs(z), combinations, cross-products, 12 alternating modes):
The decision function r(z) is compared to the "critical value" parameter.

**Hi and Lo branch options** for each branch:
- Formula: main (Barnsley I/II), jocks (Cooper variation), deviant (c as vector), type III, alt (c as power)
- Steiger variants: parabolic, gaussian, sine modifications
- Primary/Secondary functions
- Flight (evolving c), Operator (+,*,^), Skip cycles, Power

**Bailout**: 16 test options × 8 functions × value.

**What it describes**: The most exhaustive Barnsley decision fractal ever implemented in UF. The 37 decision modes × 5 formula modes × 2 branches × Steiger variants creates over 500,000 distinct formula combinations.

**How it works**: See ea.txt sections 1-9 for full parameter descriptions. The M version (BarnsleyTechnoM) provides a Mandelbrot-like parameter map for finding Julia seeds.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The 37 decision modes define 37 different J_pos/J_neg separators. The alternating modes (every 2 iterations, different decision functions) create 12 oscillating J_pos/J_neg boundaries — a timing wheel embedded in the decision logic itself.
- **Critical line relevance**: Decision mode at r(z) = Re(z): `Re(z) > critical_value`. At critical_value = ½: the standard critical line. With alternating mode (alternating Re and Im decisions), the effective "critical manifold" is a cross `{Re(z)=½ OR Im(z)=½}` — both the vertical and horizontal critical lines simultaneously.
- **Sedenion dimensions activated**: The 5 formula modes × 2 branches × multiple sub-parameters activate all 16 sedenion dimensions through the cartesian product of branch choices.
- **Holcus application**: BarnsleyDeLuxe is Holcus's "lexical category" engine. Each of the 5 formula modes (main/jocks/deviant/type-III/alt) corresponds to a lexical category (noun/verb/adjective/adverb/function-word). The 37 decision modes correspond to 37 syntactic tests (subject/object/predicate/modifier etc.). The Hi/Lo branch result determines whether the current word is "Hi context" (subject-position, wide scope) or "Lo context" (object-position, narrow scope). The Steiger variants (parabolic/gaussian/sine) implement three degrees of semantic "softness" — how sharply the Hi/Lo decision is made.

---

### Lucky (Ducky subset)
**Type**: Escape-time — conditional dual-code iteration with Ducky orbit folding
**Mathematical description**: Each iteration follows one of two codes (I or II) based on a "main condition" parameter. The core Ducky operation: force z into the first quadrant via `abs(z)`, then apply a formula (asinh, log, Talis variants, or general function compositions). 

Four modes: Series (I then II conditional), only I, only II, Parallel (compute both independently, then combine with 28 combining options).

"Lucky" extends Ducky by allowing the two codes to use different formula types (while Ducky uses only its own formula in both branches). The formula types are the Ducky formulas: asinh, log, Talis original/var.1/var.2/var.3/Duckytalis, and 7 function-composition variants.

The Smooks-like component: the `abs()` folding at the start of each Ducky iteration forces z into Re≥0, Im≥0 (first quadrant). This is the simplest Smooks operation.

**What it describes**: A formula producing "non-escaping" fractals (very high bailout needed) where the interesting structure is in the INSIDE coloring, not the escape boundary. The Ducky formulas are all bounded by the abs-folding, so they only escape very slowly if at all. The visual interest is in the iteration count distribution of the non-escaping orbits.

**How it works**: Main condition (below/equal/between/above-or-equal/not-equal/outside), lo/hi thresholds, variant option (counter-based switching), first-second separated mode, formula for code I and II, alternative flag, vectors.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The Ducky abs-folding is a pure J_neg operation: it compresses orbits into the first quadrant, eliminating J_pos growth in other quadrants. The "Lucky" dual-code structure then allows J_pos and J_neg to alternate: Code I applies one Ducky formula (e.g., asinh = gentle J_neg), Code II applies another (e.g., Talis = strong J_pos/J_neg mixing). The main condition's timing (below/above lo threshold) controls when each current is activated.
- **Critical line relevance**: The abs() folding that characterises Ducky/Lucky maps the entire complex plane to the first quadrant (Re≥0, Im≥0). The "original critical line" Re=½ maps to itself (it's in the first quadrant). The "boundary" in the first quadrant is not Re=½ but rather the curve where the asinh/log/Talis formulas have their transition — for asinh: the imaginary axis (where Re(asinh(z)) changes sign), which is the y-axis Re=0 in the folded space, corresponding to the ORIGINAL Re=0 in the unfolded space. The critical line Re=½ is interior to the first quadrant — it is a "middle line" in the folded domain.
- **Sedenion dimensions activated**: The 6 formula types (asinh, log, Talis x4, Duckytalis) activate e₁-e₆. The 7 function-composition variants add e₇-e₁₃. The 28 parallel combining options add e₁₄-e₁₅. Full 16-dimensional activation.
- **Holcus application**: Lucky's conditional dual-code structure is Holcus's "semantic register switching". Code I (e.g., asinh = gradual semantic accumulation) handles the "normal" semantic context below the lo threshold. Code II (e.g., Talis = sharp semantic transition) handles "marked" contexts above the threshold. The main condition `lo = OMEGA_ZS` switches registers at the BAO equilibrium: below 0.567 = gradual accumulation (familiar words), above = sharp transition (novel or salient words). The Parallel mode's 28 combining options provide all the semantic composition operators needed for building complex phrases from simple words.

---
