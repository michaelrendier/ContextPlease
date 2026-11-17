# 137 — The Circle Atlas

**Written 2026-11-16.** Engine `ValaQuenta/modules/circle_atlas/` (v0.1), notebook 22, tests `ValaQuenta/tests/test_circle_atlas.py`. Pointer, not authority: the code and Cody's current statement win.

**Name.** The Circle Atlas, sixth in `ContextPlease/claude/ATLAS_REGISTRY.md`; paper *The Circle Atlas: H_hat_RB and The Complete Shape of Mathematics* (FourthAgePapers/TheInterface).

**Why it exists.** Cody's question: if all of mathematics is contained in Ĥ_RB (0_RB: 16 dimensions in, 16 out, one real and fifteen imaginary), where is each piece, and how is it reached? The boundary where inside and outside meet is the Interface. The Atlas is the map of the roads *into* a circle (the fixed-point space, a circle with no inside or outside) and *out of* it. Pages are viewports: a Lagrangian does not look like a circle, but its stationary-action path, taken to phase space, is one.

**How it is built.** A mapping algorithm, not a fit. Each viewport is run: TO (the transformation that enters the circle, with the residual from |z| = 1) and FROM (the transformation out, with the fibre of choices it needs). FROM is a relation, not the inverse function: the Lagrangian L, 3L and L + d/dt F share one stationary path, so running a Lagrangian backwards from a circle is underdetermined; the Atlas measures what must be chosen instead of pretending there is an inverse. Every viewport also carries a π route (the π Derivation Toolset, 138).

**What it found.** Nineteen viewports; eighteen close on the circle to numerical zero. One does not, and says so: Berry–Keating H = xp is a hyperbola (residual 6.4), and becomes the circle x₀eⁱᵗ only under the Wick rotation t → it. In the sedenion every one of the 15 imaginary axes gives an exact circle, the 84 zero divisors are circles too, and the 336 ordered annihilating pairs are where two circle points multiply to zero; a generic pair never does (0 of 300). SIGN (θ → −θ) is carried by the whole second octonion e₈…e₁₅, not by one axis (the sign test).

**Gaps.** Four viewports have no π route yet (Apollonian, inversion, BAO ring, retraction). Named gaps: elliptic curves and modular forms (a torus is two circles; Ramanujan's route to π lives there), string-theory cardioid superstrings, wing and bell motions, 5:5:5 and 2:11:2 frames, data for BAO/CMB, and the point that becomes a circle still empty inside (the polar blow-up of a point is a candidate; INTERPRETATION).

**Census.** A text count of circle-bearing tokens over the repositories (GenerationalLineage 100 files, ValaQuenta 228, RiemannHypothesisProof 118, VAPMIP 308, FourthAgePapers 87, …) tells where to look next; the import probe found 69 modules and toolsets, none failing to import.

**Labels.** Each viewport's closure ESTABLISHED (numerics); reading TO/FROM as entry and exit of fixed-point space THEORETICAL; the point-to-circle reading INTERPRETATION.
