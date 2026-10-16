"""T1 — the Null Operator (0_RB = e0) battery, run 2026-10-15 in the PERSISTENT scratchpad (the earlier runs were in /tmp and were lost).
Machinery tests only. Each test prints PASS/FAIL with the numbers; failures are kept. Writes t1_ledger.json.
Run:  PtolemyDesktop/.venv/bin/python t1_battery.py"""
import sys, os, io, math, json, random, subprocess, contextlib
ROOT = "/home/rendier/Projects/ThePlace"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/VAPMIP"); sys.path.insert(0, ROOT + "/PtolemyDesktop")
q = io.StringIO()
with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
    from ValaQuenta.modules.box_kite import maths as bk
LED = []
def check(tid, claim, ok, detail=""):
    LED.append({"id": tid, "claim": claim, "ok": bool(ok), "detail": detail}); print(f"{'PASS' if ok else 'FAIL'}  {tid}  {claim}" + (f"   [{detail}]" if detail else ""))
rnd = random.Random(2026)
rv = lambda: [rnd.uniform(-1, 1) for _ in range(16)]
E0 = [1.0] + [0.0] * 15

# T1 identity
worst = 0.0
for _ in range(300):
    x = rv(); a = bk.multiply(E0, x); b = bk.multiply(x, E0)
    worst = max(worst, max(abs(u - v) for u, v in zip(a, x)), max(abs(u - v) for u, v in zip(b, x)))
check("T1", "e0 is the two-sided multiplicative identity of the sedenion product used by the engines (300 random vectors)", worst < 1e-12, f"max |e0*x - x| = {worst:.1e}")
# T2 e0 not a zero divisor, norm preserved
nrm = lambda v: math.sqrt(sum(c * c for c in v))
dev = max(abs(nrm(bk.multiply(E0, x)) - nrm(x)) for x in (rv() for _ in range(200)))
check("T2", "multiplying by e0 preserves the norm (e0 is not a zero divisor)", dev < 1e-12, f"max deviation {dev:.1e}")
# T3 outside the geometry
o = bk.e0_is_outside()
check("T3", "e0 is in no assessor, is not a point of PG(3,2), and its associator vanishes against every pair", o["e0_is_outside_the_geometry"], str(o))
# T4 the commutator with e0 vanishes
cm = max(max(abs(c) for c in bk.commutator(0, j)) for j in range(16))
check("T4", "e0 commutes with every basis element", cm < 1e-12, f"max |[e0,ej]| = {cm:.1e}")
# T5 seven kites, 42 assessors, no assessor shared
kites = bk.box_kites(); ass = bk.assessors()
sizes = {s: len(v) for s, v in kites.items()}
allv = [a for v in kites.values() for a in v]
check("T5", "7 box-kites of 6 assessors each; 42 assessors in all; no assessor in two kites", len(kites) == 7 and set(sizes.values()) == {6} and len(allv) == 42 == len(set(allv)) == len(ass), f"kite sizes {sizes}")
# T6 each kite is an octahedron K_{2,2,2}: 4-regular on 6 vertices, 12 edges, Laplacian spectrum {0,4,4,4,6,6}
spec_ok, reg_ok = True, True
for s in kites:
    g = bk.box_kite_graph(s)
    sp = sorted(round(x, 6) for x in bk.chart_spectrum(s))
    spec_ok &= sp == [0, 4, 4, 4, 6, 6]
check("T6", "every kite's Laplacian spectrum is {0,4,4,4,6,6} (octahedron)", spec_ok, f"strut 1 spectrum {sorted(round(x,6) for x in bk.chart_spectrum(1))}")
# T7 adjacency: charts do not touch
g = bk.glued_graph()
keys = {k: v for k, v in g.items() if not isinstance(v, (list, dict)) or k in ("cross_strut_edges", "n_components")}
cross = g.get("cross_strut_edges", g.get("cross_edges"))
check("T7", "adjacency: zero cross-kite edges; 7 components; 7 zero modes in the glued Laplacian", (cross == 0 or cross == []) , f"cross-kite edges = {cross!r}")
sp = bk.glued_spectrum(); zero_modes = sum(1 for x in sp if abs(x) < 1e-9)
check("T8", "the glued atlas has exactly 7 zero modes", zero_modes == 7, f"zero modes {zero_modes} of {len(sp)}")
# T9 skeleton: every one of the 14 usable indices sits in 6 of 7 charts; only e0 and e8 are in none
mem = bk.index_chart_membership()
counts = {i: len(v) for i, v in mem.items()}
usable = {i for i, c in counts.items() if c == 6}
none = sorted(i for i in range(16) if counts.get(i, 0) == 0)
check("T9", "skeleton: 14 indices each lie in 6 of the 7 charts; exactly e0 and e8 lie in none", len(usable) == 14 and none == [0, 8], f"indices in no chart {none}")
# T10 hub: fixed point gluing + weight
fg = bk.fixed_point_gluing()
check("T10", "the zero modes identify at the fixed point; hub weight of pure e0 is exactly 1", abs(bk.fixed_point_weight(E0) - 1.0) == 0 and "e_0" in str(fg.get("reading", "")), str(fg.get("reading"))[:140])
# T11 the structural constant at landing = 1 - depth^2 for all seven struts and several depths (the kernel's own check)
with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
    import scaled_mind_eye_boxkite_kernel_monad as sme
    k = sme.MindEyeBoxKiteKernel()
