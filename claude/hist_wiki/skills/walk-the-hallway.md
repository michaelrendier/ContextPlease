# walk-the-hallway

**Skill:** `~/.claude/skills/walk-the-hallway/` · mirror `ContextPlease/claude/skills/walk-the-hallway/`
**Created:** 2026-10-17 · **Scope widened by Cody the same day (see below)** · **Owner of the method:** Cody Michael Allison (Michael Rendier)

## What it is (Cody, 2026-10-17: the intended goal)

A **reconnaissance pass that comes before the real crawl.** Point it at any collection of public-facing information and it walks
the hallways of that thing to learn its shape: where the files live, how they are named and sharded, which protocol each level
speaks, what kind of file each leaf is, what a listing costs. It records the structure as **its own sitemap**, and the sitemap
**powers the actual crawl**. It evaluates nothing and downloads only listings and a few magic bytes.

* **Cody's example:** a collection of coin images. The hallway finds where the images exist, records the structure
  (`images/<year>/<denomination>/<id>.jpg`, page sizes, shard sizes), and the crawler then fetches exactly what the map says.
* **Every filesystem and protocol presents information its own way.** The hallway has one *backend* per way of presenting a
  hall and one common map. The **`mount` door is itself a family of public-facing protocols**: `mount -t TYPE` opens a local
  image or a remote NFS, CIFS/SMB, WebDAV, SSHFS, FTP or S3 (FUSE) filesystem, and the hall then lists like a directory.
  Beside it: S3 prefix listings, FTP `LIST`, HTTP indexes and sitemaps, REST/JSON pages, TAP schemas and ObsCore censuses, and
  container files (FITS HDUs, tar/zip members, HDF5 groups, SQLite tables, CASA tables).
* **Not all at once.** Breadth-first, one level per expansion, in bounded **chunk cycles** run by threaded workers hopping between
  hosts, checkpointed so the walk resumes. Threads help across hosts (listings are latency-bound); within one host bandwidth
  does not add (measured 4.6 vs 4.9 MB/s).
* **Every file type:** a file is a *leaf* (identified by magic bytes, not opened) or a *container* (a hall of its own).
  Unknown types stay leaves with magic, size and entropy; the offset scan is the fallback inside unknown binaries.
* **The structure hash is the fingerprint** (his Alexandria design); diffing it on a re-walk flags drift.
* **The generalised wall:** when a door is closed — AppArmor, `robots.txt`, a login, a paywall, a rate limit — record the door and
  never open it. Read `robots.txt` before touching a host.

### Status (2026-10-17)

| piece | state |
|---|---|
| mount protocol family, local images | **built and run** (`hallway_mount.py`, `scan_offsets.py`) |
| mount protocol family, remote public filesystems | designed; here: `mount.cifs`, `smbclient`, `sshfs`, `mount.fuse` present; `mount.nfs`, `showmount`, `davfs2`, `curlftpfs`, `rclone`, `s3fs` absent |
| S3 prefix listing, FTP listing, API product listing, TAP/ObsCore census, FITS HDU walk | measured by hand, not yet code |
| HTTP index / sitemap.xml / tar / zip / HDF5 / SQLite / unknown-type backends | designed |
| node table, frontier queue, chunk-cycle runner, sitemap writers, crawl-plan derivation | designed (`references/surface-map.md`) |

Measured by hand: three S3 levels, one request each. `stpubdata/` has 11 subdirectories; `hst/` has two; `hst/public/` has at least
1 000 four-character shard prefixes (truncated). The walker learns the sharding scheme from the sample and stops; that scheme is what
the crawl plan needs.

## The hard wall

Nothing touches AppArmor: no listing, globbing, `cd`, reading or mounting of any path that contains `apparmor`, nor
`/sys/kernel/security`, `/sys/module/apparmor`, `/sys/fs/apparmor`, `/etc/apparmor*`, `/proc/*/attr`. `securityfs` is
never mounted. A process inside those directories cannot leave and has to be killed. sysfs is also effectively
infinite (symlink loops among `devices`, `bus`, `class`), so sysfs, proc, securityfs, debugfs, tracefs and cgroup are
read at depth 1, names only, symlinks never followed.

## Backend 1 — the mount protocol family: the procedure for a local image

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

`SKILL.md` (operating manual) · `references/surface-map.md` (node record, walls, chunk cycles, outputs, coin example) · `scripts/hallway_mount.py` (dry-run default, `--execute`, `--sysfs-mount`, `--selftest`) ·
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
