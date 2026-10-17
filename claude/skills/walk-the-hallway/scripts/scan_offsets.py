#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Michael Rendier'
# scan_offsets.py FILE — the rung after hallway_mount.py finds nothing at offset 0.
# Read-only signature scan: where inside FILE do filesystem / firmware-volume headers sit?
# Each hit gives the `offset=` to pass to `mount -o loop,offset=N,sizelimit=M` (mount(8) LOOP-DEVICE SUPPORT).
# No mounting, no AppArmor paths, nothing written.
import sys, os, json

# (label, signature, offset-of-signature-inside-the-structure)
SIGS = [
    ('squashfs LE',        b'hsqs',                 0),
    ('squashfs BE',        b'sqsh',                 0),
    ('cramfs',             b'\x45\x3d\xcd\x28',     0),
    ('romfs',              b'-rom1fs-',             0),
    ('iso9660',            b'CD001',                1),      # volume descriptor at 0x8000 on disc images
    ('ext2/3/4 superblock',b'\x53\xef',           0x38),     # s_magic at +0x38 of the superblock (sb at +1024)
    ('NTFS',               b'NTFS    ',             3),
    ('exFAT',              b'EXFAT   ',             3),
    ('GPT header',         b'EFI PART',             0),
    ('UEFI firmware volume (_FVH)', b'_FVH',       40),      # EFI_FIRMWARE_VOLUME_HEADER.Signature at +40
    ('FFS2 volume GUID',   bytes.fromhex('78e58c8c3d8a1c4f9935896185c32dd3'), 0),
    ('FFS3 volume GUID',   bytes.fromhex('7ac07354cb3dca4dbd6f1e9689e7349a'), 0),
    ('AMI Aptio capsule GUID', bytes.fromhex('8ba63c4a2377fb48803d578cc1fec44d'), 0),
    ('UEFI capsule GUID',  bytes.fromhex('bd86663b760d3040b70eb5519e2fc5a0'), 0),
    ('gzip',               b'\x1f\x8b\x08',         0),
    ('xz',                 b'\xfd7zXZ\x00',         0),
    ('LZMA(alone) props',  b'\x5d\x00\x00',         0),
]

def main(path):
    data = open(path, 'rb').read()
    hits = []
    for label, sig, inner in SIGS:
        i = 0
        while True:
            j = data.find(sig, i)
            if j < 0:
                break
            hits.append({'label': label, 'offset': max(0, j - inner), 'found_at': j})
            i = j + 1
            if len([h for h in hits if h['label'] == label]) >= 200:
                break
    hits.sort(key=lambda h: h['offset'])
    summary = {}
    for h in hits:
        summary.setdefault(h['label'], []).append(h['offset'])
    out = {'file': path, 'size': len(data), 'summary': {k: {'count': len(v), 'first_offsets': v[:8]} for k, v in summary.items()}}
    print(json.dumps(out, indent=1))

if __name__ == '__main__':
    main(sys.argv[1])
