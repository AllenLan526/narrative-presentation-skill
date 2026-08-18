# Format and Motion Routing

Read this file immediately after the user confirms a delivery format.

## Decision Table

| Route | Choose when | Compartment implementation | Motion contract |
|---|---|---|---|
| HTML | Precise motion, interaction, responsive delivery, or independent scene choreography matters most | Semantic elements with stable `data-scene-id` values | Native Web Animations, CSS, or an available motion library; include reduced motion |
| PPTX | Office editability, handoff, and presenter-controlled playback matter most | Named native groups and editable children | Use native PowerPoint timing only when the toolchain supports and preserves it |
| Google Slides | Collaboration in Google Workspace matters most | Create/import editable objects through the supported Slides route | Re-test animations after import; do not promise PPTX parity |
| Keynote-compatible PPTX | Keynote playback is expected but direct Keynote authoring is unavailable | Conservative PPTX objects and fonts | Treat animation import as lossy until tested in Keynote |
| PDF | Print, review, or archival delivery is the goal | Preserve compartments as static visual stages | No motion; show sequence through layout or numbered states |
| Video | Timed playback and exact visual rhythm matter more than editability | Scene layers in the available video/HTML pipeline | Fixed timeline; include captions where narration is present |

## Required Capability Check

After format selection, determine whether the available toolchain can create the requested motion and whether the target playback application is available for validation. Do this before promising animated output.

If PPTX native animation cannot be authored or verified, offer exactly these alternatives:

1. switch to HTML for full compartment motion;
2. deliver a static editable PPTX with a concise animation cue sheet;
3. use duplicate-slide progressive builds, only with explicit user approval.

Do not represent slide duplication, animated GIFs, or pre-rendered video as native editable PPTX animation.

## Compartment Timing

- Animate one narrative action at a time.
- Use 350–800 ms entrances and 80–180 ms stagger as starting ranges, then adjust to meaning.
- Prefer opacity, mask reveal, short translation, scale from 98–100%, or source-derived path motion.
- Avoid bounce, elastic easing, spins, spectacle transitions, and simultaneous motion with no focal hierarchy.
- Let the anchor create continuity: a seam opens, a field expands, a silhouette migrates, or a color mass transfers.
- Keep exits quieter than entrances unless disappearance is the point.

## HTML Contract

Each compartment must have a stable ID, accessible name, source note, and reduced-motion state. Keep reading order logical without animation. Avoid hover-only information. Preserve text as text and use raster artwork only for visuals that genuinely require it.

## PPTX Contract

Name groups and children predictably:

```text
s03-scene-a
s03-scene-a__photo
s03-scene-a__torn-edge
s03-scene-a__ink-field
s03-scene-a__accent
s03-scene-a__label
```

Keep group bounds tight. Do not let hidden children enlarge the selection box. Put decorative material inside the owning compartment rather than in anonymous slide-wide layers. Record animation order in the plan even when the final route is static.

## Reduced Motion

The reduced-motion version must preserve the final information hierarchy without requiring movement to reveal meaning. HTML should honor `prefers-reduced-motion`. For live PPTX delivery, provide a static fallback or a motion-free export when requested.
