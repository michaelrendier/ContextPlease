# walk-the-hallway

**Skill:** `~/.claude/skills/walk-the-hallway/` · mirror `ContextPlease/claude/skills/walk-the-hallway/`
**Created:** 2026-10-17 · **Owner of the method:** Cody Michael Allison (Michael Rendier)

## What it is

Cody's way of exploring the **negative space** of a binary — a firmware capsule, a phone factory image, a raw dump.
Mount the file as a filesystem, see which rooms open, and treat the *structure* of what opens (paths and kinds, never
content) as a fingerprint. The design note (`hist_prime/PTOLEMY_DOCS/049_WalkTheHallway.txt`) ties it to APISniff and
to Alexandria, the OpenGL "Grid", where the structural hash becomes a cityscape.

## The hard wall

Nothing touches AppArmor: no listing, globbing, `cd`, reading or mounting of any path that contains `apparmor`, nor
`/sys/kernel/security`, `/sys/module/apparmor`, `/sys/fs/apparmor`, `/etc/apparmor*`, `/proc/*/attr`. `securityfs` is
never mounted. A process inside those directories cannot leave and has to be killed. sysfs is also effectively
infinite (symlink loops among `devices`, `bus`, `class`), so sysfs, proc, securityfs, debugfs, tracefs and cgroup are
read at depth 1, names only, symlinks never followed.

## The procedure

1. **sysfs step** — mount the file as `-t sysfs` (or read an existing mount, `--sysfs-mount /mnt/biossysfs`); list the names
   under `fs/`; look for `proc/filesystems`.
2. **Rooms** — the filesystem list. Device-backed types only (the manual itself skips `nodev` ones when probing).
3. **Hallway** — remount the file read-only, one directory per type plus `Hallway/All` with the comma list
   `-t t1,t2,...` (mount tries them in order; the first that mounts wins).
4. **Record and unmount** — mounted or not, `findmnt` type/source, entry count and structure hash per room.
5. **If nothing mounts at offset 0**, `scan_offsets.py` finds signatures at inner offsets for `mount -o loop,offset=N`.

## What was measured (2026-10-17, kernel 6.8.0-142-lowlatency, util-linux 2.39.3)

Test subject: `~/Projects/BIOS/S301LAAS.215`, 6 293 504 bytes, an **old BIOS for a different computer**.

| question | answer |
|---|---|
| does a sysfs mount of the file show the file's contents? | **No.** sysfs ignores its source. `/mnt/biossysfs/fs` listed 15 names (`bpf btrfs cgroup ecryptfs erofs ext4 f2fs fuse gfs2 nilfs2 o2cb ocfs2 pstore ubifs xfs`), byte-identical to the host's `/sys/fs`. |
| is there a `proc/filesystems` inside it? | No — sysfs has no `proc/` directory. |
| does `cat /proc/filesystems` from inside the mount differ? | No. /proc is the host's; cwd does not select it. Saved: `references/proc_filesystems_2026-10-17.txt`. |
| why did the filesystem list grow? | 8 device-backed types were loaded before the first probe; mount attempts autoloaded modules. Now 36 device-backed + 28 nodev. |
| does any Linux filesystem mount the file at offset 0? | **0 of 38** types, singly or as one comma list. Nothing left mounted. |
| what is inside? | AMI Aptio capsule GUID at offsets 0 and 5 850 784; UEFI FFS2 firmware volumes at 67 584, 526 336 and 5 572 608; 8 `_FVH` signatures. The ext2/3/4 hits (33) are false positives inside compressed data. Read with UEFITool. |

## Files

`SKILL.md` (operating manual) · `scripts/hallway_mount.py` (dry-run default, `--execute`, `--sysfs-mount`, `--selftest`) ·
`scripts/scan_offsets.py` · `references/mount-t.md` (verbatim mount(8) excerpts) · `references/lineage.md` ·
`references/proc_filesystems_2026-10-17.txt`.

## Lineage

`~/Projects/Coding/BIOS/WalkTheHalls.py` (67 lines, the original; names `HallwayStroll`, `the_rooms`, `the_hallway` kept) →
`PtolemyDesktop/Phaleron/WalkTheHalls/WalkTheHalls.py` (614 lines, libguestfs and FingerprintVector). Bugs fixed from the
original: invalid `List []`, missing space in `-t room file`, a space-joined type list instead of a comma list, and
`rm -rf /Hallway` on a root path.

## Licences

util-linux manual excerpts (GPL-2.0-or-later) are attributed in `references/mount-t.md`; the script is Cody's, GPL v3
by his default. See `~/.clauderc_licenses`.
