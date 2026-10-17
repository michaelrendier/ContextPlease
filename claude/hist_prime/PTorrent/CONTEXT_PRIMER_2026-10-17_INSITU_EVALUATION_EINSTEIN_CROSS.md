# Context primer, 2026-10-17: improving the in situ evaluation of datasets (starting pad: the most-cited Einstein cross)

## Why this exists (Cody, 2026-10-17)
His truck was burglarized and most of his telescope data is gone. He wants to improve PTorrent's **in situ evaluation of datasets** so that data can be re-obtained and evaluated where it lives, instead of depending on local copies. The engineering starting pad is to arrange **the most cited Einstein cross in the literature** as the first dataset family to evaluate.

## What is already in the repos (read these first)
* `PTorrent/spec/ptorrent-format-v1.md`: job type `evaluation` = "Data Transversal, apply evaluation terms (bin) to a structured dataset in situ"; output is a `.peval` file announced with an `EVALUATE` transaction. `output_format` includes `"peval"`, `"fits"`, `"hdf5"`.
* `PTorrent/spec/ptorrent-chain-v1.md`: `EVALUATE` (file_hash of the .peval, dataset_hash, terms_hash, peer_id). Two EVALUATE on the same dataset with the same terms merge; with different `terms_hash` they stay separate. Also `CLASSIFY`, `DISCLOSE`, etc. for dual-use data.
* `PTorrent/peval/*.peval` and `PTorrent/ptorrents/*_σface.ptorrent`: ten evaluations already exist (allsky_2mass, desi_dr1_bao, eht_blackhole, gaia_dr3, jwst_nirspec, planck_cmb, seti_breakthrough, sparc, vera_rubin, wmap_cmb). `PTorrent/evaluate_σface.py` is the evaluator. `PTorrent/android/corpus_list.json` lists the corpus jobs.
* `PTorrent/aggregators/`, `PTorrent/wiki/PTorrent-File-Spec.md`, `PTorrent/core/python/ptorrent_core/` (shared runtime, 24 modules).
* BulletCluster precedent: `BulletCluster/` (JWST program 4598 download, resumed 2026-06-30; HST/JWST optical, X-ray, radio, mm_sz subdirectories are symlinks into `/media/rendier/Datasets`); `ContextPlease/claude/hist_prime/BulletCluster/CLAUDE_PRIMER.md` (SN Refsdal "Einstein cross" in MACS J1149.5+2223, and the claim that an Einstein cross is L_(I|O)'s stationary set; time delays = values of L_(I|O)); `BulletCluster/Cleanup/ASSESSMENT.md` (ground telescopes cannot resolve 1 to 2 arcsecond crosses).
* The bulk-data volume is `/media/rendier/Datasets` (ext4, 469 GB, mirrors the repo layout).

## Open items (nothing below is decided or built)
1. **Which cross is "the most cited"?** The object conventionally called the Einstein Cross is the lensed quasar Q2237+0305 (Huchra's lens; lens galaxy ZW 2237+030). That is my recollection and still needs verifying. "Most cited" must be measured, not assumed: pull citation counts from ADS or INSPIRE for the candidates (Q2237+0305, the Refsdal cross, others) and record the query, the date and the counts.
2. **What was lost?** Cody has not yet listed which telescope datasets were in the truck. Ask for an inventory (instrument, target, dates, where copies may still exist: Datasets volume, phone pulls, cloud) before designing recovery.
3. **What "improve in situ evaluation" means concretely** (his words are the only spec): evaluate the dataset where it is hosted (archive API, no full download) and ship only the `.peval` result plus the terms. Decide which of the existing `.peval` fields are enough and what is missing for lensed-quasar light curves, astrometry of the four images and time delays.
4. Keep to the standing protocols: public archives only, Mozilla user agent on every request, a paywall or login page is a stop, every download logged in `ContextPlease/claude/references/INDEX.md` and `~/.clauderc_citations`.

## Not done in this session
No search, download or code for any of this. The primer only records the request and the existing assets.
