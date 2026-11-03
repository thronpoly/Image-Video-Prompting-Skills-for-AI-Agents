# Behavioral checks

These cases are a review rubric, not proof of better generated images. Run each in a fresh agent context with only its selected skill and required inputs. Record the actual response, chapters read, tool calls, missing requirements and unsupported controls. Do not generate media unless separately requested.

| Case | User request | Required behavior |
| --- | --- | --- |
| MJ reference pattern | Attach a geometric print and ask for a similar Midjourney prompt | Describe visible motifs; identify Image Prompt for content/composition or Style Reference for aesthetic-only transfer; include minimum setup; do not invent URLs or add tile automatically |
| Qwen accessory transfer | Qwen 2.1 Edit: put glasses from image2 on the person in image1, preserving face, background and subtitles | Map canvas/donor and real input order, preserve requested details, do not borrow donor identity/background, use the selected route's syntax |
| Strict output | Midjourney: one red apple product photo, prompt body only | Return only the copyable prompt, without setup prose or generation |
| Exact lettering | Qwen poster with the title "푸른 새", no other lettering requested | Retain title verbatim, add no subtitle, date or venue |
| H3 reference motion | H3 R2V: reference mascot walks forward and waves in one shot | Read format and writing chapters, use six ordered sections, no invented cut or first-frame constraint, separate sound decisions |
| Turbo settings | Z-Image-Turbo: explain why a negative prompt has no effect | Distinguish no-CFG Turbo and pipeline/ComfyUI conventions; do not invent higher guidance as a fix |
| Execution boundary | Ask for a prompt using a selected existing workflow | No generation or workflow creation; when actual execution is requested, inspect existing slots and use MCP first |

For an efficacy study, compare skill-on and skill-off runs under the same model, request, inputs and generation settings, with repeated trials and blinded output review. Track request preservation, reference binding, invalid parameters, unnecessary tool calls and reading volume separately. A text-only review cannot establish visual quality.
