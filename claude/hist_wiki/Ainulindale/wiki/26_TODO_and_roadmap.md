# 26 — Paper programme and validation engines: status as of 2026-11-13

| | |
|---|---|
| Replaces | the 2026-06-13 "TODO & paper roadmap" (a plan, now historical; its D-CS / D-M / D-P / D-CHEM split was superseded by the FourthAgePapers programme) |
| Sources | `FourthAgePapers/` (31 directories, git dates read 2026-11-13); `Ainulindale/AgeThird/`; `VAPMIP/engines/` (13 engines run 2026-11-13, outputs in `ContextPlease/claude/scratchpad/2026-11-13_ainulindale_audit/engine_runs/`) |
| Living lists | `Ainulindale/TODO.md`, `Ainulindale/ROADMAP.md` (full repass pending), `FourthAgePapers/TODO.md` |

## 1. The 2026-06 plan and what became of it

The June plan restructured one paper into four, with confidence propagating
upward from the computer-science paper ("the code is the proof"):

| 2026-06 paper | Working title | Fate |
|---|---|---|
| D-CS (first) | *The Sedenion Engine: a zero-free-parameter prime-hash architecture for semantic field compression* | drafts in `AgeThird/` (`D-CS_Paper.md`, `Third_Age_CS_Draft_v1/v2.md`, `D-CS_Memory.md`, `VAPMIP_Paper.md`); continued as the FourthAge memory papers (`ScalarContextPropagation`, `HyperindexingSystem`) |
| D-M | *Primes are the expansion of the universe* (explicit formula as a standing wave) | not written as one paper; material in wikis [21](21_chladni_zipf_riemann.md), [73](73_why_the_half_line.md), [133](133_canonical_maths.md), and `RiemannHypothesisProof/` (which states that it does **not** prove RH) |
| D-P | *The null-cone pair: Hawking virtual pairs, fractal fur, galaxy formation* (the Witches Hat) | material in [29](29_witches_hat_paper.md); not a paper directory |
| D-CHEM | derive drugs from the cancer itself (collaboration with Erika Schafer) | `ValaQuenta` engine `tier9_chem` and [23](23_resonant_recognition.md); the collaboration is a plan, not a result |

"The code is the proof" is retired as a wording: code establishes a
`:CALCULATED` result and a failing run is a result too (project rule: failures
stay in the code and the data). The 2026-06 "sigma" estimates that propagated
upward (20–60σ) are withdrawn with the other combined-sigma figures
([24](24_claude_conclusion.md) §2); the 2026-06 argument that Gaussian σ values
are "legitimately" large for non-Gaussian domains does not give those numbers a
meaning, since no null distribution was specified.

## 2. FourthAgePapers: the directories as they stand

Git dates are last-commit dates of the directory; "files" counts everything in
it. Statuses are quoted from each directory's own README where it states one.

| Directory | Last commit | Files | README status |
|---|---|---|---|
| AdditionMatrixOrbits | 2026-10-14 | 12 | (PDF present) |
| AxisNShape | 2026-07-31 | 2 | — |
| BoundaryLever | 2026-08-15 | 6 | STANDS: verified by enumeration at dim 16, 32, 64, 128 |
| CMB_FractalBoundary | 2026-06-28 | 18 | — |
| CMB_PlasmaBoundary | 2026-06-17 | 8 | — |
| ChiralityBlackHole | 2026-09-25 | 1 | TODO, stub |
| CollatzShift | 2026-10-14 | 27 | (PDF present) |
| Crawford_NavierStokes | 2026-09-28 | 72 | early |
| CryptoVulnerability | 2026-08-21 | 24 | pre-disclosure draft; do not publish before coordinated disclosure |
| DM_GalacticCavity | 2026-07-31 | 770 | pre-registration committed; analysis ready to run |
| DeSitterCavitation | — | 3 | — |
| FastInverse | 2026-09-23 | 1 | stub |
| FermatMonster | 2026-08-17 | 7 | — |
| ForwardPropagation | 2026-10-16 | 8 | — |
| HRB_RSA_Probe | 2026-07-31 | 2 | — |
| HaltingDiagonal | 2026-07-29 | 4 | — |
| HuchrasLens | 2026-10-18 | 1 | — (target dropped 2026-11-12; see [132](132_ptycho_weak_lensing.md)) |
| HyperindexingSystem | 2026-10-18 | 113 | the paper (README status line dated 2026-09-25 is stale) |
| InertiaEntropy | 2026-06-28 | 1 | theory first-captured; pre-registration pending |
| MonsterSiblings | 2026-06-17 | 7 | — |
| NBallTransformer | 2026-07-29 | 4 | — (engine e05 below) |
| NoetherWiles | 2026-06-17 | 7 | — |
| PhiSpiral | 2026-06-28 | 4 | — |
| PiFromAbove | 2026-06-28 | 2 | — |
| ScalarContextPropagation | 2026-10-14 | 126 | (PDF present) |
| SonificationEncoder | 2026-07-29 | 4 | — |
| Telperion | 2026-06-26 | 6 | — |
| TheInterface | 2026-09-23 | 1 | stub |
| UmbrellaNoether | 2026-09-22 | 31 files (3 commits) | ready for experimental validation |
| WhiteHoleBang | 2026-09-01 | 7 | skeleton only |
| ZeroTree | 2026-07-29 | 16 | — |
| (addenda/, Experiments/) | | | shared material |

