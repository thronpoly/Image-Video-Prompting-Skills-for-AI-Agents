# Writing a Midjourney prompt

## Turn the brief into a picture

1. Extract the irreducible subject, count, action, medium, setting, layout and exact text. Translate Korean intent into concrete English without changing named content.
2. Decide which visual relationship matters most. A centered product, two characters interacting, an architectural section and a textile pattern need different compositions.
3. Put the central image idea first. Bind each adjective to its subject: write “a red ceramic cup beside a blue glass bottle,” not a loose list of red, blue, ceramic, glass.
4. Add only useful environment, material, light and viewpoint information. Describe an actual scene, not the request to generate it. Eliminate repetitions and mutually exclusive camera/style instructions.
5. Select reference roles and parameters separately. End the prompt with supported flags. Recheck the model-specific compatibility chapter before shipping.

This process is an authoring recipe, not a required vendor syntax. Useful order:
`medium + subject/count + action + placement + setting + material/color + light + framing + supported flags`.

## Control the image through observable features

| Brief phrase | Convert into observable decisions |
|---|---|
| Expensive | Deliberate spacing, one material family, restrained highlights, precise product geometry |
| Friendly | Relaxed pose, rounded contours, open expression, low-contrast warm light |
| Dramatic | One directional source, deep shadow separation, a decisive camera angle |
| Clean | A single-color surface, a short object inventory, clear figure-ground separation |
| Retro | Name a medium/era and its visible print, color or photographic characteristics |
| Dynamic | A specific pose, direction and frame diagonal; do not merely add “dynamic” repeatedly |

Preserve a user-specified medium. Photorealistic does not mean maximal sharpness everywhere: depth of field, material response and coherent lighting matter. For illustration choose visible marks, shape treatment and palette; for a 3D object choose geometry, surface finish and light. Avoid mixing “flat vector” and “photorealistic depth” accidentally.

## Counts and spatial binding

Write exact small counts. Place distinct characters in separate regions and give each one distinguishable attributes. Express contact and gaze: “the taller figure on the left hands the envelope to the seated figure on the right.” Keep a single point of view. If one hand must hold an object, say which character and which hand. Extremely dense, exact diagrams are better treated as a layout/iteration problem than solved by adding a wall of adjectives.

## Text in the image

Put literal lettering in straight double quotes. Keep its language, capitalization and punctuation. Give one job to each text block: title at top, short secondary line below, product label on the bottle. Distinguish an empty area for later typography from a request to render type now. Do not add unwanted signage, brand names, captions or slogans. Short strings are easier to inspect. If a string is wrong, edit that string and its region rather than changing the whole aesthetic prompt. Never translate a Korean brand mark simply because descriptive prose is English.

## Reference-aware prose

For an Image Prompt or a Style Reference, describe the desired final scene. Do not write a vague “same as this but better.” For Edit Model, write the operation and scope: “Change the coat to dark green; retain the person's identity, pose and scene.” A new scene built from a character reference needs its setting described; “keep everything unchanged” would contradict the new scene.

## How much detail

Start concise for exploration; extend only where the result depends on a decision. Concision means removing low-value wording, not omitting identity, a crucial spatial relationship or a requested material. Provide one complete final prompt by default. Generate a set of alternatives only when asked or when the user is explicitly exploring directions.

## Final check

Can a person sketch the arrangement from the text? Are all mandatory elements present once, with clear owners? Does the framing fit the actual aspect? Are quoted strings exact? Is a motion instruction accidentally being used in a still-image prompt? Are version-sensitive flags and reference attachments valid? These checks usually help more than adding “masterpiece” or “award winning.”

Sources: Prompt Basics; Art of Prompting; Text Generation; Image Prompts. Full links in sources.md. Decision recipes and illustrative phrasing above are project authoring methods.
