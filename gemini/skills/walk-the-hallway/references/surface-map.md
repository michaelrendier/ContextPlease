# The surface map — node record, states, walls, chunk cycles, outputs

**DESIGN, 2026-10-17 (Cody's intended scope for walk-the-hallway). Not built, except the mounted-image backend.** The examples
marked MEASURED were produced by hand with one listing request per level, Mozilla user agent, on public endpoints.

## 1. Vocabulary

| word | meaning |
|---|---|
| **hall** | anything that can list its children |
| **node** | one entry in a hall: a `dir` (hall), a `container` (a file that is also a hall), or a `leaf` |
| **backend** | the code that knows how one kind of hall lists and presents itself |
| **frontier** | nodes known but not yet listed (`unlisted`) |
| **cycle** | one bounded batch of listings (budget of requests, bytes, seconds), then a checkpoint |
| **door** | a closed entrance (a wall) recorded in the map and never opened |

## 2. The node record (draft)

```
id            stable hash of canonical url + path
parent        id of the hall that listed it
name, kind    dir | container | leaf
protocol      mount | s3 | ftp | http | api | tap | fits | tar | zip | hdf5 | sqlite | ...
url           how to reach it
state         listed | unlisted | truncated | walled | unreachable | error | skipped
n_children    integer, or ">=N" when truncated
continuation  marker/token to resume a truncated listing (S3 start-after, API cursor, offset)
size, mtime   when the hall reports them
type_guess    {mime, magic_hex, how: "range-read magic" | "extension" | "container-index" | "unknown", entropy?}
cost          {requests, bytes, seconds} of the listing that produced it
wall          {kind: apparmor|robots|auth|paywall|tos|rate|budget, evidence}   (state == walled)
first_seen, last_seen, evidence_ids
```

States are distinct on purpose: **`unreachable` is not `absent`** (three registries and one archive did not answer from this
machine on 2026-10-17), and `walled` is not `empty`.

## 3. Backends: how each hall lists and presents itself

| backend | one level costs | what it shows | status |
|---|---|---|---|
| **mount protocol family**: local image (loop), or remote public NFS / CIFS-SMB / WebDAV / SSHFS / FTP / S3 via `mount -t TYPE` | `scandir` after the mount | names, kinds, sizes; depth-capped, symlinks not followed, wall-checked | local image **built** (`hallway_mount.py`); remote mounts **designed** (tools available here: `mount.cifs`, `smbclient`, `sshfs`; absent: `mount.nfs`, `showmount`, `davfs2`, `curlftpfs`, `rclone`, `s3fs`) |
| object store (S3) | one `list-type=2&delimiter=/&prefix=` request | `CommonPrefixes` (subdirs) and `Contents` (files); 1 000 per page; `IsTruncated` + continuation | MEASURED |
| FTP | one anonymous `LIST` | names and kinds | MEASURED (one of five hosts answered) |
| HTTP index / `sitemap.xml` / robots `Sitemap:` | one GET, parsed | links; sitemap URL lists | designed |
| REST/JSON API | one page request | items, cursor, total | MEASURED for MAST `Caom.Products` (92 products for one exposure) |
| TAP | VOSI `tables`, then an ObsCore `GROUP BY` | schemas → tables → columns; counts by collection/instrument/format | MEASURED (census of Q2237: HST by instrument, level, size) |
| FITS | header walk by range reads | the HDUs: extension names, shapes, data offsets | MEASURED (17 HDUs, 21 requests, 241 920 bytes for one 168 MB file) |
| tar / zip / HDF5 / SQLite / Parquet / CASA table | index read (member table, superblock, schema, footer) | members, groups, tables, row groups | designed |
| unknown | 2–512 magic bytes by range read | `leaf` with magic, size, entropy | designed; `scan_offsets.py` is the deep fallback |
| plug-in slot | — | rsync module lists, OPeNDAP/THREDDS, WebDAV/VOSpace, NFS/SMB; Gopher/telnet are slots that are dead in practice | open |

### MEASURED example: three levels of `s3://stpubdata`, one request each

```
stpubdata/                       11 subdirs   gaia/ galex/ hst/ jwst/ k2/ kepler/ mast/ panstarrs/ roman/ sdss/ tess/
 └ hst/                           2 subdirs   grizli-v1/  public/
    └ hst/public/              >=1000 subdirs (TRUNCATED; continuation recorded)   cg14/ e140/ e230/ f05i/ f05j/ f05l/ ...
                                              (4-character prefixes = the first four characters of the exposure name)
```

The walker learns the **sharding scheme** from the sample (`<first 4 chars>/<rootname>/<file>`) and stops; it does not enumerate
the thousand. That scheme is exactly what the crawl plan needs. A second bucket, `nasa-heasarc`, listed ≥29 mission prefixes
including `chandra/`. `ftp.eso.org` answered with eight entries (`archive ftp hpux main_ftp_site midaspub users uves Astro-Linux`).

## 4. Walls (generalising the AppArmor rule)

`apparmor` (absolute, string-level) · `robots` (disallowed for the agent) · `auth` (login page) · `paywall` (stop) · `tos` (stop) ·
`rate` (429/503/`Retry-After`: defer) · `budget` (cycle or host budget spent). A wall records the evidence (the robots line, the
status code) and the node stays closed until a human lifts it. On 2026-10-17, for a generic agent: `mast.stsci.edu` was
`walled:robots` (`Disallow: /`), HEASARC's `/xamin` and `/vo/` were `walled:robots`, ESO carried `Crawl-delay: 333.333` (a budget
wall in practice), ALMA and CADC were open.

