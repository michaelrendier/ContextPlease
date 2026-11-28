# 46 — Inertia and entropy: the atomic decomposition, and its first test

| | |
|---|---|
| Status | **First capture (2026-06-08, "revolutionary result, immediate paper"); `CONJECTURE`.** The decomposition is a reading of standard chemistry in the framework's vocabulary. Prediction P1 was computed on 2026-11-13 and **fails** (r = 0.006 against the stated threshold r > 0.90); P2–P4 need data not held locally and have not been run |
| Predecessors | [22](22_constant_facets.md), [18](18_fermat_lattice.md), [45](45_t_transformer_the_circle_itself.md) |
| Paper directory | `FourthAgePapers/InertiaEntropy/` (README: "theory first-captured, pre-registration pending") |
| Code | Listing 1 (P1 and the microstate counts); the project's chemistry engine is `ValaQuenta/modules/tier9_chem` ([23](23_resonant_recognition.md)) |
| Last verified | 2026-11-13: Listing 1 executed |

## 1. The decomposition  `interpretation`

Chemistry is read as the study of *stability*: which configurations are stable
fixed points of the Noether current at σ = 1. The atom is a fixed point that
decomposes as

```
nucleus            = Red channel  R̂_p = inertia  = "what is"
electron orbitals  = Blue channel B̂_p = entropy  = "what cannot be"          R̂† = B̂
```

The nucleus carries ≥ 99.9% of the mass, supplies the Coulomb potential, does
not take part in chemistry (nuclear reactions are MeV, chemical ones eV) and
"anchors the frame"; Z is "the inertial mass of the atom in the chemical sense".
The electrons occupy wave functions, explore the phase space around the anchor,
seek the lowest free energy and are the active participants. The Pauli
exclusion principle is read as the Fermat-lattice constraint at atomic scale
([18](18_fermat_lattice.md)), and Δx·Δp ≥ ℏ/2 as the inertia–entropy
complementarity (the nucleus: heavy, Δx ≈ 0, "nearly pure inertia"; the electron:
light, Δx = orbital size, "nearly pure entropy"). All of this is
descriptive vocabulary; the physics underneath it (Born–Oppenheimer separation of
nuclear and electronic motion, the exclusion principle, the uncertainty relation) is
standard and `ESTABLISHED`. "Entropy" in the page is used for the *spread of the
electronic wave function*, which is not the thermodynamic or the
Gibbs–Shannon entropy of a state; §3 shows that this matters.

## 2. Correction: periods are not 2n²

The page says the row lengths of the periodic table are "2, 8, 18, 32 = 2n²".
Those are the **shell capacities** 2n² for n = 1…4. The period lengths are
**2, 8, 8, 18, 18, 32, 32** (the Madelung filling order fills 4s before 3d, 5s before
4d, and so on); each is 2 × (the number of orbitals filled in that period), where
the sequence of orbital counts runs 1, 4, 4, 9, 9, 16, 16. "Each row is a level of
the entropy hierarchy" is therefore a statement about shells and not about rows.

The orbital-block mapping (s: 1 orbital ↔ U(1) ↔ ℂ; p: 3 ↔ SU(2) ↔ ℍ; d: 5 ↔ SU(3) ↔ 𝕆;
f: 7 ↔ G₂ ↔ the imaginary octonion units) is a numerology of the orbital counts
1, 3, 5, 7: the counts are those of ℓ = 0…3 (2ℓ + 1). The proposed assignments to gauge
groups are not derived; the orbital angular-momentum algebra is SU(2)/SO(3) for every
block, and the standard-model gauge groups are not "entropy sub-structures" of
the orbital blocks. `CONJECTURE`.

## 3. Noble gases as "maximum entropy under constraint": the opposite holds

