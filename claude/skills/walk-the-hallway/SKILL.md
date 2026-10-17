---
name: walk-the-hallway
description: Cody's "walk the hallway" — explore the negative space of a .bin / firmware / factory image by mounting the FILE under every filesystem type the kernel knows, read-only, and recording which rooms open and what structure they hold. Carries a HARD WALL: never enter, list, glob, cd into or mount anything that touches AppArmor. Use when the task is to find what filesystems a binary image actually contains (firmware capsules, phone factory images, BIOS files, raw dumps), to fingerprint an image by its mount geometry, or whenever Cody says "walk the hallway", "hallway", "WalkTheHalls", "mount the bin", "negative space of the binary", or asks what `mount -t a,b,c` does with a file.
---

# Walk the hallway

His method, from his own notes (`PTOLEMY_DOCS/049_WalkTheHallway.txt`): mount a binary as a filesystem,
look at the rooms that open, and treat the **structure** (not the content) as the fingerprint. The
negative space of a binary — the well-defined parts a hacker reads first — is where factory images give
up their secrets. The structure hash feeds APISniff and Alexandria ("the Grid").

## 0. HARD WALL — AppArmor. Read before every run.

**Never** enter, `ls`, `find`, glob, `cd` into, `cat` under, `stat`-walk, mount, or recurse through any path
that touches AppArmor. A process stuck inside those directories cannot leave and has to be killed.

- Walled (string test, no filesystem call needed): any path component containing `apparmor` (any case);
  `/sys/kernel/security`, `/sys/module/apparmor`, `/sys/fs/apparmor`, `/etc/apparmor*`, `/var/lib/apparmor`,
  `/var/cache/apparmor`, `/proc/self/attr`, `/proc/thread-self/attr`.
- `securityfs` and `apparmorfs` are **never mounted**; securityfs is where the AppArmor tree is exposed.
- **Never `cd` into a mount.** Use absolute paths, one named file at a time, with `timeout`.
- **Never recurse into a pseudo (`nodev`) mount** — sysfs, proc, securityfs, debugfs, tracefs, cgroup, bpf.
  Their trees are live kernel state, not the image.
- **sysfs is effectively infinite.** `devices/`, `bus/`, `class/` and `block/` are symlink loops that point back at
  each other, and `/sys/devices` alone has tens of thousands of entries. Rules: **depth 1, names only, symlinks never
  followed, a hard entry cap, never `find`/`os.walk`/`ls -R` on sysfs, proc, securityfs, debugfs, tracefs or cgroup.**
  The walker in `hallway_mount.py` is for real (device-backed) mounts only: depth 3, `follow_symlinks=False`, 5000 entries.
- Every external command runs with a timeout (`STEP_TIMEOUT = 20 s`).
- `scripts/hallway_mount.py --selftest` proves the wall rejects 7 patterns before you run anything.

## 1. The procedure (his order)

