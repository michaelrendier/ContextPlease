---
name: yoga-telescope-download
description: >
  How Cody and Claude survey and download telescope data (MAST/JWST, NRAO VLA/ALMA): survey a field read-only first,
  check polarization before committing disk, then run the resumable one-at-a-time downloader with a 15-minute status
  line. Load before any telescope or archive download, field survey, or "does polarization exist for X" question.
---

# Telescope download

Built 2026-10-20 from the Huchra's Lens / Refsdal / Bullet Cluster downloads. Two scripts sit beside this file.

## Standing rules (Cody's, do not relax)
- Every outbound request carries a Mozilla user agent (`$CLAUDE_UA`; both scripts set it).
- ONE cross at a time, ONE download at a time. No new Bullet Cluster downloads (existing data kept).
- Discuss first; download only on his explicit go. Survey queries are read-only and need no go.
- NEVER send his email to NRAO or any service unless he says so explicitly. NRAO portal downloads need it, so stop there and ask.
- Failures are data: log them, do not repair. Public works only; a login or paywall page is a stop.
- Record every download under `BulletCluster/already_evaluated/<target>/` with the scripts and the re-fetch method.
- Data lives on `/media/rendier/0123-4567/BulletCluster/<target>/data/` **on the X1 Carbon**; on the **Yoga** it lives in `$PROJ/TelescopeArchive/<target>/data/` (section 2c). Measure free space on the actual destination before sizing.

## 1. Survey (read-only): `survey_field.py`
`python3 survey_field.py "<RA Dec>"` (a python with astroquery; do NOT use `python3 -I`, it hides site-packages).
Prints JWST programs and filters on the target, polarizer filters in MAST, and NRAO TAP rows by instrument, `pol_states`, program, wavelength and beam size (`s_resolution`).
- Polarization: JWST has no imaging polarimeter. Check MAST `filters` for POL (HST ACS has them). Radio full polarization = `pol_states` containing RL/LR (circular feeds) or XY/YX (linear). ALMA rows that show only `XX, YY` are limited.
- NRAO `access_estsize` is kB per row and overcounts (rows are scans/spectral windows). Use as scale, not as the download size.
- NRAO table is `tap_schema.obscore` (not `ivoa.obscore`) at `https://data-query.nrao.edu/tap/sync`.
- MAST sizes: sum `size` over unique filenames from `Observations.get_product_list`, split by `calib_level`; products overlap across levels, so never add all levels as one total.

## 2. Download: `telescope_download.py`
```
python3 telescope_download.py MANIFEST.json --state STATE.json [--min-free-gb 5] [--notify-secs 900] [--max-mbps 40] [--trust-server-size]
```
MANIFEST = list of `{"url","dest","size"?,"sha256"?}`. MAST file URL: `https://mast.stsci.edu/api/v0.1/Download/file?uri=<dataURI>`.
- Streams in 8 MB chunks (memory bounded), writes `.part`, `os.replace` on success, sha256 recorded in STATE.
- Resume: rerun the same command; `.part` continues by HTTP Range (tested byte-identical), finished files are skipped.
- Sleep/suspend: a gap over 60 s between chunks triggers a reconnect; network errors retry with backoff up to `--retries`.
- Free-space guard stops (exit 2) before the card fills; a size/sha256 mismatch stops and is logged.
- Status line every `--notify-secs` (default 900 s = 15 min) to stdout and `STATE.json.status`.
- `TELESCOPE_DPRINT=1` turns on the dPrint feed.
- Tested 2026-10-20 on a small file: full fetch, then truncated `.part` resume, identical bytes.

`--max-mbps N` (added 2026-11-27) caps the average rate in megabit/s: use it, with `run_download.sh` (nice, ionice idle), whenever the machine is in use (Cody watching video). For NRAO request products (directory index + SHA1SUMS, per-request keys) there is also `BulletCluster/pending/nrao_downloads/crab_fetch/nrao_fetch.py` with `fetch_crab.sh`, tested against the live GBT links.

