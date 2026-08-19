# Claude scratchpad — persistent

Established 2026-08-08 at Cody's request. Replaces the ephemeral
`/tmp/claude-1000/...` scratchpad, which was lost on every reboot.

**Moved 2026-08-18** from `ThePlace/.claude/scratchpad/` to here. `ThePlace`
is not a git repository, so nothing under it was ever versioned or pushed —
this work is provenance and context, which is what ContextPlease is for.
Hardcoded absolute paths inside the archived scripts were repointed in the
same move; they are a known fragility, and new scripts should use
`$CLAUDE_SCRATCH` or paths relative to `__file__`.

**Rationale (Cody's):** the side work — benchmarks, verification scripts,
one-off numerical checks — carries archival value and supplies the *complete
storytelling* for the Ainulindale CS paper. A result is worth much less when
the script that produced it is gone.

## Convention

One dated subdirectory per piece of work:

    YYYY-MM-DD_short_slug/
        README.md      what was asked, what was measured, what it means
        *.py *.c       the actual scripts, runnable as-is

The README is the point. A directory of scripts with no README is a directory
of orphans six months later.

## Note for Claude

The harness hands you a `/tmp/claude-1000/...` scratchpad path at session
start. **Ignore it.** Use `$CLAUDE_SCRATCH` (set in `~/.clauderc` and mirrored
in `ContextPlease/claude/.clauderc`), which points here. Copy anything of value
out of `/tmp` before the session ends.

This directory is **versioned and pushed** with ContextPlease. Generated
artefacts are not: `*.bin`, `*.pyc`, `__pycache__/` and compiled check binaries
are gitignored, because anything regenerable by the script beside it should be
regenerated rather than stored.

## Index

- `2026-08-08_sedenion_igpu_benchmark/` — sedenion arithmetic throughput,
  CPU vs Intel UHD 620; also the det(L_q) = N(q)² result that corrected the
  UDEO landmark-collision diagnosis.
- `2026-08-08_residue_sieve_bounds/` — RSA residue/digit-window filters: exact
  bounds, all negative. Includes the Coppersmith threshold and the FIPS
  separation rule.
- `2026-08-08_bracketing_and_null/` — the bracketing test (alternativity is the
  wall, sedenion division 52% wrong) and the shuffled null, **including the
  retraction**: the module signal is lexical, not semantic.
- `2026-08-08_hyperwebster_wall/` — lossless address vs semantic neighbourhood
  proved incompatible; Hyperwebster compression ratio exactly 1.0000.