The page says closed shells are "not chemically inert because shells are full" but
"maximum entropy under the Pauli constraint: all accessible states occupied".
Counting microstates, a closed shell is the **minimum**-multiplicity
configuration: a single Slater determinant, one microstate (Listing 1). A
partially filled np shell with k electrons has C(6, k) microstates (1, 6, 15, 20,
15, 6, 1 for k = 0…6), and the configurational entropy ln C(6, k) peaks at the
half-filled shell (k = 3: 2.996) and is zero at k = 0 and k = 6. So noble gases are
at the entropy *minimum* in this sense. "Reactivity is the distance from the
entropy fixed point" cannot be a distance in configurational entropy; in the
standard account the inertness of a closed shell is an energetic property (a large
gap to excitation, high ionisation energy, low electron affinity).

## 4. Bonds and reactions  `interpretation`, with the thermodynamics stated

The page: a bond forms when the pair is a deeper fixed point than either atom;
covalent bonding is "shared entropy" (orbital overlap creating states across both
nuclei; "the bond *is* the entropy gain"), ionic bonding "transferred entropy",
metallic "delocalised entropy", the hydrogen bond "partial entropy sharing"; a
reaction is "entropy-gradient descent"; ΔG = ΔH − TΔS "is the inertia–entropy
balance written in thermodynamic notation".

Standing. ΔG = ΔH − TΔS is exact (`ESTABLISHED`), and "ΔG < 0 spontaneous, ΔG = 0 at
equilibrium" is standard. The assignment of ΔH to "nuclear Coulomb reorganisation
(the R̂ term)" and TΔS to "orbital reorganisation (the B̂ term)" is a
relabelling and is not exact: ΔH is the total heat of the reaction (electronic,
vibrational and nuclear-motion contributions), and the TΔS term is the
thermal entropy of translation, rotation and vibration, not the "orbital entropy".
The statement "all bonds are entropy phenomena" is contrary to the
standard account: the binding energy of a covalent bond is the lowering of the
*electronic energy* on overlap, and the entropy change of *forming* a bond between
two free fragments is usually negative (fewer translational and rotational
degrees of freedom). That the bond energy is "the entropy gain" is therefore not
the established mechanism. Activation energy as "the entropy barrier" and a
catalyst as lowering it without changing the endpoints: the latter is standard for a
catalyst (it lowers the barrier, not the thermodynamics); "entropy barrier" is a
relabelling of a free-energy barrier.

## 5. The four predictions

**P1 — reactivity correlates with distance from the noble-gas configuration**
(Pearson r > 0.90 against Pauling electronegativity, zero free parameters).
Stated before looking; computed on 2026-11-13 with the symmetric distance
d = min(electrons to add, electrons to remove) for the main-group elements
(H, Li–F, Na–Cl, K, Ca, Ga–Br; 22 elements; duplet for H, octet otherwise):

**Listing 1 — P1, and the microstate counts** (written for this page; runs
cold, Python 3.10+ for `statistics.correlation`)

```python
import math, statistics
from math import comb

EN = {'H': 2.20, 'Li': 0.98, 'Be': 1.57, 'B': 2.04, 'C': 2.55, 'N': 3.04, 'O': 3.44, 'F': 3.98,
      'Na': 0.93, 'Mg': 1.31, 'Al': 1.61, 'Si': 1.90, 'P': 2.19, 'S': 2.58, 'Cl': 3.16,
      'K': 0.82, 'Ca': 1.00, 'Ga': 1.81, 'Ge': 2.01, 'As': 2.18, 'Se': 2.55, 'Br': 2.96}
val = {'H': 1, 'Li': 1, 'Be': 2, 'B': 3, 'C': 4, 'N': 5, 'O': 6, 'F': 7, 'Na': 1, 'Mg': 2,
       'Al': 3, 'Si': 4, 'P': 5, 'S': 6, 'Cl': 7, 'K': 1, 'Ca': 2, 'Ga': 3, 'Ge': 4,
       'As': 5, 'Se': 6, 'Br': 7}
cap = lambda s: 2 if s == 'H' else 8
ys = [EN[s] for s in EN]
sym = [min(val[s], cap(s) - val[s]) for s in EN]          # the page's symmetric distance
print('P1: n=%d  r(symmetric distance, Pauling EN) = %.3f' % (len(ys), statistics.correlation(sym, ys)))
need = [-(cap(s) - val[s]) for s in EN]                    # exploratory, chosen after the fact
print('exploratory: r(-(electrons to complete the shell), EN) = %.3f' % statistics.correlation(need, ys))
print('p^k microstates C(6,k):', [comb(6, k) for k in range(7)])
print('ln C(6,k):', [round(math.log(comb(6, k)), 3) for k in range(7)])
```