### 2b. Fault tolerance (added 2026-11-14, after the 2026-11-13/14 incidents)
Incidents that taught it: an older SATA drive fell and was not unmounted; the USB 3 controller died on resume from a lid-close suspend (`xhci_hcd: HC died`), taking the drive with it; `gvfsd-google` (the desktop's Google-Drive mount) was OOM-killed three times, once at 5 GB resident; the machine did not reboot (up 5 days), it suspended and its USB bus reset.
`telescope_download.py` now: writes STATE atomically (temp + fsync + rename); fsyncs each finished file and its directory; discards the last 16 MB of a `.part` on resume; with `--require-mount PATH` **waits and never writes** when the drive is not mounted (no ghost directory on the internal disk); treats a dropped or truncated connection as retryable (a short read is not a size mismatch); waits for the network with back-off without using up retries; pauses while `STATE.json.PAUSE` exists (`touch` / `rm`); exits 130 on SIGINT/SIGTERM after saving state; caps address space (`--max-mem-mb`, default 1536) and runs at nice 10 / idle I/O priority. Tested with a local server (SIGTERM mid-file then resume, mount guard, pause file, server killed and restarted: all passed, hashes equal).
`run_download.sh MANIFEST STATE MOUNT LOG [args]` runs it under `systemd-inhibit` (sleep, idle, lid switch) so a lid-close cannot suspend the machine mid-download.
`verify_downloads.py MANIFEST STATE` checks every file (exists, manifest size, sha256 equal to the recorded one), checkpointed, read-only, low priority; it repairs nothing.
Do not use the GNOME Google-Drive mount for large files (it buffers in memory); download the Drive zips in the browser or with `rclone`.

## 2c. Machine budgets: know which machine you are on (`$CLAUDE_MACHINE`, set in ~/.clauderc)
Everything above this section was built on the **X1 Carbon** (external card at `/media/rendier/0123-4567`). The **Yoga** (added 2026-11-28, Yoga Claude) is the telescope **satellite archive**: it downloads what the X1 is not already holding; the X1's external drive gets plugged in here later for evaluation.

| | X1 Carbon | Yoga |
|---|---|---|
| CPU | Core i7 | Core Ultra 7 **155U** (Meteor Lake, 15 W U-series): 12 cores = 2 P (hyperthreaded) + 8 E + 2 LP-E, 14 threads; measured 2026-11-28, `ContextPlease/claude/yoga/machine/inxi_full_2026-11-28.txt`. A 15 W part throttles under sustained all-core load |
| RAM / swap | (see the X1's own notes) | 16 GB / 8 GB, measured 2026-11-28 (`free -g`: 15 total, 3 used, 11 available at idle with one Claude session; re-measure before sizing) |
| Data root | external card, `--require-mount` | internal NVMe: `$PROJ/TelescopeArchive/<target>/data/` (about 828 GB free on 2026-11-27) |
| Shells | ~22 concurrent seen | as many as needed; each one costs memory, so count them in the budget |

**Yoga memory budget (16 GB), PLANNED, measure and correct it:** desktop + Firefox about 4 GB; each Claude Code session about 0.5–1 GB (unmeasured); the kernel page cache takes whatever is free, so leave it alone. That leaves about 9–10 GB for work:
- **Downloader:** one at a time (standing rule), `--max-mem-mb 1536` (the default) is plenty: it streams 8 MB chunks.
- **Evaluation / FITS work:** ≤ 6 GB per process, at most one heavy job beside a download. Open FITS with `memmap=True`; never `np.load` a whole cube; process by HDU/plane/chunk.
- **Swap is a buffer, not capacity.** 8 GB of swap on NVMe keeps the desktop alive through a spike; a job that lives in swap is a job that is too big, so split it.
- **Contain every long job in its own cgroup**, so the OOM killer takes THAT job, not the desktop or Claude Code:
  `systemd-run --user --scope -p MemoryMax=6G -p MemorySwapMax=1G -p CPUWeight=50 -- <cmd>`.
  Prefer this to `--max-mem-mb` for numpy/astropy jobs: `RLIMIT_AS` counts virtual address space, and BLAS thread pools and mmap reserve far more than they touch (CHECK on this box before relying on either).
- **Threads (Yoga, measured topology):** only 2 P-cores, so a P-core cap would starve a job. Set `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=8` for one heavy job (the E-cores), leaving the 2 P-cores (4 threads) and the 2 LP-E cores for the desktop, Claude Code and the downloader; 4 each if two heavy jobs share the box. Never `nproc` (14).
- **Disk guard (measured with lsblk 2026-11-28; an earlier draft of this line wrongly said / and /home were one partition):** `/` = `nvme0n1p2`, 55.9 GB (31 GB free), which also holds `/tmp`; `/home` = `nvme0n1p4`, 889.6 GB; swap = `nvme0n1p3`, 7.5 GB. The archive fills `/home` only, but `/home` also holds every repo, every `.venv`, the Android SDK and Claude's own files, so keep `--min-free-gb 40` on Yoga. Never write data to `/tmp` (it is on the small `/` partition).
- **No mount guard on internal disk:** `--require-mount` is for the external card; on Yoga point dest at `$PROJ/TelescopeArchive/`. When the X1's external drive is plugged in here, use `--require-mount` again for anything written to it.

## 2d. Shells that must outlive Claude Code ("disown")
When Cody says to disown a download, do NOT use `nohup … &` / `disown` (no memory limit, no log, it dies with logout, and it is hard to find again). Use a transient **systemd user unit**:
```
loginctl show-user rendier -p Linger    # Linger=yes on the Yoga since 2026-11-28 (user units survive logout); else: sudo loginctl enable-linger rendier
systemd-run --user --unit=tdl-<target> -p MemoryMax=2G -p MemorySwapMax=512M -p Nice=10 -p IOSchedulingClass=idle \
  --working-directory="$PROJ/TelescopeArchive/<target>" -- \
  bash run_download.sh MANIFEST.json STATE.json "" LOG.txt --min-free-gb 40 [--max-mbps N]
systemctl --user status tdl-<target>    # state;  journalctl --user -u tdl-<target> -f   # live log
systemctl --user stop tdl-<target>      # SIGTERM -> the downloader saves state and exits 130; rerun resumes
```
It survives Claude Code exiting and has a memory cap, a log and a name. Watch it from a session with Monitor on `journalctl --user -u tdl-<target> -f` or the STATE `.status` file. Record every disowned unit's name in the target's `already_evaluated/` README so the next session can find it. (`run_download.sh`: pass "" as the mount on internal disk; the guard is then omitted. Fixed 2026-11-28.)

## 2e. Look entries up by the FULL dest path (learned 2026-11-28)
JWST level-3 basenames repeat across programs (`jw01939-o001_t001_nircam_clear-f212n_i2d.fits` and `jw09257-o001_t001_nircam_clear-f212n_i2d.fits` differ only in the program number). A lookup by basename or substring returned program 1939's 1.66 GB size for program 9257's 14.0 GB file and raised a false anomaly. Key manifest and state records by the complete `dest` path, never by a name fragment.

## 3. Notifications (how the 15-minute updates reach Cody)
A script cannot call Claude's tools. Run the download with `run_in_background`, then watch its stdout with the Monitor tool (each `[status]` line wakes the session and gets relayed). Optionally call PushNotification. This only works while the session is open; the STATE `.status` file is the fallback to read later.

## 4. Order of work for a new field
1. Survey; show Cody the camera/polarization table. 2. If polarization is a requirement and none exists, stop and propose another field before any download. 3. List products with sizes (read-only). 4. Get his go on the exact files. 5. Build the manifest, run the downloader in the background, Monitor it. 6. Record in `already_evaluated/`.
