# FLUX parameter profiles

## Route separation
| Route | Important controls | Do not assume |
|---|---|---|
| Native FLUX.1 dev/schnell/Krea | Checkpoint, text encoder, width/height, steps, scheduler, guidance convention, seed | Same sampling profile across distilled/base/adapted variants |
| Kontext | Actual input image and instruction; provider output/aspect/seed fields | FLUX 3's ten-image array or box schema |
| FLUX.2 pro/max/flex/klein | Endpoint-specific input_image slots, actual size, seed, variant-specific sampling | Identical guidance/steps or reference counts across providers |
| FLUX 3 Image API | prompt, images, aspect_ratio, resolution or width/height, seed and supported output fields | negative_prompt or prompt_upsampling |

Use the selected official template's concrete sampler settings for native FLUX.1/2 models. The public BFL FLUX.1 CLI records defaults of 4 steps for schnell and 50 for guidance-distilled variants, guidance=2.5 in that CLI, and a default 1360×768 canvas with dimensions divisible by 16. It loads the T5 text budget at 256 for schnell and 512 otherwise. These are implementation defaults, not a universal recommendation for every ComfyUI dev/Krea/LoRA graph. A community “4-step” file must supply its own compatible guidance and schedule. A ComfyUI guidance node and sampler CFG may have different purposes; do not change both under one vague “stronger prompt” request.

## FLUX 3 Image hosted snapshot
Default resolution is 1k. Named choices documented: 768sq for draft-size work, 1k, 2k, 4k, and match_input for edits. Exact width and height can be supplied together: 256–6256 pixels per side, up to 16.8MP without reference images and 4MP with them, aspect up to 8:1. Exact dimensions override resolution/aspect_ratio. `match_input` follows image one up to 4MP, unless another aspect is explicitly selected. Do not copy these limits to native ComfyUI FLUX.1.

The FLUX 3 reference page accepts 1–10 ordered images, each at least 256×256 and at most 16MP. Source image capacity and generated-output capacity are different. Auto aspect follows input one. A low-resolution draft rerendered at another resolution is a new generation, so an identical arrangement is not guaranteed.

## Choosing controls — project method
| User phrase | Semantic action |
|---|---|
| “Keep the exact product” | Use actual supported image conditioning and preserve defining design |
| “More literal” | Clarify required content; reduce competing aesthetic conditions where exposed |
| “Same result, change the color” | Retain base input and all unrelated controls; local edit |
| “Wider, leave space on the right” | Select a wider actual canvas and describe right-hand content/negative space |
| “Try several looks” | Vary medium or style deliberately; record each prompt/settings combination |
| “Exactly 1920×1080” | Use a route accepting that exact canvas, or explain required in-workflow sizing |

Seed is only one reproducibility input. Record checkpoint/endpoint, exact text, image order, preprocessing, canvas, sampling and adaptations. A fixed seed is not a reusable identity or style code. Do not attach a Midjourney flag tail to a FLUX prompt. Optional structured JSON content on a supporting route is a representation choice, not a universal API field schema.
