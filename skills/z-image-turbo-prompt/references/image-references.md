# Reference-informed Z-Image requests

## Three different situations
1. The user gives an image to communicate a look. Inspect its observable palette, material, composition and lighting, then write a corresponding text prompt. This is reference-informed authoring by the assistant, not image conditioning by Z-Image-Turbo.
2. The selected official template actually has an image/conditioning input. Verify what that input controls and whether it belongs to a compatible model variant. Map only the supported input and exposed strength values.
3. The user requests a precise edit or preservation of an existing face/product. A plain Turbo T2I prompt cannot promise those constraints. Explain the required editing/conditioning capability and keep the selected workflow unchanged unless a change is authorized.

## Extract useful visual evidence
Record the image's main subject, count, orientation, dominant geometry, palette, light direction, medium and crucial spatial relationships. Preserve the original medium if requested. Avoid guesses about invisible details, exact materials that cannot be identified, photographer/lens metadata, or a real person's identity. A prompt can say “soft overhead light” based on visible shadow behavior; it should not claim camera EXIF that was never provided.

## Multiple references as a design brief
Create a role table: A supplies silhouette, B supplies palette, C supplies composition. Translate those roles into a coherent target description rather than inserting `<image1>` labels that the T2I model may not understand. If a precise identity transfer is essential, that role table exposes the missing native conditioning instead of hiding it. No universal per-image percentage is defined by this model's basic T2I interface.

## Avoid accidental copying constraints
A desired moodboard look is not a demand to preserve every depicted object. A user asking for the palette of an image should not inherit its pose, background and crop automatically. Conversely, when the user explicitly wants an exact object, a vague textual approximation must be labeled as an approximation. Keep layout inspiration, color inspiration, free reconstruction and actual editing distinct.

## Execution boundary
This manual does not authorize converting Turbo into an editing graph, adding a ControlNet, injecting a community adapter or preparing a composite image outside ComfyUI. If those capabilities are essential and not present in the official template, state that limitation and let the user decide. Prompt quality cannot substitute for an absent model input.
