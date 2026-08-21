# Collatz as the 2-adic shift — measurements

2026-08-21. Cody asked: "multiple inputs to one small ordered loop... I see a
recursive decomposition on a modular function... what actually is it".

`collatz_probe.py` measures the six things the answer rests on. Shortcut map
throughout: T(n) = n/2 (even), (3n+1)/2 (odd).

1. The loop is {1,2}, period 2. Fixed points of T in ℤ are 0 and −1 only.
2. T^k is AFFINE on each residue class mod 2^k, slope 3^d/2^k with
   d = #odd steps, and d depends only on the class. Verified k = 1..4.
3. Q_k (parity vector) is a BIJECTION ℤ/2^k → ℤ/2^k and conjugates T to the
   binary shift. Verified exhaustively to k = 16 (65536 classes).
   This is Bernstein–Lagarias; here it is re-measured, not cited.
4. Every periodic parity word of length k with d ones gives exactly ONE
   rational cycle, denominator 2^k − 3^d. (k,d) = (2,1) is the only place
   that denominator is 1 — hence the only integer cycle in that family.
5. n has an odd predecessor ⟺ n ≡ 2 (mod 3). Multiples of 3 are leaves-only
   in the backward tree — the sieve_clock "orphan" regime, in the 3-tower.
6. Drift: predicted ½·log(3/2) + ½·log(1/2) = log(√3/2) = −0.143841.
   Measured over 5.52M steps of odd starts < 200000: −0.131172.
   The gap is a termination bias (trajectories are cut at 1), not a
   disagreement with the model — flagged, not papered over.

VERDICT (generational lineage): no new generator. T = ADD ∘ SCALE ∘ SIGN,
all three tier-0 irreducibles, coupled. See conversation for the tier table.
