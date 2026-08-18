# Spacing and Text Placement

Use this reference for every new deck and major redesign. The goal is an optically calm reading rhythm: equal relationships look equal, important transitions receive a larger gap, and text never appears accidentally glued to artwork.

## 1. Establish the spacing system

For a 1280 × 720 canvas, begin with an 8 px base unit. Scale proportionally for other canvases.

| Relationship | Starting range | Use |
|---|---:|---|
| Tight gap | 12–20 px | Eyebrow to title, label to value, lines within one semantic group |
| Regular gap | 24–32 px | Title to subtitle, paragraph to supporting note, closely related text blocks |
| Major gap | 40–64 px | Text stack to image, chart, scene compartment, or a new semantic section |
| Page margin | 64–80 px | Normal text and primary content; small page markers may use 48–64 px |
| Minimum emergency clearance | 24 px | Absolute minimum between rendered text ink and unrelated image/chart content |

Choose exact deck tokens such as `tight=16`, `regular=28`, `major=48`, and `page=72`. Reuse them instead of selecting gaps independently on every slide.

For peer gaps in one group, target `largest / smallest ≤ 1.25`. A hierarchy may use different tiers, but each change of tier must correspond to a change in meaning.

## 2. Measure rendered ink, not nominal boxes

Text-box bounds include invisible font ascender, descender, and internal padding. Image bounds may include quiet paper while the real subject begins elsewhere.

After rendering:

1. Locate the visible top, bottom, left, and right of the text ink.
2. Locate the nearest visible image subject, high-contrast mass, crop edge, chart mark, or compartment boundary.
3. Measure the shortest perceived gap between them.
4. Compare it with the intended tier in the `spacing_contract`.

Treat dark roofs, canopies, faces, hands, bright anchor shapes, and dense chart marks as subject matter. A pale or transparent part of the image rectangle does not automatically provide a safe text zone.

## 3. Reserve the title stack before placing the image

For a title-above-image layout:

```text
image_top = rendered_bottom_of_lowest_title_element + major_gap
```

The lowest title element may be the last wrapped title line, subtitle, or deck descriptor. Do not calculate `image_top` from an assumed line count or the original text-box height. Render once, find the actual lowest ink edge, and move the image or resize the title field.

When the title wraps during export or font substitution, recompute the reserve. A title field and image must never overlap merely because their original boxes did not.

## 4. Balance vertical free space

For a text stack placed above an image or between two major elements, compare:

- `g_top`: free space from the safe-area top to the first visible text ink;
- `g_bottom`: free space from the last visible text ink to the image/scene subject.

Use `0.8 ≤ g_top / g_bottom ≤ 1.25` as a diagnostic when the composition is intended to feel neutral. Optical balance outranks exact arithmetic: uppercase eyebrows, heavy titles, and dark image masses may require a small correction.

Do not force this ratio when the slide intentionally creates tension, acceleration, or directional pull. Record the deviation as a `spacing_exception`, state its narrative purpose, and keep legibility intact.

## 5. Text beside or over imagery

- For side-by-side text and imagery, keep one major gap between the text ink and the nearest image subject. Increase it when the image edge is dark or visually noisy.
- For text over imagery, use an authored quiet zone, an intentional paper field, or a low-detail area with sufficient contrast. Never rely on a coincidental pale patch.
- Do not allow a high-contrast contour to run tangent to a letterform. Move the crop, increase the gutter, shorten the copy, or add a deliberate field.
- Keep captions visually attached to their own scene with a tight or regular gap, but keep them a major gap away from the next compartment.
- A full-bleed image may touch the canvas edge; text should not, unless edge proximity is the explicit compositional device.

### Contrast reserve

Treat contrast as a geometric reserve, not a final color tweak.

- Normal text must maintain at least 4.5:1 contrast against its worst-case background; large text may use 3:1. Target 7:1 for small metadata, footnotes, page numbers, and creator credits whenever practical.
- When text overlaps an image, sample the darkest, lightest, and accent-colored areas beneath the full rendered text run. Passing on one coincidental patch is insufficient.
- If any part of a text run fails, move the text into authored quiet space or place it on a solid paper/ink field. Prefer a solid field; do not rely on translucent white or black over variable imagery.
- Keep functional text colors separate from decorative/data grays. A pale neutral may encode an undecided data category while a darker neutral is required for labels and metadata.
- Verify contrast in animation start, intermediate, and end states. A moving crop or reveal must never expose a failing background behind stationary text.

## 6. Build from relationships

Place elements in dependency order:

1. Safe area and page margin.
2. Rendered title stack.
3. Major text-to-scene gutter.
4. Image or scene compartment.
5. Captions, notes, page markers, and credits.

When text changes, recompute downstream positions from these relationships. Do not leave images at stale absolute coordinates.

For HTML, use layout variables and measured DOM geometry where practical. For PPTX, calculate provisional geometry, render the slide, inspect actual wrapping, then rebuild from source with corrected coordinates.

## 7. Required spacing audit

For every rendered slide, record or verify:

- text stays within the declared page margin;
- the full rendered title stack has its reserved major gap before imagery begins;
- no text-to-image or text-to-chart clearance falls below 24 px;
- peer gaps use the same spacing tier and remain within roughly 25% of each other;
- neutral vertical compositions satisfy the top/bottom balance diagnostic;
- captions are attached to the correct compartment and separated from neighbors;
- every intentional deviation is present in `spacing_exceptions` with a purpose;
- animation start and end states preserve the same minimum clearances.
- every visible text run meets the contrast reserve; no glyph crosses between backgrounds that require incompatible text colors.

Inspect every slide at full size. A contact sheet can reveal rhythm, but it cannot validate precise clearance.
