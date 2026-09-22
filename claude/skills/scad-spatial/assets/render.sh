#!/usr/bin/env bash
# render.sh — batch-render hyperview.scad: the canonical camera poses + a $t sweep.
# Proves the "move to a canonical pose and check the whole model is framed" step
# (§5 of SKILL.md) in the 3D case.  Needs `openscad` on PATH.
set -eu
SCAD="${1:-hyperview.scad}"
OUT="${2:-out}"
MODE="${MODE:-rotate}"
SIZE="${SIZE:-1400,1050}"          # 4:3 — matches camera.py aspect
mkdir -p "$OUT"

command -v openscad >/dev/null || { echo "openscad not on PATH"; exit 1; }

# target the model centre (0,0,0); distance chosen to fit a ~radius-20 model
DIST="${DIST:-70}"

declare -A POSE=(
  [front]="0,0,0,90,0,0"
  [top]="0,0,0,0,0,0"
  [bottom]="0,0,0,180,0,0"
  [right]="0,0,0,90,0,90"
  [left]="0,0,0,90,0,-90"
  [iso]="0,0,0,55,0,25"
)

for name in "${!POSE[@]}"; do
  IFS=, read tx ty tz rx ry rz <<< "${POSE[$name]}"
  openscad -q -o "$OUT/${MODE}_${name}.png" \
    -D "MODE=\"$MODE\"" \
    --camera="$tx,$ty,$tz,$rx,$ry,$rz,$DIST" \
    --projection=p --imgsize="$SIZE" --colorscheme=Tomorrow \
    "$SCAD"
  echo "  $OUT/${MODE}_${name}.png"
done

# a $t animation from the iso pose (0..1 over N frames)
N="${FRAMES:-72}"
openscad -q -o "$OUT/${MODE}_anim.png" \
  -D "MODE=\"$MODE\"" \
  --camera="0,0,0,55,0,25,$DIST" --projection=p --imgsize="$SIZE" \
  --colorscheme=Tomorrow --animate "$N" "$SCAD"
echo "  $OUT/${MODE}_anim*.png   ($N frames over \$t)"
echo
echo "stitch:  ffmpeg -framerate 24 -i $OUT/${MODE}_anim%05d.png -pix_fmt yuv420p $OUT/${MODE}.mp4"
