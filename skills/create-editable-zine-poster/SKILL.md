---
name: create-editable-zine-poster
description: Create, art-direct, audit, or systematize editorial zine-style posters with independently selectable text, shapes, images, charts, and scene modules. Use Canva when it is the preferred editor; otherwise use semantic HTML/CSS, modular SVG, or editor-friendly vector PDF. Use for posters, flyers, infographics, event graphics, research posters, data posters, reusable templates, poster series, or adapting a slide/deck visual system into a single-page composition without flattening the page into one image.
---

# Create Editable Zine Poster

Build a one-page narrative system, not a slide squeezed onto portrait paper. Preserve the source deck's anchor, quiet-space, compartment, data-integrity, and spacing logic while translating every useful part into a Canva-native or explicitly swappable module.

## Start with an editability gate

Confirm the preferred editor or output. Infer the poster size, audience, goal, content, brand kit, and reuse needs when they are clear. Ask only for a missing choice that materially changes the result. If Canva is unavailable or unnecessary, continue with modular SVG and vector PDF; do not block the task on Canva.

Choose the production route before composing:

1. **Canva generation:** Use for one-off posters and fast visual exploration. Generate a `poster`, show all candidates, create the selected candidate, and hand off its edit link.
2. **Brand Template + Autofill:** Use for repeatable series or content swaps. Require a user-selected autofill-capable template; inspect its dataset before mapping text, image, and chart fields. Note that Autofill generally requires Canva Enterprise and chart fields may be preview features.
3. **Canva Apps SDK:** Use only when the user wants a custom Canva app or deterministic object construction. Build native text, rect, shape, and unlocked group elements through the Design Editing API. Do not claim the Canva MCP editing transaction can create arbitrary shapes or text boxes.
4. **Modular vector fallback:** Use when Canva generation/import is disabled or another editor is preferred. Keep named SVG groups and live text as the source of truth; create a vector PDF derivative for PDF editors and state any font substitution risk.
5. **HTML renderer:** Prefer semantic HTML/CSS as the source when browser font measurement, wrapping, transforms, or repeated modular components will be more reliable than direct PDF drawing. Render with a real browser and preserve live DOM text, SVG shapes, and stable module IDs.

Read [references/editability-and-canva-routes.md](references/editability-and-canva-routes.md) whenever route selection, template reuse, imports, or post-generation editing matters.

## Write the poster contract

Create `poster-plan.json` before generating or editing. Read [references/poster-plan-contract.md](references/poster-plan-contract.md), then validate:

```bash
python3 "$SKILL_DIR/scripts/validate_poster_plan.py" poster-plan.json
```

Make the plan resolve content and editability before decoration:

1. State one governing message and one intended viewer action.
2. Choose one visual anchor derived from the subject, not a pasted logo.
3. Define one dominant scene and no more than five supporting modules.
4. Give every module a stable ID, owner group, z-order, bounds, alt text, source note, and editability class.
5. Define one spacing system and record any intentional exception.
6. Put exact copy, data, units, and citations in the plan. Keep generated artwork text-free.
7. Record creator/tool/license provenance separately from claim and asset citations. Keep design-system, skill, and production credits off the poster face unless the user explicitly requests a visible colophon; deliver them in a separate provenance file.

## Non-negotiable text-shape collision gate

Treat every anchor, decorative shape, image subject, chart mark, crop edge, and high-contrast mass as a text exclusion zone. Before rendering, measure each text module from its expected rendered ink bounds, expand that rectangle by `min_text_image_clearance`, and test it against every unrelated exclusion zone. A positive-area intersection is a build error, not an aesthetic judgment.

Allow overlap only when the text and shape form one intentional owned module, such as white text on its own red label band. Record the owning relationship and an explicit `collision_exemption`; never exempt a slide-wide or poster-wide anchor merely because the text remains technically readable.

Resolve collisions in this order: wrap or shorten copy, reduce the text field width, move the shape or crop, reroute the anchor, then reduce type size only if the reading hierarchy survives. Do not solve the problem by changing z-order, adding transparency, or putting the text above the shape: those approaches still leave the words visually covered.

For SVG/PDF/code routes, keep drawing order consistent with the plan's `z` values and run the plan validator before export. After export, inspect the rasterized page at full size because font metrics and substitutions can make a geometrically safe source collide in the render.

For HTML routes, read [references/html-rendering.md](references/html-rendering.md). Wait for `document.fonts.ready`, run the DOM geometry audit, then capture a full-page preview and print to PDF with backgrounds enabled. The DOM audit complements the plan validator; it does not replace visual inspection.

### Owned text-on-shape modules

When text intentionally sits on a band, label, panel, or other shape, transform the shape and its text as one group. Never slant or rotate the background while leaving its text unrotated. Either apply the same rotation to every child or keep the text-bearing portion of the shape level.

Measure internal padding from rendered text ink to the visible shape boundary at that line, not to the shape's rectangular bounds. Keep left/right padding and top/bottom padding optically balanced; each opposing-side ratio must stay at or below 1.5 by default. Keep the full text stack at or below 70% of the usable shape height. If the copy cannot satisfy those limits, widen the shape, shorten the copy, reduce hierarchy-preserving type sizes, or split the module.

Record every owned module in `owned_text_shape_contracts` with shape/text rotations, shape and text-stack heights, and four measured padding values. The validator must reject rotation mismatches, insufficient padding, excessive text scale, and badly unbalanced opposing margins.

Rebuild from the plan after fixes. Do not patch a flattened export as the main workflow.

## Translate the zine system to one page

Read [references/poster-visual-system.md](references/poster-visual-system.md) before art direction.

