# Seedance settings and dated provider differences

## Model/task profile
| Field | Seedance 2.0 ModelArk | Seedance 2.5 ModelArk |
|---|---|---|
| duration | 4–15 integer seconds or -1; default 5 | 4–30 or -1; default -1; edit only -1 |
| resolution | Main 2.0: 480p/720p/1080p/4k in current provider API; fast/mini: 480p/720p | 480p/720p/1080p, default 720p |
| ratio | 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, adaptive | Same ordinary choices; edit/extend/first-frame tasks require adaptive |
| generate_audio | Boolean, default true | Boolean, default true |
| return_last_frame | Boolean, default false | Boolean, default false |
| draft | Not the 2.0 path | Preview at 480p, then final from draft_task when supported |
| output_format | Follow actual endpoint | mp4 or mov where exposed |
| omni_reference_task_type | Not a generic 2.0 field | auto/reference/edit/extend where exposed |

## Do not merge conflicting routes
The saved Comfy Router schemas include broader shared fields and some stale descriptions: for example a shared resolution description says 2.0 lacks 1080p while the current provider API differentiates main 2.0 from fast/mini and lists main 2.0 at 1080p/4k. The Router ratio enum also includes 9:21 whereas the current provider API's main ratio list does not. Draft ID lifetime descriptions differ. Use the actual selected route's accepted schema; record the discrepancy and do not silently send provider-only capabilities through a narrower node.

Seed differs particularly: the provider API's seed paragraph lists range -1..2147483647 and explicitly lists older supported model families, while the captured Router exposes -1..4294967295 for its shared input. Do not assert universal Seedance 2.x seed support or a cross-route range. Use a seed only if the chosen node/schema exposes it, and do not promise bit-identical rerenders. The provider's camera_fixed and fractional-frame fields are documented for older 1.x models, not generic 2.x controls. Use explicit static-camera prose for R2V instead of inventing camera_fixed=true support.

## Frame, duration and cropping
For 2.x use actual duration choices, not the older 1.0 `25+4n` fractional-frame grid. Timestamp requests in prose do not change duration. First-frame/first-last-frame 2.5 follows first-frame framing through adaptive. A 2.0 explicit ratio inconsistent with an input may cause center cropping under provider behavior; protect the subject by choosing a compatible actual frame rather than silently modifying the image.

## Reference roles
Content items have actual types and roles: text; image_url with first_frame, last_frame or reference_image; video_url with reference_video; audio_url with reference_audio. A simple uploaded file must be staged by the actual integration; a local path is not automatically a public API URL. Preserve modality-local numbering in the prompt.

## Draft and final
Draft is a specific supported task, not a synonym for a lower resolution prompt. A 2.5 finalization from draft_task reuses prior choices and can prohibit resending fields. Follow the selected route's current draft schema and validity period. This skill does not run a preview/final pair or spend on extra generations without a user request.

## Other exposed fields
Watermark, service tier, callback, expiration/priority and result retrieval are execution controls rather than scene language. Some Router callbacks are accepted but ignored. Do not include a callback URL or change output visibility merely to write a prompt. Parameter-snapshot.json preserves the captured route facts; current template controls remain authoritative for actual ComfyUI execution.
