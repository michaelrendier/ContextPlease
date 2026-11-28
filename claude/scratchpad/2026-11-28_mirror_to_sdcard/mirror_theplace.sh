#!/usr/bin/env bash
# mirror_theplace.sh -- copy ALL of ThePlace onto the SD card, one top-level entry at a time, smallest first, so the card can move to the other machine.
# Gentle by design (the X1 has 7.5 GB RAM and a download and video running beside it): idle I/O priority, nice 19, a rate cap, a memory cap on the copy's
# cgroup when systemd-run is available (page cache counts against it, so the copy cannot starve the rest of the machine), a `sync` after every entry,
# a check of free memory before each entry and of free space on the card. Resumable (rsync is idempotent; finished entries are listed in .mirror_done).
# Nothing is deleted on either side. Read-only on the source.
#   ./mirror_theplace.sh            run (foreground)       ./mirror_theplace.sh start    background (nohup)
#   ./mirror_theplace.sh status     what is done           ./mirror_theplace.sh verify   dry-run comparison of the whole tree
# Environment: SRC (default ~/Projects/ThePlace)  DST (default /media/rendier/SDCard/ThePlace)  BWLIMIT_KB (30000 = 30 MB/s)  MEM_HIGH (700M)  MIN_AVAIL_MB (600)
set -u
SRC="${SRC:-$HOME/Projects/ThePlace}"; DST="${DST:-/media/rendier/SDCard/ThePlace}"
BWLIMIT_KB="${BWLIMIT_KB:-30000}"; MEM_HIGH="${MEM_HIGH:-700M}"; MIN_AVAIL_MB="${MIN_AVAIL_MB:-600}"
LOG="$DST/../.mirror.log"; DONE="$DST/../.mirror_done"; PIDF="$DST/../.mirror.pid"
note() { printf '%s %s\n' "$(date '+%F %T')" "$*" | tee -a "$LOG"; }
mkdir -p "$DST" 2>/dev/null || { echo "cannot create $DST (is the card mounted?)"; exit 1; }
touch "$DONE"

case "${1:-run}" in
  status) echo "done entries: $(wc -l < "$DONE")"; tail -n 5 "$LOG" 2>/dev/null; df -h "$DST" | tail -1
          [ -f "$PIDF" ] && kill -0 "$(cat "$PIDF")" 2>/dev/null && echo "running (pid $(cat "$PIDF"))" || echo "not running"; exit 0 ;;
  start)  nohup "$0" run >/dev/null 2>&1 & echo "started; $0 status"; exit 0 ;;
  resync) : > "$DONE"; echo "resync: every entry is checked again (rsync copies only what changed since the first pass)" ;;
  verify) note "verify: dry-run comparison (names, sizes, mtimes) of $SRC against $DST"
          ionice -c3 nice -n 19 rsync -ain --no-inc-recursive "$SRC/" "$DST/" 2>&1 | grep -v '^\.d' | tee -a "$LOG" | head -40
          note "verify finished: any line above is a difference (nothing above = identical)"; exit 0 ;;
esac

exec 9>"$DST/../.mirror.lock"; flock -n 9 || { echo "already running"; exit 4; }
echo $$ > "$PIDF"; trap 'rm -f "$PIDF"; exit 130' INT TERM
wrap=(ionice -c3 nice -n 19)
if command -v systemd-run >/dev/null && systemd-run --user --scope -q -p MemoryHigh="$MEM_HIGH" true 2>/dev/null; then
  wrap=(systemd-run --user --scope -q -p MemoryHigh="$MEM_HIGH" -p MemoryMax=1200M -p MemorySwapMax=0 "${wrap[@]}"); fi

# entries, smallest first (apparent size, bytes); top-level files are entries too
mapfile -t ENTRIES < <(cd "$SRC" && ionice -c3 nice -n 19 du -s --apparent-size -B1 -- * .[!.]* 2>/dev/null | sort -n | awk '{s=$1; $1=""; sub(/^ /,""); print s "\t" $0}')
note "mirror start: ${#ENTRIES[@]} top-level entries, source $SRC, destination $DST, cap ${BWLIMIT_KB} KB/s"
total=0; for e in "${ENTRIES[@]}"; do total=$((total + ${e%%$'\t'*})); done; note "total $((total/1000000000)) GB"
for line in "${ENTRIES[@]}"; do
  size="${line%%$'\t'*}"; name="${line#*$'\t'}"
  grep -qxF -- "$name" "$DONE" && continue
  while :; do avail=$(awk '/MemAvailable/ {print int($2/1024)}' /proc/meminfo); [ "$avail" -ge "$MIN_AVAIL_MB" ] && break; note "waiting: only ${avail} MB of memory available"; sleep 60; done
  free_b=$(df -B1 --output=avail "$DST" | tail -1); [ "$free_b" -gt $((size + 5000000000)) ] || { note "STOP: card has $((free_b/1000000000)) GB free, $name needs $((size/1000000000)) GB + 5"; exit 2; }
  note "copy: $name ($((size/1000000)) MB)"
  if [ -d "$SRC/$name" ] && [ ! -L "$SRC/$name" ]; then src="$SRC/$name/"; dst="$DST/$name/"; mkdir -p "$dst"; else src="$SRC/$name"; dst="$DST/"; fi
  "${wrap[@]}" rsync -aH --numeric-ids --partial --bwlimit="$BWLIMIT_KB" -- "$src" "$dst" >>"$LOG" 2>&1; rc=$?
  if [ $rc -eq 0 ] || [ $rc -eq 23 ] || [ $rc -eq 24 ]; then
    [ $rc -ne 0 ] && note "rsync code $rc for $name (some files could not be read or vanished; see the log)"
    sync; echo "$name" >> "$DONE"; note "done: $name"
  else note "FAILED: $name (rsync code $rc); stopping so the cause can be looked at"; exit 1; fi
done
# a manifest the other machine can check: every top-level repository's branch, HEAD, and whether it had uncommitted changes
{ echo "# ThePlace mirror manifest, $(date '+%F %T'), from $(hostname)"; for d in "$SRC"/*/; do n=$(basename "$d")
    if [ -d "$d/.git" ]; then echo "$n  $(git -C "$d" rev-parse --abbrev-ref HEAD 2>/dev/null)  $(git -C "$d" rev-parse --short HEAD 2>/dev/null)  dirty=$(git -C "$d" status --porcelain 2>/dev/null | grep -vc '^??')  untracked=$(git -C "$d" status --porcelain 2>/dev/null | grep -c '^??')"; fi; done; } > "$DST/MIRROR_MANIFEST.txt"
note "ALL ENTRIES COPIED. Run: $0 verify"; rm -f "$PIDF"
