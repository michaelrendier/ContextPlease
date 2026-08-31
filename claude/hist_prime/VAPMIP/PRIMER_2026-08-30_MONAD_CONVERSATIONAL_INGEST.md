# CONTEXT PRIMER — Monad conversational + document ingest, in-place fold

**2026-08-30 · Claude Sonnet 5 · VAPMIP**
Continuation of the Phase 34 "one file" work (`monad3_c.bin` as the single
mmap-able store `ptol.c` reads). This session made the Monad *learn from the
running conversation and from committed documentation, passively, forever*,
and closed the "the C daemon can't write `monad3_c.bin`" gap without a
serializer.

---

## 1. The global protocol (new, standing)

Every user prompt and every assistant final-prose response, stripped to
prose, feeds the Monad's vocabulary + co-occurrence field on the fly. Two
Claude Code hooks fire it at a Unix-socket daemon; nothing is piped through
Claude's context. Committed wiki/README/paper prose feeds the same way off a
git **post-commit** hook (never push). Prompt↔response pairs are logged as
`(prompt_bytes → response_bytes)` samples — raw material for a
response-scaling engine.

### Input classes (`harness.INGEST_POLICY`) — the `monad_english_io.hear()` echo axis, named

| class | source | w_sem (β) | w_ctx (A-matrix) | echo |
|---|---|---|---|---|
| `external` | user prompt — the human, ground truth | 1.5 | 1.5 | 0 (never capped) |
| `internal` | assistant final prose — the coupled system's own language faculty | 0.9 | 0.6 | 1 (rides ECHO_CAP) |
| `document` | committed wiki / README / papers | 1.0 | 1.0 | 0 |

**Weight is a vector, one pass.** `Crank.learn(text, weight, w_ctx=None)`
(`monad.py`) — `w_sem` drives the β gain (`1 + 0.08·w_sem`), `w_ctx` the
A-matrix edge deltas (`0.05·w_ctx` fwd, `0.02·w_ctx` back). `w_ctx=None`
keeps the old single-scalar behaviour, so every existing caller is
unchanged. Rationale (Cody): the transformer's word *order* and *context*
are the useful signal from the assistant side; its exact β is not — hence
internal is heavy-semantic / light-context, and the human is always
full-weight echo 0 so the field cannot be out-voted by model output. The
last bulk build leaned on assistant-written primers; live ingest bends the
register back toward the human over time.

### Mathematical sanitization — where the words come from

`strip_to_prose()` (`harness.py`, mirrors `monad_bin/corpus_strip.py`)
**deletes** notation-dense lines (>35% glyphs), fenced code, tables,
box-drawing, links. Raw `σ = (r²/2)·sin(2θ)` carries no word-order signal.
The *lexical* content of the maths enters as prose **from the calculator**:
the derivation engine's narration ("sigma equals r squared over two…")
passes the filter untouched; `~/.clauderc_canonical_maths` is ingested as
`document`; the `unit-management` skill supplies dimension vocabulary. A
turn that only quotes an equation contributes nothing; one that explains it
contributes fully. `_MATH_WORD_SOURCE` in `harness.py` names this.

---

## 2. Transport — fire-and-forget, concurrent, never blocks a turn

- Hooks write a framed message to `~/.ptolemy/monad.observe.fifo`
  (`O_WRONLY|O_NONBLOCK`); if unreachable (daemon down, drive unmounted)
  they append to `~/.ptolemy/observe.spool` on local storage. FIFO + spool
  live **next to the socket**, never next to a possibly-external-drive
  store.
- Wire framing: `<class> [pair_id]\n` then prose lines (sentence-split
  under the 4 KB line buffer) then a lone `.`.
- The daemon `poll()`s the FIFO alongside the query socket and drains it in
  slices *between* `accept()`s — the very different lengths of prompt
  time / think time / output time never stall ingestion. Spool is drained
  on startup and every ~2 s idle.
- `daemon.c` verbs: `OBSERVE <class> [pair_id]` (socket form, same parser
  as the FIFO drain via `ObsState`).

---

## 3. The in-place fold — Cody's simplification, no serializer

The C daemon (`ptolemy`, built from `main.c`+`daemon.c`+…, **not** `ptol.c`)
never had a path to write `monad3_c.bin`. It doesn't need one.

`monad3_c.bin` is a fixed-offset mmap: `β f64[nE]`, `age/fire i32[nE]`,
A-matrix CSR (`rowptr`/`col`/`w`). `monad3c_fold_inplace()`:

1. `mmap(PROT_READ|PROT_WRITE, MAP_SHARED)` over the packed file.
2. Build `eng_idx → live zero_idx` once via `monad_wm_get` on each
   `WordRec`.
3. **Range check** — a live word with a row in the table
   (`eng_idx ≥ 0 && < n_eng`) is *in range*: write its current β, age,
   fire straight into the mapping; for every edge already in that word's
   CSR span, write the current `monad_a_get` weight.