1. **sysfs step.** `mount -t sysfs -o ro,nosuid,nodev,noexec FILE MP` (or read a mount Cody already made:
   `--sysfs-mount /mnt/biossysfs`, which the script never unmounts). Two bounded reads: the **names directly under
   `MP/fs`** (depth 1, AppArmor names dropped) and the single path `MP/proc/filesystems`. The script also lists the
   host's `/sys/fs` and records `sysfs_fs_identical_to_host`, so the report states whether the mount told it anything
   about the file. Then `umount MP` (unless it was Cody's).
2. **Rooms.** Take the filesystem list (from step 1 if it exists there, otherwise `/proc/filesystems`).
3. **Hallway.** Remount the FILE read-only: one directory per type under `Hallway/<type>/`, plus
   `Hallway/All` mounted with the **comma list** `-t t1,t2,...` (mount tries them in order; first success wins).
4. **Record** per room: mounted or not, `findmnt` fstype/source, entry count, structure hash
   (paths + kinds only, depth 3, symlinks not followed, AppArmor names skipped). **Umount everything.**

```
python3 -I ~/.claude/skills/walk-the-hallway/scripts/hallway_mount.py --selftest
python3 -I .../hallway_mount.py FILE --work DIR              # DRY RUN: prints every mount it WOULD run
python3 -I .../hallway_mount.py FILE --work DIR --execute    # real: needs root (uses `sudo -n` if not root)
python3 -I .../scan_offsets.py FILE                          # the next rung (below), read-only
```

Report goes to `DIR/hallway_report.json`. Exit status is non-zero only if something is left mounted.

## 2. What the kernel actually does (measured 2026-10-17, util-linux 2.39.3; manual excerpts in `references/mount-t.md`)

- **The `fs/` method (Cody, 2026-10-17): the directory `MP/fs` lists the filesystems the kernel has active.** Measured on
  `/mnt/biossysfs` (a sysfs mount whose source is the BIOS file): 15 names — `bpf btrfs cgroup ecryptfs erofs ext4 f2fs
  fuse gfs2 nilfs2 o2cb ocfs2 pstore ubifs xfs` — **byte-identical to the host's `/sys/fs`**. It is a real, useful cross-check
  on `/proc/filesystems` (active vs merely loaded), but because sysfs ignores its source it is the HOST kernel's list, not
  the file's. Neither `fs/` nor `proc/filesystems` can show what is inside the image.
- **Running `cat /proc/filesystems` from a shell whose cwd is inside the mount changes nothing.** /proc is the host's procfs
  and cwd does not select it (captured from `/mnt/biossysfs`, byte-identical to a plain cat:
  `references/proc_filesystems_2026-10-17.txt`).
- **Why the list got long.** Before the first probe only 8 device-backed types were loaded; the probe's mount attempts made
  the kernel autoload modules, so the list grew to 36 device-backed + 28 nodev. The modules stay loaded until unload or reboot.
- **Step 1 as first written cannot see inside the file.** `sysfs` is a `nodev` type: mount ignores the source
  argument and shows the host's `/sys`. `proc/filesystems` does not exist inside it (measured). The list
  you get is the kernel's list of supported types, not a list of what the file contains. The script records
  that outcome honestly in `sysfs_note` and falls back to `/proc/filesystems`.
- **The comma list is the real discovery mechanism.** `-t a,b,c` is an ordered probe. A type that mounts
  the file read-only IS a filesystem the file holds at that offset.
- **The manual itself skips `nodev` types when it probes.** Their source is ignored, so mounting them tells
  you nothing about the file and some (securityfs) expose the AppArmor tree. The script mounts only
  device-backed types. `--include-nodev-types` is opt-in and still never mounts securityfs/apparmorfs.
- **/proc/filesystems lists only loaded drivers.** mount(8) also points at `/lib/modules/$(uname -r)/kernel/fs`.
  The script adds block-backed types from a whitelist whose module exists (loaded on demand), including the
  ones firmware images use: squashfs, cramfs, erofs, romfs, jffs2, ubifs, minix, iso9660, udf, vfat, exfat, ext2-4.
- Unmounted pseudo types are listed in the report as `nodev_types`, so nothing is silently dropped.
- Mounts are always `ro,nosuid,nodev,noexec`. A loop device is created by mount and freed by umount
  (mount(8): auto-destruction since Linux 2.6.25). The script verifies nothing is left (`findmnt`).
- Loading a driver for an exotic filesystem parses an untrusted image in the kernel. Fine for a vendor
  firmware file; think before pointing the full hallway at a hostile image.

## 3. When nothing mounts: the offset rung

A capsule, factory zip-of-partitions or raw flash dump has its own header at offset 0, so no Linux filesystem
opens there. Run `scan_offsets.py FILE`: it finds filesystem and firmware-volume signatures at inner offsets.
Mount a hit with `mount -t TYPE -o ro,loop,offset=N,sizelimit=M FILE MP` (mount(8) LOOP-DEVICE SUPPORT).
Caution: a 2-byte magic such as ext's `53 ef` produces many false hits inside compressed data (measured: 33
on a 6 MB capsule, none real). Trust a hit only after a parse or a successful ro mount.

UEFI firmware volumes (FFS2/FFS3) are not Linux filesystems; the readers are UEFITool / UEFIExtract
(`/usr/bin/uefitool` is installed here; it is a GUI, there is no CLI extractor).

## 4. Worked result: BIOS capsule `~/Projects/BIOS/S301LAAS.215` (6 293 504 bytes), 2026-10-17

Cody: it is an OLD BIOS file for a different computer than this one. It is only a test subject here.

- sysfs mount succeeded; `fs/` lists 15 names identical to the host's `/sys/fs`; no `proc/filesystems` inside it.
- 38 device-backed types probed, singly and as one comma list: **0 mounted** at offset 0. Nothing left mounted.
- `scan_offsets.py`: AMI Aptio capsule GUID at 0 (and 5 850 784); UEFI FFS2 firmware volumes at 67 584,
  526 336, 5 572 608; 8 `_FVH` signatures in all. So the negative space is UEFI volumes, read with UEFITool.

## 5. Lineage (see `references/lineage.md`)

The original 67-line `~/Projects/Coding/BIOS/WalkTheHalls.py` (names `HallwayStroll`, `the_rooms`, `the_hallway`
kept here), the 614-line Phaleron rewrite (libguestfs, FingerprintVector), and his design note. Bugs in the
original that this script fixes: invalid `List []`, missing space in `-t room file`, space-joined type list
instead of a comma list, and `rm -rf /Hallway` on a root path. Never reproduce that `rm -rf`; the script only
`rmdir`s empty directories it created.

## 6. Standing rules

- Dry run first; `--execute` only on a file Cody has pointed at.
- Read-only always; the image is never written.
- Use the code's own identifiers (`HallwayStroll`, `the_rooms`, `the_hallway`) when talking about it.
- Report negatives as negatives: "0 of 38 mounted at offset 0" is a data point, not a failure.
- Licences: util-linux manual excerpts are GPL-2.0-or-later and attributed in `references/mount-t.md`.
