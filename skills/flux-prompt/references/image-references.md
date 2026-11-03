# FLUX image roles and capacity

## Distinguish model routes
FLUX.1 ordinary T2I is not the same interface as Kontext. Kontext edits actual images and can preserve semantic identity across changes. FLUX.2 supports multi-reference editing with provider-specific input slots. FLUX 3 Image takes an ordered images array for up to ten references in its documented API. Do not copy that capacity into native FLUX.1 or every Klein wrapper.

The FLUX.2 official editing page describes up to eight API references versus ten in its playground. The same family may therefore expose different counts depending on where it is run. Read the selected template slots; if it exposes fewer inputs than the task needs, disclose the mismatch instead of dropping a required source silently.

## Reference planning
Use this ledger: order, filename, role, transferred attributes, preserved attributes, placement. Typical roles are base canvas, person/character identity, product geometry, garment, setting, style or surface pattern. A donor can supply multiple selected properties but should not silently supply its unrelated background. Make the base canvas first where the provider's automatic frame follows input one.

For FLUX 3 prose, “image 1” means the first actual entry in images. Use the same naming throughout. For layout rows, the same image is `ref_image_0`: natural-language references are one-based and row references are zero-based. This indexing difference is easy to mishandle. Do not use Qwen `<image1>` or MiniMax `<Picture 1>` as assumed universal FLUX tokens.

## Aspect and actual size
In the FLUX 3 API snapshot, aspect_ratio:auto follows image one and resolution:match_input follows image one's actual size up to the edit limit. An explicit aspect asks for a new frame and needs a description of newly included/cropped space. Native ComfyUI may use width/height rather than these field names. Apply the same design intent through the actual exposed controls.

## Identity versus style
A person's identity should come from its actual source; long verbal feature lists can create a similar new person rather than the same one. A product reference must preserve distinctive geometry, markings and count when those are fixed. Style transfer changes rendering treatment while preserving requested content. Separate a material donor from a shape donor explicitly if using both. A logo shape and its surface integration can need separate instructions: preserve the mark while changing scale, perspective and material response to fit its destination.

## Integration
Name target position, size, orientation, contact and occlusion. Match the inserted object's illumination to the canvas unless the user requests a contrasting light. For two subjects, name who owns a garment/prop. If exact placement matters on a supporting FLUX 3 route, use measured boxes rather than made-up coordinates. Do not describe a box as a hard clipping mask; it guides the composition.
