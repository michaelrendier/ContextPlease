# 2026-08-30 — Monad conversational + document ingest

Darts at the map for the "feed the Monad the live conversation" build. All
scripts spin a throwaway `ptolemy -d` under a fake `$HOME`, drive it, assert,
tear down. Kept as evidence per the testing-purpose rule.

| script | proves |
|---|---|
| `fifo_test.sh` | FIFO round-trip: hook → `monad.observe.fifo` → daemon drains concurrently; spool fallback fills then truncates to 0 |
| `owner_test.sh` | `monad3_c.writer.owner` gate — a live `ptolemy:<pid>` makes the daemon skip its self-flush; stale pid → proceeds |
| `repack_test.sh` | input-size repack timer: RC charge curve, `e^(-dt/TAU)` bleed exact, fires at knee `1−1/e`, `PTOL_REPACK_CMD` marker written, accum resets |
| `hook_chain_test.sh` | full chain: `monad_observe.py external/internal` → pair-id linked → daemon records `pairs.jsonl` + STATUS; thinking blocks verified NOT ingested |
| `doc_test.sh` | `monad_doc_commit.py` post-commit: `git show --root HEAD` → doc filter → `document` class → field; fenced maths stripped |
| `fold_test.sh` | `monad3c_fold_inplace()` against a real 48 MB `monad3_c.bin` copy: md5 changes, **size + MONAD3C magic intact**, `pending=0` for in-range words |
| `rt_run.sh` / `rt_client.py` | STATUS repack/pairs line shape under a burst |

Outcome: shipped. See
`ContextPlease/claude/hist_prime/VAPMIP/PRIMER_2026-08-30_MONAD_CONVERSATIONAL_INGEST.md`.
