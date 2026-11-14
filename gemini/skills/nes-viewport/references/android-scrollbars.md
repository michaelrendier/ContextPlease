# Android — three panes that scroll independently

The PTorrent APK has **ptorrent list**, **ptorrent status**, **ptorrent info** —
three viewports, each showing content larger than its frame, that must scroll
**separately** with their own thumbs. "They don't scroll properly" is nearly
always one of the four patterns below.

## 1. The shared‑outer‑ScrollView trap (most likely)

```
ScrollView                     ← ONE scroll container
 └ LinearLayout (vertical)
     ├ LinearLayout  "list"    ← rows added directly; height = wrap_content
     ├ LinearLayout  "status"
     └ LinearLayout  "info"
```

The outer `ScrollView` scrolls all three as one tall column. Each inner box has
effectively infinite height, so its own scrollbar never has anything to do.

**Fix:** three independent, bounded scroll containers, no shared scrolling
ancestor.

```
LinearLayout (vertical)                       or ConstraintLayout
 ├ RecyclerView   "list"    height=0dp weight=2   android:scrollbars="vertical"
 ├ RecyclerView   "status"  height=0dp weight=1   android:scrollbars="vertical"
 └ NestedScrollView "info"  height=0dp weight=1   android:scrollbars="vertical"
```

- `RecyclerView` + `LinearLayoutManager` for anything list‑shaped (list, status).
- `NestedScrollView` for a single long text/detail blob (info).
- Height must be bounded: `0dp` + `layout_weight`, or a fixed `dp`, or
  `maxHeight`. A scroll container with `wrap_content` height cannot scroll.
- `setScrollbarFadingEnabled(false)` if you want the thumb always visible.

## 2. Nested scrolling steals the drag

A `RecyclerView` inside a `NestedScrollView` (or another RV): the parent consumes
the vertical drag and the child never scrolls.

- Don't nest scroll containers on the **same axis** unless you mean to.
- If you must: `child.setNestedScrollingEnabled(false)` makes the child scroll
  itself and the parent leave it alone (child then needs a real bounded height,
  not `wrap_content`, or it expands and defeats the point).
- Prefer flattening: one `RecyclerView` with multiple view types beats an RV in a
  ScrollView.

## 3. Custom‑drawn content — override the three scroll metrics

If a pane draws its own content on a `Canvas` (not an adapter), the framework
cannot size or place the thumb until you tell it the numbers. Override all three
in the same units (px):

```kotlin
override fun computeVerticalScrollRange()  = contentHeightPx      // ch
override fun computeVerticalScrollExtent() = height               // vh  (the pane)
override fun computeVerticalScrollOffset() = scrollYPx            // oy
// horizontal: the same three with Horizontal / width
```

With those correct, `android:scrollbars="vertical"` draws a thumb whose length is
`Extent/Range` of the track and whose position is `Offset/(Range-Extent)` — the
exact formula in `references/viewport-model.md`. If the thumb is stuck at the top
while content scrolls, `computeVerticalScrollOffset()` is returning a constant
(you forgot to return `scrollYPx`). If the thumb is full‑length, `Range` still
equals `Extent` because `contentHeightPx` was read before the content existed —
recompute after `requestLayout()` / data change and call `awakenScrollBars()`.

For fling on a custom view: `OverScroller`; in `computeScroll()` read
`scroller.currY`, `scrollTo(0, y.coerceIn(0, maxOy))`, `postInvalidateOnAnimation()`.
`scrollTo` must clamp — override it, don't trust callers.

## 4. move‑to‑top / move‑to‑bottom (the inspector)

The buttons that let you eyeball that the bar sweeps the whole card data:

```kotlin
// top
rv.smoothScrollToPosition(0)                       // or scrollToPosition(0)

// bottom, flush (not just "last item visible")
(rv.layoutManager as LinearLayoutManager)
    .scrollToPositionWithOffset(adapter.itemCount - 1, 0)
rv.post { rv.scrollBy(0, Int.MAX_VALUE / 2) }      // settle onto max offset

// follow-tail for a live status pane
private var followTail = true
fun onRowsAppended() { if (followTail) rv.scrollToPosition(adapter.itemCount - 1) }
rv.addOnScrollListener(object : RecyclerView.OnScrollListener() {
    override fun onScrolled(v: RecyclerView, dx: Int, dy: Int) {
        followTail = !v.canScrollVertically(1)     // at the bottom -> stay pinned
    }
})
```

`v.canScrollVertically(1)` false == there is no more content below == flush at
the bottom. `canScrollVertically(-1)` false == flush at the top. Assert both
after the respective button in an instrumented test.

## Instrumented acceptance test (Espresso / UiAutomator sketch)

```
for each pane p in (list, status, info):
    scroll p to top
    assert !p.canScrollVertically(-1)                       // FLUSH top
    assert first visible item index == 0
    scroll p to bottom
    assert !p.canScrollVertically(1)                        // FLUSH bottom
    assert last visible item index == adapter.itemCount - 1
    thumb = read the drawn scrollbar (or the three compute* values)
    assert thumb at track end within 1px
    // SWEEP
    scroll p to top; seen = {}
    while p.canScrollVertically(1):
        seen += currently-bound item indices
        p.scrollBy(0, paneHeight - rowHeight)
    seen += currently-bound item indices
    assert seen == 0 .. itemCount-1
```

Map a failure to a cause with the table in `SKILL.md` §8.
