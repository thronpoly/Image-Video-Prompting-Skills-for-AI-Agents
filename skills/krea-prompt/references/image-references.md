# Krea references and adaptations

## Native Krea 2 versus hosted controls
The open Krea 2 model is a T2I model with RAW/Turbo profiles and LoRA support. Its basic public inference example is not an arbitrary image-editing API. A hosted Krea route may expose image_style_references, moodboards and styles; those are provider features and do not prove the local Turbo template has matching inputs. Krea 3 is a distinct image-editing/generation model with its own references.

## Build a role ledger
For every actual asset name its role: canvas, identity, product design, palette/style, costume, layout or motion. A style reference normally transfers visual treatment rather than exact shape. A moodboard is a curated aesthetic source. A LoRA is a learned adaptation with a compatible base model and sometimes a trigger, not a loose image attachment.

If references only guide this assistant, describe the chosen visual properties in text and disclose that this is prompt reconstruction. If exact model-side identity conditioning is needed, check the selected route's actual image inputs. Do not pretend that an image file placed in the chat is automatically passed to a T2I model.

## Krea 2 hosted style-reference profile
The recorded Router endpoint accepts up to ten style-image references and one moodboard. Each nested object has a provider-specific schema; read the saved snapshot for actual keys rather than inventing an image URL/strength structure. `styles` commonly represents provider-recognized LoRA/style identifiers, not arbitrary local paths. Image style, moodboard and creativity are separate dimensions; assign their responsibilities before varying them.

## Krea 3 editing profile
Up to eight actual input images in the recorded route. Specify which image is the base canvas and which supply products/people/styles. For a local edit, retain the base framing and untargeted scene. For a new composition, assign every donor and describe the resulting arrangement. `regional_edit` is a route flag with model/input prerequisites, not a mask syntax inferred from ordinary prose. Input URL acceptance is provider/environment-specific; a local path is not automatically an accepted hosted URL.

## LoRA identity and triggers
Read the selected LoRA's base family, compatible checkpoint, training concept, trigger if any, and documented strength. A file with Krea in its name may be a style applied to FLUX or Qwen. Keep that family's prompt grammar and image-conditioning mechanism. Do not invent angle-bracket LoRA loading tokens unless the actual node parses them; ComfyUI normally loads LoRAs through model inputs. This skill cannot add that node under the project's official-template rule.

## Conflict handling
If identity and style disagree, state which properties must survive. If two references depict different identities, do not blend faces by default. If a product's exact label matters, transfer it as an invariant rather than recaptioning guessed text. If a reference has unwanted shadows/background, exclude those roles from the transfer specification instead of expecting a single opaque strength slider to separate them.
