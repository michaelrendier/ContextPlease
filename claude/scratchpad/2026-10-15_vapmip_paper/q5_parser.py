"""Q5 — the Zork-style parser: verb->operator table parity between PtolC/zork.c and zork_parser.py (convention F: exhaustive), plus the 16-operator coverage."""
import re, sys
sys.path.insert(0, "/home/rendier/Projects/ThePlace/VAPMIP")
c = open("/home/rendier/Projects/ThePlace/VAPMIP/PtolC/zork.c").read()
tbl = c[c.index("VerbEntry VERBS[]"):]; tbl = tbl[:tbl.index("};")]
cv = {m.group(1): int(m.group(2)) for m in re.finditer(r'\{\s*"([^"]+)"\s*,\s*(\d+)\s*\}', tbl)}
import zork_parser as zp
pv = dict(zp.VERB_TO_OP)
print(f"C verbs: {len(cv)}   Python verbs: {len(pv)}")
only_c = sorted(set(cv) - set(pv)); only_p = sorted(set(pv) - set(cv)); diff = sorted(v for v in set(cv) & set(pv) if cv[v] != pv[v])
print("only in C:", only_c[:20], len(only_c)); print("only in Python:", only_p[:20], len(only_p)); print("same verb, different operator:", [(v, cv[v], pv[v]) for v in diff][:20], len(diff))
print("operators covered (C):", sorted(set(cv.values())), len(set(cv.values())), "of 16; (Py):", len(set(pv.values())), "of 16")
print("operator names (Python):", zp.OP_NAMES)
from collections import Counter
print("verbs per operator (C):", dict(sorted(Counter(cv.values()).items())))
