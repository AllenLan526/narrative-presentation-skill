# Canva Editability and Production Routes

Use this reference to choose a route and make accurate editability claims.

## Route table

| Route | Best for | Strength | Important limit |
|---|---|---|---|
| Canva generation | One-off poster, rapid art direction | Produces editable Canva design candidates | Object structure is generated, not deterministic; audit after creation |
| Brand Template + Autofill | Series, campaigns, localization, recurring reports | Stable layout with text/image/chart data fields | Requires an existing fillable template; Enterprise is generally required; chart fields may be preview |
| Canva Apps SDK | Custom poster builder, deterministic modules | Native text/rect/shape/group CRUD and unlocked groups | Requires building and shipping a Canva app; it is not the same as MCP design editing |
| Modular SVG + vector PDF | Canva unavailable or another editor preferred | Named groups, live vector paths, live text, portable source | PDF editors vary in how they expose groups and fonts; SVG remains the rebuild source |
| Semantic HTML + browser PDF | Complex typography, repeated modules, exact DOM measurement | Live text, CSS/SVG modules, browser geometry checks, reliable print rendering | HTML is the canonical editable source; PDF editor grouping may differ |
| Import | Existing PPTX/PDF/AI/PSD/office artwork | Useful migration fallback | Import success does not guarantee clean element hierarchy; SVG upload usually behaves as an asset/compartment |

## Element contract

Classify every planned object:

- `native_text`: editable text content and formatting in Canva.
- `native_shape`: editable rect, line, path, or other Canva shape.
- `native_chart`: Canva chart backed by structured data.
- `native_group`: unlocked group whose children remain individually selectable.
- `swappable_fill`: one image/video fill intended to be replaced without disturbing the layout.
- `single_vector`: one SVG-like compartment; scalable, but do not imply mark-level Canva editability.
- `fixed_raster`: one bitmap compartment; reserve for photography or intentionally raster texture.

The poster must not use `fixed_raster` or `single_vector` for the whole page.

## Modular vector fallback

When Canva is disabled or the user prefers another editor:

1. Author one SVG with stable `id` values for semantic groups and separate `<text>`, shape, and image elements.
2. Keep photos as linked or embedded image compartments with explicit bounds; never rasterize the entire page.
3. Use installed fonts or convert only display lettering to paths when font portability outweighs text editing. Keep body and data text live.
4. Produce a vector PDF derivative from the same plan for Acrobat, Illustrator, Affinity, Inkscape, or comparable PDF/vector editors.
5. Inspect the PDF render, but treat the SVG and plan as the canonical modular source.
6. Deliver a separate provenance file; keep design-method citations off the poster face.

Prefer the HTML variant of this fallback when layout depends on measured web fonts, wrapping, shared transforms, or component reuse. Preserve an SVG variant when interchange with vector editors matters.

## Canva MCP generation workflow

1. Call `generate-design` with `design_type: poster` and a complete brief.
2. Display every candidate preview.
3. Have the user select a candidate unless the user explicitly delegated selection.
4. Call `create-design-from-candidate` with the exact job and candidate IDs.
5. Return `design_summary.urls.edit_url` immediately.
6. Retrieve design metadata/pages/content for a lightweight audit when useful.

Generation candidates are previews, not design IDs. Do not call design-reading or editing tools on a candidate URL.

## Canva MCP editing limits

The editing transaction can change existing text, text formatting except font family, media fills, positions, sizes, autofill field labels, and design title. It cannot add a new text box, add/restyle native shapes, change backgrounds, group/ungroup, change opacity, edit animation, or add/reorder pages.

Therefore:

- solve hierarchy during generation or template creation;
- never promise to repair a flattened design with MCP edits;
- use an explicit start -> perform -> preview -> approval -> commit sequence;
- cancel inspection-only transactions.

## Brand Template + Autofill workflow

1. Search fillable brand templates and show the previews.
2. Let the user choose the template.
3. Query its dataset and use exact case-sensitive field names.
4. Map source fields to `text`, `image`, or `chart` fields.
5. Upload only user-authorized/public or directly supplied assets.
6. Autofill one design at a time; omit fields that should retain defaults.
7. Return the edit link and a mapping manifest.

Prefer stable field names such as `TITLE`, `SUBTITLE`, `HERO_IMAGE`, `CHART_DATA`, `CHART_FINDING`, `SOURCE`, and `CTA`.

## Canva Apps SDK route

Use the Design Editing API when deterministic creation is the product requirement. It supports native text, rect, custom shape, group, and embed elements on absolute pages. Build a page from a plan in one batch and sync once. Keep groups unlocked so users can edit children. App elements are custom re-editable units controlled by their creating app, but they are locked groups and are not a substitute for ordinary ungroupable poster modules.

Use native groups for visual compartments. Use app elements only when a special module must preserve app-owned metadata and re-render through the app.

## Honest handoff language

Use precise statements:

- “Title, labels, and footer are live Canva text.”
- “The photo is one swappable image fill.”
- “The illustration remains one SVG compartment; its internal paths were not verified as separately editable.”
- “The chart is a Canva chart with a data field.”

Avoid “everything is editable” unless every planned module has been inspected at the promised level.

## Primary sources

- [Canva Design Editing API](https://www.canva.dev/docs/apps/design-editing/)
- [Canva elements](https://www.canva.dev/docs/apps/elements/)
- [Canva grouping elements](https://www.canva.dev/docs/apps/grouping-elements/)
- [Canva app elements](https://www.canva.dev/docs/apps/creating-app-elements/)
- [Canva Autofill guide](https://www.canva.dev/docs/connect/autofill-guide/)
- [Canva design edit handoff](https://www.canva.dev/docs/mcp/workflows/design-edit/)
