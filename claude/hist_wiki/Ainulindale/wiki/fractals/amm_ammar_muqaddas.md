# Ammar Muqaddas / S0lo (amm) — Fractal Formulary

## Author
Ammar Muqaddas, a.k.a. "S0lo". Contact: ammar@solostuff.net / ammar.mu@gmail.com. Modified: 8 November 2005. Website: http://www.solostuff.net, gallery: http://l0pht.deviantart.com. His work consists of Sterlingware formula conversions: "Original formulas taken from Sterlingware by Stephen C. Ferguson. Converted to UF and modified by Ammar Muqaddas. The previous free version of Sterlingware had its sourcecode with it. That's how I was able to convert the formulas." He notes: "Unfortunately, I'm usually too busy and can hardly find extra time to play with fractals."

## Formulas

The amm.ufm file contains Sterlingware-derived formulas. Stephen Ferguson's Sterlingware is known for a large library of generalised polynomial and transcendental fractals, many exploiting non-standard bailout tests and unusual parametric families. The amm conversions retain Ferguson's mathematical structure while adapting to UF syntax.

### Sterlingware Conversions (general)
**Type**: Escape-time, polynomial and transcendental variants
**Mathematical description**: Ferguson's formulas typically iterate `z = P(z) + c` or `z = f(z, c)` where P is a polynomial of degree 2-6 or f is a transcendental (sin, cos, exp, log, tan combinations). Sterlingware's innovation was in the bailout conditions: he used complex bailout geometries including `|real(z)| <= bailout`, `|imag(z)| <= bailout`, and combinations, producing non-circular escape sets.
**What it describes**: A diverse family of Mandelbrot-like sets with non-standard topology. The asymmetric bailout tests create escape sets that are neither round nor simply connected, producing "flattened", "stretched", or "angular" variants of the classical Mandelbrot boundary.
**How it works**: Parameters typically include power/exponent, bailout value, bailout type (real/imag/modulus/etc.), and seed for Julia variants. The UF conversion by Muqaddas adds user-function slots where Ferguson's original had fixed transcendental functions.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: In Sterlingware-style formulas, the asymmetric bailout creates asymmetric J_pos/J_neg regions. Using `|real(z)| <= bailout` as the escape test means only the imaginary component drives divergence — the real axis becomes a J_neg channel (bounded, compressed), the imaginary axis a J_pos pathway (expanding). This is the Noether asymmetry between real and imaginary currents.
- **Critical line relevance**: The real-part bailout `|real(z)| <= bailout` effectively tests whether Re(z) stays bounded. The critical line Re(z) = ½ is within this region for all bailout > ½. This creates a formulation where the Riemann hypothesis region (Re(z) in (0,1)) is precisely the bounded region of the real-bailout Sterlingware fractals.
- **Sedenion dimensions activated**: e₀ (identity/standard power iteration), e₁ (real-part bailout = e₁ directional projection), e₂ (imag-part bailout = e₂ directional projection), e₃ through e₆ (polynomial degree 3-6 variants).
- **Holcus application**: The Sterlingware asymmetric bailout family provides a template for Holcus's one-sided semantic windows. Instead of bailing out when `|z| > 4` (isotropic), bail out when `|Re(hash(z))| > threshold` to create directionally sensitive semantic resonance detection. This would allow the engine to distinguish "expanding" (J_pos) from "contracting" (J_neg) semantic moves in any given direction of the sedenion space.

---
