# NES scroll archetypes — the test corpus

`/home/rendier/Games/console/nes` — **628 `.nes` files, 626 parse as iNES**,
~180 MB. Classified by `assets/nes_scan.py` (iNES mirroring bit + mapper, nudged
by a known‑title table). Rerun it after adding ROMs; it writes `nes_corpus.json`
next to the ROMs.

```
archetype        count   header axis (pre-override)
2d-free          342     2d-free    361   (incl. MMC1/MMC3 runtime mirroring)
vertical         142     vertical   146
horizontal       116     horizontal 119
screen-locked     15
parallax           7
auto-scroll        4
```

The mirroring bit is a real signal: **horizontal arrangement (bit 0 clear) →
vertically adjacent nametables → the game scrolls vertically**; vertical
arrangement (bit set) → horizontal scroll; four‑screen → 2D. MMC1/MMC3 switch
mirroring in software, so those (342) are grouped as 2d‑free for testing.

## Per‑archetype: shape, ROM examples, and what to assert

### screen‑locked — `cw == vw && ch == vh`
`Balloon_fight, Bubble_bobble, Burger_time, Arkanoid, Donkey_kong, Wrecking_crew,
Joust, Dig_dug2, Pac_man`
- both bars **hidden / disabled**; `move_to_top` and `move_to_bottom` are no‑ops
- nothing clipped; `first_visible_row == 0` and `last_visible_row == ch - 1` always
- `assert_viewport_sound` takes the `not vbar.visible` branch

### horizontal side‑scroller — `cw > vw, ch == vh`
`Castlevania, Castlevania2, Contra, Amagon, Athena, Battle_of_olympus,
City_connection, Conflict, Baby_Boomer`
- vertical bar hidden; horizontal bar present
- `move_to_left` → col 0 flush; `move_to_right` → last col flush on the right edge,
  **no gap, no clip**
- horizontal thumb: `pos 0` at left, `pos == T - len` at right, `len` proportional
- run `assert_viewport_sound` with x/w swapped in (`hbar`, `move_to_left/right`)

### vertical scroller — `ch > vh, cw == vw`   ← the PTorrent‑box shape
`1942, 1943, Airwolf, Bionic_commando (vertical stages), Black_bass, Big_foot,
Anticipation, Baseball`
- vertical bar present, horizontal hidden
- this is exactly a list pane: `move_to_top → row 0`, `move_to_bottom → row ch-1`
  flush, thumb 0 → `T - len`, SWEEP covers `{0 … ch-1}`
- **the three PTorrent boxes must each pass this independently**

### 2D free scroll — `cw > vw && ch > vh`
`Boulder_dash, Gauntlet, Gauntlet2, Demon_sword, Road_blasters, Silent_assault,
Archon, Alien_syndrome, Astyanax` (+ all MMC1/MMC3 titles)
- all four `move_to_*` land flush; **SWEEP by page must visit every content cell**
  (`union of visible rects == content`)
- both thumbs reach 0.0 and 1.0; neither thumb full‑length
- resize on both axes → re‑clamp, re‑size both thumbs

### screen‑snap 2D — offset always a multiple of `vh`/`vw`, last screen a short clamp
`Zelda (overworld & dungeons), Metroid rooms, Kid_icarus (vertical snap),
Battle_of_olympus`
- `snap_down/up` move whole screens; the **last** screen is a plain clamp to
  `max_oy` even though it is shorter than `vh`
- `end` still lands flush (`oy == max_oy`, not `(rows // vh) * vh`)
- snap math and clamp math are different paths — test both

### auto‑scroll / forced — `oy` advances on a timer, input cannot stop it
`Gradius, Life_force, Burai_fighter, Sky_shark` (+ Battletoads Turbo Tunnel,
SMB3 airships)
- model as `follow_tail`: viewport pinned to `max_oy`; content growth lengthens
  `ch`, shrinks the thumb, does **not** jump the view
- user scrolls back → unpin; new content while unpinned must not move `oy`
- `move_to_bottom` re‑pins
- this is the live‑log / "jump to newest" behaviour for a status pane

### parallax / multi‑layer background — far bg at `k·offset`, `k < 1`
`Batman, Batman_return_of_the_joker, Kirby's_adventure, Power_blade,
Shadow_of_the_ninja, Journey_to_silius`
- the "three layers" made literal: `1a` far bg `= offset * k`, `1b` playfield
  `= offset`, overlay = bars + HUD
- **only the playfield layer's extent defines `max_ox/max_oy` and the thumbs.**
  A parallax layer that is wider than the playfield must not enlarge the clamp
  or shrink the thumb — a common regression when a designer swaps in a bigger
  backdrop art asset.

## Using the corpus in a build

1. `nes_scan.py <dir>` → `nes_corpus.json` (list of `{file, archetype, prg_kb, …}`).
2. For each pane under test, pick the matching archetype's shape, synthesise a
   content map of that shape (or use the real pane's measured `cw/ch`).
3. Drive `move_to_top / move_to_bottom / move_to_left / move_to_right` and a
   `page_down` sweep; run `assert_viewport_sound`.
4. `assets/viewport_demo.py` does 2–3 interactively in curses so you can *watch*
   the thumb travel the full track while the whole map passes through the frame.
