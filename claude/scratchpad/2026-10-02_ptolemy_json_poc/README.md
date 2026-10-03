# ptolemy.json proof of concept (2026-10-02)
ptolemy.json (1 entry) -> TABLES.json (entry per ingest) -> ROWS.json (entry per chunk) -> text. Only ptolemy.json is kept.
Each ingest: reconstruct TABLES from ptolemy.json, build ROWS, append, reindex, overwrite ptolemy.json. No hashing.
perm/ascii.perm (97: TAB, LF, 0x20..0x7E, ASCII order), perm/json.perm (41, frequency order, frozen).
Run: python3 make_json_perm.py (once), python3 run_poc.py. Result: out/run1.txt.
