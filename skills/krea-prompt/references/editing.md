# Krea editing and enhancement decisions

Use actual edit instructions only in a selected route with image editing support. “Krea” as a platform can host several unrelated editors; choose the model already selected in the user's context. Krea 2 native T2I does not become an editor because the platform has an Edit page.

For a local edit, name the target, operation, new attribute and preservation scope. For a composite, identify the canvas and each donor, then state positioning, scale, contact, occlusion and matching illumination. For a new subject-driven composition, describe the new scene and preserve only necessary identity/design cues. For style transfer, allow medium/texture to change while retaining requested geometry. Repeatedly saying “unchanged” should not suppress the very attribute being edited.

Krea 3's documented regional_edit flag aims at local changes with a berry model and actual input images. It is not proof of an exact user-drawn mask, a universal per-pixel lock or independent image weights. Use only exposed controls. If the user requests three distinct edits, ensure the target ownership is clear; use a structured sentence or staged operations when the supported UI warrants it.

An enhancer/upscaler is a separate route from generation. Resolve whether the user wants faithful detail recovery or creative reinterpretation. Preserve brand geometry, logos, facial identity and composition when faithful enhancement is requested. A vague “more detailed” instruction can add invented texture. Actual output scale, creativity and resemblance controls are model-specific. Do not borrow a Krea Enhancer interface range for native Krea 2 sampling, or treat changing image DPI as adding pixels.

For real-time sketch/canvas input, distinguish the visual guide from typed instructions and identify the selected realtime model. The same prompt may react to changing canvas geometry without a text change. This manual supports constructing that prompt; it does not promise the realtime controls exist in the official local template.

For outpainting, specify the expansion direction and desired new frame separately from the prompt describing the revealed space. Keep the original subject at its requested size/position. For transparency, verify an actual alpha-capable output rather than describing a checkerboard. For text, preserve literal copy and inspect spelling after editing.
