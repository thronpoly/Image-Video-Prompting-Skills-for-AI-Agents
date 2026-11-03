# Midjourney image-to-video

Use this chapter only for Midjourney's own video route, not MiniMax or Seedance. Start with an actual image. Choose whether it supplies only the starting state, both loop endpoints, or a start paired with a separate ending frame. The animation prompt should state what changes over time and what the camera does; avoid spending the whole prompt re-captioning the still.

## Motion plan

Use `initial state → action onset → development → final state`. Bind motion to the subject: an object rotating, a person waving, cloth moving in wind. State one coherent camera path. Low Motion favors restrained activity; High Motion allows larger movement and can increase distortion. The final frame does not prove an exact cyclic velocity match. A loop request should also describe a reversible/periodic action and stable camera/background.

## Controls

--motion low or --motion high selects motion behavior. --loop uses the starting image as an ending target. --end supplies an actual custom ending frame. --bs controls the number of videos returned, using supported choices in the current interface. SD/HD availability, batch size and scheduling are model/plan controls; do not borrow image --q as a video quality setting. Starting with an external image requires the correct Animate input slot, not a Style Reference slot. Manual animation permits a custom motion prompt; automatic animation derives one from the image.

The official article describes five-second initial clips and iterative four-second extensions, with a maximum of four extensions and a total up to 21 seconds. Check the interface's available action when planning an extension. A longer requested deliverable needs an explicit continuation plan; adding “15 seconds” to the sentence alone does not select a supported duration. Distinguish the original start-frame job from each extension and its prompt.

## Original example

Assume the supplied still depicts a paper lantern above a table:
```text
The paper lantern gently sways once to the left and returns toward its starting position. Its warm light stays steady while a soft shadow moves across the tabletop. The camera remains locked, with unchanged framing and focus throughout. --motion low --loop
```

For a new final frame, inspect whether the beginning and end can be reached through continuous geometry. If the start is a close portrait and the end is a distant building, decide whether the user expects a camera reveal, transformation or cut instead of assuming an effortless interpolation. Parameters that require image URLs must use actual attached assets; never ship example URLs as working references.

Source: Video article, sources.md. The motion planning procedure and example are project authoring guidance.

## Output count
--bs accepts 1, 2 or 4, default 4 in the recorded article. This controls number of clips, not duration. Choose one for a user-authorized single controlled test when appropriate; do not generate four by accident because a generic example omitted batch size.
