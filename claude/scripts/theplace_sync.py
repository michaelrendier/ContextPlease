#!/usr/bin/env python3
"""theplace_sync.py -- keep one machine's ThePlace as a backup of another's, and see exactly what differs. Standard library plus rsync and ssh.

The model (Cody, 2026-11-28): the Yoga laptop is the main work machine; the X1 Carbon keeps a backup copy of ThePlace. The X1 PULLS from the Yoga; nothing is ever
written on the Yoga. By default nothing is deleted and nothing newer is overwritten: a file changed on BOTH sides is reported as a conflict and left alone, and every
file the pull replaces (or, with --delete, removes) is first moved into a dated backup folder.

    theplace_sync.py diff     --remote yoga:/home/rendier/Projects/ThePlace          # what a pull would do (dry run, grouped by top-level directory)
    theplace_sync.py pull     --remote yoga:/home/rendier/Projects/ThePlace --apply  # do it (add --delete to also remove what is gone on the Yoga)
    theplace_sync.py repos    [--fetch]                                              # branch, HEAD, dirty files, ahead/behind of every repository here
    theplace_sync.py manifest --root DIR --out FILE [--hash]                         # offline route: a file list to carry on the SD card ...
    theplace_sync.py compare  A.json B.json                                          # ... and compare two lists (A newer side, B backup)
    theplace_sync.py repos-compare A.json B.json                                     # compare two `repos --json` outputs

--remote is [user@]host:/path or a plain local path (the test suite uses that). Excluded by default (not part of the backup): .venv, venv, __pycache__, *.pyc,
caches, node_modules, TelescopeArchive (the Yoga's data root: it will not fit here) and Telescope Data style folders; change with --exclude / --no-default-excludes.
Exit codes: 0 ok, 1 usage or safety refusal, 2 rsync failed.
"""
import argparse
import datetime
import fnmatch
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

DEFAULT_EXCLUDES = [".venv/", "venv/", "__pycache__/", "*.pyc", ".mypy_cache/", ".pytest_cache/", ".ipynb_checkpoints/", "node_modules/", ".gradle/",
                    "TelescopeArchive/", "Telescope Data/", ".mirror*", "*.part"]
STATE_DIR = os.path.expanduser("~/.theplace_sync")
SENTINEL = "ContextPlease"          # a directory every real ThePlace has; refuse to sync from or into a folder without it


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def is_remote(spec):
    return bool(re.match(r"^[^/]*:", spec)) and not spec.startswith("/")


def ssh_host_path(spec):
    host, path = spec.split(":", 1)
    return host, path


def sentinel_ok(spec, sentinel):
    if not sentinel:
        return True
    if is_remote(spec):
        host, path = ssh_host_path(spec)
        return run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", host, "test", "-d", os.path.join(path, sentinel)]).returncode == 0
    return os.path.isdir(os.path.join(spec, sentinel))


def rsync_base(args, itemize=True):
    cmd = ["ionice", "-c3", "nice", "-n", "19", "rsync", "-aH", "--numeric-ids", "-s"]      # -s: protect spaces in remote names
    if itemize:
        cmd += ["--itemize-changes", "--out-format=%i|%l|%n"]
    if args.bwlimit:
        cmd += [f"--bwlimit={args.bwlimit}"]
    excl = ([] if args.no_default_excludes else DEFAULT_EXCLUDES) + (args.exclude or [])
    for e in excl:
        cmd += ["--exclude", e]
    return cmd


def source_arg(remote):
    return remote.rstrip("/") + "/"


def classify(lines):
    """Parse rsync --itemize-changes output into {'new': [...], 'changed': [...], 'deleted': [...]} of (path, size)."""
    out = {"new": [], "changed": [], "deleted": []}
    for ln in lines:
        if "|" not in ln:
            if ln.startswith("*deleting"):
                out["deleted"].append((ln.split(None, 1)[1].strip(), 0))
            continue
        flags, size, name = ln.split("|", 2)
        if flags.startswith("*deleting"):
            out["deleted"].append((name, 0))
        elif flags[:2] in (">f", "cf"):
            (out["new"] if "+++++++++" in flags else out["changed"]).append((name, int(size or 0)))
    return out


def dry_run(args, extra=()):
    cmd = rsync_base(args) + ["-n"] + list(extra) + [source_arg(args.remote), source_arg(args.local)]
    r = run(cmd)
    if r.returncode not in (0, 23, 24):
        sys.stderr.write(r.stderr[-800:] + "\n")
        sys.exit(2)
    return classify(r.stdout.splitlines())


