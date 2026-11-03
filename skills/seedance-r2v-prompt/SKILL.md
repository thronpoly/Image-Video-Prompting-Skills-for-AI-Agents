---
name: seedance-r2v-prompt
description: Seedance 참조 기반 영상(R2V/omni reference) 프롬프트 작성에 사용한다. 2.0/2.5와 제공 서비스의
  참조 표기법을 구분한다.
---

# Seedance R2V prompt authoring

A request to “write a prompt” authorizes drafting only. Return one copyable English prompt (keep literal dialogue/text in its original language), plus the minimum required attachment roles and non-default settings in the user's language. Treat strict “prompt body only / no explanation” as an explicit output constraint; otherwise do not omit setup needed to use references. Mark proposed settings as starting points. Do not invent files, URLs, controls or unsupported values. Preserve user-specified content, references and model.

## Start here

Preserve the selected version and provider: ModelArk, another host and Comfy Router can expose different fields. Reference generation, video editing and continuation are distinct tasks. For final R2V prompts, read prompt-writing.md and image-references.md for reference syntax, modality-local numbering and timeline construction. Bind each source to its intended identity, appearance, motion, framing or audio role. Do not use MiniMax's six-section syntax. Read audio.md for dialogue/music/soundtrack requests; editing.md for edits/continuation; parameters.md for duration, resolution, seed or provider options. Do not invent cross-provider seed support or treat first-frame input as generic reference. Keep requested duration separate from timestamps in prose.

## Read only what this task needs

For a straightforward request covered above, draft directly; do not load a general writing tutorial or all chapters. Use local chapters before source links. Browse only for uncovered versions/features, a real conflict, or a requested update. If relevant chapters are already in context and unchanged, reuse them.

For deeper composition help, use [prompt-writing.md](references/prompt-writing.md); for a missed requirement, [troubleshooting.md](references/troubleshooting.md). [guide.md](references/guide.md) indexes the full manual. [detailed-authoring.md](references/detailed-authoring.md) expands the authoring/execution contract; [sources.md](references/sources.md) records provenance. Resolve other chapter names above relative to `references/`. Snapshots are dated, not a live runtime guarantee.

## Execution boundary

Generate only when requested. Follow project instructions (AGENTS.md / CLAUDE.md): use the connected ComfyUI MCP first; inspect the selected workflow's real slots/defaults. Use a user-selected existing workflow or otherwise the official template; do not create/restructure workflows without an explicit request. Keep output transformations in ComfyUI. Missing tools require an explanation, not an unrequested generator substitution.
