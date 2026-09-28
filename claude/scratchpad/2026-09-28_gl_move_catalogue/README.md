# GenerationalLineage — catalogue of factoral-decomposition moves (2026-09-28)

Survey for "ready for public use". Read: GL README + engine/toolsets + wiki/Cipher.md,
ValaQuenta wiki/00_index + generational_lineage_map + Toolbox (38 pages, headings/APIs),
PtolemyDesktop/Kryptos (Pycrypt.py, analysis.py, Ciphers/*), MMExplorer README,
TuringStack, Tuning-the-Engine 06/26, Ainulindale wiki titles, un_sieve.
NOT read in depth: capacitor, prime_gate, understand, lexicon, corpus, telperion,
zero_lattice (index descriptions only). Nothing was executed (verify_all not re-run).

Tags: [GL] already in GenerationalLineage · [VQ] built in ValaQuenta, not yet a GL move ·
[KRY] in Pycrypt/Kryptos · [NEW] not in any repo I read.
Direction: D = descent (free, deductive) · A = ascent (paid, needs a choice/constraint).

## 0. What a "move" is

factor = whatever can be quotiented out while an invariant residual survives
(a period, a key length, a cycle type, a nilpotent part, a spectral line, a bracketing).
Contract already in GL: descend() free / build_up() paid / verify() / AscentNotFree.
Proposed extra gates every public move passes (all already practised somewhere in the repos):
 1. exact round-trip: recompose(decompose(x)) == x (scale.polar_round_trip; hyper_linear DFT)
 2. mandatory null baseline (angular_rank isotropic 4/16; udeo random-guess controls; zeta as control)
 3. degeneracy audit — "what does this statistic actually vary over?" (Tuning-the-Engine ph.26)
 4. epoch stamp on every measurement (angular_rank)
 5. tri-state status HOLDS / MATHS-FAULT / CODE-FAULT
 6. guarantee-first: exact/exhaustive beats sampled (prefix-function period > IoC estimate)
 7. decidability pre-check (turing_diagonal.prediction_diagonal_test) before hunting a factor

## 1. Taxonomy — kind of factor → canonical move

| kind of factor | canonical move | have? |
|---|---|---|
| integer / multiplicative | Two Trees, primary decomposition, sieve/un-sieve | [GL] |
| emergence | angular-rank nullity, ZD rank-deficiency, fall/survive | [GL]+[VQ] |
| process | pathway_decomposition, CRT fan-out, ping | [GL] |
| spectral signal | DFT lines, autocorrelation, residue | [GL] |
| periodic permutation | cycle type / order / lcm | [GL] partial |
| re-bracketing | Bell, Catalan, associator | [GL] Bell only |
| re-ordering | firing order, collisions | [GL] |
| periodic fn, modular (ℤ/m) | orders, Pisano, LCG, cyclotomic | [NEW] mostly |
| periodic fn, non-modular (spring) | log-polar unwrap, Mellin, rotation number | [NEW] |

## 2. Catalogue

### A. Number / multiplicative
A1 [GL] factor_lineage, primary_decomposition, fall_test, arith_deriv, euler_phi, von_mangoldt
A2 [GL] sieve_lineage, un_sieve (birth vs extinction; ΔH=+7.19 bits invariant)
A3 [GL] ping: trial, Fermat, p−1, p+1, ECM, Wiener, batch-gcd, Coppersmith
A4 [GL] hyper_linear (L_d∘T^r rows), stencil, comma_sequence, pathway_residues/tune, fermat_path
A5 [VQ] smoothness profile: fall_height ln gpf N, Dickman ρ(u), harvest Ψ(X/p,p), discovery ln lpf N
A6 [VQ] negative-space staircase: μ, Mertens M(x), envelope
A7 [VQ] splitting vector χ_N + ramified primes (Euler factor degenerates at the factors)
A8 [VQ] hypergon constructibility — Gauss–Wantzel: N = 2^k·distinct Fermat primes
A9 [NEW] multiplicative order / period of a^k mod N (classical shadow of Shor); Carmichael λ
A10 [NEW] Pollard rho (Floyd/Brent cycle finding on x²+c) — period detection as factoring
A11 [NEW] smooth-relation collection + GF(2) linear algebra (Dixon/QS) — GL has GF(2) trace-Laplacian
A12 [NEW] Pohlig–Hellman / Sylow: factor the GROUP ORDER, solve per prime power, CRT-glue
A13 [NEW] Euler-product move: multiplicative f(n)=∏f(p^a) — factor arithmetic functions locally
A14 [NEW] Möbius inversion on divisor lattice / Dirichlet convolution factorisation
A15 [MMA] carry-cascade moves: digit-by-digit LSB factor reconstruction (branch count = growth law),
     2-adic/trailing-zero reduction theorems, row-template shuffle basin, periodicity under +1 increment
A16 [NEW] continued-fraction decomposition (periodic CF ⇔ quadratic irrational; Wiener is one use)
A17 [VQ→NEW] radix moves: Horner bijection, Fano base-7 path, Zeckendorf, Stern–Brocot address

### B. Sequences / strings — exact periodicity & repetition (guarantee-first)
B1 [GL] repeat_distances + stem-vote (Kasiski = GCD-vote of gap multiset)
B2 [NEW] prefix/Z function, KMP borders → all periods, exactly (replaces the vote where a guarantee exists)
B3 [NEW] Fine–Wilf: periods p,q on length ≥ p+q−gcd ⇒ period gcd (the proof that the GCD-vote is right)
B4 [NEW] Lyndon (Chen–Fox–Lyndon) factorisation via Duval — the unique "prime factorisation" of a word
B5 [NEW] maximal repetitions / runs (Crochemore, Kolpakov–Kucherov; ≤ n runs)
B6 [NEW] necklace / Burnside–Pólya orbit counts under rotation
B7 [NEW] Burrows–Wheeler transform (sorted rotations) — periodicity shows as runs
B8 [NEW] grammar-based compression (Re-Pair, Sequitur): a straight-line program IS a lineage tree —
     nonterminal = node, depth = generation, |grammar| = Ω-analogue
B9 [NEW] LZ77/LZ78 phrase factorisation; Kolmogorov proxy
B10 [NEW] de Bruijn cyclic-window decomposition (Archimedes has the generator)
B11 [NEW] Berlekamp–Massey: shortest recurrence / linear complexity; LFSR period = lcm of orders
     of the minimal polynomial's irreducible factors (Kryptos LFSR.py is a 13-line generator only)
B12 [NEW] Pisano periods (Fibonacci/Lucas mod m): π(m)=lcm over prime powers — factoral by construction

### C. Spectral / signal
C1 [GL] dft, spectral_lines, reconstruct, spectral_residue, autocorrelation, dominant_period
C2 [GL] oscilloscope N-shape (N mod 16) + root-system pathway
C3 [VQ] angular-rank: 16-band log embedding, numerical rank, external component off a frozen span,
     bearing (drift), null occupancy — the emergence detector with mandatory null
C4 [VQ] spin/wobble split (spectral_primes): monotone phase θ'(t) vs oscillation carrying the primes
C5 [VQ] explicit-formula tones: ψ(x) rebuilt from zeros, interference profile, amplitude envelope 2√x
C6 [VQ] even/odd parity about a fixed point (sigma_expansion: only odd Taylor terms about σ=½)
C7 [VQ] inverse-Laplacian recovery (l_io_photon_path): Kaiser–Squires, Poisson solve, deflection=∇ψ
C8 [VQ] sonification: ω=pitch; beats & missing fundamental = GCD in frequency space
C9 [NEW] harmonic-series decomposition (harmonic product spectrum): continuous GCD-vote — IoC's cousin
C10 [NEW] cepstrum / homomorphic deconvolution: log turns convolutive (multiplicative) factors additive
     (GL already asserts "primary decomposition is cepstrum" as a check — make it a move)
C11 [NEW] Prony / matrix pencil / MUSIC / Hankel rank: exact damped-sinusoid lines; rank = factor count
C12 [NEW] SSA / singular-spectrum; Takens delay embedding; recurrence plots (diagonals = periodic orbits)
C13 [NEW] Lomb–Scargle (uneven sampling); wavelets / multiresolution (2-scale relation = SCALE by 2 + shift)
C14 [NEW] Walsh–Hadamard / ANF (Boolean spectra; Post-lattice clones — Ainulindale wiki 116)
C15 [NEW] Dirichlet characters = the Fourier transform on (ℤ/q)^× (GL already uses equidistribution as control)
C16 [NEW] Hilbert/analytic signal: instantaneous phase + envelope (= spin and wobble, generically)

### D. Periodic permutations
D1 [GL] permutation_cycles, order direct vs via stems (lcm = the join)
D2 [NEW] cycle type / conjugacy class; parity (= the SIGN irreducible); Lehmer code / factoradic index
     (the factorial number system IS a mixed-radix decomposition of a permutation)
D3 [NEW] Coxeter/reduced-word length; commutator & derived series
D4 [NEW] modular affine permutations x→ax+b mod m: cycle structure via multiplicative order; LCG
     period (Hull–Dobell); riffle in-shuffle order = ord_{2n+1}(2).
     Observation: ASS x↦sign·scale·x+add IS this affine group, so these are native objects.
D5 [NEW] Jordan–Hölder / Krull–Schmidt / Smith normal form / rational canonical form
D6 [NEW] Jordan–Chevalley x = x_semisimple + x_nilpotent (commuting) — pairs with t32_nilpotency
     and lineage's radical-units-split-GF(2)
D7 [NEW] Krohn–Rhodes: automaton = cascade of simple groups + reset components (process "prime factorisation")

### E. Re-bracketing / re-ordering
E1 [GL] Bell(n), set_partitions, firing orders, apply/collisions/would_collide (Recamán generalisation)
E2 [GL] jurisdiction_violation (legal op set per object)
E3 [VQ] associator (curvature) & commutator (torsion) fields; 168 quantised; 7 pencils/edge
E4 [NEW] Catalan / associahedron (Tamari flips = the pentagon); matrix-chain optimal bracketing
E5 [VQ→NEW] pregroup reduction (DisCoCat x^(a)x^(a+1)→1): bracketing that cancels; tensor contraction
E6 [NEW] Ritt / functional decomposition f = g∘h — the generational lineage of a FUNCTION
E7 [NEW] Knuth–Bendix rewriting / confluence (does bracketing order matter?)
E8 [NEW] partition-lattice Möbius function; integer partitions

### F. Periodic functions — the spring / geodesic family
F1 [VQ] log-polar fold/unfold: Γ = tanh(log(Z/Z₀)/2) exact; cross-ratio scale-blind; two-ring chart
F2 [NEW] log-periodic detection: Fourier in u=ln x (discrete scale invariance); a spring is θ=ωu, pitch=1/ω
F3 [NEW] Mellin transform — the Fourier transform of the SCALE group. ADD⋊SCALE has two dual
     transforms: Fourier (ADD) and Mellin (SCALE). Dirichlet series / Perron = Mellin.
F4 [NEW] phase unwrap + winding number / argument principle: the anti-flattening fix; integer factor
F5 [NEW] rotation number / circle map: p/q ⇔ periodic, irrational ⇔ quasi-periodic (mode locking);
     Farey / Stern–Brocot address of the tongue (Archimedes has Stern–Brocot); Arnold tongues = windows of order
F6 [NEW] quasi-periodic: two incommensurate periods — continued fraction of the frequency ratio
F7 [NEW] Floquet / Poincaré return map: periodic orbit → fixed point of a map
F8 [NEW] Chebyshev/Dickson: T_m∘T_n=T_{mn} — the periodic maps' composition semigroup is multiplicative
F9 [NEW] cyclotomic: x^n−1 = ∏_{d|n} Φ_d(x) — period n ⇔ factor by divisors
F10 [VQ] holonomy/curl test (prime_gauge_field): is path-dependence real or a coordinate artifact
F11 [NEW] persistent homology barcodes (birth/death intervals) ≈ un_sieve/sieve; speculative fit

### G. Emergence / process / dynamics
G1 [GL] emerger (5 brackets, σ_RB firing phase, ZD exact test), emerger–lineage unification
G2 [GL] Feigenbaum, Lyapunov, basins, orbit trap, box-dimension, smooth escape, label_orbit
G3 [GL] pathway_decomposition; rsa_pathway_control (CRT fan-out)
G4 [VQ] box-kite census: chart_of, address_census, skeleton_overlap, fixed-point gluing at e₀
G5 [VQ] noether conservation check along a descent; forced_sigma
G6 [VQ] control-battery scoring (udeo_crypto: 5 mechanisms vs random-guess; mod-4 identity proven)
G7 [VQ] calibration of the decomposition against all engines' own labels (0.957)
G8 [VQ] vector-symbolic bind/bundle/permute (cyclic shift = position); capacity probe; unbind at chance

### H. Ciphers
H1 [KRY→GL] Kasiski, IoC, χ², Caesar brute, pattern signature, Sukhotin, transposition divisor, keyspace product
H2 [KRY] NOT yet in GL: frequency-substitution solve; pattern-dictionary attack; break_vigenere (period→columns);
     hints(); Playfair digraph fingerprint; rail-fence/scytale; affine + affine_break; unscramble; Enigma trace_path
H3 [NEW] Rejewski: cycle type of conjugated permutations is invariant under plugboard — a conjugacy-class factor
H4 [NEW] Turing/Bombe crib loops (consistency closure); Banburismus deciban scoring
H5 [NEW] Hill cipher: known-plaintext linear solve mod 26; det unit iff gcd(det,26)=1 (ties hyper_linear L_d)
H6 [NEW] columnar transposition: key length | ciphertext length; rows×cols factor pairs; double transposition
H7 [NEW] fractionation: Polybius/Nihilist/Bifid/Trifid/ADFGVX — coordinates re-bracketed
H8 [NEW] Friedman kappa/phi, mutual IoC (align two alphabets), Sinkov, autokey, running key
H9 [NEW] unicity distance U=H(K)/D — an exact guarantee: length at which the decomposition is unique
H10 [NEW] quadgram log-likelihood hill-climb / annealing — the paid ascent, priced in evaluations
H11 [NEW] linear cryptanalysis (Walsh), differential (DDT), meet-in-the-middle (re-bracketing into halves)
H12 [NEW] BSGS, Pohlig–Hellman, index calculus, LLL; rainbow-table/Hellman chains (periodic chains)
H13 [NEW] steganography: bit-plane slicing, χ² on value pairs, RS analysis, DCT histogram
     (Kryptos/Steganography/__init__.py is empty)

## 3. Suggested first build (small, exact, compose with existing GL)
1 prefix-function/Z periodicity + Fine–Wilf (B2,B3)   2 Lyndon factorisation (B4)
3 Berlekamp–Massey (B11)   4 log-periodic + Mellin (F2,F3)   5 cycle type/parity/Lehmer (D2)
6 Rejewski invariant (H3)   7 Jordan–Chevalley (D6)   8 Re-Pair lineage (B8)
9 Pohlig–Hellman (A12)   10 unicity distance (H9)

## 4. Public-release flags found in passing (NOT changed)
- 0_RB / ∅_RB / UFT / H_RB naming appears in 10 GL files (README, wiki ×4, engine ×5) — conflicts with the
  "engineered operators" rule outside ValaQuenta.
- GL has no LICENSE file; IP policy (research free / commercial paid) needs one.
- ping.py RSA ops and any udeo_crypto port: embargo is CVE-disclosure only, so check what's in scope.
- generational_lineage_map.md and README still cite FactoralDecomposition / SedenionFactoralRelativity paths.
- README §8 says the curses UI is still planned.

## 5. BUILD STATUS — first ten (2026-09-28, later same session)
Built in GenerationalLineage/engine/toolsets/, registered in engine/lines.py, verify_all 27/27:
periodicity (B2,B3) · lyndon (B4) · berlekamp_massey (B11) · logperiodic (F2,F3) · permutation (D2,D4) ·
rejewski (H3) · jordan_chevalley (D6) · re_pair (B8) · pohlig_hellman (A12) · unicity (H9).
Dispatcher smoke log: dispatch_smoke.log (same dir). Docs deliberately not yet updated (Cody: after all code).
Decisions from Cody: GPL v3.0; GL 100% transparent; ping = TuringStack RSA (not UDEO); UI after engine.
Not fixed: `stencil` absent from lines.TOOLSETS (so verify_all skips it).
