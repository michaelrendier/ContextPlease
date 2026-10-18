# Context primer, 2026-10-17 (written 2026-10-18): Huchra's Lens, the in situ read, the console UI, the hallway skill

**Supersedes** `CONTEXT_PRIMER_2026-10-17_INSITU_EVALUATION_EINSTEIN_CROSS.md` (it said "nothing built"; much now is). Read that one only for
the burglary background. Cody (Michael Rendier; authorship block in memory `user_profile.md`) moved on to the semantic orbweaver discussion at
the end of this conversation; come back here through this file.

## 0. What this conversation set out to do, in his order
1. A **console (curses) PTorrent**; percent-of-terminal layout; the NES-viewport skill for per-box scrollbars; BIOS-style navigation.
2. An **in situ layer** (its own tab) that evaluates data **where it lives**: `in_situ.ptorrent`, target **Huchra's Lens (Q2237+0305)**.
3. A **FourthAgePaper** "Ptychography, L_(I|O) Path of the Photon and Polarization Vector Field from data".
4. Then, in this order: `~/.clauderc_licenses`; the **walk-the-hallway** skill; the **Yellow Pages** naming; a **downloader** for the experiment.
Nothing in item 1 beyond design was built. Item 2's regular `.ptorrent`, probes and design are in. The `in_situ.ptorrent` itself is NOT written.

## 1. Standing constraints stated or confirmed here (do not re-ask)
* **In situ means no STAGING, not no reading.** A bounded chunk read into memory, evaluated and discarded, is allowed; a persistent copy is not.
  "Evaluation on MAST's servers" is the *point*; the honest reading is bytes stay at the archive, only requested ranges reach RAM; no compute runs
  at MAST/AWS except ADQL (TAP).
* **One dataset at a time.** Running two downloads on this machine crashes both.
* **No build until told** applies; the explicit "write a script", "build a directory", "put it in DRAFT_PAPER.md" instructions were the goes.
* Mozilla UA on every outbound request; public works only; paywall/login = stop. **Read `robots.txt` BEFORE touching a host** (I did not, for MAST and
  HEASARC; several dozen requests; recorded).
* **HARD WALL: never enter AppArmor directories** (securityfs never mounted; a process stuck there must be killed).
* **sysfs is effectively infinite** (symlink loops): depth 1, names only.
* The PTorrent **Phonebook is now "The Yellow Pages"**; every skill gets a wiki page (`hist_wiki/skills/`) at creation and per skill loaded in a session.
* Maths in Unicode, never LaTeX; code's own identifiers first; negatives are data points; tell him plainly when he is wrong (I did, on: the figure's
  vector field is deflection not polarization; the dark lobes are negative kappa; panel 2 is potential not photon counts; "partially correct" cannot
  come from a synthetic run).
* Two partitions: `/` (92 GB, 49 GB free, holds /tmp) and `/home` (856 GB, 137 GB free). Data goes to /home. SD card `/media/rendier/0123-4567/` (exFAT, 240 GB)
  holds a July copy of ThePlace incl. telescope data; `/media/rendier/Datasets` is GONE (stolen). `sudo -n` works.