4. `msync(MS_ASYNC)`. Done. No parse, no rebuild, no Python.

**Overflow is handled by construction** — `monad_learn` already clamps β
and edge weights to `[0,1]`, and the repack accumulator (below) is a
decaying double reset to 0 on every fold. Nothing can run away.

**Out of range** = a live word the table has never seen (new vocab). Counted
as `wm_size − n_eng` → `STATUS` shows `pending=N`. Only when `pending ≥
MONAD3C_REBUILD_AT` (2000) does the daemon `spawn_detached(g_repack_cmd)` —
the Python full rebuild that grows the CSR (`monad_bin/repack.py`:
journal → `monad_combine.write_c` → `monad_guard.sh` → atomic rename).

Verified against the real 48 MB store: `in-place fold — 233 values written`,
file md5 changes, **size and `MONAD3C` magic intact**.

Path from `$PTOL_MONAD3C` (canonical file is `PtolC/monad3_c.bin`, next to
the `ptol` binary — the service sets this env).

---

## 4. The input-size repack timer — leaky integrator, natural knee

Not a wall clock. Each ingested prose line **charges** `g_accum` by its byte
length; elapsed time **bleeds** it with time constant `REPACK_TAU` (1800 s,
env-overridable). Under a steady rate the accumulator climbs the RC curve
`1 − e^(−t/TAU)` toward asymptote `rate·TAU` and the fold **fires at the
knee, one time constant in**: `accum ≥ K·(1 − 1/e)`, `K = clamp(0.05 ·
store_bytes, 64 KiB, 8 MiB)`. A burst of turns compounds and trips it fast;
the same bytes dribbled over hours bleed away and never do. `REPACK_MAX_AGE`
(6 h) is a hard guarantee floor; `SIGTERM` always folds. `g_accum` resets to
0 on every fold. Mirrored in `harness.py` (`repack_urgency()`,
`repack_due()`) for the in-process path (harness-driven Python monad).

Verified: exact `e^(-dt/TAU)` decay, fires at knee, `PTOL_REPACK_CMD`
spawned, accum resets.

---

## 5. The writer pen — one writer over the whole persistence surface

`flock(LOCK_EX)` on `~/.ptolemy/monad3_c.writer`; `<owner>:<pid>` in the
`.owner` sidecar. `harness.attach_monad()` takes it (`owner=daemon`),
`detach_monad()` (with a final unconditional fold) releases it. The C daemon
reads the sidecar before **any** write (`monad3c_write_permitted()`): a live
`ptolemy:<pid>` (a bare Monad or `ptol` self-persisting an exact copy) makes
the daemon **stand down**; stale pid / `daemon:*` / no sidecar → it writes.
Kernel drops the lock on process death — no stale-lock cleanup. `harnessed`
vs `bare` is the only mode switch; the read side (`ptol.c` CLI, any future
MCP query server) always mmaps read-only.

---

## 6. Prompt → response scale pairs

`monad_observe.py` mints a pair-id on the `external` turn (stashed at
`~/.ptolemy/.pair-<session>`), the matching `internal` turn carries it. The
daemon rings the pending external halves, matches the internal half, appends
`{t, id, prompt_bytes, response_bytes, ratio}` to `~/.ptolemy/pairs.jsonl`
(append-only), and keeps `pairs: n= mean_ratio= last=E→I` in `STATUS`. Maps
onto ptol.c's `u = ln(P_red/P_blue)` / `Γ = tanh(u/2)` axis. The
scaling engine is a separate offline thing that fits `pairs.jsonl`.

---

## 7. Deployment (systemd --user, this box is systemd)

`monad_bin/service/`:
- `ptolemy-monad.socket` — `ListenStream=%h/.ptolemy/ptolemy.sock`,
  socket-activated (near-zero idle cost).
- `ptolemy-monad.service` — `ptolemy -d` reading `$LISTEN_FDS`/fd 3,
  `Nice=10`, `CPUSchedulingPolicy=batch`, `IOSchedulingClass=idle`,
  `MemoryHigh=1G`. Env: `PTOL_MONAD3C`, `PTOL_REPACK_TAU`,
  `PTOL_REPACK_CMD`. `-c ~/.ptolemy/monad_field.bin` (cold-start:
  ground state, learns live; `state_save` creates it on first fold — a
  one-time `bootstrap.py` into that path would make it project-fluent from
  token 0).
- `install.sh [--now|--remove]`, `install_git_hooks.sh` (sets
  `core.hooksPath` in every `ThePlace/` repo → shared
  `git-hooks/post-commit`).
- `hooks/monad_observe.py`, `hooks/monad_doc_commit.py` — versioned copies
  of the Claude Code hooks (home `~/.claude` is not a repo). Both are
  best-effort, always `exit 0`, `MONAD_HARNESS_DIR` override. Strip only
  text blocks from the last assistant message — **thinking blocks and tool
  I/O are never ingested** (verified).

