#!/usr/bin/env python3
"""Read-only field survey: JWST per-camera counts, polarizer filters in MAST, NRAO TAP polarization states.

    python3 survey_field.py "11h49m35.7s +22d23m45s" [--jwst-arcsec 10] [--mast-arcsec 60] [--nrao-deg 0.01]

Needs astroquery + astropy + requests (use the venv that has them; NOT python -I).
NRAO sizes (access_estsize, kB) are per row (scan/spectral window) and OVERCOUNT: read them as scale only.
"""
import argparse, collections, csv, io, requests, astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.mast import Observations

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
ap = argparse.ArgumentParser(); ap.add_argument("coord")
ap.add_argument("--jwst-arcsec", type=float, default=10); ap.add_argument("--mast-arcsec", type=float, default=60)
ap.add_argument("--nrao-deg", type=float, default=0.01); a = ap.parse_args()
Observations._session.headers["User-Agent"] = UA
c = SkyCoord(a.coord)
o = Observations.query_region(c, radius=a.jwst_arcsec * u.arcsec)
j = o[o["obs_collection"] == "JWST"]
print(f"JWST observations within {a.jwst_arcsec}\": {len(j)}")
by = collections.defaultdict(list)
for r in j:
    by[(str(r["proposal_id"]), str(r["instrument_name"]).split("/")[0])].append(str(r["filters"]))
for k, v in sorted(by.items()):
    print("  ", k, len(v), "obs", sorted(set(v))[:8])
o = Observations.query_region(c, radius=a.mast_arcsec * u.arcsec)
pol = collections.Counter((str(r["obs_collection"]), str(r["instrument_name"]), str(r["filters"]))
                          for r in o if "POL" in str(r["filters"]).upper())
print(f"MAST polarizer filters within {a.mast_arcsec}\":", dict(pol) or "none")
q = ("SELECT instrument_name,pol_states,em_min,s_resolution,obs_publisher_did,access_estsize FROM tap_schema.obscore "
     f"WHERE 1=CONTAINS(POINT('ICRS',s_ra,s_dec),CIRCLE('ICRS',{c.ra.deg},{c.dec.deg},{a.nrao_deg}))")
r = requests.post("https://data-query.nrao.edu/tap/sync", headers={"User-Agent": UA}, timeout=180,
                  data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": q})
g = collections.defaultdict(lambda: [0, set(), []])
for x in csv.DictReader(io.StringIO(r.text)):
    pid = "ALMA" if x["instrument_name"] == "ALMA" else x["obs_publisher_did"].split("/")[-1][:14]
    k = (x["instrument_name"], x["pol_states"], pid); g[k][0] += 1
    try: g[k][1].add(round(float(x["em_min"]) * 100, 1))
    except (TypeError, ValueError): pass
    try: g[k][2].append(float(x["s_resolution"]))
    except (TypeError, ValueError): pass
print("NRAO TAP rows by (instrument, pol_states, program): rows, wavelength cm, beam arcsec (min..max)")
for k, v in sorted(g.items(), key=lambda kv: -kv[1][0])[:15]:
    b = f"{min(v[2]):.2f}..{max(v[2]):.2f}" if v[2] else "n/a"
    print("  ", k, v[0], sorted(v[1])[:3], b)
