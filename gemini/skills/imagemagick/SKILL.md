---
name: imagemagick
description: Practical ImageMagick reference for inspecting and adjusting raster images from the shell — crop, resize, DPI, draw overlays (lines/circles/rectangles/arrows), annotate text, colour/tone, composite/layer, montage, pixel probing, and figure-annotation coordinate math. Use when the task is to measure, cut, mark up, combine, convert, or batch-process an image file, or to overlay scientific annotations (mark a region, draw an axis line, label a feature) on a plot or diagram.
version: 0.1.0
---

# ImageMagick

This box runs **ImageMagick 6.9.12** — the v6 tool names are the primary
interface: `identify`, `convert`, `mogrify`, `composite`, `montage`. The v7
`magick` / `magick <tool>` wrappers also work; prefer the v6 names here for
copy-paste reliability.

## The non-destructive rule

**Never operate on the only copy.** First `cp original.png work.png`, keep
`original.png` untouched, do every adjustment on `work.png` (or a chain of
`work_v1.png`, `work_v2.png`). `mogrify` edits **in place** — only ever point
it at a throw-away copy or use `-path outdir/`.

Always `identify` before and after — confirm the dimensions, colourspace, and
that the file is still a valid image.

## Inspect

```
identify img.png                              # WxH, type, depth
identify -verbose img.png | head -60          # full metadata, histogram
identify -format '%w %h %[channels] %[colorspace]\n' img.png
convert img.png -format '%[pixel:p{412,300}]' info:   # pixel at (x=412,y=300)
convert img.png -define histogram:unique-colors=true histogram:info:- | sort -rn | head
```

Origin is **top-left**, x → right, y → **down**.

## Geometry, crop, resize, DPI

```
convert in.png -crop 800x400+120+60 +repage out.png      # WxH+Xoff+Yoff; +repage resets canvas
convert in.png -resize 50% out.png
convert in.png -resize 1200x out.png                      # width 1200, height auto
convert in.png -resize 1200x800\! out.png                 # force exact (ignore aspect)
convert in.png -density 300 -units PixelsPerInch out.png  # set DPI metadata (raster only)
convert in.png -bordercolor white -border 20 out.png
convert in.png -background white -gravity center -extent 2100x1000 out.png   # pad to canvas
```

`-crop` almost always wants `+repage` after it, or downstream ops keep the old
virtual canvas offset.

## Draw overlays (lines, shapes, arrows)

Outline only: `-fill none`. Filled: set `-fill`. Coordinates are pixels.

```
convert work.png -stroke red -strokewidth 3 -fill none \
  -draw "line 1360,40 1360,900" \
  -draw "circle 1500,300 1500,340" \
  -draw "rectangle 1340,120 1560,520" \
  -draw "ellipse 1500,300 120,60 0,360" \
  out.png
```

Arrow = a line plus a small filled triangle at the tip:

```
convert work.png -stroke '#0a7' -strokewidth 3 -fill '#0a7' \
  -draw "line 200,200 400,120" \
  -draw "polygon 400,120 384,132 392,104" \
  out.png
```

Multiple `-draw` run left→right in one pass. Semi-transparent stroke:
`-stroke 'rgba(255,0,0,0.5)'`.

## Annotate text

```
convert work.png -gravity NorthWest -pointsize 28 -fill black \
  -annotate +130+40 "period-3 window" out.png
convert -list font | grep -i dejavu          # available fonts
convert work.png -font DejaVu-Sans -pointsize 24 -fill '#c00' \
  -gravity SouthEast -annotate +20+20 "d* = 0.24631" out.png
```

`-annotate +X+Y` offset is **relative to the `-gravity` anchor**, not absolute
— set `-gravity NorthWest` for plain top-left pixel coordinates. Label with a
readable backing box: draw a filled `rectangle` first, then `-annotate` over
it.

## Colour / tone

```
convert in.png -colorspace Gray out.png
convert in.png -negate out.png
convert in.png -brightness-contrast 10x20 out.png        # brightness x contrast, -100..100
convert in.png -level 5%,95% out.png                     # black/white points
convert in.png -modulate 100,140,100 out.png             # brightness,saturation,hue (%)
convert in.png -fuzz 8% -transparent white out.png       # knock out near-white to alpha
convert in.png -threshold 50% out.png                    # hard 1-bit
```

## Composite / layer

```
convert base.png overlay.png -gravity NorthWest -geometry +120+60 -composite out.png
composite -geometry +120+60 overlay.png base.png out.png
convert base.png ovl.png -compose Multiply -composite out.png       # blend mode
convert base.png ovl.png -compose over -define compose:args=50 -composite out.png
```

Build an annotation on a transparent layer the same size as the base, then
`-composite` — keeps the base pristine and the marks editable as their own
file.

## Montage / side-by-side

```
montage a.png b.png -tile 2x1 -geometry +8+8 -background white cmp.png
montage before.png after.png -tile 1x2 -geometry +0+4 -title "d* bubble" out.png
```

## Batch

```
mkdir out
mogrify -path out -resize 1000x -format png frames/*.png       # never in place
```

## Figure-annotation coordinate math

To mark a data value on a plot you must map **data coords → pixel coords**.
Read the pixel extents of the plotted axes from the image (zoom / probe the
axis tick pixels with `-format '%[pixel:...]'` or by eye at known ticks), then:

```
x_px = x0_px + (x_data - x_min) / (x_max - x_min) * (x1_px - x0_px)
y_px = y0_px + (y_max - y_data) / (y_max - y_min) * (y1_px - y0_px)   # y inverted
```

where `(x0_px, x1_px)` are the pixel x of the left/right axis limits at data
`x_min, x_max`, similarly for y. Record the four calibration points you used
in a comment or a sidecar `.md` so the annotation is reproducible.

## Gotchas

- Operations apply **left to right**; order changes the result.
- `-crop` → follow with `+repage`.
- `-gravity` silently shifts `-annotate`, `-draw` primitives that use it, and
  `-extent`/`-crop` offsets. Set it explicitly (usually `NorthWest`) or unset
  with `-gravity None`.
- Line art / diagrams → **PNG**, not JPG (JPG rings around edges).
- `\!`, `\>`, `\<` in `-resize` must be shell-escaped.
- Big images: `-limit memory 2GiB -limit map 4GiB` if it thrashes.
- v6 has no `-magick` verb chaining like v7; keep each `convert` a full pass.

## Verify

After every adjustment: `identify -format '%wx%h %[colorspace]\n' out.png`,
then look at it. If it was a calibrated annotation, spot-check one marked
feature against its known data coordinate.