def by_top(items):
    g = {}
    for name, size in items:
        top = name.split("/", 1)[0]
        n, b = g.get(top, (0, 0))
        g[top] = (n + 1, b + size)
    return g


def gb(n):
    return f"{n / 1e9:.2f} GB" if n >= 1e8 else f"{n / 1e6:.1f} MB"


def plan(args):
    """The dry run: what a pull would do, with conflicts (changed on both sides) separated from ordinary updates."""
    everything = dry_run(args, ["--delete"])                          # --delete here only LISTS what is gone on the remote (it is a dry run)
    safe = dry_run(args, ["-u"])                                       # -u skips files that are newer on this side
    safe_changed = {n for n, _ in safe["changed"]}
    conflicts = [(n, s) for n, s in everything["changed"] if n not in safe_changed]
    updates = [(n, s) for n, s in everything["changed"] if n in safe_changed]
    return {"new": everything["new"], "updates": updates, "conflicts": conflicts, "deleted": everything["deleted"]}


def print_plan(p, top):
    for key, label in (("new", "NEW on the remote (would be copied)"), ("updates", "CHANGED on the remote, older here (would be replaced; old copy backed up)"),
                       ("conflicts", "CONFLICT: newer here than on the remote (left alone)"), ("deleted", "GONE on the remote (removed here only with --delete; backed up first)")):
        items = p[key]
        print(f"\n{label}: {len(items)} file(s), {gb(sum(s for _, s in items))}")
        for t, (n, b) in sorted(by_top(items).items(), key=lambda kv: -kv[1][1])[:top]:
            print(f"   {t:<40} {n:>7} file(s)  {gb(b)}")
        for name, size in sorted(items, key=lambda x: -x[1])[:min(top, 8)]:
            print(f"      {name}  ({gb(size)})" if size else f"      {name}")


def cmd_diff(args):
    if not sentinel_ok(args.remote, args.sentinel) or not sentinel_ok(args.local, args.sentinel):
        print(f"refused: {args.sentinel}/ not found at one end (wrong folder?). Use --sentinel '' to skip this check.")
        return 1
    p = plan(args)
    print_plan(p, args.top)
    json.dump({k: v for k, v in p.items()}, open(os.path.join(ensure_state(), "last_diff.json"), "w"))
    return 0


def ensure_state():
    os.makedirs(STATE_DIR, exist_ok=True)
    return STATE_DIR


def cmd_pull(args):
    if not sentinel_ok(args.remote, args.sentinel) or not sentinel_ok(args.local, args.sentinel):
        print(f"refused: {args.sentinel}/ not found at one end (wrong folder?). Use --sentinel '' to skip this check.")
        return 1
    if os.path.realpath(args.local) in ("/", os.path.expanduser("~")):
        print("refused: the local root looks like / or the home directory")
        return 1
    p = plan(args)
    print_plan(p, args.top)
    if not args.apply:
        print("\n(dry run: nothing was changed. Add --apply to pull.)")
        return 0
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = os.path.abspath(args.backup_dir or os.path.join(os.path.dirname(os.path.abspath(args.local)) or ".", f"ThePlace_sync_backup_{stamp}"))
    cmd = rsync_base(args, itemize=False) + ["--partial", "-u", "--backup", f"--backup-dir={backup}"]
    if args.delete:
        cmd += ["--delete"]
    cmd += [source_arg(args.remote), source_arg(args.local)]
    t0 = time.time()
    r = subprocess.run(cmd)
    rec = {"when": stamp, "remote": args.remote, "local": args.local, "rsync_code": r.returncode, "seconds": round(time.time() - t0),
           "new": len(p["new"]), "updates": len(p["updates"]), "conflicts": [n for n, _ in p["conflicts"]], "deleted_on_remote": len(p["deleted"]),
           "deleted_here": bool(args.delete), "backup_dir": backup}
    with open(os.path.join(ensure_state(), "history.jsonl"), "a") as fh:
        fh.write(json.dumps(rec) + "\n")
    if os.path.isdir(backup):
        print(f"\nreplaced or removed files were moved to {backup}")
    print("pull finished" if r.returncode in (0, 23, 24) else f"rsync failed (code {r.returncode})")
    return 0 if r.returncode in (0, 23, 24) else 2


