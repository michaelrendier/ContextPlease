# Session Context — 2026-07-28/29

Working record of the session that drafted the first three CS-framed Fourth Age
papers. Written to seed the finalised rewrite of the Ainulindale CS Paper.

Read this before starting the next paper. It carries the framing, what was
verified, what was found broken, and what not to repeat.

---

## 1. The framing that applies to every remaining paper

Stated by Cody, 2026-07-29:

> One at a time. First drafts. Purity and shortness of context per paper is
> best. This will be seeding a finalised rewrite of the Ainulindale CS Paper.
> **All papers are Computer Science in nature — no "conjecture", no "open
> problem".** This is PURELY *"Look at my code. It runs, doesn't fault, and
> produces the right answers."*
>
> The Monad is the Third Age CS paper; it and its components, and VAPMIP in
> general, are **not** necessary for this project.

Consequences, applied throughout:

- **Every prediction must be settleable by execution.** If running code cannot
  decide it, it does not go in.
- **No external datasets.** All three papers so far compute every value from a
  definition. This is a feature of a CS paper, not a limitation: the data *is*
  the execution.
- **Modules whose confidence floor is `OPEN` or `CONJECTURE` are unusable** as
  written, because the module itself declares unfinished business. That rules
  out `berry_keating` (floor OPEN, 0/6 ESTABLISHED), `clay_millennium` (6 of 7
  problems open by definition), `noether_information` (CONJECTURE), both
  translators (OPEN, known failure), `tier9_chem` (no data loaded).
- **Exclude Monad/VAPMIP dependencies.** Where an engine reaches for
  `monad_sedenion.bin` or similar, that is a signal the claim is not
  self-contained.

## 2. The Fourth Age Protocol, as practised

Four notebooks, fixed names, one directory per paper:

| Notebook | Role |
|---|---|
| `00_holcus_vision` | The single claim. Names Engine / Data / Wiki up front. |
| `01_predictions` | **Pre-registered.** Dated. Each P has a derivation and an explicit falsification criterion. Registered as executable assertions, *defined* here and *run* in 03. |
| `02_data` | Provenance of every quantity, then the runs. |
| `03_results` | Scoreboard: CONFIRMED / PARTIAL / **FAILED** per prediction. |

The load-bearing rule, quoted in every `01_predictions`:

> Results — confirmed or failed — remain in the record. Failed predictions stay
> in the data, period, full stop.

**Wiki is written LAST.** None of the three papers has a wiki page yet. That is
correct, not an omission.

### Two additions made this session, worth keeping

1. **A "What this paper does not show" section in `03_results`.** Drawn by the
   author before a reviewer draws it. Each of the three papers states plainly
   what it does *not* establish.
2. **Predictions that are the module's own documented claims.** In
   SonificationEncoder, P3 and P4 are registered *from the engine's own
   docstrings* so the record shows whether the documentation is accurate. Both
   failed. This is a good pattern: it turns documentation into a testable
   artefact.

### Path convention — important

Use:

```python
sys.path.insert(0, os.path.abspath('../..'))
from ValaQuenta.modules.X import maths
```

`FourthAgePapers/<Paper>/` → `../..` is `ThePlace`, which holds the `ValaQuenta`
package.

The older papers use `'../../../ValaQuenta'`. That does not resolve on the
phone, but it is **not a mistake** — it is correct for the laptop layout, where
`FourthAgePapers/` sat inside `Ainulindale/` on the SD card
(`/media/rendier/0123-4567/Ainulindale/FourthAgePapers/<Paper>/` → `../../..`
= the card root, so `../../../ValaQuenta` is the sibling repo).

**Standing instruction from Cody, 2026-07-29: all old laptop references stay.**
The SD card in this phone *is* the laptop's card, and the work goes back to a
computer. When a notebook needs to run in both places, **add** a portable
`sys.path` entry next to the laptop one — never replace it. Python ignores a
`sys.path` entry that does not exist, so carrying both is free.

