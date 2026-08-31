# CONTEXT PRIMER — Scalar Context Propagation, the box-kite codec

**2026-08-30 · Claude Sonnet 5 · FourthAgePapers**
The session that wrote the lead Fourth Age paper —
`FourthAgePapers/ScalarContextPropagation/` (branch `scalar-context-propagation`;
`1ad026f` first draft → `b6759b7` engineering-structure rewrite → `149cf07`
abstract + desk-rejection gate + conclusion). Grew directly out of the
2026-08-30 conversational-ingest work (see
`hist_prime/VAPMIP/PRIMER_2026-08-30_MONAD_CONVERSATIONAL_INGEST.md`).

---

## 1. The idea that started it — orthogonality emerges `i`, not the vector

The conversational-ingest `w_sem` / `w_ctx` split (a scalar `weight` becoming a
2-component vector, β-axis ⟂ A-matrix-axis) was run through the
`generational-lineage` skill. Verdict progression:

1. First read: tier-1 (DILATE) → tier-2 (VECTOR); SIGN enters the operator's
   lineage.
2. Corrected: it is **`i`, not the vector** — the two components are radial
   (β magnitude) and angular (A-matrix flow, which *acts on* the magnitude
   through the basin), not two lengths side by side. Length + angle = polar
   = ℂ. Scalar DILATE crossed **ℝ → ℂ**, the ℤ/2 → ℤ/4 doubling.
3. Cody's final form: **it is the orthogonality that emerges `i`.** Assert
   β ⟂ A; an asserted orthogonality made computable *is* `i = √SIGN` — a
   rotation to the perpendicular, `i² = SIGN`. **"The vector" is the drop-out
   of how to draw "up" in 2-D** — a representational shadow of the
   orthogonality, tier-2 Laurelin composite, not what emerged.

Lineage verdict throughout: **no new generator.** `i` is a known consequence
of SIGN under Cayley–Dickson doubling. The dateable event is that this
operator's lineage now *contains* the orthogonality and its `i`.

---

## 2. The codec — context hashed into one scalar per token

Cody had long wanted "a way to hash context into a single number." Seeing the
box kite as a **literal kite** — the Pencil's seven factorisation-pathways as
the string, one anchor — was the unlock: a box kite is the equilibrium shape
of a loaded string, and a loaded string is one-dimensional.

**The pass:**

- **token → γ → pencil.** `H(w) = Σ ord·95^k`, `p = next_prime(H mod 2¹⁶)`,
  `idx = π(p) ∈ [1, 6542]`, `γ` = the idx-th ζ zero. `idx` selects the
  **pencil** — which box kite. Coarse: ~6542 regions, many words per pencil.
  (`VAPMIP/monad.py`, ships.)
