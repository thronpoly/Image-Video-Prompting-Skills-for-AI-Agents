# Version compatibility

Snapshot: official Version article, 2026-11-03. V8.2 is the documented default. Version selection is part of the user's brief; do not upgrade a named version silently. An individual feature article may still discuss V7, so apply the Version table before copying an older setting.

| Control | V6 / V6.1 | V7 | V8.1 / V8.2 |
|---|---|---|---|
| Text generation and variations | Supported | Supported | Supported |
| Standard / HD generation | Standard; upscale separately | Standard; V6.1 upscalers | SD and native HD |
| Maximum aspect | 14:1 | 14:1 | 14:1 SD, 4:1 HD |
| Edit Model | No | No | Yes |
| Omni Reference / --ow | No | Yes | No; use Edit Model |
| Style Reference / codes / --sw | Yes | Yes | Yes |
| Image Prompt / --iw | Yes | Yes | Yes |
| Multi-prompt :: weights | Yes | No | No |
| --q | 0.5, 1, 2 | 1, 2, 4 | Not supported |
| --seed / --chaos / --raw / --stylize / --tile / --weird | Supported | Supported | Supported, subject to task restrictions |
| Pan / Zoom / Editor | V6-family tools | V6.1 processing | Edit Model processing |

Do not infer availability solely from a permissive flag list. Edit Model results are incompatible with Remix and Edit Model does not support tile. V7 Omni Reference has its own constraints, documented in image-references.md. A standard-image operation can change the engine used for an edit.

Niji is a separate anime/illustration family, selected with `--niji 7` for the currently documented generation. Do not append a conflicting `--v` selection. A Niji feature's ranges can differ from standard Midjourney; the Image Prompt article lists Niji 7 image weight 0–2 rather than V7/V8.1's 0–3. Do not assume every standard-family reference or editing feature transfers.

V8.0 is a historical alpha and no longer selectable in this snapshot. For old images, retain their source version in the record and choose the intended editing engine explicitly. Older Character Reference and Retexture belong to legacy paths. See legacy.md.

The version table is a dated compatibility record, not an instruction to browse before every prompt. If a user asks about a version newer than the recorded set, confirm that version's feature differences once and update the local chapter.
