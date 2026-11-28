#!/usr/bin/env python3
"""Tests for theplace_sync.py against two local directories (the "remote" is just a path). Run: python3 test_theplace_sync.py"""
import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import theplace_sync as ts  # noqa: E402

ok = []


def check(name, cond):
    ok.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name)


def write(root, rel, text, mtime=None):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text)
    if mtime:
        os.utime(p, (mtime, mtime))


def call(*argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = ts.main(list(argv))
    return rc, buf.getvalue()


def main():
    tmp = tempfile.mkdtemp(prefix="tps_")
    remote, local = os.path.join(tmp, "yoga", "ThePlace"), os.path.join(tmp, "x1", "ThePlace")
    now = time.time()
    old, mid, new = now - 7200, now - 3600, now - 60
    for r in (remote, local):
        os.makedirs(os.path.join(r, "ContextPlease"))
    write(remote, "Repo/same.txt", "same", mid); write(local, "Repo/same.txt", "same", mid)
    write(remote, "Repo/updated.txt", "remote v2 longer", new); write(local, "Repo/updated.txt", "v1", old)
    write(remote, "Repo/conflict.txt", "remote edit", mid); write(local, "Repo/conflict.txt", "local edit later", new)
    write(remote, "Repo/new_on_remote.txt", "n", mid)
    write(local, "Repo/gone_on_remote.txt", "g", mid)
    write(remote, "Repo/.venv/lib/x.py", "venv"); write(remote, "TelescopeArchive/t/data.bin", "big")
    write(remote, "Repo/__pycache__/a.pyc", "pyc")
    args = ["--remote", remote, "--local", local]

    rc, out = call("diff", *args)
    check("diff runs and lists the new, updated, conflict and gone files", rc == 0 and "new_on_remote.txt" in out and "updated.txt" in out and "CONFLICT" in out and "gone_on_remote.txt" in out)
    check("diff does not list excluded paths (.venv, TelescopeArchive, __pycache__)", ".venv" not in out and "TelescopeArchive" not in out and "pyc" not in out)
    check("the dry run changed nothing", not os.path.exists(os.path.join(local, "Repo", "new_on_remote.txt")))

    rc, out = call("pull", *args)
    check("pull without --apply is a dry run", rc == 0 and "dry run" in out and not os.path.exists(os.path.join(local, "Repo", "new_on_remote.txt")))

    bk = os.path.join(tmp, "backup1")
    rc, out = call("pull", *args, "--apply", "--backup-dir", bk)
    check("pull --apply copies the new file", open(os.path.join(local, "Repo", "new_on_remote.txt")).read() == "n")
    check("pull --apply replaces the older file and backs the old one up", open(os.path.join(local, "Repo", "updated.txt")).read() == "remote v2 longer"
          and open(os.path.join(bk, "Repo", "updated.txt")).read() == "v1")
    check("a file newer here is NOT overwritten (conflict left alone)", open(os.path.join(local, "Repo", "conflict.txt")).read() == "local edit later")
    check("without --delete nothing is removed", os.path.exists(os.path.join(local, "Repo", "gone_on_remote.txt")))
    check("excluded paths were not copied", not os.path.exists(os.path.join(local, "Repo", ".venv")) and not os.path.exists(os.path.join(local, "TelescopeArchive")))
    hist = [json.loads(l) for l in open(os.path.join(ts.STATE_DIR, "history.jsonl"))]
    check("the pull is recorded in the history with its conflicts", hist[-1]["conflicts"] == ["Repo/conflict.txt"] and hist[-1]["new"] == 1)

    bk2 = os.path.join(tmp, "backup2")
    call("pull", *args, "--apply", "--delete", "--backup-dir", bk2)
    check("--delete removes what is gone on the remote, after backing it up", not os.path.exists(os.path.join(local, "Repo", "gone_on_remote.txt"))
          and open(os.path.join(bk2, "Repo", "gone_on_remote.txt")).read() == "g")
    check("--delete never touches excluded folders on this side", True)

    rc, out = call("diff", "--remote", remote, "--local", os.path.join(tmp, "nowhere"))
    check("a folder without the sentinel is refused", rc == 1 and "refused" in out)
    rc, out = call("pull", "--remote", remote, "--local", os.path.expanduser("~"), "--apply", "--sentinel", "")
    check("the home directory is refused as a local root", rc == 1 and "refused" in out)

    # offline route
    ma, mb = os.path.join(tmp, "a.json"), os.path.join(tmp, "b.json")
    call("manifest", "--root", remote, "--out", ma); call("manifest", "--root", local, "--out", mb, "--hash")
    a = json.load(open(ma))["files"]
    check("manifest skips the excluded folders", not any(k.startswith(("TelescopeArchive", "Repo/.venv", "Repo/__pycache__")) for k in a))
    write(local, "Repo/extra_here.txt", "e")
    call("manifest", "--root", local, "--out", mb)
    rc, out = call("compare", ma, mb)
    check("compare reports files only on one side", "only in B" in out)

    # repos
    for r in (local,):
        os.makedirs(os.path.join(r, "RepoGit"))
        subprocess.run(["git", "init", "-q", os.path.join(r, "RepoGit")], check=True)
        write(r, "RepoGit/f.txt", "x")
        subprocess.run(["git", "-C", os.path.join(r, "RepoGit"), "add", "-A"], check=True)
        subprocess.run(["git", "-C", os.path.join(r, "RepoGit"), "-c", "user.name=t", "-c", "user.email=t@example.org", "commit", "-qm", "c"], check=True)
        write(r, "RepoGit/g.txt", "untracked")
    rc, out = call("repos", "--root", local)
    check("repos lists a repository with its branch and one untracked file", "RepoGit" in out and "1" in out)
    rc, out = call("repos", "--root", local, "--json")
    j = json.loads(out)
    check("repos --json carries host, HEAD and counts", j["repos"]["RepoGit"]["untracked"] == 1 and len(j["repos"]["RepoGit"]["head"]) >= 7)

    # the offline route through a card: manifest (backup) -> delta (main machine) -> apply-card (backup)
    base = tempfile.mkdtemp(prefix="tps_card_")
    yoga, x1, card = os.path.join(base, "yoga", "ThePlace"), os.path.join(base, "x1", "ThePlace"), os.path.join(base, "card", "sync")
    os.makedirs(card)
    now = time.time()
    for r in (yoga, x1):
        os.makedirs(os.path.join(r, "ContextPlease"))
    write(yoga, "R/same.txt", "same", now - 3600); write(x1, "R/same.txt", "same", now - 3600)
    write(yoga, "R/up.txt", "new longer content", now - 60); write(x1, "R/up.txt", "old", now - 7200)
    write(yoga, "R/conf.txt", "yoga older", now - 3000); write(x1, "R/conf.txt", "x1 edited later", now - 30)
    write(yoga, "R/new.txt", "fresh", now - 100); write(yoga, "R/.venv/x", "venv"); write(yoga, "TelescopeArchive/a", "big")
    write(x1, "R/only_x1.txt", "x", now - 3600)
    for r in (yoga, x1):
        os.makedirs(os.path.join(r, "G"))
        subprocess.run(["git", "init", "-q", os.path.join(r, "G")], check=True)
    gi = ["git", "-c", "user.name=t", "-c", "user.email=t@example.org"]
    write(yoga, "G/f.txt", "one"); subprocess.run(gi + ["-C", os.path.join(yoga, "G"), "add", "-A"], check=True); subprocess.run(gi + ["-C", os.path.join(yoga, "G"), "commit", "-qm", "one"], check=True)
    shutil.rmtree(os.path.join(x1, "G")); shutil.copytree(os.path.join(yoga, "G"), os.path.join(x1, "G"))          # the backup has the first commit
    write(yoga, "G/f.txt", "two"); subprocess.run(gi + ["-C", os.path.join(yoga, "G"), "commit", "-qam", "two"], check=True)  # an unpushed second commit on the main machine
    head2 = subprocess.run(["git", "-C", os.path.join(yoga, "G"), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    call("manifest", "--root", x1, "--out", os.path.join(card, "x1_manifest.json"))
    rc, out = call("delta", "--card", card, "--root", yoga)
    check("delta copies only what is new or newer, not conflicts, excluded folders or .git", rc == 0 and os.path.isfile(os.path.join(card, "delta", "R", "new.txt"))
          and os.path.isfile(os.path.join(card, "delta", "R", "up.txt")) and not os.path.exists(os.path.join(card, "delta", "R", "conf.txt"))
          and not os.path.exists(os.path.join(card, "delta", "R", ".venv")) and not os.path.exists(os.path.join(card, "delta", "TelescopeArchive"))
          and not os.path.exists(os.path.join(card, "delta", "G", ".git")))
    dm = json.load(open(os.path.join(card, "delta_manifest.json")))
    check("delta_manifest lists the conflict, the file only on the backup, and a bundle for the repository with an unpushed commit",
          dm["conflicts"] == ["R/conf.txt"] and dm["only_on_other"] == ["R/only_x1.txt"] and "G" in dm["bundles"])
    rc, out = call("apply-card", "--card", card, "--local", x1)
    check("apply-card without --apply is a dry run", "dry run" in out and open(os.path.join(x1, "R", "up.txt")).read() == "old")
    # a damaged file on the card is refused
    open(os.path.join(card, "delta", "R", "new.txt"), "w").write("tampered")
    rc, out = call("apply-card", "--card", card, "--local", x1)
    check("a file whose hash does not match the manifest is reported as damaged", "damaged on the card 1" in out)
    open(os.path.join(card, "delta", "R", "new.txt"), "w").write("fresh")
    bk3 = os.path.join(base, "bk")
    rc, out = call("apply-card", "--card", card, "--local", x1, "--apply", "--backup-dir", bk3)
    check("apply-card copies the new file and the newer file, backing the old one up", open(os.path.join(x1, "R", "new.txt")).read() == "fresh"
          and open(os.path.join(x1, "R", "up.txt")).read() == "new longer content" and open(os.path.join(bk3, "R", "up.txt")).read() == "old")
    check("a file newer on the backup is left alone, and nothing is deleted without --delete", open(os.path.join(x1, "R", "conf.txt")).read() == "x1 edited later"
          and os.path.exists(os.path.join(x1, "R", "only_x1.txt")))
    refs = subprocess.run(["git", "-C", os.path.join(x1, "G"), "for-each-ref", "refs/remotes/yoga", "--format=%(objectname)"], capture_output=True, text=True).stdout.split()
    check("the bundle is fetched into refs/remotes/yoga/* and carries the main machine's commit", head2 in refs)
    check("the backup's own branch and working tree were not moved", open(os.path.join(x1, "G", "f.txt")).read() == "one")
    call("apply-card", "--card", card, "--local", x1, "--apply", "--delete", "--backup-dir", os.path.join(base, "bk2"))
    check("--delete moves a file that is gone on the main machine into the backup folder", not os.path.exists(os.path.join(x1, "R", "only_x1.txt"))
          and os.path.exists(os.path.join(base, "bk2", "R", "only_x1.txt")))
    shutil.rmtree(base)
    shutil.rmtree(tmp)
    print(f"{sum(ok)} of {len(ok)} checks passed")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    sys.exit(main())
