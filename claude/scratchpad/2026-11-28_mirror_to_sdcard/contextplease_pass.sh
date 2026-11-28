#!/usr/bin/env bash
# ContextPlease Protocol pass (README §5b). Mirrors; never deletes anything from ContextPlease.
#   1 ~/.clauderc*  -> claude/clauderc/      2 staging scratchpad -> claude/scratchpad/     3 regenerate .clauderc_scratchpad_contents
#   4 repo wikis    -> claude/hist_wiki/      5 skills (plain names, not Yoga-*) -> claude/skills/
# Secret scan on everything it copies; a hit stops the pass before anything is staged.
set -eu
P=/home/rendier/Projects/ThePlace; C=$P/ContextPlease/claude
for f in ~/.clauderc*; do cp -p "$f" "$C/clauderc/"; done
rsync -a --exclude=__pycache__ --exclude='*.pyc' "$P/.claude/scratchpad/" "$C/scratchpad/"
for r in ValaQuenta Ainulindale PtolemyDesktop PTorrent GenerationalLineage SedenionSpectralRelativity DeriveCancerDrugs TuringStack FourthAgePapers; do
  [ -d "$P/$r/wiki" ] && { mkdir -p "$C/hist_wiki/$r/wiki"; rsync -a "$P/$r/wiki/" "$C/hist_wiki/$r/wiki/"; }; done
[ -d "$P/VAPMIP/docs/wiki" ] && { mkdir -p "$C/hist_wiki/VAPMIP/docs/wiki"; rsync -a "$P/VAPMIP/docs/wiki/" "$C/hist_wiki/VAPMIP/docs/wiki/"; }
for s in ~/.claude/skills/*/; do n=$(basename "$s"); case "$n" in Yoga-*) continue;; esac; mkdir -p "$C/skills/$n"; rsync -a --exclude=__pycache__ "$s" "$C/skills/$n/"; done
# manifest of the scratchpad (names + locations), same format as before
M=$C/clauderc/.clauderc_scratchpad_contents
python3 - "$M" "$C/scratchpad" <<'EOF'
import os, sys, datetime
m, root = sys.argv[1], sys.argv[2]
head = []
for l in open(m):
    head.append(l)
    if l.startswith("# Last regenerated"): break
head[-1] = f"# Last regenerated: {datetime.date.today()} (ContextPlease pass; added 2026-11-28_mirror_to_sdcard/ and the other session directories)\n"
out = "".join(head) + "\n"
top = sorted(f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f)))
for f in top: out += f"- {f}\n"
out += "\n"
for d in sorted(x for x in os.listdir(root) if os.path.isdir(os.path.join(root, x))):
    out += d + "/\n"
    for dp, dn, fn in os.walk(os.path.join(root, d)):
        dn[:] = sorted(x for x in dn if x != "__pycache__")
        for f in sorted(fn):
            if f.endswith(".pyc"): continue
            out += "    " + os.path.relpath(os.path.join(dp, f), os.path.join(root, d)) + "\n"
    out += "\n"
open(m, "w").write(out)
EOF
cp -p "$M" ~/.clauderc_scratchpad_contents
# secret scan over what changed (tracked or not)
cd "$P/ContextPlease"
hits=$(git status --porcelain | awk '{print $2}' | xargs -r -I{} find {} -type f -size -2M 2>/dev/null | xargs -r grep -IlE 'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|gho_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY' 2>/dev/null || true)
[ -z "$hits" ] || { echo "SECRET-LIKE TEXT in: $hits"; exit 3; }
echo "pass complete"; git status --short | wc -l
