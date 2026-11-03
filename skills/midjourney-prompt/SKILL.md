---
name: midjourney-prompt
description: 미드저니(Midjourney) 이미지 프롬프트 작성·수정에 사용한다. 장면을 간결하게 정리하고 모델에 맞는 파라미터를 구분한다.
---

# Midjourney prompt authoring

A request to “write a prompt” authorizes drafting only. Return one copyable English prompt (keep literal dialogue/text in its original language), plus the minimum required attachment roles and non-default settings in the user's language. Treat strict “prompt body only / no explanation” as an explicit output constraint; otherwise do not omit setup needed to use references. Mark proposed settings as starting points. Do not invent files, URLs, controls or unsupported values. Preserve user-specified content, references and model.

## Start here

Describe the finished image, not an instruction to the assistant. For composition, content and palette inspiration, assign Image Prompt; for aesthetic/texture transfer, assign Style Reference. State the actual attachment role beside the prompt; never invent a URL or style code. The local snapshot defaults to V8.2; respect a selected version. Ordinary flags covered here: --ar for integer aspect ratio, --raw for less automatic styling, --s for stylization (0–1000, default 100). A proposed low --s is a trial, not an official preset. Express requested or inferred target framing with --ar, not prose alone; label inferred ratios as starting choices. Do not add chaos, tile or negative lists automatically. V8 does not support --q or :: weights; V7 Omni and V8 Edit are different routes. Read versions.md and parameters.md for other controls; image-references.md for mixed/ambiguous references or weights.

## Read only what this task needs

For a straightforward request covered above, draft directly; do not load a general writing tutorial or all chapters. Use local chapters before source links. Browse only for uncovered versions/features, a real conflict, or a requested update. If relevant chapters are already in context and unchanged, reuse them.

For deeper composition help, use [prompt-writing.md](references/prompt-writing.md); for a missed requirement, [troubleshooting.md](references/troubleshooting.md). [guide.md](references/guide.md) indexes the full manual. [detailed-authoring.md](references/detailed-authoring.md) expands the authoring/execution contract; [sources.md](references/sources.md) records provenance. Resolve other chapter names above relative to `references/`. Snapshots are dated, not a live runtime guarantee.

## Execution boundary

Generate only when requested. Follow project instructions (AGENTS.md / CLAUDE.md): use the connected ComfyUI MCP first; inspect the selected workflow's real slots/defaults. Use a user-selected existing workflow or otherwise the official template; do not create/restructure workflows without an explicit request. Keep output transformations in ComfyUI. Missing tools require an explanation, not an unrequested generator substitution.
