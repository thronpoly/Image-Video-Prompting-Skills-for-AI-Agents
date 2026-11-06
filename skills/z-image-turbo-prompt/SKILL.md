---
name: z-image-turbo-prompt
description: Z-Image-Turbo(z_image_turbo) 이미지 프롬프트 작성·확장에 사용한다. Z-Image Base나 Edit의
  규칙과 구분한다.
---

# Z-Image-Turbo prompt authoring

A request to “write a prompt” authorizes drafting only. Return one copyable English prompt (keep literal dialogue/text in its original language), plus the minimum required attachment roles and non-default settings in the user's language. Treat strict “prompt body only / no explanation” as an explicit output constraint; otherwise do not omit setup needed to use references. Mark proposed settings as starting points. Do not invent files, URLs, controls or unsupported values. Preserve user-specified content, references and model.

## Start here

Target Z-Image-Turbo T2I, not Base/Edit. Describe the finished scene with explicit subject, composition, light, material and literal text. An attached image can inform the written description without becoming a model input: say so when that distinction matters. Do not promise editing or identity preservation through text alone. Standard Turbo disables CFG; a negative prompt has no guidance effect in that branch. Official pipeline guidance 0 and ComfyUI no-CFG 1 are route conventions, not interchangeable fields. Preserve the selected template. Read parameters.md for numerical settings (including the implementation-specific 8/9-step distinction), image-references.md for actual conditioning, prompt-writing.md for detailed expansion.

## Read only what this task needs

For a straightforward request covered above, draft directly; do not load a general writing tutorial or all chapters. Use local chapters before source links. Browse only for uncovered versions/features, a real conflict, or a requested update. If relevant chapters are already in context and unchanged, reuse them.

For deeper composition help, use [prompt-writing.md](references/prompt-writing.md); for a missed requirement, [troubleshooting.md](references/troubleshooting.md). [guide.md](references/guide.md) indexes the full manual. [detailed-authoring.md](references/detailed-authoring.md) expands the authoring/execution contract; [sources.md](references/sources.md) records provenance. Resolve other chapter names above relative to `references/`. Snapshots are dated, not a live runtime guarantee.

## Execution boundary

Generate only when requested. For ComfyUI, use the connected MCP and only workflows in the user's saved list. Reuse the verified workflow and slots for follow-ups. If selection is needed, list names in the active user's saved workflow directory and inspect only relevant candidates. Explain missing capabilities.

For every ComfyUI model, revise from the original inputs and combine retained changes with the latest request. Keep generated images, videos and extracted frames out of the model's revision inputs. Use prior results for visual comparison. Change only inputs, prompts and exposed parameters. Keep output transformations in ComfyUI and obtain an explicit workflow request before creating or restructuring a workflow.
