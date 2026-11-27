#!/usr/bin/env python3
"""build_site.py (2026-11-21): builds the user site michaelrendier.github.io: a repository index with a gallery page for EVERY repository.
Reads the repository list from GitHub (gh), the header images (the author's uploaded README/social images, web-size copies), and the gallery registry below.
Pages with a real image gallery redirect to it (project Pages of that repository); the others get a stub that grows with the repository.
usage: python3 build_site.py   (needs gh, ImageMagick `convert`)"""
import os, sys, json, subprocess, shutil, html, base64, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import contact
ROOT = os.path.expanduser("~/Projects/ThePlace"); SITE = os.path.join(ROOT, "michaelrendier.github.io"); SG = os.path.expanduser("~/Desktop/SpaceGemini")
HEAD = {"Ainulindale": f"{SG}/Gemini_Generated_Image_Ainulindale_Conjecture_1mb.png", "PtolemyDesktop": f"{SG}/Gemini_Generated_Image_Ptolemy_1mb.png",
        "RiemannHypothesisProof": f"{SG}/Gemini_Generated_Image_Riemann_Proof_1mb.png", "SedenionSpectralRelativity": f"{SG}/Gemini_Generated_Image_Sedenion_1mb.png",
        "ValaQuenta": f"{SG}/Gemini_Generated_Image_SMMIP_1mb.png", "UniversalSynth": f"{SG}/Gemini_Generated_Image_UniversalSynth_1mb.png",
        "VAPMIP": f"{SG}/Gemini_Generated_Image_VAPMIP_corrected.png", "BulletCluster": f"{ROOT}/BulletCluster/Gemini_Generated_Image_Bulletcluster_social.png",
        "TuringStack": f"{ROOT}/TuringStack/Gemini_Generated_Image_Breaking_Enigma.png", "AbrikosovTree": f"{SG}/Gemini_Generated_Image_zero-tree-images.png"}
GAL = {"AbrikosovTree": [("Abrikosov Atlas Gallery", "image_gallery/Abrikosov_Atlas_Gallery.html")], "Ainulindale": [("Ainulindalë Gallery", "image_gallery/Ainulindale_Gallery.html")],
       "RiemannHypothesisProof": [("Riemann–Fermat Atlas Gallery", "image_gallery/Riemann_Fermat_Atlas_Gallery.html")], "GenerationalLineage": [("Generational Lineage Gallery", "image_gallery/Generational_Lineage_Gallery.html")],
       "SedenionSpectralRelativity": [("Sedenion Spectral Relativity Gallery", "image_gallery/Sedenion_Spectral_Relativity_Gallery.html"), ("Equation Space Gallery", "EquationSpace/gallery/equation_space_gallery.html")],
       "VAPMIP": [("VAPMIP Gallery", "image_gallery/VAPMIP_Gallery.html"), ("Holcus 16D Paths Gallery", "holcus_paths_gallery/Holcus_16D_Paths_Gallery.html")]}
ORDER = ["VAPMIP", "ValaQuenta", "Ainulindale", "RiemannHypothesisProof", "FourthAgePapers", "SedenionSpectralRelativity", "GenerationalLineage", "AbrikosovTree", "BulletCluster", "UniversalSynth", "PtolemyDesktop"]
LOCAL_ONLY = {"BulletCluster": "The Scaffold Gallery and its viewers (JWST scaffolds with shear and polarization overlays) run locally: the telescope data is not on GitHub."}
fav = open(os.path.join(HERE, "favicon_datauri.txt")).read().strip()
raw = json.loads(subprocess.run(["gh", "repo", "list", "michaelrendier", "--limit", "100", "--json", "name,description,pushedAt,visibility"], capture_output=True, text=True).stdout)
raw = [r for r in raw if r["name"] != "michaelrendier.github.io"]
raw.sort(key=lambda r: (ORDER.index(r["name"]) if r["name"] in ORDER else 99, "" if r["name"] in ORDER else "~" + r["pushedAt"][::-1]))
os.makedirs(os.path.join(SITE, "assets", "headers"), exist_ok=True); os.makedirs(os.path.join(SITE, "gallery"), exist_ok=True)
repos = []
for r in raw:
    n = r["name"]; hdr = ""
    if n in HEAD and os.path.exists(HEAD[n]):
        out = os.path.join(SITE, "assets", "headers", n + ".jpg"); subprocess.run(["convert", HEAD[n], "-resize", "1000x1000>", "-quality", "82", out], check=True); hdr = n + ".jpg"
    repos.append(dict(name=n, description=(r["description"] or "").strip(), pushed=r["pushedAt"][:10], header=hdr, galleries=len(GAL.get(n, [])), visibility=r["visibility"]))
