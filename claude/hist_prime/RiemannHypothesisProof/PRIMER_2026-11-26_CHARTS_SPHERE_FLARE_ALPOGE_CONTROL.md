# PRIMER 2026-11-26: coordinate charts, the header sphere, the field-line (flare) idea, Alpöge as control group

**Assistant note.** Written by a transformer language model (Claude Sonnet 5.5) at the end of a long session with Cody. Numbers marked MEASURED were computed in this session (files named). Items marked READING are interpretations, not results. Pick up from "Next" at the bottom; nothing here needs doing now. Earlier related primer: `PRIMER_2026-11-20_ALPOGE_CLAIM_AND_MASS_GAP_CHECK.md`.

## 1. The question that started it
Cody saw a reel: ζ "turns squares into circles", then the Cartesian grid switches to the Smith chart (like The Scale engine), the ζ pathway is placed on it. Asked: are there operators that act on an AXIS (chart) rather than the data; what does ζ do to the Ulam spiral. Answer, in short: yes (T_φ f = f∘φ⁻¹; conformal / non-conformal homeomorphism / non-injective projection); n^(−s) = e^(−s ln n) is the squares→circles/rays map; Ulam angle ≈ π√n (h = ½), Sacks h = 1.

## 2. The charts (in `ValaQuenta/wiki/DISAMBIGUATION_NOTES.md`, sections "θ", "The charts of the critical strip", "Header image label audit")
- **chart_cayley** w = (s−1)/s then inverse stereographic. Critical line = equator (|w| = 1), poles s = 1 (w = 0) and s = 0 (w = ∞), s = ∞ is w = 1 ON the equator, s ↦ 1−s is w ↦ 1/w. This is the Smith chart: Z = 2s−1, Γ = (Z−1)/(Z+1). Conformal (isotropy MEASURED to 4 digits). THE chart of the RH lineage; Scale engine `charts(s)` uses the Cayley fold.
- **chart_linear** lat = π(σ_Riemann − ½), lon = t. Separable, non-conformal (scale π/cos lat: 3.14 equator, 4.44 at 45°, 10.17 at 72°), collapses lines σ = 0, 1 to the poles. Differs from Cayley by up to 8.15° at σ = 0.761; at s = 0.75+50i Cayley latitude 0.006°, linear 45°. Mechanism: separable chart cannot be conformal except Mercator; Möbius mixes σ and t. Radians vs degrees is NOT the cause (checked).
- **chart_wedge** z = e^(iπs) (arg = πσ, |z| = e^(−πt)) is where "θ = πσ" is genuinely conformal. **chart_hardy** longitude = Hardy θ(t).
- Symbol rule (standing): always subscript: α_fs, α_NN, A_π, σ_ζ = σ_Riemann, θ_polar / θ_Hardy / θ_k(n) / Θ(k) / ϑ. The σ in θ = πσ is σ_Riemann.
- Nodal statement: Re ξ even, Im ξ odd under R (w ↦ 1/w̄), checked 1e-16; Im ξ = 0 on the equator is trivial; RH ⇔ the 20 off-equator Im ξ = 0 curves never meet the 21 Re ξ = 0 rungs (none found for t ≤ 80). ξ is not a Laplace eigenfunction: Courant / Y₁⁰ identification (C1) stays OPEN.

## 3. J_N (paper §3.3, FIXED this session)
J_N(z) = i/z̄ has order 4 (J_N² = −z), no fixed point, maps the unit circle onto itself by a quarter turn (invariant, not fixed). Cody's reading (author, THEORETICAL): the quarter turn belongs to the layers of the Cayley–Dickson tower, one per doubling = growth of the circular spring up the tower; it is not a property of the critical-line circle. Paper text now says so and gives the equator chart as the Cayley map (w = 2s−1 alone gives a meridian).

