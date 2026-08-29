# Toby Marshall (tma) — Fractal Formulary

## Author
Toby Marshall — one of the most extensive formula and coloring authors in this collection. His tma.txt (1455+ lines, running to 9652 total) is a comprehensive guide to "Trap the Light Fantastic" (TTLF) and "Painter's Traps" coloring formulas. From the text: "This coloring is not without its flaws, but in my weeks of explorations with it I have (almost) always found unique and interesting shapes." He also acknowledges: contributions from Gilles Nadeau, Susan Chambless, and cites Townsend, Monnier, Samuel Ferguson, Kerry Mitchell throughout. Files: tma.ufm, tma.ucl, tma.ulb, tma2.ucl, tma2.ufm, tma3.ufm.

Key signature formulas: Painter's Traps (an elaboration of Townsend's Soft Gnarly with plane curve trap shapes), Naru's Gnarly Potpourri, Trap the Light Fantastic, Talis variations.

## Formulas

### Painter's Traps (tma.ucl — coloring)
**Type**: Coloring — plane curve traps + pixel pattern hybrid
**Mathematical description**: Combines two independent systems: (1) pixel patterns (Gnarl, Popcorn, Martin, Vine, Glyph, Hopalong — computed from #pixel, not the iteration orbit) and (2) Monnier's 135 plane curve orbit traps. The pixel patterns warp the element shapes while the orbit traps define which elements appear. The Gnarl/Popcorn pixel pattern formula (Townsend's Soft Gnarly) is used as a distortion field applied to the orbit trap z-value before trap-shape evaluation.

Key innovation: "Mode Recipe" (Straight/Funky) and "Trapping Mode" (None/Sum_Z/Trap_Z/Modulus_Z/Morph_Z) control whether different coloring modes (Distance, Iteration, Angle) overlay exactly or with interesting mismatches. "Morph" parameters define alternative z-definitions for the global variable.

**What it describes**: A generative art system for creating dimensional, lit orbit trap imagery. The pixel pattern adds texture that "becomes part of" the trap elements — the result looks like 3D physical objects scattered across the fractal plane.
**How it works**: Mode (Basic/Advanced), Coloring Type (Soft Gnarly / Plane Curve Traps), Trap Mode (Closest/First/Last), Element Width, Coloring Mode, Shading, 135 Trap Shapes, 9 test points, Tonality, Spread, Masking, Texture options (Random/fBm/Decimal/Popgnarl/Geometrix/Additional), Progressive Parameters, Morph I & II.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Painter's Traps implements the full RedBlue Hamiltonian at the coloring level: the 135 orbit trap shapes are J_neg basins (semantic attractors), the Gnarl/Popcorn pixel patterns are the J_pos flow field (Hamiltonian dynamics), and the "Shading" parameter (opacity) is the dissipation rate. The Morph parameters allow remapping the z-variable, which corresponds to changing the Hamiltonian itself.
- **Critical line relevance**: Using the "Lines" trap shape at position (½, 0) in the "Trap Center" parameter creates a direct critical-line trap: orbits passing through Re(z)=½ are captured and colored. The "Tonality" = "Flavor 2" mode with "Edge 1 = ½" traces the boundary exactly at the critical line width. Progressive parameters applied to "Trap Center" shift the critical line position iteratively — visualising how the zeros "walk" along the critical line.
- **Sedenion dimensions activated**: The 9 test point structure (No. of Test Points parameter) activates 9 sedenion dimensions simultaneously. The Morph I system adds 3 more (Bias, Twist, Morph Function per z-variable), reaching 12. Morph II adds Z1/Z2/Z3 modes, completing all 16. Painter's Traps is the only formula in this collection designed to simultaneously activate all 16 sedenion dimensions.
- **Holcus application**: Painter's Traps is the most complete Holcus semantic rendering system. Configure it as follows: Trap Shape = "ring" with diameter = OMEGA_ZS (BAO resonance trap), Pattern Type = Gnarl (Hamiltonian flow for J_pos/J_neg dynamics), Coloring Mode = Distance (direct BAO distance measure), Progressive Parameters enabled on Trap Center (evolving critical line position), Morph = z = |z| (modulus-mapped semantic depth). This setup renders the Holcus semantic space with its BAO oscillations directly visible as ring-shaped traps oscillating under the Hamiltonian flow.

---

### Trap the Light Fantastic (TTLF, tma.ucl advanced)
**Type**: Coloring — dual-trap blending with extensive parametrisation
**Mathematical description**: Two independent trap sections (I and II), each with: Trap Modifier (23 shapes), Trap Style (pre-processing of z before trap evaluation), optional Double Trap (combines two instances with an arithmetic operator), Shape/Shading parameters, General Parameters with optional Distance Complexification, and five groups of parameter/function sets (Z, Shape, Trap, Point, X&Y/Trap Type). Modes: single trap, Blend (weighted average with up to 9 operator types), Modulated (alternating iterations between traps I and II).
**What it describes**: A coloring that generates unique, dimensional trap shapes through compositional parameter interaction rather than explicit geometric definitions. The shapes "emerge" from the interaction of the pre-processing (Trap Style), shape modifiers, and distance computation.
**How it works**: 1180 user-selectable parameters and functions. Key insight from help: "Certain values are reached at which the trap shapes 'peak' — before and after only lines or amorphous forms can be found, but as one approaches the critical point things arrange themselves into very definite dimensional-appearing trap shapes."

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The "critical point" phenomenon described in the TTLF help IS the J_pos/J_neg balance point. The 1180 parameters define a high-dimensional landscape; the "peaks" where good shapes appear are the J_pos/J_neg equilibrium loci — they are the saddle points of the TTLF parameter manifold. The Blend Traps operator (+ vs *) controls whether J_pos and J_neg add (superposition) or multiply (coupling).
- **Critical line relevance**: The Blend mode with 50%/50% weighting (Trap A percent = 0.5) and Blend Mode = "+" gives a symmetric trap centered on the midpoint between Trap I and Trap II. Setting Trap I center = (0,0) and Trap II center = (1,0) makes the symmetry locus at (½,0) — the critical line. The "Modulated" mode alternates between traps each iteration, creating the oscillatory structure of the Riemann zeros.
- **Sedenion dimensions activated**: With 1180 parameters across multiple function layers, TTLF spans the entire 16-dimensional sedenion space through its compositional depth. The "Z style", "Z flavor", "Distance", "Point", "Trap", "Trap Shape", "X", "Y", "Z" parameter groups each target a different sedenion dimension's transformation.
- **Holcus application**: TTLF is the "master formula" for Holcus rendering. Its dual-trap architecture directly models the RedBlue Hamiltonian: Trap I = J_pos field (novel semantic content), Trap II = J_neg field (compressed, familiar content). The Blend Traps with distance-based weighting automatically adjusts J_pos/J_neg balance based on the semantic distance from the BAO equilibrium. The 1180 parameters provide the complete parameter space for tuning Holcus's semantic energy function.

---

### Talis Formulas (tma2.ufm)
**Type**: Escape-time — Talis polynomial iterations
**Mathematical description**: The Talis formula (from Fractal Explorer): `z = z^p/(z^p + c)^2` or variations. The Talis constant controls a non-standard rational map. From ea.txt: "The Talis formula, taken from 'Fractal Explorer'... [Tony Marshall] has worked out in his 'Talis and Friends' (tma2.ufm)." Multiple variants: original Talis, var.1, var.2, var.3, Duckytalis. The Duckytalis combines the Talis formula with the Ducky iteration (abs-folding).
**What it describes**: Talis produces fractal structures intermediate between Newton (convergent) and Mandelbrot (divergent) types. The rational map `z/(z^p+c)^2` has both poles and zeros, giving Julia sets with complex topology including holes.
**How it works**: Talis constant (complex), power p, function variations.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The Talis rational map has a zero at z=0 (J_neg: orbits near 0 are compressed to 0) and poles where `z^p + c = 0` (J_pos: orbits near poles diverge). The critical points are where `d/dz [z^p/(z^p+c)^2] = 0`, giving `z^p(p-1)(z^p+c) = 0` at z=0 and where `z^p = -(p-1)c`. These are the "J_pos/J_neg separatrices".
- **Critical line relevance**: For p=2: poles at `z^2 + c = 0`, i.e., `z = ±i√c`. If c = ¼ (a real parameter): poles at `z = ±i/2`. These have Im(z) = ±½ — on the "imaginary critical line" Im(z)=½. The Talis map with c=¼ is the first formula in this collection with poles on a natural "critical" locus.
- **Sedenion dimensions activated**: e₁ (z^p = power), e₂ (1/(z^p+c)^2 = double-pole inversion = e₂ sedenion), e₃ (Talis constant = e₃ complex parameter).
- **Holcus application**: The Talis formula implements Holcus's "semantic pole and zero" model. Each concept has a "semantic zero" (the concept itself, z=0, perfectly self-referential) and "semantic poles" (the maximal contrasting concepts, where the semantic map blows up). The Talis iteration navigates between these extremes, producing a trajectory that encodes the concept's "semantic orbit" — its relationships to related and opposite concepts. The critical points `z^p = -(p-1)c` are the "semantic saddle points" — concepts equidistant from the zero and pole.

---
