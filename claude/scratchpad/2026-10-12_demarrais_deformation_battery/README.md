# 2026-10-12 — De Marrais box-kite deformation battery (+ both constructs)

Run order: `cdalg.py` (parametrised Cayley-Dickson; validated 256/256 vs ValaQuenta box_kite.multiply)
→ `part1.py` (symmetries, derivations, first-order response; ~4 min) → `part2.py` / `part2b.py`
(operator battery on the 336 ZD pairs, mu-scan with the UNS constants, rotation angle, phase scale) →
`part3.py` (scalar + scaled constructs vs the maths) → `part4.py` (G2 flows of the whole kite) →
`part5.py` (function-of-pair table at three magnitudes; topic separation of the live readings).
Outputs: `output_part*.txt`, `results_part1/2.json`.  Python 3.12, numpy, scipy.

Headline results: see docs/wiki/Tuning-the-Engine/41_* and marrais_boxkite_catalog.txt §11-15.
Caveats: first CS-04 run used |z|=1 only (degenerate for Moebius and z^2) — superseded by part5.py;
the c=GAP all-levels "537 pairs" row is a tolerance artifact (part2b.py (i)); station != Assessor vertex
for the paper's pencil(r<=7).

## Added 2026-10-13
`part6.py/6b/6c` (Blackjack F21 = the 21 sign-free automorphisms; {4:8:4} blocks and edges; bracketing and firing order; kernel fiber as a bracket),
`part7.py` (pencil convention, gradient ranks, mechanism; first run inline), `zdscan.py` + `part8.py` (the 4 d* faces and 3 Lambert-W values as the
doubling parameter), `make_record.py` (builds VAPMIP/docs/wiki/Boxkite-Deformation-Record-2026-10-12.md from these outputs).