Preserve this relationship:

```text
truth or evidence -> source-derived abstraction -> one structural hue -> tactile boundary -> active quiet space
```

Use one exact accent hue, one neutral ink family, one paper/background family, and one anchor geometry. Let the anchor organize the page by becoming a seam, path, aperture, contour, or recurring relation. Keep 55–80% of the page visually quiet unless the content genuinely demands a dense information poster.

Keep the anchor visually economical. Prefer one continuous axis or contour. Do not add side branches, connector tabs, rays, flourishes, or repeated accent marks merely to make modules feel connected. Add a secondary anchor segment only when it communicates a necessary relationship that position, alignment, or spacing cannot communicate. If the reading order remains clear after removing it, remove it.

Flatten narrative sequence, not layers: the poster may read opening -> evidence -> implication -> action from top to bottom or along the anchor, but its objects must remain separate.

## Build editable modules

Use one group per semantic compartment and keep its children independently editable. Prefer these module families:

- `title-stack`: eyebrow, title, subtitle, and date as separate live text elements;
- `anchor`: preferably one native shape or contour; use additional unlocked pieces only when each carries indispensable meaning;
- `truth-scene`: a swappable image frame plus a separate torn edge, tint, caption, and credit;
- `distilled-scene`: native shapes when simple; otherwise one swappable text-free illustration with native labels outside it;
- `data-scene`: one conclusion-led chart, native labels, unit, source, and optional annotation;
- `action-block`: one direct instruction or event detail set, never commercial CTA chrome;
- `colophon`: compact creator credits and asset/data sources.

Apply this editability hierarchy:

1. Canva-native text, shapes, lines, and charts.
2. Unlocked Canva groups containing native children.
3. Swappable image fills for photographs or irreducibly textured illustration.
4. A single SVG/bitmap compartment only when native reconstruction is disproportionate.
5. Never one full-page raster, screenshot, or imported visual that makes the entire poster one object.

Generated art must contain no titles, captions, labels, chart axes, legends, or logos. Recreate them as Canva text or chart elements.

## Handle charts as evidence

Read [references/data-modules.md](references/data-modules.md) whenever quantitative information appears.

- Give each chart one independent conclusion.
- Choose the encoding from the data shape; do not imitate an attractive chart from memory.
- Prefer Canva chart fields for repeatable templates; otherwise use a native Canva chart or a small group of shapes and live labels.
- Keep units, time range, source, and annotations as separate text elements.
- Preserve zero baselines for bars and square-root scaling for area marks.
- Use deterministic demo data and mark it clearly as illustrative.
- Treat exported SVG as a swappable chart compartment, not proof that every mark is independently editable in Canva.

## Prompt Canva generation precisely

For `Canva:generate-design`, use `design_type: "poster"` and include the complete brief on every iteration. Specify:

- exact copy and reading order;
- portrait or landscape intent and print/social use;
- module names and approximate regions;
- one dominant composition, anchor identity, paper, neutral ink, and exact accent;
- which items must remain live text, native shapes, chart/data modules, or swappable image frames;
- the quiet-space target and spacing tiers;
- the prohibition on generated text inside imagery, flattened full-page artwork, dashboard cards, decorative stickers, random dots, gloss, heavy shadows, and generic CTA styling;
- accessibility, source-note, and colophon needs.

Show the candidate previews. Convert the user's chosen candidate with `Canva:create-design-from-candidate`, then return its direct edit URL. A candidate is not yet a saved Canva design.

## Edit safely

For an existing design, invoke `$canva:canva-edit-design` and follow its transaction protocol. The MCP editor can replace or format existing text, update media fills, move or resize elements, and update the title, but it cannot create new text boxes, restyle shapes, change font families, change backgrounds, group/ungroup, or add/reorder pages. Structure those features correctly during generation or template construction.

Never commit an editing transaction without the required explicit approval. If inspecting through a transaction without edits, cancel it.

## Quality gate

Before delivery:

1. Open the created design or retrieve its pages/content and inspect the full poster at print size and thumbnail size.
2. Verify the governing message reads in three seconds and the complete path reads in fifteen.
3. Confirm all visible copy is live text and no generated image contains accidental lettering.
4. Confirm the anchor, title, image, chart, captions, credits, and action block are separate modules.
5. Verify groups remain unlocked and children selectable where the route supports groups.
6. Check margins, title reserve, peer-gap consistency, text-to-image clearance, and intentional exceptions.
7. Compare rendered text ink against every shape/image/chart exclusion zone. Reject any unapproved intersection, tangent, or clearance below the declared minimum; checking only text-box bounds is insufficient.
8. For every text-on-shape module, verify shared rotation, balanced opposing insets, and text-stack scale against its `owned_text_shape_contract`.
9. Verify chart encodings, units, labels, data, and sources.
10. Check contrast, minimum type size for the final physical/social size, crop safety, and alt text.
11. Confirm creator credits, licenses/terms, citations, and asset sources are distinct and traceable.
12. Return the Canva edit link first; static exports are optional derivatives, never the editable handoff.

Do not claim element-level editability merely because an export is SVG or because a design opens in Canva. State any compartment that remains a single imported or raster element.

## Deliverables

Return:

- the Canva edit link when Canva is used, otherwise the editable HTML and/or SVG source plus a vector PDF derivative;
- `poster-plan.json` and any data source needed to rebuild or autofill;
- a short editability manifest listing native modules and single-element compartments;
- a separate provenance/credits file; do not place design-process citations under the poster by default;
- optional PNG/PDF only when requested.

Keep scratch renders and research notes out of the final handoff.
