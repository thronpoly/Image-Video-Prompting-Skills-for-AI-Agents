# Diagnose before changing a prompt

| Symptom | First diagnosis | Targeted revision |
|---|---|---|
| Reference face/product drifts | Wrong reference channel or competing aesthetic sources | Use V8 Edit Model or selected V7 Omni; state invariant design cues |
| Reference layout dominates | Image Prompt influence or reference crop is too strong | Reduce appropriate image influence; clarify desired layout |
| Right content, wrong visual language | Style channel absent or contradictory text | Choose a coherent style reference and remove conflicting medium words |
| Wrong count | Count omitted, multiple subjects bound ambiguously | State each subject and region explicitly; simplify nonessential objects |
| Colors exchange between objects | Adjectives detached from owners | Bind material/color directly to each noun |
| Text is garbled | Long string or dense typography | Shorten only if permitted; edit the text region and preserve exact requested string |
| --q rejected | V8 selected | Remove quality flag; choose SD/HD separately |
| :: weights ignored | V7/V8 selected | Rephrase as natural-language relationships or use an explicitly requested V6 route |
| V7 Omni plus Draft fails | Unsupported combination | Keep identity route and remove Draft, or discuss a different route |
| More detail changes the object | Creative upscale or engine handoff | Use source-faithful option and inspect design geometry |
| Seed does not reproduce character | Seed is not identity conditioning | Retain reference/profile along with full prompt and settings |
| Loop jumps | End pose, camera or velocity does not close | Plan a cyclic action and stable view; inspect timing after generation |
| Edit changes too much | Global description replaced a localized instruction | Name target operation and preservation scope; use bounded Editor region |

Keep a controlled revision log: failed criterion, suspected cause, one change, unchanged controls, observed result. Change medium, reference weight, seed and framing together only when intentionally redesigning. “Try more adjectives” is not a diagnosis.

Stop promising precision that the tool does not provide. Identity matching, exact text, hard region constraints, seamless loops and pixel-perfect preservation require output inspection. This is a prompt-authoring guide, not proof that an unexecuted image satisfies those requirements.
