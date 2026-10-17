#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Michael Rendier'
# hallway_mount.py — the mount-based "walk the hallway", names kept from
# ~/Projects/Coding/BIOS/WalkTheHalls.py (HallwayStroll.the_rooms / the_hallway).
#
# What it does, in his order:
#   1. mount the FILE as -t sysfs, look for proc/filesystems INSIDE that mount, note what is found, umount
#   2. take the filesystem list (from step 1 if it exists there, else the kernel's /proc/filesystems)
#   3. remount the FILE read-only, one room per device-backed type, plus a comma-list "All" room
#   4. record, per room, whether it mounted and the structure (paths + kinds, never content), then umount
#
# HARD WALL: nothing here ever lists, opens, globs, cd's into or walks a path that touches AppArmor.
# guard() refuses it before any filesystem call. The script never changes directory and never walks a
# pseudo (nodev) mount; the sysfs step reads exactly ONE path and stats nothing else.
#
# DRY RUN by default. --execute is required to mount anything.
#
# USAGE: hallway_mount.py FILE [--work DIR] [--execute] [--include-nodev-types] [--selftest]

import os
import re
import sys
import json
import argparse
import hashlib
import subprocess
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Tuple

# ── the wall ────────────────────────────────────────────────────────────────
WALL_WORD = re.compile(r'apparmor', re.I)
WALL_PREFIXES = (
    '/sys/kernel/security', '/sys/module/apparmor', '/sys/fs/apparmor',
    '/etc/apparmor', '/etc/apparmor.d', '/var/lib/apparmor', '/var/cache/apparmor',
    '/proc/self/attr', '/proc/thread-self/attr',
)
# securityfs is where AppArmor's tree is exposed: never mounted, never probed
NEVER_MOUNT = {'securityfs', 'apparmorfs'}
PROBE_FIRST = ['squashfs', 'iso9660', 'udf', 'vfat', 'exfat', 'ext4', 'ext3', 'ext2',
               'btrfs', 'xfs', 'f2fs', 'ntfs3', 'ntfs', 'hfsplus', 'hfs', 'cramfs', 'romfs', 'erofs',
               'jffs2', 'ubifs', 'minix', 'hpfs', 'jfs', 'nilfs2', 'bfs', 'befs', 'efs', 'affs', 'adfs',
               'ufs', 'sysv', 'qnx4', 'qnx6', 'omfs', 'reiserfs', 'ocfs2', 'gfs2']
MODDIR = {'iso9660': 'isofs', 'sysv': 'sysv', 'vxfs': 'freevxfs'}   # fs type name -> kernel/fs module dir
MOUNT_OPTS = 'ro,nosuid,nodev,noexec'
STEP_TIMEOUT = 20          # seconds, every external command
WALK_MAX_DEPTH = 3
WALK_MAX_ENTRIES = 5000


class Wall(Exception):
    """Raised, never caught inside this module, when a path touches AppArmor."""


def walled(path: str) -> bool:
    """String-level test only. Deliberately does NOT touch the filesystem (no realpath, no stat)."""
    p = os.path.normpath(path)
    if WALL_WORD.search(p):
        return True
    return any(p == w or p.startswith(w + os.sep) for w in WALL_PREFIXES)


def guard(path: str) -> str:
    if walled(path):
        raise Wall(f'HARD WALL: refusing AppArmor path {path!r}')
    return path


# ── dataclasses ─────────────────────────────────────────────────────────────
@dataclass
class Room:
    fstype: str
    mountpoint: str
    mounted: bool = False
    detail: str = ''
    entries: int = 0
    structure_hash: str = ''
    top: List[str] = field(default_factory=list)


