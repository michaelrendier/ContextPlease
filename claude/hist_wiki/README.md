# hist_wiki — every repo's wiki, one place

**Created 2026-08-29.** A **copy** of every `wiki/` page across every ThePlace
repo (originals stay live), organised by originating repo — same layout as
`../hist_prime/` and `../hist_todo/`.

    hist_wiki/<OriginatingRepo>/<original-subpath>      e.g.
      Ainulindale/wiki/107_add_scale_sign_datatype.md
      ValaQuenta/wiki/three_ring_scale.md
      VAPMIP/docs/wiki/Tuning-the-Engine/34_the_anomaly...md

**357 pages** — Ainulindale 190, PtolemyDesktop 56, ValaQuenta 51, VAPMIP 47,
PTorrent 7, SedenionFactoralRelativity 3, + DeriveCancerDrugs / FourthAgePapers
/ TuringStack 1 each. `.md` / `.html` / `.txt`. Point-in-time snapshot; re-copy
for a fresh one.

## Why it's here

The **"fresh context" bundle** for building a specified Monad version has four
parts, and this is one of them:

| part | where | perspective |
|---|---|---|
| the **maths** (canonical notation, constants, the fold) | `~/.clauderc*` (`_canonical_maths`, `_context*`, `_user_provenance`) | the reference |
| the **concepts** (every engine, every result, every derivation) | **`hist_wiki/`** | the wiki view |
| the **narrative** (how it was built, session by session) | `hist_prime/` | the journey |
| the **inside view** (what only the running code knows) | the repos' source | "above and inside never confused a computer" |

A Monad built from all four speaks the project's own language literally. The
`monad_bin/` builder (`../monad_bin/`, and `VAPMIP/monad_bin/`) turns the prose
parts into the `.bin` vocabulary + knowledge store.
