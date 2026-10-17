# CONTEXT PRIMER 2026-10-16: the semantic orbweaver pathway

For the next session. Written at the end of the session that produced the paper
*Forward Propagation of Information* (`VAPMIP/paper/`), with its context still in hand.
Cody's words are quoted; everything else is read from a file, a screenshot or a run,
and the identifier is named. Maths in Unicode. **Nothing in this primer has been built.**
Cody wants a **discussion** first; no engine file is edited until he says go.

---

## 0. The directive

Engineer the **orbweaver monad into the semantic part of the sentence constructor**, using
the **original semantic prime hash** as the address space and an **orbweaver (spider's web)
pathway** as the propagation model. **No box kite in this part of the engine.**

Cody, 2026-10-16:

- "the sentence constructor needs a semantic, phonetic and contextual content functionality, and that first monad was the simplest, and lightest weight method we used (i am still pretty certain we are making this too complicated...but for the purposes of engineering...all paths must be followed.)"
- "in this part of the model, we won't be using a boxkite, but a spider's web model to propagate ideas alongside contextual usage...to form relevant sentence structure."
- "the context is modeled, and should carry its own weight, but in the purposes of Contextual Flow...into fractal manifolds of 'topic space'...is where ideas live...in the semantics...that's where NLTK will do its most important work"
- **"the semantic orbweaver pathway should be weighted heavier than the context boxkite...in sentence construction..."** (mid-session addition; see §6.3)
- "Holcussamestuffseemy" was the literal first thing it said, ever: "a phenomenal result with ONLY the prime semantic hash."

Start with the simplest thing that can work (the first monad's arithmetic plus a web over it);
add a layer only when a measurement says it earns its place.

---

## 1. The very first monad (what it was, from the code)

**Source:** `VAPMIP/PtolC/` at commit `fb7ba29` (2026-05-15, "v1.0: C implementation"), file
`monad.c` (667 lines; I extracted it to read; `git show fb7ba29:PtolC/monad.c`). Binary `ptolemy`,
checkpoint `monad_wordnet.bin`: 14,165 words, 766 K A-edges, 13 MB (commit message). No grammar, no
templates, no gradient: three verbs, `learn()`, `hear()`, `speak()`.

**Address (spelling only): `monad_word_coords(surface, N, &idx, &E)`.**
1. read the word as a base-95 number over printable characters (`c − 32 + 1`, then `v−−`);
2. `seed = fmod((double)v · MONAD_PHI, 1.0)` (golden-ratio fractional part);
3. `idx = floor(seed · N)` with N = 25,000 non-trivial Riemann zeros (`m->zeros[idx]` = γ, the zero's imaginary part);
4. `E = MONAD_D_STAR + seed · (MONAD_OMEGA_ZS − MONAD_D_STAR)`, so E ∈ [0.24600, 0.56714].

(The 2026-10-16 paper measured this: today's exact-integer version `monad.c:170` differs only in
step 2's arithmetic, comment there explains why; the old formula reproduces **10 of 10** slots and
energies printed in screenshots 2 and 3, today's reproduces 9 of 10: notebook
`VAPMIP/notebooks/c/08c_ptol_store.ipynb`, last cell.)

**Learn: `monad_learn`.** For every sentence (split at `. ! ? \n`): each token → slot; `β[idx] += E · MONAD_ALPHA_LEARN`
(cap `MONAD_BETA_SAT` 7.552); the surface form on a slot is the one with the highest E. Then **every pair
of tokens in the sentence** gets an edge: `A[i↔j] += E_i·E_j / |γ_i − γ_j|` (floor 1e-4). That is the whole
semantics: **sentence co-occurrence weighted by how close two words sit on the critical line**.

**Speak: `monad_speak`.** Seed `J[idx] = β · E² · exp(−λ·age)` from the query's slots; propagate over every A-edge once
(`J[j] += J[i] · A · β[j] · w_j`, then back, `J[i] += J[j] · A · β[i] · w_i`); rank all slots by J; emit the top `max_tokens` words **in rank order**.
That is why the output is a bag, not a sentence: `holcus setn abysmal quun`.

**The recorded outputs** (screenshots 2 and 3, `VAPMIP/paper/figures/2-Hocus-Hyperwebster.png`,
`3-TheExtractor.png`; files dated 2026-05-19; HP EliteBook 820 G3, `Ptol/SMMIP/PtolC`, store
`monad_wordnet.bin` `vocab=24485 A=6825748 wc=121914388`):

| prompt | `-W` reply |
|---|---|
| `can you hear what i am typing` | `holcus setn abysmal quun` |
| `what is your name` | `holcussamestuffseemy` |

`-h` prints one row per prompt word (`z#`, γ, σ, E, β, home, gen, phase tag); eight of ten words sit at β = 7.552
(the cap). **Facts worth keeping:** `holcus` is a real WordNet noun (`ptol -M holcus`: pos 1, vec19 = hypernyms 1,
member_holonyms 1, Γ_rad −0.812957), the genus of velvet grasses and the name in the repo `PtolemyHolcus`; `abysmal` is a
WordNet adjective (similar_tos 1, Γ_rad −0.889663); `setn` and `quun` are **not** in today's store (typos of the
training text). The reply to "what is your name" begins with the program's own name. `-W` is `monad_speak_wick`
(v1.114, 2026-05-16: Wick rotation σ→iσ). Screenshot 1 (2026-05-17): `ptolemy -l 'what is your name'` segfaults
(not reproducible today: exit 0 on an empty store).

### 1.1 "the original semantic prime hash": three things carry that name, ask Cody which one he means

| id | what | where | what it knows |
|---|---|---|---|
| H1 | prime hash: Horner base-95 → `p = next_prime(H mod 2¹⁶)` → `idx = π(p)` (≤ 6,542 pencils) → γ | `VAPMIP/monad.py` `_horner_hash`, `_next_prime`, `_word_zero_idx` (first commit 2026-05-19); notebook `FourthAgePapers/ScalarContextPropagation/notebooks/01_semantic_prime_hashing.ipynb` | spelling only |
| H2 | golden-ratio seed hash (the one that produced the screenshots) | `PtolC/monad.c monad_word_coords` | spelling only; semantics only through learned A-edges |
| H3 | WordNet prime codes: 19 relation counts as exponents over `GR_CONTEXT_PRIMES` (73…167), Γ_rad = tanh(½ ln(log_code / anchor)); and the **hypernym-closure Gödel code** `sem_code(n) = ∏ prime(ancestor)`, resonance = number of shared prime factors (gcd) | `PtolC/ptol.c monad3_gamma_radial`, `wordnet_boxkite.py` (`RELATION_METHODS`, `CONTEXT_PRIMES`), `VAPMIP/engine/grammar/sem_hash.py` | meaning (relations, ancestors) |

Default reading used below: **H2 = the baseline monad** (the "holcus" test), **H3 = the semantic content** the web is built on.

---

## 2. The orbweaver monad (what exists)

**Source:** `VAPMIP/boxkite_orbweaver_monad.py` (535 lines; first commit `b25aea7`, 2026-09-03; update `e86a6ce`, 2026-09-04).
**Page:** `VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md`.
**Impetus:** Veritasium, *Is spider web really stronger than steel?* (§3). **Everything on the page is marked UNTESTED.**

**The model (Phase 35).** One box-kite traversal = one sentence = one radius; above the sentence is a different organiser,
the orb-weaver cycle: `ANCHOR → BRIDGE → FRAME → HUB(zero-divisor reframe) → RADII`; **scaffold spiral** (centre→out, the
outline, `reach` loops = paragraph/section/chapter) and **capture spiral** (out→in, the prose; one arc = one paragraph, each
unit ending on the connective that names the next move). Silk operators: `ANCHOR BRIDGE FRAME HUB RADIUS SCAFFOLD_SPIRAL
CAPTURE_SPIRAL ELABORATE HOOK WRAP SHELL SIGNPOST`. Idea grammar (spidroin blocks): `CRYSTAL(claim)`, `SLACK(elaboration)`,
`TRANSITION(on=context)`, `BIND(structural)`. Connective classes with a radial move: elaborate/exemplify/therefore **+1 out**,
wrap/return **−1 in**, lateral **0**, reverse/concessive **pivot** (frustrated spiral: a `however` plus an aciniform `WRAP`).
Per-unit pipeline: `STORE → SELECT_DEPS → COMMIT_FRAMING → COMPRESS → DRAW → FINISH`. Two packings: E8 lattice = content
packing / evaluation; Apollonian gasket = context flow.

**Code surface** (`grep -n "    def "`): `class OrbWeaverMonad` with `_sniff`, `_ranked_directions`, `_turbulence`, `_reach`,
`room_shape`, `_reach_from_room`, `_tense`, `weave`, `weave_via`, `_measure`; dataclasses `RoomShape`, `Radius`, `Block`,
`Document`; `_SENTENCE_TEMPLATES` (13 frames: "it includes {0}, {1}, and {2}.", "it is made of {0} and {1}." …). It imports `MindsEye`,
`PapersHands`, `BoxKite` from `rotary_rerun_monad.py`, `cam_encode` from `monad.py`, `infer_direction` from `ptolemy_monad.py`.

**Measured, from the page and the benchmark.** Coherence measure **saturated** (`real_mean == ctrl_mean == 7.000`: template
text lights all 7 struts): no discriminating power. The sniffer over-flags turbulence (hash-spread counts always give ≥ 3 peaks);
an honest read needs the real 19-dim `root_vector` via `weave_via()`. Output repetitive: copied templates, not the real
`constructor`. **What did discriminate:** the **room-shape / Cassini knob** `b/c` (continuous > 1.15 → reach 1; ≈ 1
lemniscate/NOW → reach 2; < 1 discrete → reach 3+): 2.269 / 0.873 / 0.805 on three inputs, identical whether `scale` is auto or hand-set.
Benchmark (Phase 42, `VAPMIP/benchmarks/all_voices/`): `OrbWeaverMonad.weave` **1.8 ms, 10.9 MB, ≈ 4.6 µWh**.
**Correction 2026-09-04:** paragraphs are anisotropic (a gasket cell with an integer curvature and an irregular boundary), so the
`Radius`/fixed-depth `Block` model is flagged for repair; sentence length comes from the *local* `b/c`, not a global scale.

**What Cody said about the results (2026-10-13 corrections, memory `project_scaled_kite_english_corrections`):**
(A) topic shift and the orb-weaver are **design targets, not authoritative**; (F) the **granular .bin "poison" was improper
sanitisation (never exercised)**; the orbweaver monad **has its own sentence constructor**; the first `ptol -w` output was
garbage **because of the bins**; bin sanitising is a later project, after prompt→response flow is approximated.
(Third pass: windspeed = *emission* of a sentence part, inexact allowed via the Recamán repass; two mechanisms,
EMISSION (discrete words) vs CONNECTION (conjugation map: tenses, participles; no grammatical tense code exists yet).)

---

## 3. The source that started it: citation record

Veritasium (2026), *Is spider web really stronger than steel?*, YouTube `wt4p2oalmRY`, uploaded 2026-08-02, 1,617 s.
**BUILT-AGAINST** (the impetus; no `Post-Hoc` tag). Fetched 2026-10-16 with yt-dlp (`player_client=mweb`), Mozilla UA, the
creator-supplied English subtitles; title verified from the site's metadata; transcript 5,119 words with cue timestamps.
Copies: `ContextPlease/claude/references/VAPMIPOrbweaver/` (transcript `.txt`, `.vtt`, metadata `.json`), mirror
`VAPMIP/docs/references/VAPMIPOrbweaver/`; ledger row in `ContextPlease/claude/references/INDEX.md`; entry in
`~/.clauderc_citations`; Ainulindale `wiki/129`.

What the episode gave the design (timestamps are in the transcript):

- **08:00–08:34 nanocrystals + amorphous regions:** ordered, rigid blocks joined by elastic cords; the cords stretch, the blocks spread the pull across the network → toughness. This is Phase 35's `CRYSTAL` / `SLACK`.
- **12:30–14:20 the pH dial:** in the storage sac the N-terminals repel (like charges, high concentration, no clumping); in the duct the pH drops, the charges neutralise, **the N-terminal ends pair and link the proteins into long chains**: a *context-triggered link*. This is `TRANSITION(on=context)`.
- **13:23–14:35 the duct:** micelles → globules → shear in a narrowing S-shaped duct → drawdown taper → final stretch aligns neighbours; "you cannot crystallise by sitting still, only by being pulled". This is the per-unit pipeline and the reason spinning is not extrusion.
- **14:56:** "exactly how the proteins assemble inside the spinning duct is still being studied": the same honesty the page carries (UNTESTED).

Secondary sources already paged in Ainulindale from the same arc (Post-Hoc): Vollrath & Knight (wiki 113), Rising & Johansson (wiki 117), Halliday & Hasan 1976 (wiki 118; the connective lexicon).

---

## 4. Where the semantics already live (the material the web is spun from)

| thing | where | note |
|---|---|---|
| the store | `VAPMIP/PtolC/monad3c.h`, `monad3_c.bin`: 347,119 words; four fields: words (164,283 learned), context/WordNet (146,743 `vec19`), phonetics (123,455), 2,248,064 co-occurrence edges | read-only mmap; the resident `ptolemy-monad.service` folds into it by design |
| 19 relations | `wordnet_boxkite.py` `RELATION_METHODS` (hypernyms … usage_domains); `vec19` per word; Γ_rad = tanh(½ ln(log_code/anchor)) | Γ_rad is a register/depth axis; `piano` (adverb sense) has an all-zero vector → NaN by design |
| hypernym-closure code | `engine/grammar/sem_hash.py` `sem_code`, `resonance` | discriminates concrete nouns that the 19-relation code leaves flat |
| the Zork parser | `PtolC/zork.c`/`zork.h`, `zork_parser.py` (C 197 verbs, Python 207; 5 verb conflicts, paper §9) | verb → one of 16 operators; PREP → relation label; IT → last noun |
| grammar layer | `engine/grammar/generate.py` (`ParseSpec`, `build_response`, `_rank`, `_resonant_pick`, `fill_phase`), `sails.py`, `shadow.py`, `frames.py`, `ptolc_bridge.py` | lexicalisation + realisation exist; **everything above the sentence does not** (`docs/context_flow_spec/08_generation_pipeline.md`) |
| the semantic part today | `console_speak` → `infer_speech_act` → word bag + ACT → bridge; Python path `ptolemy_console.py` `build_encounter_19d` + `ptolemy_monad.infer_direction` | replies are frames filled with WordNet neighbours (screenshots 4–7) |
| NLTK | skill `nltk-zork-wordnet` (`~/.claude/skills/`, mirrored in ContextPlease): no C API; RSS 346 MB with WordNet; tagger trained offline on UD-EWT 93.9 %; **Lesk / MFS / personalised PageRank each 2/7 on a tiny test** (topical edges needed); tagger / punkt_tab / stopwords data not yet downloaded | decision 2026-10-13: content processing stays on NLTK |

**Contextual Flow spec:** `VAPMIP/docs/context_flow_spec/` (95 tests, nothing implemented, first gate SM-02 ring independence):
`02` content words vs pathway words (M-SPLIT); `03` the Smith-chart topic locator (fold Γ = (Z−Z₀)/(Z+Z₀); cells = windows of order; degenerate-pair and saturation lessons);
`04` carry-over decay; `05` topic shift (TextTiling); `06` centering; `07` RST connectives; `08` the pipeline (Reiter & Dale 2000); `09` transformer methods taken.
Other pointers: wiki `Scaled-Kite-English-Thought-Center-Context.md` (two voices, §24), Tuning the Engine 35 (this model), 40/41 (boxkite deformation battery), 42 (every-voice benchmark).

---

## 5. The discussion: how to put the original semantic prime hash along an orbweaver pathway

(Recommendations, not decisions. Cody plans; the next session itemises and argues only where asked.)

### 5.1 The correspondence (web part ↔ semantic object)

| web | semantic object | existing code to reuse |
|---|---|---|
| **anchor** | the prompt's sense choice for each content word (a node with its `vec19`, Γ_rad, `sem_code`) | `monad3_lookup`, NLTK synsets |
| **hub** | the topic: the node set's lowest common hypernym / highest `sem_code` resonance; its Γ_rad is the register | `sem_hash.resonance`; NLTK `lowest_common_hypernyms`, `wup_similarity` |
| **radii** | through-lines: hypernym/hyponym chains (specificity axis) and the other relations; the prompt's `vec19` peaks rank which of the 19 relations are live radii | `vec19`, `RELATION_METHODS` |
| **scaffold spiral** (centre → out) | the outline: topic nodes ordered by hypernym depth / Γ_rad | `Radius` ↔ chain; `room_shape` b/c sets the reach |
| **capture spiral** (out → in) | the emission: the first monad's `J = β E² w` spreading over `A` (co-occurrence), restricted to the web's cells | `monad_speak` arithmetic (the lightest part) |
| **connectives** | the relation between consecutive nodes (WordNet relation → Halliday–Hasan / RST class → connective, with the radial move) | `_CONNECTIVES` in the orbweaver file; spec `07` |
| **frustration / pivot** | ≥ 3 near-equal relation peaks (needs the real `vec19`, not the sniffer) → `however` + `WRAP` | `_turbulence` |
| **sticky droplet (HOOK)** | an example word: a hyponym of the node | hyponym walk |

### 5.2 Why this is "the first monad, plus a web", not a rewrite

The first monad has exactly the two pieces a web needs and nothing else: an **address** (H2) and a **weighted neighbourhood** (A).
What it lacks is structure above the bag: no radii, no order, no connective, no sense. The web adds **order and relation** to the bag.
Start there: *the same J-spreading, but emission follows the scaffold→capture order and each step is labelled by the relation that licensed it.*
That is also the smallest change that can fail visibly.

### 5.3 Methods menu (ranked by cost, then by expected value)

1. **Spread-then-order (cheapest).** Run `monad_speak` unchanged; then re-order its top-k words by hypernym depth from the hub (scaffold) and place connectives by relation (capture). No new store. Test: relevance and order against the bag.
2. **Hub by resonance.** Compute the hub from `sem_code` gcd over the prompt's content words (H3); restrict A-spread to nodes within `r` hypernym steps of the hub. This is the "topic space" cell.
3. **Radii by relation.** One radius per live `vec19` relation; the capture spiral alternates radii (lateral move 0), steps along a chain (±1), pivots on contrast.
4. **Sense by web, not by Lesk.** Lesk scored 2/7: let the *hub* disambiguate (choose the synset whose ancestors share the most primes with the others), then check against NLTK's `lesk` as a control.
5. **Topic space as a fractal.** The hypernym tree is self-similar in the relevant sense (each level repeats the same relation vocabulary): treat `reach` (paragraph/section/chapter) as zoom level; use the Cassini `b/c` knob (the one measure that discriminated) to set it; the Apollonian gasket stays as the context-flow packing option (Phase 35, claims 10 and 12). **Test self-similarity before building on it** (distribution of branching factors per level).
6. **Phonetic channel.** The store has 123,455 phonetic entries (`ScalarContextPropagation` notebook `03_phonetic_prime_hashing`). Use as a tie-breaker and for morphology/euphony only after steps 1–4 work; no design exists yet for phonetic *selection*: ask Cody.
7. **CONNECTION (conjugation).** Tense/participle map is absent (third-pass note). NLTK lemmatiser + a small suffix table, after the above.

Not recommended now: E8 lattice evaluation, the full Navier–Stokes-of-context model, any box-kite object in this part (Cody's directive), anything that changes the store layout.

### 5.4 The weighting directive

Cody: the **semantic orbweaver pathway is weighted heavier than the context boxkite in sentence construction**.
Concretely (a proposal for Cody to confirm): the score of a candidate step is
`S = w_sem · S_web + w_ctx · S_kite`, with **w_sem > w_ctx** and the kite acting as a *constraint* that can extinguish a candidate (basin / annihilator
intersection, 2026-10-13 measurement: foci in different struts → total extinction) but **cannot outvote** the web. Starting point `w_sem : w_ctx = 2 : 1` as a **[PARAM]**,
then a measured sweep (1:1, 2:1, 3:1, 5:1, web-only), each result kept, including the ones that look worse. The kite remains the *scaled, moving* object
(De Marrais G2 deformations; never insert static functionality into it: memory `feedback_scalar_vs_scaled_boxkite`).

### 5.5 Test ladder (each rung leaves a notebook; failures stay in the code)

- **T0 baseline.** Reproduce the first monad's behaviour on today's store: `monad_speak` for `what is your name`, `can you hear what i am typing`; record the words, the J ranking, whether the program's own name appears. (The May store `monad_wordnet.bin`, 24,485 words, is not the current one; check `~/.ptolemy/` and the PtolemyHolcus clones **without writing to them**; never run `ptol` with the real HOME.)
- **T1 web only.** Relevance metric: mean hypernym distance (NLTK path similarity) of emitted words from the hub; order: fraction of consecutive pairs whose connective relation is licensed by a WordNet relation.
- **T2 weight sweep** (§5.4) against the same prompts and the six prompts of the paper (`what is a tree`, `can you play the piano?`, `finger pointer`, `good morning`, …).
- **T3 sanitisation isolation.** The granular `.bin` stays separate; run once with a deliberately poisoned bin and record what happens (Cody: the earlier poison was never exercised).
- **T4 cost.** Same harness as Phase 42: ms, MB, µWh per reply (orbweaver baseline 1.8 ms / 10.9 MB / 4.6 µWh; compiled REPL 28.8 ms/line; recorded energy method in the paper §16).

### 5.6 Traps already on the record

Saturating coherence measures (7 == 7): use `b/c` or σ_self-delta, and run a **control** with every claim. Sniffer-made `vec19` (use `weave_via`). Static
objects in the scaled kite. Anisotropic paragraphs (do not make every unit a uniform radius). "A measure that cannot discriminate is not a measure" (Phase 35).
Python `hash()` seed variation (`PYTHONHASHSEED`; the adapter varies across seeds). `ptol -say` must use the real HOME (a scratch HOME silently falls back to the word bag; paper §8). H1/H2/H3 confusion (§1.1).

---

## 6. Standing rules for the next session (short; the full set is in memory and `~/.clauderc`)

Maths in Unicode, never LaTeX. Code identifiers first. Cody plans, you itemise; opinion only when asked; no "shall I proceed?" after every change; a discussion
is a discussion. Check git/code before asking anything the repos answer. Never rewrite a mature file; modify in place. Failures stay in the code; chase every anomaly to a
verdict (CODE / MATHS / METHOD / emergence). No denial phrasing. GitHub token only (`GITHUB_TOKEN`); never touch `PTOL_SEED_TOKEN`. Every outbound request carries a Mozilla user agent; public works only.
**Push ContextPlease before clearing or rewriting any `.clauderc*` file (Cody, 2026-10-16: "always").** Primers live in `ContextPlease/claude/hist_prime/<repo>/`.
Licence: the Monad itself is Cody's; harness and everything else is GPL v3. The paper names no theory it leaves out (no GUT, Langlands or UFT); "Inside Out" is the established inversion J(z) = i/z̄.

## 7. Where to start reading (in this order, about an hour)

1. This primer; `ContextPlease/claude/.clauderc_context` newest entry.
2. `VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md` and the stub `43_semantic_orbweaver_pathway_construction.md`.
3. `VAPMIP/boxkite_orbweaver_monad.py` (535 lines; `weave`, `room_shape`, `_CONNECTIVES`).
4. `VAPMIP/PtolC/monad.c`: `monad_word_coords` (l. 170), `monad_learn_ex`, `monad_speak`; and `git show fb7ba29:PtolC/monad.c` for the original.
5. `VAPMIP/engine/grammar/sem_hash.py`, `generate.py`; `VAPMIP/wordnet_boxkite.py`.
6. `VAPMIP/docs/context_flow_spec/00_README.md`, `02`, `03`, `07`, `08`.
7. The transcript `ContextPlease/claude/references/VAPMIPOrbweaver/Veritasium_2026_Is_spider_web_really_stronger_than_steel_transcript.txt` (read 08:00–08:40 and 12:20–15:00).
8. `VAPMIP/paper/Forward_Propagation_of_Information.md` §4 (store), §7 (learning and speaking), §7.3 (the May screenshots), §8 (sentence path), §13 (encounter), §17 (tuning).
9. `FourthAgePapers/ScalarContextPropagation/` notebooks `01`, `03`, `05`; skill `nltk-zork-wordnet`.
10. Screenshots: `~/Desktop/SpaceClaude/ptol/1…7` (copies in `VAPMIP/paper/figures/`).

## 8. Questions for Cody (none block the discussion)

1. Which hash is "the original semantic prime hash": H1, H2 or H3 (§1.1)? Default used: H2 baseline, H3 content.
2. Is 2 : 1 an acceptable first `w_sem : w_ctx`, with the sweep deciding?
3. Does the May 2026 store (`monad_wordnet.bin`, 24,485 words) survive anywhere, so T0 can reproduce `holcussamestuffseemy` on its own data?
4. Phonetic selection: what should the phonetic field *choose* (rhythm, euphony, morphology)?
