#!/usr/bin/env bash
# waits for the HST downloader to exit, then opens every downloaded FITS (all HDUs) and compares size with the manifest
D="/media/rendier/Telescope Data/BulletCluster/BCData/HST"
while pgrep -f "telescope_download.py _manifest_2026-11-04.json" >/dev/null; do sleep 30; done
python3 - <<'PY' > "$D/_verify_2026-11-04.txt" 2>&1
import json, os, warnings
from astropy.io import fits
D="/media/rendier/Telescope Data/BulletCluster/BCData/HST"
ok=bad=0
for m in json.load(open(D+"/_manifest_2026-11-04.json")):
    f=m["dest"]; n=os.path.getsize(f) if os.path.exists(f) else -1
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            with fits.open(f, memmap=False) as h:
                end=sum(x.filebytes() for x in h)
        st="OK" if (end==n and (abs(n-m["size"])<=2*2880 or m["size"]==0)) else "MISMATCH"
    except Exception as e:
        st="BAD "+type(e).__name__
    ok+= st=="OK"; bad+= st!="OK"
    print(st, os.path.basename(f), n, "manifest", m["size"])
print("OK",ok,"NOT OK",bad)
PY
