# 23 — The Resonant Recognition Model (Cosic) and its Ainulindale mapping

| | |
|---|---|
| Scope | Cosic's Resonant Recognition Model (RRM); the framework's mapping of it onto the HyperWebster/Riemann-zero picture; what is and is not tested |
| Code | `ValaQuenta/modules/tier9_chem/maths.py` (`EIIP`, `cosic_eiip`; equations `tier9_chem.cosic_eiip`, `cancer_zero_divisor`, `drug_targeting`, `hydro_radiolysis_chromatography`) |
| Confidence | ESTABLISHED as published work of Cosic and co-workers (not independently assessed here) · THEORETICAL (the mapping) |
| Citation status | **Not yet in the bibliography** (`98_provenance_and_citations.md`, `~/.clauderc_citations`): see §6 |
| Last verified | 2026-11-13: the EIIP table in §2 read from the code and `cosic_eiip` run; `addendum_VII` location checked |

## 1. The model

Irena Cosic (RMIT and Macquarie University) developed the Resonant Recognition
Model in the 1990s as a quantitative account of how macromolecules recognise
one another: not by lock-and-key shape complementarity but by a shared
frequency in the spectrum of their electron–ion interaction potential (EIIP)
along the sequence. In the model's own terms:

1. assign each amino acid its EIIP value, a single real number;
2. the protein sequence of length N becomes a real signal of N values;
3. take the discrete Fourier transform of that signal;
4. proteins with the same biological function share a common dominant
   frequency peak (the function's characteristic frequency), and two proteins
   interact when their peaks coincide.

The frequency is computed from the linear sequence, not the 3-D structure: in
the model the frequency is the invariant and the shape is a coordinate choice.
The model has been applied to hormone–receptor pairs, antibody–antigen
recognition, enzyme–substrate specificity and oncogene-related mutations.
Those applications are the author's published results; this repository has
not reproduced or independently assessed them, and the 2026-06 text's
"experimentally verified" is therefore reported as "reported by Cosic".

## 2. The EIIP values

Earlier versions printed a formula for EIIP in terms of a principal quantum
number and a molecular weight; that formula was garbled and is withdrawn. The
code uses Cosic's tabulated values, one per residue:

| Residue | EIIP | Residue | EIIP | Residue | EIIP | Residue | EIIP |
|---|---|---|---|---|---|---|---|
| L | 0.0000 | I | 0.0000 | N | 0.0036 | G | 0.0050 |
| V | 0.0057 | E | 0.0058 | P | 0.0198 | H | 0.0242 |
| K | 0.0371 | A | 0.0373 | Y | 0.0516 | W | 0.0548 |
| Q | 0.0761 | M | 0.0823 | C | 0.0829 | S | 0.0829 |
| T | 0.0941 | F | 0.0946 | R | 0.0959 | D | 0.1263 |

(`tier9_chem.maths.EIIP`; the module comment attributes the table to "Cosic
1994, Biophysical Journal"; the journal attribution is unverified, §6.)

**Listing 1 — the RRM computation on a sequence** (the DFT step of
`cosic_eiip`, written for this page with the code's table; runs cold with
NumPy)

```python
import numpy as np

EIIP = {'A': 0.0373, 'R': 0.0959, 'N': 0.0036, 'D': 0.1263, 'C': 0.0829,
        'Q': 0.0761, 'E': 0.0058, 'G': 0.0050, 'H': 0.0242, 'I': 0.0000,
        'L': 0.0000, 'K': 0.0371, 'M': 0.0823, 'F': 0.0946, 'P': 0.0198,
        'S': 0.0829, 'T': 0.0941, 'W': 0.0548, 'Y': 0.0516, 'V': 0.0057}

def eiip_spectrum(seq):
    x = np.array([EIIP[a] for a in seq])
    x = x - x.mean()
    power = np.abs(np.fft.rfft(x)) ** 2
    freqs = np.fft.rfftfreq(len(x))
    k = int(np.argmax(power[1:])) + 1
    return freqs[k], power[k]

print(eiip_spectrum('CPYCGHCGLVCEH'))
```

```
(0.3076923076923077, 0.05059040940198146)
```

The call returns (dominant frequency, its power) for the iron–sulfur-site
motif the module analyses; the first value is in cycles per residue
(0.3077 = 4/13). A 13-residue signal has so few frequency bins that any
claim of a unique "characteristic frequency" from one motif is weak by
construction; the published RRM uses whole-family consensus spectra.

## 3. The framework's mapping  `THEORETICAL`

| Resonant Recognition Model | Ainulindale reading |
|---|---|
| amino-acid sequence | surface form (input string) |
| EIIP value per residue | character address, as in the Horner encoding |
| Fourier transform of the EIIP sequence | the H_NN eigenvalue at that address |
| dominant resonant frequency | the zero γₙ at σ = ½ |
| two proteins sharing a peak | two surface forms sharing a zero |
| coupling strength | the running α_NN(l) |
| biological water cage | B̂_p, the Fermat constraint surface |
| conservation at the interaction | the Noether balance (J_red + J_blue + J₃ = 0; sign convention open, [133](133_canonical_maths.md) §3) |

The `cosic_eiip` equation states the identification as f* · (2π L)/c_bio = γₙ,
with L the protein length and c_bio a "biological propagation speed", and
reports that the SOR iron–sulfur motif's dominant frequency maps to γ₃ =
25.010…. **c_bio has no independent value**: with a free scale constant and
twenty or so zeros to choose from, a match to some γₙ is expected, so the
reported γ₃ is a fit, not a test. The mapping is a proposal; "H_NN eigenvalue
= EIIP" is marked "formal mapping pending" in the earlier table and stays so.

The chain the framework draws (Cayley–Dickson algebra → H_NN spectrum → EIIP
as a projection onto the amino-acid alphabet → Fourier transform as
eigenmode decomposition → resonant frequency → molecular recognition →
stable networks → life) is a narrative of the correspondence. Its first link
used the phrase "Dixon's theorem", which overstated a published proposal
([19](19_cayley_dickson_tower.md) §3). "Life is the eigenvalue" is the
framework's motto, not a result.

## 4. Water cage, cancer, and the Hagedorn ceiling  `interpretation`

- **The water cage.** Biological water forms pentagonal and hexagonal
  clathrate cages around proteins. The framework reads them as the Blue
  channel at molecular scale: the Fermat constraint at atomic scale (Pauli
  exclusion) scaling up to molecular (fold stability) and biological (cage
  geometry), the same constraint at different depths of the tower. Whether the
  cages sustain resonance between EIIP frequencies is a proposal of the model
  (marked "theoretical (Cosic)" in the earlier table).
- **Cancer as detuning.** Cosic reports that oncogenic point mutations shift
  the EIIP spectrum. The framework reads a cancer-causing mutation as a phase
  error: the word has changed its prime and resonates with a different zero,
  and conservation is violated locally. The `cancer_zero_divisor` equation
  encodes "healthy = one dominant frequency, cancer = several with none
  dominant". The therapeutic corollary, drug design as frequency correction
  and not shape matching, is the model's, and the module's `drug_targeting`
  equation is a computation under that model, not clinical evidence. Nothing
  here is medical guidance.
- **The Hagedorn ceiling.** ω_H = e^π = 23.14069… (neural Planck units), so
  2/ln ω_H = 2/π, the prefactor of L_NN ([04](04_lagrangian_engine.md)): that
  arithmetic holds. The further claim, that ω_H corresponds to about 37 °C and
  that life operates there because the prefactor closes the U(1) cycle, has no
  derivation on this page; it is an interpretation, and the earlier text's
  "this is not a coincidence" is withdrawn as a statement of fact.

The conjecture's §VII (hydro-radiological chromatography) is the macroscopic
version of the same idea: Life(Ratio) = (π/h) ⊗ [5,6]_lattice with
G:A:V = 60:30:10 = 6:3:1, the pentagonal/hexagonal lattice being the cage
geometry. See `FourthAgePapers/addenda/addendum_VII_library_convergence.md`
(the earlier link pointed at a path that does not exist).

## 5. Status

| Component | Status |
|---|---|
| EIIP spectrum assignment | ESTABLISHED (Cosic, 1990s) |
| Frequency matching between functionally related proteins | reported by Cosic; not reproduced here |
| Oncogenic frequency shift | reported by Cosic; not reproduced here |
| Water cage as resonance medium | THEORETICAL (Cosic) |
| EIIP ↔ H_NN correspondence | THEORETICAL (this work); formal mapping pending |
| SOR motif → γ₃ | a fit with a free scale; not a test |
| Life as the Hagedorn fixed point | THEORETICAL |

## 6. Citations to add

Cosic's work is named throughout the wiki and is absent from the bibliography.
To be downloaded and verified under the Literature Download Protocol, then
added to [98](98_provenance_and_citations.md) and `~/.clauderc_citations`:
Cosic, I. (1994) "Macromolecular bioactivity: is it resonant interaction between
macromolecules? — theory and applications", *IEEE Trans. Biomed. Eng.* 41(12);
and Cosic, I. (1997) *The Resonant Recognition Model of Macromolecular
Bioactivity*, Birkhäuser. Both are given from memory and are **unverified
until the title page is read**; the code comment's "Biophysical Journal" does
not match them.

## 7. Related pages

[14 RedBlue Hamiltonian](14_redblue_hamiltonian.md) · [18 Fermat lattice](18_fermat_lattice.md) ·
[19 Cayley–Dickson tower](19_cayley_dickson_tower.md) · [20 Three-phase architecture](20_three_phase_architecture.md) ·
[98 Provenance and citations](98_provenance_and_citations.md)
