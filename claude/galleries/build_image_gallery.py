#!/usr/bin/env python3
"""build_image_gallery.py (2026-11-21): one generator for the per-repository IMAGE galleries.
usage: python3 build_image_gallery.py CONFIG.json
CONFIG: repo (path), name, slug, port, tagline, groups[{name, match, blurb}] (first regex match on the repo-relative path wins), exclude[regex], catalog (optional IMAGE_CATALOG-style markdown: '## N. `path` — title' sections become descriptions),
        titles[{match, title}] (optional regex overrides, \\1 groups allowed), notes[{match, desc}] (description when none is found), also_scan[dirs] (external folders whose byte-identical copies are listed as 'also at').
Writes <repo>/image_gallery/<slug>.html (+ serve_gallery.sh, favicon.png). Images are NOT copied: the page links them by relative path, so serve from the repo root (serve_gallery.sh does)."""
import os, re, sys, json, hashlib, subprocess, datetime, collections, base64, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(sys.argv[1])); REPO = os.path.abspath(os.path.expanduser(cfg["repo"])); OUT = os.path.join(REPO, cfg.get("out_dir", "image_gallery")); SCAN = [os.path.join(REPO, x) for x in cfg.get("scan", [""])]
IMG = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"); PRUNE = {".git", ".venv", "node_modules", "__pycache__", "site-packages", "_build", "image_gallery", "holcus_paths_gallery"}
EXC = [re.compile(p) for p in cfg.get("exclude", [])]; GRP = [(g, re.compile(g["match"])) for g in cfg["groups"]]; TIT = [(re.compile(t["match"]), t["title"]) for t in cfg.get("titles", [])]; NOTES = [(re.compile(t["match"]), t["desc"]) for t in cfg.get("notes", [])]
def walk(root):
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in PRUNE]
        for f in files: yield os.path.join(d, f)
def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
files = sorted(p for sc in SCAN for p in walk(sc) if p.lower().endswith(IMG) and not any(e.search(os.path.relpath(p, REPO)) for e in EXC))
rels = [os.path.relpath(p, REPO) for p in files]
# duplicates (same bytes) collapse to one entry, the other paths listed
by = collections.OrderedDict()
for p, r in zip(files, rels): by.setdefault(md5(p), []).append(r)
also = {}
for d in cfg.get("also_scan", []):
    d = os.path.expanduser(d)
    if os.path.isdir(d):
        for p in walk(d):
            if p.lower().endswith(IMG): also.setdefault(md5(p), []).append(p.replace(os.path.expanduser("~"), "~"))
# text index: where each image file name is mentioned
names = {os.path.basename(v[0]): k for k, v in by.items()}
alln = {os.path.basename(r): k for k, v in by.items() for r in v}
pat = re.compile(r"(?<![\w.-])(" + "|".join(re.escape(n) for n in sorted(alln, key=len, reverse=True)) + r")(?![\w-])") if alln else None
refs = collections.defaultdict(list)
TXT = (".py", ".md", ".rst", ".txt", ".ipynb", ".html", ".sh", ".tex", ".json")
if pat:
    for p in walk(REPO):
        if not p.lower().endswith(TXT) or os.path.getsize(p) > 3_000_000 or os.path.relpath(p, REPO) in rels: continue
        try: lines = open(p, errors="ignore").read().split("\n")
        except OSError: continue
        for i, ln in enumerate(lines):
            for m in pat.finditer(ln):
                refs[alln[m.group(1)]].append((os.path.relpath(p, REPO), i + 1, ln.strip()[:200]))
