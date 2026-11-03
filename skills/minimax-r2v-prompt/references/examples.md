# Original H3 production examples

All examples below are newly authored. Described assets are assumptions for demonstration; substitute the user's actual visible content. The example inference intent must be mapped onto the chosen template rather than treated as an executed result.

## A. Identity reference, one continuous performance
Assumptions: Picture 1 is a compact blue mascot with a round head and cream scarf. User requests approaching, waving and stopping, locked camera, no music. One subject reference; no first-frame constraint. Allow enough supported runtime for the complete action.

```text
subject_definitions:
<Subject 1> is the compact blue mascot in <Picture 1>, retaining its rounded head, short limbs, simple facial design and cream scarf.

summary:
[reference generation] <Subject 1> approaches the viewer along a quiet station platform, stops at a comfortable distance and gives one friendly wave. The image supplies identity rather than a fixed opening composition.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - the mascot's defining silhouette, blue body, facial design and scarf remain recognizable throughout the performance.

detailed_description:
The target video uses a softly lit three-dimensional animation style with a restrained blue-and-cream palette and a clear, uncluttered environment.
[Shot 1] A locked eye-level medium-wide view looks along a small railway platform. <Subject 1>, the compact blue mascot with the rounded head, short limbs and cream scarf from the reference, stands in the central background with its full body visible. The platform surface runs toward the camera in straight perspective, and a plain bench remains along the distant left edge. Soft daylight falls consistently from the right, leaving a gentle contact shadow beneath the mascot. Its face remains oriented toward the viewer, with a relaxed, welcoming expression and clearly separated eyes and mouth.
The mascot takes a small sequence of measured steps straight forward. Each foot lifts, swings and plants before the next step; its body rises and settles slightly with the walking rhythm. The short arms swing close to the body, while the cream scarf shifts subtly with the movement without changing its design. As it approaches, its apparent size increases naturally within the fixed frame. The bench and platform edges remain stationary, making the approach come from the character's movement rather than a camera zoom. Soft footfalls follow the planted steps.
Before reaching the foreground edge, the mascot slows, places both feet securely on the platform and settles its weight. It lifts its right hand to shoulder height, keeping its left arm relaxed beside its body. The raised hand moves gently from side to side in one compact greeting. The elbow stays near the torso so the gesture reads clearly without covering the face. The eyes continue looking toward the viewer. A faint cloth rustle accompanies the scarf settling after the last step.
The mascot lowers the hand and holds a comfortable upright pose for the ending. Its proportions, face and scarf remain consistent as the body comes to rest. The final moment gives a clean readable view of the same character, with quiet room-like outdoor ambience and no spoken line. The camera position, focal length and framing remain unchanged for the entire shot. Only a subtle breathing movement remains as the scene ends.

overall_soundscape:
Quiet platform ambience remains low and even. Soft footfalls and a light scarf rustle accompany the character's movement.

non_diegetic_music:
N/A
```

## B. Two image roles plus a new Korean line
Assumptions: Picture 1 supplies a presenter, Picture 2 supplies a silver kettle. User supplies the exact sentence. This is a compact format illustration; expand staging to normal production detail when using it for a full generation request.
```text
subject_definitions:
<Subject 1> is the presenter in <Picture 1>, preserving facial identity and the dark jacket.
<Subject 2> is the silver kettle in <Picture 2>, preserving its body shape, spout and handle design.

summary:
[reference generation] <Subject 1> introduces <Subject 2> on a studio table and delivers the supplied Korean line.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - identity and clothing remain consistent.
<Subject 2> (appears in [Shot 1]): fully_preserved - the product's defining geometry and finish remain consistent.

detailed_description:
The target video has a realistic studio-demonstration style with soft neutral lighting.
[Shot 1] In a static medium shot, <Subject 1> stands behind a plain table with <Subject 2> placed on the right side of the frame. The presenter rests one hand beside the kettle without covering its handle or spout. <Subject 1> (S1) looks toward the viewer and says in a clear conversational voice: <d>[Korean] 오늘은 이 제품을 소개할게요.</d> The presenter's mouth closes after the line, then the hand makes one small open-palm gesture toward the kettle. The product remains at its original scale and position.

overall_soundscape:
Low studio room tone and a faint sleeve movement remain audible.

non_diegetic_music:
N/A
```

## C. Role-aware repairs
Bad instruction: “Copy Picture 1 exactly but turn the person into a different character and keep everything unchanged.”
Repair: decide which identity is canonical. If only costume changes, define the same Subject identity and mark the costume's modified role as partially_preserved. If a new character replaces the original, do not mark the original face fully_preserved.

Bad instruction: “Use the dance clip and its music, but only copy the motion.”
Repair: ask whether the actual audio signal is wanted. For motion-only, remove Audio definitions and audio-reuse claims. For actual music reuse, bind the supplied Audio signal to the score phase and record its copy relationship. Never infer that a connected video soundtrack was intentionally enabled.
