# ContextPlease — read this first

**You are an AI agent working in ThePlace.** This file is addressed to you.
It exists so you do not have to rediscover the project, the environment, or
the working rules by brute force. Read it before you touch anything.

The human you are working with is Cody. He builds mathematical engines —
sedenion algebra, Riemann zeros, a semantic field engine called the monad —
across a set of sibling repositories. The work is real research. It is not a
demo, and the results are not decorative.

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
   - `…rc_ValaQuenta` — per-engine index

Do not read everything. Context purity matters here more than coverage —
overloading a session with unrelated material has caused real problems, and
Cody paces work deliberately to avoid it. Pull the one entry you need.

For an append-only log, **the end is what matters**. Later phases supersede
earlier ones and frequently correct them. Reading such a file from the top
and stopping halfway is worse than not reading it.

---

## 3. Traps that have already cost real time

### The allowlist — only two files are shell code

`…rc` and `…rc_ValaQuenta` are bash. The rest are not.

`…rc_file_structure` is a `tree -J` dump — a large JSON document beginning
`[{"type":"directory",...`. **It passes `bash -n`.** A syntax check will not
save you. `for f in .agentrc*; do source $f; done` would execute a
quarter-million lines of JSON as shell commands.

And do not invert the test: an all-comment prose skeleton *also* passes
`bash -n`, and a populated one fails it. **Whether a file parses tells you
nothing about whether it should be sourced.** The rule is the allowlist, not
the syntax check: source `…rc` and `…rc_ValaQuenta` by explicit name, and
nothing else, ever, under any circumstances.

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

```
ContextPlease/
├── README.md      this file
├── claude/        .clauderc*      live, in use
└── gemini/        .geminirc*      skeleton + USAGE.md
```

One directory per agent, same seven-file scheme under that agent's prefix:

| File | Format | Purpose |
|---|---|---|
| `…rc` | **bash** | repo paths/URLs, helpers, environment |
| `…rc_memory` | prose | cross-cutting state, standing feedback |
| `…rc_canonical_maths` | prose | authoritative equations and notation |
| `…rc_context_1` | prose | live, one current-state entry per repo |
| `…rc_context_2` | prose | **append-only** dated log |
| `…rc_ValaQuenta` | **bash** | per-engine index, one variable per module |
| `…rc_file_structure` | **JSON** | `tree -J -I '.git'` snapshot — never source |

`context_1` is overwritten as things change; `context_2` never is. One answers
*what is true now*, the other *what happened*.

**None of this is auto-loaded.** Claude Code reads `CLAUDE.md`; gemini-cli
reads `GEMINI.md`. The `*rc` set is a read-on-demand library — an agent is
pointed at it, or a shell sources the two files that are genuinely shell code.
If you did not read a file, it did not take effect. Do not assume otherwise,
and do not tell Cody a file is "loaded" when it is merely present.

---

## 7. Onboarding yourself as a new agent

1. `cp -r gemini/ <youragent>/`, rename the prefix.
2. Fill `…rc` with repo paths — those are stable and shared across agents.
3. **Leave `context_1` and `context_2` empty.** They are earned, not copied.
   Inheriting another agent's conclusions means inheriting its mistakes with
   no way to tell which are which.
4. Copy `canonical_maths` verbatim. The mathematics is not per-agent.
