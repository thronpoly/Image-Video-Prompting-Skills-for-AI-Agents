# Qwen reference roles and image ordering

## Decide the job before indexing
An image may be the canvas to edit, a person/product identity, a garment, a style, a pose or a setting. A photograph supplying identity for a new scene is not necessarily the canvas. A style donor is not the framing authority. Write an ordered mapping and retain it through the ComfyUI input slots.

For the official Qwen 2.1 edit-enhancer convention, multiple inputs use `<image1>`, `<image2>` and so on, matching input order exactly. One input is described naturally as “the image,” without those tags. That rule belongs to 2.1's enhancer; older node implementations may expect their own image order wording. Determine the selected route before substituting tags. A tag is a pointer to a real input, not a way to conjure an unseen asset.

## Canvas decision table
| Task | Canvas/framing source | Donor role |
|---|---|---|
| Put a person into a room | Room image | Person identity |
| Replace a coat | Person image | Coat design/material |
| Apply a painted look | Content image | Style example |
| Replace background behind a person | Original person image | New background environment |
| Replace one object | Existing scene | Replacement object |
| Group portrait from separate people | New scene; choose output frame | Each identity separately |
| Three-view sheet | New composed layout | Same subject identity from its references |

For multiple identity sources, state each source separately. Do not collapse them into “images 1–4” if each has a different job. Do not borrow a donor's background, crop, expression or accessories unless requested. Explicitly name the owning person or object when two similar subjects are present.

## Conflicting sources
Choose the canonical identity before writing. If one reference is a frontal photo and another is a stylized interpretation, decide whether it contributes geometry, costume or rendering style. If an angle cannot reveal the requested feature, say it is unseen rather than inventing it as verified. A new viewpoint requires inferred geometry and cannot guarantee an unseen side's exact details.

## Framing propagation
The official enhancer uses mutually exclusive wh_ratio and ratio_follow decisions: an explicit requested ratio populates wh_ratio; a canvas-following edit points ratio_follow at the selected image. With a multi-input composition, following the donor's ratio can accidentally crop the intended room or body. These fields must be translated into actual supported width/height/canvas controls. A ratio pointer is not itself a diffusion model argument unless the template exposes it.

## Actual controls
Reference tensor connection, number of supported inputs, image preprocessing and latent sizes depend on the selected model/node. A universal “reference strength 0.8” is not part of this manual. If a template exposes only two input slots and the user supplies three independently necessary sources, explain the limitation. Do not silently concatenate or transform inputs through an external script or redesign the workflow.
