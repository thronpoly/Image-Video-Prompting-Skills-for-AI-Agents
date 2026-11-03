# Qwen settings by checkpoint

## Verified example profiles
| Profile | Official documented example | Scope |
|---|---|---|
| Qwen-Image-Edit-2511 Diffusers | 40 inference steps, true_cfg_scale 4.0, guidance_scale 1.0 | This pipeline's model card; do not copy field meanings blindly into every Comfy node |
| Qwen-Image-2.1 original | 40 steps, 2048×2048 default | Base checkpoint, native 2K level |
| Qwen-Image-2.1 Turbo | Saved 8-step schedule, CFG 1 | Setting only num_inference_steps does not necessarily replace the saved schedule |
| Community Lightning/LoRA | Its own documented steps/schedule | Apply only if that variant is explicitly selected |

## 2.1 recommended frame sizes
| Aspect label | Width × height |
|---|---|
| 1:1 | 2048 × 2048 |
| 4:3 | 2400 × 1792 |
| 3:4 | 1792 × 2400 |
| 3:2 | 2528 × 1696 |
| 2:3 | 1696 × 2528 |
| 16:9 | 2752 × 1536 |
| 9:16 | 1536 × 2752 |
These are recommended aligned sizes, not mathematically exact ratios and not every model's universal dimensions. Native 2K settings can be expensive on the local GPU. Preserve the requested quality while reporting feasibility through the execution flow; do not silently substitute a different checkpoint.

## Separate control layers
Prompt language describes image content. Output width/height select canvas size. Sampler, scheduler, steps and CFG select inference behavior. LoRA strength selects an added adaptation. Image-to-image denoise, when actually present, selects how much a latent reconstruction can change. The word “reference strength” does not mean all of these are interchangeable.

An instruction-editing model can use image conditioning without a generic denoise slider. Do not propose one unless exposed by the selected official template. `true_cfg_scale` in Diffusers and a ComfyUI CFG field may involve different wiring. Negative conditioning can be used by some original CFG-capable pipelines; Turbo/CFG-disabled routes cannot be assumed to honor it. Keep any negative prompt minimal and route-specific rather than attaching a Stable Diffusion blacklist to every Qwen request.

## Parameter selection procedure
1. Read selected checkpoint and official template notes.
2. Preserve explicit user values that the route accepts; explain a mismatch instead of silently clamping.
3. Choose the requested aspect and a valid supported size.
4. Retain default sampling for that checkpoint unless a demonstrated issue motivates a controlled change.
5. Pin a seed for comparisons if useful; retain all input order and settings too.
6. If using official enhancer JSON, translate wh_ratio/ratio_follow into the current template controls.

The enhancer's output-size heuristics are not permission to ignore an explicit exact pixel deliverable. If the requested size requires a supported in-workflow resize or crop not currently exposed, explain that distinction. No external conversion should be introduced by this skill.
