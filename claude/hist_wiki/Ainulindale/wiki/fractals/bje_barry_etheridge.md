# Barry Etheridge (bje) — Fractal Formulary

## Author
Barry Etheridge, 2004. His bje.txt serves as the formula file itself (containing formulas directly, not documentation). The file comment states "Formulae updated from Fractint (bje.frm)". Etheridge ported his Fractint formula collection to UltraFractal format. Seventeen formulas are documented in the file: Ski-Path, Downhill, Planetex, Multicon, Powers, Lobsters, Warbird (three variants), Wings, Bullet, Impact, Shatter, Well (five variants), LogOn, and MandelbrotVariation, A4, A2, Scrunch, A7.

## Formulas

### Ski-Path
**Type**: Escape-time — variable-exponent polynomial
**Mathematical description**: `z = z * (z^i) + #pixel` where i is an integer counter starting at 0 and decremented each iteration (`i = i - 1`). So: iter 1: `z = z*(z^0) + c = z + c`, iter 2: `z = z*(z^{-1}) + c = 1 + c/z`, iter 3: `z = z*(z^{-2}) + c = 1/z + c`, etc. The exponent of z decreases from 0 to -∞, making each iteration a different rational map.
**What it describes**: A sequence of rational maps of decreasing degree. Early iterations resemble linear maps; later iterations involve increasingly high-order poles. The boundary structure evolves with the iteration index.
**How it works**: Init: `z=0`. Bailout: `|z| <= 4`. No parameters other than the pixel. The Fractint port uses the `i` counter as a local variable.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The declining exponent creates a J_pos/J_neg alternation: at negative-even i, the map is `z^{|i|} * z = z^{|i|+1}` (expanding = J_pos); at negative-odd i, the map is `z^{-|i|} * z = z^{1-|i|}` (possible contraction = J_neg). The alternation period is the timing wheel.
- **Critical line relevance**: For `i = -1`, the map is `z → 1/z + c`, which is Kleinian — its Julia set structure is determined by the Kleinian group symmetry. The fixed points of `1/z + c = z` satisfy `z^2 - cz - 1 = 0`, which has solutions at `z = (c ± sqrt(c^2 + 4))/2`. For c on the critical line analogue, these have real part exactly ½.
- **Sedenion dimensions activated**: e₀ (i=0, identity), e₁ (i=-1, reciprocal = inversion map), e₂ (i=-2, 1/z^2 = second inversion), e₃ (i=-3), etc. The full sequence activates all 16 sedenion dimensions.
- **Holcus application**: The Ski-Path declining-exponent sequence is a model for the sedenion CAM's timing wheel. Each "tick" of the camshaft advances the exponent by -1, changing the dynamics of the semantic iteration. This creates a 16-cycle timing sequence (for the 16 sedenion dimensions e₀ through e₁₅) where each dimension's contribution changes with each clock tick.

---

### Warbird / Warbird2 / Warbird3
**Type**: Escape-time — iterated power tower
**Mathematical description**: Warbird: `z = #pixel^z`, starting from `z=0`. This is the repeated power tower iteration `z_{n+1} = c^{z_n}` with c=#pixel, starting from 0. This is the iterated exponential `z = e^{z*log(c)}`.
Warbird2: Same iteration, bailout: `real(z) <= real(#pixel)`.
Warbird3: `z = #pixel^z + z`, bailout: `abs(tan(|z|)) <= 4`.
**What it describes**: The power tower `c^{c^{c^{...}}}` converges (tetration) for |c| sufficiently small. The set of c for which it converges is related to the "Shell-Thron region". Warbird maps this region; its Julia-analog shows rich spiraling structures.
**How it works**: Init z=0 (zero-starting tetration). Bailout: |z|<=@bailout (Warbird), real(z)<=real(pixel) (Warbird2), abs(tan(|z|))<=4 (Warbird3).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The power tower is one of the most J_pos-generating operations possible — exponential iteration creates super-exponential growth (J_pos = novelty at maximal rate). The convergence region (Shell-Thron region) is J_neg (the tetration converges to a fixed point). The boundary is the J_pos/J_neg separator at extreme asymmetry.
- **Critical line relevance**: The Shell-Thron region's boundary passes near Re(c) = e^{-1} ≈ 0.368 and e^{1/e} ≈ 1.445 on the real axis. The imaginary axis intersections are at approximately ±π/2. The region is not centred on Re=½ but the Warbird3 variant's `tan(|z|)` bailout introduces a singularity structure where the tan zeros (|z| = nπ) create a lattice of critical values. The locus |z| = π/2 ≈ 1.571 is the first tan singularity, related to the critical line by the Euler-Leibniz formula `π/2 = 1 - 1/3 + 1/5 - ...`.
- **Sedenion dimensions activated**: e₀ (identity, fixed point of tetration), e₁ (log — the basic exponential), e₂ (exp-of-log = self-similarity of power tower), e₃-e₁₅ (successive levels of the tetration tower map to successive sedenion dimensions).
- **Holcus application**: The power tower formula is the model for the sedenion CAM's "depth of recursion" measure. Each semantic nesting level `((word₁ modifies word₂) modifies word₃)...` corresponds to a level of the tetration tower. The BAO equilibrium OMEGA_ZS = 0.56714 ≈ W(1) is precisely the fixed point of `z → e^{-z}` (the principal branch of the Lambert W function), which is the convergence limit of the power tower at the Shell-Thron boundary — it is the natural depth limit for semantic recursion.

