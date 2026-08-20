# Editable Data Modules

Use one chart per independent conclusion. Treat a chart as evidence inside the poster's narrative, not as a dashboard tile.

## Choose the construction route

1. Use a Canva chart data field in an autofillable Brand Template for repeatable, data-swappable posters.
2. Use a native Canva chart for a one-off when the editor exposes the needed chart type.
3. Use native shapes plus live labels for small bars, dots, unit fields, timelines, or annotated comparisons.
4. Invoke `$scientific-figure-making` for publication-ready static Matplotlib bars, trends, scatterplots, heatmaps, or multi-panel figures. Export SVG or PDF plus a high-DPI fallback when required.
5. Use one SVG chart compartment only for other complex geometry that cannot reasonably be rebuilt. Keep title, labels, units, finding, and source native outside it.

Canva chart Autofill accepts structured tabular rows and has documented row/column limits; treat the capability as preview where Canva marks it preview. Query the current template dataset before filling it.

Do not invoke `$scientific-figure-making` for interactive web visualization, exploratory-only analysis, dominant 3D/GIS work, or Illustrator/Figma-first infographics. For its route, retain source data and Matplotlib code, import the export as one `single_vector` module, and rebuild from source rather than editing marks after export.

## Selection rules

- Bars: magnitude comparison; keep a zero baseline.
- Dots: precise comparison with less ink.
- Lines: change across ordered time.
- Unit fields: countable part-to-whole or accumulation.
- Small multiples: repeated comparison using a shared scale.
- Flow/network: only when connections are the finding.
- Map: only when spatial location is explanatory.

Reject a candidate when it distorts the data, leaves insufficient label room, adds unnecessary color categories, or reads too slowly for the poster setting.

## Data contract

Record:

- finding;
- data source and retrieval date;
- fields, types, units, and time range;
- transformation and filters;
- chosen visual encoding;
- color semantics;
- native construction class;
- fallback when the Canva route cannot represent it.

For a scientific figure, also record `construction_route: scientific-figure`, `source_data`, `source_code`, `publication_target`, and `export_formats` containing `svg` or `pdf`.

Use deterministic data in demos. Label invented values `Illustrative data` and do not cite them as findings.

## Open-source pattern library

Borrow systems, not screenshots:

- [Observable Plot](https://github.com/observablehq/plot) demonstrates layered marks and small-multiple composition; its repository is ISC licensed.
- [RAWGraphs](https://rawgraphs.github.io/rawgraphs-core/docs/workflow/) separates data loading, visual-model selection, mapping, options, and open-vector export.
- [Charticulator](https://donghaoren.org/charticulator/docs/reusing-charts.html) demonstrates reusable bespoke chart templates and SVG export.
- [Grid2Poster](https://github.com/open-energy-transition/grid2poster) demonstrates print-size tokens, theme separation, cached data preparation, and SVG/PDF/PNG poster outputs.

Open-vector output is useful for transfer, but it does not by itself guarantee Canva-native mark editability. Rebuild marks as native objects when that promise matters.
