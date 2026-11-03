# Seedance audio and visible text

## Intent before symbols
Distinguish new dialogue, a borrowed voice timbre, an actual reused recording, ambience, effects, music and subtitles. Reference audio does not automatically mean all source words or background music should be copied. Name what to borrow and what not to borrow. A source video's soundtrack may be irrelevant to a motion-only reference.

The official 2.0 guide and 2.5 tutorial describe these information markers: parentheses for music, angle brackets for sound effects, braces for dialogue, and `【】` for subtitles. For dialogue in a language other than Chinese/English, explicitly name the language. Do not substitute MiniMax `<d>[Language]` tags or its S-number rules as mandatory Seedance syntax. A provider accepting simpler quoted dialogue can have its own convention; use the selected route's documented form consistently.

## Original syntax example
```text
The presenter says in Korean {오늘은 이 제품을 소개할게요.} <A light tap is heard as the cup meets the table.> (A restrained piano pattern plays quietly.)
```
These are independent layers. If no subtitles were requested, omit the subtitle marker and state the intended clean screen if relevant. If subtitles are requested, provide the exact visible string in `【】` with position/style, not an inferred English translation.

## Voice reference
Bind the voice to a specific character and actual Audio input. “Reference only the warm mid-range timbre of Audio 1” differs from “reuse Audio 1 as the soundtrack.” Supply exact new words and a feasible delivery rate. A more emotional line should alter pitch/dynamics naturally without changing speaker identity. Do not infer a transcript from an audio file you cannot inspect.

## Dialogue pacing
Count the meaningful syllables/phrases and leave time for the intended physical action and pauses. Do not pack a long script into a short duration by silently accelerating it. If the user requires an exact script, preserve it and explain a runtime conflict. For multi-speaker scenes, use stable subject names, turn-taking and reactions. Each line must belong to an identifiable speaker; avoid attaching every utterance to “the person.”

## Music, effects and synchronization
Specify music by instrumentation, rhythm, volume/dynamic development and whether it is heard within the scene. Place discrete sound effects with visible events. A synchronization request needs both an actual reference signal and a described visual beat. Referencing rhythm is not guaranteeing sample-exact alignment. Generation_audio true/false is an actual provider control; configure it where exposed. Full silence is different from no score.

## Unwanted text or sound
The official guide notes subtitles can appear without being requested; prompt constraints reduce this risk but do not guarantee elimination. Inspect source material for embedded type before blaming only the target sentence. A user-approved input cleanup would need a supported ComfyUI operation. Do not suggest external cropping/removal scripts as an automatic remedy. Final output inspection must check dialogue wording/language, speaker identity, synchronization and any unintended text.
