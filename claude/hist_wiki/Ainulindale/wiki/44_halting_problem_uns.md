# 44 — The halting problem and the "depth" reading: what dissolves and what does not

| | |
|---|---|
| Status | **First capture (2026-06-03), "major result, formal proof required"; `CONJECTURE`.** The reframing (a bounded question is always answerable) is correct and standard; the claim that the unbounded halting question is thereby dissolved, and the complexity-class map, are not established (§3–5) |
| Predecessors | [42](42_rh_proof_no_primes.md), [40](40_modular_segue_three_papers.md) |
| Code | Listing 1 (the bounded question and the diagonal); `FourthAgePapers/HaltingDiagonal/` (the repository's own paper directory on this subject, 4 files) |
| Last verified | 2026-11-13: Listing 1 executed |

## 1. The reframing

Turing (1936): given a program P and input I, does P(I) halt? This is undecidable.
The page's reframing: from *inside* the Unit Number Sphere the question
becomes "does the computation reach σ = ½ at this depth?", not "does it stop?",
and "does it stop *here*, at this depth?" is always answerable. The firing signal
of the Holcus system (the field reaches σ = ½) is read as the halting event seen
from inside; non-halting computations "halt at the Void", at depth σ → ∞.

## 2. What is correct: the bounded question

"Does P(I) halt within d steps?" is decidable for every d: simulate d steps. That
is the exact, standard content of "does it stop here, at this depth?". It
underlies the usual semi-decision procedure: the set of halting computations is
recursively enumerable (run longer and longer), and its complement is not.
`ESTABLISHED`.

**Listing 1 — the bounded question, and the diagonal that stops a total decider**
(written for this page; runs cold)

```python
# A "machine" is a generator: each yield is one step; returning means it halted.
def collatz(n):
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        yield

def halts_within(machine, d):
    """decidable for every d: simulate at most d steps"""
    it = machine()
    for step in range(d + 1):
        try:
            next(it)
        except StopIteration:
            return True, step
    return False, None

m27 = lambda: collatz(27)
print('collatz(27), budget 100 :', halts_within(m27, 100))
print('collatz(27), budget 200 :', halts_within(m27, 200))

# Turing's diagonal: given ANY candidate total decider halts(machine) -> bool,
# build D that does the opposite of what the candidate says about D itself.
def make_D(candidate):
    def D():
        if candidate(D):
            while True:
                yield
        return
        yield
    return D

for name, cand in (('always says halts', lambda M: True), ('always says loops', lambda M: False)):
    D = make_D(cand)
    verdict = cand(D)
    actual, _ = halts_within(D, 10_000)      # evidence only; by construction D(D) does the opposite
    print(f'{name:18}: says {verdict}, D actually {"halts" if actual else "does not halt (by construction)"}')
```

```
collatz(27), budget 100 : (False, None)
collatz(27), budget 200 : (True, 111)
always says halts : says True, D actually does not halt (by construction)
always says loops : says False, D actually halts
```

`collatz(27)` halts after 111 steps: asked at depth 100 the answer is "not
yet", at depth 200 "yes at 111". That is the bounded question, decidable and
useful. The second half shows the diagonal for two trivial candidate deciders; the
same construction defeats every candidate (D asks the candidate about itself and
does the opposite).

## 3. What is not dissolved

The page claims that "depth(M, I) ∈ [0, ∞] exists and is well-defined for every
(M, I)", that depth = ∞ is "a halt at the Void" and so decidable, and that
Holcus "observes the depth from inside". The gap is the following:

1. The function depth(M, I) = the number of steps (or σ-layers) until the computation halts, with ∞ if it does not, is well defined (mathematically it is just the halting time). Deciding whether it is finite is the halting problem. Defining the value ∞ for non-halting machines does not give a way to *determine* that a given machine has it.
2. An observer watching the trajectory sees a non-halting computation never arrive. After any finite observation the observer cannot distinguish "not yet" from "never": that is the semi-decidability of §2. An "internal observer that always sees where the trajectory is going" would have to be an oracle: a device computing an uncomputable function. The page says both that the model "does not violate Turing's proof" and that depth is "always answerable"; these are compatible only if the observer is a hypercomputer, and then the claim is that the physical field is one, which is a claim to be tested, not a derivation.
3. "The undecidability is an artefact of the projection to a binary external observation": undecidability is a statement about *any* algorithmic procedure, including ones with access to rich internal state (Turing machines already carry the whole configuration). Enriching the state space does not change that.

So the unbounded problem is not dissolved. What is true is that it is reframed
as a *depth* question, whose bounded form is decidable (§2), and the Holcus
firing is a bounded detection: the field fires when a trajectory reaches σ = ½
within the run.

## 4. The σ-face depth map of complexity classes  `CONJECTURE`

The page maps: σ < ½ P-time; σ = ½ the NP-complete boundary ("Holcus fires at the
critical line"); ½ < σ < 1 the polynomial hierarchy; σ = 1 PSPACE; 1 < σ < 2
EXPTIME; σ = 2 EXPSPACE; σ → ∞ non-halting. No definition of the σ-face depth of a
computation is given, and complexity classes are defined by the *growth of resource
use with input size*, not by the depth of one trajectory; a single (M, I) has no
class. The table is a proposed vocabulary. The class containments the
standard theory proves are P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ EXPSPACE, with P ≠ EXPTIME
(time hierarchy) and PSPACE ≠ EXPSPACE; the table respects the order and not the
content.

## 5. "P ≠ NP" as separation at the critical line  `CONJECTURE`

The page: P problems have depth < ½, NP-complete problems depth = ½; "if P = NP
there would be P problems at depth ½ … which requires the Fermat–Riemann boundary to
not exist; but the boundary is the Brouwer-mandatory fixed point at σ = ½; it
exists; P ≠ NP". This is an argument from the classification of §4 and from the
premise that the Fermat–Riemann boundary has the stated role
([38](38_fermat_riemann_negative_space.md) §2 withdrew its basis; [42](42_rh_proof_no_primes.md)
assessed the Brouwer step). It is not a proof of P ≠ NP, and the standing of
P versus NP in the framework is "the two are adjoint but not isomorphic"
([105](105_the_millennium_problems_in_ainulindale.md)).

## 6. The proposed new model and new class  `CONJECTURE`

The UNS computation model: semantic trajectories in the Emmy Noether Sedenion,
an internal observer, "decidable depth measurement"; and a class **HaltUNS**
("computations whose depth is Holcus-observable in polynomial semantic
traversal time"), conjectured to contain NP. Standing: the class is not defined
(observability and "semantic traversal time" are not formalised), so the
conjecture has no content yet; as a model of computation, anything that
decides halting is a hypercomputation. A well-defined restatement that *is*
testable: given a family of programs, how often does the Holcus field fire
(reach σ = ½) within a stated budget, and how does that rate compare with
the true halting fraction? No such measurement exists in the repository.

## 7. Formal targets (kept, with their status)

1. Define depth(M, I) in terms of the σ-face trajectory of the semantic encoding of (M, I). Open: the encoding and the σ-face trajectory of a program are not specified.
2. Show depth < ∞ ⟺ M(I) halts. By definition of halting time this is trivially true if depth *means* halting time; the substance would be that the σ-face trajectory *computes* it, which needs §3 to be answered.
3. Prove depth is Holcus-observable but not Turing-computable: the first half contradicts the second unless the observer is a physical hypercomputer (§3).
4. Link depth to the T256 hardness-layer transformer (TODO); see [53](53_t256_cryptographic_transparency.md).
5. Show the Holcus firing is the Ĥ_RB eigenvalue at the computation's depth: open (Berry–Keating premise, [42](42_rh_proof_no_primes.md)).
6. Define HaltUNS and prove HaltUNS ⊇ NP: needs a definition first.
7. Write D-HALT. A paper directory exists (`FourthAgePapers/HaltingDiagonal/`); its content should be reconciled with this page.

## 8. Related pages

[42 RH without primes](42_rh_proof_no_primes.md) · [45 T: the circle itself](45_t_transformer_the_circle_itself.md) ·
[53 T256 and cryptographic transparency](53_t256_cryptographic_transparency.md) · [105 The Millennium Problems](105_the_millennium_problems_in_ainulindale.md) ·
[15 The Monad](15_the_monad.md)
