# Qwen failure diagnosis
| Symptom | Likely issue | Change |
|---|---|---|
| Local edit redraws the face | Entire scene re-described or wrong canvas | Lead with the edit and preserve identity by source |
| New scene keeps old background | Local-edit preservation used for scene creation | Define identity donors and construct the new scene |
| Edits too weak | Preservation language suppresses requested change | Name the changed attribute decisively; preserve only other attributes |
| Donor face/clothes leak | Reference roles underspecified | Assign source, target and transferred attribute separately |
| Wrong reference gets edited | Input order differs from image tags | Verify actual connection order and canvas pointer |
| Crop follows isolated object | ratio_follow points at donor | Follow canvas or choose an explicit target aspect |
| Korean lettering changes language | Prompt-language decision mixed with visible-text language | Preserve quoted strings and decide descriptive language separately |
| Output contains JSON-looking text | Enhancer wrapper fed directly to diffusion | Extract rewritten_prompt; map size fields outside the prompt |
| Turbo ignores changed step count | Saved schedule still active | Follow Turbo's documented schedule rather than an ordinary base-model setting |
| Transparency is a checkerboard | RGB depiction instead of real alpha | Verify checkpoint support and output channels |
| Quality changes identity | Unrequested beautification/cleanup | Remove unrelated enhancements and constrain the actual target |

Check requested change, untouched content, literal text, source ordering, framing and output format separately. A correct text directive cannot compensate for a missing image input or an incompatible node family.
