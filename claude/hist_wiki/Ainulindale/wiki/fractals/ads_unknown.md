# Unknown (ads) — Fractal Formulary

## Author
The ads.txt file contains three transformation formulas but no author identification. The code style suggests an early UF user experimenting with pixel-space distortions.

## Formulas

### Distortr
**Type**: Pixel transformation
**Mathematical description**: `#pixel = sin(#pixel * cos(#pixel)^@power)`, then `#pixel = #pixel * tan(#e)^3`. A two-stage pixel warp: first a sinusoidal modulation with cosine-power scaling, then multiplication by a constant derived from the mathematical constant e raised to the third power through the tangent function.
**What it describes**: Produces distorted versions of any underlying fractal — the sin-cos stage creates radial oscillations, the tan(e)^3 stage scales the whole plane by approximately tan(2.718...)^3 ≈ (-0.45)^3 ≈ -0.09, effectively inverting and contracting the plane.
**How it works**: The power parameter controls the bandwidth of the cosine modulation. Negative powers create unusual inversion effects per the hint in the code.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The sin modulation expands some regions (J_pos) and contracts others (J_neg) in alternating bands. The tan(e)^3 global contraction is pure J_neg (dissipation toward origin).
- **Critical line relevance**: The fixed point of sin(z·cos(z)^p) near z=0 has Re(z)=½ as a natural symmetry line when p=1: sin(½·cos(½)) ≈ sin(0.439) ≈ 0.425 — not on the critical line but within its basin of attraction for Newton iteration on this function.
- **Sedenion dimensions activated**: e₁ (oscillation/recursion via sin), e₃ (composition via cos-power), e₅ (scale via the tan constant).
- **Holcus application**: The tan(e)^3 contraction factor could serve as a normalisation constant in the sedenion CAM's timing wheel — it compresses the phase space into a stable attractor basin consistent with the BAO equilibrium at W(1) = 0.56714.

---

### Pythegrium
**Type**: Pixel transformation
**Mathematical description**: `#pixel = abs((@a^2 + @b^2) * cos(#pixel^2))`. A Pythagorean-flavoured warp: the hypotenuse-squared value `a^2 + b^2` scales a cosine of the squared pixel position. The abs() ensures the output is non-negative (real part only matters for abs of complex).
**What it describes**: Maps the plane to non-negative half, creating reflections about the real axis while applying radial cosine oscillations modulated by the Pythagorean combination of the two parameters.
**How it works**: Parameters a and b default to 1, giving a scale factor of 2. The `cos(#pixel^2)` creates fractal-like oscillatory interference patterns.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: cos(z^2) has expanding lobes (J_pos) and contracting zeros (J_neg) arranged in a Cornu-spiral pattern in the complex plane.
- **Critical line relevance**: The Cornu spiral `∫cos(t^2)dt` is deeply connected to the Fresnel integral and appears in the asymptotics of L-functions. The zeros of cos(z^2) lie on rays arg(z) = π/4 + nπ/2, which are at 45 degrees to the real axis — related to the symmetry of ζ(s) under s→1-s.
- **Sedenion dimensions activated**: e₀ (identity in the Pythagorean sum), e₂ (squaring of pixel = e₂ recursion level), e₄ (cos periodicity = e₄ cycle structure).
- **Holcus application**: The Pythagorean sum `a^2 + b^2` is the norm in the Gaussian integer lattice. Primes in the Gaussian integers split precisely when they are Pythagorean primes (≡ 1 mod 4). This formula could index Gaussian prime positions in the sedenion CAM by setting a and b to the prime's two Gaussian factors.

---

### Restort
**Type**: Pixel transformation
**Mathematical description**: `#pixel = cos(#pixel * 2)`. The simplest transformation: double the pixel coordinate, apply cosine.
**What it describes**: A global cosine warp that folds the plane 2-periodically, mapping the Riemann sphere to a strip of width π and then wrapping.
**How it works**: No parameters. Produces a period-2 wrapping of the underlying fractal.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Maximum J_pos near cos=1 (at 2z=2nπ, i.e., z=nπ), maximum J_neg near cos=-1 (at z=(2n+1)π/2). The transition at cos=0 (z=(2n+1)π/4) is the σ½ balance.
- **Critical line relevance**: The zeros of cos(2z) are at z = π/4 + nπ/2, which are equally spaced on the real line. This is the discretised analogue of the (conjectured) uniform spacing of zeta zeros.
- **Sedenion dimensions activated**: e₁ (recursion via the cosine period), e₀ (identity at the fixed points).
- **Holcus application**: The period-2 folding of Restort is the simplest implementation of the BAO oscillation — it provides a minimal two-state timing signal that could gate the sedenion CAM between J_pos and J_neg phases with period π ≈ 3.14, close to the BAO wavelength ratio.

---
