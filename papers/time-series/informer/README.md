<div align="center">

# 📄 Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting

**Authors:** Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, Wancai Zhang
**Published:** AAAI · 2021 (Best Paper)
**Link:** [arXiv](https://arxiv.org/abs/2012.07436) | [PDF](https://arxiv.org/pdf/2012.07436)

</div>

---

> **One-line takeaway:** *ProbSparse self-attention reduces the O(n²) cost of transformers to O(n log n), enabling direct long-horizon time series forecasting without iterative decoding.*

---

## 🏷️ Tags

![Task](https://img.shields.io/badge/-Long--Horizon%20Forecasting-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/-Efficient%20Transformer-purple?style=flat-square)
![Domain](https://img.shields.io/badge/-Time%20Series-green?style=flat-square)
![Method](https://img.shields.io/badge/-Supervised-orange?style=flat-square)
![Scale](https://img.shields.io/badge/-Long%20Sequences-red?style=flat-square)

---

## 📝 Summary

Informer tackled three key bottlenecks when applying transformers to long-horizon time series forecasting: (1) the quadratic time/memory cost of canonical self-attention, (2) the stacking of encoder/decoder layers creating memory bottlenecks, and (3) the slow speed of step-by-step autoregressive decoding for long outputs. It introduced ProbSparse attention (selects only the most informative queries), self-attention distilling (halves the cascade layer input through progressive downsampling), and a generative-style decoder that predicts the entire output sequence at once. Informer won the AAAI 2021 Best Paper award and kicked off a wave of transformer-based time series research.

---

## 🔬 Methodology

### Architecture

The encoder uses ProbSparse self-attention layers interleaved with distilling layers (Conv1d + MaxPool) that progressively reduce sequence length. Multiple encoder copies at different resolutions are combined. The decoder takes a "start token" segment (tail of the known sequence) concatenated with placeholder zeros for the prediction window, and generates all future values in a single forward pass using masked ProbSparse attention.

### Training

| Component | Details |
|---|---|
| **Loss function** | MSE |
| **Optimizer** | Adam |
| **Learning rate** | 1e-4 |
| **Batch size** | 32 |
| **Prediction horizons** | 24, 48, 168, 336, 720 steps |
| **Hardware** | Single NVIDIA V100 GPU |

### Key Equations

**ProbSparse Attention (query sparsity measurement):**

$$
M(q_i, K) = \max_j \left( \frac{q_i k_j^T}{\sqrt{d}} \right) - \frac{1}{L_K} \sum_{j=1}^{L_K} \frac{q_i k_j^T}{\sqrt{d}}
$$

Only the top-u queries (where u = c · ln L_Q) with highest M scores are computed with full attention; the rest use the mean value.

---

## 💡 Innovation

**What's new:**

The key insight behind ProbSparse attention is that in self-attention, most query-key dot products contribute little — the attention distribution is often highly concentrated. By measuring the "sparsity" of each query's attention distribution (via the KL-divergence-inspired M measure), Informer identifies and computes only the dominant queries. The generative decoder is also significant: instead of predicting one step at a time (which accumulates error), it predicts the entire horizon at once, eliminating error propagation.

**Compared to prior work:**

| Aspect | Vanilla Transformer | Informer |
|---|---|---|
| Attention complexity | O(L²) | O(L log L) |
| Memory usage | O(L²) | O(L log L) |
| Decoding | Autoregressive (step-by-step) | Generative (single forward pass) |
| Long horizon accuracy | Degrades with length | Maintains quality |
| Encoder memory | Fixed per layer | Distilling reduces progressively |

---

## 🌍 Real-World Applicability

**Use cases:**

Informer is suited for domains requiring long-horizon forecasts: energy grid load prediction (days to weeks ahead), weather forecasting, supply chain demand planning over extended horizons, and infrastructure capacity planning. Its efficiency makes it practical for scenarios with long input sequences (e.g., high-frequency sensor data) where vanilla transformers would be too expensive.

**Production considerations:**

| Factor | Assessment |
|---|---|
| **Compute cost** | 🟢 Low to 🟡 Medium — significantly cheaper than vanilla transformer |
| **Data requirements** | Needs sufficient historical data for long-range patterns |
| **Latency** | Fast — single forward pass for all future steps |
| **Scalability** | Handles sequences up to thousands of time steps |

---

## 💻 Code

> **Status:** 🔲 Not started

| File | Description |
|---|---|
| `code/` | *Implementation coming soon* |

---

## 📊 Key Results

| Benchmark | Horizon | This Paper (MSE) | Best Baseline (MSE) |
|---|---|---|---|
| ETTh1 | 720 | 0.183 | 0.424 (LogTrans) |
| ETTm1 | 672 | 0.194 | 0.543 (LSTNet) |
| ECL | 336 | 0.280 | 0.370 (LSTNet) |

---

## 🤔 Personal Notes

*Add your reflections here after studying the paper.*

---

## 📎 References

1. Li et al. "Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting" (LogTrans, 2019). [arXiv](https://arxiv.org/abs/1907.00235)
2. Kitaev et al. "Reformer: The Efficient Transformer" (2020). [arXiv](https://arxiv.org/abs/2001.04451)

---

<div align="center">

[← Back to Time Series](../README.md) · [← Back to Main](../../../README.md)

</div>
