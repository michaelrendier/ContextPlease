# Context primer — 2026-10-18 — SemPriCon: the golden-ratio monad documented as it was

Backward: `semantic_orbweaver_notes.md` (2026-10-17 trace), `CONTEXT_PRIMER_2026-10-16_SEMANTIC_ORBWEAVER.md`. Forward: the semantic prime-concept hash (not started), then the five-language test.

## What happened
Cody scrapped the WordNet-writer build and asked for the bare mechanism that produced `holcussamestuffseemy`, documented before it is changed. Work directory `VAPMIP/SemPriCon/` (pushed: `29b2d2d` assessment, `6ec2b3d` gitignore, `ba5acaf` paper). Order followed: Fresh Start Protocol (assess, push, then gitignore the bin), notebooks, paper (skill `cs-paper-code-conventions`, format of `VAPMIP/paper/Forward_Propagation_of_Information.md` §1–2), commit and push.

## Locations
| what | where |
|---|---|
| reference source, unmodified | `VAPMIP/SemPriCon/src/PtolC_eb28ce8/` (= `git archive eb28ce8 PtolC`); build copy in `build/` (gitignored) |
| the store | `SemPriCon/dirty/monad_wordnet_v4_20260519.bin` (read-only, gitignored); same bytes in `~/.ptolemy/dirty/monad_wordnet.bin`, `~/.ptolemy/clean/…`, `VAPMIP/checkpoints/clean/…`; sha256 `66f70c70…faf31` |
| notice / assessment | `SemPriCon/dirty/monad_wordnet_v4_20260519.{POISON.md,ASSESSMENT.md,assessment.json}` (+ the 2026-05-17 v2-format assessment copy) |
| tools | `SemPriCon/tools/`: `ptol_bin.py` (reader), `assess_bin.py`, `monad_py.py` (port), `verify_against_c.py`, `verify_learn_against_c.py`, `make_notebooks.py` |
| notebooks | `SemPriCon/notebooks/01…06` (executed, no errors) |
| paper | `SemPriCon/paper/The_Golden_Ratio_Monad.{md,pdf}`; `template.md` + `evidence.py` + `make_paper.py` (`--check` passes) + `build_pdf.sh` |
| older bins | `PTorrent/bin_archive/{clean,dirty}/` (the PTorrent README's "POLLUTED" notice is about the v1.111 `~/Documents` bin, a different file) |

## Findings (all measured; see paper §14–§17)
1. Store: PTOL v4, 24,485 slots, 6,825,748 links, wc 121,914,388 = the screenshot header. DIRTY/PASS (5.04 % polluted; entropy 88.68 %; Gini 0.7564). 0 non-ASCII words; the C tokenizer cannot admit any.
2. `holcus` (first word of all 8 standard prompts) = display label of slot 24639, which is the slot of the word *in* (E difference 1.2e-6); 5th best-connected slot; chosen by the nearest-E-to-Ω selector. 92/150 random prompts.
3. `PTOLEMY_IDENTITY` was learned into the store (646 of 646 identity edges present; chance ≈ 14).
4. Address collapse: float seed loses fractional bits; every word of ≥ 8 letters addresses to slot 0; 7 letters → 64 slots; `philadelphos` and `septuagint` both at slot 0.
5. Slot display = highest-E arrival; 5.1 % of WordNet lemmas are their slot's label.
6. Further limits: approximate zeros, reply length fixed at 4, β saturation, unused constants, comment/code mismatch, word map not saved, `prose_seen` per slot.

## Decisions and standing statements (Cody, 2026-10-18)
- The code is authoritative to the paper (authorship and authentication). File on arXiv (spelling) when happy.
- Fresh Start Protocol: working bins (`monad3_c.bin`, anything `ptol.c` uses) are off limits to tests; archive as clean/dirty with an assessment (diagnostic if dirty); push assessments; only then gitignore the bins.
- Primes are the destination of the hash, not a component. Semantic graph from the golden-ratio lineage; WordNet = weighting/calibration/fallback; only new functionality in the orbweaver context; modify, don't rewrite.
- Five-language test after the paper: living languages, no shared roots/semantic/cultural associations.
- His debugging practice: a `dbprint`-style live feed of every change (`Ptolemy2/Pharos/UtilityFunctions.py: dbprint`, `client.DEBUGPRINT`); the C binary's `-v` feed is the same.

## Open
- Which ingest introduced `holcus` (no training log). Whether the screenshot's missing visible spaces differ on a tty. The claude.ai project conversations (mixed Ainulindale/Ptolemy) that made the first prime-concept hash are not on disk; Cody has them.
- Literature in the paper is cited from knowledge, not fetched: verify before filing.
