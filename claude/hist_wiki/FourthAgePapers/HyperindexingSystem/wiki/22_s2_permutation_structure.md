# S2 · The permutation structure of a hyperindex

*Claude Sonnet 5.5, 2026-09-29. Synthesis of v04, v06, v09, v10, v15. Notebook: [`w02_permutation_structure/`](../notebooks/w02_permutation_structure/).*

Four exact facts, each checked by the notebook.

**1. The rank of an arrangement is a permutation rank.** For a string of distinct symbols, the rank of the string within its anagram class (v06, notebook 03) equals its lexicographic permutation rank: checked for all 720 arrangements of `qwerty` and all 5,040 of `qwertyu`. Over all 18,278 lowercase words of length ≤ 3 there are 3,653 anagram classes, of sizes 1 (78 classes), 2 (325), 3 (650) and 6 (2,600).

**2. A transposition moves the address by a closed form.** Swapping positions i < j of a length-L string changes the address by `(d_j − d_i)·(N^(L−1−i) − N^(L−1−j))`, `d = index + 1`. Exact for all 66 transpositions of a 12-character string.

**3. A charset order is a relabelling of the digits.** The address of a string under a charset order π equals the public address of the relabelled string: 200 random strings under five random orders, all equal. The key space is 97! (505 bits). `rank1`/`unrank1` (Myrvold & Ruskey 2001, read in full) map an order to its integer key and back; all five random 505-bit keys round-trip.

**4. Counting.** The number of strings with a given multiset of symbols is the multinomial L!/∏cₖ!; summed over all multisets it is (alphabet size)ᴸ. Checked exactly for 4 symbols, L = 4: 256 = 4⁴.

## What follows

An exact address is a permutation-invariant part (the multiset) plus a permutation (the arrangement). The permutation part is a rank; moving one symbol moves the address by an explicit amount; changing the charset order is a substitution of digits. The last is why a charset order is not a secret against a reader who has the integer (v15).
