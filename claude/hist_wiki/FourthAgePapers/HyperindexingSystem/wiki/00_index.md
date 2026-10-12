# HYPERINDEXING SYSTEM — WIKI INDEX

The engineering record of every distinct or successful version of the hyperindexing code, in chronological order: one page and one notebook set per version. Modelled on the VAPMIP *Tuning the Engine* wiki.

> **PROTOCOL.** A new version is a new page in this directory **and** a new notebook directory in [`../notebooks/`](../notebooks/); add its row below. Every page states its source path, its date and the basis of that date, what runs, what was measured (with the notebook that measured it), and how the version behaves under permutation of the string. **A repass on this index is part of every update:** re-check the whole table is current (no missing version, no stale date) before calling the update done.

*23 pages: versions v00–v19 (pages 01–20) and three synthesis pages S1–S3 (pages 21–23). Pages by Claude Sonnet 5.5 (2026-09-29).*

## How the notebooks work

Each notebook loads the historical source file **unmodified, by path** (`importlib`), so a notebook cannot drift from the code it documents. Each begins with the same self-contained prelude (perpetual-now rule: none depends on state from another). The fixed 4,000-character corpus sample is `notebooks/corpus_sample.txt`. Every claim in a page is a printed output of a notebook cell, or is labelled an estimate. Run all: `notebooks/_run.sh` (about fifteen minutes; v16 alone takes 100 s). Machine: Intel i7-8550U, 8 logical CPUs, Linux 6.8.0, Python 3.12.3.

## Dating

The git dates below are commit dates. **v00–v07 share one date (2026-04-18): the clean initial commit of `PtolemyDesktop`, which imported every file at once.** That commit bounds when those files existed; it does not date their writing. Their order is inferred from the code, and the evidence is stated on each page:

| pair | evidence |
|---|---|
| v01 before v02 | `list.index` lookup and the docstring "no physical location behind a multilayered 256 bit" (v01); dictionary lookup and hex address (v02); v02 keeps v01's method names |
| v02 before v03 | v03's docstring answers v02's width problem; v03's names (`_str_to_int`, `IndexRecord`) are the ones v09 keeps |
| v04 before v05 before v06 | `VectorAddress` gains `meta` (v05) and `from_label(…, meta)` (v06) |
| v06 before v07 | v07 builds on the word-token idea and carries only the limb constant |

Archive anchor: v00's file also sits, byte-identical, in the claude.ai Project archive, whose TODO ("Added: 2026-04-16") already names its classes, so v00 existed by 2026-04-16 (page 01). Dated anchors: v08 2026-04-24 (`3a5d7e6`); v09 2026-05-02 (`4f708d8`); v10 2026-05-03 (`6b987e4`); v11 2026-05-12; v12 2026-05-19 (`_word_zero_idx` unchanged since 2026-05-27, `204c75d`); v13 2026-06-14; v14 2026-06-28; v15 2026-08-25; v16 2026-08-30; v17, v18 2026-09-25; v19 2026-09-27.

## Versions

| Page | Version | Date | Code | Status |
|------|---------|------|------|--------|
| [01](01_v00_first_age_text_hyperindex.md) | v00 | 2026-04 (in-file) / 04-18 | `Archive/ainulindale_first_age/FA_smnnip_hyperindex.py` | ancestor; not a bijection (length stored) |
| [02](02_v01_bijective_prototype_and_flag_packet.md) | v01 | 04-18 (inferred first) | `HyperWebster-Data-Storage/infinite-data.py` | prototype: bijective, 8-bit flag + 248-bit coordinate; not importable |
| [03](03_v02_hex_address.md) | v02 | 04-18; used 04-24 | `HyperWebster-Data-Storage/hyperwebster.py` | **shipping baseline** |
| [04](04_v03_sha_label_and_payload.md) | v03 | 04-18 | `HyperWebster-Data-Storage/hyperwebster-hash.py` | label + payload split; adopted by v09 |
| [05](05_v04_vector_address_and_orbit_cache.md) | v04 | 04-18 | `HyperWebster-Data-Storage/infinite-data-vector-shaders.py` | distinct: limbs, GPU path, orbit cache |
| [06](06_v05_hypergallery_images_and_master_index.md) | v05 | 04-18 | `HyperWebster-Data-Storage/hypergallery.py` | distinct: images, JWST search (defective), master index |
| [07](07_v06_character_manifold_and_vocabulary.md) | v06 | 04-18 | `HyperWebster-Data-Storage/hyperwebster_manifold.py` | distinct: multiset view; exact form in notebook 03 |
| [08](08_v07_archimedes_dimensional_engine.md) | v07 | 04-18 | `HyperWebster-Data-Storage/hyperwebster_archimedes.py` | distinct: estimators; not used downstream |
| [09](09_v08_layer3_word_shards.md) | v08 | **04-24** | `Callimachus/hyperwebster_layer3.py` | deployed: word → file by address |
| [10](10_v09_callimachus_v09.md) | v09 | **05-02** | `Callimachus/v09/` | **design of record** (Unicode order, label key, SQLite) |
| [11](11_v10_kcf_charset_permutation_as_key.md) | v10 | **05-03** | `Kryptos/kcf.py` | distinct: charset as key; the N! index is not in the repo |
| [12](12_v11_semantic_ordinal.md) | v11 | **05-12** | `SemanticWordEngine/hyperwebster.py` | distinct: many-to-one, anagram-invariant |
| [13](13_v12_prime_zero_index.md) | v12 | **05-19** | `VAPMIP/monad.py` | successful: lossy spelling address |
| [14](14_v13_tn_firing_signature.md) | v13 | **06-14** | `VAPMIP/engines/e17_hyperindexing.py` | distinct: address is a permutation (argsort) |
| [15](15_v14_valaquenta_module.md) | v14 | **06-28** | `ValaQuenta/modules/hyperwebster/` | successful: packaged v00 |
| [16](16_v15_vigenere_model.md) | v15 | **08-25** | `Kryptos/Ciphers/Vigenere.py`, `Kryptos/analysis.py` | the model; rotations, breaking tools |
| [17](17_v16_debruijn_octonion_fold.md) | v16 | **08-30** | branch `data-storage-no-location` | sibling paper: fixed 64-bit fold, de Bruijn traversal |
| [18](18_v17_layered_calendrical_index.md) | v17 | **09-25** | `VAPMIP/benchmarks/hyperwebster_baseline_bench.py` + audit | the claim of this paper, measured |
| [19](19_v18_blackjack_subgroup_f21.md) | v18 | **09-25** | `VAPMIP/benchmarks/blackjack_vs_horner_bench.py` | negative result, recorded |
| [20](20_v19_midline_index.md) | v19 | **09-27** (rules rev. 10-12) | `Archimedes/Maths/MidlineIndex.py` | distinct: 4-digit T S DD code, base-96, de Bruijn generator |

