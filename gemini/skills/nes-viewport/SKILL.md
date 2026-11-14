---
name: nes-viewport
description: >
  Methodology for a 2D viewport onto a map larger than itself — offset/clamp math,
  the three composited layers, menu-driven (D-pad / arrow-key) navigation, and a
  reusable "move-to-top / move-to-bottom" acceptance test that proves a scrollbar
  sweeps the WHOLE content through its viewport. Uses NES scroll archetypes
  (side-scroller, top-down, screen-snap, auto-scroll, parallax) as the test corpus.
  Load when building or debugging any scrolling region: a scrollbar or thumb that
  is stuck / wrong-sized / out of sync with the content, an Android RecyclerView /
  NestedScrollView / ScrollView that "doesn't scroll" or has three panes that
  don't scroll independently, a curses newpad / list that clips its last row or
  never reaches the bottom, "scroll to top", "scroll to bottom", "jump to end",
  "follow tail", pane/box that shows content larger than its frame.
---

# 2D NES Viewport — ergonomics & content‑interaction methodology

A viewport is a fixed rectangle showing part of a larger content **map**. The NES
did exactly this in hardware (a 256×240 screen over a scrolling nametable map).
Every scrollable pane — an Android list, a curses pad, the three PTorrent boxes
(ptorrent list / status / info) — is the same problem. Get the model right once.

## 1. The model  (see `references/viewport-model.md` for the full derivation)

```
content   cw × ch          the map, measured AFTER data is loaded and laid out
viewport  vw × vh          the visible frame, fixed
offset    (ox, oy)         top-left of the viewport inside the content

max_ox = max(0, cw - vw)         max_oy = max(0, ch - vh)
INVARIANT:  0 ≤ ox ≤ max_ox      0 ≤ oy ≤ max_oy      (re-clamp after EVERY move)
```

Scrollbar geometry is **derived from the offset, never stored separately**. For a
vertical bar with track length `T`:

```
thumb_len = clamp(round(T * vh / ch), MIN_THUMB, T)
thumb_pos = round((T - thumb_len) * (oy / max_oy))         if max_oy > 0 else 0
no scroll needed (ch ≤ vh):  hide/disable the bar, thumb_len = T, thumb_pos = 0
drag/click at track y:  oy = round(max_oy * y / (T - thumb_len)) ; then clamp
```

The #1 defect (and almost certainly the PTorrent‑APK three‑box bug): a scrollbar
that keeps its **own** position field, or that computes `ch` from the wrong number
— `wrap_content`, a stale pre‑data measurement, or the parent's height instead of
the child's laid‑out height. The bar and the content then disagree.

## 2. The three layers  (composite every frame, in order)

1. **Map layer** — the full content, translated by `(−ox, −oy)`.
   Android: the scrolling child View / `Canvas.translate`. Curses:
   `pad = curses.newpad(ch, cw)` then `pad.refresh(oy, ox, y0, x0, y1, x1)`.
2. **Frame / mask layer** — fixed. The clip rect. Android: parent with
   `clipChildren=true` (or the `ScrollView` bounds). Curses: the destination
   window rect — `pad.refresh`'s last four args ARE the clip.
3. **Overlay layer** — scrollbar(s) + HUD, drawn in fixed viewport coordinates
   **after** the map, so the bar reads the same `oy` the map just used. They
   cannot drift apart if you never let the bar hold state.

## 3. Menu‑driven navigation (D‑pad / arrow keys — no free drag)

Each command is `offset += Δ` then **clamp** then recompute the bar.

| command | Δ (vertical) | NES analogy |
|---|---|---|
| `up` / `down` | `∓1` cell | walk one step N/S |
| `left` / `right` | `∓1` cell on `ox` | walk E/W |
| `page_up` / `page_down` | `∓(vh − overlap)` (overlap 1) | screen transition |
| `home` / `move_to_top` | `oy = 0` | warp to level start |
| `end` / `move_to_bottom` | `oy = max_oy` | warp to level end |
| `jump(n)` | `oy = clamp(n)` | password / stage select |
| `follow_tail` on | pin `oy = max_oy`; new content only grows `ch` | auto‑scroll shmup |

