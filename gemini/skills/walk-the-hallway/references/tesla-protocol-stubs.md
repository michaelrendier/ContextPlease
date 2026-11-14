# Protocols for the hallway — stubbed against Tesla (PtolemyDesktop)

**2026-10-17 (Cody): the hallway is tied into Tesla.** Tesla supplies the protocols; the hallway (Phaleron's `WalkTheHalls`) walks
them. Only what **Huchra's Lens** needs is built; everything else is a documented stub for later engineering. This page is
documentation: **nothing in `PtolemyDesktop/` has been created or changed.**

## 1. What Tesla already is (read 2026-10-17, `PtolemyDesktop/Tesla/`)

* Face docstring: *"Tesla — All interfacing for Ptolemy. Networking, device I/O, remote control, sockets."* (README: "physical
  world, sensor streams, hardware state, device I/O").
* Existing modules: `HolePunch` (`HolePunch`, `HolePunchRelay`, threads), `Sockets` (`SocketThread`, `Sockets`), `KVM` (`KVMServer`/client),
  `SensorStream` (`SensorStream`, `SensorReceiveThread`, `SensorRecorder`, per-device state), `PtolSense`, `IPZSP`/`Zork_Sentence_Parser`.
* **Conventions to follow, not invent:** `QObject` classes emitting signals; `QThread` workers with `run()`/`stop()`; `attach_bus(bus)` and
  `_publish_to_bus(packet, id)` to publish on PtolBus (`Pharos/PtolBus.py`: `BusMessage(channel, payload, priority…)`); `settings/settings.json`
  with `{module, face, display, version, settings:{key:{value,type,label,stub}}}`; **`"stub": true` marks a planned, unbuilt setting**
  (today `gps_enabled`, `sensor_stream_hz`); source markers `# TODO:BUILD`, `# TODO:SETTINGS`.
* Gaps seen: `Tesla/__init__.py` has its imports commented out; no `Tesla/settings` entry for any HTTP, S3, TAP or FTP client; no
  generic protocol interface, only per-feature classes.

## 2. The split

| piece | where | does |
|---|---|---|
| the walker, node table, sitemap, chunk cycles, crawl plan | `PtolemyDesktop/Phaleron/WalkTheHalls/` (extends the existing `WalkTheHalls.py`) | decides what to list next; knows nothing about wire formats |
| protocol handlers | `PtolemyDesktop/Tesla/Protocols/` (**proposed, not created**) | one class per protocol: how that kind of hall lists, reads and identifies itself |
| container readers (FITS, tar, …) | Phaleron, over any handler's `read()` | a file becomes a hall |
| walls and robots verdicts | the PTorrent core's `RobotsCache` (`ptorrent_core/net.py`) reused, plus the AppArmor string test | closed doors are recorded, never opened |
| results to the rest of Ptolemy | PtolBus channel `hallway.sitemap` (proposed) | other Faces and the console UI subscribe |

## 3. The interface (stub, in Tesla's idiom)

```python
class Protocol(QObject):                       # Tesla/Protocols/base.py   (PROPOSED)
    name = ""            # "https", "s3", "tap", "mount", "ftp", ...
    schemes = ()         # URL schemes it answers to
    stub = True          # mirrors settings.json "stub"; False once built
    # signals: listed(node_id, children), read_done(node_id, nbytes), wall(node_id, kind, evidence), failed(node_id, why)

    def wall(self, url) -> "Wall | None":      # robots/auth/paywall/apparmor verdict BEFORE any request
    def list(self, node, cursor=None):          # one level only -> (children, continuation|None, cost)
    def read(self, node, start, length):        # bounded bytes into memory (the read-in-place primitive) -> (bytes, cost)
    def identify(self, node) -> dict:           # magic-byte type guess via a tiny read() -> {mime, magic_hex, how}
    def close(self): ...
```

* `cost` = `{requests, bytes, seconds}`, summed per source into the sitemap and into the In Situ tab's detail box.
* One `QThread` per host (politeness: `max_concurrent_per_host`); parallel across hosts. A cycle's budget stops the batch.
* Each protocol gets a `settings.json` key, e.g. `proto_s3: {value: true, type: bool, label: "S3 listing", stub: false}`, plus
  `proto_s3_budget_requests`. A stub protocol is `stub: true` and raises `NotImplementedError` with a pointer to this page.

## 4. Build set for Huchra's Lens (and nothing else)

The smallest set that lets the hallway map the Q2237 surface and the in situ read work, **HST first** (per-exposure dithered frames are
what ptychography needs; MAST's own endpoints are `walled:robots` for a generic agent, so the compliant route is S3 + a one-off catalogue):

| # | piece | why Q2237 needs it | state |
|---|---|---|---|
| B1 | **walls**: AppArmor string test + the core's robots cache | policy before every request | reuse |
| B2 | **`https`**: `HEAD`, `GET`, `Range`; `RangeFile` (block cache, coalescing at the ≈2.4 MB gap rule, bytes/requests counters) | the read-in-place primitive | probe exists (`insitu_probe.py`) |
| B3 | **`s3`**: `list-type=2&delimiter=/&prefix=&continuation-token=` over HTTPS | lists `hst/public/<rootname[:4]>/<rootname>/` and `nasa-heasarc/chandra/…` without MAST's walled API | measured by hand, 3 levels |
| B4 | **`fits` container reader** over `read()` | HDU walk (17 HDUs in 21 requests) and cutout block reads | probe exists |
| B5 | **walker core**: node table, frontier, one-level expansion, truncation + continuation, sitemap.json + tree.txt, chunk-cycle checkpoint | the map itself | designed |
| B6 | **crawl-plan writer** for this one dataset | tells the in situ evaluator which frames, which byte ranges, which order | designed |
| (opt) | **`tap`**: VOSI `tables` + ADQL sync + VOTable (TABLEDATA and BINARY) / CSV | needed only for ALMA and ESO (their robots allow it); MAST and HEASARC TAP are walled | probes exist (`vot.py`, `votb.py`) |

ESO frames (small, often compressed, 333 s crawl-delay) and ALMA (measurement sets) are **not** in the first build set.

## 5. Stubs: documented for later engineering (`stub: true`, not built)

| protocol id | scheme / door | lists with | reads with | tools on this machine (2026-10-17) | notes |
|---|---|---|---|---|---|
| `mount_local` | `mount -t TYPE -o loop FILE MP` | `scandir` | file reads | `hallway_mount.py` **built** | not yet wired into Tesla; the script is backend 1 |
| `mount_nfs` | `mount -t nfs HOST:/export` | `scandir` | file reads | kernel module yes; `mount.nfs`, `showmount` **no** | discover exports with `showmount -e` |
| `mount_cifs` | `mount -t cifs //HOST/SHARE -o guest` | `scandir`; `smbclient -L //HOST -N` first | file reads | `mount.cifs`, `smbclient` **yes** | anonymous only |
| `mount_sshfs` | `mount -t fuse.sshfs USER@HOST:/path` | `scandir` | file reads | `sshfs` **yes** | needs an account; public only if a guest is offered |
| `mount_davfs` | WebDAV via `davfs2` | `PROPFIND` | file reads | **no** | VOSpace is WebDAV-like |
| `mount_ftpfs` | FTP via `curlftpfs` | `LIST` | file reads | **no** (`curl` lists FTP) | |
| `mount_s3fs` / `rclone` | object store as a mount | not needed: `s3` lists directly | — | **no** | |
| `ftp` | `ftp://` anonymous | `LIST` / `NLST` (`curl --list-only`) | `REST` offsets | `curl` yes; **only `ftp.eso.org` answered** | |
| `http_index` | Apache/nginx autoindex, `sitemap.xml`, robots `Sitemap:` | parse HTML/XML | `https` | stdlib | |
| `rest_api` | JSON with page/cursor | page request | — | stdlib | MAST `Caom.Products`, Zenodo, HF, Kaggle shapes |
| `datalink`, `soda` | IVOA DataLink / server-side cutout | links table | cutout URL | none advertised by the five TAP services | would give true server-side cutouts |
| `sia`, `ssa`, `scs` | IVOA image/spectrum/cone search | VOTable | — | not probed | |
| `opendap`, `thredds` | `.dds` / `catalog.xml` | catalog XML | ranged slices | not probed | |
| `rsync` | `rsync://HOST/` module list | `rsync HOST::` | `--list-only` | `rsync` **yes** | |
| `ninep`, `ceph`, `afs`, `coda` | kernel mounts | `scandir` | file reads | modules present, no servers named | |
| `gopher`, `telnet` | slots only | — | — | — | dead in practice; the slot exists so the map can say "none found" |
| container: `tar`, `zip`, `hdf5`, `sqlite`, `parquet`, `casa_ms`, `gzip/.Z` | file-as-hall | member/group/table/row-group index | ranged reads where seekable | python stdlib for tar/zip/sqlite | gzip and `.Z` streams are not seekable: whole-object |
| `science_platform` | Fornax Science Console, CANFAR | — | code runs beside the data | not accessible from here | per search results; ESA Datalabs and Astro Data Lab unverified |

**Classifier gap (for the mount family):** `/proc/filesystems` marks NFS, CIFS and FUSE `nodev`; the current script skips `nodev`
types because sysfs/proc-style types ignore the source. Network/FUSE types are `nodev` yet the source matters. When the mount
protocols are built the classifier must split *pseudo* (source ignored) from *network/FUSE* (source meaningful).

## 6. Open for Cody

1. Create `Tesla/Protocols/` (base + the four build-set classes + stub files + `settings.json` keys) now, or keep this as documentation until the Q2237 build starts?
2. The proposed PtolBus channel `hallway.sitemap` and the In Situ tab as its subscriber.
3. HST first, with `tap` deferred (MAST TAP is walled): agreed?