This was applied to the four `singularity_null` / `turing_diagonal` notebooks in
ValaQuenta, which now carry both. The eight FourthAgePapers notebooks
(Telperion, ZeroTree, NoetherWiles, FermatMonster, MonsterSiblings) still carry
the laptop form only; if they are ever needed on the phone, add — do not
substitute.

---

## 3. Papers drafted (all execute clean, none has a wiki page)

### HaltingDiagonal — 4/4 confirmed, 19/19 cells
Engine: `ValaQuenta/modules/turing_diagonal`

**Claim:** Cantor's diagonal, Gödel's *G*, Turing's *D(D)* and the Enigma
reflector are one operation — a fixed-point-free involution — and the escape
property underlying HALT's undecidability is itself decidable in linear time.

- **P1** the escape depends *only* on `diag(T)`, never the other `n²−n` entries,
  so exhaustive verification costs `2ⁿ` not `2^(n²)`. Checked to `n=16`: 65,536
  diagonals standing in for `2²⁵⁶` tables. **This is the best result in the
  paper** and is original to the framing.
- **P2** `D_n` exact by inclusion–exclusion, recurrence and `round(n!/e)`,
  agreeing on integers to `n=60`. `D_26/26! − 1/e = 0.0` in float64 — the
  alternating series converges below machine epsilon by 26.
- **P3** involution order 4; exactly 15 sedenion units square to −1, `e₀` unique.
- **P4** reflector derangement prunes crib alignments to `(1−1/A)^L`, within 0.6%.

**Deliberately excluded:** `prediction_diagonal_test()`. It classifies English by
substring-matching a keyword list. `03_results` demonstrates the failure — the
liar paradox in English returns depth 2 "undecidable", the same sentence in
French returns depth 0 "trivially true or false". It supports no claim.

### NBallTransformer — 3/4 confirmed, 23/23 cells
Engine: `ValaQuenta/fixed_point.py`

**Claim:** `V(n) = π^(n/2)/Γ(n/2+1)` is the CD layer transformer; `V(2)/V(1) =
V(4)/V(2) = π/2` exactly; breaks at ℍ→𝕆 where `V(8)/V(4) = π²/12`.

- **P1** proved **symbolically** (sympy), not numerically — deliberately, because
  the float64 ratios are *not* bit-identical to `π/2` even though the identity
  is exact. An exact identity and a 15-digit numerical coincidence are different
  claims and only the first is safe to build on.
- **P2** `V(n) = (2π/n)V(n−2)` exact.
- **P3 FAILED** — `v_nball` is not correctly rounded: 21 ulp at `n=11` against a
  4 ulp bound. **The bound was not loosened after seeing the number.**
- **P4** root find beats the engine's 10,000-point grid by ~3e11 in accuracy for
  ~800× less work.

### SonificationEncoder — 2/4 confirmed, 16/16 cells
Engine: `ValaQuenta/modules/sonification`

**Claim:** the map is exact rational arithmetic but lossy in two independent
ways.

- **P1** all 30 tones are exact `Fraction` just ratios of A440, all 5-smooth,
  largest denominator 32. The module could have used `440·2^(k/12)` — irrational
  for every non-octave interval — and did not. Real design merit; the paper says so.
- **P2** `ω = 2πf` round trip costs at most 1 ulp.
- **P3 FAILED** — the map is **not injective**: 30 names → 23 frequencies, seven
  collision classes, 0.383 bits lost per symbol. The audio stream is not
  uniquely decodable.
- **P4 FAILED** — `QUASIPARTICLE_RESTS` is labelled *"exact integer arithmetic"*
  at ESTABLISHED; four of six discard a fractional sample through `//`.

---

## 4. Claims investigated and REJECTED — do not build papers on these

This is the most important section for the CS-paper rewrite. Each of these
appears in `README.md` or `TODO.md` as a result. None survives inspection.

### 4.1 `sedenion_operators` (tier8_sedenion) — TODO calls it "MAJOR. No free parameters."

Three independent failures:

1. **The headline ratio is algebraically vacuous.**
   ```python
   D_ratio = D_STAR / (sigma_mean * D_STAR)   # = 1/sigma_mean
   ```
   `d*` cancels. The code's own comment admits it. So "d*/(σ̄·D*) ≈ 1" says
   nothing about `d*`. And it is not ≈1: **it evaluates to 85,079.**

