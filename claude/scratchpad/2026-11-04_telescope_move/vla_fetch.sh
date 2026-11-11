#!/usr/bin/env bash
# Waits for the telescope move to report DONE (copy + verify + sync), then fetches the two HE 0435 VLA blocks (anonymous NRAO link; no email sent).
set -u
TD="/media/rendier/Telescope Data/BulletCluster"
ST="$TD/_move_2026-11-04/status.log"
DEST="$TD/EinsteinCrosses/HE_0435-1223/VLA"
BASE=https://dl-dsoc.nrao.edu/anonymous/280928199/hbrc7nsu0rju6oa5rsutbhba8k
UA="${CLAUDE_UA:-Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0}"
BLOCKS=(12B-030.sb11649946.eb13791809.56226.34727347222 12B-030.sb13822707.eb13834180.56240.329852627314)
mkdir -p "$DEST"; LOG="$DEST/_download.log"
say(){ echo "[$(date +%F\ %T)] $*" | tee -a "$LOG"; }
say "waiting for move DONE"
until grep -q "DONE (copy only" "$ST" 2>/dev/null; do sleep 60; done
say "move DONE seen; free: $(df -h --output=avail "$DEST" | tail -1)"
for b in "${BLOCKS[@]}"; do
  say "FETCH $b"
  wget -c -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 --tries=20 --waitretry=30 --timeout=60 \
       -U "$UA" -P "$DEST" "$BASE/$b/" -o "$DEST/_wget_$b.log"; rc=$?
  say "FETCH $b rc=$rc"
  [ $rc -eq 0 ] || { say "STOP: wget failed on $b (logged, not repaired)"; exit 1; }
  # size check against the server, then gzip integrity of the measurement set
  f="$DEST/$b/$b.ms.tgz"
  want=$(curl -sIL -A "$UA" "$BASE/$b/$b.ms.tgz" | tr -d '\r' | awk 'tolower($1)=="content-length:"{v=$2} END{print v}')
  have=$(stat -c %s "$f")
  say "SIZE $b want=$want have=$have $([ "$want" = "$have" ] && echo OK || echo MISMATCH)"
  gzip -t "$f" && say "GZIP OK $b" || say "GZIP FAILED $b"
done
sync; say "ALL DONE (synced)"
