"""P11 — emit the catalogue tables (from the live circle.py) and write the wiki pages."""
import sys, math, csv
sys.path.insert(0, "/home/rendier/Projects/ThePlace/GenerationalLineage")
from engine.toolsets import circle as C
pi = math.pi
g = lambda x: f"{x:.6g}"
names = [n for n in C.CONSTANTS if n != "i"]

def table(role, headers):
    out = ["| constant | " + " | ".join(headers) + " | π-lattice of r |", "|---|" + "---|" * (len(headers) + 1)]
    for n in names:
        row = C.descend(n, role)
        lat = C.pi_lattice(row["radius"]); lat = f"2^{lat[0]:g}·π^{lat[1]}" if lat else "—"
        vals = [row[h] for h in headers]
        out.append(f"| {n} | " + " | ".join(g(v) for v in vals) + f" | {lat} |")
    return "\n".join(out)
T_radius = table("radius", ["radius", "diameter", "circumference", "area"])
T_diam   = table("diameter", ["diameter", "radius", "circumference", "area"])
T_circ   = table("circumference", ["circumference", "radius", "diameter", "area"])
T_area   = table("area", ["area", "radius", "diameter", "circumference"])

# sigma tables from CSV
rows = list(csv.DictReader(open("p8_sigma_scan.csv")))
def sig_table(filter_fn):
    out = ["| circle value used as σ | σ | regime (engine's own labels) | G₂ = 2^−σ | Σ₂₀ p^−σ | σ−½ | 1−σ |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        if filter_fn(r["label"]):
            out.append(f"| {r['label']} | {r['sigma']} | {r['regime']} | {r['G_2=2^-sigma']} | {r['sum_G_20']} | {r['sigma-1/2']} | {r['1-sigma']} |")
    return "\n".join(out)
T_sig_r = sig_table(lambda l: l.startswith("r = ") and "half" not in l and not l.startswith("r = 1/2 (d=1)"))
T_sig_h = sig_table(lambda l: "half of diameter" in l)
T_sig_x = sig_table(lambda l: l.startswith(("d of", "C of", "A of")) and any(k in l for k in ("r=1/2", "r=1)", "r=1 ", "r=i", "r=pi", "r=d*")))

# the r = 1/2 ladder
lad = C.descend(0.5, "radius")
ladder = []
for lab, v in (("r = ½", lad["radius"]), ("d = 1", lad["diameter"]), ("A = π/4", lad["area"]), ("C = π", lad["circumference"])):
    rd = C.sigma_reading(v); ladder.append(f"| {lab} | {g(v)} | {rd['regime']} | {g(rd['G2'])} | {g(rd['coupling_sum'].real)} |")
LADDER = "| measure of the half-radius circle | σ | regime | G₂ | Σ₂₀ p^−σ |\n|---|---|---|---|---|\n" + "\n".join(ladder)
lad1 = C.descend(1.0, "radius"); l1 = []
for lab, v in (("r = 1", lad1["radius"]), ("d = 2", lad1["diameter"]), ("A = π", lad1["area"]), ("C = 2π", lad1["circumference"])):
    rd = C.sigma_reading(v); l1.append(f"| {lab} | {g(v)} | {rd['regime']} | {g(rd['G2'])} | {g(rd['coupling_sum'].real)} |")
LADDER1 = LADDER.split("\n")[0] .replace("half-radius","unit-radius")+ "\n|---|---|---|---|---|\n" + "\n".join(l1)

# l_p table
lp = ["| p | q (dual) | π_p | area | area ÷ π_p |", "|---|---|---|---|---|"]
for p in (1.0, 1.25, 1.5, C.PHI, 2 ** 0.5, 2.0, 3.0, math.e, 4.0, 5.0, math.pi, math.inf):
    c = C.lp_circle(p); lp.append(f"| {g(p)} | {g(c['q_dual'])} | {c['pi_p']:.6f} | {c['area']:.6f} | {c['area_over_pi_p']:.6f} |")
T_lp = "\n".join(lp)

open("tables.md", "w").write("\n\n".join(["## radius\n" + T_radius, "## diameter\n" + T_diam, "## circumference\n" + T_circ, "## area\n" + T_area,
                                           "## sigma radius\n" + T_sig_r, "## sigma half\n" + T_sig_h, "## sigma other\n" + T_sig_x, "## ladder\n" + LADDER, "## ladder1\n" + LADDER1, "## lp\n" + T_lp]))
import json; json.dump(dict(T_radius=T_radius, T_diam=T_diam, T_circ=T_circ, T_area=T_area, T_sig_r=T_sig_r, T_sig_h=T_sig_h, T_sig_x=T_sig_x, LADDER=LADDER, LADDER1=LADDER1, T_lp=T_lp), open("tables.json", "w"))
print(T_radius[:600]); print(); print(LADDER); print(); print(LADDER1); print(); print(T_sig_x)
