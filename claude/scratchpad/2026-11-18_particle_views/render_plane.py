"""render_plane.py: Blender (4.0, Cycles, headless): the three parts of one particle as one object, for one Lagrangian.
usage: blender -b -P render_plane.py -- OUTDIR NAME      (NAME = sm | vap; reads plane_NAME.json)
Parts: (1) the hat = the surface z = V(beta1, beta2) (blue-grey);  (2) the brim = the ring of minima (orange glow);
       (3) the path of action = classical paths from the brim to the hilltop, coloured by aim offset, plus the author's cone (gold, translucent)
Views: iso, front (x-z), side (y-z), top (x-y).  Heights and radii are normalised: brim radius 1, depth 1."""
import bpy, bmesh, json, math, sys, os
argv = sys.argv[sys.argv.index("--") + 1:]; outdir, name = argv[0], argv[1]; os.makedirs(outdir, exist_ok=True)
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "plane_%s.json" % name)))
bpy.ops.wm.read_factory_settings(use_empty=True); sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.samples = 28; sc.cycles.use_denoising = False
sc.render.resolution_x, sc.render.resolution_y = 960, 640
sc.world = bpy.data.worlds.new("w"); sc.world.use_nodes = True
bg = sc.world.node_tree.nodes["Background"]; bg.inputs[0].default_value = (0.012, 0.014, 0.028, 1); bg.inputs[1].default_value = 0.7
def mat(n, rgba, emit=0.0, alpha=1.0, rough=0.45):
    m = bpy.data.materials.new(n); m.use_nodes = True; b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = rgba; b.inputs["Roughness"].default_value = rough
    if emit: b.inputs["Emission Color"].default_value = rgba; b.inputs["Emission Strength"].default_value = emit
    if alpha < 1: b.inputs["Alpha"].default_value = alpha; m.blend_method = "BLEND"
    return m
ZS = 0.9
X, Y, Z = D["X"], D["Y"], D["Z"]; n = len(X); x0, x1 = X[0][0], X[0][-1]; y0, y1 = Y[0][0], Y[-1][0]
def height(x, y):                                           # bilinear lookup on the exported grid (rows = y, columns = x)
    fx = (x - x0)/(x1 - x0)*(n - 1); fy = (y - y0)/(y1 - y0)*(n - 1)
    i = max(0, min(n - 2, int(fy))); j = max(0, min(n - 2, int(fx))); u = fx - j; v = fy - i
    return (Z[i][j]*(1-u)*(1-v) + Z[i][j+1]*u*(1-v) + Z[i+1][j]*(1-u)*v + Z[i+1][j+1]*u*v)
NR, NT, RMAX = 70, 160, 1.25; bm = bmesh.new(); rows = []
for i in range(NR + 1):
    r = RMAX*i/NR; rows.append([bm.verts.new((r*math.cos(2*math.pi*j/NT), r*math.sin(2*math.pi*j/NT), ZS*height(r*math.cos(2*math.pi*j/NT), r*math.sin(2*math.pi*j/NT)))) for j in range(NT)])
for i in range(NR):
    for j in range(NT): bm.faces.new((rows[i][j], rows[i][(j+1) % NT], rows[i+1][(j+1) % NT], rows[i+1][j]))
me = bpy.data.meshes.new("hat"); bm.to_mesh(me); bm.free(); ob = bpy.data.objects.new("hat", me); sc.collection.objects.link(ob)
for p in me.polygons: p.use_smooth = True
ob.data.materials.append(mat("surf", (0.16, 0.20, 0.34, 1), rough=0.35))
def curve(pts, r, m, nm):
    cu = bpy.data.curves.new(nm, "CURVE"); cu.dimensions = "3D"; cu.bevel_depth = r; cu.bevel_resolution = 2
    sp = cu.splines.new("POLY"); sp.points.add(len(pts) - 1)
    for k, p in enumerate(pts): sp.points[k].co = (p[0], p[1], p[2], 1)
    o = bpy.data.objects.new(nm, cu); sc.collection.objects.link(o); o.data.materials.append(m); return o
curve([(p[0], p[1], ZS*z + 0.012) for p, z in zip(D["ring"], D["ring_z"])] + [(D["ring"][0][0], D["ring"][0][1], ZS*D["ring_z"][0] + 0.012)], 0.012, mat("brim", (1.0, 0.62, 0.12, 1), emit=9), "brim")
aims = sorted({round(p["aim"], 3) for p in D["paths"]}); cols = [(0.85, 0.3, 1.0), (0.3, 0.55, 1.0), (0.3, 1.0, 0.85), (1.0, 0.9, 0.3), (1.0, 0.35, 0.3)]
ms = {a: mat("a%s" % a, (*cols[min(k, 4)], 1), emit=4) for k, a in enumerate(aims)}
for k, p in enumerate(D["paths"]):
    curve([(x, y, ZS*z + 0.015) for x, y, z in zip(p["x"], p["y"], p["z"])], 0.0035, ms[round(p["aim"], 3)], "p%d" % k)
ht = D["hilltop"]; bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035, location=(ht[0], ht[1], 0.02)); bpy.context.object.data.materials.append(mat("tip", (1, 1, 1, 1), emit=12))
W0 = max(p["W"][-1] for p in D["paths"])                                      # radial action to the hilltop, normalised
bpy.ops.mesh.primitive_cone_add(vertices=96, radius1=1.0, radius2=0.0, depth=W0, location=(0.0, 0.0, ZS*D["ring_z"][0] + W0/2))
c = bpy.context.object; c.data.materials.append(mat("cone", (1.0, 0.78, 0.25, 1), emit=0.4, alpha=0.10))
bpy.ops.object.light_add(type="AREA", location=(2.5, -3, 4)); L = bpy.context.object; L.data.energy = 900; L.data.size = 4
bpy.ops.object.empty_add(location=(0, 0, -0.1)); tgt = bpy.context.object
bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam
t = cam.constraints.new("TRACK_TO"); t.target = tgt; t.track_axis = "TRACK_NEGATIVE_Z"; t.up_axis = "UP_Y"; cam.data.lens = 35
def shot(az, el, dist, nm):
    cam.location = (dist*math.cos(el)*math.cos(az), dist*math.cos(el)*math.sin(az), dist*math.sin(el) - 0.1)
    sc.render.filepath = os.path.join(outdir, "%s_%s.png" % (name, nm)); bpy.ops.render.render(write_still=True)
shot(math.radians(-55), math.radians(50), 5.6, "iso"); shot(math.radians(-90), math.radians(4), 5.6, "front"); shot(0, math.radians(4), 5.6, "side"); shot(0, math.radians(89.5), 5.2, "top")
