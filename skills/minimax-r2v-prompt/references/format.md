# H3 full-reference format

## Canonical field order
Use ordinary text fields in this order, not a JSON object:
```text
subject_definitions:
[one definition per independently tracked content unit]

summary:
[task type] [target performance and main reference relationships]

retention_analysis:
[one relationship line per tracked item]

detailed_description:
[one or two sentences establishing the overall style]
[Shot 1] [opening shot and its development]
[Shot 2] At 00:03.500, [a genuine later cut, if needed]

overall_soundscape:
[ambience and physical sound, or N/A for explicitly complete silence]

non_diegetic_music:
[audience-only score, or N/A]
```
Square-bracketed drafting hints above are placeholders for the writer, not text to leave in a final production prompt. Do not invent a second shot merely to fill the pattern.

## Stable labels
`<Subject N>` identifies visible referenced content: a person, object, setting, garment, style, action or pose. `<Picture N>` identifies a concrete frame or layout anchor. `<Video N>` identifies an entire source clip or temporal/cut structure. `<Audio N>` identifies an active audio signal. Number each category separately. Subject 2 is not necessarily speaker S2. Once assigned, the definition must not drift across fields.

An image used only for identity appears as provenance inside its Subject definition. It needs a standalone Picture definition only when the frame itself has an independent anchor role. A source clip's motion can define a reusable Subject action; Video remains the whole-clip relationship. Do not create an Audio label simply because the file happens to contain sound.

## Task prefixes and retention
Supported task labels: reference generation; keyframe completion; video editing; video continuation; audio reuse; audio reference. Combine actual relationships with ` + ` inside one prefix. A directly edited video is introduced as the target being an edited version of the relevant Video label.

Visual relationship markers: `fully_preserved`, `partially_preserved`, `attribute_transfer`, `weak_reference`. Audio markers: `fully_copy`, `partially_copy`, `reference`, `weak_reference`. Use a marker and a plain English explanation of which property or signal survives. Scope fully_preserved to the item's defined role: a character identity can survive a new pose without requiring every original pixel. Do not put `(Sx)` in retention_analysis.

## Timeline syntax
[Shot 1] has no timestamp. Later cuts use `[Shot N] At MM:SS.mmm, ...` with increasing cut times inside the actual duration. A continuous single shot needs only one shot label. In full-reference mode, global style belongs before [Shot 1]; do not substitute the T2VA field integrated_multimodal_description for detailed_description.

## Output language
Write all explanatory prose in English. Keep actual dialogue/lyrics and visible on-screen text in their source language. Quote visible writing with straight double quotes. The H3 system distinguishes actual spoken content, reference provenance and final image text; do not conflate those categories. The formal field skeleton is constant, but its contents must adapt to the user's assets and controls.
