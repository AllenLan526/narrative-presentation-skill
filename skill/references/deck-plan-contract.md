# Deck Plan Contract

Write a machine-checkable `deck-plan.json` before authoring. Keep prose concise; this is a production contract, not a design essay.

## Required Shape

```json
{
  "format_decision": {
    "output_format": "pptx",
    "confirmed": true,
    "playback_environment": "PowerPoint desktop",
    "motion_required": true
  },
  "presentation": {
    "title": "Example",
    "audience": "Decision-makers",
    "purpose": "Approve the proposed direction",
    "governing_message": "One sentence that the deck proves"
  },
  "visual_anchor": {
    "identity": "A source-derived opening",
    "geometry": "Irregular aperture",
    "material": "Torn paper and dry charcoal",
    "accent_hue": "tomato red #E13B2D",
    "continuity_rule": "The aperture opens as uncertainty resolves"
  },
  "spacing_system": {
    "base_unit_px": 8,
    "page_margin_px": 72,
    "tight_gap_px": 16,
    "regular_gap_px": 28,
    "major_gap_px": 48,
    "min_text_image_clearance_px": 24,
    "peer_gap_tolerance_ratio": 1.25
  },
  "creator_credits": [
    {
      "work": "scene-distillation-zine-v1-3",
      "creator": "Zeejay0",
      "usage": "Visual direction for the opening scene",
      "location": "credits-slide speaker notes",
      "license_or_terms": "Source skill sharing-credit rule"
    }
  ],
  "slides": [
    {
      "id": "s01",
      "title": "The decision begins with one unresolved opening",
      "role": "opening",
      "layout_family": "asymmetric-island",
      "anchor_state": "compact clue",
      "spacing_contract": {
        "balance_mode": "neutral",
        "title_reserve": "lowest rendered title ink + major gap",
        "text_image_clearance_px": 48,
        "peer_gap_tier": "regular",
        "spacing_exceptions": []
      },
      "source_notes": [],
      "scenes": [
        {
          "id": "s01-scene-a",
          "role": "primary visual",
          "engine": "distilled",
          "subject": "source-derived aperture",
          "geometry": "right third, tall organic crop",
          "anchor_relationship": "contains the anchor",
          "alt_text": "An irregular red opening in a charcoal paper field",
          "credit_refs": ["scene-distillation-zine-v1-3 / Zeejay0"],
          "animation": {
            "trigger": "on-click",
            "entrance": "mask reveal",
            "emphasis": "none",
            "exit": "none",
            "duration_ms": 550,
            "reduced_motion": "show final state"
          }
        }
      ]
    }
  ]
}
```

## Rules

- Set `format_decision.confirmed` to `true` only after the first format gate is answered.
- Use a unique slide ID and unique scene ID throughout the deck.
- Use one to three scenes per slide; prefer one.
- Use `gathered`, `distilled`, `lieflat`, `scientific-figure`, or `native` as the scene engine.
- Give every slide an anchor state.
- Define one deck-wide `spacing_system`. Keep `tight_gap_px < regular_gap_px < major_gap_px`, use at least 24 px minimum text-to-image clearance, and keep the peer-gap tolerance ratio between 1.0 and 1.5.
- Give every slide a `spacing_contract`. Use `neutral` or `intentional-asymmetry` as `balance_mode`; name the title reserve rule, expected text-to-image clearance, and peer-gap tier.
- Keep `spacing_exceptions` empty by default. For `intentional-asymmetry`, add at least one exception object with `relation` and `purpose`; a purpose must explain the narrative effect, not merely that the layout fits.
- Give every scene alt text and an anchor relationship.
- Give every non-native scene at least one `credit_refs` entry.
- Add `creator_credits` entries for every invoked visual system, template family, motion library, and font. Record work, creator, usage, placement, and license/terms status. Never invent an undeclared creator.
- When motion is required, give every scene a complete animation record.
- Use a maximum of two consecutive slides from the same layout family.
- Put source URLs or source identifiers in `source_notes`; move them to speaker notes or the route's citation layer during production.
- Keep the final slide useful during discussion: conclusion, decision, or next action—not a generic “Thank you.”

## Lieflat Chart Contract

Every scene whose engine is `lieflat` must also include:

```json
{
  "chart_contract": {
    "finding": "One independent conclusion",
    "system": "lupi-editorial",
    "template_id": "L14",
    "gallery_file": "templates/lupi-gallery.html",
    "card_title": "Hundred Field",
    "color_system": "wire",
    "candidate_audit": [
      {"template_id": "L14", "decision": "selected", "reason": "honest unit field"},
      {"template_id": "F4", "decision": "rejected", "reason": "slower comparison"},
      {"template_id": "L5", "decision": "rejected", "reason": "relationship geometry is unnecessary"}
    ]
  }
}
```

If fewer than three honest candidates exist, include `candidate_shortfall_reason`.

## Scientific Figure Contract

Every scene whose engine is `scientific-figure` must also include:

```json
{
  "figure_contract": {
    "finding": "One independent conclusion",
    "figure_type": "grouped-bars",
    "publication_target": "conference presentation and PDF handout",
    "source_data": "data/results.csv",
    "source_code": "figures/result_overview.py",
    "export_formats": ["svg", "png-300dpi"]
  }
}
```

Include `svg` or `pdf` in `export_formats`. Keep the data, code, and exports traceable to one another. Add `$scientific-figure-making` to `creator_credits` as an invoked production system; when creator metadata is absent, record that it is not declared instead of inventing authorship.
