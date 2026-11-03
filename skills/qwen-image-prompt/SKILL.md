---
name: qwen-image-prompt
description: Qwen Image 이미지 생성·편집 프롬프트 작성에 사용한다. T2I와 Image Edit/2.1을 구분하고 다중 이미지의
  역할과 보존 조건을 명확히 한다.
---

# Qwen Image prompt authoring

A request to “write a prompt” authorizes drafting only. Return one copyable English prompt (keep literal dialogue/text in its original language), plus the minimum required attachment roles and non-default settings in the user's language. Treat strict “prompt body only / no explanation” as an explicit output constraint; otherwise do not omit setup needed to use references. Mark proposed settings as starting points. Do not invent files, URLs, controls or unsupported values. Preserve user-specified content, references and model.

## Start here

Distinguish T2I from Edit, 2.1 enhancer and community checkpoints. T2I describes the finished picture; editing names the operation and preserved content. Map every supplied image to canvas, identity, object, clothing, pose or style. Never copy a donor background/identity accidentally. For the 2.1 enhancer, multiple inputs use <image1>, <image2> in actual order; one input uses natural wording. Other implementations require their own convention. Follow the canvas aspect unless the user overrides it. An enhancer JSON wrapper is intermediate: extract rewritten_prompt and map size separately. Read editing.md and image-references.md for multi-input edits; parameters.md for any numerical sampling or size setting. Do not invent denoise/reference-strength controls.

## Read only what this task needs

For a straightforward request covered above, draft directly; do not load a general writing tutorial or all chapters. Use local chapters before source links. Browse only for uncovered versions/features, a real conflict, or a requested update. If relevant chapters are already in context and unchanged, reuse them.

For deeper composition help, use [prompt-writing.md](references/prompt-writing.md); for a missed requirement, [troubleshooting.md](references/troubleshooting.md). [guide.md](references/guide.md) indexes the full manual. [detailed-authoring.md](references/detailed-authoring.md) expands the authoring/execution contract; [sources.md](references/sources.md) records provenance. Resolve other chapter names above relative to `references/`. Snapshots are dated, not a live runtime guarantee.

## Execution boundary

Generate only when requested. Follow project instructions (AGENTS.md / CLAUDE.md): use the connected ComfyUI MCP first; inspect the selected workflow's real slots/defaults. Use a user-selected existing workflow or otherwise the official template; do not create/restructure workflows without an explicit request. Keep output transformations in ComfyUI. Missing tools require an explanation, not an unrequested generator substitution.
