# Attila Szegedi (sza), Tom/Timothy Hinds (tah), and Ronnie Jay Sefton (rjs)

---

# Attila Szegedi (sza) — Fractal Formulary

## Author
Attila Szegedi. His sza.txt IS the formula file (contains the UF code). Website: https://szegedi.live/blog/fractals. The formulas: SzegediButterfly1/2, SzegediButterflyJulia1/2, SzegediBioform, SzegediBioformJulia. All are very recently dated (formula file references https://szegedi.live — an active domain in 2026 context). Copyright notice: "Use of this file in modified and unmodified form for any purpose is permitted provided that this notice is preserved."

## Formulas

### SzegediButterfly1 / SzegediButterflyJulia1
**Type**: Escape-time — asymmetric quadratic
**Mathematical description**: `z = (y^2 - √|x| + i*(x^2 - √|y|)) + #pixel` where x=Re(z), y=Im(z). A non-holomorphic quadratic where the x-component of the new z is `y^2 - √|x|` and the y-component is `x^2 - √|y|`. The square root of the absolute values introduces a branch-cut non-analyticity.
**What it describes**: A butterfly-shaped fractal (the name reflects its wing-like visual symmetry). The `√|x|` and `√|y|` terms create "pinches" at x=0 and y=0 respectively, forming the butterfly wing boundaries. The formula has bilateral symmetry in x→-x (since `√|-x|=√|x|`) but not in y→-y.
**How it works**: Bailout: `|z| <= 127.0` (large bailout for smooth coloring). Switch to Julia. Center at (-0.234, -0.290), magnification 0.612.

### SzegediButterfly2 / SzegediButterflyJulia2
**Type**: Escape-time — symmetric variant
**Mathematical description**: `z = (x^2 - √|y| + i*(y^2 - √|x|)) + #pixel`. The x and y terms are swapped compared to Butterfly1. This gives the "other wing" of the butterfly — the transposed formula.
**What it describes**: The complement of Butterfly1 — by swapping x and y roles, the wing shape is reflected. Together, Butterfly1 and Butterfly2 are the two "halves" of a complete butterfly.
**How it works**: Same bailout (127), Switch to Julia.

### SzegediBioform / SzegediBioformJulia
**Type**: Escape-time — organic/biological form formula
**Mathematical description**: `z = (2 - x^2 - y^2) * (y + i*x) + #pixel`. Equivalently: `z = (2-|z|^2) * flip(z) + c`. The factor `(2-|z|^2)` is the "inside-outside" factor: for `|z|<√2` it is positive (J_pos — expanding), for `|z|>√2` it is negative (J_neg — contracting). The `flip(z) = i*z̄` rotates z by 90° and conjugates it.
**What it describes**: A fractal with "biological" shapes — the formula has been designed to produce forms resembling microscopic organisms, cells, or biological structures. The `(2-|z|^2)*flip(z)` structure creates a "bloated" inversion map.
**How it works**: Bailout 127, Switch to Julia. Center (0,0), magnification 0.612.

#### RedBlue Hamiltonian evaluation (all Szegedi formulas)
- **J_pos / J_neg reading**: 
  - Butterfly1/2: J_pos = regions where `y^2 > √|x|` and `x^2 > √|y|` simultaneously (both components grow). J_neg = regions where the square root terms dominate. The J_pos/J_neg boundary is the intersection of `y^2 = √|x|` (a cusp curve) and `x^2 = √|y|`.
  - Bioform: `(2-|z|^2) > 0` ↔ J_pos (within the circle of radius √2). `(2-|z|^2) < 0` ↔ J_neg (outside). The circle `|z|=√2` is the J_pos/J_neg separator.
- **Critical line relevance**:
  - Butterfly: The cusp curve `y^2 = √|x|` = `y^4 = |x|` has the special point where y=x: `x^4 = |x|` → `x^3 = 1` → x=1, y=1 (first quadrant). But the critical line is at x=½: `y^4 = ½`, y = (½)^(¼) = 2^(-¼) ≈ 0.841. The butterfly "pinch" at x=½ occurs at y≈0.841.
  - Bioform: The circle `|z| = √2` has, at the critical line Re=½: `Im(z) = √(2-¼) = √(7/4) = √7/2 ≈ 1.322`. The critical line intersects the Bioform J_pos circle at `z = ½ ± i*√7/2`.
