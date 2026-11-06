---
name: flux-prompt
description: FLUX 이미지 생성·편집 프롬프트 작성에 사용한다. FLUX.1, Kontext, FLUX.2/Klein 및 다른 버전의
  공통 원칙과 버전별 기능을 구분한다.
---

# FLUX Image prompt authoring

A request to “write a prompt” authorizes drafting only. Return one copyable English prompt (keep literal dialogue/text in its original language), plus the minimum required attachment roles and non-default settings in the user's language. Treat strict “prompt body only / no explanation” as an explicit output constraint; otherwise do not omit setup needed to use references. Mark proposed settings as starting points. Do not invent files, URLs, controls or unsupported values. Preserve user-specified content, references and model.

## Start here

Identify the route: FLUX.1 generation, Kontext edit, FLUX.2/Klein or FLUX 3 Image. Keep checkpoint/provider contracts separate. Generation describes the result; edits name the change and preserve defining subject geometry and unrelated scene content. Assign each image its actual role and order. Do not invent reference counts, weighting syntax or negative_prompt support. Do not copy hosted FLUX 3 limits into native FLUX.1/2 or confuse guidance nodes with sampler CFG. Read image-references.md and editing.md for actual multi-input/edit tasks; parameters.md for numerical controls; layout.md only for supported FLUX 3 box layouts. A Krea adaptation does not change the base model's input contract by name alone.

## Read only what this task needs

For a straightforward request covered above, draft directly; do not load a general writing tutorial or all chapters. Use local chapters before source links. Browse only for uncovered versions/features, a real conflict, or a requested update. If relevant chapters are already in context and unchanged, reuse them.

For deeper composition help, use [prompt-writing.md](references/prompt-writing.md); for a missed requirement, [troubleshooting.md](references/troubleshooting.md). [guide.md](references/guide.md) indexes the full manual. [detailed-authoring.md](references/detailed-authoring.md) expands the authoring/execution contract; [sources.md](references/sources.md) records provenance. Resolve other chapter names above relative to `references/`. Snapshots are dated, not a live runtime guarantee.

## Execution boundary

Generate only when requested. For ComfyUI, use the connected MCP and only workflows in the user's saved list. Reuse the verified workflow and slots for follow-ups. If selection is needed, list names in the active user's saved workflow directory and inspect only relevant candidates. Explain missing capabilities.

For every ComfyUI model, revise from the original inputs and combine retained changes with the latest request. Keep generated images, videos and extracted frames out of the model's revision inputs. Use prior results for visual comparison. Change only inputs, prompts and exposed parameters. Keep output transformations in ComfyUI and obtain an explicit workflow request before creating or restructuring a workflow.
