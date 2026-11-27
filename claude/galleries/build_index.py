#!/usr/bin/env python3
"""build_index.py (2026-11-21): writes ThePlace/galleries/index.html, the single entry point to every gallery.
The page is static; at load time it FETCHES each image gallery's page (same origin, served from ThePlace root) and reads that gallery's embedded data to build one searchable catalog.
So the index file itself holds no image data: the proprietary VAPMIP galleries are linked and read at run time, never copied into it.
usage: python3 build_index.py   (then ./serve_all.sh)"""
import os, sys, json, base64
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import contact; ROOT = os.path.expanduser("~/Projects/ThePlace"); OUT = os.path.join(ROOT, "galleries")
fav = open(os.path.join(HERE, "favicon_datauri.txt")).read().strip()
IMG = [("Abrikosov Atlas Gallery", "AbrikosovTree/image_gallery/Abrikosov_Atlas_Gallery.html", 8767, False),
       ("Ainulindalë Gallery", "Ainulindale/image_gallery/Ainulindale_Gallery.html", 8768, False),
       ("Riemann–Fermat Atlas Gallery", "RiemannHypothesisProof/image_gallery/Riemann_Fermat_Atlas_Gallery.html", 8769, False),
       ("Generational Lineage Gallery", "GenerationalLineage/image_gallery/Generational_Lineage_Gallery.html", 8770, False),
       ("Sedenion Spectral Relativity Gallery", "SedenionSpectralRelativity/image_gallery/Sedenion_Spectral_Relativity_Gallery.html", 8771, False),
       ("VAPMIP Gallery", "VAPMIP/image_gallery/VAPMIP_Gallery.html", 8772, True),
       ("Holcus 16D Paths Gallery", "VAPMIP/holcus_paths_gallery/Holcus_16D_Paths_Gallery.html", 8773, True)]
INTER = [("Scaffold Gallery", "BulletCluster/scaffolds/gallery.html", "BulletCluster", "every JWST scaffold, raw beside false colour, with selectable shear (JWST) and real-polarization (HST) vector overlays; Bullet Cluster, Crab Nebula, HE 0435, Pillars of Creation", 8765),
         ("Scaffold overlay report", "BulletCluster/scaffolds/overlay_report.html", "BulletCluster", "the shear image and the polarization image for each scaffold, side by side", 8765),
         ("Pillars of Creation shear field", "BulletCluster/scaffolds/overlays/viewers/Pillars_shear.html", "BulletCluster", "zoomable SVG: vector field over the whole composite with faint field lines", 8765),
         ("Crab Nebula polarization field", "BulletCluster/scaffolds/overlays/viewers/Crab_polarization.html", "BulletCluster", "zoomable SVG: harpoon vectors and field lines over the HST-covered area", 8765),
         ("Equation Space Gallery", "SedenionSpectralRelativity/EquationSpace/gallery/equation_space_gallery.html", "SedenionSpectralRelativity", "the two equation catalogs with their sedenion locations; the F = ma tree; the units lattice; the Niemeier/Monster threshold and the prime race mod 16", 8766),
         ("T32 Nilpotency Gallery", "ValaQuenta/gallery/t32_nilpotency/index.html", "ValaQuenta", "ValaQuenta engine 3: four interactive pages on the T32/GF(2) algebra: the square law (every word is nilpotent or an involutory unit, 128 | 128 at dimension 8), the detector w·𝟏, primes as Hyperwebster words with their control, and the zero-divisor pair matrix; each page checks its JavaScript port against the Python engine", 8791),
         ("Hypergon Constructibility Gallery", "ValaQuenta/gallery/hypergon_constructibility/index.html", "ValaQuenta", "ValaQuenta engine 4: four interactive pages: the sixteen hypergons (Gauss–Wantzel round the sedenion ring), the Niemeier gap {1, 11, 15} with the Moonshine control, the n-ball and the Gamma function (peak at n = 5.2569, the circle at n = 2, the poles of Γ), and a 3D Cartesian frame with its OpenSCAD companion; each checks its JavaScript against the Python engines",  8792),
         ("Box-Kite Gallery", "ValaQuenta/gallery/box_kite/index.html", "ValaQuenta", "ValaQuenta engine 5: five interactive pages: one box-kite as a rotatable octahedron, the 42 assessors as seven octahedra (e₀ at the eighth cube corner), the Fano plane and PG(3,2) with strut = a XOR b, the associator map (1848 of 4096 triples), the group 1344 = 8 × 168 and its non-split extension; plus an OpenSCAD printable octahedron", 8793)]
