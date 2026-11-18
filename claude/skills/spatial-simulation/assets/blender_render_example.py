"""render_hat.py: Blender (4.0, Cycles, headless) scene of the Witch's Hat.
usage: blender -b -P render_hat.py -- OUTDIR N [turntable]
Layers:  grey-blue surface = V(r) hat (ESTABLISHED shape);  glowing ring = brim (the minimum);
         coloured curves = classical paths from the brim at energy E = 0, colour = accumulated action W (ESTABLISHED dynamics);
         translucent gold cone from the brim to a point above the hilltop = the author's 'cone of dynamic action' (THEORETICAL reading).
Everything is in units of the brim radius; the figure is the same for any size and depth of hat (see paper B)."""
import bpy, bmesh, json, math, sys, os
from mathutils import Vector
argv = sys.argv[sys.argv.index("--") + 1:]
outdir, n = argv[0], float(argv[1]); turn = len(argv) > 2
os.makedirs(outdir, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(here, "hat_paths_n%g.json" % n)))
ZS = 0.9                                              # height scale for V (depth 1)
V = lambda r: (2*r**n - n*r**2)/(n - 2)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.samples = 48; sc.cycles.use_denoising = False
sc.render.resolution_x, sc.render.resolution_y = 1280, 800
sc.world = bpy.data.worlds.new("w"); sc.world.use_nodes = True
sc.world.node_tree.nodes["Background"].inputs[0].default_value = (0.01, 0.012, 0.025, 1); sc.world.node_tree.nodes["Background"].inputs[1].default_value = 0.6

def mat(name, rgba, emit=0.0, alpha=1.0, rough=0.5):
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = rgba; b.inputs["Roughness"].default_value = rough
    if emit: b.inputs["Emission Color"].default_value = rgba; b.inputs["Emission Strength"].default_value = emit
    if alpha < 1: b.inputs["Alpha"].default_value = alpha; m.blend_method = "BLEND"
    return m

# --- surface from polar grid
R, NR, NT = 1.6, 90, 160
bm = bmesh.new(); verts = []
for i in range(NR + 1):
    r = R*i/NR
    row = []
    for j in range(NT):
        t = 2*math.pi*j/NT
        row.append(bm.verts.new((r*math.cos(t), r*math.sin(t), ZS*V(r))))
    verts.append(row)
for i in range(NR):
    for j in range(NT):
        bm.faces.new((verts[i][j], verts[i][(j+1) % NT], verts[i+1][(j+1) % NT], verts[i+1][j]))
me = bpy.data.meshes.new("hat"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("hat", me); sc.collection.objects.link(ob)
for p in me.polygons: p.use_smooth = True
ob.data.materials.append(mat("surf", (0.16, 0.2, 0.34, 1), rough=0.35))

def curve(points, radius, material, name):
    cu = bpy.data.curves.new(name, "CURVE"); cu.dimensions = "3D"; cu.bevel_depth = radius; cu.bevel_resolution = 2
    sp = cu.splines.new("POLY"); sp.points.add(len(points) - 1)
    for k, p in enumerate(points): sp.points[k].co = (p[0], p[1], p[2], 1)
    o = bpy.data.objects.new(name, cu); sc.collection.objects.link(o); o.data.materials.append(material); return o

# --- brim ring
brim = [(math.cos(2*math.pi*k/200), math.sin(2*math.pi*k/200), ZS*V(1.0) + 0.012) for k in range(201)]
curve(brim, 0.012, mat("brim", (1.0, 0.62, 0.12, 1), emit=9), "brim")

# --- paths coloured by action: a few colour bins by psi
pal = {0.02: (0.2, 1.0, 0.85), 0.06: (0.3, 0.9, 0.4), 0.12: (0.95, 0.95, 0.25), 0.2: (1.0, 0.55, 0.2), 0.3: (1.0, 0.3, 0.3), 0.45: (0.85, 0.3, 1.0)}
ms = {k: mat("p%g" % k, (*c, 1), emit=4) for k, c in pal.items()}
for k, p in enumerate(data["paths"]):
    pts = [(x, y, ZS*V(math.hypot(x, y)) + 0.015) for x, y in zip(p["x"], p["y"])]
    curve(pts, 0.0035, ms[p["psi"]], "path%d" % k)

# --- hilltop point and the author's cone
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035, location=(0, 0, ZS*V(0) + 0.02)); tip = bpy.context.object
tip.data.materials.append(mat("tip", (1, 1, 1, 1), emit=12))
W0 = 0.8619                                            # radial abbreviated action brim -> hilltop (n = 4); paper B
bpy.ops.mesh.primitive_cone_add(vertices=96, radius1=1.0, radius2=0.0, depth=W0, location=(0, 0, ZS*V(1.0) + W0/2))
cone = bpy.context.object; cone.data.materials.append(mat("cone", (1.0, 0.78, 0.25, 1), emit=0.4, alpha=0.12))

# --- light, camera
bpy.ops.object.light_add(type="AREA", location=(2.5, -3, 4)); L = bpy.context.object; L.data.energy = 900; L.data.size = 4
bpy.ops.object.empty_add(location=(0, 0, -0.1)); tgt = bpy.context.object
bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam
tr = cam.constraints.new("TRACK_TO"); tr.target = tgt; tr.track_axis = "TRACK_NEGATIVE_Z"; tr.up_axis = "UP_Y"
cam.data.lens = 40
def shot(az, el, dist, path):
    cam.location = (dist*math.cos(el)*math.cos(az), dist*math.cos(el)*math.sin(az), dist*math.sin(el) - 0.1)
    sc.render.filepath = path; bpy.ops.render.render(write_still=True)
if turn:
    for f in range(0, 72, 3):                          # 24 frames, 1/3 turn each 3 deg*... full turn over 72 steps of 5 deg
        shot(math.radians(-60 + 5*f/3*3), math.radians(32), 4.6, os.path.join(outdir, "turn_n%g_%03d.png" % (n, f//3)))
else:
    shot(math.radians(-55), math.radians(34), 4.6, os.path.join(outdir, "hat_n%g_iso.png" % n))
    shot(math.radians(-90), math.radians(8), 4.6, os.path.join(outdir, "hat_n%g_side.png" % n))
    shot(0, math.radians(89.5), 4.2, os.path.join(outdir, "hat_n%g_top.png" % n))