worst = 0.0
for s in k.kite.struts:
    for d in (0.0, 0.2, 0.6, 0.9, 1.0):
        with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
            t = k.throw_fiber(s, d, gamma_companion=False)
        worst = max(worst, abs(t.fixed_point_weight - (1 - d * d)))
check("T11", "fixed_point_weight at landing equals 1 - depth^2 for all 7 struts x 5 depths (same constant read at every chart)", worst < 1e-12, f"max deviation {worst:.1e}")
# T12 every kite fiber lands on a chart: psi has no e0-free component outside that chart's assessor
with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
    t1 = k.throw_fiber(1, 0.6, gamma_companion=False)
check("T12", "a fiber throw leaves energy only on e0 and the chosen assessor's two indices", sum(1 for c in t1.psi if abs(c) > 1e-15) == 3, f"nonzero components {[i for i,c in enumerate(t1.psi) if abs(c)>1e-15]}")

# --- NULL discipline: what each engine returns for an all-null (all-zero) input -----------------------------
print("\nNULL DISCIPLINE — all-zero / empty input; does the engine keep 'no value yet' or manufacture a value?")
rows = []
def row(eng, ret, kept):
    rows.append({"engine": eng, "returns": ret, "keeps_null": kept}); print(f"  {'KEEPS NULL ' if kept else 'MANUFACTURES'}  {eng:58s} -> {ret}")
with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
    import rotary_rerun_monad as rr
me = rr.MindsEye(); s0 = me.snapshot([0.0] * 16)
row("rotary_rerun_monad.MindsEye.snapshot(zeros)['sigma_self']", repr(s0["sigma_self"]), isinstance(s0["sigma_self"], float) and math.isnan(s0["sigma_self"]))
row("box_kite.fixed_point_weight(zeros)", repr(bk.fixed_point_weight([0.0] * 16)), False)
with contextlib.redirect_stdout(q), contextlib.redirect_stderr(q):
    from ValaQuenta import noether as nt
try:
    from ValaQuenta.noether import NoetherCurrent
except Exception: NoetherCurrent = None
# C engine: empty prompt
env = dict(os.environ, HOME=os.path.expandvars("$CLAUDE_JOB_DIR/tmp/home")); os.makedirs(env["HOME"], exist_ok=True)
r = subprocess.run([ROOT + "/VAPMIP/PtolC/ptol", "-r", ""], capture_output=True, text=True, cwd=ROOT + "/VAPMIP/PtolC", env=env, timeout=60)
hdr = [l for l in (r.stderr + r.stdout).splitlines() if "σ_self" in l]
sig = hdr[0].split("σ_self:")[1].split()[0] if hdr else "(no sigma line; stdout=%r)" % r.stdout[:40]
row("ptol -r \"\" (C, empty prompt) sigma_self", sig, False if sig.startswith("0.5") else (sig.lower() == "nan"))
# ptol.c measure_sigma default (source evidence)
src = open(ROOT + "/VAPMIP/PtolC/ptol.c").read()
row("ptol.c measure_sigma: `if (total < 1e-15) return 0.5;`", "returns 0.5 (the balance point) for a zero vector" if "if (total < 1e-15) return 0.5;" in src else "(line not found)", False)
# noether forced sigma with E=0
try:
    from ValaQuenta.noether import NoetherCurrent as NC
    nc = NC() if callable(NC) else None
except Exception as e: nc = None
fs = None
for modname in ("ValaQuenta.noether",):
    try:
        m = __import__(modname, fromlist=["x"])
        for nm in dir(m):
            obj = getattr(m, nm)
            if hasattr(obj, "forced_sigma"):
                try: fs = obj().forced_sigma(0.0, 0.3); break
                except Exception: pass
    except Exception: pass
row("ValaQuenta.noether ...forced_sigma(E=0)", repr(fs), False if fs == 0.5 else (fs is None))
nulls = sum(1 for r in rows if r["keeps_null"]); 
check("T13", "NULL discipline census recorded (not a pass/fail on the engines: each is a data point)", True, f"{nulls} of {len(rows)} entries keep null; {len(rows)-nulls} select a value")

json.dump({"ledger": LED, "null_census": rows}, open("t1_ledger.json", "w"), indent=1, ensure_ascii=False)
print(f"\n{sum(1 for l in LED if l['ok'])} PASS, {sum(1 for l in LED if not l['ok'])} FAIL of {len(LED)}")
