#!/usr/bin/env python3
"""SessionStart hook: remind Claude that the ~/.clauderc* files exist, what each
holds, at what granularity, and how to pull a block into the prompt.
Fires on startup / resume / clear / compact. Output is generated live from the
files, so sizes, mtimes and block names are never stale. stdlib only."""
import glob, json, os, re, time

H = os.path.expanduser("~")
CP = "/home/rendier/Projects/ThePlace/ContextPlease/claude"
PROJ_CM = "/home/rendier/Projects/ThePlace/.claude/.clauderc_canonical_maths"

ROLE = {
 ".clauderc": ("GLOBAL env vars: repo paths, constants (D_STAR_*, LAMBERT_*), protocol shortcuts. Sourced by .bashrc.", "coarse: one var = one fact/path"),
 ".clauderc_canonical_maths": ("REFERENCE tier: equations, notation, timeless. @RCCM_<NAME> blocks.", "fine: one block = one structure"),
 ".clauderc_ValaQuenta": ("HISTORY tier: how established, refuted, open, STATUS. @RCVQ_<NAME> blocks; ctxengine <module> per engine.", "fine: one block = one engine/topic"),
 ".clauderc_ctx": ("lookup functions: rccm NAME | rcvq NAME | rcboth NAME | rcls (source it first).", "tool, not content"),
 ".clauderc_context_1": ("per-directory/repo CURRENT state, live-edited, authoritative.", "medium: one entry per repo"),
 ".clauderc_context_2": ("append-only dated log of poignant/historical moments.", "medium, chronological"),
 ".clauderc_context": ("session continuity: what a cold session needs to resume. Newest first.", "coarse"),
 ".clauderc_context_hub": ("where context LIVES + rules for keeping it there (hist_prime, scratchpad, etc).", "map of the map"),
 ".clauderc_memory": ("portable durable memory (committed+pushed copy of the idea behind auto-memory).", "coarse"),
 ".clauderc_scratchpad_contents": ("manifest of the persistent scratchpad: names+locations only.", "index"),
 ".clauderc_user_provenance": ("Cody's ORIGINAL work vs established literature; origin images; bibliography pointers.", "medium: dated sections"),
 ".clauderc_citations": ("prior-art queue by repo (Post-Hoc citation pass).", "per-repo list"),
}

def names(path, tag):
    try:
        t = open(path, errors="replace").read()
    except OSError:
        return []
    return re.findall(r"^@(%s_[A-Z0-9_]+)$" % tag, t, re.M)

out = ["CLAUDERC MAP (auto-generated at session start; Cody's context-shortcut system).",
 "Cody built ~/.clauderc* so context can be injected by the PIECE (env var / block) instead of him repeating himself.",
 "RULES: (1) You may put .clauderc* files anywhere if mirrored to ContextPlease/claude/clauderc/. (2) Before asking him anything or saying 'I don't",
 "know', look here first (rcls, rccm/rcvq/rcboth, ctxengine, grep the files). (3) If still absent: say 'I don't remember' and let him point you to",
 "the spot; do not guess. (4) Context purity matters near the prompt; rolled-out context is attention moved elsewhere, not loss: pull it back by block.",
 "(5) Use the code's own identifiers; maths in Unicode, never LaTeX. Pull a block:  source ~/.clauderc_ctx; rcboth NAME   (or rcls).", ""]
for f in sorted(glob.glob(H + "/.clauderc*")):
    b = os.path.basename(f)
    if ".bak" in b or not os.path.isfile(f):
        continue
    role, gran = ROLE.get(b, ("(not in primer table: read its header)", "?"))
    kb = os.path.getsize(f) // 1024
    d = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(f)))
    m = os.path.join(CP, b)
    mirrored = os.path.isfile(m) and open(m, "rb").read() == open(f, "rb").read()
    out.append(f"- {b} [{kb} KB, {d}{'' if mirrored else ', NOT mirrored/IN SYNC with ContextPlease/claude/'}] {role} ({gran})")
for tag, f in (("RCCM", "/.clauderc_canonical_maths"), ("RCVQ", "/.clauderc_ValaQuenta")):
    n = names(H + f, tag)
    out.append(f"\n{tag} blocks ({len(n)}): " + " ".join(x.split('_', 1)[1] for x in n))
try:
    if open(PROJ_CM, errors="replace").read() != open(H + "/.clauderc_canonical_maths", errors="replace").read():
        out.append("\nWARNING: the canonical maths injected by the other SessionStart hook (ThePlace/.claude/.clauderc_canonical_maths) is STALE vs "
                   "~/.clauderc_canonical_maths. Trust the home copy (rccm).")
except OSError:
    pass
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n".join(out)}, "suppressOutput": True}))