def walk(root, excludes, hashing):
    out = {}
    root = os.path.abspath(root)

    def skipped(rel, is_dir):
        parts = rel.split("/")
        for e in excludes:
            pat = e.rstrip("/")
            if e.endswith("/"):
                if any(fnmatch.fnmatch(p, pat) for p in (parts if is_dir else parts[:-1])):
                    return True
            elif fnmatch.fnmatch(parts[-1], pat):
                return True
        return False
    for dp, dn, fn in os.walk(root):
        rel_dir = os.path.relpath(dp, root)
        dn[:] = [d for d in dn if not skipped(os.path.normpath(os.path.join(rel_dir, d)).replace(os.sep, "/").lstrip("./"), True)]
        for f in fn:
            rel = os.path.normpath(os.path.join(rel_dir, f)).replace(os.sep, "/")
            if rel.startswith("./"):
                rel = rel[2:]
            if skipped(rel, False):
                continue
            p = os.path.join(dp, f)
            try:
                st = os.lstat(p)
            except OSError:
                continue
            rec = [st.st_size, int(st.st_mtime)]
            if hashing and os.path.isfile(p) and not os.path.islink(p):
                h = hashlib.sha256()
                with open(p, "rb") as fh:
                    for blk in iter(lambda: fh.read(1 << 20), b""):
                        h.update(blk)
                rec.append(h.hexdigest())
            out[rel] = rec
    return out


def cmd_manifest(args):
    excl = offline_excludes(args)
    m = walk(args.root, excl, args.hash)
    json.dump({"root": os.path.abspath(args.root), "host": os.uname().nodename, "when": datetime.datetime.now().isoformat(timespec="seconds"), "hashed": bool(args.hash), "files": m},
              open(args.out, "w"))
    print(f"{len(m)} files, {gb(sum(v[0] for v in m.values()))} -> {args.out}")
    return 0


def cmd_compare(args):
    a, b = json.load(open(args.a)), json.load(open(args.b))
    fa, fb = a["files"], b["files"]
    only_a = sorted(set(fa) - set(fb))
    only_b = sorted(set(fb) - set(fa))
    differ = []
    for k in set(fa) & set(fb):
        x, y = fa[k], fb[k]
        if len(x) > 2 and len(y) > 2:
            if x[2] != y[2]:
                differ.append((k, x[0], x[1], y[1]))
        elif x[0] != y[0] or abs(x[1] - y[1]) > 2:
            differ.append((k, x[0], x[1], y[1]))
    newer_a = [d for d in differ if d[2] > d[3]]
    newer_b = [d for d in differ if d[2] < d[3]]
    print(f"A: {a['host']} {a['root']} ({len(fa)} files)   B: {b['host']} {b['root']} ({len(fb)} files)")
    for label, items in (("only in A (would be added to B)", only_a), ("only in B (not in A: removed on A, or never copied)", only_b)):
        sz = sum((fa if items is only_a else fb)[k][0] for k in items)
        print(f"\n{label}: {len(items)} file(s), {gb(sz)}")
        for t, (n, bb) in sorted(by_top([(k, (fa if items is only_a else fb)[k][0]) for k in items]).items(), key=lambda kv: -kv[1][1])[:args.top]:
            print(f"   {t:<40} {n:>7}  {gb(bb)}")
    print(f"\nchanged, A newer (B is out of date): {len(newer_a)}   changed, B newer (conflict: B was edited after A): {len(newer_b)}")
    for k, s, ma, mb in sorted(newer_b)[:args.top]:
        print(f"   CONFLICT {k}")
    return 0


def git(path, *a):
    r = run(["git", "-C", path, *a])
    return r.stdout.strip() if r.returncode == 0 else ""


def repo_states(root, fetch):
    root = os.path.abspath(root)
    out = {}
    for name in sorted(os.listdir(root)):
        d = os.path.join(root, name)
        if not os.path.isdir(os.path.join(d, ".git")):
            continue
        if fetch:
            run(["git", "-C", d, "fetch", "--quiet"])
        st = git(d, "status", "--porcelain").splitlines()
        lr = git(d, "rev-list", "--left-right", "--count", "@{u}...HEAD").split()
        out[name] = {"branch": git(d, "rev-parse", "--abbrev-ref", "HEAD"), "head": git(d, "rev-parse", "--short", "HEAD"), "dirty": sum(1 for s in st if not s.startswith("??")),
                     "untracked": sum(1 for s in st if s.startswith("??")), "behind": int(lr[0]) if len(lr) == 2 else None, "ahead": int(lr[1]) if len(lr) == 2 else None,
                     "has_upstream": len(lr) == 2, "dirty_files": [s[3:] for s in st if not s.startswith("??")][:200]}
    return out


