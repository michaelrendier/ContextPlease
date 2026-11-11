"""READ-ONLY: size the per-exposure products for HE 0435-1223 from MAST product lists. Writes nothing but a CSV here."""
import collections, csv, os, astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.mast import Observations
UA = os.environ.get("CLAUDE_UA", "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0")
Observations._session.headers["User-Agent"] = UA
c = SkyCoord(69.56208 * u.deg, -12.28722 * u.deg)
o = Observations.query_region(c, radius=90 * u.arcsec)
sel = [r for r in o if str(r["obs_collection"]) in ("JWST", "HST") and str(r["dataproduct_type"]).lower() in ("image",)]
print("image observations in 90\":", len(sel))
byprog = collections.Counter((str(r["obs_collection"]), str(r["instrument_name"]).split("/")[0], str(r["proposal_id"])) for r in sel)
for k, v in sorted(byprog.items()): print(" ", k, v)
want = [r for r in sel if (str(r["obs_collection"]) == "JWST" and str(r["proposal_id"]) in ("1198", "2046")) or (str(r["obs_collection"]) == "HST" and str(r["proposal_id"]) in ("9744", "12889", "13732"))]
print("target observations:", len(want))
rows = []
for i in range(0, len(want), 20):
    pl = Observations.get_product_list([str(r["obsid"]) for r in want[i:i + 20]])
    for r in pl:
        rows.append((str(r["obs_collection"]), str(r["obs_id"]), str(r["productFilename"]), int(r["calib_level"]) if str(r["calib_level"]) != "--" else -1, str(r["productSubGroupDescription"]), int(r["size"]) if str(r["size"]) != "--" else 0, str(r["dataURI"])))
seen = {}
for r in rows: seen[r[6]] = r
rows = list(seen.values())
with open("perexposure_products.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["collection", "obs_id", "file", "calib_level", "subgroup", "bytes", "dataURI"]); w.writerows(rows)
tab = collections.defaultdict(lambda: [0, 0])
for coll, oid, fn, cl, sg, sz, uri in rows:
    suf = fn.split("_")[-1] if coll == "JWST" else fn.split("_")[-1].split(".")[0]
    key = (coll, fn.split("_")[0][:6] if coll == "JWST" else "hst", cl, suf)
    tab[key][0] += 1; tab[key][1] += sz
print("\ncollection, group, calib_level, suffix: files, GB")
for k, (n, b) in sorted(tab.items(), key=lambda kv: -kv[1][1])[:40]:
    print(k, n, round(b / 1e9, 2))
