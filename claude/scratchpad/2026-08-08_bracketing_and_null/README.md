# The bracketing test and the shuffled null — 2026-08-08

Two of the three tests Cody asked for. The third (vocabulary run over 164,283
English words) is **blocked** — see below.

## TEST 1 — `bracketing.py`: does a reverse pathway survive non-associativity?

Left-division: given a and c = a·b, recover b as a⁻¹·c.

| algebra | median relative error | associator |
|---|---|---|
| quaternion (associative) | 1.4×10⁻¹⁶ | 1.5×10⁻¹⁶ |
| octonion (**alternative**) | 1.6×10⁻¹⁶ | 1.10 |
| **sedenion** | **0.52** | 1.30 |
| T32 | 0.74 | 1.37 |

**Sedenion left-division fails with 52% median relative error.** The recovered
value is essentially unrelated to the input.

**The precise algebraic location of the wall is alternativity, not
associativity.** Octonions are *not* associative — the two bracketings of a
triple product disagree by a median 114% — yet left-division is exact to machine
precision, because alternativity is exactly the property that makes division
well-defined. Sedenions lose alternativity at the Cayley–Dickson step, and
division goes with it.

    octonion  bracketing disagreement  113.9%   but division EXACT
    sedenion  bracketing disagreement  131.5%   and division 52% WRONG

**Consequence:** any code that appears to invert a sedenion operation is
returning a bracketing artifact. The 52% is the size of the artifact. This is
the concrete form of Cody's own worry that "code has less limitations than
actual mathematics."

**But this supports the framework's design rather than refuting it.** It says
the inverse cannot be algebraic division — which is precisely what
[[project_zd_holes_are_portals]] already asserts: you recover by *retracing the
path*, not by dividing. Path-as-memory is the correct response to
non-invertibility, and this test is evidence for that choice.

## TEST 2 — `shuffled_null.py`: is there real structure in the addresses?

3,288 addresses; ground truth = 92 parent modules with ≥4 members (2,157
symbols). Null shuffles the name→vector assignment, destroying association only.
200 shuffles per arm.

| arm | within-module cos | random pair | shuffled null | z |
|---|---|---|---|---|
| raw 16D | 0.8851 | 0.7445 | 0.7425 ± 0.0049 | **+28.99** |
| **e₀ projected out** | 0.6849 | 0.3959 | 0.3959 ± 0.0093 | **+31.22** |
| e₀+e₈ projected out | 0.6882 | 0.4025 | 0.4025 ± 0.0093 | +30.75 |

**The signal is real and survives a proper null in every arm.** First cleanly
controlled positive result of the session.

**The e₀ projection is confirmed as the right move.** It does not create the
signal — it *sharpens* it. The baseline drops from 0.74 to 0.40 (that is the
common mode leaving), and the effect size **doubles**:

    raw          gap = 0.885 - 0.743 = 0.142
    e0 removed   gap = 0.685 - 0.396 = 0.289

**e₈ contributes nothing** (0.6849 → 0.6882), independently confirming the
~1% figure derived from the census means. Project out e₀; e₈ is optional.

### ⚠⚠ RETRACTED by TEST 4 — the effect is lexical, not semantic

The caveat flagged here (grouping is by symbol-name prefix; the addresses may be
name-derived) was tested and **the signal does not survive**. See below. Do not
quote the z = +31 as a semantic result.

## TEST 4 — `lexical_matched_null2.py`: the retraction

Same-module symbols share long substrings by construction
(`skills.config.Path.`). 11,979 same-module pairs matched 1:1 against
cross-module pairs at equal character-trigram similarity:

```
mean lexical sim : same 0.6495  vs matched cross 0.6501   (well matched)
mean address cos : same 0.7226  vs matched cross 0.8068
GAP = -0.0842 +/- 0.0029 (SE)    t = -28.8     NEGATIVE

corr(lexical, address)                   = +0.3216
corr(same-module, address)               = +0.2193
PARTIAL corr(same-module, address | lex) = -0.0572
```

**The entire z = +31 was spelling.** Controlling for lexical similarity, the
module effect vanishes and slightly inverts. corr(lexical, address) = +0.32 says
what the addresses encode: **the address is a function of the name.**

This is the objection a reviewer raises first, and it would have been fatal.
Found before publication, it is a result — and it is the empirical form of the
Hyperwebster incompatibility (`../2026-08-08_hyperwebster_wall/`): an address
built from names inherits a *spelling* metric, and spelling proximity is not
merely different from semantic proximity but anti-correlated with it.

**First attempt kept as `lexical_matched_null.py`** — its quantile binning
collapsed to a single usable bin because same-module pairs cluster at high
lexical similarity and cross-module pairs at low, leaving almost no overlap to
match on. That is the classic positivity/overlap failure in matching, and the
1:1 nearest-neighbour version in `lexical_matched_null2.py` is the fix.

## TEST 3 — vocabulary run: BLOCKED

`chart_of` over 164,283 English words cannot run: **per-word 16-D addresses do
not exist.** In `monad_english.bin` (v1.218), `beta` is one *scalar* per word,
not a 16-vector, and `_spsi` in `VAPMIP/monad.py` builds a sedenion from a
*window* of words rather than a single word.

This is exactly primer §14 step **(4)** — "address an English corpus through the
monad hyperindexing (still the prerequisite for chart_of/address_census on
English)" — which the 2026-08-08 primer already flagged as a prerequisite. It is
still a prerequisite. The 3,288-entry `monad_sedenion_addresses.pkl` used above
is a corpus of **code symbols**, not English words.

Doing the vocabulary run means first building the addressing pass. That is
step (4) work, not a run.