json.dump(repos, open(os.path.join(SITE, "repos.json"), "w"), indent=1, ensure_ascii=False); json.dump(repos, open(os.path.join(HERE, "site", "repos.json"), "w"), indent=1, ensure_ascii=False)
open(os.path.join(SITE, "assets", "favicon.png"), "wb").write(base64.b64decode(fav.split(",", 1)[1])); open(os.path.join(SITE, ".nojekyll"), "w").write("")
STYLE = """<style>:root{--bg:#f4f6fb;--fg:#1b2033;--mut:#5a6483;--card:#fff;--line:#d9deee;--acc:#3b5bdb}@media(prefers-color-scheme:dark){:root{--bg:#0d1020;--fg:#e6e9f5;--mut:#98a2c3;--card:#161b33;--line:#2a3257;--acc:#8fa6ff}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,sans-serif}main{max-width:900px;margin:0 auto;padding:22px 16px}h1{margin:0 0 4px}.sub{color:var(--mut)}a{color:var(--acc)}
.hero{width:100%;max-height:360px;object-fit:cover;border-radius:12px;border:1px solid var(--line);margin:12px 0}.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:12px 0}
.btn{display:inline-block;background:var(--acc);color:#fff;border-radius:8px;padding:6px 14px;text-decoration:none;margin:6px 8px 0 0}.btn.o{background:none;color:var(--acc);border:1px solid var(--acc)}</style>"""
def page(title, body, head_extra=""):
    h = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><link rel="icon" href="/assets/favicon.png">{head_extra}{STYLE}</head><body><main>{body}</main></body></html>'
    return contact.inject(h)
for r in repos:
    n = r["name"]; d = html.escape(r["description"]); g = GAL.get(n, []); hero = f'<img class="hero" src="/assets/headers/{r["header"]}" alt="">' if r["header"] else ""
    gh = f'<a class="btn o" href="https://github.com/michaelrendier/{n}" target="_blank" rel="noopener">{n} on GitHub</a><a class="btn o" href="/">All repositories</a>'
    if len(g) == 1:
        url = f"/{n}/{g[0][1]}"; ex = f'<meta http-equiv="refresh" content="0; url={url}"><script>location.replace("{url}")</script>'
        body = f'<h1>{n}: gallery</h1><p class="sub">{d}</p>{hero}<p>Opening <a href="{url}">{html.escape(g[0][0])}</a>…</p>{gh}'; out = page(f"{n} gallery", body, ex)
    elif g:
        body = f'<h1>{n}: galleries</h1><p class="sub">{d}</p>{hero}' + "".join(f'<div class="card"><b>{html.escape(t)}</b><br><a class="btn" href="/{n}/{u}">Open</a></div>' for t, u in g) + gh; out = page(f"{n} galleries", body)
    else:
        note = LOCAL_ONLY.get(n, "No images have been generated for this repository yet. This page is its gallery: it grows as the repository does.")
        body = f'<h1>{n}: gallery</h1><p class="sub">{d}</p>{hero}<div class="card">{html.escape(note)}</div>{gh}'; out = page(f"{n} gallery", body)
    open(os.path.join(SITE, "gallery", n + ".html"), "w").write(out)
import build_index as BI
INTER_PAGES = [x for x in BI.INTER if x[0] in ("Equation Space Gallery", "T32 Nilpotency Gallery")]
BI.render("/", "/", False, repos, INTER_PAGES, [os.path.join(SITE, "index.html")])
open(os.path.join(SITE, "README.md"), "w").write("""# michaelrendier.github.io

The central page for the repositories of **Michael Rendier** (Cody Michael Allison): a repository index, a gallery page for every repository, and one searchable catalog of every generated image.

Contact: [the.wandering.god@gmail.com](mailto:the.wandering.god@gmail.com) · [Facebook](https://facebook.com/rendier) · [ORCID 0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760)

- `index.html`: the repository index and combined catalog (reads each repository's gallery page at run time).
- `gallery/<Repository>.html`: the gallery page of each repository (it forwards to the repository's own image gallery where one exists, otherwise it is a page that grows with the repository).
- `assets/headers/`: the repository header images (web-size copies of the images uploaded as each repository's social preview).
- Built by `ContextPlease/claude/galleries/build_site.py`.
""")
print("site:", SITE, "|", len(repos), "repositories |", sum(1 for r in repos if r["header"]), "with header images |", sum(1 for r in repos if r["galleries"]), "with galleries")
