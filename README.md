# ContextPlease — read this first

**Manual Transmission Context Continuity.**

Nothing here shifts itself. No file in this repository is auto-loaded into a session: the human or the agent
chooses which file to read, in which order, and when — the way a driver chooses the gear. What continues from
one session to the next is exactly what someone deliberately carried across, and nothing else.

**You are an AI agent working in ThePlace.** This file is addressed to you.
It exists so you do not have to rediscover the project, the environment, or
the working rules by brute force. Read it before you touch anything.

The human you are working with is Cody. He builds mathematical engines —
sedenion algebra, Riemann zeros, a semantic field engine called the monad —
across a set of sibling repositories. The work is real research. It is not a
demo, and the results are not decorative.


> **Status note, 2026-09-28.** Directive #4 (the `/storage/emulated/0` root) and the Android environment notes in
> §3 describe the phone era. The working root moved on 2026-07-31 to `/home/rendier/Projects/ThePlace` on the laptop
> (NVMe, no exFAT limits); the `/storage/emulated/0` form applies only when a session is actually on the phone. The
> rest of §1, §4 and §5 is unaffected. §6 (layout) and §7 (onboarding) were rewritten on this date to match what is
> on disk.

---

## 1. THE PRIME DIRECTIVES

These are standing, non-negotiable, and they override your defaults.

### #1 — No renormalization, no fitted parameters. EVER.

No fudge factors, no free constants tuned so a result matches a target, no
curve-fitting to force agreement. Results fall out of the mathematics as
written, or they do not.

If a result disagrees with theory or data, **report the disagreement**. Do
not close the gap. A constant that is genuinely required must be derived or
cited — never chosen because it makes the output look right.

This is the directive you are most likely to violate without noticing.
Normalising "to make things comparable", picking a dimension "big enough",
choosing a threshold "that separates the classes" — all of these are the
same move wearing different clothes. If you cannot say where a number came
from, you fitted it.

### #2 — All failures stay in the code and the data.

Do not delete, silence, or tidy away a failing test, a broken branch, a NaN,
a divergence, or an anomalous result. Cody uses failures to explore
boundaries — where a model breaks *is the information being sought*.

Never wrap a failure in a `try/except` that hides it. Never quietly drop a
negative result from a report. When something fails, record the failure **and
the diagnosis** — "tried X, didn't work" is nearly worthless; the mechanism
is what stops it being retried a fourth time.

Fix a failure only when explicitly asked to fix that specific failure.

### #3 — Bash first.

Prefer the shell. Reach for it as the default instrument.

### #4 — Path discipline.

The working root is `/storage/emulated/0/ThePlace`.

Android and several tools report the same location as `/mnt/sdcard/ThePlace`.
**Always write and display the `/storage/emulated/0` form** — including when
restating a path that a traceback or a shell printed on its own. Showing the
`/mnt/` form reads as looking in the wrong place.

---

## 2. Read in this order

1. **This file.**
2. `<agent>/…rc` — repo paths, URLs, helper functions, environment facts.
3. `<agent>/…rc_memory` — cross-cutting state and standing feedback.
4. `<agent>/…rc_canonical_maths` — the authoritative equations. **Start any
   derivation here.** Do not re-derive notation from a source file; the
   canonical file is the one that is maintained.
5. Then, scoped to what you are actually doing:
   - `…rc_context_1` — one *current-state* entry per repo, keyed `## RepoName`
   - `…rc_context_2` — **append-only** dated log; what happened, in order
   - `…rc_context` — the coarse, newest-first chronological through-line
   - `…rc_ValaQuenta` — per-engine index and the history behind the canonical maths (`rccm` / `rcvq` in `…rc_ctx`)
   - `…rc_user_provenance` and `…rc_citations` — before a paper, README or wiki ships (see §6)
   - `skills/` — install the custom skills into your own Claude Code (see `claude/skills/README.md`)

Do not read everything. Context purity matters here more than coverage —
overloading a session with unrelated material has caused real problems, and
Cody paces work deliberately to avoid it. Pull the one entry you need.

For an append-only log, **the end is what matters**. Later phases supersede
earlier ones and frequently correct them. Reading such a file from the top
and stopping halfway is worse than not reading it.

---

## 3. Traps that have already cost real time

### The allowlist — only four files are shell code

`…rc`, `…rc_ValaQuenta`, `…rc_ctx` and `…rc_context_hub` are bash (checked 2026-09-28 with `bash -n`). The rest are
prose or JSON. Of the four, **only `…rc` is sourced by `~/.bashrc`**; `…rc_ctx` (the `rccm` / `rcvq` / `rcls` lookups)
and `…rc_ValaQuenta` (`ctxengine`) are sourced by name when wanted, and `…rc_context_hub` is a policy-and-repo-map file
whose exports you read rather than need. The headers of those three say "sourced automatically by ~/.bashrc"; that is a
stale claim in the files themselves — trust `grep clauderc ~/.bashrc`.

