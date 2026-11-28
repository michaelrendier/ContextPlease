# 116 — Post's Lattice: How Few Operations Generate Everything

| | |
|---|---|
| Scope | Post's classification of Boolean clones as the established precedent for the question the Operator Tree / tier-0 floor asks: which minimal set of operations generates all operators and operations |
| Intake | citation pass, 2026-09-04 session; [98](98_provenance_and_citations.md). **Independent parallel**: the question was reached from the generational-lineage side and is the clone-theory question Post settled for the Boolean case |
| Verification (2026-11-13) | Post 1941 (*Annals of Mathematics Studies* 5, Princeton) and Lau 2006 (Springer) are books and were not machine-verified. The completeness criterion was reproduced by running it (Listing 1) |
| Confidence | the citations as recorded · Post's criterion: ESTABLISHED (re-run) · the mapping of the tier-0 floor onto clone theory: `INTERPRETATION` |

## 1. The references

- **[Post1941]** E. L. Post, *The Two-Valued Iterative Systems of Mathematical Logic*, *Annals of Mathematics Studies* 5 (Princeton UP, 1941): the complete, countably infinite **lattice of clones** of Boolean functions: every set of logical operations closed under composition and projection, ordered by inclusion, with all generating sets classified (the "Post classes").
- **[JablonskiGavrilovKudryavtsev1966]** (the Russian monograph on the algebra of logic and Post classes); **[Lau2006]** D. Lau, *Function Algebras on Finite Sets* (Springer): the k-valued generalisation; for k ≥ 3 the clone lattice is no longer countable or tidy (Janov–Mučnik 1959), but the "minimal generating systems" programme is the same.

## 2. A criterion run in code  `ESTABLISHED`

Post's completeness criterion: a set of Boolean functions generates all Boolean functions iff it is not contained in any of the five maximal clones T₀ (preserves 0), T₁ (preserves 1), the monotone functions, the self-dual functions and the affine (linear over GF(2)) functions.

**Listing 1 — the five classes and completeness** (written for this page; python3 standard library; runs cold)

```python
import itertools
def classes(f, n):
    pts = list(itertools.product((0, 1), repeat=n)); val = {x: f(*x) for x in pts}
    t0 = val[(0,) * n] == 0; t1 = val[(1,) * n] == 1
    mono = all(val[x] <= val[y] for x in pts for y in pts if all(a <= b for a, b in zip(x, y)))
    selfdual = all(val[tuple(1 - a for a in x)] == 1 - val[x] for x in pts)
    anf = dict(val)                                            # algebraic normal form via the Moebius transform over GF(2)
    for i in range(n):
        for x in pts:
            if x[i]: anf[x] ^= anf[tuple(0 if j == i else x[j] for j in range(n))]
    affine = all(sum(x) <= 1 or anf[x] == 0 for x in pts)
    return dict(T0=t0, T1=t1, monotone=mono, selfdual=selfdual, affine=affine)
fs = {'AND': (lambda a, b: a & b, 2), 'OR': (lambda a, b: a | b, 2), 'XOR': (lambda a, b: a ^ b, 2), 'NOT': (lambda a: 1 - a, 1),
      'NAND': (lambda a, b: 1 - (a & b), 2), 'NOR': (lambda a, b: 1 - (a | b), 2), 'CONST1': (lambda: 1, 0), 'MAJ3': (lambda a, b, c: (a & b) | (a & c) | (b & c), 3)}
names = ['T0', 'T1', 'monotone', 'selfdual', 'affine']
print('%-7s %s' % ('', ' '.join('%-9s' % n for n in names)))
for k, (f, n) in fs.items(): c = classes(f, n); print('%-7s %s' % (k, ' '.join('%-9s' % c[m] for m in names)))
complete = lambda keys: all(any(not classes(*fs[k])[m] for k in keys) for m in names)
for ks in (['NAND'], ['NOR'], ['AND', 'NOT'], ['OR', 'NOT'], ['AND', 'OR'], ['XOR', 'AND'], ['XOR', 'AND', 'CONST1'], ['MAJ3', 'NOT']):
    print('complete (generates all Boolean functions):', ks, '->', complete(ks))
```

```
        T0        T1        monotone  selfdual  affine   
AND     True      True      True      False     False    
OR      True      True      True      False     False    
XOR     True      False     False     False     True     
NOT     False     False     False     True      True     
NAND    False     False     False     False     False    
NOR     False     False     False     False     False    
CONST1  False     True      True      False     True     
MAJ3    True      True      True      True      False    
complete (generates all Boolean functions): ['NAND'] -> True
complete (generates all Boolean functions): ['NOR'] -> True
complete (generates all Boolean functions): ['AND', 'NOT'] -> True
complete (generates all Boolean functions): ['OR', 'NOT'] -> True
complete (generates all Boolean functions): ['AND', 'OR'] -> False
complete (generates all Boolean functions): ['XOR', 'AND'] -> False
complete (generates all Boolean functions): ['XOR', 'AND', 'CONST1'] -> True
complete (generates all Boolean functions): ['MAJ3', 'NOT'] -> False
```

NAND and NOR are each complete (they escape all five classes); {AND, OR} is not (monotone); {XOR, AND} is not (both preserve 0, so T₀) until the constant 1 is added; {MAJ₃, NOT} is not (both are self-dual). This is the exact sense in which "adding a generator is a real claim about the lattice, not a convenience".

## 3. What it anchors  `INTERPRETATION`

- **The Operator Tree** (`GenerationalLineage/wiki/The-Operator-Tree.md`): every named operation reduced, by the four-part tier test, to compositions of exactly three tier-0 generators, **ADD, SCALE, SIGN**, the Aff(1, ℝ) = ADD ⋊ (SCALE × SIGN) floor ([107](107_add_scale_sign_datatype.md)). The analogue of Post's question, with the group Aff(1, ℝ) in place of the Boolean clone lattice: the three generators are minimal in that none is generated by the other two (SIGN is a reflection, SCALE a dilation, ADD a translation; the group laws of [107](107_add_scale_sign_datatype.md) §3).
- The **three pillars** (`ROOT_OF` classes) and the discipline "nothing new is needed; the emergence signal is a measurement bar, not a naming licence" is the clone-theoretic stance: adding a generator is a claim about the lattice.
- The Σ / Π / ∫ "big operators" as iterated tier-0 folds over an index set: n-ary compositions, still inside the clone the floor generates.

The precedent is the *form* of the question and its answer for the Boolean case; the claim that the three tier-0 generators exhaust what the generational-lineage domain needs is scoped in [107](107_add_scale_sign_datatype.md) §9.

## 4. Cite in

`GenerationalLineage/wiki/The-Operator-Tree.md`; `GenerationalLineage/wiki/ADD-SCALE-SIGN-Datatype.md`; [107](107_add_scale_sign_datatype.md).

## 5. Related pages

[98](98_provenance_and_citations.md) · [107](107_add_scale_sign_datatype.md) · [118](118_citation_pass_2026_09_04.md)
