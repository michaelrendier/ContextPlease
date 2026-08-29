# 2026-08-28 — primer corpus → Monad .bin

Cody: use the migrated context primers to adjust the Monad's `.bin` weights —
strip the delimiters/maths on the fly, feed only the prose. "Make it so the
monad learns all of them." Especially the war-corpus discussion. Use other
`.bin` files for maths / physics.

## Done

**`corpus_strip.py`** — reads every `hist_prime/**/*.{txt,md}` +
`hist_todo/**` and strips to prose: YAML frontmatter, ``` fences (the
maths/code — already in the code), `|` tables → cell text, box-drawing,
`===`/`---` rules, `#` heading markers, list/quote markers, `[t](url)` →
`t`, inline `` `code` ``, HTML tags, file paths/URLs, `KEY: value` prefixes,
and any line that is >35 % math/greek/symbol characters. → **205 files,
210,121 prose words.**

**`ingest.py`** — `VAPMIP.monad.Engine`, learned the corpus paragraph-by-
paragraph (adjacency respects sentence order), `weight = 1.5` (Cody's own
detailed engineering descriptions = authoritative). Saved to a **new** bin:

    ~/.ptolemy/monad_engineering.bin   (3.3 MB)
      202,540 words learned in 3.0 s
      20,677  unique addressed words (Horner→prime→γ addresses)
      185,424 A-matrix edges
      β field: 797 words deepened past 0.5

**Live bins untouched** — `monad_english.bin` (36 MB), `monad_war.bin` etc.
Engineering is its own domain bin, same pattern as
`monad_{mathematics,physics,python,c}.bin` already in `~/.ptolemy/`.

### Verified — reload + A-matrix probe

    monad       → the, is, information, pool, ecu, state, isolation
    sedenion    → boundary, zero, algebra, mastery
    riemann     → zeta, zeros, hypothesis
    caesar      → face, julius, cicero, corpus
    war         → corpus, famine, pestilence, wordnet, costs
    corpus      → ingestion, visualizer, bins, descriptor, acquisition
    engineering → work, experiment, built, error, first
    vocab incl. noether, octonion, holcus, crankshaft, telperion,
                hyperwebster, laplacian, box-kite

It genuinely learned the engineering vocabulary and its co-occurrence
topology. (Stop-words show as high-weight neighbours — expected for a raw
co-occurrence graph; `speak()`'s `_DIM_ROLE` grammatical machinery filters
them at emission.)

## "That's all doable right?" — yes. Status per sub-part

| sub-part | status |
|---|---|
| strip delimiters/maths on the fly, ingest prose only | **DONE** (`corpus_strip.py`) |
| monad learns all primers + TODOs | **DONE** (`monad_engineering.bin`) |
| per-domain bins for maths / physics / python / c | **already exist** in `~/.ptolemy/`; the engineering bin slots alongside; `_MATH_MARKERS` in `monad.py` routes math prompts to depth 5–8 |
| the **war-corpus discussion** = the **prime-directive conversations** (Cody) | **DONE** — `ingest_war.py`. Backed up `monad_war.bin` → `.bak-20260828-224000`, folded in `CONTEXT_PRIMER_2026-05-26_PRIME_DIRECTIVES.txt` + `_SEDENION_ROKO.txt` + `PRIMER_2026-05-29_Phase2_to_Phase5.txt` + `ArdaQuenta/CONTEXT_PRIMER_2026-05-30.txt` at weight 2.0 (directives = authoritative). 829 → **3,006 words**, 2,986 → **12,162 edges**, 86 KB → 311 KB. Probe: `prime → directives(1.0), directive, hash, p1`; `corpus → ingestion, poisoning, war, corrupted, attack`; `spectral → tools, intelligence, mathematics, directives`. |
| maths layer = "modifier to a word-group position into notation/functions" | **design, doable** — the ValaQuenta `EquationModule` registry + `monad.py` `_DIM_ROLE` grammatical roles: a word-group occupying the math dimensions triggers a registry lookup → an `Equation` (notation + exact `compute()`). "Correct even if the wrong tool" = the registry always returns the exact result of whatever equation the phrase resolves to. Wiring point: `Engine._fire()` / `generate()`. |
| Flashlight Pencil — spectrally show the **proper content of a response** | **design, doable** — the Pencil HyperString decomposes a relation into 7 strut-pairs; the Flashlight is its inverse (struts from shadows). On a raw `generate()` output (the shadow): run `spectral.py` `spectral_decompose` on the word-address / β trajectory, reconstruct the full "proper" content from the dominant spectral lines. Post-processing pass on `generate()`. |

## Files

- `corpus_strip.py`, `corpus_all.txt` (1.4 MB), `corpus_war.txt` (over-broad, see above)
- `ingest.py`, `strip_all.log`
- output: `~/.ptolemy/monad_engineering.bin`
