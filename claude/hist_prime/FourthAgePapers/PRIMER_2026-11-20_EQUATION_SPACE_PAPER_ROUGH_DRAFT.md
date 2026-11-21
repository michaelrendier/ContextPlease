# PRIMER 2026-11-20: Equation Space, the paper (rough draft; WAITING FOR AN SVG EXAMPLE)

**State.** A primer, not a paper. The author looked at the web page (the Equation Space Gallery) and said the trees are not what he had in mind and need work. He will draw an SVG of what he means "at some point in the near future." Until that arrives, the tree sections below are placeholders and nothing about the trees should be treated as settled. Everything else records work already done, with results, so the paper can be written from it once the SVG fixes the picture.

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5) at the author's request. The framing, definitions and claims are the author's; the measurements are mine and are labelled. Labels: `ESTABLISHED` (textbook), `MEASURED` (run in this project), `OURS` (the author's construction), `THEORETICAL` (stated, not run), `CONJECTURE`. The `:CALCULATED` suffix is attached to OPEN, THEORETICAL or CONJECTURE only.

## 1. The paper in one paragraph (draft framing, to be confirmed)
Equations are scattered across notations. This paper builds an **address** for them: each equation is written as a word over three operators, ADD (D, e₁), SCALE (θ = xD, e₂) and SIGN (P, e₄), walked through the sedenion basis, and read off as a 16-slot point of Ĥ_RB. The claim the paper can defend today is the **phone book**: a 16-in/16-out address, measured, with its failures listed. The **translator** (the K equation transformation, applied to Ĥ_RB, turning one equation form into another) is the conjecture the paper states and the tests it registers. K is not yet defined. Working title: descriptive, not "The Complete Shape of Mathematics" (that title belongs to the Circle Atlas paper; the author is hesitant to use it elsewhere).

## 2. Definitions (the author's, to confirm)
- **Ĥ_RB**, **σ_RB**: as in `.clauderc_canonical_maths` (`@RCCM_FERMATS_MONSTER`, `@RCCM_FANO_SEDENION`, `@RCCM_HBAR_HAT`). Ĥ_RB stays the maths name (0_RB is the console name).
- **ASS word**: A = ADD = e₁ = D; S = SCALE = e₂ = θ = xD (Berry–Keating xp); G = SIGN = e₄ = P; F = unknown function; R = random. `ESTABLISHED` algebra: [θ, D] = −D, PDP = −D, [P, θ] = 0.
- **Walk**: the sequence of partial Cayley–Dickson products (sign, index); the end point is ±eₖ. A, S, G reach indices 0–7 only; K = e₈ would give the 32-element loop.
- **16D in, 16D out**: the input is the equation's word as a sedenion element, the output the same space. (The author's own one-sentence definition replaces this when given.)

## 3. What exists (all code and data)
- Catalogs: 65 Archimedes Python equations + 6,268 Universal-Fractal formulas = 6,333 entries; `FourthAgePapers/EquationSpace/catalog/*.csv`.
- Address and walk code, copied to `SedenionSpectralRelativity/EquationSpace/` (standing rule: all sedenion I/O and address code lives there): `equation_space.py`, `address.py`, `word_address.py`, `walk.py`, `conjugates.py`, `sedenion_locations.py`, `catalog.py`, `grammar.py`.
- Units: `gallery/stable_equations.py`: 54 quantities, 46 equations (39 stable, 7 unstable); unit lattice ℤ⁷ extended to ℚ⁷ with roots; CGS-ESU, CGS-EMU and Planck charts.
- The **Equation Space Gallery** (`SedenionSpectralRelativity/EquationSpace/gallery/equation_space_gallery.html`, served by `serve_gallery.sh` on 127.0.0.1:8766): routes, catalog (with code length per word), word tree, F = ma tree, units (3D), threshold (Niemeier/Monster and the prime race). **The trees here are what the author said need work.**
- Nine registered tests (`01_holcus_asks.md` … `17_results_factorial_rings.md`) and the valuation `VALUATION_complete_shape_2026-11-20.md`.