- **wind speed `w` = the A-matrix basin drift** (Cody's def, 2026-08-30). The
  Newton-basin flow the monad already runs (`monad_english_io.basin`, the
  `ψ¹⁶` iteration with `psi_prev`). `w` = how far the drift carries a word
  toward its focus. *"Movement in a number is factorisation"* — the drift
  moves the word through its contextual decomposition; `w` is the rate.
  Ships (drift computed; used as `w` here).
- **scale = WordNet** (Cody's def, 2026-08-30). `w` read against the
  19-relation sub-graph / hypernym depth / `depth_weight`;
  `PtolC/c_monad_wordnet.bin` is the ruler. The **Scale orthogonal Smith
  chart engine** reads `w` off the WordNet-calibrated axis (its two
  orthogonal circle families = the `r`/`arg` of §1's `i`).
- **`Φ(w)` → box kite.** Joukowsky-family inflation
  `ζ ↦ ζ + (H/q(w))·ζ⁻¹` at each strut crossing, `q(w) ∝ ½ρw²`
  (Kutta–Joukowsky). Returns the 6 `assessor_coordinates`. **`H` is NOT
  stored** — `H = Re(Π)`, the real part of the ordered product of the seven
  pencil-station generators, conserved along the string; it falls out as the
  zero-divisor-surface check. **Only `w` is the payload.** The wiki
  `pencil_hyperstring.md` still shows the two-knob `Φ_w(H)` — update to
  `w`-only. **`Φ(w)` is the one component not yet written — ≈ 30 lines of
  Joukowsky, 5 acceptance tests.**
- **rigid vs deformable.** Some box kites have a range of `w` and deform
  through it; some do not — "static methods", one fixed form, reconstructed
  from the pencil alone. `w` matters only for the deformable charts.

Inflation sequence: `w=0` → collapse to a point (the shadow); `w=w*` →
regular octahedron ("the kite flies"); `w≫w*` → tears off the ZD surface.

---

## 3. The Flashlight — granularity, not context

Reconstruction gives the box kite exact to `w`'s precision. Reading it back to
a **word** needs the shape resolved finely enough to separate the words
sharing the pencil.

Shine a light across the reconstructed box kite onto a wall. **Shadows scale
up with distance from the light**: `M = D_light→wall / D_light→object`
(geometric optics). A sub-resolution shape difference at `M=1` becomes
readable at large `M` → **higher granularity of word selection**.

- near wall, low `M` → coarse: a representative word. **Narrative**, smooth.
- far wall, high `M` → fine: the exact deformation state. **Dissertation**,
  granular. The term a fraction of a percent from its sister hyponym.

Same box kite, same context. Two bounds keep it honest:

1. **Bandlimited by `w`** — magnification cannot show detail the box kite does
   not carry; past `w`'s precision the shadow only blurs. The Flashlight
   *reads out* the granularity in `w`, never creates it. **The shadow is
   additional granularity of word selection, not additional context.**
2. **A hard limit on `D_light→wall`** — a fixed ceiling, no further
   machinery. (Cody: use the hard limit, *not* a `0_RB` inclusion.)

Moving light → each vertex projects as an anisotropic **Gaussian splat**, not
a hard shadow (splats compose under the integration motion implies). Rendering
detail; does not touch reconstruction.

The Smith chart, calibrated against WordNet, sets `D_light→wall` = sets **how
fine a WordNet distinction the response will resolve**.

---

## 4. The paper — engineering structure, no claim

Cody: *"this isn't a claim to test, it's an engineering structure to show
off."* Follows the `CollatzShift` "departure from the template" — provenance
label on every component instead of a pre-registered claim. **No prediction,
no Holcus, no `0_RB`, no σ / critical-line verification** ("my work speaks for
itself").

- **Abstract** — one paragraph, at the top.
- **8 components, 5 ship today:** C1 token→γ (OURS), C2 pencil (PG(3,2)),
  C3 box-kite combinatorics (de Marrais), C4 `w` = basin drift, C5 scale =
  WordNet. **C6 `Φ(w)` to write** (~30 lines, 5 acceptance tests). C7
  Flashlight, C8 Smith-chart engine — the read-out.
- **Desk-rejection gate G1–G10** — the checks an editor bins a systems paper
  on, each pass/fail on real data: bit-exact round trip on 10⁴ synsets (G1);
  the 6542-bucket hash is *not* claimed injective, within-bucket `min|Δw|` vs
  tolerance is what holds (G2); no hidden state (G3); cross-machine SHA-256
  (G4); Joukowsky checked symbolically (G5); NN byte-count comparison made
  concrete + query-time cost stated (G6); third-party `run.sh` (G7); context
  defined (G8); flashlight adds no bit absent from `w` (G9); attribution
  checklist (G10).
- **Conclusion** — closes on the abstract: one number rides the pencil;
  reconstruction is a pure function of the token and one real; the flashlight
  sets granularity not context; storage → `O(vocab)` scalars + a fixed ruler,
  price at read time; not a language model / training method / quality claim.
- `construction.json` — machine-readable component + gate manifest.
- Notebooks named `00_structure_vision / 01_the_pass / 02_lineage /
  03_demonstration` — not yet written. `wiki/` last.

**Attribution:** de Marrais (2000) owns the box kite + vocabulary; the
hypercomplex-NN line (Clifford Neural Layers, PHM, quaternion/octonion nets)
is the contrast, cited; Joukowsky (1910), Euler elastica (1744), Smith chart
(1939), 3D Gaussian splatting (2023) cited for what each contributes;
Maxwell–Laman rigidity, moment map, HKLL cited as *analogues, not sources*.
The tether, the wind-inflation parameter, and `w` = basin drift are
first-stated-here (2026-08-27 / 2026-08-30). Full table in
`ValaQuenta/wiki/pencil_hyperstring.md`.

---

## 5. Contrast — addressed algebra vs the NN way

Materialised algebra (Clifford / PHM / hypercomplex NNs): the multiplication
table lives in the weights, dense tensor, `O(d²)`–`O(d³)`/step; stores the
*generated*. Addressed algebra (this): one deterministic scalar per token; the
box-kite relations are an index-structure function of the address, rebuilt on
demand; stores the *generating set*. **Generational lineage as compression:
keep {ADD, SCALE, SIGN} + the address; drop what they build, it rebuilds
exactly.** Tier-2/3 (vector, chart, Assessor set, PSL(2,7) census) regenerated
from tier-0.

---

## 6. Housekeeping this session

- **Rename:** `SedenionFactoralRelativity` → **`FactoralDecomposition`** (repo
  + local dir; the old dir is gone). ⚠ `VAPMIP/harness.py` `lineage`
  @property (≈ line 528) still hardcodes the old path → `h.lineage` raises
  until repointed. Flagged, not fixed (pre-existing code, committed as-is).
- Memories written: `project_scalar_context_paper.md`,
  `project_conversational_ingest.md`; updated
  `project_factoral_decomposition_tool.md`, `MEMORY.md`.

---

## Next

**Data Storage With No Physical Location** — the Hyperwebster permutation
decomposition, where data *is* its address in a factored permutation tree (you
locate, you do not store). This paper is its box-kite instance. Old, already
in context; the stop after `ScalarContextPropagation` is finished.