def ident(p):
    ext = p.lower().rsplit(".", 1)[-1]
    if ext == "svg":
        s = open(p, errors="ignore").read(4000); w = re.search(r'\bwidth="([\d.]+)', s); h = re.search(r'\bheight="([\d.]+)', s); vb = re.search(r'viewBox="[\d.\- ]*? ([\d.]+) ([\d.]+)"', s)
        if w and h: return int(float(w.group(1))), int(float(h.group(1))), 1
        if vb: return int(float(vb.group(1))), int(float(vb.group(2))), 1
        return 0, 0, 1
    try:
        o = subprocess.run(["identify", "-format", "%w %h %n\n", p + ("[0]" if ext == "gif" else "")], capture_output=True, text=True, timeout=30).stdout.split()
        n = 1
        if ext == "gif":
            n = len(subprocess.run(["identify", "-format", "x\n", p], capture_output=True, text=True, timeout=60).stdout.split())
        return int(o[0]), int(o[1]), n
    except Exception: return 0, 0, 1
def gitinfo(rel):
    try:
        o = subprocess.run(["git", "-C", REPO, "log", "--diff-filter=A", "--follow", "--format=%ad|%h|%s", "--date=short", "--", rel], capture_output=True, text=True, timeout=30).stdout.strip().split("\n")[-1]
        d, h, s = (o.split("|", 2) + ["", ""])[:3]; return d, h, s[:140]
    except Exception: return "", "", ""
