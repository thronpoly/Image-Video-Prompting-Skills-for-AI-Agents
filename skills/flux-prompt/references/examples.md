# Original FLUX examples

## A. Product generation
```text
A translucent blue glass bird rests on a low cream stone pedestal in a quiet studio. Its rounded body and curved wings are viewed from a three-quarter angle, with a soft rectangular highlight from the left and a pale blue reflection beneath the base. The warm ivory background remains empty, and the centered arrangement leaves a broad clear area above the product.
```
Use real width/height or provider aspect/resolution fields, not --ar or --s.

## B. Single-image targeted color edit
```text
Change only the bird's blue glass to transparent amber glass. Preserve its silhouette, pose, position and scale, and keep the pedestal, background, camera framing and lighting arrangement unchanged.
```
Changing glass color naturally affects colored caustics; do not lock them to blue.

## C. Product reference into a room
Inputs: image 1=room, image 2=bird product.
```text
Place the blue glass bird from image 2 on the left end of the shelf in image 1. Preserve the product's distinctive shape and material. Keep the room's framing and arrangement, and match the bird's scale, reflections and contact shadow to the window light already present in image 1.
```
For FLUX 3 with auto aspect, put the intended room canvas first. For FLUX.2, map the same ordered sources into its actual input_image fields.

## D. Garment without identity leakage
```text
The person from image 1 wears the coat design from image 2. Preserve the person's identity, hairstyle, pose and the setting of image 1. Adapt the coat's folds and fit to the existing body while retaining its distinctive cut, fabric and color.
```
The donor's face and scene are not requested.

## E. Graphic layout and exact text
```text
A vertical exhibition poster with one blue glass bird in the lower half and the exact Korean headline "푸른 새" across the upper quarter. The title is bold cobalt sans-serif lettering on warm ivory paper, with a broad clear central gap and restrained alignment. Soft light reveals the bird's glass edges without distracting from the title.
```
If exact element placement matters and FLUX 3 layout is supported, use measured/design-specific rows from layout.md.

## F. Surface pattern transfer
```text
Apply the blue-and-cream geometric pattern from image 2 to the fabric seat of the chair in image 1. Preserve the chair's frame, shape, position and the room. Make the pattern follow the seat's perspective and folds while retaining the donor pattern's scale relationships and color palette.
```
The pattern donor does not replace the chair geometry.

## G. Remove an object in an edit
```text
Remove the small cable running across the front of the tabletop. Continue the existing wood grain naturally through the exposed area and retain every other object, the light and the frame.
```
This is a legitimate operation on an image, not a negative T2I blacklist.

## H. Poster color controlled by a user HEX
```text
A simple product poster with an unmarked ceramic cup centered in the lower half, its glaze colored #1457C5. The background is warm ivory, and a soft left-side light creates one gentle shadow. A large blank region remains above the cup for later typography.
```
The code came from the user's brief. Do not promise that all shaded pixels equal that exact RGB triplet.
