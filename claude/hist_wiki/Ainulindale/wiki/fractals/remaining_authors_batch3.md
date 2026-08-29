# Remaining Authors — Batch 3

---

# Miriana Penzo (mpp) — Fractal Formulary

## Author
Miriana Penzo, Italian fractal artist. Credits: Andrea Spinozzi. Her mpp.txt IS the formula file (Ganimedes-M/J, Gingerbread, SquireQuilt, Henon-M/J, KamTorus-M/J, MandelbrotCloud-M/J, Mira-M/J, Popcorn-M/J, VerhulstModel, Gingerbread-M/J, Miriana/Miriana-J, StrangeAttractors-a-M/J, FivePetalsMandelbrot-M/J, Butterfly-M/J, FractalizedMask-M/J, AMandelbrotVariation1/2-M/J). All with Mandelbrot/Julia Switch Mode. Italian parameter descriptions ("Valore del Bailout", "funzioni", "Parametri"). Copyright 2003.

## Formulas

### Ganimedes-M/J
**Type**: Escape-time — multi-operator parameterised fractal
**Mathematical description**: Three parallel computation tracks:
- `x = (fn1(z)^c) OP₁ (fn2(z)^d)` [the "Change" operator]
- `w = (fn3(b*c_px) + fn4(b*z)) OP₂ (c_px*z)` [first track with Operator 1]
- `j = (fn5(a*z) + fn6(a*c_px)) OP₃ (c_px*z)` [second track with Operator 2]
- `z = x * ((fn1(z)^c OP₁ fn2(z)^d)) OP₄ (w+j)` [final combination with Operator 3]
with optional `z=1/z` inversion. Eight "Change" operators, five operators (OP₁-OP₄) each.
**What it describes**: A highly parameterised 3-track parallel computation with 4 operator choices and 6 function choices, creating a large combinatorial space of fractal types.
**How it works**: Parameters a,b,c,d (complex scalings), fn1-fn6 (default: sqrt, asinh, atan, asinh, cos, sin), change/op/op1/op2 operators, invert flag.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The three tracks (x, w, j) implement three parallel Noether currents. The Change operator selects how J_pos flows through the x-track; Operators 1 and 2 modulate w and j independently. The final combination `z = x * (main_track) OP₄ (w+j)` is the Hamiltonian sum of all three currents.
- **Critical line relevance**: With c=d=½ (complex parameters both equal to ½): `fn1(z)^c = fn1(z)^½ = sqrt(fn1(z))`. The combined expression `sqrt(fn1) OP sqrt(fn2) ` creates square-root combinations analogous to the symmetrized Hardy Z-function `Z(t) = e^{iθ(t)} ζ(½+it)` which has real values on the critical line.
- **Sedenion dimensions activated**: The 6 functions and 4 operators collectively activate all 16 sedenion dimensions through their compositions: fn1*fn2 = e₁⊗e₂ product, fn5*fn6 = e₅⊗e₆, operators = e₇ through e₁₀.
- **Holcus application**: Ganimedes is Holcus's "three-stream semantic engine". Stream x: direct semantic content (fn1, fn2 applied to z with power parameters c, d). Stream w: contextual modulation (fn3, fn4 applied to the b-scaled context-pixel c_px). Stream j: relational structure (fn5, fn6 applying the a-scaled relational parameter a). The three streams combine via Operator 3 to produce the final semantic update — modelling content, context, and relationship simultaneously.

---

