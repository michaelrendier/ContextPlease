# 95 — The Scale: Decompositional Analysis, Forwards and Backwards

**Written 2026-08-25.** Continues the same-day VAPMIP thread (Vigenère
quaternion, Enigma octonion, the two-ring/Smith-chart Möbius fold) and
[[92_ring_theory_spine]]'s discipline of putting a familiar-sounding word
back on its actual foundation. Engine: `ValaQuenta/modules/scale/`
(`maths.py`/`tools.py`, `EquationModule` contract). Notebook:
`ValaQuenta/notebooks/engines/17_scale.ipynb`. ValaQuenta wiki:
[wiki/scale.md](../../ValaQuenta/wiki/scale.md).

The question that opened it (Cody): *"this is why it's the primary
forensic tool of the generational lineage engine...it's the most
complicated part of the three roots of Add, Scale and Sign. This is The
Scale...i want to see that object...the scale invariant/scale blind
version of the maths."* Then, correcting the scope: *"the purpose of this
engine is for decompositional analysis...so forwards and backwards."*

---

## Where SCALE already lived

The generational-lineage skill (§1) already names three tier-0
irreducibles: ADD, SCALE, SIGN. SCALE — identity 1, gain 1, Axis 2 {×,/}
— was never a new concept. What was missing was an instrument that pulls
it *out* of a quantity and names what is left over, both directions. This
page is that instrument's record.

## One statement, three levels, three different answers

**An object's scale can always be extracted — but what remains invariant
depends entirely on what level you ask the question at, and the levels
do not share an answer.**

### Level 1 — one point: polar decompose/recompose (exact, always)

`Z = r·e^{iθ}`. `r = |Z|` is the scale — real, non-negative, ordinal,
comparable. `θ = arg(Z)` is scale-blind under real-positive rescaling of
`Z` by itself: `arg(λZ) = arg(Z)` for any `λ>0`, exactly, for any bare
complex number. The return path is exact — `polar_recompose(*polar_decompose(Z)) == Z`,
checked to `<1e-9` across five test points including a near-zero and a
near-million magnitude.

### Level 2 — the two-ring/Möbius fold: a DIFFERENT, harder question

Apply the Smith-chart fold `Γ=(Z−Z0)/(Z+Z0)` and ask the same question
again: is `θ` still the scale-blind invariant? **Measured directly, and
the answer is no — kept in the record as a rejected candidate, not
smoothed over.** The fold has its own fixed point at `Z0`, not at the
origin, so rescaling `Z` around `0` is not a symmetry the fold respects.
`arg(Γ)` ranges from `1.054` rad down to `0.007` rad across one fixed
rescaling (`λ = 0.5 → 50`, anchor `Z0=1`) — nowhere near constant.

