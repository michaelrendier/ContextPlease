import sys; sys.path.insert(0, "/home/rendier/Projects/ThePlace")
"""Append the generational-lineage calibration block toward the bottom of each
ValaQuenta engine wiki page. Idempotent: skips a page that already has the block.
The block goes BEFORE a trailing '## See also' / '## Related' section if present,
otherwise at the very end.
"""
import os, re
from SedenionFactoralRelativity.engine.valaquenta_calibration import ENGINES, wiki_block

WIKI = "/home/rendier/Projects/ThePlace/ValaQuenta/wiki"
MARK = "## Generational Lineage — calibration"
TAIL_HEADS = ("## See also", "## Related", "## see also", "## related")

done, skipped, missing = [], [], []
for name in ENGINES:
    path = os.path.join(WIKI, f"{name}.md")
    if not os.path.exists(path):
        missing.append(name); continue
    src = open(path, encoding="utf-8").read()
    if MARK in src:
        skipped.append(name); continue
    block = "\n---\n\n" + wiki_block(name).rstrip() + "\n"
    # insert before a trailing See also / Related section if one exists
    idx = -1
    for h in TAIL_HEADS:
        j = src.rfind("\n" + h)
        if j > idx:
            idx = j
    if idx != -1:
        new = src[:idx].rstrip() + "\n" + block + "\n" + src[idx:].lstrip("\n")
    else:
        new = src.rstrip() + "\n" + block
    open(path, "w", encoding="utf-8").write(new)
    done.append(name)

print(f"appended : {len(done)}")
for n in done: print("  +", n)
print(f"skipped (already had block): {len(skipped)} -> {skipped}")
print(f"missing wiki page: {len(missing)} -> {missing}")
