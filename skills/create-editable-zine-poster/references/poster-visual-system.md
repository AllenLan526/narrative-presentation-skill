# Poster Visual System

Use this reference to flatten the zine-anchor deck's narrative techniques onto one page without flattening its objects.

## One-page narrative

Translate slide sequence into reading sequence:

```text
hook -> evidence -> interpretation -> action or conclusion
```

The sequence may be vertical, diagonal, radial, or led by the anchor. Do not create equal-weight dashboard cards. One module must dominate and the others must support it.

## Shared grammar

Lock:

- one warm or cool paper/background family;
- one neutral ink plus at most one secondary neutral;
- one exact high-chroma accent hue unless brand/data semantics require more;
- one anchor geometry or relation;
- one primary illustration grammar;
- one tactile boundary logic;
- one density rhythm: quiet -> concentrated -> quiet.

Use the anchor as an organizing seam, aperture, path, contour, horizon, or enclosure. It must point, divide, contain, reveal, or connect. If removing it does not weaken meaning or reading order, redesign it.

Prefer a single clean directional gesture. A branch, connector, tab, ray, notch, or accent fragment must earn its place by carrying information that cannot be expressed through alignment or proximity. Remove ornamental side branches and duplicated gestures. Minimalism is structural: one dominant visual route, few competing axes, and enough quiet space for the eye to complete the connection.

## Composition families

Choose one:

- `seam-led`: a vertical or diagonal anchor splits truth from interpretation;
- `aperture`: a compact opening reveals the dominant image or finding;
- `field-and-island`: one active cluster floats in 65–80% quiet paper;
- `processional`: modules follow one path with clear changes in scale;
- `evidence-basin`: title and finding sit above a dominant data or map field;
- `paired-tension`: two unequal compartments express before/after, fact/meaning, or surface/structure.

Do not use more than two primary axes.

## Image handling

For a truthful photographic scene:

- keep the semantic subject and spatial invariant;
- use one swappable image frame;
- build torn edge, tint, label, and caption as separate native elements;
- compress irrelevant detail through cropping or a restrained overlay;
- keep a broad, authored quiet zone for live text.

For distilled illustration:

- identify two to four source anchors and one metaphor;
- remove roughly 65–90% of descriptive detail;
- favor cut-paper mass, dry-print silhouette, broken contour, rhythm field, fragment stack, or orbit/drift;
- keep typography out of generated art;
- recreate simple geometry with native shapes when feasible.

## Spacing system

Use an 8-unit base on a 1280 x 1800 planning canvas and scale proportionally.

| Tier | Starting range | Use |
|---|---:|---|
| Tight | 12–20 | Eyebrow-title, label-value, lines in one group |
| Regular | 24–36 | Title-subtitle, paragraph-note, related modules |
| Major | 48–72 | Text-to-image/chart, section transition |
| Margin | 72–104 | Primary safe area |
| Minimum clearance | 24 | Rendered text ink to unrelated high-contrast content |

Reserve the complete rendered title stack before the dominant scene begins. Measure visible ink and visible subjects, not only bounding boxes. Keep peer gaps within about 25% unless the hierarchy changes.

## Text-shape collision audit

Build exclusion geometry before finalizing layout:

1. Record a rendered-ink rectangle for every live text module after wrapping and font selection.
2. Record one or more `collision_zones` for every anchor, image subject, chart field, crop edge, torn handoff, and high-contrast decorative mass. Use local rectangles rather than one oversized whole-group rectangle when a shape bends across the page.
3. Expand each text rectangle by the declared minimum clearance on all sides.
4. Reject every intersection with an unrelated collision zone. Treat tangencies and gaps below the minimum as failures.
5. Permit text-on-shape only inside its own semantic module and record the exact owned shape ID as a `collision_exemption`.
6. Render the page and repeat the check against visible ink. Font substitution, tracking, rotation, and clipping can invalidate source geometry.

Z-order is not a collision fix. Text placed above a red seam is still intersecting the seam. Reroute the seam or reflow the text until the exclusion test passes.

## Text inside bands and shapes

Treat a text-bearing shape as one local coordinate system:

- Apply one shared transform to the group. A slanted background with horizontal text is usually an error; rotate both together or keep the text-bearing edges level.
- Measure padding to the visible polygon edge at each line's vertical position. A bounding rectangle can hide a near-collision with a diagonal edge.
- Keep `max(left, right) / min(left, right) <= 1.5` and the same ratio for top/bottom unless an explicit narrative asymmetry is recorded.
- Keep every internal inset at least the tight-gap token.
- Keep the full rendered text stack at no more than 70% of the usable shape height. For label bands, 45–60% usually reads more calmly.
- Reduce display size before the label feels wedged into the shape. Shorten secondary copy before shrinking it below legibility.
- Inspect the final render at full size. Rotation, font substitution, tracking, and irregular edges can change the apparent margins.

Do not compare only the left edge of the text box with the left edge of the shape. Compare all four visible insets and the distribution of negative space around the complete text stack.

## Typography

Use one expressive display family and one quiet workhorse family, or one variable family with clear roles. Keep:

- titles short and active;
- body copy left aligned by default;
- event details scannable as separate lines;
- chart labels direct;
- captions and sources visually attached to their module;
- all visible copy as native text.

Do not shrink copy to rescue an overloaded page. Shorten, remove, or split into a poster series.

## Hard avoids

Avoid generic card grids, dashboard chrome, pills, badges, detached swatches, sticker outlines, random dots, title underlines, decorative sidebars, repeated icons, glossy 3D, heavy shadows, curled paper, dense scrapbooking, generic commercial CTAs, multiple bright hues, and a full-page generated image.
