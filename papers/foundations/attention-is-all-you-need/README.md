<div align="center">

# 📄 Attention Is All You Need

**Authors:** Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin
**Published:** NeurIPS · 2017
**Link:** [arXiv](https://arxiv.org/abs/1706.03762) | [PDF](https://arxiv.org/pdf/1706.03762)

</div>

---

> **One-line takeaway:** *Replaces recurrence entirely with multi-head self-attention, achieving state-of-the-art translation quality with far greater parallelism and training efficiency.*

---

## 🏷️ Tags

![Task](https://img.shields.io/badge/-Machine%20Translation-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/-Transformer-purple?style=flat-square)
![Domain](https://img.shields.io/badge/-NLP-green?style=flat-square)
![Method](https://img.shields.io/badge/-Supervised-orange?style=flat-square)
![Scale](https://img.shields.io/badge/-Large--Scale-red?style=flat-square)

---

## 📝 Summary

This paper introduces the Transformer, an architecture built entirely on attention mechanisms, eliminating the recurrent and convolutional layers previously considered essential for sequence-to-sequence tasks. The key insight is that self-attention can model dependencies regardless of distance in a sequence, while being far more parallelizable than RNNs. The model achieved new SOTA on English-to-German and English-to-French translation benchmarks while training significantly faster than competing architectures. This paper effectively launched the modern era of LLMs, vision transformers, and foundation models.

---

## 🔬 Methodology

### Architecture

The Transformer follows an encoder-decoder structure. The encoder maps an input sequence to a continuous representation, and the decoder generates an output sequence one token at a time using autoregressive decoding. Both stacks are composed of identical layers, each containing multi-head self-attention followed by position-wise feed-forward networks, with residual connections and layer normalization throughout.

### Training

| Component | Details |
|---|---|
| **Loss function** | Label-smoothed cross-entropy (ε = 0.1) |
| **Optimizer** | Adam (β₁=0.9, β₂=0.98, ε=10⁻⁹) |
| **Learning rate** | Warmup + inverse square root decay |
| **Batch size** | ~25,000 source + target tokens |
| **Steps** | 300K (base) / 300K (big) |
| **Hardware** | 8 × NVIDIA P100 GPUs |

### Key Equations

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O
$$

---

## 💡 Innovation

**What's new:**

The paper proved that attention alone — without any recurrence or convolution — is sufficient for state-of-the-art sequence modeling. Multi-head attention allows the model to attend to different representation subspaces at different positions simultaneously. The positional encoding scheme (sinusoidal) elegantly injects order information without learnable parameters.

**Compared to prior work:**

| Aspect | Prior Approaches (RNN/LSTM) | This Paper (Transformer) |
|---|---|---|
| Sequence modeling | Sequential, O(n) steps | Parallel, O(1) with attention |
| Long-range dependencies | Degrades with distance | Constant-time access |
| Training speed | Bottlenecked by recurrence | Highly parallelizable |
| Complexity per layer | O(n · d²) | O(n² · d) |

---

## 🌍 Real-World Applicability

**Use cases:**

The Transformer architecture now underpins virtually all modern NLP systems (GPT, BERT, T5), vision models (ViT, DINO), protein folding (AlphaFold), code generation (Codex, StarCoder), and multimodal systems (CLIP, Flamingo). It is the foundational architecture of the current AI industry.

**Production considerations:**

| Factor | Assessment |
|---|---|
| **Compute cost** | 🟡 Medium (base) / 🔴 High (big) |
| **Data requirements** | Large parallel corpora (WMT datasets) |
| **Latency** | Autoregressive decoding is sequential |
| **Scalability** | Excellent — scales with data and compute |

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
| WMT 2014 EN-DE | BLEU | 28.4 | 26.4 |
| WMT 2014 EN-FR | BLEU | 41.0 | 40.5 |

---

## 🤔 Personal Notes

*Add your reflections here after studying the paper.*

---

## 📎 References

1. Bahdanau et al. "Neural Machine Translation by Jointly Learning to Align and Translate" (2015). [arXiv](https://arxiv.org/abs/1409.0473)
2. Luong et al. "Effective Approaches to Attention-based Neural Machine Translation" (2015). [arXiv](https://arxiv.org/abs/1508.04025)

---

<div align="center">

[← Back to Transformers](../README.md) · [← Back to Main](../../../README.md)

</div>
