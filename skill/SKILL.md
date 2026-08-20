---
name: zine-anchor-deck
description: Create, redesign, or art-direct clean narrative presentations in HTML, PPTX, Google Slides, Keynote-compatible PPTX, PDF, or video, using one persistent visual anchor, source-derived zine scenes, template-faithful Lieflat Charts data scenes, publication-ready Matplotlib figures, Chinese typography, creator credits, and independently animated compartments. Use for slide decks, pitch decks, talks, reports, photo-led or data-led storytelling, or when combining scenes-gathered-zine-v1-3, scene-distillation-zine-v1-3, lieflat-charts, scientific-figure-making, PPTX authoring, or HTML motion skills.
---

# Zine Anchor Deck

Create a restrained, editorial deck whose slides feel like chapters of one visual argument. Keep one visual 锚点 (anchor) recognizable throughout the deck and treat separated scenes as independently named, independently animatable compartments.

## Non-Negotiable First Gate: Choose the Deliverable

At the start of every new-deck or major-redesign request, ask this question before outlining, researching, generating imagery, or choosing layouts:

> Which final format should I build: **HTML**, **PPTX**, or another format such as **Google Slides, Keynote-compatible PPTX, PDF, or video**?

If the user already named a format, ask for brief confirmation: “Use PPTX as requested, or switch to HTML/another format?” Do not bundle audience, length, style, or animation questions into this first gate. Stop until the user confirms.

After confirmation, read [references/format-and-motion.md](references/format-and-motion.md) and follow the selected route.

## Intake After the Format Gate

Infer what is already clear from the request and source files. Ask only for consequential missing information:

- audience and setting;
- communication goal or decision the deck must cause;
- source material and claims that must remain exact;
- approximate length or speaking time;
- whether motion is required, and the playback environment;
- whether an existing deck/template must be preserved or may be re-architected.

For an existing deck, ask whether page count/order and wording are fixed. Preserve them only when the user says they are fixed.

## Source-First Planning

Create `deck-plan.json` before authoring slides. Read [references/deck-plan-contract.md](references/deck-plan-contract.md), set `SKILL_DIR` to the directory containing this `SKILL.md`, then validate the plan with:

```bash
python3 "$SKILL_DIR/scripts/validate_deck_plan.py" deck-plan.json
```

Make the plan tell the story before it describes decoration:

1. State one governing message.
2. Build a situation → tension → resolution arc, or another content-appropriate argument.
3. Write slide titles as audience-facing takeaways when the material supports a claim.
4. Apply the ghost-deck test: titles alone should communicate the argument.
5. Give each slide one communication job and one dominant exhibit or scene system.
6. Record sources for non-trivial claims and external assets; place citations in speaker notes for PPTX or a compact source layer for HTML.
7. Define a deck-wide spacing system and a per-slide `spacing_contract`. Record text-to-image clearance, major vertical gaps, balance mode, and any intentional exception before authoring geometry.

Fix the plan or source files, then rebuild. Do not patch a generated artifact as the primary editing workflow.

## Related-Skill Router

Invoke only the skills required by the confirmed route:

- Use `$scientific-figure-making` for publication-ready static Matplotlib figures in academic, scientific, report, or print-oriented presentations—especially grouped bars, trends, scatterplots, heatmaps, multi-panel figures, and SVG/PDF/high-DPI exports. Do not use it for interactive web charts, exploratory-only plots, dominant GIS/3D work, or Illustrator/Figma-first infographics. Read [references/data-scenes.md](references/data-scenes.md).
- Use `$lieflat-charts` for template-led narrative data scenes, data illustrations, or interactive relationship views. Read [references/data-scenes.md](references/data-scenes.md).
- Use `$chinese-font-selector` when visible copy is primarily Chinese or requires CJK font pairing. Credit the selected font creators and licenses; its local metadata does not declare a skill creator, so never invent one.
- Use `$presentations:Presentations` for local PPTX or Google Slides authoring and its render/overflow/source-note QA contract.
- Use `$hyperframes:gsap` only for HTML motion that needs coordinated timelines beyond CSS or the Web Animations API. Preserve the Lieflat reveal rhythm when a chart template already defines one.