```
P1: n=22  r(symmetric distance, Pauling EN) = 0.006
exploratory: r(-(electrons to complete the shell), EN) = 0.889
p^k microstates C(6,k): [1, 6, 15, 20, 15, 6, 1]
ln C(6,k): [0.0, 1.792, 2.708, 2.996, 2.708, 1.792, 0.0]
```

**Result: P1 fails** (r = 0.006 against the stated r > 0.90). The reason is
visible in the definition: the symmetric distance gives the alkali metals and the
halogens the same value (one electron from a noble-gas configuration) while their
electronegativities are at opposite ends (Cs 0.79 against F 3.98). The
exploratory line uses a *signed* quantity, the number of electrons needed to
*complete* the shell, and reaches r = 0.889; that is the standard
chemical fact that electronegativity tracks how close an atom is to filling its
valence shell, it was chosen after seeing the failure, and it is not a
prediction. Both lines are recorded. (The set excludes the noble gases, which have
no Pauling electronegativity for He, Ne, Ar, and the transition metals, for which
the shell definition used here does not apply.)

**P2 — bond energy proportional to orbital entropy change** (dataset: NIST CCCBDB).
**P3 — drug affinity correlates with orbital entropy complementarity**
(ChEMBL/BindingDB; 100 drug–target pairs against docking). **P4 — cancer
entropy signature in electron-transport expression** (TCGA, 33 cancer types).
These require data and a definition of "orbital entropy", "entropy
complementarity" and "entropy signature" that the page does not give (for P1 the
definition had to be supplied, and the result depended on it). They have **not
been run**, and none can be registered until the quantities are defined in code
before the data are examined.

## 6. Drug design and cancer  `hypothesis`, not medical content

The page proposes "entropy matching" in place of shape complementarity for
drug discovery ("the molecule whose B̂ field is the exact adjoint of the
target's R̂ field at the binding site"), and cancer as "a deranged entropy
landscape": a local σ-face that lost contact with the global σ = ½, an
operation "at the wrong entropy minimum", with the drug "built from the
cancer's own signature" and driving the landscape "toward σ < ½ (Fermat space,
structurally non-existent)". These are hypotheses in the framework's
language. Standard drug design already uses electronic-structure
(orbital) information beyond shape (quantum-mechanical scoring, pharmacophore and
electrostatic complementarity), so "shape is a subset of entropy" is not a distinguishing claim.
Nothing here is medical guidance, and no result supports a therapeutic claim. The
D-CHEM premise (the collaboration of the 2026-06 plan, [26](26_TODO_and_roadmap.md))
is recorded as a plan.

## 7. Connections

| Page | Link as the earlier page stated it | Standing |
|---|---|---|
| [18](18_fermat_lattice.md) | Pauli exclusion = the Fermat constraint at atomic scale | interpretation |
| [22](22_constant_facets.md) | σ = 1 is the chemistry face; σ = e the thermodynamic face | interpretation (facet statuses there) |
| [38](38_fermat_riemann_negative_space.md) | B̂_p = what cannot be = orbital constraint | its basis was withdrawn |
| [45](45_t_transformer_the_circle_itself.md) | chemistry is the circle at σ = 1 | the author's thesis |
| Addendum VIII | nuclear mass = spectral distance from the flat boundary | not re-checked here |

## 8. Related pages

[18 Fermat lattice](18_fermat_lattice.md) · [22 Constant facets](22_constant_facets.md) ·
[23 Resonant recognition](23_resonant_recognition.md) · [45 The T_transformer](45_t_transformer_the_circle_itself.md) ·
[47 The two trees](47_the_two_trees.md)
