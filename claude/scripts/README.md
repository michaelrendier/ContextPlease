# ContextPlease/claude/scripts

**theplace_sync.py** keeps the X1 Carbon's copy of ThePlace as a backup of the Yoga's (Cody, 2026-11-28). No network between the machines: the SD card is the link. Standard library plus `rsync`/`git`; `python3 test_theplace_sync.py` runs 27 checks on temporary folders.

The round trip (nothing is ever written on the machine that only reads; no deletes unless `--delete`; every replaced file is moved to a dated backup folder; `.venv/`, `TelescopeArchive/`, caches and `.git/` internals are not copied file by file):

1. **X1 (backup):** `python3 theplace_sync.py manifest --root ~/Projects/ThePlace --out /media/rendier/SDCard/sync/x1_manifest.json`
2. **Yoga (main):** `python3 theplace_sync.py delta --card /media/rendier/SDCard/sync --root ~/Projects/ThePlace`. It copies what is new or newer than the backup's manifest into `sync/delta/`, writes `delta_manifest.json` (sha256 of every file, conflicts, files that exist only on the backup), `repos_<host>.json` (branch, HEAD, ahead/behind of origin, dirty files, per repository) and `bundles/<repo>.bundle` for every repository with commits that are not on its origin.
3. **X1:** `python3 theplace_sync.py apply-card --card /media/rendier/SDCard/sync --local ~/Projects/ThePlace` (a dry run; add `--apply`). Hashes are checked first; a file newer on the X1 is a **conflict** and is left alone; bundles are fetched into `refs/remotes/yoga/*` so the X1's own branches never move.

Other commands: `repos [--fetch] [--json]`, `repos-compare A.json B.json`, `manifest [--hash]`, `compare A.json B.json`, and (only if an SSH path ever exists) `diff`/`pull --remote host:/path`.

**mirror** (`../scratchpad/2026-11-28_mirror_to_sdcard/mirror_theplace.sh`): the one-off full copy of ThePlace onto the card, smallest entries first, gentle on memory; writes `MIRROR_MANIFEST.txt`.
