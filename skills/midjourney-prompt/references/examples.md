# Original Midjourney task examples

These are authored examples, not copied vendor prompts. File references below mean actual user-provided attachments; do not fabricate URLs. Proposed numeric choices are starting tests, not official presets.

## 1. Literal product photograph, V8.2
Brief: one blue glass bird, cream background, realistic product image.
```text
Studio product photograph of one cobalt-blue glass bird on a matte cream plinth, three-quarter view, gently curved wings, soft rectangular reflections along the glass, one diffused light from the upper left, seamless ivory background, generous empty space above the bird --v 8.2 --ar 1:1 --raw --s 50
```
No --q: V8 does not support it. No negative list is needed because the inventory is explicit.

## 2. Same subject, two different briefs
Editorial illustration:
```text
Editorial illustration of a blue glass bird on a cream pedestal, flattened geometric shapes, subtle screen-print grain, cobalt and pale apricot palette, wide asymmetrical composition with the bird in the right third --v 8.2 --ar 3:2 --s 150
```
Architectural exhibit:
```text
A monumental blue glass bird displayed in a quiet modern gallery, a visitor stands far behind it for scale, polished stone floor, broad north-facing skylight, eye-level wide architectural photograph --v 8.2 --ar 16:9 --raw
```
The subject is stable while scale, composition and medium are intentionally different. Do not reuse all product-photo adjectives blindly.

## 3. Two inputs with separate jobs
V8: attach product.png to Edit Model, palette.png to Style Reference.
```text
Place the glass bird from the attached product reference on a low cream pedestal in a spacious editorial still life. Retain its distinctive silhouette and glass construction. Use the style reference for the restrained cobalt-and-apricot palette and paper-like finish, with the product in the lower-right and a clear upper-left text area --v 8.2 --ar 4:5
```
The attachment plan belongs beside the prompt. A single --iw cannot independently control product identity and style.

## 4. V7 character reference
Attach the user's actual character image to Omni and the desired aesthetic to Style Reference.
```text
A compact round mascot with the same distinctive head and body proportions as the Omni reference, standing beside a station bench and holding a folded map, warm hand-painted illustration, soft evening light --v 7 --ar 3:2 --ow 150 --sw 100
```
The Omni/Style inputs are attached in the web UI. Do not append --q 4 or Draft. Use the actual selected style image rather than an invented code.

## 5. Exact Korean lettering
```text
A minimal exhibition poster featuring one translucent blue glass bird, a bold cobalt Korean headline reading "푸른 새" across the upper quarter, a smaller line reading "11월의 전시" directly below, ivory background, careful vertical spacing, restrained sans-serif typography --v 8.2 --ar 2:3 --raw
```
Check the Korean strings character by character in the output. The ratio shapes the poster; it does not imply a particular print DPI.

## 6. Edit one attribute
Attach the original to Edit Model.
```text
Change only the bird's material from transparent glass to matte blue ceramic. Retain its silhouette, pose, position and scale. Keep the pedestal, background, lighting direction and framing unchanged. --v 8.2 --raw
```
Material is allowed to change; “keep all reflections unchanged” would contradict this edit.

## 7. Pattern and exploration
```text
Small blue paper birds and cream seed shapes scattered in an airy repeating textile pattern, flat ink colors, consistent motif scale, balanced spacing --v 8.2 --ar 1:1 --tile
```
Use standard generation, not Edit Model. Review a tiled preview before any upscale.
For exploration, propose three separate palettes as three explicit prompts or a supported `{cobalt,terracotta,olive}` permutation. Explain that the brace expands into multiple jobs if the user asks to run it.

## 8. Outpaint a square into a banner
Use the original as the Editor canvas, enlarge horizontally, and mask only the added space as supported by the tool.
```text
Continue the seamless cream studio wall and pedestal surface into the expanded space. Keep the blue glass bird at its original scale and position, with the same soft left-hand illumination. The newly revealed right side is a clean ivory field for a headline.
```
The canvas operation supplies the target banner shape. Writing “wide” alone is not outpainting.