A fling / smooth‑scroll is `page_*` with deceleration; the **terminal** state is
still exactly one of the clamped values above.

## 4. The acceptance test — "move to top / move to bottom" as an inspector

This is how you prove a scrollbar actually pushes every row of card data through
the viewport. `assets/viewport.py` ships it as `assert_viewport_sound(vp)`.

```
1. CLAMP     set oy = -10**9  → oy must be 0 ;  set oy = +10**9 → oy must be max_oy
             max_oy must equal max(0, ch - vh)      (not ch - vh — the max(0,…) matters)
2. FLUSH     move_to_top()    → first_visible_row() == 0
             move_to_bottom() → last_visible_row()  == ch - 1
             AND the last row is not clipped: its far edge sits on the viewport's
             far edge (allow one partial-cell of slack only when vh % row ≠ 0)
3. THUMB     move_to_top()    → thumb_pos == 0
             move_to_bottom() → thumb_pos == track_len - thumb_len
             thumb_len == clamp(round(track*vh/ch), MIN_THUMB, track)
4. SWEEP     from top, page_down repeatedly; the UNION of visible row ranges must
             equal exactly {0 … ch-1}.  A gap  → page delta ignores the partial
             last page.  An overshoot past ch-1 → clamp missing on page_down.
```

When a pane "doesn't scroll properly," run this and read which assertion fails —
the failure table in §7 maps each to a cause.

## 5. NES archetypes = the test corpus  (`references/scroll-archetypes.md`)

`/home/rendier/Games/console/nes` — 626 iNES ROMs, classified by the mirroring bit
+ mapper (`assets/nes_scan.py`). Each archetype exercises a different viewport
edge case; port the check against the matching pane:

| archetype | content vs viewport | ROM examples (this dir) | what it tests |
|---|---|---|---|
| **screen‑locked** | `cw==vw && ch==vh` | Balloon Fight, Bubble Bobble, Burger Time, Arkanoid | bar hidden/disabled; `home`/`end` are no‑ops; nothing clipped |
| **horizontal side‑scroller** | `cw>vw, ch==vh` | Castlevania, Journey to Silius, Battle of Olympus, Amagon, Athena | vert bar hidden; `move_to_left`/`right` land flush; thumb 0→1 on x |
| **vertical scroller** | `ch>vh, cw==vw` | 1942, 1943, Airwolf, Xevious, Big Foot | mirror of above on y — this is the PTorrent‑box shape |
| **2D free scroll** | `cw>vw && ch>vh` | Boulder Dash, Gauntlet, Demon Sword, Road Blasters, Silent Assault | all four `move_to_*` flush; SWEEP covers the whole map; both thumbs 0→1 |
| **screen‑snap 2D** | offset always a multiple of `vh`/`vw`, last screen a short clamp | Zelda 1 (overworld/dungeon), Metroid rooms, Alien Syndrome | `end` still flush despite the short last screen; snap math ≠ clamp math |
| **auto / forced scroll** | `oy` advances on a timer; input can't stop it | Battletoads (Turbo Tunnel), Gradius/Life Force, SMB3 airships | `follow_tail`: pinned to `max_oy`; growth while pinned lengthens `ch`, shrinks the thumb, does NOT jump the view |
| **parallax / multi‑layer bg** | far bg scrolls at `k·offset`, `k<1` | Blaster Master, Batman, Kirby's Adventure | only the playfield layer defines `max_o`; the parallax layer must not change the clamp or the thumb |

346 of the 626 report "dynamic" (mapper 1/4 control mirroring at runtime) — treat
those as **2D free scroll** for testing.

## 6. Android — the three‑box pattern

The PTorrent GUI has three panes (list, status, info) that must scroll
**independently**. The classic failure is one outer `ScrollView` wrapping three
`LinearLayout`s of rows: the outer view scrolls everything as one blob and each
inner box has effectively infinite height, so its own scrollbar never engages.

