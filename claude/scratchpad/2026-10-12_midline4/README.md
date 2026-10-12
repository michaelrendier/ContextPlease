# Midline 4-digit code T S DD — final rules (2026-10-12)

Rules (Cody's decisions): code = type·1000 + sign·100 + step. Types 0 Upper, 1 Lower, 2 Digit, 3 Punct.
Letters: sign = side of anchor M/m, step 0..13, anchor takes sign 0. Digits: sign always 0 (sign rule dropped).
Punct: LF, space + 32 symbols = 34, ASCII order, even split 17/17 (sign picks the half). Tab = four spaces
(`normalise`). 96 valid codes, hardcoded sorted list; whole-text address = base-96 Horner over the list index
(6.585 bits/char).

Files (copies of the live ones at the time of writing):
- `MidlineIndex.py` ← PtolemyDesktop/Archimedes/Maths/ (engine, self-test, de Bruijn at k=96)
- `Midline.py` ← PtolemyDesktop/Kryptos/Ciphers/ (Kryptos wrapper; keeps LF, tab→4 spaces)
- `test_midline.py` ← PtolemyDesktop/Kryptos/tests/ (39 cases; Kryptos suite 65 → 104)
- `_build_d.py`, `_build_e.py` ← FourthAgePapers/HyperindexingSystem/notebooks/ (v19 + w01 builders)
- `midline4.py` — the first standalone 94-code prototype and its tests (before space and LF were added)

Wiki: FourthAgePapers/HyperindexingSystem/wiki/20_v19_midline_index.md (+ rows in 21, 00_index).
Notebooks regenerated and executed: v19_midline_index/01, 02 and w01_taxonomy/01.
Kryptos suite is now 104 cases (65 + 39 in test_midline.py).
