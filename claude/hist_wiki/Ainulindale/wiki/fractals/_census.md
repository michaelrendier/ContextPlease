# UFformulary census — measured, 2026-11-13

Built by reading the 213 `.ufm` files in `PtolemyDesktop/Archimedes/Maths/Formula/UFformulary/`. A **formula block** is a column-0 line `Name {` (optionally with a parameter list or comment after the brace) that is not a `comment {` block; `.ufm` is the Ultra Fractal formula format, in which each formula is one such block. Author code = the file stem with its trailing digits, `_s` suffix and `-`/`+` extension removed (so `carr0900`…`carr3500` and `carr0900_s` are one code `carr`; `djk+akl` counts under `djk`).

**Listing 1 — the census** (python3 standard library; runs cold)

```python
import re, glob, collections, os
src = 'PtolemyDesktop/Archimedes/Maths/Formula/UFformulary'
files = collections.defaultdict(list); blocks = collections.Counter(); comments = 0
for f in sorted(glob.glob(src + '/*.ufm')):
    b = os.path.basename(f); stem = re.split(r'[-+]', re.sub(r'\d*(_s)?$', '', b[:-4]))[0]
    text = open(f, errors='replace').read()
    names = [m.group(1).strip().lower() for m in re.finditer(r'^([^\s;{}][^\n{};]*)\{\s*(?:;.*)?$', text, re.M)]
    n = sum(1 for x in names if not x.startswith('comment')); comments += len(names) - n
    files[stem].append(b); blocks[stem] += n
print(sum(len(v) for v in files.values()), 'files;', len(files), 'author codes;', sum(blocks.values()), 'formula blocks;', comments, 'comment blocks')
```

```
213 files; 153 author codes; 11523 formula blocks; 117 comment blocks
```

**Correction kept.** [index.md](index.md) (written when only part of the formulary had been read) gave "~95 author codes" and "approximately 1,500–2,000 formulas across 213 files". Measured: **153 codes and 11,523 formula blocks.** The 213-file count was right; the formula count was low by a factor of about six, because the large catalogues (`om`, `om2`, `jam`, `vdb`, `jrf`, `reb`, the 31 `carr` files with 3,627 blocks) were not counted. `.ucl` (108), `.ulb` (24), `.upr` (39), `.uxf` (57), `.txt` (63) and one `.ufc` companion file are not counted here; only the 213 `.ufm` files are.

