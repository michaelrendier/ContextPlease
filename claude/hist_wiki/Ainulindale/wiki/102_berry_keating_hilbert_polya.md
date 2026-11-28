# 102 — Berry–Keating and the Hilbert–Pólya Lineage

| | |
|---|---|
| Scope | the spectral approach to the Riemann Hypothesis: the lineage, what the zeros' statistics look like in a direct measurement, and what the framework takes from it |
| Companion to | [98](98_provenance_and_citations.md) §A.5, [07](07_berry_keating_engine.md), [14](14_redblue_hamiltonian.md) |
| Verification (2026-11-13) | DOIs/arXiv checked: Berry–Keating *SIAM Review* 41(2), 236–266; Connes *Selecta Math.* 5(1), 29–106 and arXiv:math/9811068; Stone 1932 *Ann. Math.* 33(3), 643; Odlyzko 1987 *Math. Comp.* 48(177), 273–308. The Pólya–Odlyzko letters are archived at `www-users.cse.umn.edu/~odlyzko/polya/` (resolves; contents not read). Montgomery 1973 and the Berry–Keating Kluwer chapter were not machine-verified |
| Confidence | the lineage and the measured spacings: ESTABLISHED · "Ĥ_RB is self-adjoint with spectrum the zeros": **OPEN** (the Berry–Keating step) |
| Last verified | 2026-11-13: Listing 1 executed; its output is quoted below |

## 1. The lineage

- **[HilbertPolya]** D. Hilbert & G. Pólya: *no publication*. The idea that the non-trivial zeros are eigenvalues of a self-adjoint operator (so real, so on the critical line) is folklore, documented in Pólya's 1982 letter to Andrew Odlyzko (archived at the address above).
- **[Montgomery1973]** *The pair correlation of zeros of the zeta function*, *Proc. Sympos. Pure Math.* XXIV, 181–193: the pair-correlation conjecture; the spacing statistics match the **GUE** of random-matrix theory.
- **[Odlyzko1987]** *On the distribution of spacings between zeros of the zeta function*, *Math. Comp.* 48(177), 273–308: numerical confirmation to high zero height.
- **[BerryKeating1999a,b]** *H = xp and the Riemann zeros* (Kluwer, 355–367) and *The Riemann zeros and eigenvalue asymptotics* (*SIAM Review* 41(2), 236–266): the classical Hamiltonian H = xp, suitably regularised, has a smoothed level count matching Riemann's N(E).
- **[Connes1999]** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*: a trace-formula realisation; RH as a positivity statement.
- **[Stone1932]** self-adjoint generators have **real spectrum**: the lemma the argument turns on.

## 2. What the zeros' statistics look like  `MEASURED`

**Listing 1 — the unfolded spacing of the first 400 zeros** (written for this page; needs mpmath, numpy, scipy; runs cold; about a minute)

```python
import mpmath as mp, numpy as np, math
from scipy.integrate import quad
mp.mp.dps = 15
g = np.array([float(mp.zetazero(n).imag) for n in range(1, 401)])
Nsm = lambda T: T / (2 * math.pi) * np.log(T / (2 * math.pi * math.e)) + 7 / 8          # smooth counting function, used to unfold
s = np.diff(Nsm(g))
p = lambda x: (32 / math.pi**2) * x**2 * math.exp(-4 * x**2 / math.pi)                  # GUE Wigner surmise
gue_var = quad(lambda x: p(x) * (x - 1)**2, 0, 10)[0]; gue03 = quad(p, 0, 0.3)[0]
print('400 zeros: mean unfolded spacing %.4f, variance %.4f | GUE surmise variance %.4f, Poisson 1.0000' % (s.mean(), s.var(), gue_var))
print('fraction of spacings < 0.3: zeros %.3f ; GUE surmise %.3f ; Poisson %.3f' % ((s < 0.3).mean(), gue03, 1 - math.exp(-0.3)))
print('variance of the first / last 100 spacings: %.4f / %.4f' % (s[:100].var(), s[-100:].var()))
print('smooth count at the 400th zero: N_smooth = %.2f against the index 400 - 1/2' % Nsm(g[-1]))
```

