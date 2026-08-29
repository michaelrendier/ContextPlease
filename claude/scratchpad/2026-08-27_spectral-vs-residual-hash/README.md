# spectral-vs-residual-hash — 2026-08-27

## Question (Cody)
"spectral decomposition" was used loosely as a name for *a* decomposition.
IF the phonetic/stress side is genuinely SPECTRAL (orthogonal modes,
conjugate faces — reCORD/REcord differ only by the phase of the stress
spectrum), THEN the prime SEMANTIC hash should be RESIDUAL in nature —
*because residuals can overlap and an orthogonal basis cannot* — and the
residual can be the Smith diagram's 4D (the object the Möbius fold eats).

## Files
- `test_spectral_vs_residual.py` — the test (venv: `../ValaQuenta/.venv/bin/python3`)
- `run_output.txt` — captured run

## Result — directionally right, imprecise as stated

### Phonetic side IS spectral (conjugate faces confirmed)
- **97.1%** of stress-moved heteronym pairs (140 found) have EQUAL
  magnitude spectrum + MOVED phase. `annotates (2,0,1)↔(1,0,2)`,
  `advertised (1,0,2)↔(2,0,1)` — literal reflections. reCORD/REcord is a
  real conjugate-face pair: same segmental norm, phase-shifted stress.
- Stress vectors are strongly low-rank (participation ratio 1.38 at L=2 —
  one dominant contrast mode). NB the in-script "DFT must diagonalise"
  check is a BAD discriminator (forces a Fourier basis; stress isn't
  translation-invariant, position 1 is privileged) — ignore that flag.

### Semantic hash IS a ~4D spectral object (not an overlap-soup)
- 19 relation components are **near-uncorrelated** (mean |off-diag r| =
  0.046; only 2.3% of pairs > 0.3). Not "residual that overlaps" at the
  component level — closer to a sparse near-orthogonal frame.
- Effective dimension **≈ 4**: participation ratio 4.26 on all 19 dims,
  **3.94 on the 9 columns that actually fire** → the 4D is NOT a
  zero-padding artifact.
- 4 interpretable orthogonal modes, ~75% of energy:
  - mode0 (40%): hyponyms — category-hub / branching factor
  - mode1 (17%): similar_tos vs hypernyms — satellite(adj) vs taxonomic(noun)
  - mode2 (10%): member_meronyms + member_holonyms — part/whole
  - mode3 ( 8%): instance_hypernyms + part_* — proper-noun / physical composition

### "Residual" holds for the LEADING mode only
- Removing mode0 raises WordNet-supersense Fisher separation
  **0.341 → 0.619**. Mode0 (branching factor) is shared scaffolding that
  *suppresses* meaning discrimination; the meaning-bearing signal is the
  **~3D residual after mode0** (modes 1–3).
- Removing >1 mode degrades separation (0.33, 0.24, …) — it's specifically
  mode0 that's boilerplate.

### "Residuals overlap" — visible in the multiplicative code, not the vector
- related-pair vs random-pair cosine of `context_vector`: 0.463 vs 0.487
  (related NOT more overlapping).
- related-pair vs random-pair shared-prime-factor overlap of
  `context_code`: **0.859 vs 0.698** (related DO share factors).
- So the *multiplicative* hash overlaps for related concepts; the additive
  vector form does not cluster by relatedness.

### Smith 4D — the prediction that fired cleanly
- Two independent measures land at ~4 (4.26 full, 3.94 live-cols).
- Residual after mode0 ≈ 3D.
- Möbius fold on residual coords currently **saturates** (20% of |Γ| >
  0.99) — a min-max-on-heavy-tails normalisation bug, same class as
  constructor.py BUG 1. Fixable, not fatal.

## Sharper statement the data supports
- `context_vector` is already a ~4D spectral object with 4 nameable
  relational axes.
- Its 1st mode (hyponym branching) is shared scaffolding; the
  meaning-bearing part is the ~3D residual after removing it.
- That residual is a legitimate candidate for the Scale engine's Möbius
  fold (primer Part 4) — once the normalisation is fixed so |Γ| doesn't
  saturate.
- Apply the same degeneracy discipline (J_red/J_blue, constructor BUG 1/2)
  before trusting any specific retooling.