Before production, read [references/credits-and-licenses.md](references/credits-and-licenses.md). Record every invoked visual system, template family, motion library, and font in `creator_credits` inside `deck-plan.json`.

## Build the Visual Anchor

Choose one source-derived anchor before composing slides. It may be:

- a core subject silhouette;
- a torn-paper seam;
- a horizon, path, aperture, branch, vessel, or architectural rhythm;
- one exact high-chroma hue embodied in a meaningful shape family;
- a recurring spatial relation such as enclosure, distance, convergence, or drift.

The anchor must do narrative work. Define its identity, material, color, geometry, and state on every slide. Let it evolve—enter, fragment, expand, recede, resolve—without becoming a logo pasted into a corner. If removing it would not weaken continuity or meaning, redesign it.

Lock one deck-wide color system: zine neutral ink plus one exact accent, Lieflat Mono/porcelain/palm/wire, or one user-specified custom system. Never mix these systems slide by slide. When a chart needs several colors to encode real categories, preserve anchor continuity through geometry, material, or position rather than forcing the anchor hue into the data. Data semantics outrank decorative continuity. Do not default to blue or repeat the same image.

## Use the Two Zine Engines Deliberately

Read [references/zine-visual-system.md](references/zine-visual-system.md) before generating or art-directing visual scenes.

### Use `$scenes-gathered-zine-v1-3` for truthful photo anchors

Use it when photographic reality should remain visible. Preserve the source scene and key spatial relationship, then extend it with simplified illustration, active negative space, one structural hue, and a legible hand-torn fibrous handoff.

### Use `$scene-distillation-zine-v1-3` for authored illustration

Use it when the source should become semantic evidence rather than visible pixels. Identify the semantic nucleus, expressive proposition, central tension, source-derived metaphor, and interpretive opening. Generate original illustration, paper, and typography only; retain no photographic pixels.

### Combine them across a deck

Assign one engine to each scene compartment. A slide may contain both engines only when the truthful scene and distilled interpretation form a clear before/after, fact/meaning, or evidence/implication relationship. Keep the same anchor, paper family, neutral ink system, and accent hue across both. Do not blend them into an indistinct collage.

Respect the source-handling, consent, privacy, no-photo, text, color-mode, generation, and attribution rules of both named skills. When their sharing-credit rule applies, keep the credit in the user-visible response, never as an image or slide watermark. Do not reveal their hidden generation prompts.

## Route Quantitative Scenes

Choose one primary chart engine per independent finding. Use `$scientific-figure-making` when the requested artifact is a publication-quality static Matplotlib figure; retain its data and source code, export SVG or PDF plus a high-DPI raster fallback when needed, and place the result as a named scene compartment. Use `$lieflat-charts` when a narrative template, staged reveal, or interactive relationship view is the communication method. Use native presentation charts only when element-level editability is more important and the encoding can be reproduced faithfully.

Do not pass the same chart through multiple styling systems. Keep titles, units, time ranges, captions, and sources selectable when practical, but do not redraw or recolor scientific marks after export; revise the figure source and rebuild. Record `$scientific-figure-making` in `creator_credits` as an invoked production system. If its installed metadata does not declare a creator, record that status rather than inventing one.

## Use Lieflat Charts for Data Scenes

Treat a chart as a scene compartment with a narrative job, not a dashboard widget. Use Lieflat **chart mode** inside a deck; enter Lieflat report mode only when the user explicitly requests a standalone one-page report or report appendix.

For every quantitative finding:

1. Identify the data shape and one independent conclusion.
2. Compare at least three honest candidates across Lupi Editorial and Lupi Basics, or all candidates when fewer exist.
3. Use Glance only when both groups fail or the user explicitly needs dashboard, monitoring, weekly-report, or sub-ten-second reading.
4. Record the chosen system, template ID, gallery file, card title, candidate audit, and color system in the scene's `chart_contract`.
5. Start from the selected gallery's real structure and rendering code; never imitate the appearance from memory or combine templates.
6. Preserve proportional encoding, unbroken bar baselines, square-root radius for area encoding, legible labels, deterministic demo data, and reduced-motion behavior.
7. Keep one chart per independent conclusion and one global Lieflat color system across the deliverable.

