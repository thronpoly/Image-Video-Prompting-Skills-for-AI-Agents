# H3 dialogue, voice and sound

## Three output layers
Use detailed_description for speech, singing and shot-synchronized effects. Use overall_soundscape for whole-scene ambience and ordinary physical sound. Use non_diegetic_music for music heard by the audience but not the characters. A radio playing in the scene is diegetic and belongs with the shot. Full silence is different from “no background music”: the latter still permits footsteps and room tone.

## Speaker syntax
Assign `(S1)`, `(S2)` in order of actual vocal events in the target. Reuse the ID for the same source across cuts and off-screen speech. A silent person needs no ID. For a referenced speaker use `<Subject 1> (S1)` at actual vocal events. When an Audio definition identifies a voice reference for that person, use the same ID rather than independently numbering audio speakers.

Write delivery outside the dialogue tag and words inside it:
```text
<Subject 1> (S1) speaks in a calm mid-range voice: <d>[Korean] 여기서 시작해요.</d>
```
This is an original example. Preserve the user's words and language; do not translate quoted speech because the surrounding prompt is English. Name pace and timbre concretely instead of “beautiful voice.” Keep line length speakable within the planned shot. Do not silently shorten user dialogue; flag a timing conflict and propose a shorter line or a longer supported clip.

## Voiceover and continuity
Use `says in an off-screen voiceover` for narration, with the corresponding visible character's lips remaining closed. A voice heard off-screen can retain the same speaker identity. For speech spanning a cut, use the documented `<scenetrans>` continuity marker and explicitly say the audio continues. For a deliberate truncation at the end use `<cutoff>`. Avoid these special markers when the sentence fits comfortably in one shot.

## Copying versus referencing sound
Copying an actual source signal is not a new performance. Voice timbre reference transfers vocal characteristics; it does not require importing the source's words. Rhythm reference does not automatically copy a song. Directly reused soundtrack verbal cues can be attributed to `<Audio N>` without inventing a separate on-screen speaker. If a person or narrator independently produces the voice, they need a stable speaker ID.

For incomprehensible source spans use an uncertainty marker such as `[unclear]` rather than hallucinating transcription. A user-supplied exact script overrides guessing from reference audio. Keep actual words faithful; do not carry decorative punctuation or markup into speech unless it is intended as content. If a script's punctuation needs normalization for model syntax, retain the original script separately and avoid changing words or meaning.

## Sound plan authoring
List the continuous ambience and each discrete event against the action. “A light tap when the cup touches the table” is temporally grounded; “cinematic audio” is not. For a score, name instruments, tempo and dynamics without claiming it changes visual motion. For no score use N/A in non_diegetic_music. For explicitly complete silence use N/A in both sound fields and state silence consistently in the shot. A downstream graph must actually include or omit the intended audio output; prompt text alone does not wire a decoder.

Source syntax: official base and reference guides. Sound-layer planning and timing checks are project methods.
