# 2026-10-13 — genealogy of the sedenion box kite, portals, G2 decomposition, moving-kite invariants, Lambert-W

Asked (Cody): factor the De Marrais box kite into its smallest components (relations, not numbers); give the mathematical definitions of spinor / fibre /
braid / twistor and what each is composed from; test whether the struts are one continuous family; repeat the three Lambert-W values; list what the
moving (scaled) kite needs.  Written up in VAPMIP/docs/wiki/Boxkite-Relational-Atlas.md and Boxkite-Deformation-Record-2026-10-12.md.

common.py (loads the battery's cdalg + cached Der basis ders.npy) | lambert3.py → output_lambert3.txt | genealogy.py → output_genealogy.txt (FIRST PASS: its
order-8 subgroup census wrongly included order-4 spans, and its face test required all three diagonals to annihilate each other; superseded by genealogy2.py) |
genealogy2.py → output_genealogy2.txt | g2decomp.py → output_g2decomp.txt | portals.py → output_portals.txt | invariants.py → output_invariants.txt |
spinor_braid.py → output_spinor_braid.txt.   Run from this folder with python3 (no -I).
