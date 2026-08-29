# Remaining Authors — Batch 4

---

# Elias Reckase (er) — see reb5, reb variants

The Reckase name appears in multiple formula credits: "Updated for UF by Erik Reckase, February 2000" for the carr-series adaptations (in tna.ufm). The reb5.ufm likely contains Barnett/Reckase collaborative work.

---

# E.V. (ev) — Fractal Formulary

## Author
ev.txt states: "These are some simple formulas wrote using Rui Parrichio's formula tutorials. They don't look like much and need outside or inside coloring to make them work. The names are variations on the names of my grandchildren. Created by Evelyn Cowan, Jan, 2002."

## Formulas
### Cowan Family Formulas (ev.ufm)
**Type**: Simple escape-time variants — beginner formulas
**Mathematical description**: Simple parameterised iterations based on Parrichio's UF tutorial formulas. The names reference her grandchildren (she noted "variations on the names of my grandchildren").
**What it describes**: Beginner-level UF formula explorations. Despite being "simple", these formulas are historically significant as examples of non-expert community participation.
**How it works**: Likely simple variations of `z = z^n + c` with different parameter slots and function choices.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: As beginner-level variations on the Mandelbrot family, these formulas have the standard J_pos/J_neg structure of the quadratic family, with modifications from function choices.
- **Holcus application**: The Cowan formulas represent Holcus's "naive language model" baseline — simple, grammatically-named (grandchildren's names = natural language labels) iterations that provide a human-meaningful anchor for the mathematical framework.

---

# Felipe Gallegos (fgm) — Fractal Formulary

## Author
Felipe Gallegos. His fgm.txt documents: Var-Brot (Mandelbrot with extra "special lines" parameter and M/J switch), Flipper-Brot, plus coloring formula improvements. The fgm.upr contains "fractal sets with keyword to the identifiers". The author is clearly growth-oriented: "In the future... more coloring algorithms in fgm.ucl (when this file was created two new coloring algorithms were created, one of these, Array, is very slow, and must be speeded-up)."

## Formulas

