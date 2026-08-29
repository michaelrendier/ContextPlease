# Andreas Hoppler (aho) — Fractal Formulary

## Author
Andreas Hoppler (aho). The aho.txt file was accidentally uploaded with the wrong content (a note about this mistake), replaced with "Nothing to see here, move along ;-)". From the formula file aho.ufm and the .ucl/.ulb companion files, Hoppler is a formula-writer known for producing UF parameter libraries. He is identified in the system as "Andreas" and signed the corrective note informally.

## Formulas

The aho.ufm file is a companion to the aho.ucl and aho.ulb files. Without reading the .ufm content directly (it requires reading), the file structure suggests Hoppler's work focuses on:
- Extension formulas referencing shared library routines in aho.ulb
- Coloring-integrated iteration formulas in aho.ucl

Based on cross-references in akl.txt (which mentions Andreas Hoppler explicitly as "aho") and the tutorial written by akl (Andreas Lober) which references Hoppler's formulas and the Hevia matrix concept:

### Hevia (cross-referenced, primary formula)
**Type**: Escape-time Mandelbrot/Julia variant using matrix operations on the complex plane
**Mathematical description**: Takes z as a 2D real vector (x,y), constructs a 2x2 complex matrix M(z) from the four lattice neighbours (floor/ceil combinations of x and y), then applies one of several matrix operations to z. Operations include: linear `z = a*x + b*y + i*(c*x + d*y)`, scalar product `z = a*z^2 + (b+c)*z*conj(z) + d*conj(z)^2`, etc. Optional Joukowskij transform `z = z + jouk/z`, lattice periodisation `z = round(z) - z`, and user functions are available as add-ons. Bailout via selectable tests (mod, real, imag, or/and, manh, manr).
**What it describes**: A generalisation of the standard Mandelbrot set where each iteration applies a locally-varying linear or bilinear transformation defined by the lattice neighbourhood. The "die-five" metaphor: z is the centre, a/b/c/d are four surrounding points. Produces complex lattice-deformed Mandelbrot structures with variable local symmetry.
**How it works**: The latticeType parameter (floor/ceil or flow) controls neighbourhood definition. The operation parameter (0=linear, 4=scalar product, etc.) controls the mathematical structure. The exponent, Joukowskij, and function parameters add further distortion.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: In the linear operation mode, J_pos regions correspond to |det(M)| > 1 (expanding, novelty-generating neighbourhoods) and J_neg to |det(M)| < 1 (contracting, stable). In the scalar product mode, the self-conjugate term `d*conj(z)^2` creates an asymmetry that breaks the standard Julia symmetry — J_pos is where the Argand-plane-reflected component dominates.
- **Critical line relevance**: The scalar product operation `z = a*z^2 + (b+c)*z*conj(z) + d*conj(z)^2` with a=d and b+c=0 reduces to `(a-d)|z|^2` which is purely real — the fixed points lie on the real axis. Perturbation analysis shows the boundary at Re(z)=½ when a=d=½, b+c=0: this IS the σ½ critical line.
- **Sedenion dimensions activated**: e₀ (identity — the lattice), e₁ (linear operation), e₄ (scalar product bilinearity), e₂/e₃ (floor/ceil lattice types), e₅ (Joukowskij transform = 1/z map). The full lattice construction activates e₀ through e₅ simultaneously.
- **Holcus application**: The Hevia matrix M(z) is a local semantic context window — it captures the four immediate neighbours of a concept (z) in the lattice space. This is precisely the structure needed for Holcus's local-field prime-hash: each sedenion CAM position z has four lattice neighbours whose hash values combine via matrix operation to produce the next address. The Joukowskij transform `z + jouk/z` mirrors Holcus's reciprocal-balancing operation between forward and backward semantic chains.

---