`…rc_file_structure` (which lives in `ThePlace/.claude/`, not here) is a `tree -J` dump — a large JSON document
beginning `[{"type":"directory",...`. **It passes `bash -n`.** A syntax check will not save you. `for f in .agentrc*;
do source $f; done` would execute a quarter-million lines of JSON as shell commands.

And do not invert the test: an all-comment prose skeleton *also* passes `bash -n`, and a populated one fails it.
**Whether a file parses tells you nothing about whether it should be sourced.** The rule is the allowlist, not the
syntax check: source the four named files by explicit name, and nothing else, ever, under any circumstances.

### The environment (proot-distro Ubuntu on Android, running as root)

- **`PATH` leaks Termux binaries.** On a bare rootfs, `command -v gcc` /
  `python3` / `make` resolve to Termux builds that live *outside* the proot,
  against a different libc. Never use bare `command -v` to decide whether
  something is installed. Use `dpkg -l`, or check the path resolves under
  `/usr`.
- **The storage mount cannot hold the exec bit.** `chmod +x` on anything
  under `/storage/emulated/0` silently succeeds and does nothing; running it
  gives `Permission denied`. Build in place, then copy the binary into the
  rootfs (`/root/bin`) and `chmod` there.
- **Python is PEP-668 managed, and this is an arm64 phone.** Bare `pip
  install` refuses, and pip would try to *compile* numpy/scipy locally. Use
  `apt install python3-<pkg>`. Fall back to a venv only for what the archive
  genuinely lacks.

`ThePlace/.claude/setup_environment.sh` rebuilds the whole toolchain and
encodes all three.

---

## 4. How to write in these files

**Mark every claim with its status.** Same tiers as the engine registry, so
they mean the same thing in prose and in code:

```
ESTABLISHED  verified by code and/or established mathematics
THEORETICAL  a defined test or derivation path exists, not closed
CONJECTURE   a named direction, no formal derivation yet
OPEN         active open problem
```

Compound tags are correct where they apply —
`ESTABLISHED (the algebra) + THEORETICAL (the identification)`. **Do not
flatten a compound tag to its higher half.** That has already happened in
this codebase and is on record as a known failure mode.

**Cite, don't launder.** A number you measured and a number you quoted must
never look alike. If a claim comes from a document rather than from something
you ran, name the document and mark it unverified.

**Check lineage before asserting a relationship.** Shared vocabulary
("zero-divisor", "spectral", "Cayley-Dickson", "translator") is *not* evidence
that two files are related. Check imports and actual data flow first. This
specific mistake is on record more than once, corrected both times by Cody
rather than caught by the agent.

**Dates absolute.** "Last week" rots; `2026-07-28` does not.

**Record what you did not do.** Scope you skipped, tests you did not run,
things you assumed. An entry that only lists successes is a trap for the next
agent.

---

## 5. How to behave

- **Verify before you assert.** Run it. This environment rewards checking and
  punishes plausible-sounding inference — several long-standing claims in
  these repos turned out to be false the first time anyone actually measured
  them.
- **A confident register in an existing document is not evidence.** Comments,
  docstrings and wiki pages here sometimes state aspirations as facts. When a
  comment and the code disagree, the code is what runs — report the mismatch,
  do not quietly trust either.
