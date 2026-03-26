<div align="center">

# 📄 Deep Residual Learning for Image Recognition

**Authors:** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
**Published:** CVPR · 2016
**Link:** [arXiv](https://arxiv.org/abs/1512.03385) | [PDF](https://arxiv.org/pdf/1512.03385)

</div>

---

> **One-line takeaway:** *Skip connections let you train networks 10–100× deeper by learning residual mappings instead of direct mappings, solving the degradation problem.*

---

## 🏷️ Tags

![Task](https://img.shields.io/badge/-Image%20Classification-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/-CNN-purple?style=flat-square)
![Domain](https://img.shields.io/badge/-Computer%20Vision-green?style=flat-square)
![Method](https://img.shields.io/badge/-Supervised-orange?style=flat-square)
![Scale](https://img.shields.io/badge/-Large--Scale-red?style=flat-square)

---

## 📝 Summary

This paper addresses a fundamental problem: deeper neural networks were performing *worse* than shallower ones, not because of overfitting, but due to optimization difficulty (the degradation problem). The authors introduce residual learning — instead of learning a mapping H(x) directly, the network learns the residual F(x) = H(x) − x through shortcut connections that skip one or more layers. This simple change enabled training of networks up to 152 layers deep (8× deeper than VGG), winning the ILSVRC 2015 classification challenge with a 3.57% top-5 error rate. ResNet became the default backbone for virtually all deep learning architectures that followed.

---

## 🔬 Methodology

### Architecture

The core building block is the residual block: the input x passes through two paths — a main path with stacked conv layers computing F(x), and a shortcut connection carrying x directly. The outputs are summed: y = F(x) + x. For deeper models (ResNet-50+), bottleneck blocks use 1×1 convolutions to reduce and restore dimensionality, making computation tractable. When spatial dimensions change, a 1×1 projection shortcut handles the mismatch.

### Training

| Component | Details |
|---|---|
| **Loss function** | Cross-entropy |
| **Optimizer** | SGD with momentum (0.9) |
| **Learning rate** | 0.1, divided by 10 when error plateaus |
| **Batch size** | 256 |
| **Epochs** | ~60K iterations on ImageNet |
| **Hardware** | Multi-GPU training |

### Key Equations

$$
y = F(x, \{W_i\}) + x
$$

Where F(x, {Wᵢ}) is the residual mapping learned by the stacked layers. When dimensions change:

$$
y = F(x, \{W_i\}) + W_s x
$$

---

## 💡 Innovation

**What's new:**

The key insight is reframing the learning problem. Rather than hoping each stack of layers learns the desired mapping directly, ResNet explicitly formulates layers as learning *residual functions* with reference to the input. If the optimal mapping is close to identity, it's much easier to push the residual to zero than to fit an identity mapping through a stack of nonlinear layers. This made very deep networks trainable for the first time.

**Compared to prior work:**

| Aspect | Prior Approaches (VGG, GoogLeNet) | This Paper (ResNet) |
|---|---|---|
| Maximum practical depth | ~22 layers | 152+ layers |
| Degradation with depth | Accuracy degrades beyond ~20 layers | Accuracy improves with depth |
| Skip connections | Not used for training depth | Core architectural principle |
| ImageNet top-5 error | ~7% (GoogLeNet) | 3.57% |

---

## 🌍 Real-World Applicability

**Use cases:**

ResNet backbones are ubiquitous in production: medical imaging diagnostics, autonomous driving perception, satellite image analysis, content moderation, and industrial quality inspection. ResNet-50 remains one of the most deployed vision models due to its balance of accuracy, speed, and simplicity. The residual connection principle has been adopted across all domains — transformers, speech models, and even graph neural networks.

**Production considerations:**

| Factor | Assessment |
|---|---|
| **Compute cost** | 🟢 Low (ResNet-18/34) to 🟡 Medium (ResNet-50/101) |
| **Data requirements** | ImageNet-scale preferred; transfers well with fine-tuning |
| **Latency** | Fast inference, well-optimized in all frameworks |
| **Scalability** | Excellent — many optimized variants (ResNeXt, SE-ResNet) |

---

## 💻 Code

> **Status:** 🔲 Not started

| File | Description |
|---|---|
| `code/` | *Implementation coming soon* |

---

## 📊 Key Results

| Benchmark | Metric | This Paper | Previous SOTA |
|---|---|---|---|
| ImageNet (ILSVRC 2015) | Top-5 Error | 3.57% | 6.67% (GoogLeNet) |
| CIFAR-10 | Error Rate | 6.43% (110 layers) | — |
| COCO Detection | mAP | 59.0% | 45.8% (VGG) |

---

## 🤔 Personal Notes

Benchmark results has evolved significantly. 

---

## 📎 References

1. Simonyan & Zisserman. "Very Deep Convolutional Networks for Large-Scale Image Recognition" (2015). [arXiv](https://arxiv.org/abs/1409.1556)
2. Szegedy et al. "Going Deeper with Convolutions" (2015). [arXiv](https://arxiv.org/abs/1409.4842)

---

<div align="center">

[← Back to Deep Learning](../README.md) · [← Back to Main](../../../README.md)

</div>