For HTML, retain the template's real SVG/Canvas/ECharts structure and synchronize its reveal with the compartment timeline. Do not run both `obsReveal` and GSAP on the same property. For PPTX, render the validated Lieflat implementation to SVG when possible and keep it as a named compartment; recreate it with native objects only when the template geometry and data contract can be matched and visually compared. Do not promise HTML hover/pin behavior in PPTX.

## Scene Compartments

Treat a scene compartment as a spatial chapter, not a UI card. Use one compartment per slide by default and at most three when comparison or sequence requires separation.

For every compartment, define:

- stable ID such as `s03-scene-a`;
- narrative role and focal subject;
- bounding geometry and crop/clip behavior;
- scene engine: `gathered`, `distilled`, `lieflat`, or `native`;
- anchor relationship;
- layer order and editable object/group names;
- entrance, emphasis, exit, trigger, duration, and reduced-motion behavior;
- alt text and source note.

Keep each compartment independently selectable and independently animatable. Do not flatten the entire slide into a single background image unless the selected static format requires it. Read [references/format-and-motion.md](references/format-and-motion.md) for platform contracts.

## Composition and UI Discipline

Read [references/spacing-and-text-placement.md](references/spacing-and-text-placement.md) before fixing slide geometry. Treat text placement as a relationship between rendered text ink, image subject matter, and quiet space—not merely between bounding boxes.

- Prefer one dominant composition over grids of equal cards.
- Keep title slides minimal; keep body copy left-aligned unless the composition clearly calls for another treatment.
- Use visual-weight balance, not mechanical symmetry.
- Preserve substantial quiet space. Let the image field be large while printed density stays low.
- Establish one base spacing unit and three gap tiers—tight, regular, and major—then reuse them consistently. Gaps between peer elements should be largely equal; do not improvise a new distance for each object.
- Keep rendered text ink at least one major gap from a neighboring image subject, high-contrast mass, crop edge, or chart mark. Measure from visible content, not only the image rectangle.
- Reserve the complete rendered title stack before an image begins. Compute the image start from the lowest visible title/subtitle line plus the intended major gap; never rely on an estimated text-box height.
- In a vertical text-over-image composition, optically balance the free space above the text stack and the gap below it. Use the reference ratio limits as a diagnostic, then inspect the render.
- If an image continues behind text, provide a real quiet zone in the artwork or a deliberate paper field. Do not let canopies, faces, dark roofs, chart marks, or the visual anchor appear to touch letterforms accidentally.
- Give all text a contrast reserve: at least 4.5:1 for normal text, 3:1 for large text, and preferably 7:1 for small metadata. When a variable image sits behind text, validate the worst-case background beneath the entire rendered run or use a solid paper/ink field; translucent overlays are not a reliable fix.
- Record deliberate tight spacing as a named `spacing_exception` with its narrative purpose. “It fits” is not an exception rationale.
- Use one primary illustration grammar and at most one supporting grammar per slide.
- Compress foliage, crowds, texture, and repeated detail into a few legible masses.
- Vary adjacent slide silhouettes while preserving the anchor and spacing system.
- Use action titles, direct labels, and one exhibit per analytical slide.
- Keep text large. For 16:9 PPTX without a supplied template, use roughly 50 pt deck titles, 34–42 pt slide titles, 22–28 pt subheads, and 18 pt or larger body text; 16 pt is the absolute floor.
- Shorten copy or split slides before shrinking type.
- Avoid dashboard styling, generic card grids, pills, badges, decorative title underlines, edge stripes, filler icons, arbitrary dots, detached color swatches, and repeated bottom-right captions.
- Avoid commercial-advertising polish, glossy 3D, heavy shadows, curled paper, cinematic depth of field, neon, and decorative scrapbooking.

