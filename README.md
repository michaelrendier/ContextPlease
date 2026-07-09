# ContextPlease

Cross-device backup of portable AI-assistant context files, so Cody isn't
dependent on any single phone/laptop's local storage.

- `claude/` — `.clauderc*` files (Claude Code's git-backed context system
  for the ThePlace working directory: repo path/URL shortcuts, canonical
  math notation, per-repo state, cross-cutting memory).
- `gemini/` — `.geminirc*` files, same idea for Gemini (added later).

Manual cadence for now: push current versions at the end of a session,
pull at the start of the next one on whichever device is active.
