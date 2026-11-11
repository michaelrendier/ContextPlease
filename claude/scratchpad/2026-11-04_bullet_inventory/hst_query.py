import os, collections, astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.mast import Observations
UA=os.environ.get("CLAUDE_UA","Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0")
Observations._session.headers["User-Agent"]=UA
c=SkyCoord(104.6098*u.deg,-55.9446*u.deg)
o=Observations.query_region(c,radius=4*u.arcmin)
h=[r for r in o if str(r["obs_collection"])=="HST" and str(r["dataproduct_type"]).lower()=="image"]
print("HST image observations within 4':",len(h))
cnt=collections.Counter((str(r["proposal_id"]),str(r["instrument_name"]),str(r["filters"])) for r in h)
for k,v in sorted(cnt.items()): print(" ",k,v)
pl=Observations.get_product_list([str(r["obsid"]) for r in h])
tab=collections.defaultdict(lambda:[0,0])
for r in pl:
    fn=str(r["productFilename"]); suf=fn.rsplit("_",1)[-1].split(".")[0]
    if not fn.endswith(".fits"): continue
    k=(suf,int(r["calib_level"]) if str(r["calib_level"])!="--" else -1); tab[k][0]+=1; tab[k][1]+=int(r["size"])
for k,(n,b) in sorted(tab.items(), key=lambda kv:-kv[1][1])[:14]: print(k,n,round(b/1e9,2),"GB")
import csv
with open("hst_products.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["obs_id","file","calib","bytes","uri","proposal"])
    pm={str(r["obsid"]):str(r["proposal_id"]) for r in h}
    seen=set()
    for r in pl:
        u_=str(r["dataURI"])
        if u_ in seen: continue
        seen.add(u_); w.writerow([r["obs_id"],r["productFilename"],r["calib_level"],r["size"],u_,pm.get(str(r["parent_obsid"]),"")])
