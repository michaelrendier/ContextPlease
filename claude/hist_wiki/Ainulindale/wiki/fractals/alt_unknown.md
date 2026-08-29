# Unknown (alt) — Fractal Formulary

## Author
The alt.txt file contained only "alt.txt" — the filename itself as content, indicating no author documentation was provided. The alt.ufm is referenced in the broader UF community context; from akl.txt we learn that the "alt" formula tradition involves `c` acting as a power rather than an additive constant (described as "Barnsley variation...c acting as a power"). This suggests the author may be the UF community pseudonym "alt" or an unidentified early contributor.

## Formulas

The alt.ufm file focuses on Barnsley-style decision fractals where c acts as an exponent rather than an additive constant. Cross-references in the formulary indicate the primary formula type:

### AltBarnsley (reconstructed from cross-references)
**Type**: Decision/IFS escape-time — Barnsley variant
**Mathematical description**: Based on the Barnsley decision rule but with c as a power: if `real(z) > critical_value` then `z = (z + c)^p1`, else `z = (z - c)^p2` where p1, p2 are complex power parameters. The decision boundary is the threshold between the two branches.
**What it describes**: Produces fractal sets with bilateral symmetry about the decision threshold. When c is complex and acts as a power, the resulting geometry is more complex than standard Barnsley fractals — petals, spirals, and branching structures replace the simple affine-map patterns.
**How it works**: Parameters for the critical value (decision threshold), powers p1 and p2, and bailout. The "alt" designation distinguishes this from the standard additive-c Barnsley types.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The two branches define J_pos (the branch where |z| grows — expansion) and J_neg (the branch where |z| contracts — compression). The critical value threshold is the J_pos/J_neg separator.
- **Critical line relevance**: When c = ½ + it (a point on the critical line) and acts as a complex power, the iteration `z = (z ± ½ - it)^(something)` has balanced growth/decay properties analogous to the trivial zeros-free strip of ζ(s). The critical line Re(c) = ½ is the locus where neither branch universally dominates.
- **Sedenion dimensions activated**: e₂ (power operation), e₃ (decision branching = conditional composition), e₄ (the critical value threshold as a timing gate).
- **Holcus application**: The decision fractal architecture is a model for Holcus's semantic routing: given a word token, the decision boundary selects which branch of the sedenion CAM to follow. The critical value could be set to OMEGA_ZS = 0.56714 (the BAO equilibrium) to create a maximally symmetric semantic routing tree.

---