@dataclass
class Report:
    target: str
    size: int
    sysfs_mounted: bool = False
    sysfs_proc_filesystems_found: bool = False
    sysfs_note: str = ''
    sysfs_fs_dirs: List[str] = field(default_factory=list)      # names under <sysfs mount>/fs (depth 1, AppArmor filtered)
    sysfs_fs_identical_to_host: Optional[bool] = None            # True = the mount shows the host's /sys/fs, not the file
    rooms_source: str = ''
    device_types: List[str] = field(default_factory=list)
    nodev_types: List[str] = field(default_factory=list)
    loadable_types: List[str] = field(default_factory=list)
    skipped_never_mount: List[str] = field(default_factory=list)
    rooms: List[Room] = field(default_factory=list)
    composite: Optional[Room] = None
    leftovers: List[str] = field(default_factory=list)


def run(cmd: List[str], use_sudo: bool, timeout: int = STEP_TIMEOUT) -> Tuple[int, str, str]:
    full = (['sudo', '-n'] if use_sudo and os.geteuid() != 0 else []) + cmd
    try:
        r = subprocess.run(full, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout, r.stderr.strip()
    except subprocess.TimeoutExpired:
        return 124, '', f'timeout after {timeout}s: {" ".join(full)}'


# ── the hallway ─────────────────────────────────────────────────────────────
class HallwayStroll:

    def __init__(self, target: str, work: str, execute: bool, include_nodev: bool = False,
                 sysfs_mount: Optional[str] = None):
        self.file = os.path.abspath(target)
        self.work = guard(os.path.abspath(work))
        self.hall = os.path.join(self.work, 'Hallway')
        self.execute = execute
        self.include_nodev = include_nodev
        self.sysfs_mount = guard(os.path.abspath(sysfs_mount)) if sysfs_mount else None
        self.fstypes: List[str] = []
        self.rep = Report(self.file, os.path.getsize(self.file))
        self._mounted: List[str] = []       # mountpoints we created, for the finally-umount
        self._made: List[str] = []          # directories we created, for rmdir (never rm -rf)

    # step 1 — his sysfs step. Depth-1, name-only reads; never walks, never cd's.
    def sysfs_step(self) -> Optional[str]:
        pre = self.sysfs_mount is not None          # a mount Cody made; we read it and do NOT umount it
        mp = self.sysfs_mount or guard(os.path.join(self.work, '_sysfs'))
        if not pre:
            os.makedirs(mp, exist_ok=True)
            self._made.append(mp)
            if not self.execute:
                self.rep.sysfs_note = f'DRY RUN: would mount -t sysfs -o {MOUNT_OPTS} {self.file} {mp}'
                return None
            rc, _, err = run(['mount', '-t', 'sysfs', '-o', MOUNT_OPTS, self.file, mp], True)
            self.rep.sysfs_mounted = rc == 0
            if rc != 0:
                self.rep.sysfs_note = f'sysfs mount failed: {err}'
                return None
            self._mounted.append(mp)
        else:
            self.rep.sysfs_mounted = True
        try:
            self._sysfs_fs_listing(mp)
            probe = guard(os.path.join(mp, 'proc', 'filesystems'))
            if os.path.isfile(probe):
                rc, out, _ = run(['cat', probe], False, timeout=5)
                self.rep.sysfs_proc_filesystems_found = rc == 0
                self.rep.sysfs_note += ' | proc/filesystems present inside the sysfs mount'
                return out if rc == 0 else None
            self.rep.sysfs_note += (' | no proc/filesystems inside the sysfs mount (sysfs has no proc/ directory)')
            return None
        finally:
            if not pre:
                self._umount(mp)

    def _sysfs_fs_listing(self, mp: str):
        """Names directly under <mp>/fs and the same under the host /sys/fs. Depth 1, names only,
        walled names dropped before anything else sees them."""
        def names(d: str) -> List[str]:
            try:
                return sorted(n for n in os.listdir(guard(d)) if not walled(os.path.join(d, n)))
            except OSError:
                return []
        mine, host = names(os.path.join(mp, 'fs')), names('/sys/fs')
        self.rep.sysfs_fs_dirs = mine
        self.rep.sysfs_fs_identical_to_host = (mine == host) if mine else None
        self.rep.sysfs_note = (f'fs/ lists {len(mine)} names; '
                               + ('IDENTICAL to the host /sys/fs (sysfs ignores the file: this is the kernel view, '
                                  'not the file contents)' if mine and mine == host else
                                  'differs from the host /sys/fs' if mine else 'no fs/ directory'))

    # step 2
    def the_rooms(self, from_sysfs: Optional[str] = None) -> List[str]:
        """Filesystem types from proc/filesystems text; nodev lines are split off (the manual does not
        probe them either)."""
        if from_sysfs:
            text, self.rep.rooms_source = from_sysfs, 'sysfs mount: proc/filesystems'
        else:
            with open('/proc/filesystems') as fh:
                text = fh.read()
            self.rep.rooms_source = '/proc/filesystems (kernel list)'
        dev, nodev = [], []
        for line in text.splitlines():
            parts = line.split()
            if not parts:
                continue
            (nodev if parts[0] == 'nodev' else dev).append(parts[-1])
        # /proc/filesystems lists only LOADED drivers; mount(8) also points at /lib/modules/$(uname -r)/kernel/fs.
        # Add block-backed types from that whitelist whose module directory/file exists (loaded on demand by mount).
        kdir = f'/lib/modules/{os.uname().release}/kernel/fs'
        loadable = []
        for t in PROBE_FIRST:
            m = MODDIR.get(t, t)
            if t not in dev and t not in nodev and (os.path.isdir(os.path.join(kdir, m)) or
                                 any(os.path.exists(os.path.join(kdir, m + ext)) for ext in ('.ko', '.ko.zst', '.ko.xz'))):
                loadable.append(t)
        self.rep.loadable_types = loadable
        dev = dev + loadable
        first = [t for t in PROBE_FIRST if t in dev]
        dev = first + [t for t in dev if t not in first]
        self.rep.device_types = dev
        self.rep.nodev_types = nodev
        self.rep.skipped_never_mount = sorted(set(nodev) & NEVER_MOUNT)
        self.fstypes = dev + ([t for t in nodev if t not in NEVER_MOUNT] if self.include_nodev else [])
        return self.fstypes

    # step 3 + 4
    def the_hallway(self):
        for d in (self.hall, os.path.join(self.hall, 'All')):
            os.makedirs(guard(d), exist_ok=True)
            self._made.append(d)
        self.rep.composite = self._room('All', ','.join(self.fstypes))
        for t in self.fstypes:
            self.rep.rooms.append(self._room(t, t))

    def _room(self, name: str, types: str) -> Room:
        mp = guard(os.path.join(self.hall, name))
        os.makedirs(mp, exist_ok=True)
        if mp not in self._made:
            self._made.append(mp)
        room = Room(name, mp)
        if not self.execute:
            room.detail = f'DRY RUN: mount -t {types} -o {MOUNT_OPTS},loop {self.file} {mp}'
            return room
        rc, _, err = run(['mount', '-t', types, '-o', MOUNT_OPTS + ',loop', self.file, mp], True)
        if rc != 0:
            room.detail = err.splitlines()[-1] if err else f'rc={rc}'
            return room
        self._mounted.append(mp)
        room.mounted = True
        rc, out, _ = run(['findmnt', '-n', '-o', 'FSTYPE,SOURCE', mp], False, timeout=5)
        room.detail = out.strip()
        room.entries, room.structure_hash, room.top = self.structure(mp)
        return room

    def structure(self, mp: str) -> Tuple[int, str, List[str]]:
        """Paths + kinds only, depth-limited, no symlink following, AppArmor names skipped."""
        seen: List[str] = []
        stack = [(mp, 0)]
        while stack and len(seen) < WALK_MAX_ENTRIES:
            d, depth = stack.pop()
            try:
                with os.scandir(guard(d)) as it:
                    for e in sorted(it, key=lambda x: x.name):
                        if walled(e.path):
                            continue
                        rel = os.path.relpath(e.path, mp)
                        kind = 'l' if e.is_symlink() else 'd' if e.is_dir(follow_symlinks=False) else 'f'
                        seen.append(f'{kind}:{rel}')
                        if kind == 'd' and depth + 1 < WALK_MAX_DEPTH:
                            stack.append((e.path, depth + 1))
            except OSError:
                continue
        h = hashlib.sha256('\n'.join(sorted(seen)).encode()).hexdigest()
        return len(seen), h, sorted(seen)[:12]

    def _umount(self, mp: str):
        rc, _, err = run(['umount', mp], True)
        if rc != 0:
            rc2, _, err2 = run(['umount', '-l', mp], True)
            if rc2 != 0:
                self.rep.leftovers.append(f'{mp}: {err} | {err2}')
        if mp in self._mounted:
            self._mounted.remove(mp)

    def close(self):
        for mp in reversed(list(self._mounted)):
            self._umount(mp)
        for d in reversed(self._made):
            try:
                os.rmdir(d)          # empty dirs only; never rm -rf
            except OSError:
                pass
        rc, out, _ = run(['findmnt', '-rn', '-o', 'TARGET'], False, timeout=5)
        for line in out.splitlines():
            if line.startswith(self.work + os.sep):
                self.rep.leftovers.append(f'STILL MOUNTED: {line}')


def selftest() -> int:
    bad = ['/sys/kernel/security/apparmor', '/sys/module/apparmor/parameters', '/etc/apparmor.d/x',
           '/mnt/x/sys/kernel/security/../security/AppArmor', '/proc/self/attr/apparmor/current',
           '/x/AppArmor', '/sys/fs/apparmor']
    good = ['/mnt/x/proc/filesystems', '/home/u/Hallway/ext4', '/sys/kernel/mm']
    for p in bad:
        assert walled(p), p
    for p in good:
        assert not walled(p), p
    try:
        guard('/sys/kernel/security')
    except Wall:
        pass
    else:
        raise AssertionError('guard did not raise')
    print(f'selftest ok: {len(bad)} walled, {len(good)} open')
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description='mount-based hallway walk (dry run unless --execute)')
    ap.add_argument('file', nargs='?')
    ap.add_argument('--work', default='.', help='work dir; Hallway/ is created inside it')
    ap.add_argument('--execute', action='store_true')
    ap.add_argument('--include-nodev-types', action='store_true',
                    help='also try nodev types (their source is ignored; securityfs is still never mounted)')
    ap.add_argument('--sysfs-mount', help='an existing -t sysfs mount of FILE to read (not unmounted by us)')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file or not os.path.isfile(a.file):
        ap.error('FILE must be an existing regular file')
    h = HallwayStroll(a.file, a.work, a.execute, a.include_nodev_types, a.sysfs_mount)
    try:
        text = h.sysfs_step()
        h.the_rooms(text)
        h.the_hallway()
    finally:
        h.close()
    out = os.path.join(h.work, 'hallway_report.json')
    with open(out, 'w') as fh:
        json.dump(asdict(h.rep), fh, indent=2)
    r = h.rep
    print(f'target      {r.target} ({r.size} bytes)')
    print(f'sysfs step  mounted={r.sysfs_mounted} proc/filesystems-inside={r.sysfs_proc_filesystems_found}  {r.sysfs_note}')
    if r.sysfs_fs_dirs:
        print(f'sysfs fs/   {r.sysfs_fs_dirs}  identical_to_host={r.sysfs_fs_identical_to_host}')
    print(f'rooms from  {r.rooms_source}: {len(r.device_types)} device-backed, {len(r.nodev_types)} nodev'
          f' (never mounted: {r.skipped_never_mount})')
    if r.composite:
        print(f'All         mounted={r.composite.mounted}  {r.composite.detail}')
    ok = [x for x in r.rooms if x.mounted]
    print(f'rooms       {len(ok)} of {len(r.rooms)} mounted: {[x.fstype for x in ok]}')
    for x in r.rooms:
        if not a.execute or x.mounted:
            print(f'  {x.fstype:10} {x.detail}')
    if r.leftovers:
        print('LEFTOVERS (act on these):', *r.leftovers, sep='\n  ')
    print('report      ', out)
    return 1 if r.leftovers else 0


if __name__ == '__main__':
    sys.exit(main())