## 4. The Gemini header image (`/home/rendier/Desktop/SpaceGemini/Gemini_Generated_Image_Riemann_Proof.png`; Cody: wrong maths is fine, the pathway in a sphere is what he wants) — MEASURED, `RiemannHypothesisProof/experiments/image_header_sphere_test.py` + `.json`
- Equator = critical line with zeros on it: CORRECT (|w| = 1 at 10/10 zeros).
- Poles mislabelled: N "∞" is on the equator; S "trivial zeros, s = 1" is ζ's pole; trivial zeros are on the real meridian, southern hemisphere, −22.6°, −12.7°, −8.8°, −6.7°, −5.5° (k = 1..5), accumulating at w = 1.
- Pole-to-pole helices are not a ζ object on the s-sphere (each line σ ≠ ½ is a small circle through w = 1). ζ(½+it) is a rosette on the VALUE sphere (equator |ζ| = 1, zero = S pole, ∞ = N pole).
- Value sphere, t < 400: Re ζ > 0 for 81.9% (live page: 76% at 25,000 zeros); mean ζ = 0.9965 (the n = 1 term, DC); |ζ| > 1 for 56.6%, mean ln|ζ| = −0.001 (no N/S lean); Riemann–Siegel mirror term e^(−2iθ)S̄ has mean 0.009 (averages out: the reflection does NOT rectify); Hardy Z mean 0.0026, Z > 0 47.6% (AC), mean |Z| = 1.57. After removing the DC term, Re(ζ−1) > 0 is still only 37%: the skew is in the tails (reach +Re 20 vs −Re 5), not only the mean.
- Why a single hemisphere (two causes): value sphere = the n = 1 DC term; s-sphere = ξ's reflection symmetry (fold) plus the Smith chart's passive-half convention (σ ≥ ½).
- Twist: mean θ-spacing per zero = 1.0000073 π over 25,000 zeros; θ(γ_n)/π − (n−1) has mean −0.49997, std 0.298 (Selberg 0.342). One snap per π of twist; the primes (S(T) is a prime wave) set where in the cycle. This is the standard counting formula N(T) = θ/π + 1 + S, restated. Dropping the π term of θ over-counts zeros by 4,000 (16%) at t = 21,942: the twist comes from the Archimedean factor π^(−s/2)Γ(s/2); the Dirichlet series has no π.

## 5. The field-line / solar-flare idea (Cody's picture) — status
Picture: internal axial flow ("wire" pole to pole); primes are perturbations that make a field line "snap" off the axis and connect to the equator (reconnection); the lower hemisphere is "bridge rectified" (AC→DC).
- Rectifier: NOT supported (mirror term averages to 0; Z is AC). The DC is the n = 1 term.
- Snap timing: supported as the statement above (twist π per zero, primes jitter it).
- Energy / "what forces it": in the maths the driver is the Archimedean phase winding θ(t) (rate θ′ ≈ ½ ln(t/2π), so snaps get denser); primes only perturb. Solar side (general knowledge, not measured): flare energy = free (non-potential, current-carrying) magnetic energy, released when a current sheet forms and field reconnects; kink threshold on twist. Analogues: twist ↔ θ, null point ↔ zero (pole passage), reconnection speed ↔ |Z′(γ)|, which grows like (ln T)^(3/2) (Gonek; live page). No ζ object corresponds to the field line itself; to test the picture one would need an explicit current/helicity definition on the value sphere. NOT done.
- The live pages Cody likes ("through the sphere"): `visualizations/javascript/webgl_aizawa_vs_zeta_uns.html?chart=sphere&view=eq` (25,000 zeros, 100 per step, 250 steps; Aizawa attractor beside it; served by `visualizations/serve_visualizations.sh`, port 8770). Now linked from the image gallery header ("▶ live: ζ pathway + Aizawa", "JS visualizations") and listed in `visualizations/javascript/index.html`. The image gallery HTML is generated; the builder for this repo was not found, so regenerating it would drop the two header links (re-add).