## 2. The target and what the archives hold (queried 2026-10-17; files in `BulletCluster/huchras_lens/catalog/`)
Q2237+0305 = SIMBAD `QSO J2240+0321` = Einstein Cross = Huchra's Lens; RA 340.125975, Dec +3.3585083. Most-cited by measurement: Huchra et al. 1985 AJ 90 691
(OpenAlex 330, INSPIRE 174). z_lens 0.0394, z_src 1.695 (his catalog). HST: 4,720 target-named ObsCore rows; **3,121 per-exposure (level 2) products, 60.8 GiB**
(ACS 656, WFC3 1,424, WFPC2 387, NICMOS 468, WFPC 90, FOC 48, STIS 48); Chandra ACIS-S **40 ObsIDs, 835.5 ks**; ALMA Band 7 2021.1.00675.S (0.207", XX/YY);
ESO 494 frames (GROND 175, FORS1 117, ISAAC 70, SINFONI 48, X-shooter 48, GIRAFFE 26, FORS2 8, EMMI 2, ~3.1 GB). XMM and HST COS = coverage only (cannot
resolve). **JWST: none found** (36" census; web search found no program; the downloader's `jwst` stage queries 2'). **Polarization: NEGATIVE** (no HST polarizer
filters in 172 observations, no ESO polarimetry; finest = ALMA 0.207" XX/YY). VLA (Falco 1996) and ground archives (CFHT, NOT, Keck, Gemini, ...) = `pending`, unqueried.
Existing local data: `BulletCluster/lensing_validation/data.premigration/A5_q2237+0305` = 35 GB of **drizzled** HST (wrong class for ptychography; not on the SD card).

## 3. How to read in place (measured on one 168 MB WFC3/UVIS frame)
HTTP Range works at MAST (206) and the public S3 `stpubdata/hst/public/<first4>/<rootname>/<file>`; `nasa-heasarc` has `chandra/`. Latency 0.49 s/request; 4.9 MB/s
single stream, parallel adds no bandwidth; whole frame 34 s vs header walk + one coalesced 1 MiB block 2.3 s; coalesce gaps < latency x bandwidth ~ 2.4 MB;
all 3,121 frames: whole ~3.7 h vs ranged ~12 min. A 64x64 cutout probe used 85 requests / 258 KB (0.15 %). TAP services (MAST, HEASARC, ESO, ALMA, CADC) advertise only
TAP/VOSI/DALI; no SODA/DataLink seen. FTP anonymous answered only at ftp.eso.org (not data). Fornax Science Console and CANFAR = compute beside the data (per search results).
**robots.txt (generic agent):** mast.stsci.edu `Disallow: /`; HEASARC disallows /xamin and /vo/; ESO Crawl-delay 333 s; ALMA and CADC open. The PTorrent core's gate would
refuse MAST and HEASARC. **DECISION OPEN** (`PTorrent/in_situ/huchras_lens/ACCESS_OUTLINE.md` section 3): honour + use the buckets, ask the helpdesks, run inside a
platform, or a documented-API exception (not compliance).

## 4. What exists, where (commits pushed 2026-10-18)
| thing | where | commit |
|---|---|---|
| regular dataset `.ptorrent` (parses, preflight passes) | `PTorrent/ptorrents/einstein_cross_q2237_alltelescopes.ptorrent` | PTorrent `1ecd658` |
| in situ INPUT design, ACCESS_OUTLINE, probe + TAP helpers | `PTorrent/in_situ/huchras_lens/` | PTorrent `1ecd658` |
| OUTPUT dir: DRAFT_PAPER.md, censuses, probe logs, figure decode | `BulletCluster/huchras_lens/` | BulletCluster `3663ca8` |
| downloader `--huchra {jwst,pol,hst,all}` + 15 offline tests | `BulletCluster/lensing_validation/download_validation_targets.py`, `test_huchra_mode.py` | BulletCluster `3663ca8` |
| paper mirror | `FourthAgePapers/HuchrasLens/DRAFT_PAPER.md` (md5-identical to the BulletCluster copy) | FourthAgePapers `04e89e8` |
| walk-the-hallway skill, wiki page, Tesla protocol stubs | `ContextPlease/claude/skills/walk-the-hallway/`, `hist_wiki/skills/` | ContextPlease `b3f6f4d`, `3650108`, `03908e6`, and the commit that adds this primer |
| licences by work used | `~/.clauderc_licenses` (+ mirror) | the commit that adds this primer |
| record of the download scripts | `~/.clauderc_context_2` (2026-10-17 entry) | the same commit |

**Downloader facts:** extended IN PLACE; other modes untouched. One stage at a time; tiered products (1 per-exposure + pointing incl. `_spt/_jit/_jif/_asn`; 2 drizzled; 3 ramps opt-in);
data dir default `BulletCluster/huchras_lens/data` (git-ignored; must not be on `/`); global lock `~/.cache/one_download_at_a_time.pid`; `--respect-robots` refuses MAST;
`--geometry-pass` offline. **It has never been run against MAST** (its dry run queries MAST). Earth-orbit geometry computed: annual aberration 3.8"-20.7", differential
0.5 mas over the 5" cross but 16 mas across a chip, PSF-star parallax up to 0.5 px at 50 pc, Q2237 itself ~0.

## 5. The paper, the prediction, the figure
`DRAFT_PAPER.md`: claim = HYPOTHESIS (Cody): gravity is a shape, not a stuff; in-phase polarization across the four images would mean no scattering "stuff". Nothing evaluated.
**Prediction NOT RUN.** Model identified for the record: `VAPMIP/scaled_mind_eye_boxkite_kernel_monad.py` (class `MindEyeBoxKiteKernel`), sha256 `e9016cd8ac4570c9…`,
VAPMIP `147e29b`, ValaQuenta `fde11c1`; its outputs live on grammatical slots, with no mapping to an optical observable, and it throws static fibers (his Oct 13 correction:
the scaled kite must MOVE under G2). The attached photon-path figure (`~/Desktop/SpaceClaude/l_io_slingshot_map.png`) was run on **synthetic** data per Cody (its title says real;
generator not found). Decoded from pixels (`BulletCluster/huchras_lens/probe_log/figure_decode_*`): panel 2 = -psi, the double integral of panel 1 (corr(kappa, lap(-psi)) = -0.80
at coarse scale); 80 % of its variance is one large-scale gradient; the two dark-blue lobes are kappa ~ -0.19 (saturated): relative underdensity, so photons **spread** there
(mu ~ 1 + 2 kappa). The slingshot vector field = deflection alpha, NOT polarization. Cody's reading ("photon-path gradient partly confirms the hypothesis") is recorded as his reading.
Bullet lessons built in as required controls (nulls through the identical pipeline, generating code for every figure, pre-registration): `BulletCluster/Cleanup/RETRACTED.md`.

## 6. The console UI design (nothing built)
Existing base: `PTorrent/releases/curses/ptorrent_gui` (shell, wizard, settings; `common/geometry.py Rect.pct`); core `PTorrent/core/python/ptorrent_core`. Cody's decisions: extend, do not rewrite;
**layers = tabs across the top** (BIOS-style bar, one tab per layer); `\t` cycles focus between boxes WITHIN a layer; mouse wheel scrolls the box under the pointer; the BitTorrent layer and the
**In Situ layer** are separate; **pending -> "move to queue" key**; In Situ shows the **live queue on the right**, the selected item's detail (rung, bytes read, requests, errors) in the **bottom box**.
Each box is its own viewport (nes-viewport skill; windowed content needs a real total count: `Engine.items` has none yet). The BIOS file `~/Projects/BIOS/S301LAAS.215` is an old AMI Aptio capsule for a different
computer and could not give the legend; if he sends the key legend it becomes authoritative.

## 7. The hallway and Tesla
`walk-the-hallway` = a breadth-first, level-at-a-time **surface mapper for any public-facing collection** (his example: coin images), recording its own sitemap to power the real crawl, in resumable
threaded chunk cycles; the **mount door is itself a protocol family**. Built: local-image mount backend only (`hallway_mount.py`, `scan_offsets.py`). Everything else = design (`references/surface-map.md`).
Tied to **Tesla** (PtolemyDesktop): walker in Phaleron `WalkTheHalls`, protocols as `Tesla/Protocols/` (proposed; `references/tesla-protocol-stubs.md`; Tesla's `settings.json` `"stub": true` convention).
Huchra build set = walls + https/Range + s3 listing + FITS container + walker + crawl-plan (tap optional); all else stubs. Nothing in PtolemyDesktop was changed.

## 8. Open items, in the order they gate work
1. The **robots route** for MAST/HEASARC (section 3). 2. Is a Fornax/CANFAR run acceptable as "in place"? 3. Create `Tesla/Protocols/` now or later? HST first, `tap` deferred?
4. Page the full HST per-exposure manifest (the saved list is 2,239 of 4,720). 5. Query the pending telescopes (VLA, CADC/CFHT/Gemini, ...). 6. Stokes data: does any exist at all?
7. First J for a cutout and its controls; forward lens model for Q2237 (Kaiser-Squires does NOT apply to a quad lens); the dynamic Lagrangian with n(x); 2-D image ptychography (only a 1-D CMB ePIE exists).
8. The observable mapping + a moving scaled kite before any prediction is committed. 9. `jffs2`/`ubifs` classification fix and the pseudo-vs-network `nodev` split in `hallway_mount.py`.
10. `~/.clauderc_licenses` open items: PTorrent root GPL v3 vs core/curses LGPL-3.0-or-later; UD-EWT share-alike on the tagger; verify every `[MEMORY]` acknowledgement wording at its archive.

## 9. Traps
* MAST TAP's `OVERFLOW` flag appears even on `COUNT(*)`: a service quirk, not truncation. HEASARC returns BINARY VOTable (`votb.py` decodes it); its TAP rejects `FORMAT=csv`.
* `reg.g-vo.org`, `vao.stsci.edu`, `data-query.nrao.edu` did not answer from this machine: `unreachable` is not `absent`.
* The figure's title says "real shear"; Cody says synthetic; the module docstring says "no synthetic fallback". Do not call it real.
* My probes loaded kernel modules (8 -> 36 device-backed filesystem types) until reboot. Harmless; do not be surprised.
* Uncommitted work from OTHER sessions was left alone: FourthAgePapers `HyperindexingSystem/`, PtolemyDesktop Midline files, ValaQuenta `basile`.

## 10. Where to start next time
`PTorrent/in_situ/huchras_lens/README.md` and `ACCESS_OUTLINE.md`, then `BulletCluster/huchras_lens/DRAFT_PAPER.md` (sections 0, 3, 7, 8, 10, 12), then the skill `walk-the-hallway`
(`references/surface-map.md`, `tesla-protocol-stubs.md`). Ask Cody the robots question first; everything downstream of MAST depends on it.
