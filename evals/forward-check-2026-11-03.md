# Text-only forward check: 1.1.0

An independent agent used the revised installed skills with three realistic requests. No generation, browsing, paid tools or workflow changes were performed.

| Request | Chapters actually loaded | Observed behavior |
| --- | --- | --- |
| Midjourney parametric pattern from the supplied print reference | SKILL.md and the actual image | Described visible cross/grid motifs and colors; explicitly instructed Image Prompt attachment; did not invent a URL |
| Qwen 2.1 transfer black glasses from image2 to image1, preserve face/background/captions | SKILL.md, editing.md, image-references.md | Assigned canvas and donor in order, scoped transfer to glasses, preserved captions without inventing their text |
| Midjourney red apple product photo, strictly prompt body only | Reused loaded SKILL.md | Returned only prompt prose; no setup explanation or generation |

This checks instruction-following and read routing for three cases, not visual outcomes, automatic skill selection across hosts, or statistical improvement against a baseline. The Qwen tagging follows the documented 2.1 enhancer route; another implementation still needs its own compatibility check. The aspect-ratio instruction was clarified after this check; required aspect controls must be expressed with --ar rather than prose alone.
