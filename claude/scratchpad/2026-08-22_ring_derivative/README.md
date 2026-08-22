# The ring-theory derivative — 2026-08-22

Cody: "what is the ring theory version of a derivative in calculus?" Answer:
a DERIVATION (any additive map with Leibniz), tested two ways in
ring_derivative_test.py, and now engine relation
SedenionFactoralRelativity/engine/lineage.py ring.arithmetic_derivative (G8),
35/35.

- formal derivative on R[x] (any ring, no limit): gcd(f,f')!=1 detects a
  repeated root = the discriminant = ramification (ties to the cyclotomic
  Z[zeta_n] frontier in Ainulindale wiki/92).
- arithmetic derivative on Z (Barbeau 1961): p'=1, Leibniz forces the rest.
  n'/n is the log-derivative = the SAME cepstral order-2 datum (primary
  decomposition / von Mangoldt) already in the engine, read as a rate.
  Fixed points D(n)=n forced to n=p^p: 4=2^2, 27=3^3, 3125=5^5 — the
  "arithmetic e^x".
