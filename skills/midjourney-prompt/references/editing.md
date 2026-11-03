# Editing, variations and framing changes

## Choose the smallest adequate operation

| Need | Route | Prompt style |
|---|---|---|
| Similar composition with small differences | Vary Subtle | Retain main prompt; change one decision if needed |
| Broader alternatives from an existing idea | Vary Strong | Keep core concept; expect layout and detail changes |
| Change prompt/settings while deriving a variation | Remix on a compatible result | Describe the whole target result, retaining what should survive |
| One specific attribute on V8 | Quick Edit / Edit Model | Operation + target + desired value + preservation scope |
| Replace a bounded region | Editor mask / Smart Select | A localized replacement that fits context |
| More room around existing content | Zoom Out / Editor canvas expansion | Describe newly revealed surroundings |
| Add scene in one direction | Pan / Editor | Content in the added strip plus continuity |
| Different perspective of the same subject | Edit Model with reference | New view and necessary identity/design invariants |
| Larger pixel result | Supported upscaler / HD route | Separate size request from content changes |

## Local-edit procedure

Identify the existing picture as the base. Name the target unambiguously, then the requested change. Preserve untargeted content by scope rather than re-describing every detail. Example: “Replace the red cap on the left-hand bottle with a brushed silver cap. Retain the bottle body, label, background and framing.” For removal describe the exposed surface if needed; “remove the cable” may require a continuous wall or tabletop behind it. For two edits affecting the same object, keep them in one coherent instruction. For unrelated changes, prioritize or use staged edits if the current tool can do so.

A local region should include enough boundary context for coherent edges. Smart Select is a region-selection aid; Erase/Restore or paint masks define where modification is requested. A text-only preservation instruction is not a hard pixel lock. Do not claim a selected region guarantees unselected pixels never change. Follow current Editor behavior for layers, positioning, scale, transparent space and submission. The Edit Model does not use tile and its outputs do not support Remix in this snapshot.

## Outpainting and camera language

Zoom Out increases visible surroundings rather than moving a physical camera through a scene. Pan grows one side of the canvas. Write what should be revealed and how ground planes, horizons and lighting continue. Avoid introducing a second camera angle inside the new border. Legacy Zoom values typically expose 1.5×, 2× and custom framing; use current UI choices, not an invented flag. “Make Square” is a framing operation. Check resulting aspect and pixel size instead of assuming both original dimensions were retained.

## Upscalers

Subtle aims at retaining the source appearance; Creative allows new interpretation and detail. Neither is an instruction to alter the brief. On V7, the documentation routes these through V6.1 upscalers. On V8, HD is native generation, so rerunning in HD is not equivalent to enlarging existing pixels. Inspect text, hands, fine geometry and logos after a detail-generating operation. Tile edges can lose continuity after upscaling; inspect a repeat preview before accepting.

## Version-aware handoff

Older Vary Region and V7 Pan/Zoom can use V6.1 processing. V8 Editor/Pan/Zoom use Edit Model. Thus identity, style and engine behavior can change even if the original was V7. Keep a record of source model and requested edit route. Editor replaces the old Retexture role for V8; preserve legacy instructions only for a user explicitly working in that legacy path.

Sources: Modifying Your Creations, Variations, Remix, Editor, Edit Model, Pan, Zoom Out, Upscalers and Vary Region legacy notes. See sources.md for scope mapping.
