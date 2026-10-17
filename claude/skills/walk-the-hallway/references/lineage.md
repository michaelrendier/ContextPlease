# Where the hallway script lives (found 2026-10-17)

| copy | lines | what it is |
|---|---|---|
| ~/Projects/Coding/BIOS/WalkTheHalls.py | 67 | the ORIGINAL mount-walk: `HallwayStroll.the_rooms()` reads /proc/filesystems, `the_hallway()` makes Hallway/<fstype>/ and Hallway/All and runs `sudo mount -t ...`. Its Hallway/ dir (38 empty fstype dirs, 2026-03-24) is the result of a run. |
| ~/Projects/ThePlace/PtolemyDesktop/Phaleron/WalkTheHalls/WalkTheHalls.py | 614 | the Phaleron rewrite: FingerprintVector dataclass, GPT/MBR parse, magic-byte survey, libguestfs instead of mount. Identical (md5) to ~/Projects/Ptol/PtolemyDesktop/Phaleron/WalkTheHalls/. |
| ContextPlease/claude/hist_prime/PTOLEMY_DOCS/049_WalkTheHallway.txt | — | Cody's design notes: "mount-as-sysfs → walk the tree → hash the structure (not content)"; feeds APISniff and Alexandria (the OpenGL "Grid"). |

Bugs in the 67-line original (all fixed in scripts/hallway_mount.py, names kept):
- `filetypes: List []` is a syntax error (and `List` is never imported).
- `"sudo mount -t " + room + self.file` has no space between type and file.
- `-t a b c` joins types with SPACES; mount wants a COMMA list (`-t a,b,c`).
- `rm -rf /Hallway` deletes a path under the filesystem ROOT, not the work dir. Never reproduce this.
- every type in /proc/filesystems is mounted, including nodev ones, which ignore the file and
  expose kernel trees (securityfs = the AppArmor tree).
