#!/usr/bin/env bash
# Telescope data move, 2026-11-04. COPY ONLY (no deletion here). One rsync at a time (old SATA drive).
# Phase 1 copy, phase 2 verify (checksum for the home sources that will later be removed; size+mtime for SD sources), phase 3 sync.
set -u
export LC_ALL=C.UTF-8
HOME_BC=/home/rendier/Projects/ThePlace/BulletCluster
SD=/media/rendier/0123-4567
TD="/media/rendier/Telescope Data/BulletCluster"
LOG="$TD/_move_2026-11-04"; mkdir -p "$LOG"
EC="$TD/EinsteinCrosses"; BC="$TD/BCData"
# label | source | destination | verify mode (sum = checksum, fast = size+mtime)
JOBS=(
"A2_SDSS_J1004|$HOME_BC/lensing_validation/data.premigration/A2_sdss_j1004+4112/|$EC/SDSS_J1004+4112/legacy_2026-08/|sum"
"A3_RXJ1131|$HOME_BC/lensing_validation/data.premigration/A3_rxj1131-1231/|$EC/RX_J1131-1231/legacy_2026-08/|sum"
"A4_HE0435|$HOME_BC/lensing_validation/data.premigration/A4_he0435-1223/|$EC/HE_0435-1223/legacy_2026-08/|sum"
"BC_scaffold|$SD/BulletCluster/bullet_cluster/|$BC/JWST_scaffold_level3/|fast"
"BC_jwst|$SD/ThePlace/BulletCluster/optical/jwst/|$BC/JWST/|fast"
"BC_hst|$SD/ThePlace/BulletCluster/optical/hst/|$BC/HST/|fast"
"BC_chandra|$SD/ThePlace/BulletCluster/xray/chandra/|$BC/Chandra/|fast"
"BC_meerkat|$SD/ThePlace/BulletCluster/radio/meerkat/|$BC/MeerKAT/|fast"
"BC_planck|$SD/ThePlace/BulletCluster/mm_sz/planck/|$BC/Planck/|fast"
"Dust_planckval|$SD/ThePlace/BulletCluster/lensing_validation/data/|$TD/Dust/planck_foreground_validation/|fast"
"Ctl_sparc_ifu|$SD/ThePlace/DataSets/Astrophysics/JWST/SPARC_IFU/|$TD/Galaxy_Controls/JWST_SPARC_IFU/|fast"
)
EXC=(--exclude=__pycache__ --exclude=.ipynb_checkpoints)
RS=(rsync -rlt --no-perms --no-owner --no-group --partial --info=stats2,name0 "${EXC[@]}")
say(){ echo "[$(date +%F\ %T)] $*" | tee -a "$LOG/status.log"; }
say "START free: $(df -h --output=avail "$TD" | tail -1)"
for j in "${JOBS[@]}"; do
  IFS='|' read -r lab src dst mode <<<"$j"
  [ -d "$src" ] || { say "SKIP $lab: source missing $src"; continue; }
  mkdir -p "$dst"
  say "COPY  $lab  ($(du -sh --apparent-size "$src" 2>/dev/null | cut -f1))"
  "${RS[@]}" "$src" "$dst" > "$LOG/$lab.copy.log" 2>&1; rc=$?
  say "COPY  $lab rc=$rc"
  [ $rc -eq 0 ] && echo "$lab" >> "$LOG/copied.ok"
done
say "PHASE 2: verify"
for j in "${JOBS[@]}"; do
  IFS='|' read -r lab src dst mode <<<"$j"
  [ -d "$src" ] || continue
  if [ "$mode" = sum ]; then f=(-rlnc); else f=(-rlnt); fi
  rsync "${f[@]}" --no-perms --no-owner --no-group "${EXC[@]}" --itemize-changes "$src" "$dst" > "$LOG/$lab.verify.log" 2>&1
  n=$(grep -c '^[<>c]' "$LOG/$lab.verify.log")
  nf_src=$(find "$src" -type f -not -path '*/__pycache__/*' | wc -l); nf_dst=$(find "$dst" -type f | wc -l)
  say "VERIFY $lab mode=$mode differing=$n files src=$nf_src dst=$nf_dst"
  [ "$n" -eq 0 ] && echo "$lab" >> "$LOG/verified.ok"
done
say "PHASE 3: sync"; sync; say "DONE (copy only; nothing deleted)"
