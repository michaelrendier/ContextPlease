"""export_plane.py: write the two-Lagrangian snapshots as plain JSON for the renderer.  Run from ThePlace:  python3 .../export_plane.py
Coordinates are normalised (brim radius 1, depth 1) so the two models share one chart; the physical scales are kept in the metadata."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace"))
from ValaQuenta.modules.witches_hat import maths as M
out_dir = os.path.dirname(os.path.abspath(__file__))
def dump(name, model):
    s = M.snapshot_plane(model, grid=60); R, D = s["brim_radius"], s["depth"]; top = s["hilltop"]
    z0 = s["E"]                                                         # height reference: V at the hilltop (the separatrix energy)
    d = {"name": name, "brim_radius": R, "depth": D, "hilltop": [top[0]/R, top[1]/R], "E": z0,
         "X": (s["X"]/R).tolist(), "Y": (s["Y"]/R).tolist(), "Z": ((s["Z"] - z0)/D).tolist(),
         "ring": (s["ring"]/R).tolist(), "ring_z": ((s["ring_z"] - z0)/D).tolist(),
         "paths": [{"aim": p["aim"], "x": (p["x"]/R).tolist(), "y": (p["y"]/R).tolist(), "z": ((p["z"] - z0)/D).tolist(), "W": (p["W"]/(R*np.sqrt(D))).tolist()} for p in s["paths"]]}
    json.dump(d, open(os.path.join(out_dir, "plane_%s.json" % name), "w")); print(name, "paths", len(d["paths"]), "hilltop", d["hilltop"])
dump("sm", M.lagrangian_sm())
dump("vap", M.lagrangian_vap(g=0.2, psi=(1.0, 0.0), convention="ssb"))
