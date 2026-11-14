# gemini/ — usage

Instance of the ContextPlease scheme for Gemini / Antigravity CLI.
**Read `../README.md` first** — it carries the Prime Directives, environment traps,
and writing conventions. This file covers what is specific to `gemini/`.

## File Index

| File | Format | State | Purpose |
|---|---|---|---|
| `.geminirc` | **bash** | **active** | Project root (`/home/rendier/Projects/ThePlace`), repo paths, helper functions (`gpush`, `rstatus`, `canon`, `vale`, `psearch`…), canonical constants |
| `.geminirc_memory` | prose | **active** | Standing directives (#1 No renormalization, #2 All failures stay in code/data), git/credential rules, persistent scratchpad rules |
| `.geminirc_canonical_maths` | prose | **authoritative** | Authoritative equations and notation — **start any derivation here** (synced verbatim from `.clauderc_canonical_maths`) |
| `.geminirc_ValaQuenta` | **bash** | **active** | Engine index (`ctxengine <module>`), history tier pairing with canonical maths |
| `.geminirc_valaquenta_engines`| symlink | **active** | Symlink to `.geminirc_ValaQuenta` for naming compatibility |
| `.geminirc_ctx` | **bash** | **active** | Lookup helpers: `rcgm` (canonical maths block), `rcvq` (ValaQuenta history), `rcboth`, `rcls`, `rctree`, `rcrepos` |
| `.geminirc_context_1` | prose | **active** | One *current-state* entry per repository, keyed `## RepoName` |
| `.geminirc_context_2` | prose | **active** | **Append-only** dated log; what happened, in chronological order |
| `.geminirc_context` | prose | **active** | Coarse chronological through-line (newest entry first) |
| `.geminirc_context_hub` | **bash** | **active** | Hand-maintained policy and repository map (`THEPLACE_REPOS`) |
| `.geminirc_citations` | prose | **active** | Live queue of published work formalizing independently engineered concepts |
| `.geminirc_user_provenance` | prose | **active** | Cody Michael Allison's original work vs established prior art |
| `.geminirc_official_names` | prose | **active** | Canonical names ("The Boundary", "The Stability", "The Flow", "The Translator") |
| `.geminirc_licenses` | prose | **active** | Licensing policy per codebase and third-party dependency |
| `.geminirc_scratchpad_contents` | prose | **active** | File manifest of `scratchpad/` |
| `ATLAS_REGISTRY.md` | prose | **active** | Quick reference table of key concepts, files, and locations |
| `scratchpad/` | directory | **active** | Persistent scratchpad storage (never `/tmp`) |
| `skills/` | directory | **active** | Custom skills (addition-matrix, cs-paper-code-conventions, generational-lineage…) |

## Sourcing

To load into a shell session:

```bash
source /home/rendier/Projects/ThePlace/ContextPlease/gemini/.geminirc
```

Only `.geminirc` (which sources `.geminirc_ctx`) and `.geminirc_ValaQuenta` are bash.
Never `source .geminirc*` via glob — `.geminirc_file_structure` is JSON.

## Quick Lookup Helpers

```bash
rcgm FANO_SEDENION        # print canonical equations for block
rcvq FANO_SEDENION        # print historical context and open leads
rcboth FANO_SEDENION      # print both reference and history
rcls                      # list all available RCCM and RCVQ blocks
canon                     # print key canonical constants
rstatus                   # sweep git status across all 20+ project repos
ctxdir Ainulindale        # print current-state context for one repo
scratch my_check          # create & cd to dated persistent scratchpad dir
```

## Persistent Scratchpad Rule

The AI harness scratchpad is shimmed to:
`/home/rendier/Projects/ThePlace/ContextPlease/gemini/scratchpad/YYYY-MM-DD_<topic>/`
All temporary scripts, checks, and calculations must be preserved here with a `README.md`.
Never rely on `/tmp` (wiped on reboot).
