#!/usr/bin/env bash
# migrate_datasets.sh — move DATA off /home onto the external, symlink back.
#
# THREE SAFETY LAYERS, in order, because Cody has lost unrecoverable files to
# exactly this operation:
#
#   1. rsync copies. The source is untouched.
#   2. FLUSH -- sync twice with a pause. rsync writes land in the PAGE CACHE,
#      and du/find on the destination read from that SAME cache. A verify can
#      therefore PASS on bytes that never reached the platter, and the delete
#      that follows is unrecoverable. Flush before believing anything.
#   3. VERIFY -- file count, byte total, AND a byte-for-byte cmp of the largest
#      file, read back from the destination after the flush.
#
# Only when all three pass is the source removed and replaced by a symlink.
# An interrupted run leaves the source intact and is safe to re-run.
# Code is never moved. Only directories holding observational data.
set -u
SRC=/home/rendier/Projects/ThePlace
DST=/media/rendier/Datasets/ThePlace
LOG=/tmp/migrate_datasets.log

PAIRS=(
  "BulletCluster/lensing_validation/data"
  "BulletCluster/optical/jwst"
  "BulletCluster/optical/hst"
  "BulletCluster/mm_sz/planck"
  "BulletCluster/radio/meerkat"
  "BulletCluster/xray/chandra"
  "DataSets"
)

log(){ echo "[$(date +%H:%M:%S)] $*" >> "$LOG"; }
count(){ find "$1" -type f 2>/dev/null | wc -l; }
bytes(){ du -sb "$1" 2>/dev/null | cut -f1; }
flush(){ log "  FLUSH: sync ..."; sync; sleep 3; sync; log "  FLUSH: done"; }

log "=== migration start ==="
for rel in "${PAIRS[@]}"; do
  s="$SRC/$rel"; d="$DST/$rel"
  [ -e "$s" ] || { log "SKIP $rel (absent)"; continue; }
  if [ -L "$s" ]; then log "SKIP $rel (already migrated)"; continue; fi

  sc=$(count "$s"); sb=$(bytes "$s")
  log "COPY $rel  ($sc files, $(numfmt --to=iec "$sb"))"
  mkdir -p "$(dirname "$d")"
  rsync -a --partial "$s/" "$d/" >>"$LOG" 2>&1
  rc=$?

  flush

  dc=$(count "$d"); db=$(bytes "$d")
  if [ "$rc" -ne 0 ] || [ "$sc" -ne "$dc" ] || [ "$sb" -ne "$db" ]; then
    log "  MISMATCH $rel  rc=$rc  files $sc vs $dc  bytes $sb vs $db"
    log "  SOURCE LEFT INTACT. Nothing deleted. Re-run to retry."
    continue
  fi

  big=$(find "$d" -type f -printf '%s %p\n' 2>/dev/null | sort -rn | head -1 | cut -d" " -f2-)
  if [ -n "$big" ]; then
    relbig=${big#"$d"/}
    if cmp -s "$big" "$s/$relbig"; then
      log "  BYTE-COMPARE OK on largest file: $relbig"
    else
      log "  BYTE-COMPARE FAILED on $relbig -- SOURCE LEFT INTACT"
      continue
    fi
  fi

  log "  VERIFIED $rel  ($sc files, $sb bytes) -> removing source, linking"
  rm -rf "$s" && ln -s "$d" "$s" && log "  LINKED $s -> $d"
done
flush
log "=== migration done, buffers flushed ==="
log "free /home:  $(df -h /home | tail -1 | awk "{print \$4}")"
log "free target: $(df -h "$DST" | tail -1 | awk "{print \$4}")"