## Synthesis

| Page | Notebook | Content |
|------|----------|---------|
| [21](21_s1_taxonomy_of_kinds.md) | `w01_taxonomy/` | every kind, one input set: collisions on 18,278 words, size on 1,000 characters |
| [22](22_s2_permutation_structure.md) | `w02_permutation_structure/` | rank = permutation rank; transposition offset; charset order = digit relabelling; multinomial count |
| [23](23_s3_babel_scale.md) | `w03_babel_scale/` | the Library of Babel numbers recomputed; a page's location; one book |

## Paper draft

The opening sections are drafted in [`../paper/00_sections_1_to_4_draft.md`](../paper/00_sections_1_to_4_draft.md) (Babel recipe → ordered address → definition of a hyperindex), with Listings in `../paper/listings/` (single source: the notebooks in `notebooks/p01_babel_to_ordered/` and the draft use the same text), `../paper/test_listings.py` and `../paper/test_transcripts.py` (every `>` transcript in the draft re-run in a fresh namespace).

## Behaviour under permutation of the string

The axis this paper reads every version along:

| Version | Address under a permutation of the string's positions | Under a permutation of the charset |
|---|---|---|
| v00, v14 | order-sensitive; length stored; many strings share the Fano index | order changes the integer |
| v01, v02, v03, v08, v09 | bijective (shortlex rank); transposition = closed-form offset | relabelling of the digits |
| v04 | as v02; the orbit is named and cached as an exact string, no offset computed | as v02 |
| v06 | multiset view: (count vector, rank among arrangements) is the exact form | as v02 |
| v07 | boundary filter constant on each anagram class; SVD order-sensitive | — |
| v10 | — | the charset order is the key (monoalphabetic substitution, v15) |
| v11 | **constant on every anagram class** (Σ ord) | — |
| v12 | order-sensitive, then many-to-one | — |
| v13 | the address is itself a permutation (argsort); many-to-one | — |
| v15 | position-dependent rotation (Vigenère); sorted rotations (BWT) | — |
| v16, v19 | de Bruijn traversal: each window once, neighbours by a one-symbol shift | — |

## Open items

- Path forward, not built: hyperindexing of the Emmy Noether Sedenion (𝕊_EN, the 16-dimensional Cayley–Dickson algebra, `Ainulindale/wiki/43`). Present code touching it: v16 rung 4 (𝕊, dimension 16: fixed 64-bit address, 3.0 s forward on the 3,360-byte document) and v05's fixed-length vector address.
- Speed: `point_to_text` (v02) grows as about n^2.5; a forward Horner loop returns the identical address at n^1.8 (page 03). Every timing in pages 03, 18 and 23 that used `point_to_text` is an upper bound.
- v16's fold runs from a local, unpushed branch; the notebook reads it with `git show` and stops working if the branch is renamed.
- v15 notebook 02's pattern test takes word boundaries from the plaintext.
- The exact (count vector, rank) address (v06 notebook 03) and the `rank1`/`unrank1` charset key (v10 notebook 02) are written in the notebooks, not in the engine home named by the paper stub (`ValaQuenta/modules/hyperwebster/`).
