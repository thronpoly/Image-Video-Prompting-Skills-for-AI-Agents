# Turbo inference and parameter mapping

## Official example versus interface conventions
The official repository configuration specifies 1024×1024, 8 inference steps, guidance_scale 0.0, cfg_truncation 1.0 and max_sequence_length 512. The Hugging Face Diffusers example uses num_inference_steps=9 with a comment that this produces eight DiT forward passes, and guidance_scale=0.0. These are implementation-specific schedule conventions. Do not treat “8” and “9” as conflicting quality advice or force a Diffusers count onto a ComfyUI template.

Turbo is distilled and uses no CFG in its standard path. A ComfyUI CFG value of 1 commonly disables classifier-free mixing, while the official pipeline calls its no-guidance setting 0.0. These numbers are not interchangeable field names. Preserve the actual official template's value and semantics. A negative prompt has no guidance effect in that disabled branch. Base Z-Image and Edit use different paths; their settings must not be copied into Turbo.

## Control table
| Control | What it changes | Practical handling |
|---|---|---|
| checkpoint | Turbo versus Base/Edit | Match the selected task; retain user choice |
| width/height | Canvas and resource use | Choose supported aligned dimensions with the intended aspect |
| steps | Schedule/compute | Start from official template's Turbo profile |
| CFG / guidance_scale | Conditional mixing | Keep route-specific disabled-guidance convention |
| scheduler / timestep shift | Denoising trajectory | Retain template defaults unless a selected variant documents another profile |
| seed | Starting randomness | Pin for controlled comparisons, not identity preservation |
| max_sequence_length | Encoder text budget in the official pipeline | Keep key content early; do not assume all UI nodes expose it |
| LoRA / strength | Added adaptation | Use a real compatible file and documented trigger/settings |
| denoise | Latent reconstruction strength, if actually supported | Do not invent this field for a plain T2I template |

## Choosing size
Treat 1024 square as a documented reference configuration, not the only supported shape or a promise that all arbitrary large sizes fit hardware. A target 16:9 frame needs an aligned width/height pair accepted by the actual template; avoid claiming an unverified maximum. Keep framing consistent with text: a tight full-body portrait may need breathing room around the feet. Increasing pixel count does not reliably repair an omitted object or wrong count.

## Comparison method
Keep checkpoint, seed, canvas and sampling constant while changing one prompt clause. Then compare whether that clause changes the intended property. If a different seed produces a better composition, record it as selection rather than claiming the original instruction was fixed. If a LoRA is in use, compare with its documented strength and preserve all other settings.

Source references are in sources.md. These settings are dated official example profiles, not a universal preset for every wrapper or quantized/accelerated model.