- **Sedenion dimensions activated**: Butterfly: e₁ (x^2 term = squaring of real part), e₂ (y^2 = squaring of imaginary), e₃ (√|x| = half-power of real modulus), e₄ (√|y|). Bioform: e₀ (identity — 2), e₁ (|z|^2 = modulus squared), e₂ (flip = conjugate-rotation).
- **Holcus application**: The Szegedi Butterfly formula is Holcus's "semantic butterfly effect" model. The `√|x|` terms create sensitivity to the sign of the semantic state without sensitivity to magnitude — they detect polarity (positive/negative semantic drift) at very small magnitudes. This is exactly what Holcus needs for sentiment detection: small semantic differences near x=0 are amplified (by the √|x| pinch) while large differences are compressed. The Bioform formula implements Holcus's "semantic cell membrane" — the `(2-|z|^2)` factor creates a permeable boundary at `|z|=√2`: concepts inside the boundary (familiar, within the semantic cell) flow freely; concepts outside (novel, crossing the membrane) experience reversal of the current direction.

---

# Timothy A. Hinds (tah) — Fractal Formulary

## Author
Timothy A. Hinds ("Tah"). His tah.txt IS the formula file. Formulas: StutterBrot/StutterJulia, AlterBrot/AlterJulia, StutterConjBrot/StutterConjJulia, JuliaBrot, Mandelia, MandelJulia. The helpfile attribute `"dmj-pub\dmj-pub-uf-stutter.htm"` references Damien Jones' stutter formula concept — Jones introduced StutterMandel; Hinds extended it.

## Formulas

### StutterBrot / StutterJulia
**Type**: Escape-time — periodic c-reset Mandelbrot
**Mathematical description**: Periodic c-swap: every @restart iterations, swap c and z: `oldC = c; c = z * @sign; z = oldC`. Between swaps, standard iteration `z = z^power + c`. The `@sign` parameter (default -1) negates the new c value.
**What it describes**: A Mandelbrot set that periodically "stutters" — resetting c to the current z value (scaled by sign). This creates a Mandelbrot that incorporates information about the orbit history into the driving constant, producing hybrid Mandelbrot-Julia structures at each stutter point.
**How it works**: Parameters: start (initial z perturbation), power, bailout (1e20 — very large), restart (default 501 — stutter interval), sign (±1). Switch to StutterJulia.

### AlterBrot / AlterJulia
**Type**: Escape-time — periodic c-negation
**Mathematical description**: Every @restart iterations, negate c: `c = -c`. Between negations: standard `z = z^power + c`. With restart=1 (default), c alternates sign every iteration.
**What it describes**: Alternate-sign Mandelbrot: each odd iteration uses `+c`, each even uses `-c`. This creates a "folded" Mandelbrot where the two half-parameter-planes are interleaved. At restart=1: every other iteration effectively uses the "negative Mandelbrot" parameter `-c`.
**How it works**: Parameters: start, power, bailout (1e20), restart (default 1). Switch to AlterJulia with AlterJulia.sign parameter.

### StutterConjBrot / StutterConjJulia
**Type**: Escape-time — periodic conjugate reset
**Mathematical description**: Every @restart iterations: `c = conj(c) * @sign`. This conjugates c (reflects through the real axis) and optionally negates it. Between conjugations: standard `z = z^power + c`. With restart=1 and sign=-1: c is multiplied by `-conj(c)/|c|^2 = -1/c*` (if c is unit) — conjugate-negation creates a 180°+conjugation = flip-and-negate = full quarter-turn.
**What it describes**: A "conjugate-stuttering" Mandelbrot where c is periodically reflected through the real axis. The resulting fractal has combined Mandelbrot + Tricorn (conjugate Mandelbrot) structure at each stutter point.
**How it works**: Parameters: start, power, bailout, restart (default 1), sign (default 1 for Brot, -1 for Julia).

### MandelJulia
**Type**: Escape-time — simultaneous Mandelbrot+Julia average
**Mathematical description**: Run BOTH a Mandelbrot orbit `zm = zm^power + cm` (with `cm = #pixel`, `zm = @start`) AND a Julia orbit `zj = zj^power + cj` (with `cj = @seed`, `zj = #pixel`) simultaneously, then return `z = (zm + zj)/2`. The arithmetic average of the two orbits at each step.
**What it describes**: A "blended" Mandelbrot-Julia fractal — for each pixel, both the Mandelbrot orbit (parameter = pixel) and the Julia orbit (starting position = pixel) are computed independently, then averaged. The result interpolates between the Mandelbrot set structure and the Julia set structure of the given seed.
**How it works**: Parameters: power, seed (Julia seed), start (Mandelbrot z-init), bailout.