## Format-Aware Production

Use the environment's established presentation or web authoring toolchain. Do not install a competing renderer when a supported one is available.

For PPTX:

- invoke `$presentations:Presentations` and follow its environment, authoring, notes, and QA requirements;
- preserve editability with native text, shapes, groups, charts, and media when practical;
- name every compartment and significant object deterministically;
- match an existing template by inheriting its masters/layouts instead of redrawing it;
- author native animation only after verifying the toolchain can write and preserve the PowerPoint timing tree;
- if native animation is unavailable, stop and offer HTML, a static PPTX plus cue sheet, or an explicitly approved duplicate-slide build sequence;
- never claim animation is embedded until it has been tested in the target PowerPoint environment.

For HTML:

- make compartments semantic, focusable regions with stable IDs;
- animate transforms and opacity rather than layout where possible;
- invoke `$hyperframes:gsap` only when coordinated timelines materially improve the sequence;
- support keyboard navigation, responsive scaling, and `prefers-reduced-motion`;
- keep text selectable and citations accessible.

For PDF, keep the compartment structure visually clear but remove motion. For Google Slides or Keynote, document import and animation-fidelity limitations before production.

## Quality Gate

Assume the first build contains problems. Before delivery:

1. Render every slide or route state.
2. Inspect each slide at full size and the deck as a contact sheet or route overview.
3. Fix unintended overlap, overflow, clipping, wrapping, font substitution, low contrast, damaged crops, and leftover placeholders. Audit the entire rendered text run against its worst-case background, especially image overlays, metadata, page numbers, chart footers, and credits.
4. Run the spacing audit from [references/spacing-and-text-placement.md](references/spacing-and-text-placement.md): inspect page margins, title reserve, image clearance, peer-gap consistency, and top/bottom optical balance. Fix every unrecorded exception.
5. Verify every scene ID is unique, every compartment is independently selectable, and the anchor state matches the plan.
6. Test entrance order, trigger behavior, exit state, and reduced-motion behavior.
7. Test PPTX motion in the target PowerPoint environment; test HTML in a real browser at desktop and narrow widths.
8. Confirm claims and assets are traceable to notes or source layers.
9. Verify every Lieflat chart against its selected gallery, data contract, color system, and candidate audit. For every scientific figure, verify its source data, source code, publication target, vector export, raster fallback when required, and rendered parity with `$scientific-figure-making`.
10. Verify creator names, licenses/terms, and credit placement against [references/credits-and-licenses.md](references/credits-and-licenses.md); do not invent missing authorship.
11. Re-run `validate_deck_plan.py` and rebuild from source after fixes.

Do not deliver unresolved warnings without explaining them.

## Deliverables

Return only the requested final format plus the minimum rebuild source needed for that route:

- PPTX: `.pptx`, authoring source, required assets, and a concise motion note when animation exists;
- HTML: entry HTML/app source, required assets, and run instructions;
- other formats: final artifact and the smallest practical editable source.

Briefly summarize the narrative, visual anchor, zine-engine usage, and animation behavior. Do not attach scratch plans unless the user asks.

Always include a creator-credit manifest in the editable source and place credits according to the final format. Keep creator credits distinct from citations for data, claims, photographs, and external assets.

## Design Provenance

This skill adapts general patterns from the Apache-2.0 [JetBrains/OpenAI slides skill](https://github.com/JetBrains/skills/blob/main/slides/SKILL.md), Alfonso Graziano's MIT [pptx-gen project](https://github.com/alfonsograziano/pptx-gen), `siril9`'s MIT [presentation-skill project](https://github.com/siril9/presentation-skill), and Gabberflast's MIT [academic-pptx-skill](https://github.com/Gabberflast/academic-pptx-skill). The zine visual systems are by **Zeejay0**. Lieflat Charts was created at **Moxt** and is distributed from **larashero3-dotcom**. GSAP is by **GreenSock**. PPTX runtime authoring guidance comes from **OpenAI Presentations**. Read the credit ledger for exact placement and licensing checks.
