# gemini/ — usage

Skeleton instance of the ContextPlease scheme. **Read
`../README.md` first** — it carries the Prime Directives, the environment
traps, and the writing conventions. This file only covers what is specific to
using this directory.

## Status

| File | Format | State |
|---|---|---|
| `.geminirc` | bash | **usable** — root, 3 repo paths, helpers, environment facts |
| `.geminirc_ValaQuenta` | bash | skeleton — index empty, `ctxengine` works |
| `.geminirc_memory` | prose | **usable** — directives, git hygiene, feedback log |
| `.geminirc_canonical_maths` | prose | **stub — copy from `../claude/`, do not paraphrase** |
| `.geminirc_context_1` | prose | deliberately empty |
| `.geminirc_context_2` | prose | deliberately empty |
| `.geminirc_file_structure` | JSON | not generated yet |

## Load it

```bash
source /storage/emulated/0/ThePlace/ContextPlease/gemini/.geminirc
source /storage/emulated/0/ThePlace/ContextPlease/gemini/.geminirc_ValaQuenta
```

Those two only. Never `source .geminirc*` — the glob would catch
`.geminirc_file_structure`, which is JSON and would execute as commands.
Note that `bash -n` will *not* protect you here: an all-comment prose file
passes it, and a populated one fails it. Parseability says nothing about
whether a file should be sourced. Use the names.

Then:

```bash
cdrepo vapmiP              # jump to a repo (case-insensitive)
ctxdir VAPMIP              # one repo's current-state entry
ctxengine _crosscutting    # read this first, once the index is populated
```

## First-run checklist

1. `cp ../claude/.clauderc_canonical_maths ./.geminirc_canonical_maths`
   — verbatim. The mathematics is not per-agent and a paraphrase introduces
   notation drift, which has caused real errors here.
2. Fill in the remaining repo paths in `.geminirc` from
   `../claude/.clauderc`. Paths are stable and shared; **URLs must stay
   clean** — several local git remotes have plaintext PATs in them.
3. Generate the structure snapshot when you need it:
   ```bash
   tree -J -I '.git' "$THEPLACE" > .geminirc_file_structure
   ```
4. Survey `ValaQuenta/modules/` yourself and populate
   `VALAQUENTA_ENGINE_INDEX`. Do **not** copy the claude index — it records
   what that agent verified, and some of its entries name modules that are
   absent from this working copy.
5. Leave `context_1` and `context_2` empty until you have verified something
   yourself.

## Why the two context files are empty

Not an oversight. Context here is earned by running things, not inherited.
Copying another agent's conclusions means copying its mistakes with no way to
tell which are which — and this project has a documented history of claims
that were confidently recorded, drifted, and turned out false when someone
finally measured them.

Write `context_1` when you know the current state of a repo. Append to
`context_2` when a session establishes something. Both want the diagnosis of
failures, not just the successes — see Directive #2.
