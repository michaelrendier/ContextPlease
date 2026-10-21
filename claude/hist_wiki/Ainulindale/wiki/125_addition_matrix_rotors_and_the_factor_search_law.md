# 125 — The Addition Matrix as Rotors, and the Law of the Factor Search

**Built 2026-10-14.** Engine: `ValaQuenta/modules/addition_matrix/` (v1.0). Follows [[124_basile_invertible_location_maps]] (another invertible address map) and the Multiplication Matrix Explorer's own `factor_reconstruction.py`.

---

## Origin

Cody, 2026-10-14, while the Collatz parity-shift paper was being finished: whether the diagonals of the addition matrix can be *orbits of orbits*, like Enigma rotors; whether that is ring theory; "find the 'law' that's sitting in plain view with the orbit of orbits for the addition matrix machinery"; and then "i want to know if those orbits of orbits are found at a 'final_answer' address". Afterwards: "i'm aware of the odometer nature of the 'address'... i would still like that mechanism included".

## What changed

The Explorer's factor search had measured a ×10 growth of live states per added digit (2026-09-26) and called it a law of the search. It is a count of solutions of one congruence, and the count has a closed form:

- the digit-by-digit search keeps exactly the pairs (p, q) mod 10^(c+1) with p·q ≡ N there;
- by the Chinese remainder theorem that count is a product over the primes 2 and 5;
- for N with both valuations below c+1 it is (v₂+1)(v₅+1)·φ(10^(c+1)) = (v₂+1)(v₅+1)·4·10ᶜ. The ×10 per digit is the order of the unit group (ℤ/10ᵏ)ˣ. The solution set is (v₂+1)(v₅+1) torsors of that group, acting by (p, q) → (u·p, u⁻¹·q), and every solution has exactly ten lifts.

So the "orbit of orbits" is the ring ℤ/10ᵏ = ℤ/2ᵏ × ℤ/5ᵏ: two stacks of wheels. The odometer x → x + 1 returns, on the multiples of 10, to the odometer one scale down. It is the adding machine on the 10-adics and is self-similar, like a rotor stack that carries into the next rotor. The digit in column c is one such wheel with exact period 10^(c+1)/gcd(num1, 10^(c+1)).

## The address

The question was whether the final answer has an address in that structure. It does: for a unit solution mod 10ⁿ, K = (p′q′ − N)/10ⁿ is an integer, and the true factorisation into two n-digit numbers is exactly K = 0. It is also not isolated. In 30 products of 3-digit primes, each N had 400 unit solutions and exactly 2 with K = 0 (the pair and its swap), while other solutions had |K| as small as 1. The group's own coordinates do not single the true pair out in advance; what separates it is the size constraint in the high columns.

## Honest boundaries

- The engine is not a factoring method. The live-state count is the cost of the search.
- The closed form for N divisible by 2ᵏ or 5ᵏ is exhaustively checked for k ≤ 3 and N in [0, 2·10ᵏ+50), and for six chosen N; it is not proved in the wiki.
- The wheels are bijections only for `num1` coprime to 10; for other `num1` the column map is many-to-one and the code raises.
- Digit-by-digit (branch-and-prune) recovery from low-order digits or bits exists in the literature (Heninger and Shacham 2009, for RSA keys with random bits revealed). That paper is cited as `Post-Hoc:`; the engine does not claim the technique.

## Links

[[ValaQuenta/wiki/addition_matrix]] · notebooks `ValaQuenta/notebooks/addition_matrix/` · paper stub `FourthAgePapers/AdditionMatrixOrbits/` · Explorer wiki `MultiplicationMatrixExplorer/wiki/` · [[../../FourthAgePapers/CollatzShift/README]] (the odometer and 2-adic maps).
