# Parameter selection and interactions

Put flags after all descriptive text, separated by spaces. Use two ordinary hyphens and no trailing punctuation on a value. Copy exact codes only from user inputs or existing jobs. A website attachment can carry a reference without a URL in the text.

| Field / flag | Snapshot values | Effect and decision rule |
|---|---|---|
| --v / --version | Existing selected version, e.g. 8.2 or 7 | Select before any version-sensitive controls |
| --niji | 7 in current article | Anime family; not a second simultaneous --v choice |
| --ar / --aspect | Integer ratio, default 1:1 | Shape, not pixel resolution; write 139:100 instead of 1.39:1 |
| --sd / --hd | Standard or native HD on V8 | Resolution route, not artistic quality |
| --s / --stylize | 0–1000, default 100 | Lower favors literal direction; higher allows more aesthetic interpretation |
| --c / --chaos | 0–100 | Variation across results; lower for controlled comparisons |
| --w / --weird | 0–3000, default 0 | Experimental unconventional interpretations; avoid for precision matching |
| --raw | Boolean | Reduce automatic stylistic embellishment; still needs a well-written prompt |
| --seed | 0–4294967295 integer | Controlled starting randomness, not a character/style identifier |
| --q / --quality | V6: 0.5/1/2; V7: 1/2/4 | Processing investment; unsupported on V8; does not set output dimensions |
| --iw | See image-references.md | Overall Image Prompt influence |
| --sref / --sw / --sv | Reference/code; weight 0–1000 default 100; version-dependent style implementation | Style channel; --sw cannot be used with moodboards |
| --oref / --ow | V7 only; 1–1000 default 100 | Subject-reference channel; incompatible with --q 4 |
| --edit | V8 Edit Model route | Use website Attach to prompt; do not add invented attachment identifiers |
| --p / --profile | Existing personalization/profile/board code | A real selected taste source, not a random number |
| --no | Named unwanted concepts | Each word can be interpreted independently; prefer desired attributes for phrases |
| --tile | Boolean | One repeatable tile, not a tiled preview; Edit Model incompatible |
| --repeat / --r | Plan/mode-dependent batch count | Re-run the same specification, not preserve the seed automatically |
| --fast / --relax / --turbo | One eligible execution mode | Scheduling and cost, not prompt semantics; seed comparisons should avoid Turbo |
| --public / --stealth | Publication visibility controls | Output management only; do not change without a user request |
| --motion / --loop / --end / --bs | Video only | Read video.md rather than treating them as image-generation controls |

## Useful starting experiments — project heuristics

Literal product image: Raw, stylize around 25–75, low chaos, default quality where supported. Express exact composition and material in text. A stylized cover exploration: moderate stylize and chaos, perhaps 4 intentionally different prompt directions. Those trial values are suggestions, not model defaults or promises. Keep the existing seed if comparing only one setting; record model, prompt, references, resolution and all other controls too.

High stylize, strong style references, a moodboard and high Omni strength can compete. Identify the primary invariant before raising every slider. When identity is primary, simplify unrelated styles. When style is primary, preserve necessary shape cues while allowing nonessential texture to change. Raising quality cannot fix a contradictory brief.

## Multi-prompts and batch expansion

`::` conceptual separation and numeric weights are a V6-and-earlier feature in this snapshot, not V7/V8. On supported models the unspecified weight is 1; negative weights require a positive total. Do not use Stable Diffusion `(phrase:1.2)` syntax as a substitute.

Permutations use `{a,b}` and expand combinatorially; two sets of three choices produce nine jobs. Escaping a comma inside a choice prevents an unintended split. Repeat and permutation availability is plan/mode-dependent; both consume multiple jobs. Provide explicit alternatives when a batch feature is unavailable. Do not submit a large combinatorial batch just because the user asked for one prompt.

## Exact sizes

At a square aspect V8.2 SD is 1024² and HD is 2048² in the size article. Other aspects use different dimensions. An HD-generation ratio limit of 4:1 is narrower than SD's 14:1. Inpainting/outpainting on an HD result can return SD, requiring a subsequent supported upscale. For print, pixel count divided by target DPI gives physical inches; changing the DPI label alone adds no image detail. These facts do not authorize external image conversion in this project.

## Batch and style-algorithm details
Repeat limits: Basic 2–4, Standard 2–10, Pro/Mega 2–40. Permutation expansion permits up to 4/10/40 prompts respectively. Both require Fast or Turbo rather than Relax in their articles. Nested braces multiply combinations. Repeat is removed from completed metadata and must be added again for another repeated submission. Chaos defaults to zero in the documented standard profile.

V7 style algorithms: --sv 1–6, default 6; style codes/random work with 4 or 6. V6 algorithms: --sv 1–4, default 4. This is not the main model version or style-strength value. Do not assign an undocumented V8 algorithm combination.

V8.2 output examples from Upscalers: 4:3 SD 1232×928 → HD/upscaled 2464×1856; 2:3 896×1344 → 1792×2688; 16:9 1456×816 → 2912×1632. Aligned pixel dimensions need not have the exact named ratio. Native HD currently has no additional built-in upscale in that article.
