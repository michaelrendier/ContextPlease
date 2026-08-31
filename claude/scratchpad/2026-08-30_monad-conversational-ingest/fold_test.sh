#!/bin/bash
SB=/tmp/claude-1000/-home-rendier-Projects-ThePlace/03517d2c-e833-40d5-91fc-c8d9a44eff9b/scratchpad
PC=/home/rendier/Projects/ThePlace/VAPMIP/PtolC
pkill -9 -f 'ptolemy -d' 2>/dev/null; sleep 1
rm -f /tmp/monad.observe.fifo /tmp/ptf.sock
export HOME="$SB/fhome"; rm -rf "$HOME"; mkdir -p "$HOME/.ptolemy"
cp "$PC/ptolemy" "$HOME/"
cp "$PC/monad3_c.bin" "$SB/m3c_test.bin"
cp "$PC/monad3c.h" "$SB/"   # ptol.c -M needs the header next to it? no, embedded. skip.

export PTOLEMY_SOCKET=/tmp/ptf.sock
export PTOL_MONAD3C="$SB/m3c_test.bin"
export PTOL_REPACK_TAU=8

BEFORE=$(md5sum "$SB/m3c_test.bin" | cut -d' ' -f1)
BEFORE_MAGIC=$(head -c 8 "$SB/m3c_test.bin" | tr -d '\0')
echo "before: md5=$BEFORE magic=$BEFORE_MAGIC size=$(stat -c%s "$SB/m3c_test.bin")"

cd "$HOME"
./ptolemy -d -q -v -S /tmp/ptf.sock > d.out 2>&1 &
DPID=$!
sleep 2
kill -0 $DPID 2>/dev/null && echo "daemon up" || { echo DEAD; cat d.out; exit 1; }
grep -hE 'in-place fold target|repack timer' .ptolemy/logs/*

# burst of common English so most words hit existing rows; ~50KB > K*knee(41KB)
python3 - <<'PY'
import socket
S="/tmp/ptf.sock"
big=("the field learns from every word the wandering god speaks about time and "
     "space and number and the light that moves through the world we know ")*18
for i in range(60):
    s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM); s.connect(S)
    f=s.makefile("rwb",buffering=0)
    f.write(b"OBSERVE external burst%d\n" % i)
    f.write((big+"\n").encode()); f.write(b".\n")
    for l in iter(f.readline,b""):
        if l.strip()==b".": break
    s.close()
print("sent 60 turns")
PY
sleep 3

echo "--- daemon log: fold ---"
grep -hE 'repack firing|in-place fold|CSR rebuild' .ptolemy/logs/* || echo "(no fold logged)"

kill -TERM $DPID 2>/dev/null; wait $DPID 2>/dev/null

AFTER=$(md5sum "$SB/m3c_test.bin" | cut -d' ' -f1)
AFTER_MAGIC=$(head -c 8 "$SB/m3c_test.bin" | tr -d '\0')
echo "after:  md5=$AFTER magic=$AFTER_MAGIC size=$(stat -c%s "$SB/m3c_test.bin")"
[ "$BEFORE" != "$AFTER" ] && echo "CHANGED (in-place fold wrote to the file)" || echo "unchanged"
[ "$BEFORE_MAGIC" = "$AFTER_MAGIC" ] && echo "magic intact — still a MONAD3C store" || echo "MAGIC BROKEN"
# structural check: header size + a lookup via ptolemy -M if it supports it
"$HOME/ptolemy" -M the -S /tmp/ptf.sock 2>&1 | head -3 || true
rm -f /tmp/ptf.sock "$SB/m3c_test.bin"
