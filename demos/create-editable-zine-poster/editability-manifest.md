# Demo Editability Manifest

Target editable construction:

| Module | Target class | Editing expectation |
|---|---|---|
| Paper field | Native shape | Recolorable background object |
| Eyebrow, title, subtitle | Native text | Independently rewritable and format-editable |
| Vermilion seam | Native shape | One movable/recolorable path with no decorative branches |
| Exploded layer stack | Unlocked native group | Each band and label independently selectable |
| Module ledger | Unlocked native group | Each row and label independently selectable |
| Action line | Native text | Independently rewritable |
| Edition marker | Native text | Independently rewritable |

No full-page bitmap, generated lettering, raster chart, or baked-in footer is permitted. `design-as-layers.html` is the canonical measured rendering source: text remains live HTML, shapes remain separate SVG nodes, and stable `data-module-id` values preserve the module map. `design-as-layers.svg` is the parallel vector-interchange source. The PDF is printed directly from the HTML DOM, not from a screenshot, so text and vector geometry remain editable in capable PDF editors. `build_pdf.py` remains a direct-PDF fallback.

Before export, `render_html.cjs` waits for fonts, measures the rendered DOM, and rejects text/shape collisions, insufficient inset clearance, transform mismatches, and page overflow. Design-system and production credits live only in `credits-and-sources.md`, not on the poster face.

- Accent: `#E4472E`
- Paper: `#F3EFE6`
- Ink: `#1C1B1A`