cat = {}
if cfg.get("catalog") and os.path.exists(os.path.join(REPO, cfg["catalog"])):
    txt = open(os.path.join(REPO, cfg["catalog"])).read()
    for m in re.finditer(r"^## \d+[a-z]?\. `([^`]+)`\s*[—-]\s*(.*?)\n(.*?)(?=^## |\Z)", txt, re.M | re.S): cat[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
def humanize(rel):
    b = os.path.splitext(os.path.basename(rel))[0]; b = re.sub(r"_?\d{9,}$", "", b); b = re.sub(r"[_-]+", " ", b).strip()
    return b[:1].upper() + b[1:]
items = []
for k, paths in by.items():
    rel = paths[0]; p = os.path.join(REPO, rel); st = os.stat(p); w, h, n = ident(p); d, hh, sub = gitinfo(rel)
    grp = next((g["name"] for g, rx in GRP if rx.search(rel)), "Other")
    title = next((rx.sub(t, rel) if "\\" in t else t for rx, t in TIT if rx.search(rel)), None)
    desc = ""
    for cp, (ct, cd) in cat.items():
        if cp == rel or cp.endswith("/" + os.path.basename(rel)) or os.path.basename(cp) == os.path.basename(rel) and rel.endswith(cp):
            title = title or ct; desc = cd
    if not desc: desc = next((d for rx, d in NOTES if rx.search(rel)), "")
    ref = refs.get(k, []); gen = [r for r in ref if r[0].endswith((".py", ".sh"))][:4]; doc = [r for r in ref if not r[0].endswith((".py", ".sh", ".json", ".html"))][:4]
    if not desc and doc:
        m = re.search(r"!\[([^\]]*)\]", doc[0][2]); desc = m.group(1) if m and m.group(1) else ""
    if not desc and gen:
        try:
            import ast
            fp = os.path.join(REPO, gen[0][0]); mdoc = ast.get_docstring(ast.parse(open(fp, errors="ignore").read())) if fp.endswith(".py") else None
            if mdoc: desc = "Written by `" + gen[0][0] + "`: " + " ".join(mdoc.strip().split("\n\n")[0].split())[:420]
        except Exception: pass
    if cfg.get("svg_meta") and rel.endswith(".svg"):
        try:
            sv = open(p, errors="ignore").read(); texts = re.findall(r'<text[^>]*?fill="([^"]*)"[^>]*>([^<]*)</text>', sv); prompt = texts[0][1] if texts else ""
            words = [t for f, t in texts if f == "#2a2a2a"]; nodes = re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="2.5"', sv)
            amp = [round(((float(a) - 250) ** 2 + (float(b) - 260) ** 2) ** .5 / 210, 3) for a, b in nodes][:16]
            ep = re.search(r"_(\d{10})\.svg$", rel); when = datetime.datetime.fromtimestamp(int(ep.group(1))).strftime("%Y-%m-%d %H:%M") if ep else ""
            title = (prompt or title or humanize(rel)) + (" · " + when if when else "")
            desc = ("Prompt: **" + prompt + "**" + ("\n- spoke words (the prompt hashed onto the 16 spokes): " + " · ".join(words) if words else "") +
                    ("\n- node distances from the centre (outer ring = 1.0), spokes in file order: " + ", ".join(map(str, amp)) if amp else "") + ("\n- written " + when if when else "") + "\n- original output of `ptol.c -s` (the 16-spoke sedenion path paper); unmodified copy.")
        except Exception: pass
    items.append(dict(id=len(items), path=rel, url=urllib.parse.quote(rel), title=title or humanize(rel), group=grp, type=rel.rsplit(".", 1)[-1].lower(), w=w, h=h, frames=n, bytes=st.st_size,
                      mtime=datetime.date.fromtimestamp(st.st_mtime).isoformat(), added=d, commit=hh, commit_msg=sub, also=paths[1:] + also.get(k, []), generated_by=[f"{r[0]}:{r[1]}" for r in gen],
                      referenced_in=[dict(file=r[0], line=r[1], text=r[2]) for r in doc], desc=desc))
order = {g["name"]: i for i, g in enumerate(cfg["groups"])}; items.sort(key=lambda x: (order.get(x["group"], 99), x["path"])); [x.update(id=i) for i, x in enumerate(items)]
groups = [dict(name=g["name"], blurb=g.get("blurb", ""), count=sum(1 for x in items if x["group"] == g["name"])) for g in cfg["groups"]]
groups = [g for g in groups if g["count"]] + ([dict(name="Other", blurb="", count=sum(1 for x in items if x["group"] == "Other"))] if any(x["group"] == "Other" for x in items) else [])
os.makedirs(OUT, exist_ok=True)
fav = open(os.path.join(HERE, "favicon_datauri.txt")).read().strip(); open(os.path.join(OUT, "favicon.png"), "wb").write(base64.b64decode(fav.split(",", 1)[1]))
data = dict(name=cfg["name"], tagline=cfg.get("tagline", ""), built=datetime.date.today().isoformat(), thumb_bright=bool(cfg.get("thumb_bright")), repo=os.path.basename(REPO), groups=groups, items=items, port=cfg.get("port", 8800))
tpl = open(os.path.join(HERE, "image_gallery_template.html")).read().replace("/*DATA*/", json.dumps(data, ensure_ascii=False)).replace("%%FAVICON%%", fav).replace("%%TITLE%%", cfg["name"])
open(os.path.join(OUT, cfg["slug"] + ".html"), "w").write(tpl)
sh = os.path.join(OUT, "serve_gallery.sh")
open(sh, "w").write(f'''#!/bin/bash
# Open the {cfg["name"]} through a local web server on 127.0.0.1 (Firefox shows the favicon only for http pages). Serves the repository root so the image links resolve.
# Usage: ./serve_gallery.sh [port={cfg.get("port", 8800)}]   (loopback only; stop with: pkill -f "http.server {cfg.get("port", 8800)}")
cd "$(dirname "$0")/.."; PORT=${{1:-{cfg.get("port", 8800)}}}
curl -s -o /dev/null "http://127.0.0.1:$PORT/image_gallery/favicon.png" || {{ nohup python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 & sleep 1; }}
xdg-open "http://127.0.0.1:$PORT/image_gallery/{cfg["slug"]}.html" >/dev/null 2>&1
''')
os.chmod(sh, 0o755)
print(f'{cfg["name"]}: {len(items)} images in {len(groups)} groups; {sum(1 for x in items if x["also"])} with copies; page {os.path.join(OUT, cfg["slug"] + ".html")}')
for g in groups: print(f'   {g["count"]:3d}  {g["name"]}')