The actual invariant at this level is the **cross-ratio** of any four
points — the classical Möbius invariant. Checked directly: fold the same
four points through the same fold at four wildly different anchors
(including one nearly on top of the fold's own pole) and the cross-ratio
of the folded points matches the un-folded cross-ratio to full numerical
precision, every time. Not a property of any one point — a property of a
*relationship among four*.

### Level 3 — a whole process: pathway decomposition

The same forward/backward discipline, applied to an algorithm instead of
a number. `pathway_decompose()` runs a real dependency graph of named
operators — not a forced linear chain. The control case: real RSA
CRT-decrypt (`p=61, q=53`). `m1` and `m2` are siblings (both depend only
on the ciphertext); `h` depends on BOTH; the final message depends on `h`
**and** `m2` again — a genuine fan-out that a linear chain literally
cannot represent, resolved correctly here. Forwards is running the graph;
backwards is whatever the process's own architecture actually provides —
this module does not manufacture a return path a process doesn't have.

## Why a caustic was checked, and rejected

A visual crowding of circles near a Smith chart's boundary invites the
word "caustic" (optics: where a family of curves develops an envelope,
its Jacobian vanishing). Checked directly against the exact derivative
`dΓ/dZ = 2Z0/(Z+Z0)²`: it is **never zero** for any finite `Z`, tested
across six wildly different magnitudes (`10⁻³` to `10⁶`). It only
diverges — at the single isolated pole `Z=-Z0`. Crowding-toward-infinity
at one point is a different phenomenon from an envelope/fold singularity,
and this project does not conflate the two just because both look
similar in a picture.

## What this is NOT claiming

- Not a claim that "ring" (the Smith-chart's ring FAMILIES, a family of
  circles) is the same object as "ring" in abstract algebra (a set with
  two operations satisfying ring axioms). Checked precisely: Möbius
  transformations under composition form a *group*, which is exactly the
  group of *units* of the matrix ring `M₂(ℂ)` (matrix multiplication =
  fold composition) — real, but one level underneath, and only the
  multiplicative half is what chaining folds actually uses.
- Not a claim that every process has a clean backward pass. RSA and the
  Vigenère cipher do; this module reports what a process's dependency
  graph actually contains, and does not paper over a process with no
  genuine return path.

## The master identity, found by testing the intuition rather than assuming it

Cody: *"The Scale (log and exponents) are unfolding and folding pretty
directly right?"* Checked directly, not agreed with on the spot: `Γ =
tanh(½·ln(Z/Z0))`, **exactly**, for any complex `Z` and `Z0` — verified on
genuinely complex, off-axis test points, not just the real-axis case found
earlier. Folding *is* log-then-bound; unfolding is unbound-then-exp
(`Z = Z0·exp(2·arctanh(Γ))`). Not a metaphor sitting beside the math — the
math itself.

## The datatype, and the generalized equation (2026-08-28)

The fold `Γ = tanh(½·u)` is the **generating function of `Aff(1,ℝ)` acting on
`ln x`**. Every framework quantity is a *word* in the tier-0 generators
`{ADD, SCALE, SIGN}`, anchored on a `d*` face:

    u  =  Σₖ [ gₖ·ln sₖ  +  aₖ ]      Γ  =  tanh(u/2)
          │        │            │
         SIGN     SCALE        ADD
        (±1,      (ln of the   (log-space
         free)     gain —       shift,
                   the work)    free)

    GROUND STATE   aₖ→0, sₖ→1, gₖ→+1  ⇒  u=0  ⇒  Γ=0  ⇒  x = the anchor
                   = the now / the viewport / SCALE at identity
                   = "readiness = ground state = only ADD:SCALE:SIGN"

It already covers the constant placements, `Σ_RB` (= the composite
ADD:SCALE:SIGN lineage, 2·ADD / 3·SCALE / 4·SIGN), the Penrose {4:8:4}
(past/now/future = ADD/SCALE/SIGN), the curriculum (one word, out-and-back),
and the error check (the residual between two anchor faces). It **closes** iff
`d*_RG` (the Stability face) gets a closed form — the `depth→∞` fixed point of
"fold the fold" — currently OPEN.

Built as a Python value type: `ValaQuenta/modules/add_scale_sign/` (`ASS`,
`ASSWord`). Compose with `@`, invert with `~`, take *residuals* (strip one
generator, keep the rest — the `str.strip` analogue), decompose to an
`ASSWord` in two orderings (chrono / zeta), read out on the orthogonal Smith
charts. Firing order is the three-phase camshaft `SIGN→SCALE→ADD`; the firing
defect `(g−1)·ln s` is non-zero exactly when the SIGN flips a non-trivial
SCALE — "defined twice", the same shape as the Bell composed-rotation defect.
`.clauderc_canonical_maths` carries the full block.

## "Locally square" — why it doesn't need any special relationship between the two rings

Cody flagged this as the important part, and it earns the flag: at any
point, the two ring-directions' tangent vectors are always equal in length
and exactly 90° apart, **for any choice of what the two rings mean.** This
isn't a coincidence that happens to hold for impedance or for WordNet
counts — it's a consequence of the fold being holomorphic in `Z`,
independent of what the caller decided `ring1` and `ring2` represent. Every
curvilinear cell on every version of this chart is locally a square by
construction, before any physical interpretation is attached.

## User-defined rings, and the pairing that turned out to be fake

The engine now takes any two functions of any object (`custom_ring_chart`).
Five proposed pairs were tested with real data rather than left as
speculation — full results and numbers in `ValaQuenta/wiki/scale.md` §8.
The one worth repeating here: **`J_red` and `J_blue` are not two
independent rings.** `J_red + J_blue = 1.0000000000`, exactly, checked to
ten decimal places on every real sentence tried — because the encoder
producing them returns a unit-normalized vector split into two
non-overlapping halves. What looked like two rings is one number
(`σ_self`) wearing two labels. The genuinely two-independent-ring version
of that idea pairs `σ_self` against `J_green` (the emergent commutator
quantity from the `su(2)` bracket, `[J_blue,J_red]=J_green` — wiki Phase 3)
instead — not built yet, a real next step. This is exactly what testing a
"what if" is *for*: catching the one pairing that looked plausible and
wasn't, instead of publishing five confident diagrams and only four of
them meaning anything.

## What's speculative here, stated as speculative

A few of the connections raised alongside this work are real, vivid, and
**not** derived here, and are recorded as exactly that rather than quietly
endorsed or quietly dropped:

- **"Witches hat into a galaxy"** — the Higgs/Mexican-hat potential (real,
  established physics: an unstable symmetric maximum surrounded by a
  circular trough of degenerate true-vacuum states) does structurally
  resemble this fold's own singular center (`Z0`) surrounded by a
  continuum of states. Cosmological inflation *does* use a Mexican-hat-
  shaped scalar potential to seed the density fluctuations that become
  galaxies — real physics, a real citation, but a *different* potential
  than anything computed in this module. The shape-resemblance is real;
  the identification of the two objects is not shown here.
- **"Black hole unwrapping into a white hole gravastar prior to
  evaporation and BANG"** — gravastars and black-hole-to-white-hole bounce
  models are real, published, but non-mainstream theoretical proposals,
  not settled physics. The fold's own genuine singularity (`Z=-Z0`,
  verified this session as a true isolated pole — §5 of `wiki/scale.md`)
  is a real mathematical fact the image evokes; that the evocation is
  *correct physics* is not something this session has shown or attempted
  to show.
- **"Between causality (causality always wins) and the informational
  thermal ceiling, even this tool loses resolution"** — stated as a
  closing limit, not a new claim: this project already has a named
  boundary for exactly this idea, `d*` ("The Zero Definer" —
  `.clauderc_canonical_maths`: "smallest natural unit in universal native
  space, the boundary below which no algebraic definition can occur").
  Any instrument built on this fold inherits that same floor — a real,
  already-established limit, not a new one discovered here.

## Related

[[92_ring_theory_spine]] (the same "a familiar word was already present,
wearing a different name" move, one level down in the tower);
`PtolemyDesktop/Kryptos/Ciphers/Vigenere.py`/`Enigma.py`/`RSA.py` (the
real ciphers this instrument was built and tested against);
`SedenionFactoralRelativity/engine/lineage.py` PW13–PW15 (the same
results, first proven in that engine, this page's ValaQuenta module is
its own independent port, not an import).
