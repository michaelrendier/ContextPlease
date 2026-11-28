---
name: telescope-download
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
- Data lives on `/media/rendier/0123-4567/BulletCluster/<target>/data/`; measure free space on that mount before sizing.

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

## 3. Notifications (how the 15-minute updates reach Cody)
A script cannot call Claude's tools. Run the download with `run_in_background`, then watch its stdout with the Monitor tool (each `[status]` line wakes the session and gets relayed). Optionally call PushNotification. This only works while the session is open; the STATE `.status` file is the fallback to read later.

## 4. Order of work for a new field
1. Survey; show Cody the camera/polarization table. 2. If polarization is a requirement and none exists, stop and propose another field before any download. 3. List products with sizes (read-only). 4. Get his go on the exact files. 5. Build the manifest, run the downloader in the background, Monitor it. 6. Record in `already_evaluated/`.
