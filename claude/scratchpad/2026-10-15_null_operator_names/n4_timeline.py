"""N4 — commit subjects across all repos that name or rename the object (chronological). Raw material for the curated timeline."""
import subprocess, os, re
ROOT = "/home/rendier/Projects/ThePlace"
pat = re.compile(r"Ĥ_RB|H_hat_RB|HhatRB|H_RB|RedBlue|Red-Blue|0_RB|∅_RB|Emptyset|Null Operator|null operator|Boundary Generator|Observer Hamiltonian|Hamiltonian of Consciousness|rename|renam|0_BR", re.I)
rows = []
for r in sorted(os.listdir(ROOT)):
    p = os.path.join(ROOT, r)
    if not os.path.isdir(os.path.join(p, ".git")): continue
    out = subprocess.run(["git", "-C", p, "log", "--format=%ad|%h|%s", "--date=short"], capture_output=True, text=True).stdout.splitlines()
    for l in out:
        d, h, s = l.split("|", 2)
        if pat.search(s): rows.append((d, r, h, s))
rows.sort()
open("n4_timeline_raw.tsv", "w").write("\n".join("\t".join(x) for x in rows))
print(len(rows), "commits")
key = re.compile(r"renam|Null Operator|∅_RB|0_RB|Emptyset|Consciousness|Observer Hamiltonian|Boundary Generator|Inductive|H_hat_RB|Ĥ_RB", re.I)
for d, r, h, s in rows:
    if key.search(s): print(f"{d} {r:22s} {h} {s[:170]}")
