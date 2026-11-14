---
name: nltk-zork-wordnet
description: >
  Reference and working method for using NLTK (Natural Language Toolkit) as the
  content-processing base for the Zork Sentence Parser and the WordNet-hashed
  monad: tokenising, POS tagging, chunking, lemmatising, WordNet synsets and
  relations, verb frames, word-sense disambiguation, topic bags, and what can
  and cannot be ported to C. Use whenever the work involves extracting topics,
  subjects, verbs, nouns or senses from a prompt, extending the Zork parser with
  WordNet, or discussing what NLTK offers. Records what was MEASURED in this
  environment (versions, data present, memory, accuracy), not what NLTK
  documentation claims.
---

# NLTK for the Zork Sentence WordNet Parser

Written 2026-10-13 from a working session (Claude Sonnet 5.5). Every number below was run on this machine unless tagged `[LIT]` (from memory, unverified). Labels: `[MEASURED]` `[LIT]` `[HYP]`.

## 0. Ground rules for this project
* NLTK stays the base (Cody's decision, 2026-10-13): the scalar boxkite already uses it. spaCy/Gensim/Stanza are NOT part of the plan. Overhead matters less than **bloat**.
* **NLTK is a pure-Python package. It has no C API.** But **Princeton WordNet has its own C library** (`wordnet-dev`, `wn.h`, `-lwordnet`) and this project already uses it (§8): the C side reproduces NLTK's WordNet-derived numbers with that library, mirrored against the Python side, and never calls NLTK. For anything else NLTK offers (perceptron tagger, chunk patterns, overlap counting) "C" means porting the algorithm and its data.
* No transformers. Offline at run time. Learning-time ingestion (search/crawl, treebanks) may use the network.
* Read before asking: definitions live in `~/.clauderc*` (`rcls`, `rccm`, `rcvq`), `Ainulindale/wiki`, and the context page `VAPMIP/docs/wiki/Scaled-Kite-English-Thought-Center-Context.md` (§13–§19 hold the NLTK experiments).

## 1. The Zork parser this extends (read these, do not re-derive)
**Provenance:** the Zork Sentence Parser is prior work Cody specifically engineered with, a deliberate tool selection. All references to it are built-against, NEVER `Post-Hoc:` (Cody, 2026-10-13).
* **Reference implementation:** `VAPMIP/zork_parser.py` (570 lines). Philosophy in its docstring: *the Infocom parser fit in 512 KB because it constrained the problem: vocabulary first, verb governs, grammar is a table, unknown words fail loudly, scope limits candidates.* Lineage studied: ZIP 1979, ZIL 1981, ZILCH 1982-85, Inform 6 `parser.h` 1993 (Inform 7 skipped).
* **Mapping:** VERB → one of 16 sedenion operators (`OPERATOR_VERBS`, hand table, e0 identity … e15 emit); NOUN → a word in the monad vocab; PREP → A-matrix relation; IT/THEM → anaphor = last noun (e11 dereference).
* **Parse steps (`_parse_one`):** tokenise (lowercase, split on whitespace/punctuation, 6-letter prefix expansion on the VERB ONLY) → direction shorthand → verb is always token 1 (two-word verbs tried first: "pick up") → unknown verb = helpful error → strip articles → resolve pronouns → `_split_prep` (first PREP not at index 0 splits into ≤2 noun phrases) → remember last noun. `_split_conjunctions` splits on "and" only when the right side starts with a known verb. Templates: `()`, `(N)`, `(N,P,N)`, `(P,N)`, `(D)`.
* **Other incarnations:** `VAPMIP/PtolC/zork.c` (same verb table in C, 344 lines, header `zork.h`); `PtolemyDesktop/Archimedes/parser.py` (maths version: verb → operation, `from..to`, `with respect to`); `PtolemyDesktop/Tesla/Zork_Sentence_Parser.py` and `IPZSP.py` (game-style `ParsedCommand`: action, direct/indirect object, preposition); `monad_harness_diagnostic.py` and `lshs_portrait.py` also mention the Zork parser (not read).
* **ACTIVE IN THE MONAD (read 2026-10-13, not run):** `zork.c` is in the `ptolemy` Makefile `SRCS` and `main.c` calls `zork_parse(linebuf)` on every line of the `-r` REPL (`ZorkResult`: `op 0-15, op_name, verb, noun, noun2, prep, prompt, ok, error, is_slash, slash_cmd, slash_args`). Slash commands (`/generate /status /health /vocab /reset /help /RTFM`) are handled in the REPL; a known verb becomes `prompt` ("take lamp" → e5 abstract lamp) and goes to `monad_speak()`; plain text passes through; unknown verb prints the Zork error and falls back to the raw line. `zork_reset_context()` clears the pronoun noun.
* **The constraint to honour:** the original ran in a tiny memory budget (Cody: 256 MB machine, months of work). NLTK does not fit there (see §3).

## 2. Where NLTK plugs into each Zork step
| Zork step | NLTK machinery | Notes |
|---|---|---|
| tokenise | `nltk.tokenize.NLTKWordTokenizer().tokenize(s)` (no data); `RegexpTokenizer`; `MWETokenizer([('pick','up')], separator=' ')` for two-word verbs | `word_tokenize` needs `punkt_tab` (missing here) |
| verb inflection ("took", "takes") | `wn.morphy(word, 'v')` → lemma or `None` | rule + exception lists; `[MEASURED]` took→take, children→child, mice→mouse, running→run |
| verb → operator | `Synset.lexname()` gives 15 verb classes (`verb.body … verb.weather`) | `[HYP]` could extend the 16-operator hand table to the whole verb lexicon; untested |
| verb grammar template | `Lemma.frame_ids()` / `frame_strings()`: 35 distinct frame ids (`[MEASURED]`), e.g. "Somebody give somebody something" | WordNet's own per-verb Infocom-style template table |
| noun lookup / sense | `wn.synsets(w, pos)` (ordered by frequency), `Synset.definition()`, `.hypernyms()`… | |
| disambiguation | `nltk.wsd.lesk(context_sentence, ambiguous_word, pos=None, synsets=None, lang='eng')` | weak, see §4 |
| POS tags | `nltk.tag.PerceptronTagger` | **must be trained locally**, §3 |
| chunks (noun/prep phrases) | `nltk.chunk.RegexpParser(grammar, root_label='S', loop=1, trace=0)` | grammar like `NP: {<DET>?<ADJ|NOUN>*<NOUN>}` |
| anaphor | keep the Zork rule (last noun); NLTK has nothing better offline | |
| conjunction split | keep the Zork rule | |

## 3. Environment facts `[MEASURED]`
* NLTK 3.10.3, Python 3.12, **venv: `PtolemyDesktop/.venv/bin/python`** (system `python3` crashes on `import nltk`: pandas ABI mismatch; see memory). `nltk` resolves from `ValaQuenta/.venv/lib/python3.12/site-packages`.
* Data present: WordNet 3.0 as `~/nltk_data/corpora/wordnet.zip` (10.7 MB), `punkt`, `words`, `cmudict`. **Missing:** `averaged_perceptron_tagger*`, `punkt_tab`, `stopwords`, `maxent_ne_chunker`, `omw-1.4`, WordNet IC corpora (so `res/jcn/lin_similarity` fail; `path`, `wup`, `lch` work).
* **Memory (peak RSS):** bare Python 12 MB → `import nltk` **164 MB** → WordNet loaded **346 MB** (2.7 s) → iterating every synset **571 MB**. Does not fit a 256 MB budget; the monad's precomputed `.bin` files exist for that reason.
* **POS tagger without downloads:** train `PerceptronTagger(load=False).train(sentences, nr_iter=5)` on `VAPMIP/datasets/UD_English-EWT` (CoNLL-U, UPOS). Result: **93.9 % UPOS accuracy** on the EWT test set (uni+bigram backoff 87.3 %), 4.1 MB pickle, 0.28 ms per 7-token sentence, 44 s to train. Script and weights: `.claude/scratchpad/2026-10-13_nltk_extraction_pipeline/` (`tagger_train.py`, `perceptron_ewt.pkl`).
* Prompt pipeline (tokenise → tag → chunk → morphy → own extended Lesk): 3–19 ms warm; first call ≈ 3.9 s (WordNet load). `extract.py` in the same folder.

## 4. Disambiguation, measured `[MEASURED]` (tiny samples, illustrative)
* On 7 sentences: NLTK `lesk` 2/7, most-frequent-sense 2/7, personalised PageRank over the typed WordNet graph 2/7 (`.claude/scratchpad/2026-10-13_wsd_lesk_vs_ppr/`). Plain Lesk picked the *electrical* `reactor.n.01` for "neutron generation in different reactor types".
* Own **extended Lesk** (sense gloss + glosses of its related synsets vs glosses of the context words' senses) fixed `bank` and the power `plant`, but still failed the six-word target prompt.
* **Topic bag from an ingested overview** (114 lemmas from a search-AI overview of "neutron generation") resolved `reactor` → `nuclear_reactor.n.01` (21 vs 2), `generation` → `generation.n.06` (3 vs 2, thin), `neutron`; failed on generic `type`. Generic words need a margin rule with an explicit MFS fallback.
* **WordNet gaps found:** "pressurized water reactor" is not a synset; reactor/atom_bomb/neutron share only top-level ancestors. Typed edges lack the topical tie; learned `A` edges or ingested topic bags must supply it. `monad3_c.bin` stores relation **degree** (log2-compressed count), not identity; identity must come from WordNet or an overlay.

## 5. API cheat-sheet (verified by introspection, 3.10.3)
* `from nltk.corpus import wordnet as wn`: `wn.synsets(word, pos=None)`, `wn.synset('dog.n.01')`, `wn.lemmas`, `wn.all_synsets(pos)`, `wn.all_lemma_names()`, `wn.morphy(form, pos)`, `wn.ensure_loaded()`; lexicographer class via `Synset.lexname()`. POS letters: `n v a s r`.
* `Synset`: `.definition() .examples() .lemmas() .lemma_names() .pos() .lexname() .hypernyms() .hyponyms() .instance_hypernyms() .member/part/substance_holonyms() .member/part/substance_meronyms() .attributes() .entailments() .causes() .also_sees() .verb_groups() .similar_tos() .topic_domains() .region_domains() .usage_domains() .hypernym_paths() .common_hypernyms() .lowest_common_hypernyms() .path_similarity() .wup_similarity() .lch_similarity()` (+ IC-based `res/jcn/lin` needing `wordnet_ic`). The 19 relation methods are the project's `RELATION_METHODS` (`wordnet_boxkite.py`).
* `Lemma`: `.name() .count() .antonyms() .derivationally_related_forms() .frame_ids() .frame_strings() .synset()`. `Lemma.count()` = SemCor sense frequency (basis for most-frequent-sense).
* Tagging/chunking/stemming: `nltk.tag.{PerceptronTagger, UnigramTagger, BigramTagger, DefaultTagger, RegexpTagger, AffixTagger, CRFTagger, BrillTaggerTrainer, HiddenMarkovModelTagger}`; `PerceptronTagger.train(sentences, save_loc=None, nr_iter=5)`; `nltk.chunk.RegexpParser`; `nltk.stem.WordNetLemmatizer().lemmatize(word, pos='n')`, `PorterStemmer`, `SnowballStemmer`.
* Text statistics: `nltk.text.{Text, TextCollection, ContextIndex, ConcordanceIndex}`, `nltk.probability.{FreqDist, ConditionalFreqDist}`, `nltk.collocations`, `nltk.lm` (n-gram models), `nltk.tokenize.texttiling.TextTilingTokenizer` for topic-shift splitting. Not needed here (bloat): `parse, sem, inference, ccg, translate, cluster, classify, sentiment`.

## 6. Pitfalls
* `wn.morphy` returns `None` for unknown forms; fall back to the surface form.
* `wn.synsets(w)[0]` is the most frequent sense, not the right sense (`reactor` → electrical).
* `lesk` ignores everything but gloss overlap; short prompts give it almost nothing.
* `frame_strings()` has the verb word baked in (28,267 distinct strings); use `frame_ids()` (35) as the template key.
* UD tags are UPOS (NOUN, VERB, ADJ…), not Penn tags; map UPOS → WordNet pos with `{'NOUN':'n','PROPN':'n','VERB':'v','ADJ':'a','ADV':'r'}`.
* Tagger errors seen: "produces" → NOUN; "neutron" → ADJ (compound modifier). The Zork-style repair (a word WordNet knows only as a noun, directly before a noun, is a noun) fixed the second.
* Never claim a C binding; never claim an accuracy that was not run.

## 7. Working method
1. State the question in Zork terms (which step: verb, noun, prep, anaphor, template).
2. Prototype in the venv, in `.claude/scratchpad/<date>_<topic>/` with a README of what was measured, mirrored to `ContextPlease/claude/scratchpad/`.
3. Record results on the context page, tag evidence, mirror per the ContextPlease protocol.
4. Port to C only after the Python design is accepted; the C side reads WordNet dict files / `.bin` files, never NLTK.

## 8. The C side that already exists (read 2026-10-13)
* `VAPMIP/PtolC/dump_boxkite_bin.c` **builds `c_monad_wordnet.bin`** with the real Princeton WordNet C library (`gcc … -lwordnet`; `WNSEARCHDIR=/usr/share/wordnet`): one `BoxKiteEntry` per word's FIRST sense (`word[32], pos, synset_offset, vector[19], depth_weight`, header in `boxkite_bin.h`), 154,725 entries / 12.7 MB. It reads `index.noun/verb/adj/adv` as text (`getindex()` is a fuzzy search, not an iterator), calls `index_lookup()` and `read_synset()`, counts only synset-level pointers (`pfrm==0 && pto==0`, as NLTK's synset accessors do) and applies `compress_count = round(log2(n+1))`. Same 19 relations in the same order as `wordnet_boxkite.RELATION_METHODS`. `wntest.c` verified `bank` (HYPERPTR=1, HYPOPTR=2) against Python. CHANGELOG: "built against the real WordNet C library, not the NLTK dump, mirrored against `wordnet_boxkite.export_pickle()`" (Python export: 147,306 entries; C: 154,725 — coverage differs, not reconciled here).
* `ptol.c` mmaps `monad3_c.bin` (48 MB: `c_monad_wordnet.bin` + `monad_phonetic.bin` + `monad_english.bin`, `Monad3cHeader`, one bsearch on a sorted `WordRec` table) and computes the Gamma-Radial windspeed in C (`monad3_gamma_radial`). Sentence creation is still Python: `ptol.c` `popen`s python3+NLTK (`get_monad_words`, then `engine/grammar/ptolc_bridge.py` = VerbNet sails + WordNet hypernym fill + SELRESTR gate; sentence mode default since 2026-09-11). `make corpus` fetches NLTK WordNet for the Python side. The pure-C port of the WordNet composter is noted as future work in `ptol.c`.
