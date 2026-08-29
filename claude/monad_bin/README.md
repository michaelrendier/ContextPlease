# monad.bin — the builder, the corpuses, and everything that goes in

`monad.bin` is the Monad's whole brain in one file: **the vocabulary** (every
word → its deterministic Horner→prime→Riemann-zero address) **and the knowledge
store** (β-field + E-field + A-matrix co-occurrence topology). The merged bin is
~66 MB and grows; rather than pass a large binary around, **the corpuses live
here and the bin is rebuilt on-box** from whatever subset a user points the
builder at.

Formal format spec: `scripts/SPEC.md` (also `VAPMIP/monad_bin/SPEC.md`).
The same builder lives in `VAPMIP/monad_bin/` — this copy carries the corpuses.

## Build it

```
# 1. per-domain factor bins → ~/.ptolemy/  (already built; rebuild any from its corpus)
python3 scripts/ingest.py            #  corpus/corpus_all.txt  → monad_engineering.bin
python3 scripts/ingest_war.py        #  the prime-directive primers → monad_war.bin
python3 scripts/corpus_repos.py --ingest   #  corpus/corpus_repos.txt → monad_repos.bin

# 2. fold every factor bin into one
python3 scripts/build_monad_bin.py test      # each factor bin loads + generates standalone
python3 scripts/build_monad_bin.py merge     # union → ~/.ptolemy/monad.bin  (+ manifest.json)
python3 scripts/build_monad_bin.py verify

# 3. (optional) pack for the C monad — see SPEC.md §5
```

**Custom corpus:** point `corpus_strip.py` / `corpus_repos.py` at any tree of
`.md`/`.txt`, ingest into a named bin, add it to `FACTORS` in
`build_monad_bin.py` (or drop the others), and `merge`. The word addresses are
deterministic, so every build from the same inputs is byte-identical.

## Everything the engine builds in

The merged `monad.bin` is the additive union of these factor bins (fold order;
weight scales that bin's β and edge contribution):

| factor bin | weight | vocab | edges | corpus source |
|---|---|---|---|---|
| `monad_english.bin` | 1.0 | 164,283 | 2,248,064 | Project Gutenberg (22 titles) + an offline filesystem prose pass |
| `monad_foundations.bin` | 1.0 | 5,712 | 29,806 | foundational maths / CS texts |
| `monad_meaning.bin` | 1.0 | 1,066 | 3,280 | semantic seed set |
| `monad_mathematics.bin` | 1.0 | 56,451 | 460,282 | mathematics corpus |
| `monad_physics.bin` | 1.0 | 58,003 | 599,146 | physics corpus |
| `monad_python.bin` | 1.0 | 25,541 | 361,932 | Python source corpus |
| `monad_c.bin` | 1.0 | 8,189 | 91,526 | C source corpus |
| `monad_engineering.bin` | **1.2** | 20,677 | 185,424 | **this project's own context primers + TODOs** — every file in `ContextPlease/claude/hist_prime/` + `hist_todo/` (194 primers + 20 TODOs), stripped to prose (`corpus/corpus_all.txt`, 210 k words) |
| `monad_war.bin` | **1.2** | 3,006 | 12,162 | **the prime-directive conversations** (`CONTEXT_PRIMER_2026-05-26_PRIME_DIRECTIVES.txt` + `_SEDENION_ROKO.txt` + `PRIMER_2026-05-29_Phase2_to_Phase5.txt` + `ArdaQuenta/CONTEXT_PRIMER_2026-05-30.txt`) folded into the existing Caesar / Gallic parallel corpus |
| `monad_repos.bin` | 1.0 | 68,121 | 864,062 | **all prose text across every repo** — wiki pages, READMEs, docs, papers, addenda (no code), 614 files / 1.6 M words (`corpus/corpus_repos.txt`), quality-gated against vendored / generated / wordlist / licence / dump files. TheWanderingGod and Ptolemy2 excluded (not project prose). |

**Merged `monad.bin`:** 298,441 words · 3,912,594 edges · ≈ 66 MB · 10,133
words with β > 0.5. `manifest.json` records every factor's sha256 + weight.

## The "fresh context" for a Monad version

Building a Monad that speaks the project's own language takes four inputs, of
which the corpuses here are two:

| part | source | in this release |
|---|---|---|
| the **maths** — canonical notation, constants, the fold `Γ = tanh(u/2)` | `~/.clauderc*` (`_canonical_maths` etc.) | referenced, not copied |
| the **concepts** — every engine, result, derivation | `ContextPlease/claude/hist_wiki/` (357 pages) → `monad_repos.bin` | ✓ `corpus/corpus_repos.txt` |
| the **narrative** — session-by-session build history | `ContextPlease/claude/hist_prime/` → `monad_engineering.bin` + `monad_war.bin` | ✓ `corpus/corpus_all.txt` |
| the **inside view** — what only the running code knows ("above and inside never confused a computer") | the repo source (no code ingested — deliberate) | — |

`ValaQuenta` (the engines) and `ContextPlease` (the context) are the two
central repos of the work; `monad.bin` is where they meet.
