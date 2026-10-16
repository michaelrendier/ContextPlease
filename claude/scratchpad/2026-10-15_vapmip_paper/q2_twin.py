"""Q2 — the Python twin: ptolemy_monad.PtolemyMonad.process_input on the six prompts (cold load, cold round, warm round, determinism),
plus a pure-Python re-implementation of ptol.c project()/measure_sigma/measure_gamma checked against `ptol -r` to 1e-9."""
import sys, time, json, math, subprocess, os, io, contextlib, hashlib
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP"); sys.path.insert(0, "/home/rendier/Projects/ThePlace/PtolemyDesktop")
PROMPTS = ["finger pointer", "what is a tree", "neutron generation in different reactor types", "good morning", "can you play the piano?", "the first reactor was built after neutrons were discovered"]
res = {}
t0 = time.perf_counter()
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    import ptolemy_monad as pm
    m = pm.PtolemyMonad()
res["load_s"] = round(time.perf_counter() - t0, 3)
def one(p):
    t = time.perf_counter()
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        r = m.process_input(p)
    return (getattr(r, "text", None) or getattr(r, "response", None) or str(r)), (time.perf_counter() - t) * 1000, r
rounds = []
for rnd in (1, 2):
    rows = []
    for p in PROMPTS:
        txt, ms, r = one(p); rows.append({"prompt": p, "reply": txt, "ms": round(ms, 2)})
    rounds.append(rows)
res["cold"] = rounds[0]; res["warm"] = rounds[1]
print("fields of response:", [a for a in dir(r) if not a.startswith("_")][:20])
for a, b in zip(rounds[0], rounds[1]):
    print(f"> {a['prompt']}\n   cold {a['ms']:8.2f} ms: {a['reply']}\n   warm {b['ms']:8.2f} ms: {b['reply']}   same={a['reply']==b['reply']}")
# ── projection parity with ptol.c
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
src = open("/home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptol.c").read()
import re
mm = re.search(r"static const int P\[16\]\s*=\s*\{([^}]*)\}", src) or re.search(r"P\[\s*16\s*\]\s*=\s*\{([^}]*)\}", src)
if mm: P = [int(x) for x in mm.group(1).replace("\n", " ").split(",") if x.strip()]
print("P from ptol.c:", P)
def project(s, k, sig):
    freq = 2*math.pi/P[k]; blue = 4 <= k <= 7 or 12 <= k <= 15
    return sum(c * i**(-sig) * (math.sin(freq*i) if blue else math.cos(freq*i)) for i, c in enumerate(s, 1))
def raw(prompt):
    o = subprocess.run(["./ptol", "-r", prompt], capture_output=True, text=True, cwd="/home/rendier/Projects/ThePlace/VAPMIP/PtolC", env=dict(os.environ, HOME=os.path.expandvars("$CLAUDE_JOB_DIR/tmp/home"))).stdout
    blocks = o.split("---\n"); return [float(x) for x in blocks[0].splitlines()[0:16]], ""  # CHASED: header 'eye:' is stderr; the first version sliced [1:17] and shifted every value by one
worst = 0
for p in PROMPTS:
    v, head = raw(p); s = p.encode()
    py = [project(s, k, 0.5) for k in range(16)]
    nrm = math.sqrt(sum(x*x for x in py)); py = [x/nrm for x in py]   # ptol.c divides by the L2 norm
    d = max(abs(a-b) for a, b in zip(v, py)); worst = max(worst, d)
    pr = sum(x*x for k, x in enumerate(py) if not (4 <= k <= 7 or 12 <= k <= 15)); pb = sum(x*x for k, x in enumerate(py) if (4 <= k <= 7 or 12 <= k <= 15))
    sig_self = pr/(pr+pb); gam = 2*sig_self-1
    print(f"parity {p[:30]:30s} max|C-Py|={d:.2e}  sigma_self py={sig_self:.10f} Gamma={gam:.10f}  C head: {head[:90]}")
res["projection_worst_abs_diff"] = worst
json.dump(res, open("q2_twin.json", "w"), indent=1, ensure_ascii=False)
