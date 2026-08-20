# Poster Plan Contract

Write a concise, machine-checkable `poster-plan.json` before production.

## Required shape

```json
{
  "format": {
    "platform": "canva",
    "design_type": "poster",
    "route": "generation",
    "orientation": "portrait",
    "width": 1280,
    "height": 1800
  },
  "poster": {
    "title": "Design as Layers",
    "audience": "Design teams",
    "purpose": "Demonstrate modular poster construction",
    "governing_message": "A poster can feel tactile without becoming a flat image",
    "viewer_action": "Open the Canva design and move one module"
  },
  "visual_anchor": {
    "identity": "a torn vermilion seam",
    "geometry": "vertical irregular path",
    "material": "native paper-like shape",
    "accent_hue": "#E4472E",
    "continuity_rule": "the seam connects title, evidence, and action"
  },
  "spacing_system": {
    "base_unit": 8,
    "page_margin": 88,
    "tight_gap": 16,
    "regular_gap": 32,
    "major_gap": 64,
    "min_text_image_clearance": 32,
    "peer_gap_tolerance_ratio": 1.25
  },
  "creator_credits": [
    {
      "work": "zine-anchor-deck",
      "creator": "local supplied skill",
      "usage": "anchor, spacing, and compartment method",
      "location": "colophon",
      "license_or_terms": "adaptation requested by user"
    }
  ],
  "modules": [
    {
      "id": "title-stack",
      "role": "hook",
      "kind": "text",
      "editability": "native_text",
      "owner_group": "g-title",
      "bounds": {"x": 88, "y": 96, "w": 760, "h": 330},
      "bounds_basis": "rendered_ink",
      "z": 30,
      "content": "DESIGN AS LAYERS",
      "alt_text": "Poster title",
      "source_note": "User-authored demo copy"
    }
  ],
  "spacing_exceptions": []
}
```

## Rules

- Set `platform` to `canva` or `vector` and `design_type` to `poster`.
- Use `generation`, `brand-template`, `apps-sdk`, `modular-vector`, or `html-vector` as the route.
- Keep `tight_gap < regular_gap < major_gap` and minimum clearance at least 24 planning pixels.
- Use unique module IDs and one owner group per semantic compartment.
- Use `text`, `shape`, `image`, `chart`, `group`, or `texture` as `kind`.
- Use `native_text`, `native_shape`, `native_chart`, `native_group`, `swappable_fill`, `single_vector`, or `fixed_raster` as `editability`.
- Do not use `single_vector` or `fixed_raster` for a module that covers more than 85% of the page.
- Keep all bounds inside the canvas and use positive dimensions.
- Set `bounds_basis` to `rendered_ink` for every text module; do not store a padded authoring box as the collision geometry.
- Give shapes, images, charts, and textures one or more `collision_zones` when their visible mass occupies a more precise area than their module bounds.
- The validator expands text bounds by `min_text_image_clearance` and rejects intersections with unrelated collision zones.
- Use `collision_exempt: true` only for non-content page backgrounds. For intentional text-on-shape, list the exact owning module ID in the text module's `collision_exemptions`; never exempt an anchor or decorative mass.
- Add `owned_text_shape_contracts` for every intentional text-on-shape group. Record `shape_rotation_degrees`, `text_rotation_degrees`, `shape_height`, `text_stack_height`, and `padding` with `left`, `right`, `top`, and `bottom` values measured from rendered ink to visible shape edges.
- Keep shape/text rotations equal, every padding value at least the tight-gap token, opposing-side padding ratios at or below 1.5, and text-stack height at or below 70% of shape height.
- Give every module alt text and a source note, including decorative modules.
- Record every deliberate spacing deviation with `relation` and narrative `purpose`.
- Keep creator credits separate from data, claim, photo, and asset sources.

## Chart Contract

Every module whose `kind` is `chart` must include a `chart_contract` with `finding`, `construction_route`, `data_source`, and `units`. Use `canva-template`, `canva-native`, `native-shapes`, `scientific-figure`, or `single-vector` as the construction route.

For `scientific-figure`, also record `publication_target`, `source_data`, `source_code`, and `export_formats` containing `svg` or `pdf`; set the module editability to `single_vector`. Preserve the data and Matplotlib source with the rebuild files and keep poster-level findings, captions, and sources native when practical.
