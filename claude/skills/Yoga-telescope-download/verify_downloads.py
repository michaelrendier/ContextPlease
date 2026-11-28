#!/usr/bin/env python3
"""Verify a finished or interrupted telescope download against its manifest and state. Read-only, resumable, low memory.

    python3 verify_downloads.py MANIFEST.json STATE.json [--checkpoint FILE] [--no-hash]

For every manifest entry: the file exists, its size equals the manifest size (when the manifest knows it), and its sha256
equals the one recorded in STATE. Progress is checkpointed (a JSON list of verified paths) so an interrupted run resumes.
Exit code 0 = all verified, 1 = problems found (listed; nothing is repaired or deleted).
"""
import argparse, hashlib, json, os, sys, time

ap = argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("state")
ap.add_argument("--checkpoint"); ap.add_argument("--no-hash", action="store_true"); a = ap.parse_args()
cp = a.checkpoint or a.state + ".verified"
items = json.load(open(a.manifest)); state = json.load(open(a.state))
done = set(json.load(open(cp))) if os.path.exists(cp) else set()
bad = []; t0 = time.time(); nbytes = 0
try: os.nice(15)
except OSError: pass
for k, it in enumerate(items, 1):
    d = it["dest"]
    if d in done: continue
    if not os.path.exists(d): bad.append((d, "missing")); continue
    sz = os.path.getsize(d)
    if it.get("size") and sz != it["size"]: bad.append((d, f"size {sz} != {it['size']}")); continue
    rec = state.get(d)
    if not rec: bad.append((d, "not in state")); continue
    if rec["bytes"] != sz: bad.append((d, f"state bytes {rec['bytes']} != {sz}")); continue
    if not a.no_hash:
        h = hashlib.sha256()
        with open(d, "rb") as f:
            for b in iter(lambda: f.read(8 << 20), b""): h.update(b)
        nbytes += sz
        if h.hexdigest() != rec["sha256"]: bad.append((d, "sha256 differs from the recorded one")); continue
    done.add(d)
    if k % 50 == 0:
        tmp = cp + ".tmp"; json.dump(sorted(done), open(tmp, "w")); os.replace(tmp, cp)
        print(f"[verify] {k}/{len(items)} entries, {nbytes/1e9:.1f} GB hashed, {nbytes/1e6/max(time.time()-t0,1e-9):.0f} MB/s, problems so far {len(bad)}", flush=True)
tmp = cp + ".tmp"; json.dump(sorted(done), open(tmp, "w")); os.replace(tmp, cp)
print(f"[verify] finished: {len(done)}/{len(items)} verified, {len(bad)} problem(s)")
for d, why in bad: print("  PROBLEM", d, "-", why)
sys.exit(1 if bad else 0)