### Mira-M/J
**Type**: Escape-time — Mira attractor generalisation
**Mathematical description**: Initialise `w = fn1(a*z + (1-a)*(2z^2/(1+z^2)))` and `j = fn2(b - z)`. Then `z = c OP (w*j)`. The core `a*z + (1-a)*(2z^2/(1+z^2))` is a specific nonlinear combination: it interpolates between the identity map (a=1) and the lemniscate map `z → 2z^2/(1+z^2)` (a=0).
**What it describes**: A generalisation of the Mira attractor (a conservative 2D map with island chains). The `2z^2/(1+z^2)` term is a rational approximation to a nonlinear rotation, producing KAM torus structure when iterated. Penzo's version uses it as the inner iteration of a Mandelbrot/Julia framework.
**How it works**: Parameters a (mixing weight), b (Mira parameter), fn1/fn2 (functions), op (5 operators), invert flag.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The Mira map `z → az + (1-a)*2z^2/(1+z^2)` is area-preserving (like a Hamiltonian system) for the appropriate parameter a. The parameter a=1 gives identity (J_neg — no change), a=0 gives the lemniscate map (J_pos — dynamic structure). The mixing weight a interpolates between conservative (J_pos=J_neg balanced) and dissipative dynamics.
- **Critical line relevance**: The lemniscate map `2z^2/(1+z^2)` has a fixed point at z=0 and z→∞. For z on the unit circle |z|=1: `|2z^2/(1+z^2)| = 2/|1+z^2|`. At z=e^{iπ/3}: `|2z^2/(1+z^2)| = 2/|1+e^{2iπ/3}| = 2/|½-i√3/2| = 2/1 = 2`. The unit circle maps to a 2-fold cover — the "period-doubling" of KAM theory, analogous to the period-doubling cascades near the Mandelbrot boundary.
- **Sedenion dimensions activated**: e₀ (identity component, a=1), e₁ (lemniscate component, a=0), e₂ (fn1 = cosh = hyperbolic cosine), e₃ (fn2 = sin = trigonometric). The interpolation parameter a activates the mixing e₅ dimension.
- **Holcus application**: The Mira-M formula is Holcus's "semantic KAM torus" model. KAM (Kolmogorov-Arnold-Moser) theory describes which tori survive small perturbations of integrable Hamiltonian systems. In semantic space, "KAM tori" are robust conceptual clusters that maintain their structure under semantic perturbation (context change). The Mira parameter a controls how much perturbation is applied: a=1 = no perturbation (rigid semantic structure), a=0 = full lemniscate rotation (maximum semantic fluidity). Set a = OMEGA_ZS ≈ 0.567 for the BAO-resonant semantic flexibility.

---