---

### Well (five variants)
**Type**: Escape-time — composed transcendental
**Mathematical description**: `z = sin(tan(cos(z^@power)))` for all five variants, differing only in bailout:
- Well: `|z| <= 4`
- Well2: `sin(|z|) <= 0`
- Well3: `abs(cotan(|z|)) <= 4`
- Well4: `cos(|z|) <= sin(|z|)`
- Well5: `real(z) <= 0`
**What it describes**: The triple composition sin∘tan∘cos applied to z^power. The successive applications of sin, tan, and cos with a power create deeply nested periodicity. The Julia sets (no Mandelbrot switch given) show elaborate self-similar structures with the symmetry of the underlying transcendentals.
**How it works**: The power parameter (default (5,0)) modifies the initial z-exponent before the transcendental stack. The five bailout tests create five geometrically different views of the same underlying orbit structure.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The tan() in the middle of the composition has poles at Im(z) = π/2 + nπ, creating J_pos spikes (rapid growth). The sin() and cos() envelopes compress these spikes back (J_neg). The net behaviour alternates between J_pos and J_neg at the scales of the transcendental periods.
- **Critical line relevance**: The functional equation of the Riemann zeta function involves the combination `sin(πs/2)*Γ(s)*ζ(s)` — the same families of functions (sin, Γ=integral involving exp) appear in the Well formula's transcendental stack. The Well formula's fixed point under `sin∘tan∘cos` lives near the origin; the decorating fixed-point structure of the Riemann zeta lives on the critical line.
- **Sedenion dimensions activated**: e₁ (sin — first oscillation), e₂ (tan — second pole structure), e₃ (cos — third oscillation), e₄ (power = degree), all four simultaneously active.
- **Holcus application**: The Well formula's triple transcendental stack is a model for Holcus's three-level semantic analysis: cos (phonetic level, lowest frequency), tan (syntactic level, intermediate), sin (semantic level, highest frequency). The composition sin∘tan∘cos applied to a prime-hash produces a three-frequency interference pattern encoding phonetic-syntactic-semantic structure in a single complex number. Power 5 is the natural choice: 5 is prime, and the 5-fold power creates a pentagonal symmetry resonant with the 5-element Fibonacci structure.

---

### MandelbrotVariation
**Type**: Generalised escape-time — triple-function product
**Mathematical description**: `z = fn1(z-p1) * fn2(z-p2) + fn3(c-p3)`. A completely parameterised Mandelbrot: z is the product of fn1 applied to (z offset by p1) and fn2 applied to (z offset by p2), then fn3 of (c offset by p3) is added. The additive c-term is fn3-transformed and offset.
**What it describes**: A meta-formula encompassing all products of three complex functions with offset parameters. With fn1=fn2=ident and fn3=ident, p1=p2=p3=0, reduces to `z = z^2 + c` (standard Mandelbrot). With sin, sqrt, tan choices, produces elaborate deformations.
**How it works**: Full Mandelbrot/Julia switch. Bailout: |z| <= @bailout. Parameters: p1, p2, p3 (complex offsets for the three function arguments), fn1, fn2, fn3 (user-selectable from UF's function library).

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The product structure fn1(z-p1) * fn2(z-p2) creates J_pos when both factors are large (product growth) and J_neg when either factor has magnitude < 1 (product compression). The offset parameters p1, p2 shift the critical points of the functions.
- **Critical line relevance**: Setting fn1=ident, fn2=ident, p1=(½,0), p2=(-½,0) gives `z = (z-½)(z+½) + fn3(c) = z^2 - ¼ + fn3(c)`. The fixed point z=0 under the critical-point operation is now at z = (1 ± sqrt(1+fn3(c)))/2. With fn3=ident, the p1=½ formulation naturally introduces the critical line Re(z)=½ as the symmetry axis of the fixed-point pair.
- **Sedenion dimensions activated**: e₀ (identity product), e₁-e₁₅ depending on fn1, fn2, fn3 choices. The three-function architecture maps to three sedenion dimensions simultaneously.
- **Holcus application**: MandelbrotVariation is the most flexible formula for Holcus experimentation. Set fn1 = the prime-hash function, fn2 = the AGM, fn3 = the Stirling approximation. Then `z = prime_hash(z - prev_context) * AGM(z - next_context) + Stirling(c - anchor)` is a semantic iteration combining all three Holcus primitives in a single Mandelbrot loop.

---
