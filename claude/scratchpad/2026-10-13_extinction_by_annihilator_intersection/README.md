# Extinction by annihilator intersection (2026-10-13)
Question (Cody's C): basin foci checked against each other, "what maps onto the same objects", to extinguish response possibilities.
Model [HYP]: each prompt focus = a zero-divisor diagonal y; surviving responses = common kernel of x -> xy over the foci. Exact SVD, tol 1e-9.
[MEASURED]: every N(y) is 4-dim. Two foci: 3276/3486 pairs leave NOTHING; 168 leave a 2-dim space; 42 leave all 4 (the +/- diagonals of one Assessor share an annihilator).
All 168+42 survivors are SAME-STRUT (same kite) pairs; foci from different struts: 3024/3024 total extinction. Triples: 168 of 95284 survive (dim 2).
No surviving space contains a lattice basis vector e_i. Reading: one coherent context = one kite; the foci must sit in it for any response to remain.

## Second pass (tests2.py, tests3.py; outputs alongside)
[MEASURED] The 168 two-dim survivors are EXACTLY the kite edges (same strut, different, non-reversed Assessors): 168/168 = 7 kites x 12 edges x 2 sign choices.
[MEASURED] The 42 four-dim survivors are NOT the +/- diagonals of one Assessor (0/42; my guess was wrong): they are REVERSED Assessors with opposite sign, e.g. (1,2,+1)&(2,1,-1) - the pair the edge rule excludes shares its whole annihilator.
[MEASURED] x->xy has normalised singular values {0 x4, 1 x8, sqrt2 x4} = contract:neutral:dilate = {4:8:4}. One map: forward is many-to-one (z+N(y) -> z, err 3e-15); read backward it is one-to-many (z has a 4-dim coset).
[MEASURED] A G2 flow exp(sum t_i D_i) carries a reference diagonal onto a focus diagonal (residual 2e-9, |t|=6.17); it is an automorphism (err 2e-14); N(gy)=gN(y); the flowed diagonal leaves the lattice (3 nonzero entries). Common-kernel dims preserved on 210/210 pairs under a random flow: extinction logic is frame-invariant; lattice labels are frame-relative.