| Code | Files | Formula blocks | Files (first four) |
|------|------:|---------------:|---------------------|
| carr | 37 | 3627 | carr0900.ufm, carr0900_s.ufm, carr1000.ufm, carr1000_s.ufm … |
| om | 2 | 2087 | om.ufm, om2.ufm |
| jam | 4 | 560 | jam-newton.ufm, jam.ufm, jam2.ufm, jam3.ufm |
| vdb | 1 | 294 | vdb.ufm |
| sss | 2 | 253 | sss.ufm, sss2.ufm |
| jrf | 1 | 225 | jrf.ufm |
| tma | 3 | 203 | tma.ufm, tma2.ufm, tma3.ufm |
| reb | 2 | 202 | reb.ufm, reb5.ufm |
| as | 2 | 189 | as.ufm, as2.ufm |
| rjs | 1 | 187 | rjs.ufm |
| pwc | 2 | 184 | pwc-convert.ufm, pwc.ufm |
| gfp | 1 | 158 | gfp.ufm |
| gnd | 1 | 146 | gnd.ufm |
| bobm | 2 | 111 | bobm.ufm, bobm000.ufm |
| kec | 1 | 104 | kec.ufm |
| mpp | 1 | 104 | mpp.ufm |
| tvc | 1 | 103 | tvc.ufm |
| mt | 2 | 89 | mt-mod.ufm, mt.ufm |
| tna | 1 | 88 | tna.ufm |
| rsp | 1 | 82 | rsp.ufm |
| gwfa | 2 | 79 | gwfa-matrix.ufm, gwfa.ufm |
| dmj | 3 | 78 | dmj.ufm, dmj3.ufm, dmj5.ufm |
| lkm | 3 | 78 | lkm-special.ufm, lkm.ufm, lkm3.ufm |
| anv | 1 | 77 | anv.ufm |
| kpk | 2 | 76 | kpk+akl.ufm, kpk.ufm |
| mac | 1 | 71 | mac.ufm |
| dac | 1 | 69 | dac.ufm |
| ejb | 1 | 68 | ejb.ufm |
| akl | 1 | 65 | akl.ufm |
| rlw | 1 | 63 | rlw.ufm |
| mmf | 4 | 62 | mmf.ufm, mmf3.ufm, mmf4.ufm, mmf5.ufm |
| sam | 1 | 62 | sam.ufm |
| blb | 1 | 58 | blb.ufm |
| jcp | 1 | 53 | jcp.ufm |
| dan | 1 | 50 | dan.ufm |
| em | 1 | 50 | em.ufm |
| jaw | 1 | 50 | jaw.ufm |
| sp | 1 | 49 | sp.ufm |
| bwp | 1 | 48 | bwp.ufm |
| ik | 1 | 48 | ik.ufm |
| mch | 1 | 48 | mch.ufm |
| obsolete | 1 | 45 | obsolete.ufm |
| sdc | 1 | 43 | sdc.ufm |
| bje | 1 | 42 | bje.ufm |
| lal | 1 | 39 | lal.ufm |
| amm | 1 | 38 | amm.ufm |
| aho | 1 | 35 | aho.ufm |
| pdf | 1 | 35 | pdf.ufm |
| jock | 1 | 33 | jock.ufm |
| wkc | 1 | 33 | wkc.ufm |
| eew | 1 | 31 | eew.ufm |
| ben | 1 | 29 | ben.ufm |
| mde | 2 | 28 | mde.ufm, mde3.ufm |
| jay | 1 | 25 | jay.ufm |
| ea | 1 | 24 | ea.ufm |
| lgn | 1 | 24 | lgn.ufm |
| macp | 1 | 24 | macp.ufm |
| ddr | 1 | 23 | ddr.ufm |
| dpb | 1 | 23 | dpb.ufm |
| mjd | 1 | 22 | mjd.ufm |
| alt | 1 | 21 | alt.ufm |
| enr | 1 | 20 | enr-convert.ufm |
| lmc | 1 | 20 | lmc.ufm |
| fhq | 1 | 19 | fhq.ufm |
| phs | 1 | 18 | phs.ufm |
| dav | 1 | 17 | dav.ufm |
| ev | 1 | 17 | ev.ufm |
| djk | 2 | 16 | djk+akl.ufm, djk.ufm |
| jlb | 1 | 16 | jlb.ufm |
| spr | 1 | 16 | spr.ufm |
| anon | 1 | 15 | anon.ufm |
| fgm | 1 | 15 | fgm.ufm |
| sg | 1 | 15 | sg.ufm |
| ahm | 1 | 14 | ahm.ufm |
| gmc | 1 | 14 | gmc.ufm |
| jbo | 1 | 14 | jbo.ufm |
| jh | 1 | 14 | jh.ufm |
| wla | 1 | 12 | wla.ufm |
| dpm | 1 | 11 | dpm.ufm |
| ks | 1 | 11 | ks.ufm |
| rvr | 1 | 11 | rvr.ufm |
| sft | 2 | 11 | sft-dizzy.ufm, sft.ufm |
| mwb | 1 | 10 | mwb.ufm |
| wjd | 1 | 10 | wjd.ufm |
| cep | 1 | 9 | cep.ufm |
| fa | 1 | 9 | fa.ufm |
| hth | 1 | 9 | hth.ufm |
| tah | 1 | 9 | tah.ufm |
| ads | 1 | 8 | ads.ufm |
| drd | 1 | 8 | drd.ufm |
| esa | 1 | 8 | esa.ufm |
| fwp | 1 | 8 | fwp.ufm |
| mjw | 1 | 8 | mjw.ufm |
| mmfs | 1 | 8 | mmfs.ufm |
| mtc | 1 | 8 | mtc.ufm |
| thm | 1 | 8 | thm.ufm |
| asz | 1 | 7 | asz.ufm |
| djw | 1 | 7 | djw.ufm |
| jgr | 1 | 7 | jgr.ufm |
| jos | 1 | 7 | jos.ufm |
| lp | 1 | 7 | lp.ufm |
| pdd | 1 | 7 | pdd.ufm |
| svg | 1 | 7 | svg.ufm |
| adm | 1 | 6 | adm.ufm |
| lgr | 1 | 6 | lgr.ufm |
| sza | 1 | 6 | sza.ufm |
| ck | 1 | 5 | ck.ufm |
| ifb | 1 | 5 | ifb.ufm |
| ldm | 1 | 5 | ldm.ufm |
| slf | 1 | 5 | slf.ufm |
| cy | 1 | 4 | cy.ufm |
| fracmod | 1 | 4 | fracmod.ufm |
| maz | 1 | 4 | maz.ufm |
| mbs | 1 | 4 | mbs.ufm |
| rbs | 1 | 4 | rbs.ufm |
| rdf | 1 | 4 | rdf.ufm |
| jwx | 1 | 3 | jwx.ufm |
| kto | 1 | 3 | kto.ufm |
| la | 1 | 3 | la.ufm |
| ost | 1 | 3 | ost.ufm |
| smp | 1 | 3 | smp.ufm |
| amb | 1 | 2 | amb.ufm |
| amc | 1 | 2 | amc.ufm |
| bmg | 1 | 2 | bmg.ufm |
| cdj | 1 | 2 | cdj.ufm |
| hjk | 1 | 2 | hjk.ufm |
| jjd | 1 | 2 | jjd.ufm |
| jml | 1 | 2 | jml.ufm |
| jvx | 1 | 2 | jvx.ufm |
| mtz | 1 | 2 | mtz.ufm |
| pb | 1 | 2 | pb.ufm |
| pfj | 1 | 2 | pfj.ufm |
| pny | 1 | 2 | pny.ufm |
| rm | 1 | 2 | rm.ufm |
| scb | 1 | 2 | scb.ufm |
| abs | 1 | 1 | abs.ufm |
| alf | 1 | 1 | alf.ufm |
| ar | 1 | 1 | ar.ufm |
| daz | 1 | 1 | daz.ufm |
| des | 1 | 1 | des.ufm |
| evc | 1 | 1 | evc.ufm |
| gbd | 1 | 1 | gbd.ufm |
| jmh | 1 | 1 | jmh.ufm |
| jmk | 1 | 1 | jmk.ufm |
| jp | 1 | 1 | jp.ufm |
| kr | 1 | 1 | kr.ufm |
| mas | 1 | 1 | mas.ufm |
| phr | 1 | 1 | phr.ufm |
| rhk | 1 | 1 | rhk.ufm |
| rkb | 1 | 1 | rkb.ufm |
| tjs | 1 | 1 | tjs.ufm |
| vb | 1 | 1 | vb.ufm |
| wk | 1 | 1 | wk.ufm |


