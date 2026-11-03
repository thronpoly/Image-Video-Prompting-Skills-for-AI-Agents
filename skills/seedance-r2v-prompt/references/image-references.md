# Seedance reference allocation

## Asset indexing
2.0 ModelArk references use Image 1, Video 1, Audio 1 by order within each modality, starting at one. An asset URI is an upload identifier, not its model-facing name. The 2.5 tutorial uses @Image 1 / @Video 1 / @Audio 1. Preserve the chosen version/provider syntax and actual input order. Do not assign MiniMax's Picture labels by habit.

## Stable subjects and selective transfer
Define each important subject once with a few visible distinguishing features and a source. Use the same name later. When several inputs show the same character, state that relationship rather than letting the model create clones. For image-based transfer specify whether appearance, garment, prop, composition or style should carry over. For video-based transfer specify motion, camera, effects or whole-source editing. Audio role is handled separately.

## Input profile snapshot
| Model | Image reference capacity | Video references | Audio references |
|---|---|---|---|
| Seedance 2.0 family | Up to 9 images in documented omni profile | Up to 3, 2–15 sec each, at most 15 sec combined | Up to 3, 2–15 sec each, at most 15 sec combined; requires an image or video |
| Seedance 2.5 | Up to 30 images | Up to 10 with combined duration at most 30 sec; source-edit videos 4–30 sec | Up to 10, 2–30 sec each, at most 30 sec combined; audio-only reference supported |
The 2.5 overall multimodal maximum is 50 assets in that profile. These are provider/model capacities, not a promise that the current ComfyUI node exposes every slot. Input file dimensions, size and accessibility still need validation against the route.

## Identity source quality
The 2.0 troubleshooting guide favors a clear headshot plus a full-body image for a human character and cautions that crowded/multi-view sheets can be interpreted as multiple subjects. Do not import a blanket “more angles always improves identity” rule from another model. If a sheet is all the user has, explicitly bind its panels to the same identity and describe the limitation; creating a new crop/composite is a separate input-preparation action under project constraints.

## Donor-role matrix
| Brief | Asset responsibilities |
|---|---|
| Same person, new pose | Head/identity source + optional pose donor, one resulting subject |
| Same product, moving camera | Product design source + camera-only video reference |
| Character copies dance | Character appearance + action-only video; donor identity excluded |
| Same room, add product | Scene source + product source, physically integrated |
| Sequence/storyboard | Assign panels to intended order and scenes; do not create simultaneous clones |
| Effect transfer | Name effect origin, timing and physical interaction, not donor setting |

## First/last-frame route versus omni
Use first_frame/last_frame roles only for genuine anchors supported by the selected task. A normal reference image should not become a required first frame. For a storyboard or sequence, describe its temporal mapping explicitly. For a 2.5 anchored image task, aspect follows the first frame under its adaptive restriction; do not promise a freely selectable concrete ratio in that mode.

## Conflict check
If a motion reference has a camera move but the target camera is fixed, borrow only actor motion. If a product donor has a promotional caption but the target is text-free, exclude that caption's role. If appearance and style conflict, preserve declared identity and specify a consistent target medium. Use reference roles to resolve conflicts before raising any generic “strength” setting.
