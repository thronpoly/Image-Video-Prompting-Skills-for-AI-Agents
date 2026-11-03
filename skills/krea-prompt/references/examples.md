# Original Krea examples

## A. Krea 2 production prompt
```text
A small blue glass bird is displayed as a contemporary design object on a low cream pedestal. Its curved wings and rounded head catch a soft rectangular reflection from the upper-left light, revealing fine bubbles inside the translucent body. The pedestal sits slightly below center against an uninterrupted warm ivory wall. A faint blue caustic spreads across the surface beneath the bird, while generous empty space above it creates a restrained editorial composition.
```
Native Turbo settings should follow its 8-step no-CFG profile, not a Krea 3 thinking mode.

## B. Exploration in three real directions
Brief: a bird sculpture, no fixed material.
Direction 1:
```text
A compact bird sculpture made of folded cobalt paper, photographed on warm cream paper with crisp cast shadows and a simple asymmetrical arrangement.
```
Direction 2:
```text
A small bird sculpted from pale blue glazed ceramic, sitting on a rough stone ledge under overcast daylight, a quiet tactile object study.
```
Direction 3:
```text
A graphic bird silhouette built from interlocking blue and cream shapes, flat screen-printed illustration with subtle ink grain and a wide open background.
```
Do not deliver these alternatives when the user explicitly required blue glass; their openness is an assumption in this exploration example.

## C. Krea 3 one-image edit
```text
Change only the plinth to warm terracotta stone. Keep the glass bird's identity, material, scale and position intact, and retain the original framing and light direction.
```
If using regional_edit, validate berry and an actual input image. Do not infer a 2D mask from the sentence alone.

## D. Krea 3 two-image composite
Inputs: image 1=interior canvas, image 2=glass bird.
```text
Place the blue glass bird from image 2 on the shelf in image 1, near the left edge of the framed print. Preserve the bird's design and translucent blue material. Retain the room's existing arrangement and frame, and adapt the bird's size, contact shadow and reflections to the shelf and window light.
```
The setting remains image 1; the product donor does not supply a new room.

## E. Poster with literal text
```text
A vertical exhibition poster on subtly textured cream paper, with one blue glass bird occupying the lower third. A bold dark-blue headline across the top reads "푸른 새". The typography is a clean sans-serif with generous spacing, and the open center separates the headline from the object. Soft left-hand light creates delicate blue reflections beneath the bird, keeping the palette restrained and the layout calm.
```
Pass aspect through the selected provider's actual field. Keep the title Korean.

## F. Qwen + Krea-named LoRA
If the loaded base is Qwen Image Edit and the actual adapter supplies a photographic style, keep Qwen's editing grammar:
```text
Apply a restrained editorial photographic treatment to the image, with soft directional light and natural material texture. Preserve the subject's identity, pose and clothing, and retain the composition and all readable text.
```
The actual compatible LoRA is loaded through the existing template. Never invent a Krea hosted endpoint or change the base model because of a file name.
