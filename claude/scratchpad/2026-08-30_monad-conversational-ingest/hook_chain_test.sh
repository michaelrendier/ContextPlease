#!/bin/bash
SB=/tmp/claude-1000/-home-rendier-Projects-ThePlace/03517d2c-e833-40d5-91fc-c8d9a44eff9b/scratchpad
export MONAD_HARNESS_DIR=/home/rendier/Projects/ThePlace/VAPMIP
HOOK=/home/rendier/.claude/hooks/monad_observe.py
DOCHOOK=/home/rendier/.claude/hooks/monad_doc_commit.py
pkill -9 -f 'ptolemy -d' 2>/dev/null; sleep 1
rm -f /tmp/monad.observe.fifo /tmp/ptc.sock
export HOME="$SB/chome"; rm -rf "$HOME"; mkdir -p "$HOME/.ptolemy"
cp /home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptolemy "$HOME/"
export PTOLEMY_SOCKET=/tmp/ptc.sock
cd "$HOME"

./ptolemy -d -q -v -S /tmp/ptc.sock > d.out 2>&1 &
DPID=$!
sleep 2
kill -0 $DPID 2>/dev/null && echo "daemon up" || { echo DEAD; cat d.out; exit 1; }

# --- external turn via the hook ---
printf '{"session_id":"S1","prompt":"Explain how the sedenion zero divisor annihilation relates to the Riemann critical line, using the box kite and the Two Trees framing."}' \
  | python3 "$HOOK" external
echo "external hook exit=$?  pairfile=$(cat "$HOME/.ptolemy/.pair-S1" 2>/dev/null)"

# --- synthetic transcript with a last assistant turn (text + thinking blocks) ---
TS="$HOME/transcript.jsonl"
cat > "$TS" <<'JSONL'
{"type":"user","message":{"role":"user","content":"Explain the sedenion zero divisor."}}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"thinking","thinking":"internal reasoning that must NOT be ingested, mentioning secret scaffolding"},{"type":"text","text":"The zero divisor sits where the sedenion product collapses to zero. In box kite terms it is an Assessor pair whose strut annihilates. Mapped onto the critical line, that collapse is the sigma equals one half balance point. The Two Trees read it as Telperion feeding Laurelin."}]}}
JSONL

printf '{"session_id":"S1","transcript_path":"%s"}' "$TS" | python3 "$HOOK" internal
echo "internal hook exit=$?  pairfile-after=$(cat "$HOME/.ptolemy/.pair-S1" 2>/dev/null || echo consumed)"

sleep 1
echo "--- daemon log: OBSERVE + pair ---"
grep -hE 'daemon OBSERVE|daemon pair' .ptolemy/logs/* 2>/dev/null
echo "--- STATUS pairs line ---"
python3 - <<PY
import socket
s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM); s.connect("/tmp/ptc.sock")
f=s.makefile("rwb",buffering=0); f.write(b"STATUS\n")
for l in iter(f.readline,b""):
    if l.strip()==b".": break
    if b"pairs" in l or b"repack" in l: print("  "+l.decode().rstrip())
s.close()
PY
echo "--- pairs.jsonl ---"; cat .ptolemy/pairs.jsonl 2>/dev/null
echo "--- thinking block leaked? (should be empty) ---"
grep -c "internal reasoning" .ptolemy/logs/* d.out 2>/dev/null | grep -v ':0' || echo "  clean — no thinking leaked"

# --- doc commit hook ---
echo
echo "=== doc-commit hook ==="
R="$HOME/repo"; mkdir -p "$R/docs"; cd "$R"; git init -q; git config user.email t@t; git config user.name t
cat > docs/wiki-page.md <<'MD'
# The Abrikosov Lattice

The Riemann zeros arrange as an Abrikosov vortex lattice. Each zero is a flux tube
through the critical line. The lattice spacing follows the pair correlation.

```
sigma = 1/2   <- dropped fenced block
```

| col | dropped table |
MD
git add -A; git commit -q -m "add wiki page"
python3 "$DOCHOOK"
echo "doc hook exit=$?"
sleep 1
grep -hE 'daemon OBSERVE document' "$HOME/.ptolemy/logs/"* 2>/dev/null || echo "  (no document OBSERVE logged)"

kill -TERM $DPID 2>/dev/null; wait $DPID 2>/dev/null
rm -f /tmp/ptc.sock
