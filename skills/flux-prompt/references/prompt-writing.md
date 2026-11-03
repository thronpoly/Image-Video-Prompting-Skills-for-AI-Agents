# FLUX image construction

## Build the visual specification
Start with the main subject and action/pose. Establish the medium, setting, light and frame. Prioritize the detail whose failure would invalidate the result: exact product shape, number of figures, a camera relation, a text block or a material. Bind attributes directly to their subjects. A connected paragraph usually communicates these relationships better than an unstructured tag stack.

For example, a studio object needs geometry, material, scale, background and reflections; a documentary scene needs subjects in a plausible place and a coherent moment; an infographic needs regions, reading order and exact content. A prompt that only says “professional, high quality, 8K” leaves those decisions unresolved.

## Generation versus editing
For T2I describe the finished image. For an edit name the change to an actual input and what remains. A directive to remove an existing object is a valid edit instruction even though ordinary generation works best by describing the positive target state. Do not convert “remove the chair from this room” into an ambiguous T2I prompt about a completely new empty room.

## Medium, camera and light
Keep the user's medium. Use viewpoint and focal behavior as visual intent, not a claim of real camera metadata. Describe shallow focus only when it should blur parts of the scene. A flat illustration may use shape, line, grain and palette instead. Define a consistent light source and direction; ask surfaces to respond appropriately. For a product label that must be readable, avoid a viewpoint or glare pattern that hides it.

## Color and typography
Use concrete color names; when the user supplied a HEX code and the selected route supports color-specific prompting, bind it to the target surface. Exact pixel color still depends on shading, texture and output interpretation. Quote literal lettering in its original script. Specify type hierarchy and location, and distinguish a new generated text block from an existing label that must survive an edit. Do not insert a slogan simply because the composition resembles an advertisement.

## Complex scenes
Plan separate regions for multiple subjects, then state interactions and occlusions. A foreground product, background person and title should each have a clear role. If a precise position cannot be achieved reliably through text and the selected FLUX 3 route supports boxes, use layout.md. Boxes are not a substitute for coherent descriptions of how objects touch, overlap or fit the environment.

## Positive target states
FLUX generation routes documented here do not expose a universal negative-prompt field. Describe an unmarked package, an empty wall, a single subject or an open promenade rather than relying on a long forbidden-concepts list. Do not infer that a custom CFG graph or a newly released endpoint has the same field set. In particular, the current FLUX 3 Image API has neither negative_prompt nor prompt_upsampling.

## Refinement procedure — project method
Check inventory and relationships first, aesthetic direction second, fine texture last. Change one meaningful clause or control at a time. Keep seed, version, canvas and reference order fixed for a comparison. Use the requested resolution after the design is understood, while recognizing that rerendering at another size can change composition. No text prompt is evidence that an ungenerated result meets its exact text/identity requirements.
