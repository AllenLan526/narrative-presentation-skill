# Narrative Presentation and Poster Skills

A public collection of editorial narrative-design skills for presentations and one-page posters. Both systems use a clear visual anchor, active quiet space, independently editable compartments, explicit spacing contracts, and separate creator-credit manifests.

## Skills

- [`skill/`](skill/) — `$zine-anchor-deck`, the original presentation skill. Its implementation ID and legacy path remain unchanged for compatibility.
- [`skills/create-editable-zine-poster/`](skills/create-editable-zine-poster/) — `$create-editable-zine-poster`, a one-page poster skill with Canva, semantic HTML/CSS, modular SVG, and editable vector-PDF routes.

## Demonstrations

- [`demo/`](demo/) — the original eight-slide interactive HTML and editable PPTX demonstration.
- [`demos/create-editable-zine-poster/`](demos/create-editable-zine-poster/) — an editable HTML/SVG poster, browser-generated vector PDF, validated poster plan, rendering source, preview, and separate provenance file.

Open `demo/index.html` directly in a modern browser. Use the arrow keys or spacebar to move between slides and `F` for fullscreen.

Open `demos/create-editable-zine-poster/design-as-layers.html` directly to inspect the poster. To rebuild its preview and PDF, install the demo dependency and run `npm run render` inside that directory.

## Design principles

- One persistent visual 锚点 that changes state as the argument develops.
- Scene compartments remain independently selectable and animatable.
- Text placement follows an 8 px spacing system and rendered-ink clearances.
- Normal text targets at least 4.5:1 contrast; small metadata targets 7:1 where practical.
- Quantitative scenes preserve their declared Lieflat template and data contract.
- Publication-ready static chart requests route to `$scientific-figure-making`; template-led narrative or interactive chart scenes remain with `$lieflat-charts`.
- HTML supports reduced motion; PPTX documents honest static fallback behavior.
- Posters retain live type, named modules, separately editable vector geometry, and a single clear visual route.
- Poster credits and design-method sources remain outside the poster face.

## Validation

The included demo passed:

- browser console, scene-ID, motion, and narrow-viewport overflow checks;
- full-slide and contact-sheet visual inspection;
- exported PPTX rendering inspection;
- PowerPoint canvas-overflow validation.
- poster-plan schema validation and rendered DOM collision, inset, transform, and overflow checks;
- PDF object inspection confirming live text/vector content rather than a full-page screenshot.

## Credits and provenance

This project intentionally keeps creator credit visible and machine-readable. See [AUTHORS.md](AUTHORS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the complete ledger.

Key contributors and source systems include **@Zeejay0**, **Moxt**, **larashero3-dotcom**, **JetBrains/OpenAI**, **Alfonso Graziano**, **siril9**, **Gabberflast**, **GreenSock**, **Rasmus Andersson**, and **OpenAI**.

## Licensing

This repository uses mixed licensing because the demonstration incorporates components with different terms. See [LICENSE.md](LICENSE.md) before reuse, especially for Lieflat-derived chart material, which is identified as PolyForm Noncommercial 1.0.0.
