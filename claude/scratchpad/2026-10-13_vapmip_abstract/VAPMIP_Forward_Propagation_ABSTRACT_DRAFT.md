# Forward Propagation of Information: Teaching The Maths how to speak English

**Cody Michael Allison** (Michael Rendier) · independent researcher · the.wandering.god@gmail.com · ORCID 0009-0007-7239-6760

*DRAFT abstract, 2026-10-13, for Cody's review. Not yet placed in `VAPMIP_Paper.md` (that file's own note defers the "teach the maths to speak English" thesis; this draft is the first statement of it).*

## Abstract

We report a successful experiment in teaching the maths to speak English. A language engine built from engineered operators runs entirely offline on a 2018 ThinkPad X1 Carbon (Core i7-8550U, no GPU, no network): a verb-governed parser in the Infocom/Zork tradition selects one of sixteen operators, a WordNet-derived store holds each word as the counts of its 19 relation pointers, and every word carries a prime-number address. It replies in about 19 to 26 ms and 63 MB of resident memory; a single word lookup finishes inside the timer's 10 ms resolution and 3.2 MB. Measured on battery discharge, the whole laptop spends **66.6 µWh per reply**, about 4,500 times less than the roughly 0.3 Wh public estimate for one typical LLM query; the engine's own share is below the method's resolution (at most about 12 µWh). Its replies are word-level and sentence-level fragments built from the prompt's firing words ("what is a tree" → "kite its engine probe"). Section 1 reports these benchmarks as literal terminal transcripts with the script that produced every number; the sections after it define the address, the parser and the store, each as code that runs. The next stage, carrying the prompt's topic through the reply (prompt extraction, sense choice, a document planner), already has a built front end (3 to 19 ms warm; a part-of-speech tagger trained offline to 93.9%) and is specified here as the road from fragments to conversation.

## Evidence for every number (convention D: transcripts; every figure is a measured figure or labelled arithmetic)

| Claim in the abstract | Where it comes from | Kind |
|---|---|---|
| 2018 ThinkPad X1 Carbon, i7-8550U | `/sys/class/dmi/id`, `/proc/cpuinfo` (2026-10-13) | measured |
| 19–26 ms per reply | 82 REPL lines in 1.672 s after a 0.182 s startup = 18.6 ms/line; 5,000 lines in 129.3 s = 25.9 ms/reply (with the 0.5 s power sampler running) | measured |
| 63 MB resident | `/usr/bin/time` on `ptolemy -r -n`, 63,176 KB | measured |
| lookup under 10 ms, 3.2 MB | `ptol -M tree`, 0.00 s wall, 3,200 KB | measured (timer resolution 10 ms) |
| 66.6 µWh per reply | mean 9.255 W whole laptop on battery × 25.9 ms = 0.240 J | measured power, arithmetic |
| ≈4,500× below ≈0.3 Wh | 0.3 Wh ÷ 66.6 µWh; 0.24 Wh (Google), 0.34 Wh (OpenAI), ≈0.3 Wh (Epoch AI) | public figures via secondary coverage |
| engine share ≤ ≈12 µWh | (9.255 − 7.57 W idle) × 25.9 ms; idle drifted 7.57 → 10.35 W so the true share is unresolved | bound, not a measurement |
| sixteen operators, Zork parser | `VAPMIP/zork_parser.py`, `PtolC/zork.c`, `main.c` REPL | read, run |
| 19 relation counts, prime address | `wordnet_boxkite.py`; C rebuild `PtolC/dump_boxkite_bin.c` (154,725 entries, 12.7 MB) | measured earlier, companion paper |
| "kite its engine probe" | `ptolemy -r -n`, input "what is a tree" (Zork `e0/identity`) | run 2026-10-13 |
| 3–19 ms warm, 93.9% tagger | `.claude/scratchpad/2026-10-13_nltk_extraction_pipeline/` (`extract.py`, `tagger_train.py`, UD-EWT test set) | measured |

Scripts and raw output: `.claude/scratchpad/2026-10-13_monad_energy/`, `…_nltk_extraction_pipeline/`; context page `VAPMIP/docs/wiki/Scaled-Kite-English-Thought-Center-Context.md` §22, §23.

## Conventions applied (cs-paper-code-conventions)
* Benchmarks = **D** (REPL transcripts, prompt included). Parser, address, store = **B** (short verbatim listings) or **A** (path + function) by size. WordNet, NLTK, Infocom/Zork = **A**: cited, not re-derived; Zork is built-against, not post-hoc. The unbuilt planner = **C**, labelled THEORETICAL.
* The abstract uses the engineered-operator vocabulary only (no theory names), per the standing rule for the speaking engine.