2. **Two outputs read as confirmations but are errors.**
   `sigma_mean_vs_OMEGA_ZS = 0.567132` sits beside `OMEGA_ZS = 0.56714329` and
   looks like a match. It is `abs(σ̄ − Ω_ZS)` — the *error*. It resembles Ω_ZS
   only because `σ̄ ≈ 1.2e-05 ≈ 0`. Identically for
   `d_star_vs_sigma_mean = 0.245988` against `d* = 0.246`.

3. **The stated premise is false.** The docstring says the 16 σ-addresses are
   "spread across [0,1]" and "cluster at σ=½". All 16 sit below `2.2e-05`
   (`hash/(10⁹+7)` is tiny for short strings). Operators within 0.1 of ½:
   **0 of 16.** The dict also carries `perfect_bijection: False`,
   `10/16 dimensions covered`, and a `monad_sedenion_bin` dependency marked
   "verification pending".

The docstring makes three mutually inconsistent claims about what the ratio
should be (`≈1`, `≈2`, `σ̄ = Ω_ZS`). **This needs a rethink before it is a paper
and must not enter the CS rewrite as-is.**

### 4.2 D7 Schumann — "zero-parameter prediction"

`f_n = (c/2πR)√(n(n+1))` gives **10.46 Hz** against a measured **7.83 Hz** — a
**25.14% deviation the engine reports itself** (`deviation_pct` in
`spherical.schumann_frequencies()`). That is the textbook lossy-ionosphere gap;
the ideal perfectly-conducting cavity always overestimates. Further, only `n=1`
has a stored measured value, so modes 2–7 cannot be checked at all, and the
cavity radius 6451 km already embeds an 80 km ionosphere height — itself a
parameter. **Not zero-parameter, and not confirmed.**

The module was reframed as an *encoder* instead, which is what produced the
SonificationEncoder paper.

### 4.3 The entire D-series (D1–D16) has no engine

Every engine path named in `TODO.md` for D1–D16 is **missing**:
`modules/berry_keating/d_star_empirical.py`, `modules/jwst/bao_lambert.py`,
`modules/hyperwebster/zipf_prime_test.py`, `modules/jwst/cmb_riemann_peaks.py`,
`modules/berry_keating/mass_gap_spectral.py`,
`modules/sonification/schumann_verify.py`,
`modules/noether/navier_stokes_cr.py`,
`modules/berry_keating/chladni_prime_gap.py`,
`modules/noether/gw_ringdown.py`, `modules/noether/eeg_riemann_bands.py`,
`modules/berry_keating/gap_empirical.py`,
`modules/noether/crawford_rotating_outflow.py`.

Only **D17** points at real code (`galactic_cavity.py`). Most of the rest also
require external datasets (LIGO, PhysioNet, Planck FITS, TCGA), which cuts
against the "no external data" posture. **The D-series is aspirational, not
built.**

---

## 5. Engine defects found (ValaQuenta, all fixed or recorded)

Fixed in ValaQuenta `main`, commit `b0c98c8`:

- **`tier7_cosmos` and `tier9_chem` could not be instantiated at all** — neither
  implemented the abstract `viewer_data`, so neither could register. Their
  notebooks only worked by importing `maths.py` directly, bypassing the
  registry. Fixed; +21 reachable equations.
- **Four notebooks hard-coded `/media/rendier/0123-4567`** — unrunnable
  anywhere else. 0/38 cells → 38/38.
- **`notebooks/core/` was written against an older `maths.py` schema** —
  renamed keys, removed functions. 41/83 → 94/94.
- **`critical_line_samples` re-ran the full 84-pair ZD search per sample point**
  (`zeta_geometric` defaults `pairs=None`), making the n=2000 sweep take ~30
  minutes. Hoisted out of the loop: **bit-identical results, ~11,000× faster.**
