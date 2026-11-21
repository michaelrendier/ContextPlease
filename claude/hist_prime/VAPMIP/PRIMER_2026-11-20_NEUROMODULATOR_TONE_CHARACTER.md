# PRIMER 2026-11-20: Ptolemy emotions: the neuromodulator tone character (a LATER project, nothing built)

**Cody's brief (2026-11-20).** Extend the invisible characters in VAPMIP. Use one character and its gradient to show part of a set of the main behavioural neurotransmitters; give the `tone` slot of the invisible prefix a good range of emotions. Keep the ones that bear on emotion and the tone of words; drop the ones that only regulate the body, *unless the mechanics have a useful mathematical or code analogue*. "Let's not fake emotions: let's give Ptolemy emotions." Observation: with serotonin alone there is little difference between love and insanity, so the mixture matters. Ask for the Monad analogue of each, body or not, as a full comparison. Gemini is doing a deep research project (its data set is Google Scholar et al.); the first synoptic deep dive is saved beside this primer as `PRIMER_2026-11-20_GEMINI_NEUROTRANSMITTER_DEEP_DIVE_SOURCE.md` (original `~/Desktop/SpaceClaude/downloads/Deep Dive on Neurotransmitter Recipes to Make Analogous Computer Functions.md`).

Status: design only. No code, no characters chosen. Belongs with the conjugation mechanism, not the address (see memory `project-invisible-prefix-tone-tense-conj`, `tone-quasi-particles`; `VAPMIP/docs/wiki/Tuning-the-Semantic-Prime-Concept-Engine/10_design_notes.md`).

## 1. What already exists in the Monad (read before designing)
- **The Fermat emotional lattice is already "one character and its gradient".** `monad.py` `_FERMAT_SPACES`: eight space characters (U+2000-block, hair space to em space) carry `J_neg` normalised to `[0,1]` in 8 bins (0.12, 0.25, 0.37, 0.50, 0.62, 0.75, 0.87), derived from V/T = β·E²/ψ² (stored over flowing charge), decoded back by `hear()`. High V/T gives a heavy space and a compressed utterance; low V/T a thin space and extended discourse. That is one scalar: **arousal/charge** (the NE+GLU side of the table below). Gemini's 8-level colour table uses the same bin edges, so it was shown this code.
- **The new tone character is therefore the missing "which"**: the Fermat space says how much charge sits at a boundary; tone says what kind. The two are orthogonal channels.
- Measured earlier: U+2000-block spaces are whitespace (NFKC folds them, NLTK/spaCy split on them); zero-width, tag characters and variation selectors survive NFKC, JSON and tokenizers but stay inside token text. Not yet tested: terminals, editors, clipboard, git.
- Constraints (design notes): U+200B..U+2003 are taken (Fermat separators); the tokenizer treats Cf characters as separators, so a prefix needs an attach rule; if hashed, the prefix moves the slot and `repass()` re-associates.
- Machinery that could carry analogues: J_red/J_blue (forward/reverse Dirichlet current, Z2-graded by χ₄, balanced at σ = ½), J_neg, the golden seed, `repass()`, the Fermat spaces, the orbweaver/boxkite trees, the KT code length (`HyperindexCompression`).