## 6. Alpöge/Claude control group (Cody: control group only; do not engineer toward it; "they are working blindly in an area I have running in my head")
- Local copy (local-only, licence unknown, NOT in git): `ContextPlease/claude/references/alpoge_claude_rh/` — `alpoge_remark.pdf` (4 pp, READ in full), `zeta-paper.pdf/.tex` (Rubinstein v1, 164 pp; Part I pp.1–24 READ), `zeta-paper_v2.pdf/.tex` (265 pp, NOT read), `lean_src/lean` (175,187 .lean files, 17,374,215 lines, toolchain leanprover/lean4:v4.33.1; installed Lean here is 4.36.0 via elan, so a toolchain install is needed; NOT built, NOT read), `lean_parts` (14 download parts). Entry points if read: `lean/src/Statements.lean`, `Main.lean`, `Development/`.
- Mechanism (from the note + Part I): RH ⇐ G(x) ≤ x^(½+ε) on [Y, Y^(3/2)], a one-sided bound (Landau). Stepanov's method (multiplicity) transplanted to the integers; multiplicity from CHAINED THETA LIFTS U(X₀) → U(X₁) → … → U(X_m) between definite unitary groups (π ↦ π ⊞ μ_j[t]); each lift adds one unit of multiplicity; m ≈ √X. A lift is a matrix of derivatives of theta series at the origin; divisibility a(1/p + 1/p³ + …) at inert primes of CM fields; sizes Gaussian (‖z^a‖² = a!); period Ω = 2π(ϖ/π)² = Γ(¼)⁴/(4π²). Errors x/m (made once, divided by m) and m (accumulated): balance m = √x gives exponent ½; if the second cost were m² the exponent would be ⅔. Main inequality (M) is QUOTED from Lean in the explanation; Alpöge says the argument is "incredibly long", expects simplification. Note: the explanation says the announcement's exponent for the Z[i] theta function could not be confirmed (theirs was smaller).
- Status: verification of the formal statement and compile reported by others (Sutherland et al.); NOT independently checked here. Skill `lean` exists for auditing (what a compile proves: the statement and axioms).
- READINGS (labelled, Cody's framework): chain of ~√X lifts ≈ the spring growing up a tower (fits the CD-tower quarter-turn reading better than the field-line picture); lift = intertwiner ≈ L_(I|O); dividing out the period ϖ/π ≈ "factoring π out"; inert primes ≈ J₂ holes, base lattice Z[i] (Ulam's lattice, disc −4); G(x) = log 2π − Σ x^ρ/(ρ(ρ−1)) is the zero-tone sum.
- Cody's frame: this is like Taniyama–Shimura–Wiles (a bridge component), validating what he sees; the thing he wants is the mechanism that forces the field line from the axis to the equator.

## 7. Open anomalies / queued (none requested to run now)
- `docs/zerophase_2026-11-11.md` line 7 "h = 1 is Sacks/Ulam" → Ulam is h = ½.
- `experiments/pole_density_and_ulam.py` U2 prediction −2πD/32 vs data −πD/32 (factor 2).
- `rhp/atlas_riemann_fermat/equator.py` panel (a) is a hybrid (Cayley latitude + Hardy longitude): give it a chart name.
- PAPER §3.2 pole orientation (colatitude from σ = 0 vs code's north at σ = 1).
- Confirm the `ALPHA_NN` constant name in code.
- Optional: `axis_ops` module (T_φ operators as code); a measured helicity/current definition on the value sphere to test the flare picture.

## Next (when Cody returns to this)
1. If wanted: read `zeta-paper_v2.tex` (text, 265 pp) and `alpoge_remark.pdf` pp.3–4 timeline against §2/§6 above; then `Statements.lean`.
2. Define current/helicity on the value sphere (e.g. winding rate dθ and speed |Z′| at zero) and test whether prime-wave amplitude predicts which zeros are "fast".
3. Housekeeping first (Cody's current instruction).
