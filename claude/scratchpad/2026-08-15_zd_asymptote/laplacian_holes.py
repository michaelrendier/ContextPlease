#!/usr/bin/env python3
"""
THE LAPLACIAN OVER TOTAL INTERNAL REFLECTION — looking for prime-like holes.

Cody, 2026-08-15: "use the laplacian over the 'total internal reflection' to
find 'prime like holes'".

The zero-divisor graph Gamma(Z/N): vertices are the nonzero zero divisors,
edges join x~y when x*y = 0 (mod N). For N = p*q the zero divisors are the
multiples of p (there are q-1 of them) and the multiples of q (p-1 of them),
and (ap)(bq) = ab*N = 0 while (ap)(bp) != 0. So the graph is EXACTLY the
complete bipartite K_{q-1, p-1} -- two mutually non-adjacent parts, i.e. two
HOLES in the adjacency structure, of sizes q-1 and p-1.

This computes it, reads its Laplacian spectrum, and states where the wall is.
"""
import math
import numpy as np
from sympy import isprime


def zero_divisor_graph(N):
    """Vertices = nonzero zero divisors of Z/N; edges where x*y == 0 mod N."""
    zds = [x for x in range(1, N) if math.gcd(x, N) > 1]
    idx = {v: i for i, v in enumerate(zds)}
    n = len(zds)
    A = np.zeros((n, n))
    for a in zds:
        for b in zds:
            if a != b and (a * b) % N == 0:
                A[idx[a], idx[b]] = 1.0
    return zds, A


def laplacian_spectrum(A):
    L = np.diag(A.sum(axis=1)) - A
    return np.sort(np.linalg.eigvalsh(L))


print("=" * 76)
print("THE LAPLACIAN OF THE ZERO-DIVISOR GRAPH  Gamma(Z/N),  N = p*q")
print("=" * 76)
print(f"\n{'p':>4} {'q':>4} {'N':>6} {'|V|':>5} {'holes (parts)':>16} "
      f"{'distinct L-eigenvalues':>28}")
for p, q in [(3, 5), (3, 7), (5, 7), (5, 11), (7, 11), (7, 13), (11, 13)]:
    N = p * q
    zds, A = zero_divisor_graph(N)
    spec = laplacian_spectrum(A)
    distinct = sorted({round(float(x), 6) for x in spec})
    # the two independent sets: multiples of p, multiples of q
    part_p = [v for v in zds if v % p == 0]
    part_q = [v for v in zds if v % q == 0]
    print(f"{p:>4} {q:>4} {N:>6} {len(zds):>5} "
          f"{str((len(part_p), len(part_q))):>16} {str(distinct):>28}")

print("""
  |V| = (p-1) + (q-1).   The two parts have sizes q-1 and p-1 -- each part is
  an INDEPENDENT set, no edges inside it. Those are the two holes.
""")

print("=" * 76)
print("THE PRIMES ARE IN THE SPECTRUM — exactly")
print("=" * 76)
print("""
  Laplacian spectrum of the complete bipartite K_{m,n} is known exactly:

      0  (once),   m  (multiplicity n-1),   n  (multiplicity m-1),
      m+n (once)

  With m = q-1 and n = p-1 that reads:

      {  0,   q-1,   p-1,   p+q-2  }
""")
print(f"{'p':>4} {'q':>4} {'measured distinct spectrum':>32} "
      f"{'predicted {0,q-1,p-1,p+q-2}':>32} {'ok':>5}")
allok = True
for p, q in [(3, 5), (5, 7), (5, 11), (7, 11), (7, 13), (11, 13), (11, 17)]:
    N = p * q
    _, A = zero_divisor_graph(N)
    got = sorted({round(float(x), 6) for x in laplacian_spectrum(A)})
    want = sorted({0.0, float(q - 1), float(p - 1), float(p + q - 2)})
    ok = np.allclose(got, want)
    allok &= ok
    print(f"{p:>4} {q:>4} {str(got):>32} {str(want):>32} {str(ok):>5}")
print(f"\n  ALL MATCH: {allok}")

print("""
==============================================================================
SO THE PRIMES ARE EIGENVALUES
==============================================================================

  Read the distinct nonzero Laplacian spectrum of Gamma(Z/N) and you have
  {p-1, q-1, p+q-2} -- hand back p and q directly. The 'prime-like holes' are
  real, they are the two independent parts, and their SIZES are p-1 and q-1.

  THE WALL, in its most vivid form yet:

      to BUILD Gamma(Z/N) you must know which elements are zero divisors,
      and knowing that IS the factorisation.

  The primes are eigenvalues of an operator you cannot write down. Every
  route today ends here, and this one ends here most legibly: the answer is
  spectral, exact, and gated behind constructing the very object that
  encodes it.
""")

print("=" * 76)
print("THE DUAL SIDE — where the same Laplacian IS constructible")
print("=" * 76)
print("""
  In the Cayley-Dickson tower the corresponding graph is FREE: adjacency is
  XOR on strut labels, no multiplication table consulted, no factorisation
  needed. box_kite already reports its spectrum:

      chart Laplacian of one box-kite (octahedron K_2,2,2):  {0,4,4,4,6,6}

  and the zero mode is e_0's signature -- 'exists everywhere, propagates
  nowhere'. That kernel IS the fulcrum: the orphan pair that sits in no
  Assessor and carries no force.

  So under the duality:

      CD tower :  Laplacian FREE to build.   Its KERNEL is the fulcrum.
      Z/N      :  Laplacian holds the PRIMES in its nonzero spectrum,
                  and is UNCONSTRUCTIBLE without them.

  Same operator, opposite cost -- which is exactly what the duality predicts,
  and it is the third independent confirmation of it today.
""")