def cmd_repos(args):
    root = os.path.abspath(args.root)
    out = repo_states(root, args.fetch)
    if args.json:
        print(json.dumps({"host": os.uname().nodename, "root": root, "repos": out}))
    else:
        print(f"{'repo':<28}{'branch':<22}{'head':<10}{'dirty':>6}{'untracked':>10}{'behind':>8}{'ahead':>7}")
        for n, v in out.items():
            print(f"{n:<28}{v['branch']:<22}{v['head']:<10}{v['dirty']:>6}{v['untracked']:>10}{str(v['behind']):>8}{str(v['ahead']):>7}")
    return 0


def cmd_repos_compare(args):
    a, b = json.load(open(args.a)), json.load(open(args.b))
    names = sorted(set(a["repos"]) | set(b["repos"]))
    print(f"A: {a['host']}   B: {b['host']}")
    for n in names:
        x, y = a["repos"].get(n), b["repos"].get(n)
        if x is None or y is None:
            print(f"  {n:<28} only on {'A' if y is None else 'B'}")
        elif (x["head"], x["branch"], x["dirty"]) != (y["head"], y["branch"], y["dirty"]):
            print(f"  {n:<28} A {x['branch']}@{x['head']} dirty {x['dirty']}   B {y['branch']}@{y['head']} dirty {y['dirty']}")
    return 0


# ---------------------------------------------------------------- the offline route: manifests and a delta carried on the SD card
# THE PROTOCOL (no network between the machines; the card is the only link; nothing is ever written on the machine that only reads):
#   1. X1  (the backup)   manifest --root ~/Projects/ThePlace --out CARD/sync/x1_manifest.json          what the backup holds now
#   2. Yoga (main)        delta    --card CARD/sync --root ~/Projects/ThePlace                          reads x1_manifest.json, copies what is new or newer on the Yoga into
#                                                                                                       CARD/sync/delta/, writes delta_manifest.json (sha256 of every file),
#                                                                                                       repos_<host>.json (branch, HEAD, ahead/behind, dirty files), bundles/<repo>.bundle
#                                                                                                       for every repository with commits that are not on its origin
#   3. X1                 apply-card --card CARD/sync --local ~/Projects/ThePlace [--apply]             verifies the hashes, plans (dry run by default), applies with backups;
#                                                                                                       a file newer on the X1 is a conflict and is left alone; bundles are
#                                                                                                       fetched into refs/remotes/yoga/* (the X1's own branches are never moved)
# .git/ directories are NOT copied file by file (a repository mid-operation would arrive half-updated); git history travels through GitHub or the bundles.

def offline_excludes(args):
    return ([] if args.no_default_excludes else DEFAULT_EXCLUDES) + ([] if args.with_git else [".git/"]) + (args.exclude or [])


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def cmd_delta(args):
    """Run on the main machine: copy what is new or newer here (compared with the backup's manifest) onto the card."""
    root = os.path.abspath(args.root)
    if args.sentinel and not os.path.isdir(os.path.join(root, args.sentinel)):
        print(f"refused: {args.sentinel}/ not found in {root}")
        return 1
    other = json.load(open(os.path.join(args.card, "x1_manifest.json")))
    theirs = other["files"]
    mine = walk(root, offline_excludes(args), False)
    new, changed, conflicts, same = [], [], [], 0
    for rel, (size, mtime) in mine.items():
        o = theirs.get(rel)
        if o is None:
            new.append(rel)
        elif o[0] == size and abs(o[1] - mtime) <= 2:
            same += 1
        elif mtime > o[1] + 2:
            changed.append(rel)
        else:
            conflicts.append(rel)                                  # the backup's copy is newer (or the same age but different): left alone
    only_other = sorted(set(theirs) - set(mine))
    todo = new + changed
    need = sum(mine[r][0] for r in todo)
    free = shutil.disk_usage(args.card).free
    print(f"{len(mine)} files here; same {same}, new {len(new)}, newer here {len(changed)}, CONFLICT (newer on the backup) {len(conflicts)}, only on the backup {len(only_other)}")
    print(f"to copy: {len(todo)} file(s), {gb(need)}; card has {gb(free)} free")
    if need + 5e9 > free:
        print("refused: not enough space on the card (5 GB are kept free)")
        return 1
    d = os.path.join(args.card, "delta")
    files = {}
    for i, rel in enumerate(sorted(todo), 1):
        dst = os.path.join(d, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(root, rel), dst)
        files[rel] = [mine[rel][0], mine[rel][1], sha256_file(dst)]
        if i % 500 == 0:
            print(f"  copied {i} of {len(todo)}")
    repos = repo_states(root, False)
    bundles = {}
    for name, v in repos.items():
        if (v["ahead"] or not v["has_upstream"]) and not args.no_bundles:
            bdir = os.path.join(args.card, "bundles")
            os.makedirs(bdir, exist_ok=True)
            b = os.path.join(bdir, name + ".bundle")
            r = run(["git", "-C", os.path.join(root, name), "bundle", "create", b, "--all"])
            if r.returncode == 0:
                bundles[name] = {"sha256": sha256_file(b), "size": os.path.getsize(b)}
    json.dump({"host": os.uname().nodename, "root": root, "when": datetime.datetime.now().isoformat(timespec="seconds"), "files": files, "conflicts": conflicts,
               "only_on_other": only_other, "bundles": bundles}, open(os.path.join(args.card, "delta_manifest.json"), "w"))
    json.dump({"host": os.uname().nodename, "root": root, "repos": repos}, open(os.path.join(args.card, f"repos_{os.uname().nodename}.json"), "w"))
    print(f"delta written to {d}; {len(bundles)} bundle(s); repos_{os.uname().nodename}.json written. Now take the card to the backup machine and run apply-card.")
    return 0


