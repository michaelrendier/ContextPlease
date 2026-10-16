"""T2 — re-run the 2026-10-13 J_red/J_blue battery scripts (scratchpad 2026-10-13_jred_jblue_battery) and compare with the output recorded then."""
import subprocess, os, sys, re, difflib
SRC = "/home/rendier/Projects/ThePlace/ContextPlease/claude/scratchpad/2026-10-13_jred_jblue_battery"
PY = "/home/rendier/Projects/ThePlace/PtolemyDesktop/.venv/bin/python"
env = dict(os.environ, PYTHONHASHSEED="0")
for name, rec in (("jb", "output_jb.txt"), ("jgreen", "output_jgreen.txt"), ("anticomm", "output_anticomm.txt"), ("muscle2", "output_muscle2.txt"), ("trine", "output_trine.txt")):
    r = subprocess.run([PY, f"{SRC}/{name}.py"], capture_output=True, text=True, cwd=SRC, env=env, timeout=600)
    new = r.stdout.strip().splitlines(); old = open(f"{SRC}/{rec}").read().strip().splitlines()
    norm = lambda L: [re.sub(r"\d+\.\d+s|[0-9]+\.[0-9]+ ms", "T", l.rstrip()) for l in L]
    d = list(difflib.unified_diff(norm(old), norm(new), "recorded", "now", lineterm="", n=0))
    print(f"{name:9s} rc={r.returncode} lines recorded {len(old)} now {len(new)} -> {'IDENTICAL' if not d else str(len(d))+' diff lines'}")
    if d: print("   " + "\n   ".join(d[:8]))
    if r.returncode: print("   stderr:", r.stderr[-300:])
