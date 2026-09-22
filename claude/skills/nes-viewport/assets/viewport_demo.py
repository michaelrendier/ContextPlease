"""Curses demo of the 2D viewport + scrollbars.

    python3 viewport_demo.py

Drive an NES-style scroll archetype with the D-pad / arrow keys and WATCH the
thumb travel the full track while the whole content map passes through the frame.
Press `t` to run assert_viewport_sound() and see PASS / which assertion failed —
this is the "move-to-top / move-to-bottom" inspector for a real scrollbar.

Keys
  ← ↑ → ↓        scroll one cell            PgUp / PgDn   page
  Home / End     move_to_top / move_to_bottom
  , / .          move_to_left / move_to_right
  a              cycle archetype            f   toggle follow_tail
  +              append rows (test growth while follow_tail / while scrolled up)
  t              run assert_viewport_sound()
  q              quit
"""
from __future__ import annotations

import curses
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from viewport import Viewport, assert_viewport_sound  # noqa: E402

# (label, cw, ch)  — synthetic content shapes; a cell here is a grid square
ARCHETYPES = [
    ("screen-locked      cw==vw ch==vh", 18, 12),
    ("horizontal scroller ch==vh",       120, 12),
    ("vertical scroller   cw==vw   (the PTorrent-box shape)", 18, 400),
    ("2d-free scroll",                    120, 400),
    ("auto-scroll / live log (follow_tail)", 18, 60),
]


def make_vp(idx: int, vw: int, vh: int) -> Viewport:
    _, cw, ch = ARCHETYPES[idx]
    cw = max(cw, vw)
    ch = max(ch, vh)
    vp = Viewport(cw=cw, ch=ch, vw=vw, vh=vh)
    if "follow_tail" in ARCHETYPES[idx][0]:
        vp.follow_tail = True
        vp.move_to_bottom()
    return vp


def draw(stdscr, vp: Viewport, arch: int, msg: str):
    stdscr.erase()
    my, mx = stdscr.getmaxyx()
    # layout: frame occupies most of the screen, 1-col vbar on the right,
    # 1-row hbar on the bottom, a status line under that.
    fy, fx = 1, 1
    fh = max(4, my - 5)
    fw = max(10, mx - 4)
    vw, vh = fw - 1, fh - 1          # room for the bars inside
    if (vw, vh) != (vp.vw, vp.vh):
        vp.viewport_resized(vw=vw, vh=vh)

    stdscr.addstr(0, 0, f" archetype {arch+1}/{len(ARCHETYPES)}: {ARCHETYPES[arch][0]}"[:mx-1],
                  curses.A_REVERSE)

    # ── layer 1: the map, translated by (-ox, -oy) ──
    for row in range(vh):
        cy = vp.oy + row
        if cy >= vp.ch:
            break
        line = []
        for col in range(vw):
            cx = vp.ox + col
            if cx >= vp.cw:
                break
            # a readable cell: last two digits of (cy) and a col tick
            ch_ = str(cy % 100).rjust(2, "0") if col == 0 or cx % 8 == 0 else (
                "·" if (cx + cy) % 2 else " ")
            line.append(ch_)
        try:
            stdscr.addstr(fy + row, fx, "".join(line)[:vw])
        except curses.error:
            pass
    # frame edges
    for row in range(vh):
        try: stdscr.addstr(fy + row, fx + vw, "│")
        except curses.error: pass

    # ── layer 3: scrollbars (pure views of the offset) ──
    vb = vp.vbar(track_len=vh)
    if vb.visible:
        for r in range(vh):
            on = vb.pos <= r < vb.pos + vb.length
            try:
                stdscr.addstr(fy + r, fx + vw, "█" if on else "░",
                              curses.A_REVERSE if on else curses.A_DIM)
            except curses.error:
                pass
    hb = vp.hbar(track_len=vw)
    for c in range(vw):
        on = hb.visible and hb.pos <= c < hb.pos + hb.length
        try:
            stdscr.addstr(fy + vh, fx + c, "█" if on else ("─" if hb.visible else " "),
                          curses.A_REVERSE if on else curses.A_DIM)
        except curses.error:
            pass

    st = (f" oy {vp.oy:>4}/{vp.max_oy:<4}  ox {vp.ox:>3}/{vp.max_ox:<3}  "
          f"rows {vp.first_visible_row()}..{vp.last_visible_row()} of {vp.ch}  "
          f"vthumb[pos {vb.pos} len {vb.length}{' hidden' if not vb.visible else ''}]  "
          f"follow_tail {'ON' if vp.follow_tail else 'off'}")
    try:
        stdscr.addstr(my - 3, 0, st[:mx - 1], curses.A_BOLD)
        stdscr.addstr(my - 2, 0,
                      " ←↑→↓ PgUp/PgDn Home/End , . = move_to_*   a arch  f follow  + grow  t test  q quit"[:mx-1],
                      curses.A_DIM)
        if msg:
            stdscr.addstr(my - 1, 0, msg[:mx - 1],
                          curses.A_REVERSE)
    except curses.error:
        pass
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    arch = 2
    my, mx = stdscr.getmaxyx()
    vp = make_vp(arch, max(10, mx - 5), max(4, my - 6))
    msg = ""
    while True:
        draw(stdscr, vp, arch, msg)
        msg = ""
        k = stdscr.getch()
        if k in (ord("q"), 27):
            return
        if k == curses.KEY_UP:        vp.up()
        elif k == curses.KEY_DOWN:    vp.down()
        elif k == curses.KEY_LEFT:    vp.left()
        elif k == curses.KEY_RIGHT:   vp.right()
        elif k == curses.KEY_PPAGE:   vp.page_up()
        elif k == curses.KEY_NPAGE:   vp.page_down()
        elif k == curses.KEY_HOME:    vp.move_to_top()
        elif k == curses.KEY_END:     vp.move_to_bottom()
        elif k == ord(","):           vp.move_to_left()
        elif k == ord("."):           vp.move_to_right()
        elif k == ord("f"):
            vp.follow_tail = not vp.follow_tail
            if vp.follow_tail:
                vp.move_to_bottom()
        elif k == ord("+"):
            vp.content_resized(ch=vp.ch + 25)
            msg = f" appended 25 rows -> ch {vp.ch}  (oy stayed {vp.oy}, thumb reshaped)"
        elif k == ord("a"):
            arch = (arch + 1) % len(ARCHETYPES)
            vp = make_vp(arch, vp.vw, vp.vh)
        elif k == ord("t"):
            try:
                assert_viewport_sound(vp, track_len=vp.vh)
                msg = " assert_viewport_sound: PASS — the thumb sweeps the whole content"
            except AssertionError as e:
                msg = f" assert_viewport_sound: FAIL — {e}"
            vp.move_to_top()


if __name__ == "__main__":
    curses.wrapper(main)