ATL = [("Riemann–Fermat Atlas", "the UNS space containing the Two Trees and the ζ pathway: sphere, wheels, springs, extinction flow, nodal ladder, heartbeat, prime pathway", "RiemannHypothesisProof/rhp/atlas_riemann_fermat/", "Riemann–Fermat Atlas Gallery"),
       ("Box-Kite Atlas (sedenion)", "the 42-vertex, 84-edge glued graph of the seven box-kites, joined only at e₀", "ValaQuenta/gallery/box_kite/ (five pages: octahedron, the 42 as seven octahedra, Fano and PG(3,2), associator, group)", "Box-Kite Gallery"),
       ("Abrikosov Zero-Divisor-Tree Atlas", "the zero-divisor propagation T16…T512, radial tree", "AbrikosovTree/render/atlas_abrikosov_zd_tree/", "Abrikosov Atlas Gallery"),
       ("Abrikosov CD-Tower Lattice Atlas", "the Two Trees on each Cayley–Dickson plane ℝ→𝕊→T₈₁₉₂", "AbrikosovTree/render/atlas_abrikosov_cd_lattice/", "Abrikosov Atlas Gallery"),
       ("Abrikosov CD-Tower UNS Atlas", "the same planes in native (UNS) coordinates", "AbrikosovTree/render/atlas_abrikosov_cd_uns/", "Abrikosov Atlas Gallery"),
       ("Circle Atlas", "every viewport through which the mathematics meets a circle (TheInterface paper)", "FourthAgePapers/TheInterface (branch; no image set yet)", "")]
def render(base, site, local, repos, inter, out_paths):
    cfg = dict(base=base, site=site, local=local, repos=repos, img=[dict(name=n, page=p, port=po, proprietary=pr) for n, p, po, pr in IMG],
               inter=[dict(name=n, page=p, repo=r, blurb=b, port=po) for n, p, r, b, po in inter], atlases=[dict(name=n, maps=m, where=w, gallery=g) for n, m, w, g in ATL])
    tpl = open(os.path.join(HERE, "index_template.html")).read().replace("/*CFG*/", json.dumps(cfg, ensure_ascii=False)).replace("%%FAVICON%%", fav).replace("%%CT_CSS%%", contact.CSS).replace("%%CT_TOP%%", contact.top()).replace("%%CT_BOTTOM%%", contact.bottom())
    for p in out_paths: os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w").write(tpl)
if __name__ == "__main__":
    repos = json.load(open(os.path.join(HERE, "site", "repos.json"))) if os.path.exists(os.path.join(HERE, "site", "repos.json")) else []
    render("../", "../michaelrendier.github.io/", True, repos, INTER, [os.path.join(OUT, "index.html"), os.path.join(HERE, "index.html")])
    open(os.path.join(OUT, "favicon.png"), "wb").write(base64.b64decode(fav.split(",", 1)[1]))
sh = os.path.join(OUT, "serve_all.sh")
open(sh, "w").write('''#!/bin/bash
# One server for every gallery: serves ~/Projects/ThePlace on 127.0.0.1:8760 (loopback only) and opens the index. Stop with: pkill -f "http.server 8760"
PORT=${1:-8760}; ROOT="$(cd "$(dirname "$0")/.." && pwd)"
curl -s -o /dev/null "http://127.0.0.1:$PORT/galleries/favicon.png" || { nohup python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$ROOT" >/dev/null 2>&1 & sleep 1; }
xdg-open "http://127.0.0.1:$PORT/galleries/index.html" >/dev/null 2>&1
''')
os.chmod(sh, 0o755); print("wrote", os.path.join(OUT, "index.html"), "and", sh)
