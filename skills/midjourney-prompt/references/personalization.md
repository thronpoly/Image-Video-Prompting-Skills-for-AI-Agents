# Personalization, moodboards and style development

Personalization supplies a taste bias derived from a user's actual profile. A moodboard supplies an aesthetic direction collected from selected images. A Style Reference supplies the look of particular references or a real style code. None substitutes for defining subject, count, camera or layout in the prompt.

## Select by user intention

“Use my usual style” requires a known active personalization profile; do not invent one. “Match this campaign board” requires the board the user selected. “Use this picture's brushwork” normally calls for Style Reference. “Build three possible looks” is an exploration request; prepare alternatives without changing the user's account state or ranking images for them.

The web interface can enable personalization as a default or choose a profile per request. Existing profile/moodboard identifiers can be passed with --p. Preserve which profile was active in a reproducible job record. A profile being edited can change later results even when the same textual prompt is reused. For V8.2 the documentation states that the V7/V8 global profile is compatible; do not generalize that to every historical profile or model family.

## Moodboard use

Curate a coherent set by medium, palette, light, composition or subject treatment. Name which dimension should carry through, because a mixed board can contain incompatible cues. A board is not a list of specific product shapes to copy. Keep exact product or character references in their proper input channel. Style Weight --sw is incompatible with moodboards, so do not propose it as a moodboard intensity slider. Use the current board selection and supported controls instead.

## Style Creator and Profiles

Style Creator is an interactive preference process producing a reusable style direction/code. Describe the target look, compare meaningful alternatives and retain the actual resulting code after user selection. Do not fabricate a numeric code from prose. Personalization profiles let a user manage and select different aesthetic identities rather than pretending one general prompt fits all projects. Pin the intended profile or resulting code for a series; record it alongside the text and references.

## Iteration recipe — project method

First test content with modest stylistic interference. Then add one actual taste source and assess palette, marks, lighting and geometry separately. If identity weakens, remove competing aesthetic sources before increasing every strength. If style overwhelms a brand's exact color or object count, state those invariants and simplify the board. If the user wants a deliberate departure from their normal look, omit personalization for that job when authorized rather than fighting it through excessive wording.

Complete Tasks and ranking tools can contribute to personalization or available fast time, but they are not prompt syntax. Organizing and reviewing outputs is documented in web-tools.md. This skill does not change a user's preferences or run taste-training interactions without a request.

## Version and stacking details
The official Style Creator uses V7 previews. Existing --sref codes stay active when a new code is added, so reopening a coded image can stack styles instead of merging them. The article describes initial stabilization around 5–10 rounds, with diminishing changes later; these are interactive user decisions, not an automatic generation loop.

V8-specific personalization profiles do not run on V7, although the global V7 profile is compatible with V8.1/V8.2. Stylize controls personalization/moodboard influence: 0–1000, default 100. Moodboards are incompatible with both --sw and --sv. Profile IDs may convert to codes after submission; retain the real returned value rather than inventing one.