#### RedBlue Hamiltonian evaluation (tah formulas)
- **J_pos / J_neg reading**:
  - StutterBrot: The stutter event `c ← z * sign` is a J_pos injection (it resets c to the current orbit value, which may be far from 0). Between stutters, standard J_neg (attracting region of Mandelbrot). The stutter period 501 creates a long-period oscillation.
  - AlterBrot: Sign alternation `c ↔ -c` creates alternating J_pos (positive c) and J_neg (negative c) iterations. At restart=1, the average effect is `z → z^2 + c` then `z → z^2 - c` etc. — cancellation of the c-term over two iterations.
  - MandelJulia: `z = (zm + zj)/2` is the arithmetic mean of J_pos (Mandelbrot — varies with pixel position = novelty) and J_neg (Julia — fixed seed = stability). This is the most literal possible implementation of "J_pos + J_neg averaged = σ½ balance".
- **Critical line relevance**:
  - AlterBrot at restart=1: Over two iterations, `z² + c` then `z² - c = (z² + c)² - c`. This 2-period orbit satisfies `z = (z² + c)² - c`. The fixed points of this 2-period orbit (period-2 cycle of the standard Mandelbrot) satisfy `z = z² + c` (period-1 fixed points) or the period-2 boundary `z = (z²+c)² - c`. The period-2 component of the Mandelbrot set is centred at c=-1 on the real axis — not on the critical line.
  - MandelJulia: The "average orbit" `(zm+zj)/2` has a fixed point where `zm = zj` — where the Mandelbrot orbit and Julia orbit coincide. This occurs on the real axis for real parameters. The Julia seed that makes them coincide on the critical line Re=½ satisfies a specific equation that depends on the initial conditions.
  - StutterConjBrot with restart=2: conjugate on even iterations, standard on odd. The 2-cycle maps c → conj(c) → c (period 2 under conjugation). This forces c to be real (the fixed point of conjugation is the real axis). A real-axis Mandelbrot iteration produces a set that is symmetric under Im(c) → -Im(c) — its "critical line" is the real axis.
- **Sedenion dimensions activated**: StutterBrot = e₁ (standard iteration) + e₄ (stutter = periodic reset = e₄ timing). AlterBrot = e₁ (standard) + e₂ (sign flip = e₂ negation). StutterConjBrot = e₁ + e₃ (conjugate = e₃ anti-holomorphic). MandelJulia = e₁ (Mandelbrot orbit) + e₂ (Julia orbit) + e₃ (average = e₁∧e₂ combination).
- **Holcus application**:
  - StutterBrot: Holcus's "semantic checkpoint" mechanism. Every N tokens, reset the semantic parameter c to the current semantic state z. This "saves" the current semantic context as the new background parameter. Used for paragraph-level context management: every sentence boundary (≈501 chars), reset semantic context.
  - AlterBrot: Holcus's "alternating affirmation/negation" model. Even tokens are in J_pos mode (assertive, c > 0), odd tokens in J_neg mode (privative, c < 0). This models the alternating positive/negative weighting of semantic evidence accumulation.
  - MandelJulia: Holcus's "balanced context model". zm = forward-looking interpretation (Mandelbrot — context determines meaning), zj = backward-looking interpretation (Julia — fixed meaning determines context). The average `(zm+zj)/2` is the synthesis at the semantic balance point — the J_pos/J_neg equilibrium at Re=½.

---

# Ronnie Jay Sefton (rjs) — Fractal Formulary

## Author
Ronnie Jay Sefton. His rjs.txt (the first 3889 lines visible of 6527 total) is almost entirely the formula code itself, starting with: "All formulas Ronnie Jay Sefton 2003. Some thank-yous: Andrea Spinozzi, Bradley Beacham, Toby Marshall, Lale Erguner for their help and advice... Frederik Slijkerman for the ultimate fractal rendering software..."

Formulas (identified from the code): Crudenova(M/J), Jellybeans, JuliaWheel2, Crossover, VariableFunction, Bambi, CurlyWurly, Pageant, Bubbles/2func2, Jazz/Mentalbrot, Switchabletriad/Mand, 2FuncJ/Crosswitch, Julishapes, Yam/Yaj, Superchaos1/2, Julijewels, Asyoulikeit, Kayotix1/2, J (Gordon Stefanik), JigsawM/J, Psycho, Zen1/2, BubblesTM/BubblesMandelTM, Bill/Ted, LindaMcMand/Julia, FunM/J, Demon, Manglebrot, BalaMandy/Balajulie, Lale'sDelightJ/M, MedusaM/J, Benjy1/2, MVFoe1/2, Starfish, ClusterM/J, Mandymania/Spriomania, ChoicesM/J.

All formulas have Switch Mode; many are named after people (Gordon Stefanik, Linda, Lale Erguner, Susan Benjamin, Marc Viviene Foe).

