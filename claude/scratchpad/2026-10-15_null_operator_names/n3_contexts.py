"""N3 — where the rarer names actually occur (path:line:text), excluding this session's scratch dir. Usage: python3 n3_contexts.py [name ...] (default: the rare set)."""
import os, re, sys
ROOT = "/home/rendier/Projects/ThePlace"
SKIP_DIRS = {".git", ".venv", "lambeq_env", "__pycache__", "node_modules", "_worktrees", "bins", "Music", "Pictures", "datasets", "checkpoints", "2026-10-15_null_operator_names"}
SKIP_FILES = {"corpus_repos.txt", "corpus_all.txt"}
TEXT = (".md", ".txt", ".py", ".c", ".h", ".json", ".tex", ".rst", ".sh", ".html")
PATS = {
 "seg fault": r"seg[ -]?fault|segmentation fault",
 "Inductive Geometric Coupling": r"Inductive.{0,25}Coupling|Geometric Coupling",
 "Observer Hamiltonian": r"Observer[ -]Hamiltonian",
 "Hamiltonian of Consciousness": r"Hamiltonian of Consciousness|Consciousness Hamiltonian",
 "Mathematical Hyperindexer": r"Mathematical Hyper-?[Ii]ndexer",
}
sel = sys.argv[1:] or list(PATS)
cp = {k: re.compile(PATS[k], re.I) for k in sel}
cnt = {k: 0 for k in sel}
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fn:
        if f in SKIP_FILES or not f.endswith(TEXT): continue
        p = os.path.join(dp, f)
        try:
            if os.path.getsize(p) > 20_000_000: continue
            lines = open(p, encoding="utf-8", errors="ignore").read().splitlines()
        except OSError: continue
        for i, l in enumerate(lines, 1):
            for k, c in cp.items():
                if c.search(l) and cnt[k] < 9:
                    cnt[k] += 1; print(f"[{k}] {os.path.relpath(p, ROOT)}:{i}: {l.strip()[:230]}")
for k in sel: print(k, "-> shown", cnt[k])
