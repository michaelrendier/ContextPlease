# 2026-10-20 — SemPriCon exploration scratch: English dictionary PDF, Chinese structure probes, exact zeros, ring-circle

Throwaway scripts and logs behind the 2026-10-20/21 work; the results live in the repos (SemPriCon `tools/`, `SpecTools/`, `VAPMIP/RingCircle/`, wiki pages 11–16).
- `en1_*.py` — English v1.0 bin exploration (slot/label census) behind `SemPriCon/tools/en1_dict_pdf.py`.
- `zh_probe1.py`, `zh_lab1.py`, `zh_lab2.py`, `zh_key.py` — the Chinese structure-order experiments (what failed: pure mixed-radix, golden hash of rank) behind `tools/zh_half_line.py`.
- `rc_min.py`, `rc_all.log`, `rc_part1.log` — ring-circle minimal generating-set search and battery logs.
- `zeros25000.log`, `zeros25000b.log` — the exact-zero runs (the first was stopped without a checkpoint; the second checkpointed and finished, 25,000 zeros checked against mpmath.zetazero).
Large intermediates (pickles, PNGs, venv) are not kept.
