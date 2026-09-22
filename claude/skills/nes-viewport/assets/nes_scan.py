"""Classify a directory of NES ROMs into scroll archetypes.

    python3 nes_scan.py /home/rendier/Games/console/nes

Signal used (no emulation):
  iNES byte 6 bit 0 — nametable arrangement:
      0 -> horizontal arrangement / vertical mirroring  -> game scrolls VERTICALLY
      1 -> vertical arrangement / horizontal mirroring   -> game scrolls HORIZONTALLY
  iNES byte 6 bit 3 — four-screen VRAM                    -> 2D free scroll
  mapper (byte 6 hi | byte 7 hi) in the "dynamic" set     -> mirroring is switched
      at runtime (MMC1/MMC3/...) -> treat as 2D free scroll for viewport testing

Emits a histogram and writes <dir>/nes_corpus.json  (also to CWD if unwritable).
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

DYNAMIC_MAPPERS = {1, 4, 5, 9, 10, 19, 21, 23, 24, 25, 64, 69, 85}

# Well-known titles whose behaviour the header cannot capture. Substring match on
# a normalised filename. Keeps the corpus honest for the classics.
KNOWN = {
    "screen_locked":  ["balloon_fight", "bubble_bobble", "burger_time", "arkanoid",
                       "donkey_kong", "mario_bros", "wrecking_crew", "dig_dug",
                       "pac_man", "joust", "warpman"],
    "horizontal":     ["castlevania", "super_mario_bros", "contra", "ninja_gaiden",
                       "journey_to_silius", "battle_of_olympus", "double_dragon",
                       "ducktales", "mega_man", "rush_n_attack", "rygar", "shatterhand"],
    "vertical":       ["1942", "1943", "xevious", "tiger_heli", "ikari", "commando",
                       "spy_hunter", "jackal", "dragon_spirit", "airwolf"],
    "twod":           ["zelda", "metroid", "blaster_master", "gauntlet", "faxanadu",
                       "crystalis", "goonies_2", "battle_of_olympus", "milon",
                       "guardian_legend", "solstice", "marble_madness"],
    "autoscroll":     ["gradius", "life_force", "battletoads", "silkworm",
                       "sky_shark", "burai_fighter"],
    "parallax":       ["batman", "kirby", "blaster_master", "power_blade",
                       "shadow_of_the_ninja", "journey_to_silius"],
}


def _norm(name: str) -> str:
    return name.lower().replace(".nes", "").replace(" ", "_").replace("'", "")


def _known(name: str) -> str | None:
    n = _norm(name)
    for arch, keys in KNOWN.items():
        if any(k in n for k in keys):
            return {"screen_locked": "screen-locked", "horizontal": "horizontal",
                    "vertical": "vertical", "twod": "2d-free",
                    "autoscroll": "auto-scroll", "parallax": "parallax"}[arch]
    return None


def classify(path: str) -> dict:
    name = os.path.basename(path)
    try:
        with open(path, "rb") as f:
            head = f.read(16)
    except OSError as e:
        return {"file": name, "ok": False, "why": str(e)}
    if head[:4] != b"NES\x1a":
        return {"file": name, "ok": False, "why": "not iNES"}
    prg, chr_, b6, b7 = head[4], head[5], head[6], head[7]
    mapper = (b6 >> 4) | (b7 & 0xF0)
    if b6 & 0x08:
        axis = "2d-free"
    elif b6 & 0x01:
        axis = "horizontal"
    else:
        axis = "vertical"
    if mapper in DYNAMIC_MAPPERS and axis not in ("2d-free",):
        axis = "2d-free"          # mirroring is runtime-controlled
    known = _known(name)
    return {"file": name, "ok": True, "prg_kb": prg * 16, "chr_kb": chr_ * 8,
            "mapper": mapper, "header_axis": axis,
            "archetype": known or axis, "known_override": bool(known),
            "size": os.path.getsize(path)}


def main(argv: list[str]) -> int:
    d = argv[1] if len(argv) > 1 else "/home/rendier/Games/console/nes"
    roms = sorted(f for f in os.listdir(d) if f.lower().endswith(".nes"))
    rows = [classify(os.path.join(d, f)) for f in roms]
    ok = [r for r in rows if r.get("ok")]

    print(f"# NES scan — {d}")
    print(f"total .nes {len(rows)}   parsed {len(ok)}   skipped {len(rows) - len(ok)}\n")
    print("## archetype")
    for k, c in Counter(r["archetype"] for r in ok).most_common():
        print(f"  {k:<14} {c}")
    print("\n## header axis (before known-title override)")
    for k, c in Counter(r["header_axis"] for r in ok).most_common():
        print(f"  {k:<14} {c}")
    print("\n## examples per archetype")
    ex: dict[str, list[str]] = {}
    for r in ok:
        ex.setdefault(r["archetype"], [])
        if len(ex[r["archetype"]]) < 16:
            ex[r["archetype"]].append(r["file"].replace(".nes", ""))
    for k, v in ex.items():
        print(f"\n[{k}]  " + ", ".join(v))

    for target in (os.path.join(d, "nes_corpus.json"), "nes_corpus.json"):
        try:
            json.dump(ok, open(target, "w"), indent=1)
            print(f"\nwrote {target}")
            break
        except OSError:
            continue
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
