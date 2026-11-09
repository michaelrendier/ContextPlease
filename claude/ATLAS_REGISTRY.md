# ATLAS REGISTRY — which atlas is which  (created 2026-11-09, Cody + Claude)

Rule: every atlas has a unique name of the form "<Space> Atlas", a directory or document that carries that name, and a row here. Never say "the atlas" alone. New atlases get a row the day they are started.

| # | Atlas | What it maps | Where | Form |
|---|---|---|---|---|
| 1 | **Riemann–Fermat Atlas** | the UNS space containing The Two Trees (Telperion/Laurelin) and the ζ pathway: sphere, wheels, springs, extinction flow, nodal ladder, heartbeat, wave, prime pathway, Gemini sims. One part of what 0_RB covers, pointed at one space. | `RiemannHypothesisProof/rhp/atlas_riemann_fermat/` (python package `rhp.atlas_riemann_fermat`; index in its README.md; catalog PDF `RHP_Image_Catalog_2026-11-08.pdf`) | SVG + generator modules |
| 2 | **Box-Kite Atlas** (sedenion) | the 42-vertex, 84-edge glued graph of the seven box-kites, joined only at e₀; chart of addresses, Laplacian spectrum | `ValaQuenta/modules/box_kite/` (functions `atlas`, `atlas_spec`, `glued_graph`, `glued_spectrum`, `chart_of`, `fixed_point_gluing`); wiki `ValaQuenta/wiki/box_kite.md`, `toolbox/28_box_kite.md`; `VAPMIP/docs/wiki/Boxkite-Relational-Atlas.md` (+ `VAPMIP/Broca/docs/` copy) | code + prose (no picture directory) |
| 3 | **Abrikosov Zero-Divisor-Tree Atlas** | the zero-divisor propagation T16…T512, radial tree | `AbrikosovTree/render/atlas_abrikosov_zd_tree/` | PNG |
| 4 | **Abrikosov CD-Tower Lattice Atlas** | the Two Trees on each Cayley–Dickson plane ℝ→𝕊→T₈₁₉₂ (+0b/0c/0d) | `AbrikosovTree/render/atlas_abrikosov_cd_lattice/` | PNG |
| 5 | **Abrikosov CD-Tower UNS Atlas** | the same planes in native (UNS) coordinates | `AbrikosovTree/render/atlas_abrikosov_cd_uns/` | PNG |

Public-API note: ValaQuenta's `atlas*` function names (Box-Kite Atlas) are part of a released GPL API and were NOT renamed; the prose now says "Box-Kite Atlas".
Renames on 2026-11-09: `RiemannHypothesisProof/rhp/atlas` → `rhp/atlas_riemann_fermat`; `AbrikosovTree/render/Arrangement/{ZeroDivisorTree,CDTowerZeroLattice,UNS}` → `render/atlas_abrikosov_{zd_tree,cd_lattice,cd_uns}`.
Documentation still to propagate when each atlas is revisited: Abrikosov generators write into `render/`, not the atlas dirs; Ainulindale wiki and papers that say "atlas" without a qualifier.