## 5. Chunk cycles and threaded hopping

```
cycle:
  pick unlisted nodes breadth-first, round-robin across hosts
  per host: at most max_concurrent_per_host requests in flight, honouring Crawl-delay / Retry-After
  list each node ONE level; write children as unlisted; write walls and costs
  stop when the cycle budget (requests, bytes, seconds) is spent
  checkpoint the sitemap atomically; release the workers
```

* **Resumable:** the state is the sitemap itself (nodes + frontier + continuations). A killed run resumes at the next cycle.
* **Threads help across hosts, not within one:** measured on one link, 8 parallel 1 MiB reads gave 4.6 MB/s against 4.9 MB/s
  for one stream; latency (0.49 s per request) overlaps, bandwidth does not add. Listings are latency-bound, so threads across
  hosts and across independent halls are the win.
* **Divisible:** cycles can be spread over days, or handed to several workers/machines, because each cycle only needs the
  frontier and the budget.

## 6. Outputs

* `sitemap.json`: metadata (root, started, cycles run, budgets, walls) + node table + frontier + **structure hash**.
* `tree.txt`: a `tree`-style view with counts, truncation marks and walls.
* `sitemap.xml`: optional, sitemaps.org-compatible, leaves only.
* `crawl_plan.json`, derived from the map: where the leaves of interest live; naming and sharding patterns; per-host
  protocol, robots verdict and cost per request; estimated bytes; a suggested order; the doors that need a human.
* Re-walks diff the **structure hash** to flag drift.

## 7. The coin-image example, end to end (Cody's illustration)

1. Point the hallway at the collection's landing URL; read `robots.txt` first; record walls.
2. Walk breadth-first: landing page → listing pages / API → image directories; one level per expansion, cycles of N requests.
3. Learn the layout: where the images are, the path pattern, the shard size, extensions and magic bytes (JPEG/PNG/TIFF), sizes.
4. Write `sitemap.json` + `tree.txt` + `crawl_plan.json`.
5. The crawler reads `crawl_plan.json` and fetches only what the map says, in the order and at the rate it says.

## 8. Relationship to PTorrent

The Yellow Pages (the PTorrent phonebook) entry for a dataset can be seeded from a sitemap; an `in_situ.ptorrent` manual page can cite
it. The existing core supplies the robots cache, per-host scheduler and HTTP client; the hallway adds the level-at-a-time walker
and the common map, as a new module beside them.
