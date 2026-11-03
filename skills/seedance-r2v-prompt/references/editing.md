# Seedance source editing and continuation

## Task language matters
For a new reference performance, say which dimensions to reference. For source editing or extension, directly identify Video N as the source to edit/extend; the 2.0 guide warns that “reference Video N” can be classified as a new reference-generation task instead. A combined task can borrow an attribute from one asset while strictly editing a different source.

## Edit operations
Add: element design, location, appearance time and relationship to action. Remove: exact target and what remains/replaces the exposed region. Modify: original property → requested property while retaining timing, other subjects and source composition as appropriate. Restyle: target medium and structural invariants. Audio edit: target vocal/music/effect layer and the visuals that remain. For a small source edit, avoid re-authoring an entirely different plot.

## Seedance 2.5 constraints
`omni_reference_task_type` can explicitly select reference, edit or extend, with auto also available where exposed. The prompt must agree with the selected task; a mismatch can fail asynchronously. Editing requires a source reference_video, aspect ratio adaptive and duration -1, keeping approximately the selected source length. Extension needs a source reference_video and adaptive framing. This differs from an ordinary reference generation where a concrete supported ratio/duration can be chosen.

## Continuation procedure — project method
Inspect the end state: subject placement, pose, movement direction, camera speed, light, ongoing sound and unfinished action. Start the continuation from that state. Describe the next change rather than replaying the entire previous plot. Keep a continuous camera unless a cut is intended. An extending subject should not suddenly reverse direction or reset facial expression without an event causing it. For backward/prepending extension, state that content leads into the known beginning; use unambiguous before/after wording rather than relying on an English “forward” that might be interpreted differently.

## Connecting several clips
Define the order and the transition between each source. Decide whether source clips themselves remain in the output or only their transition is generated; provider continuation behavior can vary. A transition should account for space, subject identity, sound and motion, not simply say “seamless.” If clips have incompatible visual styles or aspect ratios, clarify which is canonical before generation. Do not silently crop or recolor them externally.

## Quality and seam checks
Repeated extension can accumulate detail drift and timing discontinuity. Use a supported first/last-frame or source-video continuation profile deliberately, not a generic text prompt plus a guessed trim. Inspect the seam for identity, posture, camera velocity, object continuity and audible jumps. If the selected official template does not expose required source/length/postprocessing controls, explain that limitation without building a substitute graph.
