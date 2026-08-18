# Narrative Presentation Skill

A general-purpose presentation skill for clean, editorial narrative decks built around one evolving visual anchor. It supports HTML, editable PPTX, independently animated scene compartments, source-derived imagery, Lieflat chart scenes, explicit spacing/contrast contracts, and creator-credit manifests. The current packaged skill keeps the implementation ID `zine-anchor-deck` for compatibility.

## Included

- `skill/` — the reusable `zine-anchor-deck` skill and validation references.
- `demo/index.html` — an eight-slide interactive HTML demonstration.
- `demo/zine-anchor-complex-demo.pptx` — an editable static-final-state PowerPoint with animation cues and sources in speaker notes.
- `demo/source/` — the validated deck plan, PPTX build source, and browser QA record.
- `demo/prompt.md` — the prompt used to generate the demonstration.

Open `demo/index.html` directly in a modern browser. Use the arrow keys or spacebar to move between slides and `F` for fullscreen.

## Design principles

- One persistent visual 锚点 that changes state as the argument develops.
- Scene compartments remain independently selectable and animatable.
- Text placement follows an 8 px spacing system and rendered-ink clearances.
- Normal text targets at least 4.5:1 contrast; small metadata targets 7:1 where practical.
- Quantitative scenes preserve their declared Lieflat template and data contract.
- HTML supports reduced motion; PPTX documents honest static fallback behavior.

## Validation

The included demo passed:

- browser console, scene-ID, motion, and narrow-viewport overflow checks;
- full-slide and contact-sheet visual inspection;
- exported PPTX rendering inspection;
- PowerPoint canvas-overflow validation.

## Credits and provenance

This project intentionally keeps creator credit visible and machine-readable. See [AUTHORS.md](AUTHORS.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the complete ledger.

Key contributors and source systems include **@Zeejay0**, **Moxt**, **larashero3-dotcom**, **JetBrains/OpenAI**, **Alfonso Graziano**, **siril9**, **Gabberflast**, **GreenSock**, **Rasmus Andersson**, and **OpenAI**.

## Licensing

This repository uses mixed licensing because the demonstration incorporates components with different terms. See [LICENSE.md](LICENSE.md) before reuse, especially for Lieflat-derived chart material, which is identified as PolyForm Noncommercial 1.0.0.
