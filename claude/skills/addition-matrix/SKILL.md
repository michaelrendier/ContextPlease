---
name: addition-matrix
description: >
  Methodology for exploring the addition-matrix space of two numbers'
  digit-by-digit multiplication — built from MultiplicationMatrixAnimator/
  (matrix_math.py, render.py, mapper.py, driver.py, curses_ui.py). Load
  before studying periodicity under single-digit incrementing, carry
  propagation structure, or any digit-cascade question Cody frames in
  colors rather than numbers — the tool and this skill are the training
  ground for the factoral decomposition / spectral recombination tool
  (GenerationalLineage), not a standalone toy. Load whenever Cody says
  "addition matrix," "the cascade," references row templates or the
  10x10 grid, or asks to study how a product's structure changes as one
  input increments.
---

# The Addition Matrix — periodicity under single-digit incrementing

Built 2026-09-22 from `MultiplicationMatrixAnimator/`, a working tool
before it was a skill — Cody's own framing: *"it's how i'm teaching you
how to build my factoral decomposition tool... a spectral factoral
decomposition / recombination tool."* Treat the tool's own findings as
load-bearing, not illustrative — they're the reason this skill exists.

## 1. The core structural fact — why this studies periodicity at all

Grade-school long multiplication of `num1 * num2` decomposes into
`N_DIGITS` rows, row `j = num1 * digit_j(num2)`, shifted by place value
`j`. **Fix `num1` and there are exactly 10 possible rows in existence** —
`num1*0` through `num1*9` — full stop. Incrementing `num2` can only
*reshuffle which of those ten fixed templates appears at which stagger
position*; it can never produce an eleventh. This is a hard consequence
of the arithmetic, not an empirical tendency — checked directly,
2026-09-22, across many `num2` values with `num1=1234567890` fixed: the
row for "multiplied by 6" is byte-for-byte `7407407340` every single
time, no exceptions.

**Consequence for periodicity studies:** all the interesting structure
under "single incrementing" of `num2` lives in *which row-template lands
where*, not in the templates themselves. To generate genuinely new
templates (not just a new arrangement of the same ten), the lever is
`num1`, not `num2` — the tool's `curses_ui.py` binds this to `Ctrl+N`.
Reaching for `num2` alone to find "more variation" is reaching for the
wrong control; recognized and corrected live, 2026-09-22 (Cody: *"i tried
for more variation in the numbers"* — while only ever changing `num2`).

## 2. The zero-count table — the right way to characterize a row set, exactly

The tempting shorthand ("zeros are always 2, 1, 0, or a whole row") is
close but **not exact** — checked directly for `num1=1234567890`:

```
num1*0 = 0              -> whole row (all zero)
num1*1 = 1234567890     -> 1 zero
num1*2 = 2469135780     -> 1 zero
num1*3 = 3703703670     -> 3 zeros   <- breaks "2,1,0"
num1*4 = 4938271560     -> 1 zero
num1*5 = 6172839450     -> 1 zero
num1*6 = 7407407340     -> 3 zeros   <- breaks "2,1,0"
num1*7 = 8641975230     -> 1 zero
num1*8 = 9876543120     -> 1 zero
num1*9 = 11111111010    -> 2 zeros
```

**The general, exact method, for any `num1`:** compute `num1*d` for
`d in 0..9`, count zeros in each — that IS the complete, exhaustive
characterization of every row you will ever see for that `num1`. Don't
report an approximate pattern from a handful of observed rows when the
full table is ten numbers and trivial to compute exactly. This is the
same discipline as `[[feedback_chase_every_anomaly]]` applied here: a
pattern that's "almost" 2/1/0 is a different, less interesting fact than
one that's exactly 2/1/0 — report which one you actually have.

## 3. Colors are the interface — keep the mapping exact, speak in it

Cody's console shows digits as colors, not numbers — when discussing a
matrix with him, describe cells by color, not digit value, to match what
he's actually looking at. Canonical mapping (`render.py`/`curses_ui.py`
`DIGIT_COLOR`/`DIGIT_RGB`, identical in both):

| digit | color | note |
|---|---|---|
| 0 | **black** | deliberately invisible in the live/curses cascade view (blends into terminal bg on purpose, so the eye tracks only 1-9); kept visually distinct from blank in the static PIL renderer instead — two different tools, opposite calls, both intentional |
| 1 | red | |
| 2 | green | |
| 3 | yellow | |
| 4 | blue | |
| 5 | orange | |
| 6 | purple | |
| 7 | cyan | |
| 8 | magenta | |
| 9 | lime | |

Do the actual computation in numbers (exact, checkable); translate to
color names only in what you say to Cody. Keep this table handy rather
than re-deriving it — it's fixed, not per-session.

