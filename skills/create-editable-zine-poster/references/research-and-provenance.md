# Research and Provenance

This skill adapts the user-supplied `zine-anchor-deck` system: one source-derived anchor, one governing message, independently named compartments, active quiet space, strict spacing tiers, source-first planning, honest charts, and creator-credit separation. It translates the slide sequence into a one-page reading path while preserving element-level separation.

## Canva findings

- Canva defines elements as containers for content and supports text, images, groups, shapes, tables, rich text, and videos.
- The Design Editing API can read and edit page ingredients and can create native text, rect, custom shape, and group elements on supported absolute pages.
- Ordinary unlocked groups let users manipulate the group and still edit individual children.
- App elements are custom re-editable elements controlled by their creating app, but behave as locked groups and have a separate lifecycle.
- Brand Template Autofill supports text, image, chart, and sheet data fields; Enterprise access is generally required and some field types are preview.
- Canva MCP generation yields candidates that must be converted to a design before other design tools can use the design ID.
- Canva's handoff guidance requires a direct edit URL after design-touching work.

Primary sources:

- [Canva Design Editing API](https://www.canva.dev/docs/apps/design-editing/)
- [Canva elements](https://www.canva.dev/docs/apps/elements/)
- [Canva grouping elements](https://www.canva.dev/docs/apps/grouping-elements/)
- [Canva app elements](https://www.canva.dev/docs/apps/creating-app-elements/)
- [Canva Autofill guide](https://www.canva.dev/docs/connect/autofill-guide/)
- [Canva Autofill job reference](https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/)
- [Canva MCP handoff](https://www.canva.dev/docs/mcp/workflows/design-edit/)

## Open-source poster and chart findings

- [PosterLLaVA](https://github.com/posterllava/PosterLLaVA) frames poster generation as layout plus editable SVG output, but its announced PosterGen pipeline should not be treated as a production dependency without verifying the current code release and license.
- [Grid2Poster](https://github.com/open-energy-transition/grid2poster) separates data preparation, theme configuration, named paper sizes, metadata, and vector/raster output. Reuse the architectural pattern, not its maps or styling assets.
- [Observable Plot](https://github.com/observablehq/plot) uses layered marks and scales, useful for decomposing data scenes into native Canva marks. Its repository declares the ISC license.
- [RAWGraphs](https://rawgraphs.github.io/rawgraphs-core/docs/workflow/) separates data, chart model, variable mapping, visual options, and export. This separation directly informs the data-module contract.
- [Charticulator](https://donghaoren.org/charticulator/docs/reusing-charts.html) treats bespoke charts as reusable templates that can accept new datasets and export SVG.

SVG is a transfer format, not an editability guarantee inside Canva. Do not copy code, templates, artwork, or datasets into a deliverable without reading and recording the applicable license.