- Each box is its **own** scroll container: `RecyclerView` + `LinearLayoutManager`
  for the list; `NestedScrollView` (or another `RecyclerView`) for status / info.
  No `ScrollView` ancestor shared between them.
- `android:scrollbars="vertical"` + `setScrollbarFadingEnabled(false)` so the
  framework draws and sizes the thumb from `computeVerticalScrollRange()` /
  `…Offset()` / `…Extent()`. If the content is custom‑drawn, **override those
  three** — Range = `ch`, Extent = `vh`, Offset = `oy` (px). The thumb formula in
  §1 is exactly what the framework then applies.
- `move_to_top` = `smoothScrollToPosition(0)` / `scrollToPosition(0)`.
  `move_to_bottom` = `layoutManager.scrollToPositionWithOffset(itemCount-1, 0)`
  then `scrollBy(0, LARGE)` to pin, or keep a `followTail` flag and
  `scrollToPosition(itemCount-1)` on each insert only while it is set.
- Give each box a bounded height (`0dp` + layout weight, or a fixed `dp`) — a
  scroll container with `wrap_content` height never scrolls.
- If a box lives inside a scrolling parent anyway: set the child
  `nestedScrollingEnabled` deliberately so the drag isn't stolen; prefer
  refactoring the parent out.

## 7. Curses

`pad = curses.newpad(ch, cw)`; draw all content once; blit with
`pad.refresh(oy, ox, top, left, bot, right)` — the last four args clip for free.
Draw the bar in the frame column at `right+1`: rows `[thumb_pos, thumb_pos+thumb_len)`
in the selection attr, the rest as a dim `│`. Keys: `KEY_UP/DOWN → oy ∓= 1`,
`KEY_PPAGE/NPAGE → oy ∓= vh-1`, `KEY_HOME/END → 0 / max_oy`, then always
`oy = max(0, min(oy, max_oy))`. `assets/viewport_demo.py` is a working reference.

## 8. Failure → cause

| assertion that fails | almost always |
|---|---|
| `max_oy != max(0, ch-vh)` | `ch` measured before data bound / from `wrap_content` / from the parent, not the laid‑out child; or `ch - vh` without `max(0, …)` so an empty/short list gives a negative max |
| FLUSH top ok, bottom short (gap under last row) | `move_to_bottom` sets `oy = ch - vh - 1` (off‑by‑one) or scrolls to *position* without the trailing offset |
| FLUSH bottom clips the last row | viewport height counted in whole cells but `vh` isn't a multiple of the row height, and the partial cell isn't accounted for |
| THUMB stuck at top while content scrolls | the scrollbar holds its own offset and nothing writes `oy` into it; or `computeVerticalScrollOffset()` not overridden on a custom view |
| THUMB full‑length when it should be short | `thumb_len` uses `vh/ch` with `ch` still == `vh` (pre‑data) — recompute after the data loads and on every resize |
| SWEEP leaves a gap | `page_down` delta is `vh` but should be `vh - overlap`, or the last partial page is skipped because `oy` already equals a value `> max_oy - vh` |
| SWEEP overshoots past `ch-1` | no clamp after `page_down` |
| box scrolls the whole screen instead of itself (Android) | shared outer `ScrollView`; make each box its own bounded scroll container (§6) |

## Files

- `references/viewport-model.md` — full math, snap‑vs‑clamp, follow‑tail, resize.
- `references/scroll-archetypes.md` — the NES table + per‑archetype checks + the corpus scan.
- `references/android-scrollbars.md` — RecyclerView / NestedScrollView / custom `computeVerticalScroll*`.
- `assets/viewport.py` — framework‑agnostic `Viewport` + `Scrollbar` + `assert_viewport_sound()`.
- `assets/viewport_demo.py` — curses demo: drive an archetype, watch the thumb, run the test.
- `assets/nes_scan.py` — classify a NES directory by iNES header.
