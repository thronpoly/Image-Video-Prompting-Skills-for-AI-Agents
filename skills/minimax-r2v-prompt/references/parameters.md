# H3 parameters: native model, template and hosted API

Always identify the route. Native width/height/length, hosted duration/resolution and a LoRA's sampling settings are different contracts. Never infer local sampling from a paid API form.

## Native ComfyUI profile
The bundled native-node-snapshot.json records MiniMaxH3ReferenceToVideo: width 1344, height 768; both use increments of 32. `length` is a frame count at 24 fps, default 124, with a displayed 17-frame grid and a trained-region note around 124–362. This bundled snapshot is read-only evidence from the original setup, not a live capacity check. The UI's broad maximum does not prove stable output at that limit. At 24 fps, 124 frames occupy approximately 5.17 seconds, not exactly five. A 17k+5 alignment requirement may snap requested lengths; inspect the actual current node/template and the encoder's effective frame count.

The same snapshot's `ref_image_size` offers `match` and `max`. Match reduces to the generation area while maintaining aspect; max uses a larger reference pipeline, described as a 2048-pixel short edge and potentially several times slower. This is a quality/compute tradeoff, not an independent identity percentage. Keep the official default unless a reference-detail problem motivates a change.

Optional visual/audio VAEs affect actual reference conditioning. Naming a reference without its connected tensor or relevant encoder cannot supply missing visual/audio information. Those are structural checks, not permission to add nodes. Use template notes and current slots to verify required components before execution.

## Hosted MiniMax H3 example route
The recorded Comfy Router schema for minimax/minimax-h3 accepts content, resolution and duration. It exposes 768P/2K, duration 4–15, optional seed, ratio and watermark. The schema notes MiniMax's own duration documentation starts at five while a four-second Router request is accepted. Keep that route distinction explicit. Ratio choices include adaptive and common landscape/portrait formats; first/last-frame behavior can determine framing instead. These fields are not the native Base-Ref2VA frame grid.

## Inference controls
| Control | Meaning | How to choose |
|---|---|---|
| checkpoint / mode | FL2VA versus Ref2VA, base versus regeneration | Match the requested task and official template |
| width, height | Actual frame size and memory | Keep aspect/composition coherent; use valid increments |
| length / duration | Frame count or seconds depending on route | Calculate real playback length; reconcile any snapping |
| fps / save rate | Temporal playback interpretation | Keep model cadence and saved cadence consistent |
| seed | Randomness | Pin only for a controlled comparison; record all conditioning |
| steps, sampler, scheduler, guidance | Denoising behavior | Use the selected checkpoint/template's documented settings |
| accelerated LoRA | May change step schedule, guidance and motion response | Use only a deliberately selected, documented variant |
| reference sizing | Detail versus compute | Test a specific identity-detail issue rather than maximizing blindly |

Do not invent universal H3 step/CFG defaults from a community Turbo file. Do not change playback fps merely to “fix” motion, because that also changes duration. An exact-length deliverable may require an exposed in-workflow trim or length control; if absent, explain the structural limitation under the project instructions (AGENTS.md or CLAUDE.md). No external FFmpeg/Python conversion is authorized by this skill.

See parameter-snapshot.json for factual route fields and sources.md for dates and source distinctions.
