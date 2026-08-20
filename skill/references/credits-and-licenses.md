# Creator Credits and License Checks

Read this file before production and again before delivery. Credit actual creators; never infer or invent authorship.

## Required Credit Ledger

| Work or skill | Creator credit | When to record | License or terms check |
|---|---|---|---|
| `scenes-gathered-zine-v1-3` | Visual Skill by **@Zeejay0** | Whenever the skill generates or materially directs an asset | Follow its first/second-generation sharing-credit rule; never watermark the slide |
| `scene-distillation-zine-v1-3` | Visual Skill by **@Zeejay0** | Whenever the skill generates or materially directs an asset | Follow its first/second-generation sharing-credit rule; never watermark the slide |
| Lieflat Charts | Created at **Moxt**; repository by **larashero3-dotcom** | Whenever Lieflat templates, tokens, or its named visual system are used | Read the installed `LICENSE` before commercial/public use; its third-party libraries retain separate licenses |
| Scientific Figure Making / `figures4papers` | **Chen Liu (@ChenLiu-1996)**; upstream README acknowledges **Shan Chen** for suggesting the LLM-skill integration | Whenever its plotting conventions or skill materially direct a figure | GitHub reports no detected repository license; reference the workflow unless separate reuse terms permit copying code or assets |
| GSAP | **GreenSock** | When GSAP ships in an HTML deliverable | Verify the current GSAP license/terms for the delivery context |
| OpenAI Presentations | **OpenAI** | When its authoring workflow/runtime materially produces the PPTX | Preserve ordinary source attribution; a visible tool credit is optional unless the user requests a full production colophon |
| Chinese Font Selector | Creator not declared in local metadata | When it informs typography | Do not invent a skill creator; credit each chosen font's designer/foundry and license instead |

Lieflat's installed third-party notice identifies Chart.js (MIT), Apache ECharts (Apache-2.0), and Inter (OFL-1.1). Record only libraries that actually ship in the final artifact.

For the broader skill architecture, keep these credits in the package provenance: JetBrains/OpenAI slides skill; Alfonso Graziano for `pptx-gen`; Siril for `presentation-skill`; Gabberflast for `academic-pptx-skill`.

## Placement by Format

- **PPTX:** Put claim/asset citations in `[Sources]` blocks in speaker notes. Put design-system and creator credits in the final Sources/Credits slide or its speaker notes; use a visible line when the deck will circulate without notes.
- **HTML:** Add a concise visible colophon/footer and machine-readable metadata. Link creator/project names when appropriate.
- **PDF:** Add a visible final colophon or compact credits block because speaker notes will not travel.
- **Video:** Put credits in the end card or attached description, depending on the user's publishing context.

Do not repeat credits on every slide. Do not turn attribution into a logo wall. Keep creator credits separate from data sources, image credits, and research citations.

## Commercial-Use Gate

Before copying any template, code, font, or animation library into a commercial deliverable:

1. Read the installed or current license.
2. Confirm the planned use is permitted.
3. Record the license/terms result in `creator_credits`.
4. If permission is unclear or incompatible, do not copy that asset. Use a compatible native/original route and state the substitution.

Credit does not replace license permission.
