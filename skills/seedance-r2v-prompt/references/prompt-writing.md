# Seedance temporal prompt authoring

## Parse the brief
Identify who/what, the actual reference roles, the intended action, setting, medium, camera and sound. Record immutable identity/design features separately from motion and staging. Determine whether the job is reference generation, edit, extension or a deliberate combination. If the user supplies a clip only as an action example, do not classify it as the source being edited.

## Construct the spatial and temporal plan
For each subject define a stable, discriminative name and source. Describe the initial visible state, action onset, meaningful intermediate motion and final state. For multiple subjects say who does what to whom, where they are and which object belongs to which person. Give the scene enough ground contact, perspective and light to make the interaction coherent.

For a complex clip use Shot 1 / Shot 2 / Shot 3 in order. The 2.0 official guide cautions that rigid per-shot timing is unstable; prefer a clear action sequence with natural pacing unless the user's intent specifically requires timed beats. Overall duration is still an actual execution parameter. Do not borrow MiniMax's exact timestamp grammar as a mandatory Seedance format.

## Observable action
Replace “moves beautifully” with the actual mechanics: lifts the right hand, turns the wrist, waves once, lowers it and settles. Distinguish actor movement from camera movement. A fixed-camera shot of an approaching subject makes the subject grow in frame; a tracking shot may hold scale while the background moves. Use one coherent primary camera path and define its start/end relationship.

## Camera and visual style
Define shot size/viewpoint first, then motion. A slow push toward a tabletop is different from an optical zoom. A pan reveals content to one side; an arc changes the subject's angle against the background. State static camera explicitly when requested and avoid conflicting tracking/zoom instructions elsewhere. Keep the visual medium stable: a realistic motion donor should not convert a requested drawn character into live action.

## Constraints
State the few constraints that matter: identity/design consistency, stable camera, intended material, no unrequested subtitles or an uncluttered background. Constraints should reinforce a feasible scene, not create a paragraph of unrelated prohibitions. Do not assume there is a separate negative_prompt field when the selected provider does not expose one. If text-free output matters, check whether source references already contain captions or logos; do not silently modify the input to remove them.

## Information density
Fit action count and dialogue length to the supported runtime. Remove competing secondary events before sacrificing the core action. Multiple characters need clear ownership, not more loosely labeled images. A heavy VFX request needs an effect's origin, shape, movement, timing and interaction with the environment, rather than a single “epic effect” tag.

## Final organization
Use a clear subject/reference preface, scene/action progression, camera/style and intentional sound. For a new source edit, begin by saying which video is being edited. For extension, identify the source and continuation direction. Use the selected version's asset and audio conventions from image-references.md and audio.md. Return actual parameter choices outside the prompt, with only relevant fields and no fabricated values.

Procedures above are project writing methods grounded in the official Seedance prompt guide's task, subject, action and storyboard distinctions.
