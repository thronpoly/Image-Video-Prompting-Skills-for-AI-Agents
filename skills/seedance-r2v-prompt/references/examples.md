# Original Seedance examples

## A. Appearance plus motion, 2.0
Inputs: Image 1=blue mascot; Video 1=walking motion only. Intent: a new scene, not editing the dancer's source clip.
```text
Define the compact blue mascot in Image 1 as the main character, preserving its round head, body proportions and cream scarf. Reference only the measured walking action from Video 1, not its performer, setting or camera. In a quiet station platform scene with soft daylight, the mascot walks toward the viewer, slows to a stop, raises its right hand and gives one small wave, then lowers the hand and settles. The camera remains locked at eye level with unchanged framing. Maintain the same three-dimensional animated style throughout. <Soft footfalls and a faint cloth rustle accompany the action.> No background music or subtitles.
```
Choose a supported overall duration separately. Do not force per-shot microseconds into an action that needs natural pacing.

## B. Product animation with a distinct camera donor
Inputs: Image 1=ceramic mug; Video 1=slow arc camera.
```text
Use the mug in Image 1 as the product reference, retaining its handle shape, proportions, glaze and exact printed mark. Reference only the slow arc movement from Video 1. The mug remains stationary on a cream tabletop as the camera moves gently from a frontal three-quarter view toward its right side, revealing the curve of the handle. Soft left-hand studio light stays consistent and the background remains a smooth ivory field. The movement settles into a clear final product view.
```
The mug does not rotate merely because the camera moves. Inspect the mark if brand fidelity is required.

## C. New line in a referenced voice, 2.5
Inputs: @Image 1=presenter; @Audio 1=voice timbre only.
```text
Use the presenter in @Image 1 as the appearance reference. Reference only the warm mid-range vocal timbre of @Audio 1, not its original spoken words or background sound. In a softly lit studio, the presenter faces the camera, gestures once toward the table and says in Korean {오늘은 이 제품을 소개할게요.} The presenter closes their mouth after the line and holds a relaxed pose. Keep the camera fixed and the screen free of subtitles. <Low studio room tone remains audible.>
```
Use generate_audio true where exposed. This is a new spoken performance rather than copying the original recording.

## D. Source edit, 2.5
Input: @Video 1=existing product clip.
```text
Edit @Video 1. Change only the red tabletop cloth to muted navy linen throughout the clip. Preserve the product, hand movement, camera motion, scene timing and other visible elements. Let the new fabric's folds and shading follow the original cloth's motion while retaining the rest of the scene and original audio.
```
Parameters: task edit, adaptive ratio, duration -1 on the supporting 2.5 route. A new requested ten-second output would conflict with source-duration-preserving editing.

## E. Continue from a source ending
```text
Extend Video 1 by continuing after its final moment. The mascot completes its existing wave, lowers the hand and turns its gaze toward the arriving train without changing position on the platform. Continue the source's fixed camera, soft daylight, animated style and low platform ambience. Do not restart the earlier approach or replay the original wave.
```
Inspect the actual source ending before using this text. If it ends mid-step, the continuation must finish that step instead.

## F. Structured two-shot demonstration
```text
Use the silver kettle from Image 1 as the same product in both shots. Shot 1: A close tabletop view shows a hand lifting the kettle by its handle under soft studio light. Shot 2: Cut to a side view as the spout tilts over a white cup and a thin stream of water enters it. Preserve the kettle's design and finish, with consistent table surface and lighting across the cut. <A light handle movement and gentle pouring sound accompany the action.>
```
This describes event order without imposing a rigid frame-level schedule. Add a user-required total duration in actual controls.

## G. Image sequence reference
```text
Use the three panels in Image 1 as successive story beats of the same character, not three simultaneous copies. First the character notices the folded note, then picks it up, then smiles after reading it. Retain one consistent identity and setting throughout, with a single gentle camera push toward the character.
```
If the sheet is ambiguous about identity or order, clarify it before execution rather than treating every panel as an independent actor.