The PDFs kept at the top level are the current papers (one PDF per paper;
git is the history); copies for sharing are in `~/Desktop/SpaceClaude/FinalPapers/`.

## 3. The validation engines e05–e17, run on 2026-11-13

Each engine was written to test one cascade claim ("test first, wiki from
results"). All thirteen were run today with `python3 -I engines/<file>.py` from
`VAPMIP/`; all exit 0 (they report their own pass or fail). The outputs below
are the engines' own verdicts, quoted without adjustment.

| Engine | Tests | Result today |
|---|---|---|
| e05 `nball_transformer` | V(n) peak; ratio V(n)/V(n−2) against π/2 at each doubling; V(16) against d* | **4 pass / 1 fail.** V(0), V(1), V(2) exact; peak n* = 5.2569464; the ratio is π/2 at ℝ→ℂ and ℂ→ℍ (1.5707963268) and **not** at ℍ→𝕆 (0.8225) or 𝕆→𝕊 (0.0580). V(16) = 0.2353306, which is not d*_spec = 0.24600 (difference 0.0107) |
| e06 `two_trees` | π-family vs φ-family separation | mean T/L ratio 0.4564 against π/φ = 1.9416 (delta 1.485: not close); T ⟂ L: mean 0.85, max 0.88: **not orthogonal** |
| e07 `observer_fixed_point` | Wankel dual-thread convergence to Ω_ζΣ | **0/6 converged**; all within 0.1 of Ω_ζΣ (flag reads FAIL as written); 0/50 random starts converged |
| e08 `vortex_quantizing_shear` | J_cross > GAP predicts word firing | mean agreement 0.2648 **FAIL**; the vortex half-turn check e^(πe₁)e₀ = −e₀ **PASS** (residual 1.2·10⁻¹⁶); prime gaps in P16 [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6] |
| e09 `j2_involution` | J₂² = identity; J₂ automorphism; zero-divisor pairs | J₂² = id **PASS**; J₂ automorphism **FAIL** (256 failures); zero-divisor tests **FAIL** by construction (§4); non-associativity confirmed (1848 of 4096 triples) |
| e10 `caustic_l_dynamic` | similar inputs converge; antonyms diverge | 0/5 groups fully converged (mean similarity 0.9759) **FAIL**; 0/5 antonym pairs divergent (mean ρ = 0.9641) **FAIL** |
| e11 `two_doublings` | pathway count after 1 vs 2 doublings | counts: base ℂ: 2, 12, 56; base ℍ: 12, 56, 240; base 𝕆: 56, 240, 992; ratios 6.0 → 4.667, 4.667 → 4.286, 4.286 → 4.133; J₂ as 4th-doubling cross-term **PASS** |
| e12 `index_not_value` | does the index or the value carry information | mean cosine distance from the original geometry: index shuffle 0.4059, value shift 0.0860, single swap e₀↔e₁₅ 0.2484: the index carries more (PASS) |
| e13 `fermat_riemann_firing` | specific prompts depart more from ordinal firing than flat ones | mean departure 0.4750 (specific) vs 0.7583 (flat): **claim not supported** (the engine's PASS: False) |
| e14 `fermat_near_miss` | 3987¹² + 4365¹² vs 4472¹² | residual 1.2119·10³³; agrees to 10.72 significant figures: invisible at 10 digits (PASS) |
| e15 `futurama_theorem` | permutation restoration needs at most two fresh elements | PASS at n = 4, 6, 8, 10, 16 (500 trials each): the maximum number of fresh elements needed was **1** (so "all ≤ 2" holds, and the plan's "always 2" is not what the runs show: 1 sufficed); mean cycles 1.09 → 2.35, max cycles 2 → 5 |
| e16 `penrose_swap` | (I\|O)² ≠ (I\|O)⁻¹; perturbation below GAP snaps back | below GAP: 100/100 same firing order **PASS**; above GAP: 8/100 different **FAIL**; 5 variant inputs gave 5 distinct firing orders **FAIL**; period 4 for each tested text |
| e17 `hyperindexing` | injectivity crossover | effectively injective by N = 8; index discriminability 10/10 unique firing signatures (100%) PASS |

Three older results in the plan are unconfirmed today: "Riemann + Fermat =
Ĥ_RB numerically" (e09 does not test it), "semantically similar inputs converge
to the same word" (e10 fails), and "fixed point = Ω_ζΣ" (e07 reports
non-convergence). These stay in the engines as they are.

## 4. Anomaly found while running them: e09's zero-divisor test cannot pass

`e09_j2_involution.py` tests whether products of **basis elements** e_a·e_b are
zero (its `KNOWN_ZD_PAIRS`, then a scan of all i < j). In a Cayley–Dickson
algebra every basis product is ±e_{a⊕b}, of norm 1, never zero; the zero
divisors are the sums e_a ± e_b (see [25](25_sedenion_manual.md) §4: 84 such
elements, 42 index pairs {a, b} with a < 8 ≤ b). The "found 0, expected 42" and
"0/14 confirmed" are therefore artefacts of the test, not of the algebra.
Logged; `VAPMIP/engines/e09_j2_involution.py` is **not edited** (project rule:
fix a failure only when asked to). The correct check is
(e_a ± e_b)(e_c ± e_d) = 0, as in the listing on [25](25_sedenion_manual.md).

## 5. The 2026-05-31 "key insights", with current status

| Statement (2026-05-31) | Status | Where |
|---|---|---|
| Primes are the expansion of the universe: the x term of ψ(x) = x − Σ x^ρ/ρ is the expansion; ln is the Hubble constant of ℕ; H = xp the Hubble flow | interpretation of an established formula | [21](21_chladni_zipf_riemann.md), [20](20_three_phase_architecture.md) |
| Navier–Stokes is the sedenion, term for term | THEORETICAL; not a regularity proof | [106](106_the_navier_stokes_problem.md) |
| sin/cos as two counter-rotating frequencies; tan = 1 where they balance (σ = ½) | an identity of trigonometry plus the framework's reading | [73](73_why_the_half_line.md) |
| the inside-out witches hat is a galaxy (conformal inversion of the infalling null cone) | THEORETICAL | [29](29_witches_hat_paper.md) |
| life is the upper sedenion e₈–e₁₅, the zero-divisor zone | interpretation; the lower/upper pairing of zero-divisors is exact ([25](25_sedenion_manual.md) §9) | [25](25_sedenion_manual.md) |
| 24D defines 16D (the Leech lattice as ambient container; zero-divisors as its shadow) | THEORETICAL; not derived | [134](134_the_library.md) §2 |
| cancer is a zero-divisor collapse; the drug is the inside-out of its signature | a research hypothesis, not a medical result | [23](23_resonant_recognition.md) §4 |

## 6. UniversalSynth

The roadmap's "Ptolemy's piano" (a 16-track piano roll over the sedenion) is
the repository `UniversalSynth/`, a specification with no code. Its
status, the points where it disagrees with this wiki, and what it would take
to build it are recorded in [08](08_sonification_engine.md) §7 and in the
UniversalSynth README (updated 2026-11-13).

## 7. Related pages

[24 Archived assessment](24_claude_conclusion.md) · [25 Sedenion manual](25_sedenion_manual.md) ·
[27 Third Age CS paper](27_third_age_CS_paper.md) · [98 Provenance and citations](98_provenance_and_citations.md) ·
[133 Canonical maths](133_canonical_maths.md)
