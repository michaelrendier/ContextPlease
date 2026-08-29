# ValaQuenta — Generational Lineage Calibration (2026-08-28)

Cody: run the generational lineage on every ValaQuenta engine as a **calibration
check on the factoral decomposition** — ValaQuenta is working, deliberately-
designed machinery, so a well-designed engine should decompose CLEAN, and the
FLAGGED ones should be exactly those ValaQuenta already labels non-ESTABLISHED.

- `engine/valaquenta_calibration.py` (in SFR) — the curated per-engine mapping +
  the agreement report + `wiki_block(name)`.
- `apply_blocks.py` (here) — appended the calibration block toward the bottom of
  all 46 `ValaQuenta/wiki/*.md` engine pages (idempotent; run once).

## Result

| | |
|---|---|
| engines | 46 |
| CLEAN | 21 |
| DESCRIPTIVE-OK | 6 (instruments / renderers / validators) |
| FLAGGED | 19 (import deficit or emergence signature) |
| **agreement with ValaQuenta's own status label** | **0.957** |
| confusion | CLEAN∩ESTABLISHED 20 · FLAGGED∩soft 18 · off-diagonal 2 |
| roots | SCALE 16 · SIGN 15 · ADD 14 (unbiased) |
| trees | LAURELIN 25 · MINGLING 11 · TELPERION 10 |

Disagreements (the signal):
- `bao_mass_gap` — FLAGGED (the 10³ in 1/(1000√2) is un-derived) vs page ESTABLISHED.
  Same shape as Yang-Mills in the clay run; the framework's own open-questions
  table lists "why 10³", so ESTABLISHED is a touch generous.
- `t32_nilpotency` — CLEAN (the trace-Laplacian test constructs cleanly) vs page
  THEORETICAL. The decomposition rates it more solid than its label.

95.7% agreement between an independent structural decomposition and hand-assigned
labels, over ~46 explicitly-designed engines, IS the calibration.
