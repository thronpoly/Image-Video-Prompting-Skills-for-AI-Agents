---
name: minimax-r2v-prompt
description: MiniMax H3 reference-to-video(minimax_h3_r2v) 프롬프트 작성·수정에 사용한다. 참조 매핑과
  공식 6개 섹션 형식을 적용한다. I2V와 구분한다.
---

# MiniMax H3 R2V prompt authoring

A request to “write a prompt” authorizes drafting only. Return one copyable English prompt (keep literal dialogue/text in its original language), plus the minimum required attachment roles and non-default settings in the user's language. Treat strict “prompt body only / no explanation” as an explicit output constraint; otherwise do not omit setup needed to use references. Mark proposed settings as starting points. Do not invent files, URLs, controls or unsupported values. Preserve user-specified content, references and model.

## Start here

Use the open H3 Ref2VA six-section format, not generic I2V prose or a hosted Hailuo contract. For every final R2V prompt, read format.md and prompt-writing.md: exact field/label rules and the production-length guidance matter. References supply separately defined identity, frame, action or sound roles; R2V does not automatically pin the first frame. Read image-references.md for supplied assets and audio.md for dialogue, music, sound or video soundtracks. First-shot and later-cut syntax differ. Do not invent a second shot. Preserve spoken/on-screen language while writing descriptive prose in English. Read parameters.md for timing/sampling; native frame length, hosted seconds and LoRA schedules are separate contracts.

## Read only what this task needs

For a straightforward request covered above, draft directly; do not load a general writing tutorial or all chapters. Use local chapters before source links. Browse only for uncovered versions/features, a real conflict, or a requested update. If relevant chapters are already in context and unchanged, reuse them.

For deeper composition help, use [prompt-writing.md](references/prompt-writing.md); for a missed requirement, [troubleshooting.md](references/troubleshooting.md). [guide.md](references/guide.md) indexes the full manual. [detailed-authoring.md](references/detailed-authoring.md) expands the authoring/execution contract; [sources.md](references/sources.md) records provenance. Resolve other chapter names above relative to `references/`. Snapshots are dated, not a live runtime guarantee.

## Execution boundary

Generate only when requested. Follow project instructions (AGENTS.md / CLAUDE.md): use the connected ComfyUI MCP first; inspect the selected workflow's real slots/defaults. Use a user-selected existing workflow or otherwise the official template; do not create/restructure workflows without an explicit request. Keep output transformations in ComfyUI. Missing tools require an explanation, not an unrequested generator substitution.
