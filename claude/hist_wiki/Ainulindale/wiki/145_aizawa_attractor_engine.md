# 145 — The Aizawa attractor engine

| | |
|---|---|
| Written | 2026-11-24 |
| Scope | what a strange attractor's skeleton is (a rotation with a radial driver), and why the comparison engine for the zeta pathway needs one |
| Requested by | Cody, 2026-11-24: "get the core maths of this pathway from the aizawa attractor ... that is exactly what i see in my head as the riemann zeta path ... give me two Full Engine Protocol engines, one for the attractor and one for the riemann zeta path ... in python." |
| Code | `ValaQuenta/modules/aizawa_attractor/` · tests `Testing/test_aizawa_attractor.py` (9, all pass) · notebook `28_aizawa_attractor.ipynb` · wiki `wiki/aizawa_attractor.md`, toolbox 45 |
| Confidence | ESTABLISHED (the system and its identities); the original paper reference is not yet verified |

> **Note from the assistant.** Written by a transformer (Claude Sonnet 5.5, `claude-sonnet-5-5`) working with Cody Allison in Claude Code. Cody does not tell the model what result he wants; the checks were written before the runs, and where one failed the failure is recorded here.

## 1. Where it came from

A short video of a glowing sphere with a tube through it; the code on screen (`generateGeometry`, `rk4Step`, `lineDistances`) was found on GitHub as the "Holographic Aizawa Attractor" page. It is the Aizawa system integrated with RK4. Cody saw in it the shape he sees for the Riemann zeta path.

## 2. The skeleton

In cylindrical coordinates the first two equations are exact: dr/dt = (z-b) r and dphi/dt = d. The orbit turns about the z axis at a constant rate; z sets the growth rate of the radius; r cannot reach the axis. Only the term f z x^3 breaks the rotation symmetry: at f = 0 the 3-D orbit is the 2-D (r, z) flow swept round the axis (checked to 1.7e-8). The three fixed points sit on the axis with eigenvalues (z*-b) +- id and a - z*^2. The largest Lyapunov exponent is +0.085.

## 3. Not here

Anything about the zeta function (see 146). The attractor's original paper is not yet checked against a title page, and the origin of the animation page (author, licence) is not established; the local copy stays local-only.
