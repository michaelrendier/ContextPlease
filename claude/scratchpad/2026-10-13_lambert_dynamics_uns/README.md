# 2026-10-13 — Lambert W as a fixed-point object, and its values in Universal Native Space
lambert_uns.py → output_lambert_uns.txt.  Four tests (W0 at 0, 1, -1/e; W-1 at -1/e) → three distinct values (double root); UNS values (divide by ln 10; in d*_taut units);
W as the negated fixed-point multiplier of exp(-lam x) / exp(lam x) (flip at lam=e, fold at lam=1/e); the fold as a projection; the cardioid cusp as multiplier +1.
Corrected during the session: a naive "4 distinct values" came from a 1e-41 evaluation error splitting the double root by ~5e-21; and the claim that the real map goes on to chaos is false (decreasing map).
