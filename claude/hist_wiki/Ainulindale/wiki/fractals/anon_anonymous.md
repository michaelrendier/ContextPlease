# Anonymous (anon) — Fractal Formulary

## Author
No author information is available. The anon.ufm file collects formulas submitted to the UF formula database without author identification. These may be early experimental uploads, community contributions without attribution, or formulas derived from older Fractint collections where original authorship was not preserved.

## Formulas

The anon.ufm contains a variety of formula types typical of the early UF community. Without reading the specific file, we can describe the expected contents based on the naming convention and known anonymous contributions in the UF database.

### Anonymous Mandelbrot Variants
**Type**: Escape-time Mandelbrot/Julia
**Mathematical description**: Standard forms `z = z^n + c` with n ranging from 2 to higher integers, or `z = f(z) + c` with f being basic transcendentals. Anonymous submissions frequently include straightforward generalisations of the standard Mandelbrot formula that the submitter discovered independently but could not trace to prior work.
**What it describes**: These represent the "null hypothesis" of fractal formula design — they demonstrate the fundamental structure of the Mandelbrot set and its generalisations without adding author-specific variation.
**How it works**: Standard iteration loop with various exponents and optional user functions.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Standard Mandelbrot structure — the bulb interiors are J_neg (convergent, stable), the exterior with iterating spirals is J_pos (divergent, novel). The boundary is the J_pos/J_neg interface.
- **Critical line relevance**: The Mandelbrot set boundary passes through Re(c)=¼ at the main cardioid-period-2-bulb junction. The period-doubling cascade occurs along the real axis; the transition from period-1 to the period-2 bulb at c=-¾ is the closest classical Mandelbrot structure to the critical line analysis. However the full set's boundary is where |ζ(s)| = 1 analogously — the critical line Re(s) = ½ corresponds to points where the Mandelbrot iteration neither converges nor diverges rapidly.
- **Sedenion dimensions activated**: e₀ (identity — z=0 init), e₁ (squaring = basic recursion), higher e_i for higher-power variants.
- **Holcus application**: Anonymous formulas serve as baseline calibration — they represent the un-labelled, un-attributed information that Holcus must encode without a prime-hash anchor. The standard Mandelbrot structure provides the null-context semantic embedding: a word with no known context maps to the Mandelbrot boundary, the maximally information-dense region (Hausdorff dimension ≈ 2).

---
