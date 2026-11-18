# Viewport model — full derivation

Symbols in **cells** (a cell is one list row / tile / screen). For a pixel bar,
multiply row counts by `row_px` and use `vh_px` for the real pane height.

```
cw, ch     content size   (measured AFTER data load + layout — see §Measuring ch)
vw, vh     viewport size  (fixed; the visible frame)
ox, oy     offset         (top-left of the viewport inside the content)
```

## Clamp

```
max_ox = max(0, cw - vw)
max_oy = max(0, ch - vh)
ox := clamp(ox, 0, max_ox)          clamp(v,lo,hi) = min(max(v,lo),hi)
oy := clamp(oy, 0, max_oy)
```

The `max(0, …)` is not optional: when the list is empty or shorter than the
pane, `ch - vh` is negative and an un‑guarded clamp would let `oy` go negative
or pin the thumb below the track.

Apply the clamp **after every mutation** — arrow, page, drag, `home`/`end`,
`jump`, and after `content_resized` / `viewport_resized`. Nothing else needs to
"recompute" because the scrollbar is derived, not stored.

## Visible range

```
first_visible_row = oy
last_visible_row  = min(ch - 1, oy + vh - 1)
```

At `oy = max_oy` and `ch > vh`, `last_visible_row == ch - 1` **exactly**. If your
code produces `ch - 2` there, `move_to_bottom` or the clamp is off by one.

## Scrollbar (vertical; horizontal is the same with x/w)

Track length `T` (rows for a text bar, px for a drawable). `MIN_THUMB` keeps the
thumb grabbable on a huge map (1 row, or ~24–48 px).

```
if ch <= vh or max_oy == 0:        bar hidden;  thumb_len = T;  thumb_pos = 0
else:
    thumb_len = clamp(round(T * vh / ch), MIN_THUMB, T)
    thumb_pos = round((T - thumb_len) * (oy / max_oy))          # 0 … T - thumb_len
```

Inverse — user grabs the thumb top to track‑row `y` (0 … T − thumb_len):

```
span = max(1, T - thumb_len)
oy   = round(max_oy * clamp(y, 0, span) / span)   ; then clamp
```

Click in the track (not on the thumb): page toward the click, i.e. `page_down` if
`y > thumb_pos + thumb_len` else `page_up`.

## Page delta and the partial last page

```
page_delta = max(1, vh - overlap)        overlap = 1 (keep one row of context)
```

`page_down` then clamps to `max_oy`, which is usually **not** a multiple of
`page_delta`. That last short jump is expected and correct — do not "round" it to
a page boundary or you leave a gap at the bottom. The SWEEP test in
`assets/viewport.py` catches both a gap (missing rows) and an overshoot (no clamp).

## Screen‑snap vs. clamp

Snap games (Zelda overworld, Metroid rooms) move `oy` in whole `vh` steps:

```
snap_down:  oy = min(max_oy, ((oy // vh) + 1) * vh)
snap_up:    oy = max(0,      ((oy - 1) // vh) * vh)
```

The **last** screen is still a plain clamp to `max_oy` (it may be shorter than
`vh`). `end` = `oy = max_oy`, never `(rows // vh) * vh`. Snap math and clamp math
are different code paths; test both land flush.

## follow_tail (auto‑scroll / live log)

```
follow_tail on   -> after every set_offset and every content_resized:  oy = max_oy
user scrolls up  -> follow_tail off (unpin)
while unpinned, appending rows:  ch grows -> thumb_len shrinks, thumb_pos falls
                 toward 0 relative to the new track; oy does NOT move
re‑pin           -> move_to_bottom() sets follow_tail on again
```

New content must never yank a viewport the user has scrolled away from. It only
lengthens the content and reshapes the thumb.

## Measuring ch (the usual bug)

`ch` is the height of the **laid‑out content**, available only *after*:

- the data is bound (adapter `itemCount` set, rows measured), and
- the container has a real height (not `wrap_content` inside another scroller).

Recompute `ch` and the thumb on: data set / changed, first layout pass, size
change, orientation change. A thumb sized while `ch == vh` (pre‑data) stays
full‑length forever if you never recompute.

## Reference implementation

`assets/viewport.py` — `Viewport`, `Thumb`, `vbar/hbar`, `vbar_to_offset`,
`content_resized`, `viewport_resized`, `follow_tail`, and
`assert_viewport_sound()`. Port the arithmetic; keep the test.
