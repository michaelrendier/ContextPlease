# SPDX-License-Identifier: GPL-3.0-only
"""Build NOTEBOOK_CATALOG.ipynb at the root of a repository: every notebook in it, with kernel, size and a one-line synopsis.
Usage: python3 make_notebook_catalog.py REPO_DIR [REPO_DIR ...]      (a notebook's synopsis is read from the notebook itself, never written by hand)"""
import json, os, re, sys

SKIP = (".venv", "node_modules", "site-packages", ".ipynb_checkpoints", "_worktrees", "lambeq_env", ".git/")

def find(repo):
    out = []
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in (".venv", "node_modules", ".git", ".ipynb_checkpoints", "site-packages", "_worktrees")]
        for f in files:
            if f.endswith(".ipynb"): out.append(os.path.relpath(os.path.join(root, f), repo))
    return sorted(out)

def clean(t):
    t = re.sub(r"[`*_#>|]", "", t); t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t); return re.sub(r"\s+", " ", t).strip()

def describe(path):
    try: nb = json.load(open(path))
    except Exception as e: return dict(kernel="unreadable", cells=0, code=0, title=os.path.basename(path), synopsis=f"could not be read ({type(e).__name__})")
    cells = nb.get("cells", []); kern = nb.get("metadata", {}).get("kernelspec", {}).get("name", "unknown")
    title, syn = None, None
    for c in cells:
        if c.get("cell_type") != "markdown": continue
        lines = [l for l in "".join(c.get("source", [])).splitlines() if l.strip()]
        for l in lines:
            if l.lstrip().startswith("#") and title is None: title = clean(l); continue
            if title is not None and syn is None and not l.lstrip().startswith(("#", "|", "-", "```", "---")) and len(clean(l)) > 25 and not re.match(r"(Requires|Install|Run with|Prerequisite)", clean(l)): syn = clean(l)
        if title and syn: break
    if syn is None:
        for c in cells:
            if c.get("cell_type") == "code":
                m = re.search(r'"""(.+?)"""|/\*+\s*(.+?)\*/|^\s*(?:#|//)\s*(.+)$', "".join(c.get("source", [])), re.S | re.M)
                if m: syn = clean(next(g for g in m.groups() if g))[:200]; break
    return dict(kernel=kern, cells=len(cells), code=sum(c.get("cell_type") == "code" for c in cells), title=title or os.path.splitext(os.path.basename(path))[0], synopsis=(syn or "no description cell; see the notebook")[:220])

def build(repo):
    repo = os.path.abspath(repo); name = os.path.basename(repo); nbs = [p for p in find(repo) if os.path.basename(p) != "NOTEBOOK_CATALOG.ipynb"]
    rows = {p: describe(os.path.join(repo, p)) for p in nbs}
    kc = {}
    for r in rows.values(): kc[r["kernel"]] = kc.get(r["kernel"], 0) + 1
    md = [f"# {name}: notebook catalog\n", f"{len(nbs)} notebooks. Kernels: " + ", ".join(f"`{k}` × {v}" for k, v in sorted(kc.items(), key=lambda kv: -kv[1])) + ".\n",
          "Each row links to the notebook, names its kernel, counts its cells, and gives the synopsis the notebook itself carries (its first heading and first descriptive line). "
          "Notebooks with kernel `c` run C code in cells (the Jupyter C kernel; `jupyter kernelspec list` should show `c`); `python3` notebooks need the repository's own environment. "
          "A notebook's stored outputs are what was shown when it was last run: re-run it to check them.\n"]
    by = {}
    for p in nbs: by.setdefault(os.path.dirname(p) or ".", []).append(p)
    for d in sorted(by):
        md.append(f"\n## `{d}/`\n\n| notebook | kernel | cells (code) | synopsis |\n|---|---|---|---|")
        for p in by[d]:
            r = rows[p]; md.append(f"| [{os.path.basename(p)}]({p.replace(' ', '%20')}) | `{r['kernel']}` | {r['cells']} ({r['code']}) | **{r['title'][:80]}**: {r['synopsis'].replace('|', '/')} |")
    code = f'''import json, os
root = os.path.abspath(".")          # run this notebook from the repository root
SKIP = {{".venv", "node_modules", ".git", ".ipynb_checkpoints", "site-packages", "_worktrees"}}
found = []
for r, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in SKIP]
    found += [os.path.relpath(os.path.join(r, f), root) for f in files if f.endswith(".ipynb") and f != "NOTEBOOK_CATALOG.ipynb"]
kernels = {{}}
for p in found:
    try: k = json.load(open(p)).get("metadata", {{}}).get("kernelspec", {{}}).get("name", "unknown")
    except Exception: k = "unreadable"
    kernels[k] = kernels.get(k, 0) + 1
print(len(found), "notebooks on disk;", {len(nbs)}, "in this catalog when it was built")
print("kernels:", kernels)
'''
    nb = {"cells": [{"cell_type": "markdown", "metadata": {}, "source": "\n".join(md)},
                    {"cell_type": "markdown", "metadata": {}, "source": "### Check: does the catalog still match the disk?"},
                    {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": code}],
          "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
    json.dump(nb, open(os.path.join(repo, "NOTEBOOK_CATALOG.ipynb"), "w"), indent=1)
    return name, len(nbs), kc

if __name__ == "__main__":
    for r in sys.argv[1:]: print(*build(r))
