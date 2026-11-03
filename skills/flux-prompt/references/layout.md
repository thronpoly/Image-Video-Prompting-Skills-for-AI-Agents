# FLUX 3 layout and box-aware editing

Use this only when the chosen route actually supports FLUX 3's layout prompt format. Prose, JSON layout rows and request parameters are separate layers.

## New-image layout
Write a caption with each important element referenced by a unique `<id>`. Append an array of element rows with `id`, `bbox` and `desc`. Coordinates are normalized on a 0–1000 grid in the order `[top, left, bottom, right]` — y before x, not the common x/y convention. For a full-frame background use [0,0,1000,1000]. Boxes can overlap where objects overlap. The grid stretches to the selected output aspect, so plan the actual frame first.

Example, newly authored:
```text
A minimal poster on an ivory field <background_1>, with a large headline <title_1> above one blue glass bird <bird_1>.
[
  {
    "id": "background_1",
    "bbox": [
      0,
      0,
      1000,
      1000
    ],
    "desc": "An even warm ivory paper surface."
  },
  {
    "id": "title_1",
    "bbox": [
      70,
      100,
      200,
      900
    ],
    "desc": "Centered dark-blue text reading \"푸른 새\" in a bold sans-serif typeface."
  },
  {
    "id": "bird_1",
    "bbox": [
      470,
      280,
      900,
      720
    ],
    "desc": "One translucent blue glass bird on a low cream pedestal."
  }
]
```
The coordinates are illustrative, not measured from a user asset. Match caption tokens exactly to row IDs and keep every text block independently described. A box is a composition cue, not a clipping rectangle.

## Existing-image source and target
Box-aware edit rows can identify a reference with `from`, a source region `src_bbox`, and target region `tgt_bbox`. `ref_image_0` means the first input; `ref_image_1` means the second. Measure source boxes on actual images. A donor object moved from image two should use its donor source index, not image one's. An anchor row with matching source/target regions can express preserved placement. Exact row variants, including removal, must follow the selected route's schema; do not create a generic mask format from memory.

## Coordinate procedure
Given image dimensions W×H, a pixel point (x,y) maps to x/W×1000 and y/H×1000. Build the box in top/left/bottom/right order, check 0≤top<bottom≤1000 and 0≤left<right≤1000, then verify it visually. A square object in a portrait frame needs a different normalized width/height relationship than in a square canvas. Keep the textual location consistent with the measured region.

## When not to use boxes
A straightforward recolor or removal often only needs a precise instruction. Do not burden every prompt with fabricated coordinates. Use boxes when the user needs a deliberate layout, an exact region or separation of similar subjects and the route supports it. If the selected template cannot accept this form, provide a prose alternative and describe the limitation; do not change workflow structure without authorization.

Source: FLUX 3 Image Editing, Layout Prompts, Multi-Reference Editing and bounding-box documentation. See sources.md.