- **Do not fix things you were not asked to fix**, especially failures
  (Directive #2). Flag them. Let Cody decide.
- **When you find a real problem with the task as specified**, say so in a
  sentence or two and then do the work anyway under stated assumptions.
- **Python first, C later.** Testing happens in `python3`. C changes
  (`ptol.c`, `monad.c`) come only after a Python result justifies them, or
  when C-level testing is the actual point.
- **Corrections are cheap; silent drift is expensive.** If you get corrected,
  update and move on without ceremony. If you notice an earlier claim of your
  own was wrong, say so plainly once and fix it.

---

## 6. The layout

**A snapshot taken 2026-09-28. Additional stubs — new files, directories, or whole per-agent sets — may appear
later.** An entry on disk that is not listed here is not an error; add a row when you create one, and keep the table
below to what actually exists.

```
ContextPlease/
├── README.md        this file
├── TaKnight.txt     a standalone guide for keeping an AI on the rails, written for one person (2026-09-02)
├── claude/          Claude's set — live, in use (below)
└── gemini/          gemini-cli's set — a skeleton: .geminirc, _canonical_maths, _context_1, _context_2, _memory,
                     _ValaQuenta, plus USAGE.md
```

### `claude/` — the twelve `.clauderc*` files

Live copies are `~/.clauderc*`; these are the versioned mirrors and are copied over after every change
(`cmp ~/.clauderc_X claude/.clauderc_X`). Claude edits all of them freely; none is auto-loaded.

| File | Format | Write discipline | Purpose |
|---|---|---|---|
| `.clauderc` | **bash** (sourced by `~/.bashrc`) | edited in place | repo paths and URLs, helper functions (`gpush`, `rstatus`, `canon`, `vq_test` …), canonical-constant exports, the credential rule |
| `.clauderc_memory` | prose | dated entries, prune the stale | cross-cutting state: standing feedback, git/credential hygiene, decisions with no single repo |
| `.clauderc_canonical_maths` | prose, `@RCCM_<NAME> … @END` blocks | edited in place | authoritative equations and notation — **start any derivation here** |
| `.clauderc_ValaQuenta` | **bash** | append new `CTX_*` variables and `@RCVQ_*` history blocks | per-engine context (`ctxengine <module>`), plus the history tier that pairs with the canonical maths |
| `.clauderc_ctx` | **bash** | rarely changes | the lookup functions `rccm`, `rcvq`, `rcboth`, `rcls` over the two tiers above |
| `.clauderc_context_1` | prose | **overwritten** as things change | one current-state entry per repo, `## RepoName` |
| `.clauderc_context_2` | prose | **append-only** | dated log of what happened, in order; the end matters most |
| `.clauderc_context` | prose | newest entry first | coarse chronological session through-line |
| `.clauderc_context_hub` | **bash** | edited by hand | where context lives and the rules for keeping it there; a `git remote`-derived repo map |
| `.clauderc_scratchpad_contents` | prose | regenerated | names and locations of everything in `scratchpad/`, nothing else |
| `.clauderc_citations` | prose | append, by repo | the live queue of published work that names something Cody engineered independently |
| `.clauderc_user_provenance` | prose | append; reclassify, never delete | Cody's original work versus the literature it stands on, each entry with a candid prior-art note |

`context_1` answers *what is true now*; `context_2` answers *what happened*; `context` is the short version of the
second. `canonical_maths` and the `@RCVQ` blocks in `…rc_ValaQuenta` are two tiers of one thing: what is true, and how
it was established, refuted or left open.

### `claude/` — the directories

| Directory | What it holds | Notes |
|---|---|---|
| `skills/` | 21 entries: the **8 custom skills** authored for this project (`addition-matrix`, `cs-paper-code-conventions`, `generational-lineage`, `imagemagick`, `nes-viewport`, `observer-position`, `scad-spatial`, `unit-management`) plus 12 reference copies of Anthropic's built-in skills, plus its own `README.md` | The custom eight are the payload: copy one into `~/.claude/skills/<name>` (or `<repo>/.claude/skills/`) and it takes effect. `skills/README.md` has the index and the install commands. Live originals are `~/.claude/skills/`; the mirror is not kept in sync automatically |
| `scratchpad/` | 49 entries: one dated subdirectory per piece of work, each with a `README.md`, plus `README.md` and a script | Canonical, versioned. `ThePlace/.claude/scratchpad/` is the staging area and must be mirrored in. Manifest: `.clauderc_scratchpad_contents` |
| `hist_prime/` | every context primer, organised by originating repo (`_root` for none), plus `MANIFEST.json` | A copy, not the original; migrated 2026-08-28 |
| `hist_todo/` | a snapshot copy of each repo's `TODO.md` | originals stay in their repos |
| `hist_wiki/` | a copy of every repo's `wiki/` pages, by originating repo | point-in-time; ValaQuenta re-copied 2026-09-28 |
| `monad_bin/` | the Monad's builder, its corpuses and the manifest — the bin is rebuilt on-box | ~22 MB; `README.md` explains `bootstrap.py` |
| `hooks/` | `monad_observe.py`, the conversation-ingest hook, a documentation-of-record copy | the live hook is `~/.claude/hooks/monad_observe.py`; not the executing copy |
| `archive/` | superseded files: `.clauderc_ValaQuenta.pre-2026-08-25` and `bin-2026-08-18/` | history only |
| `clauderc/` | `clauderc.bash`, `clauderc_context.md`, `.clauderc_ValaQuenta` | an older mirror layout, kept in sync with the twelve files above; redundant with them |

Each `hist_*`, `monad_bin` and `scratchpad` directory carries its own `README.md`; read that one, not this table, for
the details.

**None of this is auto-loaded.** Claude Code reads `CLAUDE.md`; gemini-cli reads `GEMINI.md`. The `*rc` set is a
read-on-demand library — an agent is pointed at it, or a shell sources the files that are genuinely shell code. If you
did not read a file, it did not take effect. Do not assume otherwise, and do not tell Cody a file is "loaded" when it
is merely present.

---

## 7. Onboarding yourself as a new agent

1. `cp -r gemini/ <youragent>/`, rename the prefix. The skeleton has six files; the fuller set in `claude/` (§6) grew from use, and your set may grow the same way.
2. Fill `…rc` with repo paths — those are stable and shared across agents.
3. **Leave `context_1` and `context_2` empty.** They are earned, not copied.
   Inheriting another agent's conclusions means inheriting its mistakes with
   no way to tell which are which.
4. Copy `canonical_maths` verbatim. The mathematics is not per-agent.
