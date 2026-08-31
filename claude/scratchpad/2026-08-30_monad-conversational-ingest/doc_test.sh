#!/bin/bash
SB=/tmp/claude-1000/-home-rendier-Projects-ThePlace/03517d2c-e833-40d5-91fc-c8d9a44eff9b/scratchpad
export MONAD_HARNESS_DIR=/home/rendier/Projects/ThePlace/VAPMIP
pkill -9 -f 'ptolemy -d' 2>/dev/null
sleep 1
rm -f /tmp/monad.observe.fifo /tmp/ptd.sock
export HOME="$SB/dhome"
rm -rf "$HOME"
mkdir -p "$HOME/.ptolemy"
cp /home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptolemy "$HOME/"
export PTOLEMY_SOCKET=/tmp/ptd.sock

"$HOME/ptolemy" -d -q -v -S /tmp/ptd.sock > "$HOME/d.out" 2>&1 &
DPID=$!
sleep 2
echo "daemon: $(kill -0 $DPID 2>/dev/null && echo up || echo DEAD)"

R="$HOME/repo"
mkdir -p "$R/docs/wiki"
cd "$R" || { echo "cd repo failed"; exit 1; }
git init -q
git config user.email t@t
git config user.name t
{
  echo "# Abrikosov Lattice"
  echo
  echo "The Riemann zeros arrange as an Abrikosov vortex lattice. Each zero is a flux"
  echo "tube through the critical line. The lattice spacing follows the pair correlation"
  echo "function that Montgomery derived and Dyson recognised."
} > docs/wiki/abrikosov.md
echo "plain readme prose about the engine and its resident field" > README.md
git add -A
git commit -q -m "docs: abrikosov + readme"

echo "--- committed ---"
git diff-tree --no-commit-id --name-only -r HEAD

echo "--- doc hook ---"
python3 /home/rendier/.claude/hooks/monad_doc_commit.py
echo "exit=$?"
sleep 2

echo "--- daemon log ---"
grep -hE 'OBSERVE|drained|document' "$HOME/.ptolemy/logs/"* 2>/dev/null || echo "(nothing)"
echo "--- d.out learn lines ---"
grep -E 'learn|Abrikosov|Montgomery' "$HOME/d.out" | head

kill -TERM $DPID 2>/dev/null
wait $DPID 2>/dev/null
rm -f /tmp/ptd.sock
