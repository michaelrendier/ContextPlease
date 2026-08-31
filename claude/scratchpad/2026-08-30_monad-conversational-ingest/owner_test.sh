#!/bin/bash
set -e
SB=/tmp/claude-1000/-home-rendier-Projects-ThePlace/03517d2c-e833-40d5-91fc-c8d9a44eff9b/scratchpad
rm -rf "$SB/fh4"
mkdir -p "$SB/fh4/.ptolemy"
cp /home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptolemy "$SB/fh4/"
cd "$SB/fh4"

# a live process to "own" the pen as ptolemy
sleep 300 &
OWNER=$!
echo "ptolemy:$OWNER" > .ptolemy/monad3_c.writer.owner

HOME="$SB/fh4" ./ptolemy -d -q -v > d.out 2>&1 &
DPID=$!
sleep 3

echo "=== HEAR query still works with pen held by a bare Monad ==="
HOME="$SB/fh4" ./ptolemy -D "what is a sedenion" 2>&1 | head -5 || true
sleep 1

kill -TERM $DPID 2>/dev/null || true
wait $DPID 2>/dev/null || true
kill $OWNER 2>/dev/null || true

echo
echo "=== log: ownership / self-flush / checkpoint ==="
grep -iE 'held by a bare Monad|self-flush|checkpoint|NOT saving' .ptolemy/logs/* 2>/dev/null || echo "(none)"
echo
echo "=== now with a STALE owner pid (999999) ==="
echo "ptolemy:999999" > .ptolemy/monad3_c.writer.owner
HOME="$SB/fh4" ./ptolemy -d -q -v > d2.out 2>&1 &
DPID2=$!
sleep 3
kill -TERM $DPID2 2>/dev/null || true
wait $DPID2 2>/dev/null || true
grep -iE 'held by a bare Monad|saving checkpoint|NOT saving' .ptolemy/logs/* 2>/dev/null | tail -4