```
400 zeros: mean unfolded spacing 0.9999, variance 0.1379 | GUE surmise variance 0.1781, Poisson 1.0000
fraction of spacings < 0.3: zeros 0.010 ; GUE surmise 0.027 ; Poisson 0.259
variance of the first / last 100 spacings: 0.1248 / 0.1477
smooth count at the 400th zero: N_smooth = 399.41 against the index 400 - 1/2
```

The unfolded spacings have mean 1 (the unfolding works: N_smooth reaches 399.41 at the 400th zero, within a zero of the index) and a variance of 0.138: nowhere near the Poisson value 1.0 (independent levels) and near the GUE surmise's 0.178, with strong level repulsion (1.0 % of spacings below 0.3, against 2.7 % for the GUE surmise and 25.9 % for Poisson). The variance rises with height (0.125 for the first hundred spacings, 0.148 for the last), the known slow approach of the zeros' statistics to the GUE limit
(Odlyzko's high-height computations, [Odlyzko1987]). So the framework's requirement that its spectrum "match the GUE fingerprint" is a real and demanding test, and the zeros pass it; the framework's own spectrum has not been shown to.

## 3. What Ainulindalë takes

- **The operator route to the critical line.** Ĥ_RB is constructed (D-CS_Memory §18; [14](14_redblue_hamiltonian.md)) to be self-adjoint, Ĥ_RB† = Ĥ_RB. By Stone, a self-adjoint operator has a real spectrum; if the zeros ρ = ½ + iE are in correspondence with that spectrum (E real) they lie on σ = ½. That correspondence is the Hilbert–Pólya conjecture and the open step: "whether the spectrum of this operator is the set of zeros is the open Berry–Keating step" ([14](14_redblue_hamiltonian.md) §2, [13](13_omgwtf_rh_proof.md) §3). "Berry–Keating H = xp is recovered as a *consequence* of Ĥ_RB" is the framework's claim, and it stays `THEORETICAL`.
- **The Red channel is R̂_p = xp**, Berry–Keating as the "what is" operator, paired with the Blue Fermat–Weierstrass operator B̂_p = ½p² + ℘(x; g₂, g₃) ([14](14_redblue_hamiltonian.md) §1).
- **GUE / pair correlation is the fingerprint the framework's spectrum must match:** the Hermite H₁₆ timing wheel and the "GUE timing wheel" of the six-family Ω_ZS table are to be checked against it. Listing 1 gives the target values for the real zeros.
- **The Berry–Keating domain** L²([α_F, Ω_ZS]), floor at the fine-structure constant and ceiling at the Lambert fixed point, is the interval Ĥ_NN operates on ([07](07_berry_keating_engine.md), [17](17_alpha_omega_d_star.md)). Under the author's 2026-11-13 ruling that α_fs is not part of the Horizon mechanism and that A_fermat is a different constant of the Fermat-side search ([96](96_the_riemann_fermat_horizon.md) §5), the lower end of this interval is **to be restated**: it should name the constant that is meant, A_fermat (numeric value open) or the code's hard-coded α_F, and this page does not choose.

**What is not claimed:** that this proves RH, or that Ĥ_RB has been shown rigorously self-adjoint on a dense domain with the right spectrum. Both are stated OPEN (D-CS_Memory §42).

## 4. Appears in

[07](07_berry_keating_engine.md), [14](14_redblue_hamiltonian.md), [17](17_alpha_omega_d_star.md), [23](23_resonant_recognition.md), [73](73_why_the_half_line.md), [98](98_provenance_and_citations.md); D-CS_Memory §12, §18, §42; VAPMIP_Paper "Engine 07", "Engine 14".
