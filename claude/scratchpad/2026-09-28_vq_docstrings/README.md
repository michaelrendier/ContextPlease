# 2026-09-28 — ValaQuenta → "API: Code Reference"

Tools (kept for reuse; all AST-based, none of them safe to run without reading the diff afterwards):
- `docedit.py` — dump/apply docstrings by qualified name (specs in `edits/*.json`: doc | sub | params/returns/raises).
- `rstfix.py` — make docstrings valid reST without changing words (indented blocks → literal blocks; `|` `*` escaped).
- `add_process.py` — give every Equation a `process=` (first sentence of compute()'s docstring, else display).
- `gen_class_docs.py` — class/`__init__` docstrings for tools.py modules from their metadata.
- `audit.py` / `stale.py` / `check_raises.py` — coverage+style counts, stale-phrase finder, documented-vs-actual raises.
- `README.before.md` — the README prior to the Code Reference rewrite. `noether_tools.before` — a tools.py before add_process.

Method lessons: two scripted substitutions garbled oblique_gear's docstring and a move script dropped blank lines at 12
junctions — Sphinx -W and reading the diff caught both. See ~/.clauderc_context_2 (2026-09-28) for the full log.
