#!/bin/bash
set -e
SB=/tmp/claude-1000/-home-rendier-Projects-ThePlace/03517d2c-e833-40d5-91fc-c8d9a44eff9b/scratchpad
export HOME="$SB/fh5"
rm -rf "$HOME"
mkdir -p "$HOME/.ptolemy"
cp /home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptolemy "$HOME/"
cd "$HOME"

export PTOL_REPACK_TAU=8
export PTOL_REPACK_CMD="echo fired-$(date +%s) >> $HOME/repack.marker"
export SOCK="$HOME/.ptolemy/ptolemy.sock"

./ptolemy -d -q -v > d.out 2>&1 &
DPID=$!
sleep 3
echo "daemon alive: $(kill -0 $DPID 2>/dev/null && echo yes || echo NO)"
grep -hE 'repack timer|daemon listening' .ptolemy/logs/*

status() {
python3 - <<PY
import socket
s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM); s.connect("$SOCK")
f=s.makefile("rwb",buffering=0); f.write(b"STATUS\n")
while True:
    l=f.readline()
    if not l or l.strip()==b".": break
    t=l.decode().rstrip()
    if "repack" in t: print("  STATUS:", t)
s.close()
PY
}

echo "--- before input ---"; status

python3 - <<PY
import socket
big=("The wandering god speaks a long sentence about sedenions zero divisors "
     "box kites and the critical line. ")*20
for i in range(12):
    s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM); s.connect("$SOCK")
    f=s.makefile("rwb",buffering=0)
    f.write(b"OBSERVE external\n"); f.write((big+"\n").encode()); f.write(b".\n")
    while True:
        l=f.readline()
        if not l or l.strip()==b".": break
    s.close()
print("sent 12 big external turns (~%d KiB)" % (len(big)*12//1024))
PY

echo "--- right after burst ---"; status
echo "--- wait 4s for an idle sweep to run maybe_repack() ---"; sleep 4
grep -hE 'repack firing|repack due' .ptolemy/logs/* || echo "  (no fire logged)"
echo "--- marker ---"; cat "$HOME/repack.marker" 2>/dev/null || echo "  (no marker)"
echo "--- after fire ---"; status
echo "--- idle-bleed check: wait 20s (>2*TAU), urgency should collapse ---"; sleep 20; status

kill -TERM $DPID 2>/dev/null || true
wait $DPID 2>/dev/null || true
echo "--- shutdown ---"
grep -hE 'final repack|saving checkpoint|NOT saving' .ptolemy/logs/* | tail -3
