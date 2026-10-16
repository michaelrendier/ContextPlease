"""N1 — census of every name used for the object, per repo (files, hits). Read-only. Skips .git, venvs, caches, binaries, ipynb, the two giant corpus dumps."""
import os, re, sys, collections, json
ROOT = "/home/rendier/Projects/ThePlace"
SKIP_DIRS = {".git", ".venv", "lambeq_env", "__pycache__", "node_modules", "_worktrees", "bins", "Music", "Pictures", "datasets", "checkpoints", "2026-10-15_null_operator_names"}
SKIP_FILES = {"corpus_repos.txt", "corpus_all.txt"}
TEXT = (".md", ".txt", ".py", ".c", ".h", ".json", ".tex", ".rst", ".sh", ".cff", ".toml", ".yml", ".yaml", ".html", ".cfg", ".csv")
NAMES = {
 "Hamiltonian of Consciousness": r"Hamiltonian of Consciousness|Consciousness Hamiltonian",
 "Observer Hamiltonian": r"Observer Hamiltonian",
 "Inductive Geometric Coupling": r"Inductive Geometric Coupling",
 "Boundary Generator": r"Boundary Generator",
 "Seg Fault Handler": r"[Ss]eg[ -]?[Ff]ault [Hh]andler",
 "Fixed Point Space": r"Fixed[ -][Pp]oint [Ss]pace",
 "Mathematical Hyperindexer": r"[Hh]yper-?[Ii]ndexer",
 "H_hat_RB (any spelling)": r"H_hat_RB|Ĥ_RB|HhatRB|H_hat_\{RB\}|\\hat\{H\}_\{?RB|H-hat-RB|Hhat_RB",
 "RedBlue Hamiltonian": r"Red-?Blue Hamiltonian",
 "H_RB": r"\bH_RB\b|\bH_\{RB\}",
 "RedBlue Geometries Engine": r"Red-?Blue Geometries",
 "Red Blue Empty Set": r"Red[ -]?Blue Empty|Empty ?[Ss]et_RB|Emptyset_RB",
 "∅_RB": r"∅_RB",
 "The Null Operator": r"[Nn]ull [Oo]perator",
 "0_RB": r"\b0_RB\b",
 "0_BR": r"\b0_BR\b",
 "Geometric Observer": r"Geometric Observer",
 "Hyperwebster (related)": r"[Hh]yper-?[Ww]ebster",
}
comp = {k: re.compile(v) for k, v in NAMES.items()}
files = collections.defaultdict(lambda: collections.defaultdict(int)); hits = collections.defaultdict(lambda: collections.defaultdict(int))
nfiles = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fn:
        if f in SKIP_FILES or not f.endswith(TEXT): continue
        p = os.path.join(dp, f)
        try:
            if os.path.getsize(p) > 30_000_000: continue
            t = open(p, encoding="utf-8", errors="ignore").read()
        except OSError: continue
        nfiles += 1
        repo = os.path.relpath(p, ROOT).split(os.sep)[0]
        for k, c in comp.items():
            n = len(c.findall(t))
            if n: files[k][repo] += 1; hits[k][repo] += n
print(f"{nfiles} text files scanned")
print(f"{'name':32s} {'files':>6s} {'hits':>6s}  top repos (files)")
out = {}
for k in NAMES:
    fs = sum(files[k].values()); hs = sum(hits[k].values())
    top = sorted(files[k].items(), key=lambda x: -x[1])[:6]
    out[k] = {"files": fs, "hits": hs, "repos": dict(files[k])}
    print(f"{k:32s} {fs:6d} {hs:6d}  " + ", ".join(f"{r}:{n}" for r, n in top))
json.dump(out, open("n1_census.json", "w"), indent=1, ensure_ascii=False)
