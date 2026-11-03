# Website operation and finding creative controls

This chapter covers the website portions of the requested Documentation category. It intentionally omits Discord command operation and policy/account/billing material.

## Create

The Imagine bar accepts the scene text, web reference attachments and supported trailing parameters. Use the settings panel for model/version, aspect, stylization and eligible execution options. Text flags and selected defaults can interact: state important per-job values explicitly and inspect the actual job metadata. Creation Actions expose variations, rerun, editing, animation and upscaling as appropriate to the source result. Reusing a prompt is different from reusing its image and references; confirm the selected reuse action.

## Inputs

Open the image panel and place each uploaded file in the correct reference area: Image Prompt, Style Reference, Edit Model attachment, or Animate. Locking an input keeps it available across jobs; this persistence can contaminate an unrelated prompt. Check for accidentally retained attachments or a default personalization profile when results do not match the new brief. Removing an attachment from a job is different from deleting the user's upload.

## Describe

Describe extracts possible prompt directions from an image. It is useful for vocabulary and discovering composition/style cues, but it is not a pixel reconstruction recipe or proof of an artist/model identity. Inspect the image and choose useful observable phrases. Update-specific Describe output can be longer; do not take every generated detail as ground truth. Preserve a supplied brand string even when an automatic description misreads it.

## Draft and conversation

Draft is an exploration mode; conversational input can rewrite a loose instruction into a prompt. Inspect the resulting text before treating it as an exact interpretation of the user's brief. Draft/Conversational availability is version-specific and incompatible with V7 Omni. A V7 draft can be enhanced through the current action rather than assumed to equal a final rendering with the same pixels. The manual's direct authoring route already does brief-to-prompt translation; automatic service rewriting is a separate layer worth recording.

## Organize and folders

Use Create for recent job work and Organize for finding prior outputs, filtering and reviewing a series. Folders group selected creations and support project management; they are not model conditioning. Likes/favorites, archive and delete affect organization differently; do not perform destructive library actions merely to tidy up a generation task. Profiles and moodboards hold aesthetic information and should not be confused with folders containing deliverables. Existing job details can recover prompt, source settings and seed for a controlled comparison.

## Profiles, tasks and transition from Discord

Profile pages expose a creator's work and aesthetic context. Complete Tasks/rating activities can affect personalization or available resources but do not replace subject-reference inputs. A user moving to the web should translate a prior job into text + attachment roles + web settings, rather than pasting command prefixes into the Imagine bar. Stealth/public visibility and GPU scheduling are separate from image content. Preserve them unless the user asks to change them.

## Settings record

For a repeatable series retain: source filenames and reference slots; exact prompt; model/version; aspect and SD/HD; active personalization/board/style codes; influence values; seed; relevant variation/edit action; intended output location. A saved seed alone is insufficient.

Use ComfyUI for execution when the user requests it and a corresponding connected integration exists. A web-only Midjourney capability is not evidence that `comfy_local` exposes it. This skill can still author a web-ready prompt and attachment/settings instructions; it must describe an execution limitation instead of fabricating a ComfyUI node.

## Specific web controls in this snapshot
The public Profile Page is distinct from a personalization profile. Eligible profile pictures use 1:1 framing and banners 11:3, with V7/Niji 6 creations using a personalization, moodboard or Style Reference. Eligible images may be animated for profile use. These account-presentation actions are performed only when requested.

V8.1/V8.2 web Draft produces a batch of 24 lower-resolution 512-square images; V7 Draft produces four at reduced processing cost. Do not assume every Draft mode is the same four-image batch. Do not select a draft automatically for a final-quality deliverable.

In Editor, choose the active layer before moving, scaling or masking it. Smart Select creates a selection; apply Erase Selection or Erase Background before submission. A still-green highlight is not an applied erase mask. Move/Resize changes placement, scale, rotation and frame extent; Erase/Restore changes regenerated areas. Layered compositions flatten on submit. For older-editor behavior, transparent areas are regenerated while visible content is retained; use the documented Retexture or V8 Edit Model route for a whole-image medium change. Uploaded/layered edits may require upscaling to appear in Create/Organize.
