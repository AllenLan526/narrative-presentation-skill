# Data Scene Routing

Choose one primary engine per finding:

| Need | Route |
|---|---|
| Publication-ready static bars, trends, scatterplots, heatmaps, or multi-panel figures | Invoke `$scientific-figure-making` |
| Template-led narrative data illustration or interactive relationship view | Invoke `$lieflat-charts` |
| Simple chart whose marks must remain editable in PPTX/Slides | Use native chart objects when the encoding stays faithful |

Do not invoke `$scientific-figure-making` for interactive web visualization, exploratory-only plots, dominant 3D/GIS work, or Illustrator/Figma-first infographics. Do not invoke `$lieflat-charts` merely to restyle a scientific figure.

## Scientific figure route

- Open only the relevant `$scientific-figure-making` reference for the requested figure family.
- Preserve the canonical data and Matplotlib source beside the deck rebuild source.
- Export SVG or PDF for vector placement and a high-DPI PNG only when the target format needs a raster fallback.
- Place the figure as one named scene compartment. Keep slide-level title, finding, source, and optional annotation native when that avoids duplicated labels.
- Rebuild from the figure source instead of editing exported marks by hand.
- Treat a static scientific figure as static in HTML; choose another route if hover, filtering, or live data is required.
- Record a `figure_contract` with the finding, figure type, publication target, source data, source code, and export formats.

## Lieflat route

Read the original `$lieflat-charts` skill before building a Lieflat chart. The remaining guidance explains how to place it inside a zine-anchor deck.

## Route

Use chart mode by default. A deck slide, PPT illustration, or evidence graphic is not a Lieflat report. Enter report mode only for an explicitly requested annual report, monthly report, white paper, one-page research brief, poster, notebook, or dashboard report delivered as its own narrative page.

## Template Selection

For each independent finding:

1. Determine the data shape and visual channels that can encode it honestly.
2. Compare at least three candidates across Lupi Editorial L1–L15 and Lupi Basics F1–F13, or all candidates when fewer exist.
3. Prefer the candidate that best preserves semantic truth, label room, expected reading speed, narrative force, and batch variety.
4. Use Glance G1–G18 only after recording why Lupi and Basics fail, or when the user explicitly requests dashboard/monitoring/weekly-report speed.
5. Use Interactive templates for dense networks, paths, or flows that genuinely require hover or pinning.
6. Record `template_id`, `gallery_file`, `card_title`, `candidate_audit`, and any shortfall reason in `chart_contract`.

Always begin with the real gallery card and matching render block. Preserve its encoding, geometry, proportion, and animation rhythm. Color samples are palettes, never structural sources.

## Color Reconciliation

Lock one system for the full deck:

- `mono` for high density or when color has no stable meaning;
- `porcelain` for ordered or single-series cool data;
- `palm` for up to four unordered categories, with five or six only when still legible;
- `wire` for grayscale data with one controlled hero;
- `custom` only when the user supplies brand colors or explicit values.

If the zine anchor hue matches a real data role, map it to `HERO`. Otherwise keep the chart semantically correct and express the anchor through contour, torn seam, position, or motion. Never add a decorative color to a chart.

## PPTX Translation

- Generate and validate the chart from its original Lieflat template first.
- Prefer SVG for placement in PPTX; preserve selectable native labels outside the SVG when useful.
- Name the chart group with the scene ID and preserve its source/template metadata in speaker notes.
- Use native PowerPoint objects only when the chart can match the template's geometry and data mapping; visually compare both versions.
- Animate the chart as one compartment by default. Split into data layers only when the selected template's reveal order can be preserved.
- Convert hover/pin behavior into explicit static labels, presenter builds, or an HTML companion; never imply it remains interactive.

## HTML Translation

- Keep the gallery's actual SVG/Canvas/ECharts structure.
- Use the template's `obsReveal` behavior when sufficient.
- If GSAP coordinates the wider slide, drive the compartment wrapper and let Lieflat own internal data marks, or disable one system explicitly. Never double-animate the same property.
- Preserve click replay, timer cleanup, and `prefers-reduced-motion`.

## Data Integrity

- Never break a bar axis.
- Use radius proportional to `sqrt(value)` for area encoding.
- Do not add hover to marks with no underlying record.
- Use deterministic demonstration data, never `Math.random()`.
- Keep titles conclusion-led and include units, time range, and source.
- One chart must carry one independent conclusion; remove repeated evidence instead of filling space.
