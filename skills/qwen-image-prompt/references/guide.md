# Qwen Image manual
Read prompt-writing.md for generation; editing.md for image changes; image-references.md for single/multiple inputs; parameters.md for checkpoint, size or sampling choices; examples.md and troubleshooting.md for task recipes.

Supported local knowledge: original Qwen-Image generation, Qwen-Image-Edit family, and Qwen-Image-2.1's generation/edit prompt-enhancer conventions and base/Turbo distinction. This package does not assume an original Edit checkpoint, a 2.1 checkpoint and a custom Qwen-based LoRA have identical settings. Keep a selected checkpoint explicit. Newer API products with a similar name require their own route contract.

A T2I prompt describes the finished picture; an edit prompt directs an operation on actual inputs. The official enhancer's JSON wrapper is an intermediate result: extract rewritten_prompt before inserting text into a diffusion prompt field, and map its size fields separately. Source links are in sources.md; routine use should rely on these local instructions.
