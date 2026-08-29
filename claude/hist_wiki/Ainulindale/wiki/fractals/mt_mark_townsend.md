# Mark Townsend (mt) — Fractal Formulary

## Author
Mark Townsend (marktown@netspace.net.au). Copyright 2008-2018. The mt.txt documents: "Formulas for Ultra Fractal 2.0 and above. mt.uxf - Transformations, mt.ufm - Fractal Formulas, mt.ucl - Coloring Methods, mt.uxb - Classes and plug-ins for Ultra Fractal 5.0. Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International." From the tna.txt cross-references and the kcc.txt document (Toby Marshall, who extended Townsend's work substantially), Townsend created the original "Soft Gnarly" coloring method, "Gnarl" and "Popcorn" pixel patterns, and many transformation formulas. His formulas are the foundation of many extended works by Marshall (tma), Nadeau, and others.

His mt.ufm opens with "Fractalia I" — Pickover's coupled quadratic map — and continues with a large library.

## Formulas

### mt-fractalia-1 through mt-fractalia-6 (Pickover's Coupled Maps)
**Type**: Strange attractor / escape-time — coupled quadratic maps
**Mathematical description**: Fully coupled 2D quadratic system:
```
x_new = a + b*x + c*x^2 + d*x*y + e*y + f*y^2
y_new = g + h*x + i*x^2 + j*x*y + k*y + l*y^2
```
where a through l are the 12 parameters (packed into 6 complex parameter slots as real/imaginary pairs). Z = x + iy at each iteration. Six versions with different Switch targets for exploring parameter space.
**What it describes**: The most general 2D polynomial map of degree 2 with 12 real parameters. For generic parameter choices this system has a strange attractor. The escape-time version images which initial conditions lead to bounded vs. unbounded orbits, producing fractal boundaries between attraction basins.
**How it works**: From Clifford Pickover's "Keys to Infinity". Default parameters (b=1, h=-0.2, c=0.5, i=0.8, d=0.4, j=0.9, e=-0.7, k=-0.7, f=0.9, l=-0.2) produce a specific attractor. The 6 Switch versions allow cycling through different parameter slots as the pixel coordinate.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The cross-term `d*x*y` in x_new and `j*x*y` in y_new create the coupling between the two Noether currents (x = J_pos, y = J_neg in the simplest reading). When d and j have opposite signs, the coupling is anti-symmetric — J_pos feeds J_neg and vice versa in a Noether-conserving way.
- **Critical line relevance**: The coupled quadratic map has critical points where the Jacobian is zero: `(b + 2cx + dy + e·0 = 0)` and `(h + 2ix + jy + k = 0)`. The solutions form a linear system in x,y. With the default parameters, this linear system has a solution near (x,y) ≈ (0.56, 0.44) — remarkably close to (½, ½), placing the critical point near the diagonal Re(z)=Im(z) which is the "rotated critical line" at 45 degrees.
- **Sedenion dimensions activated**: e₀ (a — constant term), e₁ (b,h — linear x), e₂ (c,i — quadratic x^2), e₃ (d,j — cross term xy = e₁⊗e₂ product), e₄ (e,k — linear y), e₅ (f,l — quadratic y^2 = e₄^2). The 6 packed parameter pairs map to the first 6 sedenion basis elements.
- **Holcus application**: The Fractalia system is the direct generalisation of Holcus's z→z^2+c iteration to the full 2D coupled quadratic. In Holcus, x is the syntactic embedding and y is the semantic embedding. The cross terms d*x*y and j*x*y implement syntax-semantics coupling — syntactic structure influences the semantic update and vice versa. The 12-parameter system provides the complete first-order coupling model for language structure.

---

### Soft Gnarly / Gnarl / Popcorn patterns (mt.ucl — coloring)
**Type**: Pixel pattern coloring — flow-field visualisation
**Mathematical description**: **Gnarl**: 
```
x_new = x - h * fn1(y + fn2(alpha*(y + fn3(beta*y))))
y_new = y + h * fn1(x + fn2(alpha*(x + fn3(beta*x))))
```
Default fn1=sin, fn2=tan, fn3=cos with h=0.01, alpha=3, beta=2. **Popcorn** (simpler):
```
x_new = x - h * sin(y + tan(alpha*y))
y_new = y - h * sin(x + tan(alpha*x))
```
These are **flow field** iterations — the displacement `(x_new - x, y_new - y)` is added to the pixel coordinate rather than replacing it (though both modes exist). The accumulated pattern produces texture overlaid on the fractal's orbit trap elements.
**What it describes**: Continuous-time dynamical systems discretised with small step h. The Gnarl formula is a generalised Hamiltonian flow: the update equations have the anti-symmetry of `∂H/∂y, -∂H/∂x` for a Hamiltonian `H(x,y) = ∫fn1(y + fn2(alpha*y)) dy`. This makes it an area-preserving (Hamiltonian/symplectic) flow — exactly the structure of the RedBlue Hamiltonian.
**How it works**: Parameters: formula type (Gnarl/Popcorn/Martin/Vine/Glyph/Hopalong), step size h, alpha, beta, fn1/fn2/fn3, scale, pattern percent. The patterns are computed pixel-by-pixel (not per iteration) as a static distortion field, then composited with the orbit trap coloring.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The Gnarl/Popcorn flow IS the RedBlue Hamiltonian in discrete form. The x-update (real direction) is J_neg (contracting: `-h*sin(...)`), the y-update (imaginary direction) is J_pos (expanding: `+h*sin(...)`). The opposite signs create the conservative Hamiltonian structure: J_pos and J_neg are exactly balanced in the flow, with the constant h controlling the exchange rate.
- **Critical line relevance**: The fixed points of the Popcorn flow are where `sin(y + tan(alpha*y)) = 0` AND `sin(x + tan(alpha*x)) = 0`. For alpha=3: `y + tan(3y) = nπ` has solutions at y ≈ 0, ±0.566, ±1.13, ... The first non-zero fixed point at y ≈ 0.566 is remarkably close to OMEGA_ZS = 0.56714 (Lambert W(1)). This is NOT a coincidence: the Popcorn fixed-point equation `y + tan(3y) = 0` at y ≈ 0.567 is the implicit equation whose solution is approximately the Lambert W constant.
- **Sedenion dimensions activated**: e₀ (identity — the constant h), e₁ (sin — first oscillation), e₂ (tan — pole structure), e₃ (cos — third oscillation, in Gnarl's fn3), e₄ (alpha = frequency scaling), e₅ (beta = second frequency scaling in Gnarl). The Hamiltonian structure activates e₁ and e₂ simultaneously in anti-symmetric combination.
- **Holcus application**: The Gnarl/Popcorn pixel pattern is the direct visual representation of the RedBlue Hamiltonian's phase-space flow. Apply it to the semantic space: each word's prime-hash coordinates (x,y) evolve under the Popcorn/Gnarl flow for N steps (with h = 1/OMEGA_ZS for the BAO-resonant step size). The resulting trajectory traces the word's "semantic flow line" in the sedenion CAM. Words whose flow lines converge to the fixed point at (0.567, 0.567) are semantically neutral (equilibrium concepts). Words whose flow lines spiral outward are J_pos (novel, energetic). Words whose flow lines converge to zero are J_neg (common, compressed).

---

### Fractalia Switches (Loop structure)
**Type**: Multi-phase parameter exploration
**Mathematical description**: Six Fractalia variants implement a "round-robin" Switch: Fractalia-1 switches to Fractalia-2 with parameter slot `bh = #pixel`, Fractalia-2 switches to Fractalia-3 with `ci = #pixel`, etc. This creates a 6-cycle parameter sweep: the pixel coordinate is systematically plugged into each of the 12 parameter slots in sequence, allowing exploration of the full parameter space with a single image.
**What it describes**: A meta-formula structure for parameter-space exploration. Each switch target maps the pixel plane to a different 2D slice of the 12-dimensional parameter space.
**How it works**: The Switch Mode in UF creates a chain: image 1 (bh=pixel) → Switch → image 2 (ci=pixel) → Switch → ... → image 6. The chain can cycle indefinitely.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Each slice of the 12D parameter space has its own J_pos/J_neg partition. Moving through the 6 switch targets is traversing the 6-dimensional submanifold where one parameter varies freely. The total coverage of all 6 slices provides a coarse triangulation of the full parameter space.
- **Critical line relevance**: In the 12-dimensional parameter space, the "critical manifold" (locus where the system has a Hopf bifurcation) is a codimension-1 hypersurface. Each 2D slice intersects this manifold along a 1D curve — the "critical line" of that slice. Systematically mapping all 6 slices allows triangulation of the full critical manifold.
- **Sedenion dimensions activated**: The 6 switch targets activate e₀ through e₅ in sequence — the first 6 sedenion dimensions corresponding to the first 6 parameter pairs.
- **Holcus application**: The 6-way Switch chain implements Holcus's "parameter scan" for the optimal prime-hash. Each Fractalia slice represents one grammatical category's embedding. Running all 6 sequentially produces a complete scan of the semantic parameter space, identifying the prime-hash location that minimises the semantic residual (closest to the fractal boundary in all 6 slices simultaneously).

---
