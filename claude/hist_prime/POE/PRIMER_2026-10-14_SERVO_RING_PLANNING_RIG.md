# POE primer — the free-standing point of light: servo-ring planning rig (2026-10-14)

*For a cold session. Everything here is in the POE repo (commit bd58717 on main) or ContextPlease. Nothing is built or measured; this is a concept and planning rig.*

## What it is (the author's design, fixed constraints)
A ring of independent arms, each carrying a weak deep-red laser beam, aimed so all beams pass through one point and arrive **in phase** there (constructive interference
at the focal point is the one fixed requirement). The point can be moved in 3D by re-aiming and re-phasing every arm; the intended use is a naked-eye point of light
projected from the P.O.E. pendant (the Altered Carbon season-2 Edgar Allan Poe AI pendant is the model for the pendant). The macro-scale ring is the prototype to build
from and against, to be handed to integrated-circuit and nanotech engineers (University of Washington is a ten-minute walk from the author's new apartment) to miniaturise.
No scattering medium is part of the design; a haze ("pea-soup fog") scatter volume is used only for testing and monitoring the focal point.

## Where things are
| What | Path |
|---|---|
| Concept page (design, constraints, open questions) | `POE/pendant/optics/FREE_STANDING_POINT_OF_LIGHT.md` |
| Narrative 3D mock-up, Blender 4.x python3 (13 arms, animation, safety check, previews; isometric PNG on the Desktop in SpaceClaude) | `POE/pendant/cad/blender/poe_servo_ring.py` |
| Full-scale planning rig, OpenSCAD (wall-mounted, N = 13 or 18, working volume to ~4 ft) | `POE/pendant/cad/scad/` (`poe_servo_ring.scad`, `design_calc.py`, `README.md`, `render.sh`, PNGs) |
| Copper pancake coil guide + calculator | `POE/radio/pancake_coil/COIL_PRODUCTION.md`, `coil_design.py` |
| Beam-geometry numbers (plane-wave interference, scattering estimate) | `ContextPlease/claude/scratchpad/2026-10-14_poe_servo_ring/` |
| Earlier primers | `hist_prime/POE/hardware_primer.md`, `architecture_primer.md` |

## The rig as drafted (OpenSCAD)
Ring of 1/2 in steel round parallel to a wall; beams go into the room. Each arm: coarse pan servo (axis along the ring normal) + coarse tilt servo + lens tube with a fixed 25.4 mm lens
+ a 3-axis fibre-tip positioner behind it (fine steering by lateral fibre shift, focus by axial shift). One coherent source (633 nm HeNe or stabilised single-mode red) through
polarisation-maintaining fibre, 1×N splitter. Servo stand-in: ROBOTIS DYNAMIXEL XL330-M288-T class (20×34×26 mm, 4096 pulses/rev, from reseller listings). Ring diameter from arm pitch:
D = N·pitch/π (48 mm pitch: 199 mm for 13 arms, 275 mm for 18). Focal point test: haze enclosure, camera, pinhole photodiode on the focus for the phase lock, beam dump.

## Derived constraints (design_calc.py, estimates)
- Worst tilt from the wall normal ≈ 35° (13 arms) / 39° (18) for depth 0.3–1.22 m, lateral cone 20°.
- Pointing tolerance ≈ 10 µrad (waist w0 = λd/(πW), W = 5 mm); one servo step is 1.5 mrad = **~150× too coarse**: a fine stage is required (lateral fibre-tip shift behind the f = 50 mm lens, ~126 nm steps).
- Focus: ~8 mm axial fibre travel covers 0.3–1.5 m. Phase: ~21 nm (λ/30) per arm for 96% of peak; mechanical geometry cannot supply it over a metre, so lock on a signal at the focus. Air: ~1200 nm per kelvin over 1.2 m.
- Power cap used: ~75 µW per arm (~1 mW total, class-2 region); 18 arms at 75 µW exceeds 1 mW.
- Pass test for the rig: peak with all arms locked ≈ N × the peak with phases scrambled.

## Findings the author has heard and decided around (state them plainly)
- Constructive interference raises intensity at the point (N² for N equal coherent beams) but air shows light only by scattering; a Rayleigh estimate puts the focal needle ~10⁻⁵ as bright as the beam paths (focus ~1.4×10⁻¹⁴ W vs paths ~10⁻⁹ W at 75 µW/arm). A trapped or seeded particle would be vivid; none is in the design. The author decided: the design stands, no scatterer, visibility is the research question (stated as OPEN in the concept page).
- A planar ring of coplanar beams makes a needle (line) along the axis, not a point, in the plane-wave limit; each beam's finite waist limits the overlap to a short needle (~100 µm at the macro scale), a point to the naked eye. 13 beams leave rival maxima (~40% of peak a few microns off axis); 25–50 beams isolate the central point.
- Coil: the earlier primer's inductances (3.58 µH whole coil) omit a leading constant; the current-sheet expansion gives ~6.5 µH (tuning capacitors change). A conductive-PLA coil has Q ≈ 0.006 at 13.56 MHz with an assumed ~0.75 Ω·cm, so the RF coil is specified in copper and PLA is an appendix. NanoVNA measurement decides.
- Eye-safety design (author-specified): a hard-no cone (45° half-angle, like the shoulder-launcher back-blast area) around the direction to the wearer's eyes, enforced in hardware by a separate safety processor, mechanical stops, IMU, beam dump; an eye-tracking CNN is "intended safety engineering". Deep red is not intrinsically safer per mW and the blink reflex is weaker; total accessible power capped ~1 mW.

## Licensing and outreach (2026-10-14)
POE `LICENSE`: proprietary, not for sale or licensing; README invites partners in design or production, and names integrated-circuit engineers, nanotechnology engineers and 3D modelers (for 3D-printing guidance) as wanted. VAPMIP `LICENSE`: "Short-term licensing available upon request with offer".

## Open / not done
Fritzing board map; Blender previews (other than isometric) were rendered before a final lighting tweak; vendor STEP models not downloaded (OpenSCAD can't read STEP; FreeCAD would); fibre-tip positioner has no part; fibre routing; eye-safety classification; power/battery/harvest build (later, with the coil: copper coil with NFC, AM/FM harvest and Qi receiver); no part of this has been measured.
