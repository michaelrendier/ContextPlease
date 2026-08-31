#!/bin/bash
SB=/tmp/claude-1000/-home-rendier-Projects-ThePlace/03517d2c-e833-40d5-91fc-c8d9a44eff9b/scratchpad
pkill -9 -f 'ptolemy -d' 2>/dev/null
sleep 1
rm -f /tmp/monad.observe.fifo /tmp/pt.sock
export HOME="$SB/rthome"
rm -rf "$HOME"
mkdir -p "$HOME/.ptolemy"
cp /home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptolemy "$HOME/"
cd "$HOME"
export PTOL_REPACK_TAU=8
export PTOL_REPACK_CMD="printf 'FIRED %s\\n' \"\$(date +%s)\" >> $HOME/repack.marker"

./ptolemy -d -q -v -S /tmp/pt.sock > d.out 2>&1 &
DPID=$!
sleep 2
if ! kill -0 $DPID 2>/dev/null; then echo "daemon DEAD"; cat d.out; exit 1; fi
echo "daemon up (pid $DPID)"
grep -hE 'repack timer|listening' .ptolemy/logs/*

timeout 45 python3 "$SB/rt_client.py" /tmp/pt.sock
echo "client rc=$?"

echo "--- log: OBSERVE / repack / drain ---"
grep -hE 'daemon OBSERVE|repack firing|repack due|drained' .ptolemy/logs/* | tail -14
echo "--- marker ---"
cat "$HOME/repack.marker" 2>/dev/null || echo "  (none)"

kill -TERM $DPID 2>/dev/null
wait $DPID 2>/dev/null
echo "--- shutdown ---"
grep -hE 'final repack|saving checkpoint|NOT saving' .ptolemy/logs/* | tail -3
rm -f /tmp/pt.sock
