"""N2 — first appearance of each name in each repo's git history (pickaxe -S, oldest first), plus the repo's own first commit.
Output: n2_first_appearance.tsv (name, repo, date, commit, subject) and a per-name earliest-overall list."""
import subprocess, os, collections, json
ROOT = "/home/rendier/Projects/ThePlace"
NAMES = ["Hamiltonian of Consciousness", "Consciousness Hamiltonian", "Observer Hamiltonian", "Inductive Geometric Coupling", "Boundary Generator",
         "Seg Fault Handler", "Fixed Point Space", "Hyperindexer", "H_hat_RB", "Ĥ_RB", "HhatRB", "RedBlue Hamiltonian", "H_RB", "RedBlue Geometries",
         "Emptyset_RB", "Red Blue Empty", "∅_RB", "Null Operator", "0_RB", "0_BR", "Geometric Observer", "Lagrangian Laplacian Hamiltonian"]
repos = [d for d in sorted(os.listdir(ROOT)) if os.path.isdir(os.path.join(ROOT, d, ".git"))]
rows = []
first_commit = {}
for r in repos:
    p = os.path.join(ROOT, r)
    fc = subprocess.run(["git", "-C", p, "log", "--reverse", "--format=%ad|%h", "--date=short", "-1"], capture_output=True, text=True).stdout.strip()
    # --reverse with -1 gives the newest; use rev-list for the root
    root = subprocess.run(["git", "-C", p, "rev-list", "--max-parents=0", "HEAD"], capture_output=True, text=True).stdout.split()
    if root:
        d = subprocess.run(["git", "-C", p, "log", "-1", "--format=%ad", "--date=short", root[-1]], capture_output=True, text=True).stdout.strip()
        first_commit[r] = d
    for n in NAMES:
        o = subprocess.run(["git", "-C", p, "log", "--reverse", "-S" + n, "--format=%ad|%h|%s", "--date=short"], capture_output=True, text=True).stdout.splitlines()
        if o:
            d, h, s = o[0].split("|", 2)
            rows.append((n, r, d, h, s[:90], len(o)))
rows.sort(key=lambda x: (x[0], x[2]))
with open("n2_first_appearance.tsv", "w") as f:
    f.write("name\trepo\tfirst_date\tcommit\tsubject\tcommits_touching\n")
    for x in rows: f.write("\t".join(map(str, x)) + "\n")
print("repos with git history:", len(repos)); print("repo first commits:", dict(sorted(first_commit.items(), key=lambda x: x[1])))
best = {}
for n, r, d, h, s, c in rows:
    if n not in best or d < best[n][1]: best[n] = (r, d, h, s)
print()
for n in NAMES:
    if n in best: print(f"{n:34s} earliest {best[n][1]}  {best[n][0]:22s} {best[n][2]}  {best[n][3]}")
    else: print(f"{n:34s} (no git commit introduces this string)")
json.dump({"first_commit": first_commit, "earliest": best}, open("n2_earliest.json", "w"), indent=1, ensure_ascii=False)
