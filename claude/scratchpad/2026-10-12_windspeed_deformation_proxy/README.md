# 2026-10-12 — which parts of the box kite respond to a windspeed, and how it enters

Question (Cody): test what the A-Matrix Basin windspeed deforms before assuming it matches
the Gamma-Radial windspeed. Kite-string picture: windspeed varies, tension in the string
depends on the kite shape.

Method: the scalar-context-propagation paper's own PROXY (branch scalar-context-propagation,
repo_appendix/windspeed_reconstruction/07): H = Re(Pi), Pi = ordered product of the 7 pencil-station
generators, each cos(phi)e_a + sin(phi)e_b. H = string tension. Phi_w (sail-pressure/strut-angle
mechanics) is NOT built, stations are NOT Assessor vertices; this is a proxy, as the paper says.

Results (output.txt):
 1. Noether-path swing of H: struts 1,3,6 = 0 (pinned); 4 = 2.0 (-1 -> +1 -> -1); 2,7 = 1.2225; 5 = 0.3765.
 2. |dH/dphi_k| is identical across all 7 stations for a given strut (collective, not local).
 3. Non-uniform wind (rates scaled by 1+d*u_k): struts 1,3,6 gain swing 0.0032/0.0287/0.1874 at
    d = .05/.15/.4; struts 2,4,5,7 change only slightly.
 4. A time-varying SCALAR wind (gusts) only reparameterises the path: strut 1 stays at exactly 0 swing.
 5. NEW, numerically exact (<= 8e-16 over 200 random phase vectors per strut):
        H = -cos( sum_k eps_k^(s) * phi_k )
    eps (stations 1..7): struts 1,3,6 ++--++-  | 2,7 +--++--  | 4 +++++++  | 5 +-+-+-+
    Signed Noether rate sum S_s = sum eps_k (k+1)/7 * pi/2:
        1,3,6: 0 (pinned)  |  4: 2pi  |  2,7: -4pi/7  |  5: 2pi/7
    So the pinned set {1,3,6} is exactly where the signed rates cancel -- an answer to the paper's
    open question "why {1,3,6}", within this proxy. Fit, not proof.
Consequence: any SCALAR windspeed (Gamma-Radial or a scalar A-Matrix reading) moves only the single
phase and leaves 1,3,6 rigid. Rigid struts respond ONLY to a differential (per-station) wind.

## Follow-up (test2.py, output2.txt)
 A. The four distinct eps patterns are rows 0-3 of the Sylvester-Hadamard (Walsh) matrix on station
    index j = k-1 = 0..6 (strut 4 = row 0, strut 5 = row 1, struts 1,3,6 = row 2, struts 2,7 = row 3).
    The one-phase law H = -cos(sum eps*phi) also fits pencils r = 8, 9 (not Hadamard rows) and FAILS
    for r = 10..15 (err ~1.3). 40 random phase vectors per r, 128 sign patterns tried.
 B. Holding a subset of stations fixed (anchoring): 128 subsets -> 7 distinct groupings of the
    7 struts; {1,3,6} stay rigid under only 8 of 128 subsets.
 C. Same law spans the regimes: phi in {0,pi/2} -> H in {-1,0,1} (the paper's quantised lattice);
    phi on a pi/8 grid -> 9 distinct H values; phi real -> H fills [-1,1].
