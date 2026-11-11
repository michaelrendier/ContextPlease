"""Physically validate every FITS file under BCData: open every HDU (headers), compare file length with the length the headers imply.
Truncated or unreadable files are reported. Nothing is modified."""
import os, sys, warnings, csv, collections
import numpy as np
from astropy.io import fits
ROOT = "/media/rendier/Telescope Data/BulletCluster/BCData"
rows = []
for dp, dn, fn in os.walk(ROOT):
    for f in sorted(fn):
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, ROOT)
        size = os.path.getsize(p)
        status, detail = "n/a", ""
        low = f.lower()
        if low.endswith((".fits", ".fit", ".fits.gz", ".fz")) or ".fits" in low:
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("error")
                    with fits.open(p, mode="readonly", lazy_load_hdus=False, memmap=False) as h:
                        end = 0
                        for hd in h:
                            nb = hd.filebytes() if hasattr(hd, "filebytes") else 0
                            end += nb
                        n = len(h)
                if not low.endswith((".gz", ".fz")):
                    status = "OK" if end == size else "SIZE-MISMATCH"
                    detail = f"hdus={n} implied={end} actual={size}"
                else:
                    status = "OK(gz)"; detail = f"hdus={n}"
            except Exception as e:
                status, detail = "BAD", f"{type(e).__name__}: {str(e)[:90]}"
        rows.append((rel, size, status, detail))
with open("validate_BCData.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["file", "bytes", "status", "detail"]); w.writerows(rows)
c = collections.Counter(r[2] for r in rows)
print("files:", len(rows), dict(c))
for r in rows:
    if r[2] in ("BAD", "SIZE-MISMATCH"): print(r)
