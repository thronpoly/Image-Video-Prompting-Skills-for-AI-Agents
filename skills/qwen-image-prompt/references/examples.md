# Original Qwen prompt recipes

## A. New typographic image
User: a Korean exhibition poster, one blue glass bird, title “푸른 새”, portrait.
```text
The image is a vertical minimalist exhibition poster in cobalt blue and warm ivory. A single translucent blue glass bird occupies the lower-center area, its rounded body resting on a low cream pedestal. Across the upper quarter, a large dark-blue Korean headline reads "푸른 새" in a clean, heavy sans-serif typeface. A smaller line directly below reads "11월의 전시" with generous letter spacing and clear separation from the headline. The center of the page stays open, giving the title and object distinct visual zones. The bird's glass edges catch a soft rectangular highlight from the upper left, while a pale blue caustic reflection crosses the pedestal. The background is uninterrupted ivory with no additional props. The overall design uses a precise vertical hierarchy, a restrained two-color palette and ample negative space.
```
Settings: choose a 2:3-aligned canvas for the selected checkpoint. The requested strings stay Korean. Do not infer dates or a venue the user never supplied; the secondary line above is illustrative input and must be omitted when not requested.

## B. Local material change, single input
```text
Change only the glass bird's material to matte cobalt ceramic, preserving its exact silhouette, pose, size and position. Keep the pedestal, framing and the rest of the image unchanged, with surface shading appropriate to the new ceramic material.
```
Do not insist on keeping the glass's transmission/refraction while converting it to opaque ceramic.

## C. Product into a scene, 2.1 multi-input
Inputs: image1=room canvas, image2=lamp product.
```text
Place the lamp from <image2> on the left end of the cabinet in <image1>, preserving the lamp's design, proportions and finish. Use <image1> as the canvas, retain the cabinet and room arrangement, and match the lamp's scale, contact shadow and illumination to the existing scene.
```
Size decision: follow image1 unless the user requested a different ratio. Do not follow the isolated product reference's crop.

## D. Separate pose, identity and costume
Inputs: image1=person canvas, image2=coat donor.
```text
Replace the person's coat in <image1> with the coat design from <image2>. Preserve the person's facial identity, hairstyle, pose, visible hands and the background of <image1>. Adapt the coat's folds and fit to the existing body orientation while retaining the donor coat's cut, color and material.
```
Copy the garment, not the donor model's face or background. If a third pose reference is essential, verify the actual template has another reference slot.

## E. Style transfer with a content canvas
```text
Render the scene in <image1> using the dry-brush ink texture and restrained monochrome treatment of <image2>. Preserve the subject identities, object count, spatial arrangement and framing of <image1> while changing the rendering medium consistently across the scene.
```
This explicitly permits the medium change, so the default medium invariant must not block it.

## F. Text correction
```text
Replace the headline "푸른 세" with "푸른 새" in the image. Retain the headline's position, scale, color and type style, and keep all other image content unchanged.
```
Inspect the original before naming the wrong string. If it is unreadable, identify the region instead of fabricating an old spelling.

## G. Three-view sheet
```text
Create a clean character reference sheet using the person in the image as the identity source. Arrange three equal-height panels from left to right: front view, left profile and back view. Show the same full-body character at a consistent scale and ground line in all panels, preserving the outfit and body proportions. Use a plain neutral background and even illumination, with clear spacing between the panels.
```
Choose an aspect from the panel geometry. Do not assume each standing-person panel is landscape or that a 3:1 overall frame is always appropriate.

## H. Extending a composition
```text
Outpaint the image to the right, continuing the same cream wall and tabletop under the existing illumination. Keep the original product at the same scale and position in the left part of the enlarged canvas, and make the added right side a continuous uncluttered surface.
```
Specify the larger actual canvas separately. A prompt cannot create extra pixels if the unchanged template fixes the original canvas.
