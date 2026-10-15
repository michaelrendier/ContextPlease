# Addition-matrix columns as rotors: orbit and ring-theory checks (2026-10-14)
Question (Cody): can each diagonal of the addition matrix be an orbit of orbits like Enigma rotors; is that ring theory; what are the dynamics. `orbits.py` (stdlib, exact), output in `output_orbits.txt`.
[MEASURED] 1. x -> a x + b on Z/10^m: the cycle type equals the CRT product of the cycle types on Z/2^m and Z/5^m (a cycle of length l1 times a cycle of length l2 gives gcd(l1,l2) cycles of length lcm), for all 336 maps tried (m<=4), units and non-units. FAULT KEPT: the first cycle-type function only worked for permutations and reported 117 false failures, all non-unit multipliers.
2. The first-return map of the odometer x -> x+1 on Z/10^m to {x = 0 mod 10} is the odometer on Z/10^(m-1) via x/10 (m = 2,3,4): exact self-similarity.
3. The digit at global column c of num1*(num2+t) is periodic in t with period exactly 10^(c+1)/gcd(num1, 10^(c+1)) (8 values of num1, c = 0..3).
4. Odometer, x->3x+1 and x->5x+7 on Z/2^n are solenoidal (tree automorphisms) and have only power-of-two cycle lengths; x->2x+1 on Z/5^n has cycles of length 1, 4, 20, 100, 500: not a 5-group.

## law_and_address.py (added same day)
Live-state count of the factor search at column c = number of solutions of pq ≡ N (mod 10^(c+1)), exactly (6 N tested). For v2(N), v5(N) < c+1 that count is (v2+1)(v5+1)·φ(10^(c+1)) = (v2+1)(v5+1)·4·10^c: unit-group torsors, ×10 per column. "final_answer address" test (n=3, 60 products): the true pair is exactly the K=0 overflow origin (2 of 400 unit solutions, pair + swap), but near-misses |K|=1..14 exist, so it is addressed but not isolated by the group's own coordinates. Output: output_law_and_address.txt.
