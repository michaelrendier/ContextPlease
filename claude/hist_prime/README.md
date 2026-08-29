# hist_prime — the centralised context-primer store

**Created 2026-08-28.** Every context/session primer that was loose in a
`ThePlace` repo has been **moved** here, organised by originating repo (the
top-level `ThePlace` directory it pertains to; `_root` for none). `PTOLEMY_DOCS/`
was moved wholesale and the original directory deleted. Nothing was left behind
outside `ContextPlease`.

`git history` in each source repo preserves the pre-move lineage — chain of
custody is not tracked here (by design).

## Layout

    hist_prime/<OriginatingRepo>/<original-subpath-within-that-repo>

e.g. `Ainulindale/outreach/primers/PRIMER_2026-05-03_four_phases.txt`,
`VAPMIP/CONTEXT_PRIMER_2026-08-27_CONSTRUCTOR_BOXKITE_SEMANTIC_HASH.txt`,
`PTOLEMY_DOCS/016_5thread_model.txt`.

## Index

`MANIFEST.json` — full tree: per-repo file lists with size and extension, and
totals. Regenerate after adding files.

Current totals: **194 files** (174 `.txt`, 19 `.md`, 1 other), ~1.5 MB, across
13 repo buckets — Ainulindale (30), PTOLEMY_DOCS (89), PtolemyDesktop (27),
phone_pull_2026-06-06 (21), VAPMIP (13), PDesktop (3), POE (2), PTorrent (2),
RiemannHypothesisProof (2), _root (2), ArdaQuenta (1), BulletCluster (1),
FourthAgePapers (1).

## Protocol (going forward)

Every context primer written from now on goes to
`hist_prime/<OriginatingRepo>/<subpath>` — never loose in a repo. Shell:
`histprime <Repo>` (defined in `~/.clauderc`). See `../hist_todo/` for the
snapshot copies of every repo's `TODO`.

## Next

These primers are staged as a corpus to ingest into the Monad's `.bin` file
(pending discussion).
