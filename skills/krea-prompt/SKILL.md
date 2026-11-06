---
name: krea-prompt
description: Krea 이미지 프롬프트 작성에 사용한다. Krea 2, FLUX.1 Krea 및 Krea 서비스 안의 타사 모델을 구분한다.
---

# Krea prompt authoring

A request to “write a prompt” authorizes drafting only. Return one copyable English prompt (keep literal dialogue/text in its original language), plus the minimum required attachment roles and non-default settings in the user's language. Treat strict “prompt body only / no explanation” as an explicit output constraint; otherwise do not omit setup needed to use references. Mark proposed settings as starting points. Do not invent files, URLs, controls or unsupported values. Preserve user-specified content, references and model.

## Start here

Identify whether Krea means the platform, Krea 1/2/3, FLUX.1-Krea-dev, or a LoRA on another base. A Qwen checkpoint with a Krea LoRA remains a Qwen input route. Preserve the selected model. For image prompts, specify observable content, framing, medium, materials, lighting and palette; keep exact text in its original language. Separate a style donor from subject identity and canvas. Native Krea 2 RAW and Turbo and hosted Krea 2/3 have different sampling/input contracts. Read parameters.md before numerical controls or endpoint fields; image-references.md and editing.md for actual image conditioning/changes. Do not switch to a newer hosted model to satisfy a missing capability.

## Read only what this task needs

For a straightforward request covered above, draft directly; do not load a general writing tutorial or all chapters. Use local chapters before source links. Browse only for uncovered versions/features, a real conflict, or a requested update. If relevant chapters are already in context and unchanged, reuse them.

For deeper composition help, use [prompt-writing.md](references/prompt-writing.md); for a missed requirement, [troubleshooting.md](references/troubleshooting.md). [guide.md](references/guide.md) indexes the full manual. [detailed-authoring.md](references/detailed-authoring.md) expands the authoring/execution contract; [sources.md](references/sources.md) records provenance. Resolve other chapter names above relative to `references/`. Snapshots are dated, not a live runtime guarantee.

## Execution boundary

Generate only when requested. For ComfyUI, use the connected MCP and only workflows in the user's saved list. Reuse the verified workflow and slots for follow-ups. If selection is needed, list names in the active user's saved workflow directory and inspect only relevant candidates. Explain missing capabilities.

For every ComfyUI model, revise from the original inputs and combine retained changes with the latest request. Keep generated images, videos and extracted frames out of the model's revision inputs. Use prior results for visual comparison. Change only inputs, prompts and exposed parameters. Keep output transformations in ComfyUI and obtain an explicit workflow request before creating or restructuring a workflow.
