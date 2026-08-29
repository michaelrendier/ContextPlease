# Adam Schwalbe (abs) — Fractal Formulary

## Author
Adam Schwalbe (aschwalbe@alaska.com). Self-described as still learning; his abs.txt is actually a complete formula body embedded in the text file rather than documentation. He writes: "I stumbled upon this 'fractal' quite by accident. I was writing the code for another formula I hope to post soon, and I did the Algebra incorrectly. The results I find quite pleasing." This honest description of discovery-by-mistake characterises his approach. One known formula: "Fortuitous Mistakes".

## Formulas

### Fortuitous Mistakes
**Type**: Distance-field / Density-map (non-standard escape-time)
**Mathematical description**: Pre-loop global section iterates `y = 200*x` over a user-defined x-interval, recalculates coordinates via the tangent field `y1 = ((tan(x)*x + tan(y)*x) / 2`, `x1 = 2*y1 / (tan(x) + tan(y))`, stores valid points in arrays, then measures minimum Euclidean distance from each pixel to the nearest stored point. Iteration count encodes proximity via `maxcoloriter = maxiter - round((mindist/mindistance[l]) * maxiter + 1)`. No classical z->f(z)+c recursion occurs in the loop; the "fractal" is a density map of the tangent-recalculated curve.
**What it describes**: A scattered point-cloud attractor derived from the intersection of tangent-weighted midpoints along `y = 200x`. The geometry produces non-uniform density clusters that appear fractal-like due to the tan(x) singularity structure.
**How it works**: Global section pre-computes the point cloud; init section computes per-pixel minimum distance; loop section uses a counter against `maxcoloriter` as a fake bailout. Parameters: X start/end intervals, step size. Bug noted: maxiter > 15 creates artifacts; pan/rotate breaks the coordinate system.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The tan-recalculated points that lie within the viewing area are J_pos (novelty — they survived the tan-field selection); pixels far from any stored point are J_neg (dissipation). Density gradient is the Red/Blue gradient directly.
- **Critical line relevance**: The coordinate recalculation `x1 = 2*y1/(tan(x)+tan(y))` has poles wherever `tan(x) + tan(y) = 0`, which occurs on lines `y = -x + nπ`. These are not the Riemann half-line, but the density of surviving points near these poles creates a spectral structure analogous to zero-free regions — points cluster at the edges of the excluded zone.
- **Sedenion dimensions activated**: e₀ (identity — points that map to themselves under the tangent midpoint), e₁ (recursion depth via the mindistance accumulator), e₂ (branching at tan singularities).
- **Holcus application**: The distance-to-nearest-point field is a primitive form of the BAO correlation function: it measures how close any given point is to a "resonance". The array-based precomputation pattern could seed Holcus's prime-hash lookup table, where the stored points are primes and the tangent-midpoint operation replaces the standard hash.

---
