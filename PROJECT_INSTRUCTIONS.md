# Optional project instructions for ComfyUI work

Copy the following block into the team's existing AGENTS.md (Codex) or CLAUDE.md (Claude Code) only if this is the team's desired operating policy. The installer does not modify either file.

```text
Use the connected ComfyUI MCP server first for server status, input uploads, saved workflow inspection, exposed parameter changes, execution and output retrieval. Use its configured name, such as comfy_local. Use Computer Use only for a necessary screen operation outside MCP's capabilities and explain the reason.

Choose only from the active user's saved workflow list. Reuse the verified saved path and slots for follow-ups. When selecting a new workflow, list filenames in the active profile's workflows directory and inspect only relevant candidates. Use read-only directory enumeration if MCP cannot list it. Exclude the official gallery, web search and broad filesystem search from workflow selection. Explain missing capabilities or a material choice among candidates before running.

For every ComfyUI image and video model, revise from the original user-provided sources and their slot roles. Combine retained changes and the new request into one prompt and parameter set. Use earlier results for comparison and keep generated images, videos and extracted frames out of the model's revision inputs, including edit bases, references, first/last frames and mask targets. If an original or necessary slot is missing, explain the limitation.

For a generation request, change input files, prompts and exposed parameters in the selected saved workflow. An explicit workflow creation request permits a separate editable ComfyUI UI-format JSON with readable layout and controls. Explain structural limitations before changing the graph.

Keep image/video transformations and postprocessing reproducible inside ComfyUI. Do not silently replace missing functionality with external Python/FFmpeg conversion scripts. Read-only result inspection is allowed. Respect the user's specified model and inference route.
```
