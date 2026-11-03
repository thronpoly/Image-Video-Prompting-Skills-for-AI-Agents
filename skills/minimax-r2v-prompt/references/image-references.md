# H3 multimodal references

## Input inventory and supported quantities
Official H3-Base-Ref2VA model card: at most 9 images, 3 video clips and 3 audio clips, with at most 12 files across modalities. Each reference video/audio clip is 2–15 seconds and each modality's total duration is at most 15 seconds. This is a documented model profile, not permission to assume every API or custom loader accepts the same inputs.

## Role matrix — project decisions
| Asset intent | Definition | What the output may change |
|---|---|---|
| Product identity photo | Subject with Picture provenance | View, environment and pose; not requested invariant geometry |
| Several views of one mascot | One Subject citing each supplied view | New motion with a single stable identity |
| Final pose still | Standalone Picture endpoint; subjects defined separately | Continuous path into the final frame |
| Storyboard sheet | Picture with explicit shot assignments | Only the assigned composition/order information |
| Dance demonstration | Action Subject and/or Video structural role | Performer appearance unless it is separately an identity source |
| Existing clip to edit | Video source plus needed visible Subjects | Only requested changes |
| Source for an extension | Video continuation source | New action beyond the inherited state |
| Voice example | Audio timbre role bound to an actual speaker | New dialogue unless copying was requested |

Use multiple views to disambiguate one identity, not as multiple clones. When image A supplies face and image B supplies costume, say which attribute comes from each and preserve one character. When two people must remain separate, use separate Subjects and spatial/interaction binding. Do not use a high-level “combine images” sentence as the whole instruction.

## Provenance and ordering
Write the attachment table before the prompt for complex tasks. Example: portrait.png → Picture 1 → Subject 1 identity; coat.png → Picture 2 → Subject 1 clothing; walk.mp4 → Video 1 → motion only. Preserve the actual connection order when setting the template's input filenames. A reordered loader changes index meaning even if the words are unchanged. Disabled references must not remain in the active numbering.

## Reference sizing and evidence
Resolution is not reference strength. A large reference may reveal identity detail but also carries more input cost or local compute. The native node snapshot has match/max reference sizing with different computational load; see parameters.md. An image label without the actual image cannot transfer geometry. Likewise, an audio label without an audio signal cannot supply a voice. Report that missing conditioning rather than writing a more elaborate claim.

## Keyframes versus inspiration
A free identity reference does not determine frame zero. If the user wants the exact first frame, use the route that actually supports the anchor; if the selected official template exposes only free references, explain the limitation. Never redesign the graph to add keyframes without authorization. A prompt describing identical start/end states expresses intent; it does not prove an exact seamless loop or a supported endpoint constraint.

## Input conflict resolution
If two images disagree on identity, ask which is canonical or assign distinct roles. If style and material conflict, preserve what the user made immutable. If a source video camera conflicts with an explicitly locked target camera, borrow the actor motion only. Write those selections into retention_analysis and the actual shot, rather than leaving a contradiction for the model.