- **`ZeroLattice/03_results.ipynb` P2 had a misplaced parenthesis** —
  `bool(a|b) & frozenset` raised `TypeError` and **masked a genuinely failing
  prediction.** Fixed; P2 now honestly reports FAIL.

Recorded, still open:

- **`noether.forced_sigma` converges to σ=½ only for `E ≲ 10`.** Above that the
  softmax iteration exits on its first step and returns `σ₀` unchanged; for
  `σ₀ < 0` and large `E` it raises `OverflowError`. **The `E=100 → 0.500000000000`
  figure in README and wiki does not reproduce** and has been corrected. The
  analytic derivation (F=B ⟹ σ=½) is unaffected, as are the independent
  derivations in `hamiltonian.py` and `understand.py`.
- **ZeroLattice P2 is FALSE** — "Monster gap in ALL odd-sector pairs": 10/12
  directed pairs meet `MONSTER_GAP={1,11,15}`; one unordered class,
  `{(3,9),(7,13)}`, does not.
- **`fixed_point.v_nball`** off by up to 21 ulp; **`v_nball_peak()`** returns
  `n*=5.256606` while the module's own `N_STAR` is `5.256946` — they disagree at
  the 4th decimal. Anything quoting `n* = 5.2570` quotes the constant, not the
  function.
- **`sonification.FREQ`** not injective; **`QUASIPARTICLE_RESTS`** mislabelled
  exact.

---

## 6. State of ValaQuenta (companion work, same session)

On `main`, commit `b0c98c8`. Visitor-ready:

- **37 wiki pages** (was 11) — one per engine. Every Results block generated by
  importing and running the engine.
- **70 notebooks**, **393/393 code cells execute clean.**
- `requirements.txt` derived by walking the AST of every `.py`/`.ipynb`.
- `install.sh`, `install-macos.sh`, `install.ps1`, and `verify_install.py` —
  which recomputes GAP from its inputs, checks `Ω_ZS·e^{Ω_ZS}=1`, counts the 84
  ZD pairs and confirms `H=xp` conserves energy. Imports passing only proves
  files parse.
- `wiki/00_index.md` carries a **Known defects** table. Start there.

**Security note:** `ValaQuenta/.git/config` still embeds a GitHub PAT in the
remote URL (`ghp_…`). Not pushed with commits, but it leaks if the directory is
zipped or shared. Scrub when the new token lands:
`git remote set-url origin https://github.com/michaelrendier/ValaQuenta.git`

---

## 7. Candidates for the next papers

Engine exists in ValaQuenta, no paper directory yet, no external data:

| Candidate | Engine | ESTABLISHED / runs | Note |
|---|---|---|---|
| `singularity_null` / Zero Divisors of S¹⁵ | `modules/singularity_null` + `zero_lattice.py` | 4/5, 5/5 | Exact counts 84/42; `tan(π/8)` residual 1.11e-16. Overlaps ZeroTree. |
| `pilot_wave` (D17) | `tier6_physics` + `galactic_cavity.py` | 8/10, 10/10 | Needs SPARC data for the physics claim; a CS framing would avoid it. |
| `lagrangian_identity` | `h_rb_hat` | 10/16, 16/16 | The "97% overhead" claim is unverified — check before drafting. |
| `hypercomplex_spectral` | `modules/jwst` | 3/5, 5/5 | **Synthetic spectra only** — no real JWST data is loaded. |

**Method that worked, and should be repeated:** verify the claim *first*, with
independent code, before writing a single notebook cell. Two of the four
candidates investigated this session (`sedenion_operators`, D7 Schumann) did not
survive that check. Writing the paper first would have produced two papers
asserting false results.

---

## 8. Environment notes

- Commit everything locally, always; **never push**. Cody pushes in one batch
  from a computer. All repos on `main`.
- The sdcard cannot hold the exec bit, so `.git/hooks/pre-commit` is silently
  skipped and shell scripts need `bash install.sh`, not `./install.sh`.
- `jupyter` is not installed on this device. Notebooks were verified by
  executing every code cell in order in a shared namespace with the `Agg`
  matplotlib backend — equivalent to a kernel run, and the reason "393/393
  cells" can be asserted.