def cmd_apply_card(args):
    """Run on the backup machine: check the delta on the card against the manifest hashes, plan, and (with --apply) copy it in with backups."""
    local = os.path.abspath(args.local)
    if args.sentinel and not os.path.isdir(os.path.join(local, args.sentinel)):
        print(f"refused: {args.sentinel}/ not found in {local}")
        return 1
    if os.path.realpath(local) in ("/", os.path.expanduser("~")):
        print("refused: the local root looks like / or the home directory")
        return 1
    dm = json.load(open(os.path.join(args.card, "delta_manifest.json")))
    plan_new, plan_up, plan_conf, bad = [], [], [], []
    for rel, (size, mtime, digest) in dm["files"].items():
        src = os.path.join(args.card, "delta", rel)
        if not os.path.isfile(src) or sha256_file(src) != digest:
            bad.append(rel)
            continue
        dst = os.path.join(local, rel)
        if not os.path.lexists(dst):
            plan_new.append((rel, size))
        elif int(os.lstat(dst).st_mtime) + 2 < mtime:
            plan_up.append((rel, size))
        else:
            plan_conf.append((rel, size))
    gone = [r for r in dm["only_on_other"] if os.path.lexists(os.path.join(local, r))]
    print(f"from {dm['host']} ({dm['when']}): new {len(plan_new)}, newer on the card {len(plan_up)}, CONFLICT (newer here, left alone) {len(plan_conf)}, damaged on the card {len(bad)}, "
          f"gone on the main machine {len(gone)} (removed here only with --delete)")
    for label, items in (("NEW", plan_new), ("UPDATE", plan_up), ("CONFLICT", plan_conf)):
        for t, (n, b) in sorted(by_top(items).items(), key=lambda kv: -kv[1][1])[:args.top]:
            print(f"   {label:<9}{t:<40}{n:>7} file(s)  {gb(b)}")
    for r in bad[:10]:
        print("   DAMAGED (hash mismatch or missing on the card):", r)
    rj = os.path.join(args.card, f"repos_{dm['host']}.json")
    if os.path.exists(rj):
        mine = repo_states(local, False)
        print("\nrepositories that differ (card machine vs here):")
        for n, v in sorted(json.load(open(rj))["repos"].items()):
            w = mine.get(n)
            if w is None:
                print(f"   {n:<28} only on {dm['host']}")
            elif (v["head"], v["branch"], v["dirty"]) != (w["head"], w["branch"], w["dirty"]):
                print(f"   {n:<28} {dm['host']}: {v['branch']}@{v['head']} dirty {v['dirty']} ahead {v['ahead']}   here: {w['branch']}@{w['head']} dirty {w['dirty']}")
    if not args.apply:
        print("\n(dry run: nothing was changed. Add --apply.)")
        return 0
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = os.path.abspath(args.backup_dir or os.path.join(os.path.dirname(local), f"ThePlace_sync_backup_{stamp}"))
    done = 0
    for rel, _ in plan_new + plan_up:
        src, dst = os.path.join(args.card, "delta", rel), os.path.join(local, rel)
        if os.path.lexists(dst):
            b = os.path.join(backup, rel)
            os.makedirs(os.path.dirname(b), exist_ok=True)
            shutil.move(dst, b)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        done += 1
    removed = 0
    if args.delete:
        for r in gone:
            b = os.path.join(backup, r)
            os.makedirs(os.path.dirname(b), exist_ok=True)
            shutil.move(os.path.join(local, r), b)
            removed += 1
    for name, info in dm.get("bundles", {}).items():
        bpath = os.path.join(args.card, "bundles", name + ".bundle")
        repo = os.path.join(local, name)
        if os.path.isdir(os.path.join(repo, ".git")) and os.path.isfile(bpath) and sha256_file(bpath) == info["sha256"]:
            r = run(["git", "-C", repo, "fetch", "--quiet", bpath, "+refs/heads/*:refs/remotes/yoga/*"])
            print(f"   bundle {name}: {'fetched into refs/remotes/yoga/*' if r.returncode == 0 else 'fetch failed: ' + r.stderr.strip()[-120:]}")
    rec = {"when": stamp, "card_host": dm["host"], "copied": done, "removed": removed, "conflicts": [r for r, _ in plan_conf], "damaged": bad, "backup_dir": backup}
    with open(os.path.join(ensure_state(), "history.jsonl"), "a") as fh:
        fh.write(json.dumps(rec) + "\n")
    print(f"\ncopied {done} file(s), removed {removed}; replaced files were moved to {backup}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p, remote=True):
        if remote:
            p.add_argument("--remote", required=True, help="[user@]host:/path/to/ThePlace (the machine to pull FROM), or a local path")
            p.add_argument("--local", default=os.path.expanduser("~/Projects/ThePlace"))
            p.add_argument("--bwlimit", type=int, default=0, help="KB/s")
            p.add_argument("--sentinel", default=SENTINEL)
            p.add_argument("--top", type=int, default=15)
        p.add_argument("--exclude", action="append")
        p.add_argument("--no-default-excludes", action="store_true")
    d = sub.add_parser("diff"); common(d); d.set_defaults(fn=cmd_diff)
    p = sub.add_parser("pull"); common(p)
    p.add_argument("--apply", action="store_true"); p.add_argument("--delete", action="store_true"); p.add_argument("--backup-dir")
    p.set_defaults(fn=cmd_pull)
    m = sub.add_parser("manifest"); common(m, remote=False); m.add_argument("--root", required=True); m.add_argument("--out", required=True)
    m.add_argument("--hash", action="store_true"); m.add_argument("--with-git", action="store_true", help="include .git/ (excluded by default in the offline route)"); m.set_defaults(fn=cmd_manifest)
    dl = sub.add_parser("delta", help="main machine: copy what is new or newer onto the card"); common(dl, remote=False)
    dl.add_argument("--card", required=True); dl.add_argument("--root", default=os.path.expanduser("~/Projects/ThePlace")); dl.add_argument("--sentinel", default=SENTINEL)
    dl.add_argument("--with-git", action="store_true"); dl.add_argument("--no-bundles", action="store_true"); dl.set_defaults(fn=cmd_delta)
    ac = sub.add_parser("apply-card", help="backup machine: check the card's delta and copy it in"); common(ac, remote=False)
    ac.add_argument("--card", required=True); ac.add_argument("--local", default=os.path.expanduser("~/Projects/ThePlace")); ac.add_argument("--sentinel", default=SENTINEL)
    ac.add_argument("--apply", action="store_true"); ac.add_argument("--delete", action="store_true"); ac.add_argument("--backup-dir"); ac.add_argument("--top", type=int, default=15)
    ac.set_defaults(fn=cmd_apply_card)
    c = sub.add_parser("compare"); c.add_argument("a"); c.add_argument("b"); c.add_argument("--top", type=int, default=15); c.set_defaults(fn=cmd_compare)
    r = sub.add_parser("repos"); r.add_argument("--root", default=os.path.expanduser("~/Projects/ThePlace")); r.add_argument("--fetch", action="store_true")
    r.add_argument("--json", action="store_true"); r.set_defaults(fn=cmd_repos)
    rc = sub.add_parser("repos-compare"); rc.add_argument("a"); rc.add_argument("b"); rc.set_defaults(fn=cmd_repos_compare)
    a = ap.parse_args(argv)
    if shutil.which("rsync") is None and a.cmd in ("diff", "pull"):
        print("rsync is required")
        return 1
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
