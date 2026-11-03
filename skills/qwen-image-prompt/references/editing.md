# Qwen editing instructions

## Local changes versus new scenes
For a local edit, start with the operation and target. Describe only the appearance being changed; preserve untargeted content by role and scope. Repainting every preserved face, garment and background in words can encourage regeneration. For a new scene based on identity sources, build the scene actively: pose, framing, setting, light and interaction must be specified. Do not preserve the original background in a task that explicitly replaces it.

## Operation recipes — original writing patterns
| Operation | Instruction components |
|---|---|
| Add | New object + precise region + scale/orientation + relationship to surface/light |
| Remove | Exact target + what should be revealed + unaffected objects |
| Replace | Existing target → supplied/new design + preserved placement/contact |
| Recolor | Target surface + new color + preserved material/shape |
| Change material | Target + new material response + preserved geometry |
| Outfit | Person canvas + garment donor/design + identity/pose/background preservation |
| Expression | Requested facial action + retained identity, head orientation and scene |
| Relight | Desired direction/quality + which existing shadows/reflections may change |
| Restyle | Target medium + retained content and arrangement |
| Background | Subject retained + new environment + coherent contact/light |
| Viewpoint | New view + invariant subject geometry + expected revealed surfaces |
| Text edit | Exact old/new lettering + location + retained type/layout as requested |
| Outpaint | Direction/target frame + extended content + retained source scale/placement |

Do not dilute a requested change into a barely visible effect. Preservation protects untargeted attributes; it does not mean applying the requested edit weakly. Conversely, do not repair unrelated clutter or color grading merely because it looks unattractive.

## Literal text language
For 2.1 editing, Korean user instructions produce English descriptive prose. Visible text follows explicit user copy/language; otherwise it normally follows the existing image's dominant text language. If no prior text or explicit language exists, use the user's language when new text is requested. Keep these decisions independent. A “technical poster” request does not justify automatically turning Korean labels into English.

## Aspect and outpainting
If the user explicitly gives a ratio, use it separately from the edit sentence. Otherwise a local edit should generally inherit its canvas. A new portrait scene can choose a new portrait aspect. A three-view sheet needs a frame based on panel dimensions, not an automatic ultrawide default: three narrow standing-person panels may fit a square sheet. Outpainting changes frame extent; define which direction expands and which input stays anchored. Repeating “same size” while asking for a wider canvas is contradictory.

## Enhancement and transparency
“Sharper” should target readable edges and texture without changing identity or color. Exact upscaling/pixel size still requires an actual supported output operation. Qwen 2.1 includes demonstrated alpha generation, but that is checkpoint-specific; do not promise native transparency for every older Qwen-Image/Edit checkpoint. A pale checkerboard rendered into RGB is not an alpha channel. Verify output channels if transparency is requested.

## Enhancer output contract
For 2.1 edit-enhancer JSON, use rewritten_prompt, wh_ratio, ratio_follow. Exactly one of the last two is populated. Ratio and resolution do not belong inside rewritten_prompt. That schema is a preprocessing artifact. For an ordinary user prompt request, provide the rewritten directive and corresponding frame choice without requiring them to manage internal JSON.
