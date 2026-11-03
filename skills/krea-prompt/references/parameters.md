# Krea parameter profiles

## Open Krea 2 official examples
| Profile | Documented settings | Interpretation |
|---|---|---|
| RAW | 52 steps, CFG 3.5 in recommended example; roughly 1K training resolution | Undistilled base; appropriate for training/adaptation |
| Turbo | 8 steps, CFG 0.0, mu 1.15, example 2048² | Distilled inference; CFG disabled in that code |
The CLI parser separately has generic defaults such as 28 steps/CFG 4.5. Use the recommended checkpoint profile, not unrelated parser defaults. Official instructions recommend training LoRAs on RAW and applying them to Turbo; actual compatible file formats still matter.

Native controls include width/height, steps, cfg, seed, number of images and timestep-shift parameters y1/y2 or a constant mu override. Width/height are padded to a multiple of 16 in the public implementation. A ComfyUI no-CFG setting may be expressed as CFG 1 rather than this CLI's zero. Preserve the actual template's convention. Native seed increments per image in the CLI example; a UI's batching policy may differ.

## Hosted Krea 2 medium-turbo snapshot
Required: prompt, aspect_ratio, resolution. The captured route offers resolution `1K` only even though native Turbo can generate larger images. Aspect choices: 1:1, 4:3, 3:2, 16:9, 2.35:1, 4:5, 2:3, 9:16. Creativity: raw/low/medium/high, default medium, described as different prompt-interpretation levels. Optional seed, styles, image_style_references (up to 10), moodboards (up to 1). These are route-specific; do not silently promote the native 2K example into an accepted hosted enum.

## Hosted Krea 3 snapshot
Required prompt and resolution, with 1k/2k documented. Models: berry quality default, jam speed. Up to eight image_urls. Optional negative_prompt with 1024-character limit, seed, aspect_ratio, regional_edit and thinking_mode. Thinking modes fast/high/ultra; ultra needs 2k. Regional editing needs berry and at least one image. These features belong to Krea 3; they are not universal Krea 2 or FLUX Krea fields. Read parameter-snapshot.json for the recorded schema and mark a current endpoint mismatch explicitly.

## How to choose
Preserve named model and user controls. Use the matching official template defaults for sampling. Select output aspect based on the deliverable and actual accepted choices. For a seed comparison, keep input order and all reference/style controls fixed. A request for “less creative” should first be interpreted as stricter adherence to immutable content; if the chosen provider exposes creativity, adjust that control separately from CFG or LoRA strength. Do not promise stronger guidance always improves adherence or identity.

Krea 1 proprietary service, open FLUX.1-Krea-dev, native Krea 2 and hosted Krea 3 are separate profiles. For a missing profile, author with supported common natural language and identify the exact unsupported setting. Do not fill in plausible numeric ranges from another model.
