# Image & Video Prompting Skills for AI Agents

Seven model-specific prompting skills for **Codex, Claude Code, and Claude Skills**. Turn natural-language requests into detailed image and video prompts, reference-image roles, preservation constraints, and model-specific settings.

The English manuals live inside each skill. Agents read the relevant local chapters instead of opening documentation links for every request. Official links remain available for attribution and updates.

**[한국어 설치·사용 설명서](USAGE_KO.md)** · **[Download the complete package](downloads/team-prompt-skills-v1.1.0.zip)**

## Included skills

| Model / service | Skill | Main coverage |
| --- | --- | --- |
| Midjourney | [midjourney-prompt](skills/midjourney-prompt/SKILL.md) | Prompt structure, references, parameters, editing, and version compatibility |
| Z-Image Turbo | [z-image-turbo-prompt](skills/z-image-turbo-prompt/SKILL.md) | Turbo-specific prompt construction and settings |
| MiniMax H3 R2V | [minimax-r2v-prompt](skills/minimax-r2v-prompt/SKILL.md) | Reference mapping, six-section prompts, motion, and audio |
| Qwen Image | [qwen-image-prompt](skills/qwen-image-prompt/SKILL.md) | Generation, image editing, multiple references, and preservation constraints |
| Krea | [krea-prompt](skills/krea-prompt/SKILL.md) | Krea model distinctions, visual direction, references, and settings |
| FLUX | [flux-prompt](skills/flux-prompt/SKILL.md) | FLUX version differences, generation, references, and editing |
| Seedance R2V | [seedance-r2v-prompt](skills/seedance-r2v-prompt/SKILL.md) | Provider-specific reference syntax, motion, audio, and generation settings |

Each skill includes a `SKILL.md` entry point and detailed `references/` chapters covering prompt writing, examples, troubleshooting, and source records.

## Quick start

Clone this repository or extract the [standalone ZIP](downloads/team-prompt-skills-v1.1.0.zip). Run installer commands from the repository or extracted package directory. Python 3.8+ is optional; the installer uses only the standard library.

Verify the bundled skill files:

```sh
python install.py --verify
```

### Codex

Install for all your local projects:

```sh
python install.py --client codex --scope user
```

Or install into an existing project:

```sh
python install.py --client codex --scope project --project "/path/to/project"
```

Invoke explicitly, or describe a task that matches the skill:

```text
$qwen-image-prompt Use image 1 as the base. Put the glasses from image 2
on the person in image 1. Preserve their identity, expression, clothing,
background, framing, and existing text. Prepare the editing prompt only.
```

### Claude Code

```sh
python install.py --client claude --scope user
```

Invoke with `/qwen-image-prompt`, `/midjourney-prompt`, or another skill name, followed by your request. Natural-language requests can also select a matching skill automatically.

For both clients in one existing project:

```sh
python install.py --client both --scope project --project "/path/to/project"
```

Use `py -3` on Windows or `python3` on macOS/Linux if that is your Python command. Replace the example path with your actual project path.

### Manual installation

Copy complete folders from `skills/`, including their `references/` files:

| Client | Project installation | User installation |
| --- | --- | --- |
| Codex | `<project>/.agents/skills/<skill-name>/` | `~/.agents/skills/<skill-name>/` |
| Claude Code | `<project>/.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` |

Reload or restart the client if newly installed skills do not appear. `agents/openai.yaml` contains Codex metadata; Claude reads `SKILL.md`.

### Claude web, Desktop, and Cowork

Upload the individual skill ZIPs from [claude-upload/](claude-upload/) through **Customize → Skills**, then enable them. For example, upload `qwen-image-prompt.zip`. Do not upload the complete team package as a single skill. Availability and menu labels depend on your client and account.

Ask naturally: “Use the qwen-image-prompt skill to write an editing prompt for these two images.” Local Claude Code slash commands and local file access do not automatically transfer to cloud skills.

## Installation controls

```sh
# Preview an installation without changing files
python install.py --client codex --scope user --dry-run

# Install only selected skills
python install.py --client claude --scope user --skills qwen-image-prompt flux-prompt

# Update existing skills after reviewing the changes
python install.py --client codex --scope user --replace
```

The installer refuses same-name collisions by default. `--replace` backs up existing skill folders under `.prompt-skills-backups/` in the selected project or home before copying updates. Extra local files are preserved. It does not change client settings, project instructions, or MCP configuration, and it performs no downloads.

## Prompt authoring and actual generation

Prompt authoring works without ComfyUI, model files, or MCP. Actual image/video generation requires your own compatible execution tools, installed models, and accessible inputs. The skills use the available host tools and configured MCP server names; they do not install a runtime.

Optional ComfyUI execution rules are provided in [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md). Copy the relevant block into your own `AGENTS.md` or `CLAUDE.md` if appropriate. User-selected existing workflows take priority; otherwise use the model's official template and change inputs, prompts, and parameters within the authorized scope.

## Package contents

- `skills/`: seven portable skills and English manuals.
- `claude-upload/`: seven individually uploadable skill archives.
- `install.py`: optional local installer with verification and backups.
- `USAGE_KO.md`: detailed Korean installation guide and examples.
- `PROJECT_INSTRUCTIONS.md`: optional project execution instructions.
- `MANIFEST.json`: hashes for the distributable skill files, archives, and installation documents.
- `downloads/`: the original self-contained team package ZIP.

Version **1.1.0**. Source records were checked on **2026-11-03**. See each skill's source and coverage notes for version boundaries. Numerical API/node snapshots are dated examples, not a claim about your local runtime.

Model weights, personal images, generated media, user workflows, credentials, and MCP server software are not included. Third-party documentation and product names remain attributable to their respective owners; this is an independent skill collection.

## Updating and checking this collection

Version 1.1.0 keeps the detailed manuals and adds a shorter default read path, essential reference/setup output, and a corrected Qwen lettering example. H3/Seedance tasks still load their required specialist chapters.

The canonical distributable sources are `skills/` in this repository. After editing skills or documents, run `python scripts/build_package.py --version 1.1.0`, then `python install.py --verify`. This rebuilds the individual Claude ZIPs, repository manifest and standalone ZIP together. The builder uses Python 3.8+ and performs no downloads. Existing release ZIPs remain available.

See [evals/README.md](evals/README.md) for behavioral cases and success criteria. Installation/hash checks and text-only forward checks do not establish improved image/video output quality.
