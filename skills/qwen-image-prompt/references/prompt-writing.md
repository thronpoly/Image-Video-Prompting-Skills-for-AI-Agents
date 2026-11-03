# Qwen text-to-image authoring

## Convert the brief into a frame
Separate mandatory content from implementation instructions. A requested brand string, object count, color and position are content. “Use a 2K image” is an execution choice, not text to paint into the picture. Retain exact requested words in their original script, including punctuation and spacing.

The 2.1 T2I enhancer describes an image as an observer: medium/style, background, frame organization, subjects, materials, light and the overall design. Use English descriptive prose for a Korean request. Do not address the renderer or leave private planning tags in the final prompt. Unlike a compact Midjourney exploration prompt, a 2.1 production description can be a substantial developed paragraph. Preserve a detailed user brief rather than flattening it into generic adjectives.

## Spatial construction — project procedure
For a poster or interface, plan the background, top band, left/center/right body and bottom band. Name every required block and align related blocks. For a single subject, plan its position, silhouette, pose, face/view, material/clothing and nearby interactions. Keep foreground, subject and background depth clear. Use counts instead of “several,” and say which items overlap. If an aspect is wide, give the frame useful horizontal relationships; if tall, use vertical hierarchy.

## Material and light
A material should have observable consequences: frosted glass diffuses the background; brushed metal has directional highlights; paper has grain and flat edges; knitted wool has loops and folds. Choose a coherent light source, direction, softness and shadow pattern. Avoid mutually contradictory styles such as purely flat vector with complex photographic lens blur unless the user explicitly asks for a hybrid. A mood word alone does not determine lighting.

## Text and layout
Quote exact visible strings using straight double quotes. Describe type weight, relative size, placement and reading order. Separate title, subtitle, labels and footer copy. For a chart, labels and data are actual content and must be supplied or clearly designated, not fabricated from the word “infographic.” If the user wants empty space for later type, describe a blank region rather than generating a placeholder heading. Respect Korean copy even when the picture description is English.

## Completion depth
Fill underspecified aesthetic choices only as far as the user's request allows. A simple subject study should not acquire extra animals, signage or unrelated props just to make a longer paragraph. For a publication-style composition, resolve layout and content into a concrete design. The 2.1 official T2I rewriter is more expansion-oriented than the edit rewriter; do not apply its density requirements to a tiny local edit.

## Size output
If emulating the official T2I enhancer, emit rewritten_prompt plus wh_ratio as separate data fields. The user-facing default can be a prompt block and a settings block instead of raw JSON. Only provide strict enhancer JSON when requested or when the existing template consumes that schema. Never paste a JSON object's braces into a plain prompt slot unintentionally.

Sources: original Qwen-Image model card; Qwen 2.1 T2I enhancer and rewrite README. Frame-construction steps are project writing guidance.
