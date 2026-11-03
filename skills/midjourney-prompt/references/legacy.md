# Legacy and historical features

Load this chapter for an older model, an old prompt the user wants to preserve, or an unsupported old flag. Keep historical information separate from the selected current route.

V6/6.1 support `::` conceptual multi-prompts and numeric weights. V7/V8 do not in the current compatibility table. A weight rescales conceptual emphasis, not a bounding region or independent layer. Total weight must remain positive when negative weights are used. Rewrite as clear natural language when migrating a weighted older prompt to V7/V8.

Character Reference `--cref` and Character Weight `--cw` belong to older character-reference workflows, not the current V8 Edit Model or V7 Omni channel. Do not carry these flags into a new V8 prompt. Use Edit Model attachments for V8 reference-based identity or Omni for the selected V7 path. A migration should preserve the intended identity rather than merely rename a flag, because the channels differ in capacity and behavior.

Older Retexture inferred appearance from an existing image while permitting style/material reinterpretation. V8's Edit Model assumes that role. Existing V6.1 Editor actions and legacy Vary Region have their own processing engine; the original image's model is not necessarily the model used to edit it.

Historic model-specific style names, upscalers, image weighting syntax and retired parameters are not universal APIs. Before preserving an old flag, confirm the user is actually targeting its supported legacy version. For old `--stop`, old upscaler flags, broad numeric width/height flags, or an old `--style` preset, do not pretend that the current web image model accepts them. State the current equivalent operation if verified; otherwise mark the precise historical support as unresolved rather than infer a range.

The official Legacy Features article is represented here by its migration-relevant roles; it is not an instruction to reactivate retired products. The source coverage table records its inclusion. V8.0 alpha is no longer selectable; images made with it remain historical artifacts. Keep source provenance when editing them in the current engine.

## Historical parameter profiles
| Profile | Relevant behavior and constraints |
|---|---|
| V5.2 | More detailed/coherent V5 family; supports its own stylize and legacy upscalers |
| V5.1 | Stronger built-in aesthetic; Raw helps reduce automatic interpretation |
| V5 | More photographic starting behavior; can need fuller aesthetic direction |
| Niji 5 | --style cute / expressive / original / scenic are model-specific presets |
| V4 | --style 4a/4b/4c; 4c supports aspect up to 2:1/1:2, 4a/4b have a narrower set |
| Test / Testp | Experimental legacy generation, no image/multi-prompts, limited aspect, optional --creative |
| V1–3 | Older painterly/coherence behavior; V3 --sameseed has a specific same-noise role |
| Old --hd model | Historical model, not current V8 native HD output |

For supported versions through V6, --stop defaults to 100 and accepts 10–100, ending generation early for softer/less complete detail. It is not a V8 control. Older V5 quality choices include 0.25/0.5/1; do not mix those with the current V7 quality set. Historic --w can mean width, while modern --w means weird: never migrate it without interpreting the old version first. --width/--height and old --fast-as-quality, --vibe, --upanime, --hq, --newclip, --nostretch, --old and --upbeta are deprecated/historical rather than general current size/quality controls.

V5 upscalers offer 2×/4× from 1024-square source sizes but do not combine with Pan/tile. V4-and-earlier Light/Beta/Detail/Max options have different size and detail behavior; use the action available on that historical result instead of promising an arbitrary multiplier. Max was resource-intensive; old --upbeta is unreliable/deprecated. Existing Style Tuner codes can be historical inputs, but new tuner creation is retired. Remaster creates a V5.2 interpretation of a historical result, so it is not identity-preserving enlargement. Rooms were discontinued; they are not an available production/organization feature. Retexture remains a V7-and-earlier Editor route, while V8 uses Edit Model. Legacy Character Reference works on Midjourney/Niji 6, with --cw default/max 100 and lower weight narrowing carried appearance toward facial identity.

The Legacy article contains a stale reference to V7 as the current default. Prefer the current Version article's V8.2 snapshot for current selection; keep this conflict explicit rather than propagating the stale claim.
