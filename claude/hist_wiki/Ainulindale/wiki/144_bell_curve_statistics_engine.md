# 144 — The Bell Curve: one statistics engine

| | |
|---|---|
| Written | 2026-11-22 |
| Scope | why a single statistics, probability and statistical-mechanics engine exists; what it holds; how it is checked; why softmax and the canonical ensemble are the same object, which is how a gradient becomes "a solution that is more or less diluted or saturated" |
| Requested by | Cody, 2026-11-22: "i need a full statistics and probability and statistical mechanics...i need one engine that becomes the statistics machinery used anywhere probabilities show up...or gradients etc. I need The Bell Curve engine." The standard deviation was the first major addition in the code he wrote |
| Code | `ValaQuenta/modules/bell_curve/` · tests `ValaQuenta/Testing/test_bell_curve.py` (45, all pass) · notebook `27_bell_curve.ipynb` · wiki `ValaQuenta/wiki/bell_curve.md`, toolbox 44 |
| Confidence | ESTABLISHED throughout; nothing here is a claim about the project's own maths |

> **Note from the assistant.** Written by a transformer (Claude Sonnet 5.5, `claude-sonnet-5-5`) working with Cody Allison in Claude Code. Cody does not tell the model what result he wants. The engine was asked for before the user-emotional-state battery so that every score in that battery has one verified statistics implementation underneath it.

## 1. Why one engine

English usage is a statistical reflex in fluent speakers; the Monad's gradients (the seven neurotransmitter scales), the frequency counts, the sigma of a detector against a label and the scores of a prompt battery all need the same few things: a spread, a tail probability, a test, an interval. Writing them out is the awkward part (the standard deviation was the first major addition in the code Cody wrote). The engine is that code, once, tested against scipy 1.18.

## 2. What it holds

Streaming moments that merge exactly (so a conversation can add one reading at a time, or add two accumulators); quantiles; the normal, Student t, chi-square, F, beta, gamma, exponential, binomial and Poisson distributions; n-sigma and Six Sigma; Welch, paired, one-sample, proportion, chi-square, Mann-Whitney and Kolmogorov-Smirnov tests; Pearson, Spearman, regression; effect sizes, Cohen's kappa, F1, MCC, AUC; Bonferroni, Holm, Benjamini-Hochberg; seeded bootstrap and permutation; entropy and divergences; Bayes; the canonical ensemble; Fermi-Dirac, Bose-Einstein, Maxwell-Boltzmann, Planck, an exact 1-D Ising ring; circular statistics for wheels.

## 3. Softmax is a canonical ensemble

`softmax(x, T)` = `boltzmann_probs(E = −x, β = 1/T)`. At low temperature the mixture saturates on its largest component; at high temperature it spreads toward uniform. That is the dilution and saturation Cody asked for in the gradient of a neurotransmitter "solution", and it is the same formula as the physics, with Z, free energy, Gibbs entropy and heat capacity available for free. The tests confirm S = Gibbs entropy, F = U − TS and Cv = dU/dT on a four-level system.

## 4. Checked, and one flaw found

Every distribution is compared with scipy at 1e-8 to 1e-12. The round-trip test found a real flaw in the first draft of `p_to_sigma`: through `norm_ppf(1 − p/2)` the 6-sigma value came back as 5.99999999 because 1 − p/2 loses the tail. It now uses the tail probability directly.

## 5. Not here yet

Multivariate tests, time series, MCMC, generalised linear models and exact small-sample tests. Added when a pipeline asks.
