import nbformat as nbf, sys
which=sys.argv[1]
imp = ("import sys, os; sys.path.insert(0, os.path.abspath('..'))\nfrom fractions import Fraction as F\nfrom firing_plan import *\nfrom firing_plan import _equal, _matmul"
       if which=="ssr" else
       "import sys, os; sys.path.insert(0, os.path.abspath('..'))\nfrom fractions import Fraction as F\nfrom engine.bracketing_firing_order import *\nfrom engine.bracketing_firing_order import _equal, _matmul")
md=nbf.v4.new_markdown_cell; code=nbf.v4.new_code_cell
cells=[
md("""# 0%d — Brackets that carry firing orders

A **bracket** groups operators into one operation. It now carries a **firing order**, written beside it: `(R I | 2 1)` fires the second child (`I`, the imaginary octonion) first and the first child (`R`, the real octonion) second. A bracket runs as a single operation inside its parent, in the parent's own order, so a plan can carry firing orders at every depth.

**Why it matters.** The order the operators are used in changes the output, as a numerator driving a denominator differs from a denominator driving a numerator. Application order and traversal order are the same order in different terms; "direction" here is *order arrived at* and nothing more.

Everything below is exact (`Fraction`) and is run live by this notebook.""" % (2 if which=="ssr" else 3)),
code(imp),
md("""## 1 · The two-octonion model of the sedenion
`a = (a1, a2)`. `R = L((a1, 0))` is the real octonion half, `I = L((0, a2))` the imaginary octonion half, and `L_a = R + I` exactly. The bracket composes the halves as operators: fired first is applied first."""),
code("""a = tuple(F(x) for x in (1, 2, 0, 1, 0, 0, 3, 0, 0, 1, 0, 0, 2, 0, 0, 1))
R, I = two_octonion_leaves(a)
La = left_matrix(a)
print("L_a = R + I :", all(La[r][c] == R.matrix[r][c] + I.matrix[r][c] for r in range(16) for c in range(16)))
p12, p21 = two_octonions(a, (1, 2)), two_octonions(a, (2, 1))
print(notation(p12), "fires", fire_sequence(p12))
print(notation(p21), "fires", fire_sequence(p21))
M12, M21 = operator(p12), operator(p21)
print("(R I) = I·R :", _equal(M12, _matmul(I.matrix, R.matrix)), "   (R I | 2 1) = R·I :", _equal(M21, _matmul(R.matrix, I.matrix)))
print("entries where the two orders differ:", sum(M12[r][c] != M21[r][c] for r in range(16) for c in range(16)), "of 256")
x = tuple(F(int(i == 3)) for i in range(16))
print("same input e3, the two outputs:", apply_plan(p12, x), "|", apply_plan(p21, x), sep="\\n  ")"""),
md("""The two plans are different operators: the difference is the commutator of the two halves. Where the halves commute (one of them zero) the orders agree; the order is the whole content."""),
code("""zero_imag = a[:8] + (F(0),) * 8
print("imaginary half zero -> orders agree:", _equal(operator(two_octonions(zero_imag, (1, 2))), operator(two_octonions(zero_imag, (2, 1)))))"""),
md("""## 2 · A bracket inside a bracket runs as one operation in its own order"""),
code("""A, B, C = (Leaf(n, left_matrix(tuple(F(int(i == k)) for i in range(16)))) for n, k in (("A", 1), ("B", 2), ("C", 12)))
inner = Bracket([A, B], (2, 1))          # inside: B first, then A
outer = Bracket([inner, C], (2, 1))      # outside: C first, then the whole inner operation
print(notation(outer), "fires", fire_sequence(outer))
print("operator = A·B·C (C applied first):", _equal(operator(outer), _matmul(_matmul(A.matrix, B.matrix), C.matrix)))
print("parsed from text, round trip:", notation(parse("((A B | 2 1) C | 2 1)", {"A": A.matrix, "B": B.matrix, "C": C.matrix})))"""),
md("""## 3 · How many plans, and which orders they reach
`flat` = one bracket, any order (n!). `binary` = every bracket has two children, two orders each. `nary` = every bracket has at least two children and k! orders."""),
code("""print("n   flat    binary      nary   orders reached by written-order binary plans")
for n in range(2, 7):
    reach = len({tuple(fire_sequence(p)) for p in binary_plans([Leaf(str(i)) for i in range(n)])}) if n <= 5 else "—"
    print(f"{n}  {count_plans(n,'flat'):6d} {count_plans(n,'binary'):9d} {count_plans(n,'nary'):9d}   {reach}")"""),
md("""Written-order binary plans reach 6 of 6 orders for three leaves, **22 of 24** for four, **90 of 120** for five: the separable permutations (large Schröder numbers 6, 22, 90). With adjacent grouping a bracket cannot fire `2 4 1 3` or `3 1 4 2`. A bracket tree *restricts* which firing orders exist; that is a measured property of the notation."""),
code("""L = [Leaf(str(i)) for i in range(1, 5)]
reached = {tuple(fire_sequence(p)) for p in binary_plans(L)}
import itertools
print("missing orders:", sorted(set(itertools.permutations(['1','2','3','4'])) - reached))"""),
md("""## 4 · Two readings of a bracket
*Operator reading* (`operator`): composition of matrices is associative, so regrouping at the default order never changes the result; only the firing order does.
*Element reading* (`value`): the bracket is the algebra product of its fired children, folded left to right. The sedenion product is not associative, so **here the bracketing itself changes the result**."""),
code("""E1, E2, E3 = (Leaf(n, vec=tuple(F(int(i == k)) for i in range(16))) for n, k in (("A", 1), ("B", 10), ("C", 12)))
M1, M2, M3 = (Leaf(l.name, matrix=left_matrix(l.vec)) for l in (E1, E2, E3))
print("operator reading, ((A B) C) vs (A (B C)):", _equal(operator(Bracket([Bracket([M1, M2]), M3])), operator(Bracket([M1, Bracket([M2, M3])]))))
for x, y, z in itertools.permutations([E1, E2, E3]):
    l, r = value(Bracket([Bracket([x, y]), z])), value(Bracket([x, Bracket([y, z])]))
    print(f"element reading, (({x.name} {y.name}) {z.name}) vs ({x.name} ({y.name} {z.name})):", "same" if l == r else "DIFFERENT")"""),
md("""## 5 · The ring-circle triples, re-expressed as plans
Each slot is a circle element `3/5 + 4/5 e_k` (exact). Every triple of slots, every bracketing shape over every ordering, element reading. The earlier tables (`VAPMIP/RingCircle/`) found 35 triples giving 6 distinct results, 168 giving 8, 252 giving 12."""),
code("""from collections import Counter
def circ(k):
    v = [F(0)] * 16; v[0] = F(3, 5); v[k] = F(4, 5); return tuple(v)
cnt = Counter()
for t in itertools.combinations(range(1, 16), 3):
    leaves = [Leaf(f"e{k}", vec=circ(k)) for k in t]
    cnt[len({value(p) for p in permuted_shapes(leaves)})] += 1
print("triples by number of distinct results:", dict(sorted(cnt.items())))"""),
]
if which=="ssr":
    cells+= [md("""## 6 · The existing engine's rule is one policy
`bracket_firing_engine.py` fires the smaller-norm child first (a tie breaks left). `plan_of_tree` writes that rule out as a plan: every bracket of the 31-node tree carries the order the rule gave it."""),
code("""from bracket_firing_engine import build_tree, firing_order, plan_of_tree
from emerger_spectrum import parse_vec
v = parse_vec("e1+e10")
print(notation(plan_of_tree(v)))
old = [n["path"] for n in firing_order(build_tree(v)) if n["dim"] == 1]
new = fire_sequence(plan_of_tree(v))
print("leaf firing order identical to firing_order():", [int(p.replace("L","0").replace("R","1"),2) for p in old] == [int(s[1:]) for s in new])"""),
md("""`policy_written` (always `1 2`) and `policy_reversed` (always `2 1`) are the other two obvious policies; any function of the node's vector and its two halves is a policy.""")]
nb=nbf.v4.new_notebook(); nb.cells=cells
nb.metadata={"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"}}
nbf.write(nb, sys.argv[2])