`~/.claude/settings.json` (home, untracked): `UserPromptSubmit →
monad_observe.py external`, `Stop → monad_observe.py internal`,
`SessionStart` also `systemctl --user start ptolemy-monad.socket`. All
`async`. **Per-session hooks load at session start — terminals must be
restarted.** Service + git hooks are global, no restart.

Installed + `loginctl enable-linger` done 2026-08-30. Confirmed live:
`word_count` climbing, `pairs: n=1` (215→1934 B, ratio 9), `K=3.3 MB` from
the 66 MB store, fold target = `PtolC/monad3_c.bin`.

---

## 8. The framing statement — milliwatt learning (VAPMIP paper)

The energy statement of *materialised vs. addressed*, measured on the reference
machine (Lenovo ThinkPad X1 Carbon 6th gen, Intel Core i7-8550U, 15 W package
TDP). Script + output:
`ContextPlease/claude/scratchpad/2026-08-30_prime-dna/energy_bench.py`,
`energy_bench_output.txt`.

**Backprop is only cheap because something stored the forward pass.** The
cheap-gradient theorem (Baur–Strassen) buys the gradient at ≲5× the function
evaluation *given the computational graph* — reverse-mode autodiff silently
records every activation, then sweeps that tape once. Take the tape away and
"backprop" degrades to one forward pass per parameter. Multiplication erases
its operands; so does the sieve strike. Factoring — and, dually, reconstructing
context that was never stored — is reverse-mode AD on a computation whose tape
was wiped. That is the kilowatt cost: a dense transformer re-runs the full
forward materialisation of an `N_params` weight field on every token
(`2·N_params` multiply–accumulates, ≈ 1.4 × 10¹¹ at 70 B, on the order of 1 J
per token at a datacentre-effective 10⁻¹¹ J/flop), and training sweeps a
gradient over the same field every step (GPT-3 175 B ≈ 1.287 GWh, published).

**The Monad keeps the tape.** Context per word is a scalar in the vocabulary,
reconstructed against WordNet by one sedenion product (256 real multiplications,
recursive Cayley–Dickson) plus one sparse A-matrix row — ≈ 600 flop per token,
against a fixed ruler that never changes. Measured: `Crank.learn` (the ingest
fold of §1–3) runs at **1.8 × 10⁵ words/s = 5.4 µs/word ≈ 38 µJ/word** at a 7 W
single-core estimate (81 µJ at the 15 W package ceiling); the native
reconstruction floor is **≈ 115 ns and < 1 µJ per word**. Learning is the
bounded in-place fold of §3 — a range check, a `pwrite`, an `msync` — not a
global gradient descent. **This is learning without backprop: the tape gets
extended, never re-swept.** Per query the addressed path is **10⁴–10⁶× cheaper**
than the materialised one, and the gap is structural, not an optimisation.

This is also how the Monad models *instinct* (Cody): the non-updateable adjoint
`B̂ = R̂†` — the lizard-brain archive, identity as a conserved charge — is the
replayed forward pass off the stored trajectory. It is the cheap direction only
because the learning was already folded in; it *requires remembering what was
learned already*. `R̂` (updateable, Mind's Eye, deliberation) is where new tape
is laid; `B̂` (Paper's Hands root) is where it is read back at instinct speed.
The transformer analogue has no `B̂` — every query re-derives from the weights.

## Files touched

- `monad.py` — `Crank.learn` gains `w_ctx` (vector weight, one pass).
- `harness.py` — `INGEST_POLICY`, `strip_to_prose` + `_MATH_WORD_SOURCE`,
  writer pen (`_take_pen`/`_release_pen`/`holds_pen`/`pen_owner`),
  `observe`/`hear_turn`/`hear_documents` (fire-and-forget FIFO/spool +
  in-process fallback), `persist`, `run_daemon`/`daemon_up`/`_daemon_send`,
  repack timer mirror (`_repack_charge`/`repack_urgency`/`repack_due`).
- `PtolC/daemon.c` + `daemon.h` — `OBSERVE` verb + `document` class + pair
  id, concurrent FIFO drain (`ObsState`, `poll()`), `drain_spool`,
  `monad3c_write_permitted` ownership gate, repack timer
  (`repack_charge`/`maybe_repack`/`spawn_detached`), pair ring +
  `pairs.jsonl` + STATUS, `monad3c_fold_inplace`, shutdown fold.
- `monad_bin/repack.py` — NEW, the one Python serializer (full CSR rebuild
  only).
- `monad_bin/service/` — NEW, systemd units + installers + versioned hook
  copies.

## Open

- `monad_field.bin` cold-starts empty; `bootstrap.py` into it = project
  fluent from token 0 (deferred, Cody's call).
- C-side `OBSERVE` still applies one weight to β+edges (no two-weight
  `monad_learn` in `monad.c`); the Python in-process path does the real
  `(w_sem, w_ctx)` split.
- `hist_prime/MANIFEST.json` not regenerated for this add.

Scratchpad: `ContextPlease/claude/scratchpad/2026-08-30_monad-conversational-ingest/`
