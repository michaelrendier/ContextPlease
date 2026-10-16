"""Q1 — the surface of the compiled Monad (ptol / ptolemy) and its Python twin on the six benchmark prompts.
Read-only against the engine: ptol runs with a scratch HOME (it writes papers to $HOME/.ptolemy); ptolemy -r -n never saves.
Records: outputs, wall time, run-to-run determinism (hash of two runs), binary/source checksums before and after."""
import subprocess, os, sys, time, json, hashlib, shutil
PC = "/home/rendier/Projects/ThePlace/VAPMIP/PtolC"
SC_HOME = os.path.expandvars("$CLAUDE_JOB_DIR/tmp/home")
PROMPTS = ["finger pointer", "what is a tree", "neutron generation in different reactor types",
           "good morning", "can you play the piano?", "the first reactor was built after neutrons were discovered"]
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
FILES = [f"{PC}/{n}" for n in ("ptol", "ptol.c", "ptolemy", "monad.c", "monad3_c.bin", "monad_grammar.bin", "monad_phonetic.bin")] + ["/home/rendier/Projects/ThePlace/VAPMIP/ptolemy_monad.py"]
before = {os.path.basename(f): sha(f) for f in FILES if os.path.exists(f)}
env = dict(os.environ, HOME=SC_HOME)
def run(cmd, inp=None, e=env, cwd=PC):
    t = time.perf_counter()
    r = subprocess.run(cmd, input=inp, capture_output=True, text=True, cwd=cwd, env=e, timeout=120)
    return (r.stdout + ("" if not r.stderr.strip() else "\n[stderr] " + r.stderr.strip())).strip(), (time.perf_counter() - t) * 1000
out = {"before": before, "prompts": PROMPTS, "rows": []}
for p in PROMPTS:
    row = {"prompt": p}
    for label, cmd in (("ptol", ["./ptol", p]), ("ptol_say", ["./ptol", "-say", p]), ("ptol_raw", ["./ptol", "-r", p])):
        a, ta = run(cmd); b, tb = run(cmd)
        if label == "ptol":   # strip the volatile paper path (timestamp)
            a = "\n".join(l for l in a.splitlines() if not l.startswith("paper:")); b = "\n".join(l for l in b.splitlines() if not l.startswith("paper:"))
        row[label] = {"out": a, "ms": round(min(ta, tb), 1), "deterministic": a == b}
    # REPL (real store; -n = never save)
    a, ta = run(["./ptolemy", "-r", "-n"], inp=p + "\n\n", e=os.environ.copy())
    row["ptolemy_repl"] = {"out": a, "ms": round(ta, 1)}
    out["rows"].append(row)
after = {os.path.basename(f): sha(f) for f in FILES if os.path.exists(f)}
out["after"] = after; out["unchanged"] = before == after
json.dump(out, open("q1_surface.json", "w"), indent=1, ensure_ascii=False)
for r in out["rows"]:
    print("\n>>>", r["prompt"])
    for k in ("ptol", "ptol_say", "ptolemy_repl"):
        print(f"  [{k}  {r[k]['ms']} ms{'  det' if r[k].get('deterministic') else ''}]", r[k]["out"].replace("\n", "\n      ")[:700])
    print(f"  [ptol_raw {r['ptol_raw']['ms']} ms det={r['ptol_raw']['deterministic']}] first line:", r["ptol_raw"]["out"].splitlines()[0])
print("\nengine files unchanged:", out["unchanged"])
