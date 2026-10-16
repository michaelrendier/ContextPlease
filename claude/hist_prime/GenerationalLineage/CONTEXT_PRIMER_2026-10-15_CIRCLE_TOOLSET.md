# CONTEXT PRIMER — GenerationalLineage `circle` toolset (2026-10-15)

**State: built, self-checked, documented, NOT committed or pushed.** Working tree of `GenerationalLineage` has uncommitted changes (list below). Cody has not asked for a commit.

## What exists
- `engine/toolsets/circle.py` — the 29th toolset, `LINE="both"`, ONE file (Cody: "for the last time, everything goes in the one file"). 27 `verify()` checks pass. Contents: `Circle` (Add centre / Scale radius / Sign orientation), `from_role`, `descend` (number+role → row), `catalogue`, `build_up` (target measure → constants×roles), `pi_unit_circles`, `pi_lattice`, the six operators `orbit unfold cut fold project shuffle` (names approved by Cody), the SEVENTH circle `pi_p`/`lp_circle`/`CAYLEY_KLEIN`/`classify_sl2`, imaginary circle (`imaginary_circle`, `flat_laws`, `heron_squared`, `sphere_triangle_angle`, `triangle`), `sigma_reading`, `CITATIONS`.
- Registered: `engine/toolsets/__init__.py`, `engine/lines.py`, `devtools/build_docs.py` (MOVES entry sec 4.29 + 8 REFS). Tutorial `examples/50_circle.py` + generated transcript. Generated `wiki/Circle.md`, `wiki/Tools-Reference.md`, README blocks. Hand-written `wiki/Circle-Catalogue.md` (tables are generated from the live code by the scratch script p11/p12), index row in `wiki/README.md`, NEWS entry, skill row in `generational-lineage/SKILL.md` (mirrored to ContextPlease/claude/skills).
- Other wikis: `Ainulindale/wiki/126_the_circle_catalogue.md` (+ row in 00_index.md); `TuringStack/wiki/Lp-Circles-Fermat-Curves-and-the-Two-Factoring-Conics-2026-10-15.md`.
- Evidence: `ContextPlease/claude/scratchpad/2026-10-15_circle_unit_session/` — p1–p12 scripts + outputs, `p8_sigma_scan.csv` (76 rows: every value as σ_RB), README.md with verdicts.

## Cody's decisions (this session)
Six drawings = orbit/unfold/cut/fold/project/shuffle (approved). Seventh circle (ℓ_p) goes IN the same file and also gets its own TuringStack wiki (RSA / English-word factoring). π as the UNIT at diameter, area, circumference. Everything in one file. Cataloguing/relating, not pointing to specific functionality. "Zeta produces a cardioid" is NEVER to be questioned.

## Verdicts (chase-every-anomaly)
π-lattice near-equalities = exact algebra; Ω/(4π) vs optimal fast-inv-sqrt σ = weak coincidence; π_p min at 1.992 = grid (METHOD); spherical cosine form fails R≳1e5 = METHOD (documented limit, haversine remedy); Euler-method None for 221 = my wrong gcd formula (fixed: gcd(N, ad∓bc)); Euler's circle method works iff both primes ≡1 mod 4 (210/210, 0/780 below 200).

## Still open
- Add/Scale/Sign placement of π is MY proposal (C→Add, A→Scale, d→Sign; derived from the log chart u=ln r: d,C shifts, A slope 2, imaginary radius = u+iπ/2 quarter turn = Sign) — Cody has not confirmed.
- Lobe shape factor flattens for s>1.05 (p6b); lobe/cusp ↔ GL emerger link.
- ℓ_p word-factoring tests (TuringStack page, "OPEN, test plan"): none run.
- Citations were written from bibliographic records; NOTHING downloaded — verify before any paper (Literature Download Protocol not triggered).
- README of GL: hand-written counts (29 toolsets, test totals) updated only where verified; no "Current Repo Focus" section existed before this session (see README top).
- Not committed. Commit message trailer (if asked): `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.

## Next
Return to VAPMIP (Tuning-the-Engine notebooks done: 44 notebooks, FINDINGS.md current; paper draft in VAPMIP/docs/paper_drafts).
