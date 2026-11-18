---
name: zork-mapping
description: >
  Cody's hand method for mapping Infocom / Z-machine / ZIL games onto one sheet of graph paper, as an algorithm and as outputs (SVG, ASCII/Unicode text,
  later curses and PyQt6). Load when: reading ZIL source for rooms and exits, building a room map of any Lost Treasure of Infocom (Zork I-III, Enchanter,
  Planetfall, ...), laying rooms on a 3x3-per-room lattice, writing a text-mode map, numbering rooms, colouring levels, or working on the ZorkMapper repo.
  Built 2026-11-17 from the Zork I-III maps; the lattice rules are the author's own.
version: 1.0.0
---

# Zork mapping: the graph-paper lattice

Repository: `~/Projects/ThePlace/ZorkMapper` (GPL-3.0; `github.com/michaelrendier/ZorkMapper`). Sources (MIT, Microsoft 2025) are fetched by `./fetch_sources.sh` into `sources/` (zork1, zork2, zork3 from `historicalsource`); every request carries a Mozilla user agent. Other Infocom games: the same `historicalsource` account holds many ZIL sources; games with only a story file (`.z3`/`.z5` in `/home/rendier/Games/dosbox/zork/infocom/`) need a Z-machine object-tree reader (not built).

## 1. Read the game (`zorkmapper/zil.py`, `model.py`)
ZIL is LISP-like: `<FORM>`, `(LIST)`, `"string"`, `;` comments out the next form. Rooms are `<ROOM NAME (DESC "Name") (LDESC "text") (NORTH TO X) ... (FLAGS ...) (GLOBAL ...) (ACTION fn)>`; objects `<OBJECT NAME (IN ROOM) (DESC ..) ...>`; room objects attach to their room.
Exit kinds: **to** `(DIR TO ROOM)`; **cond** `(DIR TO ROOM IF FLAG [IS OPEN] [ELSE "msg"])`; **per** `(DIR PER ROUTINE)` (a routine decides; destination unknown); **blocked** `(DIR "message")`. Directions: NORTH SOUTH EAST WEST NE NW SE SW UP DOWN IN OUT LAND (+ game-specific). **`(IN ROOMS)` is the parent, `(IN TO KITCHEN ...)` an exit**: tell them apart by the first value (TO/PER/SORRY/string = exit).
Descriptions: `LDESC`, else the strings the ACTION routine prints under `M-LOOK`; `LDESC " "` is a placeholder. Dynamic rooms (flags) come out as the concatenation of every variant: hand-edit before feeding an image generator.

## 2. The lattice (`lattice.py`): one sheet of graph paper
- A room is one square and owns a **3 x 3 block**: its **eight neighbours are pathway squares**. Rooms sit on every second square (a sub-grid lattice), so neighbouring rooms are separated by exactly one pathway square. No spacing decisions.
- N/S/E/W: a line through the whole next square to the next room. Diagonals run corner to corner through the square.
- **UP and DOWN are drawn as diagonals** (up leans up-right then up-left; down leans down-left then down-right), labelled **U** and **D**.
- Long runs may skip lattice spots (the line passes straight over them) while no room sits in the way. A link that cannot be drawn straight is a **connector**: a stub labelled with the target's number. A straight link replaces an earlier connector for the same pair.
- One-way (no exit back): an arrow in the **middle** of the line. Conditional exits dashed. Exit to itself: a circle. PER exits: a marker (direction letters), no line. IN/OUT/LAND have no geometry: connectors.
- **Leave out mazes and puzzles**: point into blank space and write the word. Exclusion profiles: Zork I `MAZE-n` and `DEAD-END-1..4` (DEAD-END-5 is the coal mine's); Zork II the nine "Oddly-angled Room"; Zork III `CP` (the Royal Puzzle).
- Placement is a breadth-first walk from the start room (Zork I WEST-OF-HOUSE, II INSIDE-BARROW, III ZORK2-STAIR): nearest straight spot first, longer runs next, then rooms are set apart (dashed square). The result depends on the order, so rooms can be pinned by hand and the rest re-flowed.

## 3. Outputs
- `sheetsvg.py` / `--svg`: graph-paper SVG in the manner of the Infocom map (boxes, plain lines, arrows, U/D, `to N` notes, legend of numbered names).
- `asciiart.py` / `--ascii PREFIX`: text map (`.txt` plain Unicode, `.ans` ANSI colour). **A square is two characters with a one-space buffer on each side and a blank row between rows** (`RR  ==  RR`: two spaces between neighbours, a blank row between rows; where two passage squares meet the gap fills so hallways stay continuous: `====` and a column of `||`; a room never touches its passages; the two pipes sit under the two digits). Rooms: two digits (`07`); **100 = `**`, 101..109 = `*1..*9`, 110 = `*0`**. Passages: **east/west `==`, north/south `||` (a hallway look), diagonals `//` and `\\`** (the top row of a room's block reads `\\ || //`); crossings `XX` `++`. One-way arrows replace the passage in the middle square (`=>` `<=` `^^` `vv`, `↗/` `↖\\` `↘\\` `↙/`). U/D replace the first character of the diagonal next to the room that goes up/down. Connectors: the target number in superscript (`²³`). Maze/puzzle: the word (`Ma ze`). `⟲` own-room loop; `?N` a routine decides that exit.
- Background colour = **level**: the start room's level (the surface, around the white house) is white; up is lighter (yellow, cyan ...), underground darker (blue, purple, brown ...). Levels come from a walk over UP/DOWN exits (first assignment wins; inconsistent vertical exits in a game can mislabel a room).
- `describe.py` / `--descriptions FILE`: plain text of room names and descriptions.

## 4. Rules for the viewers (planned)
Curses and PyQt6 viewers: the map is larger than the viewport; the **current room is centred**; all geometry in **percentages** so a bigger window adds viewport, not map scale (see the `spatial-simulation` skill, nes-viewport section: clamp, derive indicators, never store them). Left palette = the adventure-toolkit hand mapper; right sidebar (collapsible) = room parts; bottom status box (collapsible).
