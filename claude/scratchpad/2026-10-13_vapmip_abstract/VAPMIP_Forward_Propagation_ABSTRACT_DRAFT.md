# Forward Propagation of Information: Teaching The Maths how to speak English

**Cody Michael Allison** (Michael Rendier) · independent researcher · the.wandering.god@gmail.com · ORCID 0009-0007-7239-6760

*DRAFT abstract v2, 2026-10-13, for Cody's review (v1 used only the compiled voice; v2 adds the box-kite voice from `claude-stuff.png`). Not placed in `VAPMIP_Paper.md`: that file's own note defers the "teach the maths to speak English" thesis; this draft is the first statement of it.*

## Abstract

We report a successful experiment in teaching the maths to speak English. A language engine built from engineered operators runs entirely offline on a 2018 ThinkPad X1 Carbon (Core i7-8550U, no GPU, no network). A verb-governed parser in the Infocom/Zork tradition selects one of sixteen operators; the store holds each word as the counts of its 19 WordNet relation pointers, with a prime-number address per word. The engine speaks in two voices, both measured. The **compiled voice** replies in about 19 to 26 ms and 63 MB of resident memory, with a single word lookup inside the timer's 10 ms resolution and 3.2 MB; measured on battery discharge, the whole laptop spends **66.6 µWh per reply**, about 4,500 times less than the roughly 0.3 Wh public estimate for one typical LLM query (the engine's own share is below the method's resolution, at most about 12 µWh). The **box-kite voice** chooses a grammatical frame from whichever WordNet relation dominates the prompt's context and fills it with the words nearest that context: "finger pointer" returns "it is made of pinkie and pinky." It decomposes, classifies, enumerates, compares and situates, in about two seconds per reply in Python. Section 1 reports these benchmarks as literal terminal transcripts, each with the script that produced it; the sections after it define the address, the parser and the store as code that runs. The road from here is a single voice: porting the relational composter into the compiled engine, with a prompt-extraction front end already built (3 to 19 ms warm, a part-of-speech tagger trained offline to 93.9%) to carry the prompt's topic through the reply.

## Evidence for every number (convention D: transcripts; each figure is measured or labelled arithmetic)

| Claim in the abstract | Where it comes from | Kind |
|---|---|---|
| 2018 ThinkPad X1 Carbon, i7-8550U | `/sys/class/dmi/id`, `/proc/cpuinfo` (2026-10-13) | measured |
| 19–26 ms per reply (compiled) | `ptolemy -r -n`: 82 lines in 1.672 s after a 0.182 s start = 18.6 ms/line; 5,000 lines in 129.3 s = 25.9 ms/reply with the 0.5 s power sampler running | measured |
| 63 MB resident | `/usr/bin/time` on `ptolemy -r -n`, 63,176 KB | measured |
| lookup under 10 ms, 3.2 MB | `ptol -M tree`, 0.00 s wall, 3,200 KB | measured (timer resolution 10 ms) |
| 66.6 µWh per reply | mean 9.255 W whole laptop on battery × 25.9 ms = 0.240 J | measured power, arithmetic |
| ≈4,500× below ≈0.3 Wh | 0.3 Wh ÷ 66.6 µWh; public figures 0.24 Wh (Google), 0.34 Wh (OpenAI), ≈0.3 Wh (Epoch AI) | public, via secondary coverage |
| engine share ≤ ≈12 µWh | (9.255 − 7.57 W lower idle) × 25.9 ms; idle drifted 7.57 → 10.35 W so the true share is unresolved | bound, not a measurement |
| sixteen operators, Zork parser | `VAPMIP/zork_parser.py`, `PtolC/zork.c`, REPL in `main.c` | read, run |
| 19 relation counts, prime address | `wordnet_boxkite.py`; C rebuild `PtolC/dump_boxkite_bin.c` (154,725 entries, 12.7 MB) | measured earlier, companion paper |
| box-kite voice, "finger pointer" → "it is made of pinkie and pinky." | `rotary_rerun_boxkite_monad.py` `process_input()`; `.claude/scratchpad/2026-10-13_boxkite_monad_voice/bk_try.py`; matches the 2026-09-11 console screenshot | run twice (2026-09-11 console, 2026-10-13 headless) |
| ≈2 s per reply (box-kite) | 1.8, 2.1, 2.4 s warm; 8.05 s first call (WordNet load) | measured |
| 3–19 ms front end, 93.9% tagger | `.claude/scratchpad/2026-10-13_nltk_extraction_pipeline/` (`extract.py`, `tagger_train.py`, UD-EWT test set) | measured |

Raw output: `.claude/scratchpad/2026-10-13_monad_energy/`, `…_boxkite_monad_voice/`, `…_nltk_extraction_pipeline/`; context page `VAPMIP/docs/wiki/Scaled-Kite-English-Thought-Center-Context.md` §22–§24.

## Conventions applied (cs-paper-code-conventions)
* Benchmarks = **D** (REPL transcripts with prompt and reply). Parser, address, store = **B** (short verbatim listings) or **A** (path + function) by size. WordNet, NLTK, Infocom/Zork = **A**: cited, not re-derived; Zork is built-against, not post-hoc. The unported composter = **C**, labelled THEORETICAL.
* Engineered-operator vocabulary only (no theory names), per the standing rule for the speaking engine.
