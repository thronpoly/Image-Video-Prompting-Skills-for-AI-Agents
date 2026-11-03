# From a free-form brief to an H3 R2V prompt

## 1. Build the reference ledger
List only actual enabled inputs in their connection order: filename, modality, category index, supplied information and permitted changes. Inspect images for visible identity/material/layout. Inspect video for action, cuts and camera. Determine whether a supplied audio signal should be copied or used as a voice/music reference. If sound is unavailable, do not infer a transcript from the video image.

## 2. Separate invariants from the action
Identity is not a pose. A reference face, product silhouette, clothing or logo can remain stable while pose, view and scene change. Conversely, a requested transformation means the changing attribute must not be declared fully preserved. Write a small invariant list and a change list before constructing the formal fields. Do not describe an unknown back surface as verified reference detail.

## 3. Choose the actual task relationship
A new performance based on a person's image is reference generation. A still that must appear as a specific start/end/keyframe adds keyframe completion. Modifying an existing source clip is video editing. Extending beyond its end is continuation. Reusing the actual audio signal is audio reuse; a new voice with the source timbre is audio reference. A dance video supplying motion alone is not automatically video editing.

## 4. Design a feasible visual timeline
Map opening state → action onset → continuous development → settled result. Preserve the user's requested length and camera. A five-second shot should not include walking across a room, changing clothes, reading a paragraph and a long crane move. Prioritize the core action and scale secondary events to the time available. Plan each cut to introduce information. If the user requested a locked camera, keep all zoom, tracking, shake and reframing out of the description.

## 5. Fill the six fields
Define roles, state task summary, assign retention, then write the actual performance. Put the overall style opening before [Shot 1] in detailed_description. For normal generation, the official target is a substantial 350–500-word detailed description; use that space for meaningful staging, visible action and temporal continuity, not repeated praise. Dialogue-heavy tasks prioritize a complete speakable timeline. Editing complexity can justify a different length. A short compact example is not a substitute for this production form.

## 6. Ground every shot
Describe: framing and viewpoint; each important subject's visible reference cues and frame position; environment and light; current action and its consequences; a coherent camera behavior; relevant sound or speech. State what the viewer sees as the referenced feature becomes relevant. Repeat the subject label for continuity, not an entire redundant identity paragraph after each sentence. For occlusion, describe the subject exiting behind something and reappearing rather than teleporting.

## 7. Resolve camera intent
Zoom changes focal length; push/pull physically changes viewpoint; pan/tilt rotate; truck/pedestal translate; arc circles; tracking follows. Use direction and speed only where helpful. A camera tracking a walking person can keep their screen position steady while the background passes. A static shot of a walking person changes their position in frame. Distinguish those requests instead of using “camera fixed” and “tracks the character” together.

## 8. Validate the prompt as a contract
Every label must refer to an actual input or a clearly defined subject. Every retention line must agree with the requested edit. Every shot timestamp must be increasing and before the output ends. Exact text and dialogue must survive translation. Soundscape, score and synchronized events must agree. Finally compare the timeline against actual length/fps settings; the prompt cannot fix a wrong frame count or mismatched save speed.

Authoring heuristics above are procedural guidance. Formal H3 fields, language and syntax are specified in format.md and audio.md.
