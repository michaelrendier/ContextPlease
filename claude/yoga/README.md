# `claude/yoga/` — Yoga Claude's set (the second machine)

Everything else under `ContextPlease/claude/` is **X1 Carbon Claude's** (the primary machine). This directory holds what is specific to the
**Lenovo Yoga 7 2-in-1 16IML9** (Core Ultra 7 155U, 16 GB RAM, 8 GB swap, Linux Mint 22.3), set up from 2026-11-27 as the telescope-data
**satellite archive**, the heavy-evaluation box, and the PTorrent web/Android workbench. Machine marker in the shell: `CLAUDE_MACHINE=yoga`.

| path | what |
|---|---|
| `machine/inxi_full_2026-11-28.txt` | full `inxi -Fxxxaz` report, for benchmarking later (serials, UUIDs, MACs and the MAC-derived interface name masked as `<filter>`) |
| `clauderc/` | only the Yoga's live `~/.clauderc*` files that **differ** from the X1 mirrors in `claude/`; a file missing here is byte-identical to the X1 copy |
| `scratchpad/` | mirror of the Yoga's own scratchpad, `ThePlace/.claude/scratchpad/` |
| `RESUME_*.md` | the Yoga bring-up plan, dated |
| `HANDOVER_TO_PRIMARY_2026-11-28.md` | Carbon Claude's handover: prime directives, rules, campaign state, readiness list for the Yoga to become primary |

**Skills.** The Yoga's live skills are named `Yoga-{skill}` (directory; the `name:` field is lowercase `yoga-{skill}`). Only skills whose content
differs from the X1 copy are mirrored, as `claude/skills/Yoga-{skill}/`; the X1 copies under their plain names are never overwritten from the Yoga.
As of 2026-11-28: `Yoga-telescope-download` (Yoga memory/CPU/disk budgets, systemd user units for disowned jobs, optional mount guard) and
`Yoga-html-spatial-awareness` (§8, application faces / PTorrent web face, CherryPy). The other 16 were byte-identical to the X1 copies when installed.

**Live locations on the Yoga:** `~/.clauderc*`, `~/.claude/skills/Yoga-*`, `ThePlace/.claude/` (scratchpad, persistent Claude Code temp via
`CLAUDE_CODE_TMPDIR`), telescope data in `ThePlace/TelescopeArchive/` (not in git).
