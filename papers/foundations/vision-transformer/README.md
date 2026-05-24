<div align="center">

# 📄 An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

**Authors:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, et al.
**Published:** ICLR · 2021
**Link:** [arXiv](https://arxiv.org/abs/2010.11929) | [PDF](https://arxiv.org/pdf/2010.11929)

</div>

---

> **One-line takeaway:** *Splitting images into 16×16 patches and treating them as token sequences lets a standard transformer — with no convolutions — match or beat CNNs on image classification when pre-trained at scale.*

---

## 🏷️ Tags

![Task](https://img.shields.io/badge/-Image%20Classification-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/-Vision%20Transformer-purple?style=flat-square)
![Domain](https://img.shields.io/badge/-Computer%20Vision-green?style=flat-square)
![Method](https://img.shields.io/badge/-Supervised-orange?style=flat-square)
![Scale](https://img.shields.io/badge/-Large--Scale-red?style=flat-square)

---

## 📝 Summary

The Vision Transformer (ViT) proved that the transformer architecture, originally designed for NLP, could be applied directly to images with minimal modification. An image is split into fixed-size patches (e.g., 16×16 pixels), each patch is linearly embedded into a vector, and the resulting sequence of embeddings is fed into a standard transformer encoder. A key finding was that ViT underperforms CNNs when trained on mid-size datasets (ImageNet alone) due to lacking inductive biases like translation invariance, but *surpasses* CNNs when pre-trained on large datasets (ImageNet-21K, JFT-300M). This opened the floodgates for transformer-based vision models.

---

## 🔬 Methodology

### Architecture

The image is divided into N patches of size P×P. Each patch is flattened and projected to dimension D via a linear layer. A learnable [CLS] token is prepended, and learnable 1D position embeddings are added. This sequence passes through a standard transformer encoder (multi-head self-attention + MLP blocks with Layer Normalization). The [CLS] token's output is used for classification via a small MLP head.

### Training

| Component | Details |
|---|---|
| **Loss function** | Cross-entropy |
| **Optimizer** | Adam (β₁=0.9, β₂=0.999) |
| **Learning rate** | Linear warmup + cosine decay |
| **Batch size** | 4096 |
| **Pre-training data** | JFT-300M (best), ImageNet-21K, ImageNet-1K |
| **Hardware** | TPUv3 cores, days to weeks depending on model |

### Key Equations

**Patch embedding:**

$$
z_0 = [x_{\text{class}}; \; x_p^1 E; \; x_p^2 E; \; \dots; \; x_p^N E] + E_{\text{pos}}
$$

Where E is the patch projection matrix and E_pos are position embeddings.

---

## 💡 Innovation

**What's new:**

ViT deliberately avoided adding vision-specific inductive biases (no convolutions, no local connectivity assumptions). It showed that with sufficient data, a general-purpose architecture can learn these patterns from scratch. This was a powerful statement: domain-specific architectural engineering may be less important than scale. The patch tokenization idea also elegantly bridged the gap between NLP and vision, enabling unified multimodal architectures.

**Compared to prior work:**

| Aspect | CNNs (ResNet, EfficientNet) | ViT |
|---|---|---|
| Inductive bias | Strong (locality, translation invariance) | Minimal (only position embeddings) |
| Small data performance | Strong | Weak — overfits without large pre-training |
| Large data performance | Plateaus | Surpasses CNNs |
| Architecture | Domain-specific (convolutions) | General-purpose (standard transformer) |
| Unification potential | Vision only | Bridges vision and language |

---

## 🌍 Real-World Applicability

**Use cases:**

ViT and its successors (DeiT, Swin, BEiT, DINO) now power production vision systems in medical imaging, autonomous driving, document understanding, and satellite imagery. The CLIP model (ViT + text encoder) enables zero-shot image classification in production. ViT backbones are the default for modern multimodal models.

**Production considerations:**

| Factor | Assessment |
|---|---|
| **Compute cost** | 🟡 Medium to 🔴 High (scales quadratically with image resolution) |
| **Data requirements** | Needs large-scale pre-training; DeiT variants reduce this |
| **Latency** | Comparable to ResNet-50 at similar FLOPs |
| **Scalability** | Excellent — benefits from more data and compute |

---

## 💻 Code

> **Status:** 🔲 Not started

| File | Description |
|---|---|
| `code/` | *Implementation coming soon* |

---

## 📊 Key Results

| Benchmark | Metric | This Paper (ViT-H/14) | Previous SOTA |
|---|---|---|---|
| ImageNet | Top-1 Accuracy | 88.55% | 88.36% (EfficientNet-L2) |
| CIFAR-100 | Top-1 Accuracy | 94.55% | — |
| VTAB (19 tasks) | Average | 77.63% | 76.21% |

---

## 🤔 Personal Notes

*Add your reflections here after studying the paper.*

---

## 📎 References

1. Vaswani et al. "Attention Is All You Need" (2017). [arXiv](https://arxiv.org/abs/1706.03762)
2. Touvron et al. "Training data-efficient image transformers" (DeiT, 2021). [arXiv](https://arxiv.org/abs/2012.12877)

---

<div align="center">

[← Back to Transformers](../README.md) · [← Back to Main](../../../README.md)

</div>
