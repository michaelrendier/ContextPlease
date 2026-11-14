# Gemini Scratchpad — Persistent

Established 2026-11-13 at Cody's directive.
Replaces any ephemeral `/tmp/...` scratchpad, which would be lost on reboot.

**Location:** `ContextPlease/gemini/scratchpad/` (versioned and pushed).

**Rationale (Cody's):** Side work — benchmarks, verification scripts, one-off numerical checks,
and explorations — carries archival value and supplies complete storytelling and mathematical provenance.
A result is worth far less when the script and environment that produced it are lost.

## Convention

One dated subdirectory per piece of work:

    YYYY-MM-DD_short_slug/
        README.md      what was asked, what was measured, what it means
        *.py *.c *.sh  the actual scripts, runnable as-is

The README is essential: it records the question, the method, and the result.

## Note for Gemini / Antigravity

Any harness-provided `/tmp/...` or internal scratch directory is shimmed to use
`$GEMINI_SCRATCH` (`ContextPlease/gemini/scratchpad/`).
Do not leave scratch scripts or numerical outputs in `/tmp`.

## Index

- `2026-11-13_initial_onboarding/` — Initial onboarding survey, repository structure validation,
  and harness scratchpad shimming.