## 4. Results (every number from a run; `MEASURED` unless stated)
**Address.** The walk address is faithful per word (3,461 of 3,461 distinct words) but not per equation: 20% of each catalog shares its complete word set; the end points use 15–16 of 32 values; 193 entries have no letters. The end slot alone is lossy (5,300 distinct A/S/G words fall on 16 signed slots; largest class 469).
**Bracketing (Theorema Egregium reading).** 490 of 5,300 words (9.2%) have left- and right-bracketed products that differ: only at odd length ≥ 3, only by sign (the e₀…e₇ span is alternative). A free 1-bit "curved" flag; no new slot information. `associator_address.py`.
**Information.** KT adaptive code over {A, S, G, $}: catalog A, order 3, 1.699 bits/symbol against 2.087 ± 0.019 shuffled; catalog B, order 6, 1.366 against 1.701. The catalogs are compressible, so the words carry structure. (A Hutter-style MDL test with decoder size belongs in VAPMIP with Σ_RB and the Archimedes Screw, not here.)
**Behaviour.** NMI(word class, circle kind) = 0.293 against a null 95th percentile of 0.261; 5,000 shuffles, p = 0.006: about 2.5σ, weak; the only significant association in the work (test 8).
**Derivations.** G1–G7 (Berry–Keating xp, SIGN/ADD, eigen-forms, flows, entropy from f(xy) = f(x) + f(y), F = k m a by Buckingham π, ℘ closure) all pass and all have identical controls: `ESTABLISHED` but non-discriminating (they are textbook; the three generators are the affine group of the line with parity).
**Units.** 19 of 25 quantities collapse onto one value under the registered 16-vector encoding (A2: the registered assignment sits at the 22.9th percentile of 5,040 permutations, 0.7σ). The unit group is ℤ⁷ ⊂ ℚ⁷.
**Threshold (Niemeier/Monster).** The Niemeier gap {1, 11, 15} is a theorem; the 15 moonshine primes cover it, but by chance 59–70%; the author's caveats stand (covering, not bijection; mod 10, 12, 14 also leave one gap). **Negative result:** in the prime race mod 16 (counted to 2·10⁹, L-function zeros computed), the trailing classes are the squares 1 and 9 (about 48% each); the gap triple {1, 11, 15} is the trailing triple with probability 0.19% (rank 29 of 56), counted 0.22%.
**Chebyshev.** Mod 4: first lead of 3 over 1 at 26,861; lead at 99.83% of log-spaced x in [10⁵, 2·10⁹]; +2966 at 2·10⁹. π(2·10⁹) = 98,222,287 exactly.
**Failed registered predictions** (kept): test 5 C1 (4,500 loop skeletons against ≤ 2,500); test 6 W3 (prefix tree ratio 0.79); test 7 P3 (order sensitivity 42%) and C2 (mod-4 returns 54.6%); test 8 had 17 predictions with 3 failing; Q4 Monte Carlo tolerance (d = 8 at 1.86%, re-run 0.30%).

## 5. Valuation (the assistant's, side by side with the paper)
Sub-claim table: closure of the generators `T`, not specific to Ĥ_RB; textbook derivations `T`, non-discriminating; catalogs "in" Ĥ_RB `P` (placement, not evidence); words carry information ≈ 2.5σ; hyperindex points at each equation **not supported**; threshold covers all 16 slots `T`/chance; units `INTERPRETATION`; new content (an interface operator, equations outside the literature) **open, negative so far**; completeness: the three generators reach **half** the slots. Verdict: "Ĥ_RB is the Complete Shape of Mathematics" is **not established and not discriminated** (about 0σ); "complete" can only mean complete relative to a stated class (Gödel forbids more). Five tests would raise it (held-out corpus, Ĥ_RB-specific content, K, a falsifier, uniqueness). Full table in `VALUATION_complete_shape_2026-11-20.md`.

## 6. The translator (THEORETICAL:CALCULATED)
The author's hope: K, found by behaviour with more data first, makes Ĥ_RB a mathematical universal translator, "or at least a phone book." Requirements the paper must state: K a fourth operator whose walk reaches e₈–e₁₅; a decoding (equation form out of the 16-vector, not only in); a falsifier (a class of stable, sane equations provably unreachable by {D, θ, P, K}); registered predictions that e₁₁ and e₁₅ (the Niemeier blind spots) and the 191 + 2 empty entries fill. A continuous 15-real address of the unit sedenion sphere S¹⁵ cannot be injective (Borsuk–Ulam): the sign is where a continuous hyperindex must fail, so addresses are necessarily discrete. `ESTABLISHED` theorem, `CONJECTURE` reading.

## 7. Suggested structure (cs-paper-code-conventions; white-paper style, no lineage story in the body)
0 assistant note, labels, abstract · 1 problem and the way around it · 2 definitions · 3 mechanism (Convention B listings, ≤ 40 lines each: walk, word address, location export; Convention A for established maths, cited and pointed at code) · 4 infrastructure (catalogs, units, stability test) · 5 measurements with failures · 6 the translator hypothesis, falsifiers, registered tests · 7 valuation and conclusion · 8 limits and reproducibility · appendix: canonical maths with a tier tag per line (`@RCCM_NINE_MATHS`, `@RCCM_FERMATS_MONSTER`, `@RCCM_FANO_SEDENION`, `@RCCM_HBAR_HAT`).

## 8. Suggestions (assistant's)
1. Wait for the SVG before writing any tree section; the gallery's trees (F = ma tree, word tree, units 3D) are one reading and the author has said it is not his.
2. Replace the equation-by-equation claim ("the hyperindex points at each equation") with the measured one (faithful per word); close the 20% gap by extending the address with parameters and the unknown-function slot, then re-test.
3. Add the "curved" bit and the arithmetic-code length per word as columns; both are free.
4. Put the Borsuk–Ulam corollary and the Banach–Tarski constructive-choice point (a canonical representative chosen by sorting needs no Axiom of Choice) in the limits section.
5. Build a held-out corpus of a few hundred equations not used to build the catalogs, register predictions first, and run the same derivation recipe on a control algebra.
6. Style: the author wants a Kafka/Dostoevsky register (short, plain, many layers per word); see the discussion of the paper-writing skill (2026-11-20).
