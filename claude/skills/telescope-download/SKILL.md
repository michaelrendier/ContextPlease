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
python3 telescope_download.py MANIFEST.json --state STATE.json [--min-free-gb 5] [--notify-secs 900]
```
MANIFEST = list of `{"url","dest","size"?,"sha256"?}`. MAST file URL: `https://mast.stsci.edu/api/v0.1/Download/file?uri=<dataURI>`.
- Streams in 8 MB chunks (memory bounded), writes `.part`, `os.replace` on success, sha256 recorded in STATE.
- Resume: rerun the same command; `.part` continues by HTTP Range (tested byte-identical), finished files are skipped.
- Sleep/suspend: a gap over 60 s between chunks triggers a reconnect; network errors retry with backoff up to `--retries`.
- Free-space guard stops (exit 2) before the card fills; a size/sha256 mismatch stops and is logged.
- Status line every `--notify-secs` (default 900 s = 15 min) to stdout and `STATE.json.status`.
- `TELESCOPE_DPRINT=1` turns on the dPrint feed.
- Tested 2026-10-20 on a small file: full fetch, then truncated `.part` resume, identical bytes.

## 3. Notifications (how the 15-minute updates reach Cody)
A script cannot call Claude's tools. Run the download with `run_in_background`, then watch its stdout with the Monitor tool (each `[status]` line wakes the session and gets relayed). Optionally call PushNotification. This only works while the session is open; the STATE `.status` file is the fallback to read later.

## 4. Order of work for a new field
1. Survey; show Cody the camera/polarization table. 2. If polarization is a requirement and none exists, stop and propose another field before any download. 3. List products with sizes (read-only). 4. Get his go on the exact files. 5. Build the manifest, run the downloader in the background, Monitor it. 6. Record in `already_evaluated/`.
