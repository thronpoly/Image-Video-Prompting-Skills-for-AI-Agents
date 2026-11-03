# Reference images: choose the right channel

## Role selection

| What the user wants to carry over | Channel | What to write |
|---|---|---|
| General content, palette or composition inspiration | Image Prompt | A description of the complete target picture |
| Palette, medium, texture, lighting aesthetic | Style Reference | New content with non-conflicting style language |
| Specific person/object in a new picture on V8 | Edit Model attachments | Which reference supplies which subject and the new scene |
| One person/object reference on V7 | Omni Reference | Target scene plus identity/design cues |
| A curated aesthetic spanning many images | Moodboard | Target content; select the existing board |
| Precise change to an existing picture | Quick Edit / Editor | Change instruction and preservation scope |
| Animate this still | Video starting frame | Temporal development, not a second still-image caption |

Attach actual files in the website's appropriate slot. Record filename → role → attachment order. A single Image Prompt needs text; image-only blending needs at least two images. Typical accepted image extensions are png, jpg/jpeg, webp and gif. Matching reference crop and target framing reduces unintended composition conflicts. Do not crop or rewrite an input asset as a hidden convenience.

## Image Prompt strength

`--iw` changes overall Image Prompt influence, not a named object's individual strength. Documented default: 1. V7 and the V8.1 table: 0–3; Niji 7: 0–2. The table does not explicitly name V8.2: retain a user value within confirmed UI limits rather than inventing a different range. More influence can retain composition you meant to replace; less influence can loosen both palette and shape. An Image Prompt is inspiration, not pixel-preserving editing. Image-only jobs do not support stylize or weird.

## Style Reference

Use `--sref` only with actual image references or an existing style code. `--sw` ranges 0–1000, default 100; it is not compatible with moodboards. A style image does not preserve a person's face or an object's geometry. Keep target content explicit and avoid a competing list of unrelated style labels. `--sref random` explores a new code; do not use random when the user wants a fixed series. A code is not calculated from an uploaded picture. Style versions `--sv` are meaningful only within their documented model implementation; carry an existing value through rather than guessing.

## V7 Omni Reference

One reference image, a required text prompt, `--oref` and `--ow`. Weight 1–1000, default 100; the official article advises staying below 400 in ordinary conditions. It can combine with Style References and Image Prompts. The article excludes Draft/Conversational, --q 4, and several older region/outpainting actions; it also currently lists a Fast-mode incompatibility. Treat that as a recorded constraint, not a reason to silently switch models. Detailed logos/freckles are not guaranteed. Increasing identity strength can resist an intended style change. For edits to an Omni result, the documented route is Editor after removing the Omni reference and its flags.

## V8 Edit Model attachments

Up to four reference images. Decide whether one is a base canvas or whether all supply subjects for a newly composed picture. It normally follows the first image's aspect; provide `--ar` explicitly to override, because default aspect settings do not carry automatically. It can combine with Image Prompts, Style References, Personalization, Moodboards and HD. Preserve role ordering when regenerating the prompt. If subjects exchange clothing or faces, bind each role by image and visible description; a combined character reference is an optional preparation suggestion, not permission to create one automatically.

## Multi-reference planning example

Input A: product geometry. Input B: pastel print aesthetic. Requested result: an overhead poster.
Choose Edit Model attachment for A on V8; Style Reference for B; use text for the overhead view, product count and poster layout. Do not send both as anonymous Image Prompts and expect independent content/style weights. Keep actual URLs out of a web-ready prompt if the attachments already carry the references.