## 4. Orientation — the bug that was actually backwards, and why it mattered

Screen columns read left-to-right like normal writing: most significant
digit on the left, each row staggering further **left** as the
multiplier digit's place value rises (real grade-school layout). An
earlier version had this exactly backwards (units on the left, rows
staggering right) — caught from a live screenshot 2026-09-22, fixed in
both `render.py` and `curses_ui.py`. Verify orientation on any new
render by checking: the row for the *units* digit of `num2` should sit
flush right, unshifted; the row for the *leading* digit should sit flush
left, maximally shifted. If that's inverted, the column math is
backwards again.

## 5. Where this is actually going — honest status

Cody's own framing names the destination: this addition-matrix
methodology (row templates, periodicity under incrementing, exact
zero/digit-count characterization) is training for
`GenerationalLineage`'s factoral decomposition / spectral recombination
engine — studying how a *fixed* generating object (`num1`) produces a
*bounded, enumerable* set of components (the ten row templates) that
then recombine under a second parameter (`num2`)'s digits is the same
shape as decomposition/recombination there. **The bridge is now built
and checked (2026-09-26)** — see §6. Don't read this section's original
"not built yet" as still current; it described the state before that
session.

## 6. The bridge, built and checked — a three-way constraint search for undoing the product

2026-09-26: reframed as an RSA-modulus factoring exercise (`N=p*q`, both
factors unknown). Three geometric objects, confirmed to be genuinely
distinct depending on coordinate frame, not the same thing twice:

- **Rows** (`j=0..9`, one per digit of the known-in-forward, unknown-in-
  reverse factor) — the multiplicative constraint: fixing one factor
  gives exactly 10 possible row values, full stop (§1).
- **Local-offset lines** (`k=0..10`, position within a row's own
  11-digit product) — fixed at `k=0` (a row's units digit depends ONLY
  on that factor's own units digit, verified independent of every other
  digit), fuzzy at `k=10` (the 11th-digit/overflow position, which
  depends on the FULL factor and can flip the row's own digit count).
  These are diagonals in the assembled (row, global-column) view, but
  straight lines in the native (row, local-offset) view.
- **Global columns** (`c=j+k`, the place-value position that must match
  a digit of the known product `N`) — the additive-with-carry
  constraint. Diagonal in the native view, straight column in the
  assembled view. Rows, local-offset lines, and global columns are
  mutually transversal (any two meet at exactly one cell) — the same
  three-way structure real Sudoku gets from row+column+box, not a
  simplification of it.

**The algorithm**: digit-DP / constraint-propagation search recovering
BOTH factors' digits simultaneously, column by column from the fixed
(units) end outward, using the column-convolution sum (all `p_i*q_j`
with `i+j=c`, plus carry-in) to prune which `(p_c, q_c)` digit pairs
survive at each step. Script:
`ContextPlease/claude/scratchpad/2026-09-26_addition_matrix_sudoku/
factor_search.py` — reproducible directly, stdlib only.

**Verified, exactly, three sizes:**

| n_digits per factor | example | max live states | columns |
|---|---|---|---|
| 2 | `61*53=3233` | 40 | 4 |
| 3 | `113*127=14351` | 400 | 6 |
| 4 | `1009*1013=1022117` | 4000 | 8 |

Correctly recovers the true factor pair in every case (verified
`p*q==N` directly, not assumed). **Exact scaling law measured, not
estimated: peak live-state count is `O(10^n_digits)`, a clean ×10 per
added digit.** That is the same exponential order as brute-force search
over one factor's digits — real, useful pruning at almost every
individual column (survival ratios well below 1 most steps — column 2
of the 3-digit case cuts 400→48, for instance), but the peak still
grows exponentially. Also worth recording as found, not smoothed over:
the branching is **not monotonic** — it can transiently grow before
later columns prune it back down (`4→40→400` before collapsing to `2`
in the 2-digit case).

**Status: CALCULATED, honestly scoped.** This is a real, correct,
working constraint-propagation algorithm for the addition-matrix
undoing direction — not a claim of polynomial-time factoring, which
would be a fundamentally different kind of result and is not what this
measures. See `[[feedback_calculated_label]]`.

## Files

`MultiplicationMatrixAnimator/`: `matrix_math.py` (exact arithmetic,
self-checking), `render.py` (static PNG, quarter-inch grid), `mapper.py`
(constructor/evolution-mode generator, memory-safe streaming export),
`driver.py` (Tkinter odometer-wheel live view), `curses_ui.py` (terminal
live view — `Ctrl+O` cycles step place, `Ctrl+G`/`Ctrl+N` jump
num2/num1 directly, nano-style status bar).