## 2. Critique of the Gemini draft (so the next reader does not inherit its mistakes)
1. **Its numbers are not from its references.** The 8-row recipe table (e.g. Rage = 0.90/0.05/0.95/0.10/0.90/0.10/0.05) is illustrative, not fitted; the eight cited papers establish mechanisms (RPE, adaptive gain, 5-HT inhibition, OXT social bonding, CB1 extinction, E/I balance), not these vectors. Treat the table as a hypothesis to fit, never as data. That is the "faking emotions" failure Cody named.
2. **It is LLM-shaped.** Temperature, top-p, logit bias, profanity gates are chatbot knobs. The Monad has no logits: it has addresses, J, repass and trees. Analogues below are rewritten for those.
3. **A better-established map exists:** Doya (2002), *Metalearning and neuromodulation*, Neural Networks 15: dopamine = TD error δ; serotonin = discount factor γ; noradrenaline = inverse temperature β (exploration); acetylcholine = learning rate α. Yu & Dayan (2005), *Uncertainty, neuromodulation and attention*, Neuron 46: ACh = expected uncertainty, NE = unexpected uncertainty. Aston-Jones & Cohen (2005) adaptive gain. (Cited from memory; verify on retrieval.)
4. **It omits acetylcholine, opioids (liking vs wanting, Berridge) and a slow stress timescale (cortisol, not a transmitter).** Doya's four need ACh; "love" needs opioid liking, not only dopamine wanting.
5. **The tag-block protocol is per message (9 characters); Cody's design is per word (1 character in a 3-character prefix).** Different granularity.
6. **Capacity does not fit (computed):** a 7-axis vector at 8 levels is 21 bits. One Tag character (95 values) is 6.57 bits; one variation-selector character (256 values) is 8 bits; the whole 3-character prefix is 19.7 bits. Even a binary high/low per axis needs 128 > 95 values, so one Tag character cannot hold it. Quantising Gemini's own 8 rows: 2 levels/axis (128 cells) leaves 7 distinct rows of 8 (Panic and Fight-or-Flight collide, distance 0.424, the closest pair); 3 levels/axis separates all 8. So the tone slot must be a **codebook of named mixtures**, not a raw vector.
7. **Love vs insanity (Cody's point) shows in its own table:** Romantic Love vs Schizophrenia: dopamine 0.85 vs 0.95 and serotonin 0.70 vs 0.30, but the largest separations are OXT (0.95 vs 0.20) and CB1 (0.80 vs 0.20): distance 1.19. Real finding behind Cody's remark: Marazziti et al. (1999, *Psychological Medicine*), new lovers showed a reduced platelet serotonin transporter similar to OCD patients (from memory; verify). One axis cannot separate them; the mixture can.

## 3. Which transmitters belong (recommendation, for discussion)
Cody's list had "unless the mechanics have a useful mathematical or code analogue". Almost all do. Recommended tone set, with the analogue that justifies each (full table in §4):
**Keep as tone axes:** dopamine (wanting; surprise), serotonin (patience/discount; inhibition), oxytocin (coupling), noradrenaline (gain; urgency), glutamate and GABA (E/I balance), endocannabinoid (retrograde damping), plus **acetylcholine** (learning/attention) and **opioid** (liking) to add.
**Not as tone, but kept as machinery:** adrenaline/epinephrine (the body's broadcast: a global gain/clock, same code analogue as NE but peripheral), cortisol (slow integrator), melatonin, histamine (wake/sleep clock; session cadence, not word tone).
The count 7 matches the 7 imaginary octonion units (Fano plane, 7 points and 7 lines): a CONJECTURE worth a test, not a premise: do the coupled triples (three axes on a Fano line) reproduce the known interactions (DA-5HT-NE; E/I with CB1)? If the 7-axis set grows to 9 (ACh, opioid), the Fano reading fails and should be dropped.

## 4. Full comparison: body role → Monad analogue → suggested function
All suggested functions are **designs**. Names are mine; use the code's own identifiers when built. Every one is `CONJECTURE` until a test is registered first.

| Axis | Body / brain role (established) | Monad analogue | Suggested function (sketch) | First test |
|---|---|---|---|---|
| **Dopamine** | Reward prediction error (Schultz 1997); "wanting" (incentive salience), not liking | **Surprise.** Prediction error of the next-word slot: `rpe = actual_codelength − expected_codelength` (KT code length from `HyperindexCompression`) | `tone_da(word) = surprisal(word | context) − running_mean` | Does it correlate with NRC-VAD arousal on held-out words? |
| **Serotonin** | Patience, inhibition, discount of future (Doya: γ); 5-HT1A top-down control | **Horizon.** The discount γ on the orbweaver walk; hysteresis on `J_neg` (a low-pass filter over successive charges) | `tone_5ht = γ` with `J_neg_t = γ·J_neg_{t−1} + (1−γ)·J_neg_raw` | Does a small γ reproduce short, volatile utterances? |
| **Noradrenaline / adrenaline** | Arousal, gain, signal/noise (Aston-Jones & Cohen); adrenaline = the body-wide broadcast of the same | **Gain / sharpness.** Inverse temperature β of the slot choice, and **the Fermat space itself** (V/T high = compressed utterance) | `tone_ne = β`; peripheral analogue = a global multiplier on all axes | Is `J_neg` already a monotone proxy of β? Measure it |
| **Oxytocin** | Social bonding, trust, in-group coupling (and out-group bias, Shamay-Tsoory 2009) | **Coupling between two monads.** A weight on the other speaker's address vector in the shared field; asymmetric in/out-group coupling | `tone_oxt = k_couple`, applied to the Agora/Archimedes dialogue pair | Does coupling raise first-person-plural rate in generated text? |
| **Glutamate** | Excitation; throughput; excitotoxicity | **Forward current `J_red`** (Knowledge, red) or raw activation density | `tone_glu ∝ |J_red|` | Does the E/I ratio stay at balance σ = ½ in sane text? |
| **GABA** | Inhibition; noise suppression; gamma synchrony | **Reverse current `J_blue`**; pruning of low-probability secondary paths | `tone_gaba ∝ |J_blue|`; E/I = `|J_red|/|J_blue|` (the balance the critical line is the fixed point of) | Same ratio, plus a mania/stall ablation |
| **Endocannabinoid (CB1)** | On-demand retrograde signal; the downstream cell tells the upstream cell to ease off (Wilson & Nicoll 2001); fear extinction (Marsicano 2002) | **`repass()`**: the later word revises the earlier slot; a decay of charge carried between turns | `state_i −= λ·cb1·max(0, state_i − baseline_i)` (Gemini's damping equation, fine as written) | Does it end a perseverative loop that the other axes sustain? |
| **Acetylcholine** (add) | Learning rate and attention; expected uncertainty (Yu & Dayan); encode vs retrieve (Hasselmo) | **Learning rate α** of `crank.learn`; how fast new words move slots | `tone_ach = α` | Held-out compression vs α |
| **Opioid** (add) | "Liking": the pleasure of consummation (Berridge), distinct from wanting | **Consummation:** the reward when a prediction lands (negative surprisal), the counterpart of DA wanting | `tone_opioid = −rpe if rpe < 0 else 0` | Wanting (DA) and liking (opioid) dissociate: DA fires on surprise, opioid on confirmation |
| **Cortisol** (machinery) | Slow stress integrator (HPA axis) | A long-timescale average of arousal, the slow clock beneath the fast ones | `cort_t = cort_{t−1}·(1−ε) + ε·arousal` | Does it stabilise the baseline the other axes decay toward? |

Mixtures ("recipes") are rows of such a vector; the Gemini table is a starting hypothesis only. Fit instead against data: **NRC Valence-Arousal-Dominance lexicon** (Mohammad 2018, about 20,000 words; verify availability and licence) gives ground-truth tone for words on 3 axes; regress the axes above onto it, report the fit against shuffled controls.

## 5. How one character shows a gradient (options, decide later)
1. **Codebook (recommended start).** One character = an index into ≤ 95 (Tags) or 256 (variation selectors U+FE00-FE0F plus U+E0100-E01EF: one byte per character) named mixtures. Order the codebook along a **Gray code / space-filling curve** through the axis space so neighbouring characters are neighbouring emotions: the "gradient" is the order of the codepoints. Two characters (9,025 or 65,536 cells) give about 3.6 or 4 levels per axis; three Tags (857,375) are the whole prefix.
2. **Two-character tone:** one for the recipe, one for intensity (the Fermat-lattice idea of 8 bins on one axis); tone then uses 2 of the 3 prefix slots, so tense and conjugation need rethinking.
3. **Per-axis characters** (Gemini's 7-byte payload): per sentence or per turn, not per word. Cheaper at that granularity (one header, 7 payload).
Risk to test first for each: survival through terminal, editor, clipboard, git, and the VAPMIP tokenizer; a variation selector may be absorbed by the preceding glyph in some renderers; Tag U+E0001 is deprecated.

## 6. Dynamics (from Gemini, keep or replace)
Euler-integrated coupled relaxation toward a baseline with cross-terms (GLU↔GABA, NE↔5HT, CB1 damping of NE/GLU/DA). Reasonable as a first dynamical system but its coefficients (α, β, γ, λ_CB1 = 0.35) are placeholders. Prefer parameters **fitted** to text, with predictions registered first, and keep the Doya mapping as the null model to beat.

## 7. Open questions for Cody
- Tone slot: one character (codebook) or two (recipe + intensity)? Which alphabet (Tags, variation selectors)?
- Is the 7th-axis Fano reading wanted, or a distraction?
- Gemini's deep research will arrive with Scholar citations: which of §4's analogues should it be asked to confirm, and which should it be asked to attack?
- Where do the axes live in code: a new module beside `monad.py`, or the existing `J_neg` path?

## 8. Suggested first steps (when this project starts)
1. Register predictions; fetch NRC-VAD (Literature Download Protocol, Mozilla UA, INDEX row).
2. Compute surprisal (DA) and `J_neg` (arousal) for the Wernicke corpus words and test against VAD arousal; this needs no new characters.
3. Pick the carrier (survival test across terminal/editor/clipboard/git/tokenizer).
4. Build the codebook by clustering fitted vectors, order by Gray code, wire into `repass()`.