### VerhulstModel
**Type**: Escape-time — logistic map
**Mathematical description**: `z = a*z*(1-z)`. The complex logistic map, the canonical example of chaos from a simple nonlinear rule. For real a in [0,4], produces period-doubling to chaos. For complex a (and complex z = #pixel), produces rich fractal structure — the "complex logistic set" analogous to the Mandelbrot set but for the logistic family.
**What it describes**: The complex logistic fractal. The connection between the logistic map and the Mandelbrot set: the change of variables `z = (1-w)/2`, `a = 4-λ` converts `z → az(1-z)` to `w → w^2 - λ` — the Mandelbrot family. So the Verhulst logistic set IS (conformally equivalent to) a subset of the Mandelbrot set.
**How it works**: Parameter a (default (1.5, 1.0) — complex), bailout = 4.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The logistic map `az(1-z)` has J_neg fixed points at z=0 and z=1-1/a. The fixed point at z=0 is stable (J_neg) when |a|<1. For |a|>2, both fixed points are J_pos (unstable). The "chaotic" regime (real a∈[3.57,4]) is J_pos dominated. The VerhulstModel at complex a maps out these stability regions in the complex plane.
- **Critical line relevance**: The change of variables connecting logistic to Mandelbrot maps the logistic "critical value" a=4 (edge of chaos for real maps) to the Mandelbrot "critical value" c=0 (centre of main cardioid). The logistic a-values mapping to the critical line Re(c)=½ of the Mandelbrot are `a = 4-λ` where `λ = 4 - Re(c) - i*Im(c)`. For Re(c)=½: `Re(a) = 4 - ½ = 7/2 = 3.5` — in the real logistic map, this is well into the chaotic regime (just past the period-3 window). The critical line corresponds to the "strongly chaotic" logistic parameters.
- **Sedenion dimensions activated**: e₀ (identity — the z term), e₁ (the (1-z) factor = one minus identity = negation), e₂ (product az(1-z) = e₀⊗e₁ product = e₂).
- **Holcus application**: The Verhulst logistic map is Holcus's "semantic population dynamics" model. `semantic_density_new = a * semantic_density * (1 - semantic_density)` models how a semantic concept "grows" in a language corpus: too rare (density≈0) = no semantic pressure; too common (density≈1) = saturation. The parameter a controls the semantic "growth rate". At a=OMEGA_ZS*7 ≈ 3.97 (close to the onset of chaos at a=4), the semantic density shows maximal sensitivity to context — the most semantically "alive" configuration.

---

# Piotr Borys (pb) — Fractal Formulary

## Author
Piotr Borys (utak3r@o2.pl). Last update: 12.12.2004. From pb.txt: Generalised Julia set equation `z = c^@cpower * fn_z(z^@zpower) + c^@cpower * fn_c(c)`, Generalised Mandelbrot `z = #pixel^@ppower * fn_z(z^@zpower) + #pixel^@ppower * fn_p(#pixel)`, Iteration Power (coloring), Wavy Traps (coloring). The Wavy Traps coloring: "Original idea taken from Damien M. Jones, and then expanded to my personal wishes. Thanks goes to Toby Marshall for his help."

## Formulas

### Generalised Julia / Mandelbrot (pb.ufm)
**Type**: Escape-time — power-separated Julia/Mandelbrot
**Mathematical description**: Julia: `z = c^cpower * fn_z(z^zpower) + c^cpower * fn_c(c)`. The c-value is raised to a separate power (cpower) before being used, and both the iteration-term and the additive-c-term use this powered-c scaling. For cpower=1, fn_z=ident, fn_c=ident: reduces to `z = c*z^zpower + c = c*(z^zpower + 1)` — not the standard `z^2+c`.
**What it describes**: A two-power generalisation of the Julia set where the c-value and z-value use independently settable powers. This creates a richer family than the standard z^n+c: different combinations of (zpower, cpower) produce qualitatively different fractal types.
**How it works**: Parameters: cpower (power applied to c, also called ppower in Mandelbrot), zpower (power applied to z), fn_z and fn_c/fn_p (user functions applied to z^zpower and c respectively).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: With cpower=2, zpower=2: `z = c^2 * (z^2 + 1)`. The c^2 scaling makes J_pos grow at rate proportional to |c|^2 per unit |z| growth. For |c|>1 (parameters outside the unit disk), J_pos dominates. For |c|<1, J_neg. The unit circle |c|=1 is the J_pos/J_neg separator in the c-plane.
- **Critical line relevance**: The Mandelbrot version `z = #pixel^ppower * fn_z(z^zpower) + #pixel^ppower * fn_p(#pixel)`. For ppower=½ (square root of pixel): `z = sqrt(c) * z^zpower + sqrt(c)`. The fixed points satisfy `z = sqrt(c)*(z^zpower + 1)`, giving for zpower=2: `z/(z^2+1) = sqrt(c)`, i.e., `c = z^2/(z^2+1)^2`. The critical point (dz/dc = 0) gives the Mandelbrot boundary. The critical values where this equals ½ determine the "critical line" in this family.
- **Sedenion dimensions activated**: e₀ (zpower=1 base), e₁ (zpower=2 standard), e₂ (cpower=2 additive), e₃ (cpower+zpower combination), e₄/e₅ (fn_z, fn_c function choices).
- **Holcus application**: Borys' two-power Julia is Holcus's "semantic scaling" formula. The cpower parameter controls how strongly the context c scales the semantic output. cpower=1 = linear context influence; cpower=2 = quadratic (J_pos²); cpower=½ = sublinear (J_neg√). The optimal context scaling for Holcus is cpower = OMEGA_ZS ≈ 0.567 (the BAO equilibrium): sub-unity power gives soft context saturation, preventing context-dominance while still capturing semantic dependencies.

---

# Various Minor / Smaller Authors

The following author codes have confirmed .ufm files but limited or no .txt documentation. They are catalogued here with the information available.

## adm (unknown)
adm.ufm exists. No .txt file. Unknown author.

## amc (unknown)
amc.ufm exists. No .txt file. Unknown author. 

## ar (unknown)
ar.ufm exists. No .txt file.

## as / as2 / asz (unknown)
as.txt states only "as.txt". as.ufm, as2.ufm, asz.ufm exist. asz has .ucl and .uxf companions. Unknown author.

## ben (unknown)
ben.ufm exists. No .txt file.

## bmg (unknown)
bmg.ufm exists. No .txt file.

## bobm (Bob Margolis?)
bobm.ufm and bobm000.ufm exist. Referenced by ddr formulas ("Bob Margolis") — likely Bob Margolis, who assisted with formula development. No .txt file.

## bwp (unknown)
bwp.ucl and bwp.ufm exist. No .txt file.

## cep (unknown)
cep.txt exists. cep.ufm referenced by name. Content unknown.

## ck (Christian Kleinhuis)
ck.txt exists. The ck.ucl contains TrapShapeSuperShape (the SuperShape formula from Paul Bourke's website — n1, n2, n3, m parameters), AlternatingFormulaObject, ChangeFormula_AfterNIterations, BlendFormula (interpolating between two formulas using ComplexInterpolator), Image (using pixel colors as z-perturbation), and the InterpolateBase/Linear/SphericalLinear interpolation classes. This is a UF5 class-based library.

### SuperShape (ck.ucl)
**Type**: Trap shape — parametric superellipse/Lamé curve family
**Mathematical description**: `r(θ) = (|cos(mθ/4)/a|^n2 + |sin(mθ/4)/b|^n3)^(-1/n1)`. The Gielis superformula — a single parametric equation generating a vast family of shapes including circles (n1=n2=n3=2, m=0), squares (m=4, n1=n2=n3=∞), stars (m=5, n1=2, n2=n3=large), and biological forms.
**What it describes**: The "SuperShape" of Johan Gielis (2003) — a mathematical generalisation of the circle to all closed curves via three exponents and a frequency parameter. The Gielis superformula generates shapes resembling leaves, flowers, snowflakes, bacteria, and crystals.
**How it works**: Parameters n1 (radial normalisation), n2 (cos exponent), n3 (sin exponent), m (number of "lobes"), a and b (semi-axis scaling, default 1).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: At r(θ) > threshold: J_pos (outside the shape). At r(θ) < threshold: J_neg (inside the shape). The shape boundary is the J_pos/J_neg separator. The sharpness of the transition depends on n1: large n1 gives a sharp shape (abrupt J_pos/J_neg transition), small n1 gives a soft shape.
- **Critical line relevance**: The superformula at n1=n2=n3=½, m=2: `r(θ) = (|cos(θ/2)|^½ + |sin(θ/2)|^½)^2`. This reduces to `r(θ) = (√|cos(θ/2)| + √|sin(θ/2)|)^2`. The maximum of this function occurs at θ=π/2: `r = (cos(π/4)^½ + sin(π/4)^½)^2 = (2^{-¼} + 2^{-¼})^2 = 4/√2 = 2√2`. The equal point where cos and sin terms are equal occurs at θ=π/2 — a 45° angle. This is the "balanced" point where J_pos and J_neg contributions are equal, analogous to the critical line Re=½.
- **Sedenion dimensions activated**: The superformula at m=16 (16 lobes) creates a 16-fold symmetric shape that directly activates all 16 sedenion dimensions simultaneously — the superformula IS a single parametric curve encoding 16-fold sedenion symmetry.
- **Holcus application**: The SuperShape trap is Holcus's "semantic category shape" — each semantic category has a characteristic shape (round for proper nouns, star-shaped for punctuation, flower-shaped for emotional words, etc.). Use m = 16 (16 lobes) and vary n1, n2, n3 per category to define semantically meaningful boundaries in the sedenion CAM. The Gielis superformula then provides a universal parametric family covering all semantic category shapes with just three exponents.

### AlternatingFormulaObject / BlendFormula (ck.ucl UF5 classes)
**Type**: Meta-formula — formula composition via UF5 class system
**Mathematical description**: AlternatingFormulaObject alternates between Formula1 and Formula2 each iteration (via `count%2`). ChangeFormula_AfterNIterations switches from Formula1 to Formula2 at iteration @atIteration. BlendFormula interpolates: `z_result = Interpolate(@blend, f1.Iterate(z), f2.Iterate(z))` at each step.
**What it describes**: UF5's class-based approach to formula composition. Any two Formula objects can be combined via alternation, phase switching, or interpolation.
**How it works**: Formula params allow any UF5 Formula class as plug-in. BlendFormula uses a ComplexInterpolator with exchangeable interpolation strategies (Linear, SphericalLinear).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: AlternatingFormulaObject implements the time-varying J_pos/J_neg partition of the sedenion CAM timing wheel. On even iterations, Formula1 (e.g., J_pos expanding formula) applies; on odd iterations, Formula2 (J_neg contracting formula). This is the exact structure of the sedenion CAM's timing oscillation.
- **Critical line relevance**: BlendFormula at blend=0.5 is the "critical line formula" — it equally weights J_pos and J_neg formulas. With Formula1 = standard Mandelbrot and Formula2 = conjugate Mandelbrot (Tricorn), Blend=0.5 gives `z = 0.5*(z^2+c) + 0.5*((z̄)^2+c)` = `z^2/2 + (z̄)^2/2 + c` = `Re(z)^2 + c` — a formula that depends only on Re(z), placing all its content exactly on the real axis analogue.
- **Sedenion dimensions activated**: AlternatingFormulaObject with N formulas activates N sedenion dimensions cyclically. BlendFormula's SphericalLinear interpolation (SLERP) activates the full angular sedenion structure.
- **Holcus application**: The UF5 class system of ck is the exact architecture Holcus needs for its modular formula plug-in system. BlendFormula at blend=OMEGA_ZS implements the BAO-resonant semantic interpolation between any two formula objects. AlternatingFormulaObject with period 16 is the sedenion CAM timing wheel implemented as a UF5 class.

---
