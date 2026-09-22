# skills — part of ContextPlease's portable historical context

**Created 2026-09-22, expanded same day to cover all 19.** `ContextPlease`
exists to let someone else — or this user, on a different machine — drop
the exact accumulated context of this project's repos and this
conversation's own work straight into their own Claude Code, without
having to rebuild any of it by hand. This directory is the skills half of
that: the custom skills below are behavior this project actually taught
Claude, not generic tooling, and they're worth zero to a new setup until
they're actually installed into it.

## The 7 that matter for that purpose — install these

`cs-paper-code-conventions`, `generational-lineage`, `imagemagick`,
`nes-viewport`, `observer-position`, `scad-spatial`, `unit-management` —
authored during this project's own sessions, each one real accumulated
context (methodology, conventions, corrected mistakes) that would
otherwise have to be re-derived from scratch in a new session. **To drop
them into a fresh Claude Code setup:**

```bash
# user-level -- active in every project on that machine
cp -r ContextPlease/claude/skills/<name> ~/.claude/skills/<name>

# OR project-level -- ships with one specific repo, travels with its git history
cp -r ContextPlease/claude/skills/<name> <repo>/.claude/skills/<name>
```

`generational-lineage` already has a worked example of the project-level
route, with its own onboarding README, at
`GenerationalLineage/.claude/skills/generational-lineage/`.

## The other 12 — reference copies only, not part of the payload

`built-in-browser`, `chrome-browser`, `computer-use`, `deep-research`,
`docs`, `docx`, `import-memory`, `morning`, `pdf`, `pptx`,
`skill-creator`, `xlsx` are Anthropic's own built-in skills
(`~/.claude/skills/synced/`) — every Claude Code install already has
them natively. Kept here only for a complete local reference of what's
available, not because a new setup needs them copied in — copying them
would do nothing a fresh install doesn't already have.

Live originals: `~/.claude/skills/<name>/` (custom) and
`~/.claude/skills/synced/<id>/<name>/` (built-in), both user-level. This
directory is a plain **mirror**, not a different version — if a copy
here and a live one disagree, this is the one to reconcile against.
Point-in-time snapshot, not kept in sync automatically; re-copy when a
skill changes.

Not included: the Claude Code plugin-marketplace skills (`~/.claude/
plugins/marketplaces/.../skills/*/SKILL.md` — Discord/iMessage/Telegram
integrations, plugin-dev tooling, etc.). Third-party/opt-in plugin
content, not part of this project's own accumulated context.

---

## Index — custom (authored for this project)

| skill | what it's for |
|---|---|
| `cs-paper-code-conventions` | When a CS paper should show a runnable code listing vs. describe an API in prose vs. use boxed pseudocode — captioning/numbering/citation conventions. For `FourthAgePapers` and similar. |
| `generational-lineage` | Track the lineage of every operation in a derivation and watch for emergent geometries, decomposed against the Two Trees domain. Load for any mathematical/physical/structural derivation in this project. Also ships with the `GenerationalLineage` repo directly. |
| `imagemagick` | Shell-based ImageMagick reference: crop/resize/DPI, draw overlays, annotate, colour/tone, composite, montage, pixel-probing, figure-annotation coordinate math. |
| `nes-viewport` | Methodology for a 2D viewport onto content larger than itself — offset/clamp math, layered compositing, D-pad navigation, a reusable "sweeps the whole content" acceptance test for scrollbars. |
| `observer-position` | Tracking your own vantage point inside hypergeometric/algebraic maths with no camera or screen (sedenion space, box-kite structure). Combines `nes-viewport`'s bounded-window discipline with `scad-spatial`'s camera-angle parameters, applied abstractly. |
| `scad-spatial` | 3D spatial-awareness methodology: camera as viewport, OpenSCAD's edge/transform/camera language, disciplined visualization of higher-dimensional maths within human 3D perception limits. |
| `unit-management` | Identify which physical equations are relevant to a prompt by decomposing its quantities into SI base-dimension exponent vectors and matching against known equations. |

## Index — built-in (ship with Claude Code / the Claude apps)

| skill | what it's for |
|---|---|
| `built-in-browser` | The in-app browser pane inside the Claude desktop app (Cowork) — persistent sign-ins, tabs, reading pages as text, site approvals. Not Claude in Chrome. |
| `chrome-browser` | Claude in Chrome, the browser extension acting in the person's real Chrome with their own sign-ins — tool loading, tab handling, site permissions, safety rules. Not the built-in browser pane. |
| `computer-use` | Controlling apps on the person's own computer (screenshots, clicks, typing, scrolling) via the Claude desktop app or a linked remote session. Not for websites (that's the two browser skills). |
| `deep-research` | Multi-source research, comparison, trend/market analysis, or literature review, synthesized into a narrative report — coordinates research subagents. |
| `docs` | Living docs (shared, commented-on, editable pages) — when to create one vs. keep an answer in chat vs. use a different file format. |
| `docx` | Create, read, edit, or reformat Word documents (.docx/.dotx) — tables of contents, tracked changes, images, templates. |
| `import-memory` | Import a memory export from another AI assistant into Claude's memory, conversationally and additively. |
| `morning` | Render or schedule the user's morning brief as a styled HTML artifact. Only on explicit request or `/morning`. |
| `pdf` | Read/extract, merge/split, rotate, watermark, create, fill forms, encrypt/decrypt, or OCR PDF files. |
| `pptx` | Create, read, or edit PowerPoint decks (.pptx/.potx) — layouts, speaker notes, templates, comments. |
| `skill-creator` | Create a new skill, edit/optimize an existing one, or run evals to benchmark a skill's triggering accuracy. |
| `xlsx` | Open, edit, create, clean, or convert spreadsheet files (.xlsx/.xlsm/.xltx/.csv/.tsv). |
