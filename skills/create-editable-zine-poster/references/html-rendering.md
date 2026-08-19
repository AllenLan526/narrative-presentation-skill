# HTML Rendering Route

Use semantic HTML/CSS when browser layout measurement is more reliable than hand-calculated PDF geometry.

## Source contract

- Create one fixed-size `.poster` page with `data-document-role="page"` and stable `data-module-id` values.
- Keep every visible text item as HTML text and every vector visual as CSS/SVG. Do not use a full-page canvas or bitmap.
- Use one semantic element per compartment and one shared wrapper for each owned text-on-shape module.
- Apply transforms to the owning wrapper, not independently to its background and text children.
- Store spacing, colors, dimensions, and type sizes as CSS custom properties.
- Add print CSS with an explicit page size, zero browser margins, exact colors, and disabled animation.

## Browser measurement gate

After loading the local page in a real browser:

1. Wait for `document.fonts.ready`.
2. Measure text and exclusion zones with `getBoundingClientRect()` and line fragments with `Range.getClientRects()` when wrapping matters.
3. Expand unrelated text rectangles by the required clearance and reject intersections.
4. For owned text-on-shape modules, compare the union of rendered text ink with the visible safe interior. Check shared transform, minimum insets, opposing-side ratios, and text-stack height.
5. Check `scrollWidth <= clientWidth` and `scrollHeight <= clientHeight` for every text module.
6. Check the full page for overflow beyond the declared canvas.
7. Capture a full-page PNG and inspect it at full size.
8. Print to PDF with backgrounds enabled and inspect the rendered PDF again.

Expose the audit as a deterministic page function such as `window.posterAudit()` and fail the build when it returns any errors.

## PDF output

Use Chromium print output when it preserves text and SVG as vectors. Set page width/height explicitly and enable background graphics. Treat HTML as the editable source of truth because PDF editors may reinterpret DOM groups.

Do not use screenshot-to-PDF. A PNG preview is for QA only.
