# 2026-10-12 — does w >> w* tear the box kite off the ZD surface?

Claim: ValaQuenta/wiki/pencil_hyperstring.md ("w >> w*: chart_of outside_share -> 1,
is_zero_divisor -> False"), status CONJECTURE, its test 5. Phi_w is not implemented
in the repo; test.py builds the literal reading (Joukowsky z -> z + c/z, c = H/q(w),
q = 1/2 rho w^2, on each Assessor vertex z = d+ + i d-). Open choices marked CHOICE.

Files: test.py (run: python3 test.py), output.txt (captured run).

Findings (see output.txt):
 A. c = H/q(w) -> 0 as w -> inf, so the map tends to the IDENTITY at large w, and
    blows up at small w. The page's sequence (w=0 collapse, large w tear) is not
    produced by the formula as written.
 B. A real zero divisor stays a zero divisor, outside_share = 0, at every w tested
    (0.01 .. 1000): Joukowsky preserves the real and imaginary axes of z = d+ + i d-,
    which is exactly where the diagonals sit. A mixed vector is NOT a ZD to begin with.
 C. The six-vertex "kite vector" (one diagonal per Assessor, 4096 sign/diagonal choices,
    strut 1): 0 of 4096 are zero divisors at baseline, so the page's "chart_of should
    report is_zero_divisor = True" cannot be met by this reassembly.
 Structural: indices e0, e8 belong to no Assessor, so no map acting inside Assessor
 planes can move energy onto them; outside_share -> 1 needs a step the page does not specify.
Verdict: tear-off is NOT reproduced; it is also not refuted for the real Phi_w, which
is under-specified (station generators g_k, circulations Gamma_k, reassembly).
