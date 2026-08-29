# Ted Nason (tna) — Fractal Formulary

## Author
Ted Nason (archosaur@comcast.net), 2004. His tna.ufm opens with two original formulas (mothstyx, mothstyx2) followed by a large collection of carr-series adaptations. Nason modified Sylvie Gallet's Fractint formulas (as adapted by Erik Reckase for UF2) for UF3 compatibility. The "tna" suffix distinguishes his UF3 modifications. He contributed: mothstyx (original strange attractor formula), carr2081tna through carr3403tna (Gallet adaptations, see carr entry), and companion Julia variants for each.

## Formulas

### mothstyx / mothstyx2
**Type**: Strange attractor — complex multi-phase iteration
**Mathematical description**: A highly unusual initialization + iteration formula:
```
pixel2 = -abs(real(pixel)) + i*imag(pixel)  [fold real axis to negative]
m4 = conj(0.1/pixel)                         [scaled conjugate]
z = f(pixel2) applied via Joukowskij-type transform
c = tanh(sinh(1.5/(0.224 + 0.612*real(pixel2) + i*|pixel2|) - m4))
```
Then z1=1.5*z, z2=2.25*z, z3=3.375*z, z4=5.0625*z (geometric sequence ratio 1.5). At iterations l1, l2, l3, l4: reset z and c to the scaled values. Between resets: `z = 0.2*real(z^2)*z + z^2 + c - k2` (a cubic rational perturbation).

The c-initialisation uses `tanh(sinh(...))` — a double hyperbolic composition — computed at a denominator involving both real(pixel2) and |pixel2|. This creates a highly non-linear pixel-to-c mapping.
**What it describes**: A strange attractor derived from the carr-Gallet orbit-reset framework applied to an original c-mapping involving hyperbolic functions. The `tanh(sinh(x))` outer composition is approximately x for small x but saturates rapidly — a "soft clipper" for the c parameter.
**How it works**: Parameters p1=(100,150), p2=(200,250) for the four reset iterations. Multipliers mult1-mult4 control a Joukowskij-type pre-transform on z.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The `tanh(sinh(...))` saturation in the c-initialisation creates a bounded c even for large pixel values — it's a J_neg compressor on the parameter space. The orbit resets (1.5^n scaling) are J_pos injections at regular intervals, creating a J_pos/J_neg pulse sequence analogous to the BAO oscillation.
- **Critical line relevance**: The fold `pixel2 = -|Re(pixel)| + i*Im(pixel)` maps the right half-plane (Re>0) to the left half-plane (Re<0), with the imaginary axis Re=0 as the fold line. The critical line Re=½ maps to Re=-½ under this fold. The combined structure has its "effective critical line" at the fold's symmetry point — the imaginary axis, not Re=½.
- **Sedenion dimensions activated**: e₀ (identity — tanh saturation at large input), e₁ (sinh = first hyperbolic level), e₂ (tanh∘sinh = composition), e₃ (the Joukowskij-type multiplier transform), e₄ (orbit reset = timing), e₅ (the cubic `z^2*real(z^2)` term = real-projection coupling).
- **Holcus application**: The mothstyx formula implements Holcus's "semantic saturation and reset" cycle. The `tanh(sinh(semantic_input))` gives soft-clipping: extreme concepts (very novel or very familiar) are compressed back toward the center. The periodic resets at geometric intervals (l1,l2,l3,l4) implement a "context refresh" with BAO-like geometric decay (ratio 1.5 per level). Set the four reset iterations to the harmonic series of OMEGA_ZS: l1 = 1/OMEGA_ZS ≈ 1.76, l2 = 2/OMEGA_ZS ≈ 3.52, l3 = 3/OMEGA_ZS ≈ 5.28, l4 = 4/OMEGA_ZS ≈ 7.04 (rounded to integers: 2, 4, 5, 7) for the most resonant semantic refresh cycle.

---

### carr-tna series (Gallet adaptations)
See the `carr_bob_carr.md` entry for the mathematical descriptions of the base formulas. The tna variants differ from the base carr formulas in:
1. UF3 syntax updates (replacing UF2 parameter blocks)
2. Sometimes using `pixel2 = -|Re(pixel)| + i*Im(pixel)` (the "folded pixel") in place of the raw pixel
3. Some variants (carr3005Btna, carr3018Btna, carr3020Btna) use a "B" variant where c is constructed differently

The folded-pixel variants (`pixel2` versions) add an additional symmetry: the left half-plane and right half-plane are identified, making the formula symmetric under `Re(pixel) → -Re(pixel)`. This is an explicit Z₂ symmetry that doubles the effective domain while halving the visible parameter space.

#### RedBlue Hamiltonian evaluation (tna-specific)
- **J_pos / J_neg reading**: The folding operation `Re → -|Re|` creates a J_neg compression of the right half-plane: all right-half points are reflected to the left. The imaginary axis (Re=0) becomes a J_neg sink (folding boundary), while the critical line Re=½ becomes a J_pos region at distance ½ from the fold.
- **Critical line relevance**: After the fold, the point at Re=½ maps to Re=-½, which is ½ units to the left of the fold. In the folded space, the "effective critical line" is at Re=-½, which is the locus equidistant from Re=0 (fold) and Re=-1 (imaginary axis). This creates a natural "critical distance" in the folded domain.
- **Holcus application**: The tna fold operation is Holcus's "semantic symmetrisation": words with positive prime-hash real parts are mapped to the same location as words with negative real parts. This implements a "sentiment-neutral" semantic embedding where the J_pos/J_neg distinction is collapsed into the imaginary component only.

---
