# Foundations

> The architectures every modern AI system inherits. If you don't understand these, you can't reason about what newer systems are doing or where they break.

## Why this category exists

A CTO's job isn't to chase the latest arXiv drop — it's to know which substrate the team is building on, and where each substrate's assumptions show through. This folder collects the architectures and training tricks that show up, in some form, inside almost every model my team ships: image encoders inherit from ResNet; every LLM inherits from the Transformer; every long-context system either pays the quadratic cost or borrows from Mamba's state-space ideas; every segmentation pipeline now starts from SAM-style promptable masks.

## Papers

| Paper | Year | What it gave us | Folder |
|---|---|---|---|
| Attention Is All You Need | 2017 | Self-attention replaces recurrence. The substrate of everything since. | [attention-is-all-you-need](attention-is-all-you-need/) |
| Deep Residual Learning (ResNet) | 2016 | Skip connections let networks go 10–100× deeper without degradation. | [resnet](resnet/) |
| Batch Normalization | 2015 | Re-normalize activations per mini-batch → much higher LRs, less initialization fragility. | [batch-normalization](batch-normalization/) |
| Vision Transformer (ViT) | 2021 | Treat 16×16 patches as tokens — transformers beat CNNs once data is big enough. | [vision-transformer](vision-transformer/) |
| Mamba: Selective State Spaces | 2024 | Linear-time sequence modeling that finally rivals attention on long contexts. | [mamba](mamba/) |
| SAM 2: Segment Anything in Images and Videos | 2024 | A foundation model for segmentation — promptable masks across image + video. | [sam2](sam2/) |

## Demo notebook

`foundations.ipynb` — implements scaled dot-product attention from scratch on a toy bilingual translation task, then swaps in a residual+layernorm block. Two cells; one shows attention weights as a heatmap, the other shows the loss curve when you remove the skip connections (it diverges). Designed to be runnable on CPU in under 90 seconds.

## My take

The boring lesson buried under ten years of architecture papers: **whatever you build will route a gradient through a skip connection, normalize an activation, and read keys and values from some context**. The interesting questions in 2026 are not "is attention enough" — they're "where is attention too expensive" and "what bias do we put back in when we strip the inductive priors out." Mamba and ViT bracket that question from opposite ends.
