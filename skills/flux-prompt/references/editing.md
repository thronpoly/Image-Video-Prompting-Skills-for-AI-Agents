# FLUX editing operations

## Local edit recipe
Name the base picture and exact target; state the new property; specify what else remains. Keep the operation scoped. “Change the chair's fabric to muted blue linen while preserving its frame and placement” is easier to execute than a full caption of the entire room containing that chair. If a requested edit changes physical material, let highlights/shadows change accordingly rather than locking an impossible appearance.

## Common edit families
| Task | Describe |
|---|---|
| Recolor | Target surface, desired color, preserved material/geometry |
| Material transfer | New material properties and retained design shape |
| Object replacement | Removed target, donor object, scale/contact/orientation |
| Removal | Exact item and plausible exposed surface/background |
| Clothing/try-on | Person identity/pose and donor garment design |
| Background substitution | Foreground invariants, new environment and matching light |
| Restyling | New medium/marks and content that should remain |
| Relighting | Direction, softness and intended shadow/reflection changes |
| Text replacement | Exact replacement string and retained type/layout where relevant |
| Camera/view change | New viewpoint and subject identity/design invariants |
| Outpainting | Desired frame expansion, anchored subject and new surroundings |
| Sharpen/detail | What detail should improve, without an unrequested redesign |

## Multi-reference composite
State the base and each donor separately. Bind the donor to the destination, not merely to the image set. A person from one input wearing a coat from another in a third room needs all three roles plus pose and scale. Preserve the room's frame when it is the canvas. For a new composition built from several identities, select an explicit frame rather than inheriting an arbitrary cutout's crop.

## Text and small designs
Keep exact lettering quoted. For an edit, identify the existing text by content if readable or by region if not. Keep typography, placement and size when only spelling changes. A logo can have both vector shape and text; describe the desired invariant. If exact readability is the acceptance criterion, inspect it explicitly after generation; additional adjectives cannot certify correctness.

## Kontext versus FLUX 2/3
Kontext supports instruction editing, consistent subjects and style changes, but it does not inherit all newer multi-input or coordinate controls. FLUX.2 exposes endpoint-specific input_image slots and variants such as max/pro/flex/klein. FLUX 3 supports its own images array and optional inline layout/box rows. Keep the requested model; do not upgrade a workflow to use a convenient new feature without authorization.

## Region targeting
For text-only edits, a discriminative target can be sufficient. For precise placement on a supporting FLUX 3 route, measure and use source/target boxes described in layout.md. If the existing template only accepts a plain prompt and no compatible box-aware input, do not assume arbitrary JSON in text produces that feature. For a selected inpainting/Fill route, use its actual mask conventions and controls rather than treating every FLUX image model as masked Fill.

## Iteration boundaries
If one edit unexpectedly changes identity, retain the original canvas and reduce unrelated restyling before changing seeds. If the requested change is too weak, state the new attribute more decisively instead of lowering all preservation. Multiple operations can be staged through the same supported workflow when authorized, but this skill does not add a node chain or external postprocessing pipeline.