## Where the per-author estimates of [index.md](index.md) differ from the measurement by more than a factor of three

The index table's "# Formulas (approx.)" column was written from partial reading. Measured counts of `.ufm` blocks for the same code are below; a measured 0 means the code has **no `.ufm` file** in the formulary (the work is in `.ucl`/`.ulb`/`.upr`/`.uxf`/`.txt` files, which this census does not count). The index estimates are kept in place; where they differ, this table is the measurement.

| Code | Index estimate | Measured `.ufm` blocks |
|---|---|---:|
| akl | 20+ | 65 |
| alt | 5+ | 21 |
| amm | 10+ | 38 |
| bar | 3 | 0 |
| carr | 200+ (in ~40 files) | 3627 |
| dja | 9 | 0 |
| em | 10+ | 50 |
| ev | 5? | 17 |
| fgm | 5+ | 15 |
| ifb | 1 | 5 |
| ik | 15+ | 48 |
| jam | 8 coloring | 560 |
| jay | 5? | 25 |
| jcp | 12 | 53 |
| jlp | 4 transformations | 0 |
| jrf | 15+ | 225 |
| kcc | 40+ | 0 |
| maz | 1 (encrypted) | 4 |
| mch | 15+ | 48 |
| mpp | 30+ | 104 |
| pb | 6 | 2 |
| pwc | 2 | 184 |
| reb | 30+ | 202 |
| rjs | 60+ | 187 |
| sft | 2+ | 11 |
| vdb | 1+ | 294 |