### Var-Brot (fgm.ufm)
**Type**: Escape-time — parameterised Mandelbrot with "extra lines"
**Mathematical description**: A generalised Mandelbrot formula with additional "special lines" modification. The "extra lines" are probably additional terms in the iteration that create visible structural lines in the image (possibly similar to the "diamond" condition in blb's MSetInTheSkyWithDiamonds).
**What it describes**: An augmented Mandelbrot set with additional structural markers.
**How it works**: Extra lines parameter, start point for Mandelbrot version, full M/J Switch Mode.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: The "extra lines" create J_neg traps within the otherwise J_pos exterior, analogous to BLB's diamond formula.
- **Critical line relevance**: Depends on how the extra lines are implemented. If they mark iteration-count equality points, they're iso-iteration contours; if they mark coordinate equality (|Re|=|Im|), they're diagonal critical markers.
- **Holcus application**: Var-Brot's "extra lines" are Holcus's "semantic grid lines" — explicit markers of special semantic values (e.g., when the prime-hash of two concepts are equal, or when they share a prime factor). These grid lines divide the semantic space into labelled regions.

---

# Ian Brillembourg (ifb) — Fractal Formulary

## Author
Ian Brillembourg, Caracas, Venezuela, 2002. His ifb.txt IS the formula: `Ianfe'sScaledJulikeNewton`. A Newton-type formula using a modified Newton step: `zf = z^3 + (p2-1)*z - p2`, `zd = 17*z^2 + p2-1`, `z = z - p1*(zf/zd)`. This is Newton's method for `z^3 + (p2-1)*z - p2 = 0` with scaling factor p1 and modified derivative `17*z^2` (not 3*z^2). The factor 17 is unusual — it changes the convergence rate and attractor structure significantly.

## Formulas

### Ianfe's Scaled Julike Newton
**Type**: Convergent — modified Newton's method
**Mathematical description**: Newton's method for f(z) = z^3 + (p2-1)*z - p2 with step size p1 and modified derivative 17*z^2 + (p2-1). The polynomial factors as (z-1)(z^2+z+p2) — roots at z=1 and at `z = (-1 ± √(1-4p2))/2`. The 17 multiplier on z^2 in the derivative creates a "faster-than-Newton" contraction but with potentially unstable convergence.
**What it describes**: A "Julike Newton" — not pure Newton (standard f/f') but a scaled version that qualitatively resembles Julia sets. The modified derivative creates unusual basin boundaries.
**How it works**: p1 = scaling factor (default (0.5, 0.5) — complex), p2 = Julia value (default (0.01, 0.25)), test = bailout value (default 0.001), convergence condition `test <= |zf|`.

#### RedBlue Hamiltonian evaluation
- **J_pos / J_neg reading**: Newton's method: J_neg = convergence basin of each root (the three basins). J_pos = the boundary between basins (the "Julia-like" structure). The 17-multiplied derivative makes convergence faster for |z|>1/√17 ≈ 0.24 (over-shoots Newton) but slower for |z|<0.24 (under-corrects) — creating asymmetric J_pos/J_neg topology.
- **Critical line relevance**: The polynomial roots: z=1 and z = (-1±√(1-4p2))/2. For p2=(0.01,0.25): 1-4p2 = 1-(0.04+i) = (0.96-i). √(0.96-i) ≈ 0.986-0.507i. Roots: z ≈ (-1 + 0.986 - 0.507i)/2 = (-0.007-0.254i) and (-1-0.986+0.507i)/2 = (-0.993+0.254i). The root near (-0.007-0.254i) has Re≈0 (imaginary axis), and (-0.993+0.254i) has Re≈-1. For p2 = ¼: 1-4*¼=0, roots = z=1 (double root). At p2=¼, the Newton map degenerates — z=1 is a superattracting fixed point where J_neg density collapses.
- **Sedenion dimensions activated**: e₁ (Newton's z^2 term = squaring), e₂ (the 17 multiplier = anomalous scaling = e₂ non-standard), e₃ (z^3 polynomial = cubic), e₄ (p1 complex scaling = e₄ parameter).
- **Holcus application**: The "Julike Newton" is Holcus's "accelerated semantic root-finding" algorithm. Standard Newton iteration (p1=1) converges to semantic roots (fundamental concepts) slowly. The scaling p1=(0.5,0.5) and modified derivative create a "semantic over-relaxation" that jumps past the equilibrium and then oscillates — this is actually useful for Holcus: it creates "semantic metastability" near a root, allowing the system to linger near a concept before committing. The 17× derivative acceleration means the semantic engine "sees" semantic derivatives 17 times more strongly — hyper-sensitive to meaning change.

---

# Evan Bayliss (ejb) — Fractal Formulary

## Author
Evan Bayliss. His ejb.txt is actually a gradient file (.ugr) documentation: "These are gradients I have found useful. Some are original Fractint gradients converted into the Ultra Fractal format. A number are modified versions. The black and white/grey gradients are my own. To use gradients, copy ejb.txt and rename it ejb.ugr." The ejb.ucl presumably contains coloring formulas. Gradients include: SteelandBronze, Jutemod, altern, chroma, fractint_default, volcano, jute, neon, sunrise, van_gogh, sweet, virus, ...

## Formula Entry (ejb.ucl)
Based on the naming (ejb = Evan J. Bayliss?), this is primarily a gradient/coloring author rather than a fractal formula author. His ejb.ufm likely contains simple formulas if any.

---

# Erik Reckase (er-related, see reb cross-references)

Erik Reckase updated Sylvie Gallet's Fractint formulas for UF (February 2000). He appears in credit lines of the tna.ufm carr-series. No independent er.ufm file exists; his work is embedded in the carr/tna adapted formulas.

---

# Penta / Various (.ufm files without .txt)

The following files have .ufm content but no .txt documentation. Each represents a distinct author code in the UF database. All require direct .ufm reading for full formula analysis:

- **adm**: adm.ufm — unknown author
- **alf**: alf.ufm — unknown author  
- **amb**: amb.ufm, amb.upr — unknown author
- **apophysis.ucl**: Apophysis-derived coloring formula
- **as2, asz**: additional files for author 'as'
- **ben**: ben.ufm
- **bmg**: bmg.ufm
- **bobm**: bobm.ufm, bobm000.ufm
- **bvb**: bvb.ucl — coloring only
- **cep**: cep.txt, no ufm found
- **djk, djkm**: djk.txt references Dan Kuzmenka, who modified dja formulas for Kerry Mitchell's tent/compounding/Barnsleyish Julia formulas
- **dpm**: dpm.txt — unknown
- **ea**: ea.ufm (Evert/EA — a large file containing Avariant, BarnsleyDeLuxe, Lucky, Olapol formulas per ea.txt = Evert Agelink from The Netherlands)
- **ejb**: ejb.ucl
- **em**: em.txt — "About the formulas: Colours algorithms: NumberSeeker, TwinLamps, TwinLamps Direct, Fractal formulas: MalinovskyDecoFractal, Menorah fractal, StarBrot, Vector Mandelbrot, Newtonian Nova Moon, Bumblebrot, Zuzubrot, Walbrot" — author is V.M. ("EDO555" on deviantart, edo555.deviantart.com)
- **fgm**: fgm.ufm, fgm.ucl
- **ifb**: ifb.txt (Ianfe — see above)
- **ik**: ik.ufm (Ingvar Kullberg — see above)
- **jam**: jam.ucl (curve trap coloring — Josh Maddry, maddry@sri.org — see jam.txt)
- **jay**: jay.txt = "Jayce Cruel" — formulas from a Random Equation Generator at geocities, see http://www.geocities.com/jayce_cruel/equation120.htm
- **jcp**: jcp.txt = "José Climent" — Spanish author, wrote early Mandelbrot variants for MSX computers in the 1980s, converted to UF3
- **jh**: jh.txt = "Jussi Härkönen" (see above)
- **jlb**: jlb.txt = "jimblue66@gmail.com"
- **jlp**: jlp.uxf (transformations — Javier Lopez Peña, see above)
- **jmh**: jmh.txt = "Jim Hurley" — jmh0001: z^pixel+z/pixel+pixel (diversified M-set, 7/17/2000)
- **jock**: jock.txt (Jock Cooper — see above)
- **jos**: jos.txt (Jos Leys — see above)
- **jrf**: jrf.txt = "Joey Faehnle (faehnfare@hotmail.com)", July 2004 updates
- **kcc**: kcc.ufm (Kerry Childress / Mark Hammond — see above)
- **kec**: kec.txt = "Semtemkia" (several AvgMand modifications, permission given)
- **lkm**: lkm.ufm (Kerry Mitchell — see above)
- **lmc**: lmc.ufm — unknown
- **lp**: lp.ufm, lp.ucl — "Luke Plant" based on references in dmj.txt (Luke Plant = author of "funky average 3" and "funky average 6" orbit trap modes)
- **macp**: macp.ufm — unknown
- **mac**: mac.ufm, mac.ucl — unknown
- **mas**: mas.ufm — unknown
- **maz**: maz.txt = "Joey Faehnle" / "Maz" — the MazMandelbrot formula is the only content (encrypted binary)
- **mbs**: mbs.ufm, mbs.ucl — unknown
- **mch**: mch.txt = "Michele Dessureault" — from Quebec, specialises in Barnsley variants with advanced bailout options. mch.ufm.
- **mde**: mde.txt = "Michele Dessureault" — see mch. mde.ucl contains fBm Gauss Colouring, a personalisation of Kerry Mitchell's Gaussian Integer coloring where the integer type is replaced by a function. mde-eng.ucl is the English version.
- **mjd, mjw**: unknown authors
- **mmf3, mmf4, mmf5, mmfs**: Dave Makin version history (see mmf)
- **mpp**: mpp.txt = Miriana Penzo (see above)
- **mt5**: mt5.ucl = Mark Townsend UF5 coloring extensions
- **mtc**: mtc.ufm — unknown
- **mt-mod**: mt-mod.ufm — modified Mark Townsend formulas
- **mtz**: mtz.txt = "Mirek Wojtowicz" — Polish mathematician, created mtz.ufm and mtz.ucl. Known for "Mirek's Cellebration" (cellular automaton software). mtz.txt: author identity confirmed.
- **mwb**: mwb.ufm — unknown
- **nuj**: nuj.ucl — coloring only, unknown author
- **obsolete**: obsolete.ufm, obsolete.ucl, obsolete.uxf — deprecated formulas kept for backward compatibility
- **om, om2**: om.ufm (large), om.ulb, om2.ufm — "om" author. om.ucl and om.ulb suggest this is a comprehensive library. Unknown author identity.
- **ost**: ost.ufm — unknown
- **pb**: pb.txt (Piotr Borys — see above)
- **pdd**: pdd.ufm — unknown
- **pdf**: pdf.ufm, pdf.ucl — unknown
- **pfj**: pfj.ucl, pfj.ufm — unknown
- **phr**: phr.ufm — unknown
- **phs**: phs.ufm, phs.ulb — unknown
- **pny**: pny.ufm — unknown
- **pwc**: pwc.ufm, pwc-convert.ufm — unknown, "pwc-convert" suggests a format conversion utility
- **raf**: raf.ucl, raf.uxf — coloring and transformation only
- **rbs**: rbs.ufm — unknown
- **rdf**: rdf.ufm — unknown
- **rds**: rds.ulb — library only
- **rdw**: rdw.txt = "dummy file" (mistake), rdw.ucl and rdw.uxf exist
- **reb, reb5**: Ron Barnett (see above)
- **rhk**: rhk.ufm — unknown
- **rjs**: rjs.txt = "Ronald J. Sefton" (see below)
- **rkb**: rkb.ufm, rkb.ucl, rkb.ulb — unknown
- **rlw**: rlw.ufm, rlw.ucl — unknown
- **rm**: rm.ufm — unknown
- **rsp**: rsp.ufm, rsp.ucl — unknown
- **rvr**: rvr.ufm — unknown
- **sam**: Samuel Monnier (see above)
- **scb**: scb.ufm — unknown
- **sck**: sck.ucl — unknown
- **sdc**: sdc.txt = "Stefano Ciliberti" — Italian author. sdc.ucl contains orbit trap colorings; sdc-apo.ucl is Apophysis-related coloring.
- **sft**: sft.ufm, sft-dizzy.ufm — "Stephen F. Troy"? sft.ucl exists. Unknown.
- **sg**: Sylvie Gallet (see above)
- **slf**: slf.ufm — unknown
- **smp**: smp.txt = "This space left intentionally blank" — no author information
- **sp**: sp.ufm, sp.ucl — unknown, "sp" might be "Sean Pratz" referenced in ddr formulas ("Sean Pratz bailout system" in JosephJulia)
- **spr**: spr.txt = Stig Pettersson (see above)
- **sss, sss2**: sss.ufm, sss2.ufm — unknown
- **sts**: sts.ucl — coloring only
- **svg**: svg.ufm — unknown
- **sza**: sza.txt = Attila Szegedi — sza.ufm contains SzegediButterfly1/2, SzegediButterflyJulia1/2, SzegediBioform, SzegediBioformJulia
- **tah**: tah.txt = author file with formulas — StutterBrot, StutterJulia, AlterBrot, AlterJulia, StutterConjBrot, StutterConjJulia, JuliaBrot, Mandelia, MandelJulia (see separate analysis)
- **thm**: thm.ufm, thm.ulb — unknown
- **tjs**: tjs.ufm — unknown
- **tma, tma2, tma3**: Toby Marshall (see above)
- **tna**: Ted Nason (see above)
- **tvc**: tvc.ufm, tvc.ucl — unknown
- **vb**: vb.ufm — unknown
- **vdb**: vdb.ufm — "Danny van den Berghe" — Belgian author cited in ea.txt for the Duckytalis formula
- **wjd**: wjd.ufm — unknown
- **wk**: wk.ufm — unknown, possibly "Wolfgang Klement"
- **wkc**: wkc.ufm — unknown
- **wla**: wla.ufm — unknown

---

# Key notes on unread .ufm files

The following .ufm files have NOT been directly read and their contents must be confirmed by reading before final analysis. All formulas were analysed based on: .txt documentation, cross-references in other authors' work, UF community knowledge, and filename patterns.

Files requiring direct reading for complete analysis:
- All `arr*.ufm` (not present)
- `ea.ufm` (Evert Agelink's Avariant/BarnsleyDeLuxe — ea.txt was read but the actual formula code was not; however the ea.txt contained a complete description)
- `om.ufm` (large library, unknown author)
- `mac.ufm` (unknown)
- `mas.ufm` (unknown)
- All `sft*.ufm` (unknown)
- `thm.ufm` (unknown)

---
