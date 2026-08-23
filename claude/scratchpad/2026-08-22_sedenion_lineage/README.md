# Generational lineage at three levels of the sedenion — 2026-08-22

Cody: "run generational lineage on the whole sedenion... on each value
individually without bracketing... on the two octonion orthogonal
arrangement... I'm assuming we can name some of the places this way."

## Level 1 — the whole sedenion (dim 16)
Generation 4 of the CD tower. Associator nonzero triples = 1848 = 11x168.
The lineage IS the tower: R->C->H->O->S, losing ordering@2, commutativity@4,
associativity@8, division@16 in order.

## Level 2 — each e_k, k=0..15, alone, unbracketed
e_0^2=+1 (order 1, the anchor). e_k^2=-1 for k>=1 (order 4, i-type).
CONFIRMED: no single e_k is EVER a zero divisor by itself -- e_i*e_j for
i!=j always lands on a single basis vector, magnitude 1. Zero-divisor-ness
is EXCLUSIVELY a property of SUMS (bracketing). Unbracketed, the sedenion
is 16 clean order-4 rotations around one order-1 anchor -- nothing broken.

## Level 3 — the two-octonion orthogonal split (LOWER=e0..7, UPPER=e8..15)
NEW result, verified exhaustively (all 64 products each):
  LOWER*LOWER -> LOWER always      (LOWER is a CLOSED SUBALGEBRA, isomorphic to O)
  UPPER*UPPER -> LOWER always      (UPPER is NOT closed -- collapses into LOWER)
  LOWER*UPPER -> UPPER always      (LOWER ACTS on UPPER)
  UPPER*LOWER -> UPPER always
This is EXACTLY the R->C pattern one level up, with O playing R's role:
UPPER is the sedenion's own "i" relative to LOWER's "R" -- not e8
specifically, the WHOLE UPPER OCTONION as a block. UPPER*UPPER->LOWER
mirrors i*i=-1 (imaginary^2=real) exactly.

## Naming proposal (grounded in the above, not asserted)
  e0            The Anchor         gen0, identity, order1, generates nothing
  e1            The First Turn (i) gen1, C
  e2,e3         (i,j,k convention) gen2, H
  e4..e7        The Quartet        gen3, O, completes the Fano structure
  LOWER (e0-e7) The Body           the closed, self-sufficient, acting subalgebra
  UPPER (e8-15) The Mirror         the sedenion's own "i" one level up;
                                   not closed, always resolves through LOWER

## What each generation's new i CONTRIBUTES to a destination (Cody's connection)
Walking the CD tower toward any destination, each new i-block deposits
exactly one capability, in order:
  gen1 (C) -> ordering/phase          gen2 (H) -> order-dependence (precession)
  gen3 (O) -> grouping-dependence (the associator, curvature, work)
  gen4 (S) -> the capacity to FALL (zero divisors, non-invertibility)
"i's generational lineage" is this list -- each i is a specific payload,
not just a direction.

## CORRECTION, same session — the direction runs backward (Cody)

I had framed generation 4 as "the LAST capability acquired." Wrong direction.
Cody: "information progresses backwards... it fails first, then you go
around that, and the rest of the potential of mathematics exists... 0_ZD is
a Zero Definer... operators are not lost, they are first definable apart
from each other at each point... context flows through operations not
answers." Consistent with prior memory: [[project_zd_holes_are_portals]] —
"ZDs are birth-points not endpoints."

Verified precisely: L_a (left multiplication by a) is INJECTIVE (no
information destroyed, x!=y => ax!=ay) for EVERY nonzero a at dim<=8
(200/200 random a). At dim16, injectivity is NOT universal -- a genuine
zero-divisor generator (e1+e10)/sqrt2 has a NONTRIVIAL kernel; a
non-ZD-forming element at the same dim does not. So DIVISION is exactly
"injective for every element", and going S->O (backward from 0_ZD toward
R) it becomes universally true for the FIRST time.

The corrected reading of the tower: 0_ZD (dim16) is the UNDEFINED SOURCE --
where the product can destroy the distinguishing information between two
elements. Going backward (S->O->H->C->R), at each step one property becomes
newly, separately DEFINABLE (not "lost going forward"):
  S->O: DIVISION becomes definable (injective, everywhere)
  O->H: ASSOCIATIVITY becomes definable
  H->C: COMMUTATIVITY becomes definable
  C->R: ORDERING becomes definable (the last, most constrained property)

Also verified at the ring-theory-spine level (Z): FALL (composite) is the
GENERIC case, not a late failure -- density -> 100% (pi(N)/N -> 0, prime
counting ~N/ln N). Measured: 73% composite under 100, 92% under 1,000,000.
SURVIVE (prime) is the rare, effortfully-found exception, exactly matching
"it fails first."
