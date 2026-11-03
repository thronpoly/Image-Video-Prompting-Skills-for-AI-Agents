# Optional project instructions for ComfyUI work

Copy the following block into the team's existing AGENTS.md (Codex) or CLAUDE.md (Claude Code) only if this is the team's desired operating policy. The installer does not modify either file.

```text
Use the connected ComfyUI MCP server first for server status, input uploads, workflow/template inspection, exposed parameter changes, execution and output retrieval. The server was named comfy_local in the original setup; use its actual configured name here. Explain any unsupported action before using another interface. Use Computer Use only when necessary for a UI operation unsupported by MCP and authorized for this task.

Use the existing workflow explicitly selected by the user; otherwise use the model's official default template. A normal generation request permits input, prompt and exposed parameter changes, but does not authorize creating, saving or restructuring a separate workflow. Explain structural limitations. If workflow creation is explicitly requested, provide an editable ComfyUI UI-format JSON with readable layout and controls.

Keep image/video transformations and postprocessing reproducible inside ComfyUI. Do not silently replace missing functionality with external Python/FFmpeg conversion scripts. Read-only result inspection is allowed. Respect the user's specified model and inference route.
```