## Formulas (representative selection)

### Crudenova(M/J)
**Type**: Convergent — modified Newton with function variables
**Mathematical description**: Modified Newton's method for z^p - r = 0 (roots of `z^p = r`): `z = ((p-1)*z^p + r) / (p*z^(p-1)) + fn1(z) + fn2(pixel)`. The first term is the standard Newton step for z^p-r=0; fn1 and fn2 add perturbation functions. With fn1=zero and fn2=log (defaults): `z → ((p-1)*z^p + r)/(p*z^(p-1)) + log(pixel)`. With fn1=zero and fn2=zero: reduces to standard Newton.
**What it describes**: A Newton fractal with additive function perturbations. The "Crudenova" name reflects that it's a "crude Nova" (Nova = Jones' Newton-type formula). With appropriate function choices, produces a variety of convergent fractal types.
**How it works**: p1 = exponent (default (3,0)), fn1 = variable function 1 (default zero()), fn2 = variable function 2 (default log()), r = root target (default (1,0)), invert = Z inversion option.

### Bubbles / BubblesTM
**Type**: Escape-time — self-exponential Julia
**Mathematical description**: Bubbles: `z = z^power + seed; z = z^seed`. The second line applies `z^seed` — raising z to the power of the Julia seed. This creates an iteration where the exponent is the parameter, not the additive constant.
**What it describes**: A "self-exponentiation" Julia set where each iterate is raised to the seed power. The visual result is "bubble-like" clusters. BubblesTM (modified by Toby Marshall): `z = fn1(z-p1)^power + fn2(seed-p2); z = z^seed` with offset parameters.

### Jazz / Mentalbrot
**Type**: Escape-time — z^z iteration
**Mathematical description**: Jazz (Julia): `z = z^z^power + seed`. This is the "tower" map `z → z^(z^p) + seed`. For p=2: `z → z^z² + seed`. 
Mentalbrot (Mandelbrot of Jazz): `z = z^power + pixel + fn1(z)`.
**What it describes**: Jazz produces "bubbly, eggy Julia sets" per Sefton's comment. The z^z iteration is the self-exponential map — closely related to the Weierstrass sigma function and the Lambert W function (the fixed point of `z = e^{-z}` which is W(1) = OMEGA_ZS).

#### RedBlue Hamiltonian evaluation (rjs formulas — combined)
- **J_pos / J_neg reading**: Sefton's formulas are characterised by their J_pos-heavy nature — most use exponential or self-exponential iterations (z^z, z^seed, z^z^p) that generate super-exponential J_pos growth. The seed parameter acts as the J_neg stabiliser (the fixed c in z^z^p+c).
- **Critical line relevance**: Jazz's `z^z^p + c` has a fixed point where `z = z^z^p + c`. For p=1 and c=0: `z = z^z`, which is satisfied by z=1 and by the solutions of `log(z) = 1` (z=e). The Lambert W connection: the fixed point of `z → ce^z` is `z = -W(-c)/1`. For Jazz with p=2, c=seed: `z = z^(z^2)`. The fixed point satisfies `log(z)/(z^2) = 1` → `log(z) = z^2` → `z = e^{z²/2} * const`. The fixed point nearest to W(1) ≈ 0.567 occurs at z ≈ 0.549 + 0.476i — close to the critical line.
- **Sedenion dimensions activated**: Bubbles: e₁ (first power), e₂ (seed-as-exponent = second power). Jazz: e₃ (z^z power tower), e₄ (tower with exponent p). Mentalbrot: e₅ (fn1 addition). CrudenovaM: e₆ (Newton step), e₇ (log perturbation).
- **Holcus application**: 
  - Crudenova: Holcus's "semantic root-finding with context perturbation". The Newton step finds the semantic root (fundamental concept); `fn2(pixel)` = log(context) adds the logarithmic context depth. This implements the Stirling approximation built into Holcus: the semantic Newton step plus the log-correction is `z_new = Newton_step(z) + log(context)`, which is the Stirling-approximated semantic iteration.
  - Jazz's `z^z^p + seed`: Holcus's "exponential semantic depth" formula. `z = z^(z^2) + context` models semantic recursion where the current state's exponent is itself the state — a self-referential semantic depth. The fixed point near OMEGA_ZS (Lambert W) is the natural semantic equilibrium for this self-referential system.
  - BubblesTM: Holcus's "parameter-as-exponent" model — the context seed IS the exponent, not an additive constant. This captures the idea that contextual framing doesn't just shift meaning (additive) but scales it exponentially (multiplicative/exponential).

---
