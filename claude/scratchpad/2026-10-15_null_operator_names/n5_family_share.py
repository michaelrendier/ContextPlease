"""N5 — how much of the record is the H-family name (H_hat_RB / Ĥ_RB / H_RB / RedBlue Hamiltonian) vs the null-family name (0_RB / ∅_RB / 0_BR / Emptyset_RB)?
File-level and hit-level, per repo, excluding the two giant corpus dumps and this scratch dir."""
import os, re, collections
ROOT = "/home/rendier/Projects/ThePlace"
SKIP_DIRS = {".git", ".venv", "lambeq_env", "__pycache__", "node_modules", "_worktrees", "bins", "Music", "Pictures", "datasets", "checkpoints", "2026-10-15_null_operator_names"}
SKIP_FILES = {"corpus_repos.txt", "corpus_all.txt"}
TEXT = (".md", ".txt", ".py", ".c", ".h", ".json", ".tex", ".rst", ".sh", ".html")
H = re.compile(r"H_hat_RB|Ĥ_RB|HhatRB|H_hat_\{RB\}|\\hat\{H\}_\{?RB|\bH_RB\b|\bH_\{RB\}|Red-?Blue Hamiltonian")
N = re.compile(r"\b0_RB\b|∅_RB|\b0_BR\b|Emptyset_RB")
fh = fn = fb = 0; hh = hn = 0; per = collections.defaultdict(lambda: [0, 0, 0, 0, 0])
for dp, dn, fs in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fs:
        if f in SKIP_FILES or not f.endswith(TEXT): continue
        p = os.path.join(dp, f)
        try:
            if os.path.getsize(p) > 20_000_000: continue
            t = open(p, encoding="utf-8", errors="ignore").read()
        except OSError: continue
        a, b = len(H.findall(t)), len(N.findall(t))
        if not (a or b): continue
        repo = os.path.relpath(p, ROOT).split(os.sep)[0]
        hh += a; hn += b
        if a and b: fb += 1; per[repo][2] += 1
        elif a: fh += 1; per[repo][0] += 1
        else: fn += 1; per[repo][1] += 1
        per[repo][3] += a; per[repo][4] += b
tot = fh + fn + fb
print(f"files naming the object: {tot}:  H-family only {fh} ({fh/tot:.0%}) | null-family only {fn} ({fn/tot:.0%}) | both {fb} ({fb/tot:.0%})")
print(f"files using the H-family at all: {fh+fb} ({(fh+fb)/tot:.0%});  null-family at all: {fn+fb} ({(fn+fb)/tot:.0%})")
print(f"hits: H-family {hh:,} ({hh/(hh+hn):.0%}) | null-family {hn:,} ({hn/(hh+hn):.0%})")
print(f"\n{'repo':24s} {'H only':>7s} {'N only':>7s} {'both':>5s} {'H hits':>8s} {'N hits':>8s}")
for r, v in sorted(per.items(), key=lambda x: -(x[1][3] + x[1][4]))[:12]: print(f"{r:24s} {v[0]:7d} {v[1]:7d} {v[2]:5d} {v[3]:8d} {v[4]:8d}")
