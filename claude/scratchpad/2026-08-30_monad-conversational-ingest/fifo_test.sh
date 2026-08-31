#!/bin/bash
set -e
SB=/tmp/claude-1000/-home-rendier-Projects-ThePlace/03517d2c-e833-40d5-91fc-c8d9a44eff9b/scratchpad
rm -rf "$SB/fh3"
mkdir -p "$SB/fh3/.ptolemy"
cp /home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptolemy "$SB/fh3/"
cd "$SB/fh3"

HOME="$SB/fh3" ./ptolemy -d -q -v -v > d.out 2>&1 &
DPID=$!
sleep 3

echo "daemon alive: $(kill -0 $DPID 2>/dev/null && echo yes || echo NO)"

# external turn
printf 'external\nThe wandering god tests the ingest pipe with real prose.\nA second sentence mentioning sedenions and zero divisors.\n.\n' > .ptolemy/monad.observe.fifo
# internal turn
printf 'internal\nAssistant prose about the harness daemon and the writer pen.\n.\n' > .ptolemy/monad.observe.fifo
sleep 2

# simulate drive-gone: hook falls back to spool, daemon drains on idle
printf 'external\nThis line went to the spool because the pipe was pretend-unmounted.\n.\n' >> .ptolemy/observe.spool
sleep 3

kill -TERM $DPID 2>/dev/null || true
wait $DPID 2>/dev/null || true

echo "=== log: observe/pipe/spool/drain ==="
grep -iE 'observe|pipe|spool|drain' .ptolemy/logs/* d.out 2>/dev/null || echo "(no matching log lines)"
echo
echo "=== spool file after run (should be empty/truncated) ==="
wc -c .ptolemy/observe.spool 2>/dev/null || echo "(gone)"
echo
echo "=== full daemon log tail ==="
tail -30 .ptolemy/logs/* 2>/dev/null
