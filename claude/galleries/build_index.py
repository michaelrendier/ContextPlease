#!/usr/bin/env python3
"""build_index.py (2026-11-21): writes ThePlace/galleries/index.html, the single entry point to every gallery.
The page is static; at load time it FETCHES each image gallery's page (same origin, served from ThePlace root) and reads that gallery's embedded data to build one searchable catalog.
So the index file itself holds no image data: the proprietary VAPMIP galleries are linked and read at run time, never copied into it.
usage: python3 build_index.py   (then ./serve_all.sh)"""
import os, json, base64
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.expanduser("~/Projects/ThePlace"); OUT = os.path.join(ROOT, "galleries")
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
         ("Equation Space Gallery", "SedenionSpectralRelativity/EquationSpace/gallery/equation_space_gallery.html", "SedenionSpectralRelativity", "the two equation catalogs with their sedenion locations; the F = ma tree; the units lattice; the Niemeier/Monster threshold and the prime race mod 16", 8766)]
ATL = [("Riemann–Fermat Atlas", "the UNS space containing the Two Trees and the ζ pathway: sphere, wheels, springs, extinction flow, nodal ladder, heartbeat, prime pathway", "RiemannHypothesisProof/rhp/atlas_riemann_fermat/", "Riemann–Fermat Atlas Gallery"),
       ("Box-Kite Atlas (sedenion)", "the 42-vertex, 84-edge glued graph of the seven box-kites, joined only at e₀", "ValaQuenta/modules/box_kite/ (functions; no image set yet)", ""),
       ("Abrikosov Zero-Divisor-Tree Atlas", "the zero-divisor propagation T16…T512, radial tree", "AbrikosovTree/render/atlas_abrikosov_zd_tree/", "Abrikosov Atlas Gallery"),
       ("Abrikosov CD-Tower Lattice Atlas", "the Two Trees on each Cayley–Dickson plane ℝ→𝕊→T₈₁₉₂", "AbrikosovTree/render/atlas_abrikosov_cd_lattice/", "Abrikosov Atlas Gallery"),
       ("Abrikosov CD-Tower UNS Atlas", "the same planes in native (UNS) coordinates", "AbrikosovTree/render/atlas_abrikosov_cd_uns/", "Abrikosov Atlas Gallery"),
       ("Circle Atlas", "every viewport through which the mathematics meets a circle (TheInterface paper)", "FourthAgePapers/TheInterface (branch; no image set yet)", "")]
cfg = dict(img=[dict(name=n, page=p, port=po, proprietary=pr) for n, p, po, pr in IMG], inter=[dict(name=n, page=p, repo=r, blurb=b, port=po) for n, p, r, b, po in INTER], atlases=[dict(name=n, maps=m, where=w, gallery=g) for n, m, w, g in ATL])
tpl = open(os.path.join(HERE, "index_template.html")).read().replace("/*CFG*/", json.dumps(cfg, ensure_ascii=False)).replace("%%FAVICON%%", fav)
os.makedirs(OUT, exist_ok=True); open(os.path.join(OUT, "index.html"), "w").write(tpl); open(os.path.join(HERE, "index.html"), "w").write(tpl)
open(os.path.join(OUT, "favicon.png"), "wb").write(base64.b64decode(fav.split(",", 1)[1]))
sh = os.path.join(OUT, "serve_all.sh")
open(sh, "w").write('''#!/bin/bash
# One server for every gallery: serves ~/Projects/ThePlace on 127.0.0.1:8760 (loopback only) and opens the index. Stop with: pkill -f "http.server 8760"
PORT=${1:-8760}; ROOT="$(cd "$(dirname "$0")/.." && pwd)"
curl -s -o /dev/null "http://127.0.0.1:$PORT/galleries/favicon.png" || { nohup python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$ROOT" >/dev/null 2>&1 & sleep 1; }
xdg-open "http://127.0.0.1:$PORT/galleries/index.html" >/dev/null 2>&1
''')
os.chmod(sh, 0o755); print("wrote", os.path.join(OUT, "index.html"), "and", sh)
