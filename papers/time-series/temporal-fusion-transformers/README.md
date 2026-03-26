<div align="center">

# 📄 Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting

**Authors:** Bryan Lim, Sercan O. Arik, Nicolas Loeff, Tomas Pfister
**Published:** International Journal of Forecasting · 2021
**Link:** [arXiv](https://arxiv.org/abs/1912.09363) | [PDF](https://arxiv.org/pdf/1912.09363)

</div>

---

> **One-line takeaway:** *A transformer-based architecture purpose-built for time series that automatically selects relevant features, handles multiple input types, and provides interpretable attention over temporal dynamics.*

---

## 🏷️ Tags

![Task](https://img.shields.io/badge/-Forecasting-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/-Transformer-purple?style=flat-square)
![Domain](https://img.shields.io/badge/-Time%20Series-green?style=flat-square)
![Method](https://img.shields.io/badge/-Supervised-orange?style=flat-square)
![Scale](https://img.shields.io/badge/-Multi--Horizon-red?style=flat-square)

---

## 📝 Summary

The Temporal Fusion Transformer (TFT) addresses a key limitation of existing deep learning forecasting models: they treat all inputs uniformly and provide little interpretability. TFT introduces specialized components for handling different input types (static covariates, known future inputs, observed past inputs), a variable selection network that learns which features matter, and an interpretable multi-head attention mechanism over time steps. It produces multi-horizon probabilistic forecasts while revealing which variables and time steps drive predictions. TFT achieved state-of-the-art on multiple real-world forecasting benchmarks while providing insights that domain experts can actually use.

---

## 🔬 Methodology

### Architecture

TFT consists of several specialized components stacked together: (1) **Variable Selection Networks** — gated residual networks with softmax that select the most relevant input features at each time step. (2) **Static Covariate Encoders** — condition the entire temporal processing on static metadata (e.g., store ID, product category). (3) **LSTM Encoder-Decoder** — captures local temporal patterns for both past and known future inputs. (4) **Temporal Self-Attention** — interpretable multi-head attention that captures long-range dependencies across time. (5) **Quantile Outputs** — predicts quantiles (10th, 50th, 90th) for probabilistic forecasts.

### Training

| Component | Details |
|---|---|
| **Loss function** | Quantile loss (sum over quantiles 0.1, 0.5, 0.9) |
| **Optimizer** | Adam |
| **Learning rate** | Tuned per dataset (typically 1e-3 to 1e-2) |
| **Batch size** | 64 |
| **Epochs** | Early stopping on validation loss |
| **Hardware** | Single GPU |

### Key Equations

**Gated Residual Network (core building block):**

$$
\text{GRN}(a, c) = \text{LayerNorm}(a + \text{GLU}(\eta_1))
$$
$$
\eta_1 = W_1 \eta_2 + b_1, \quad \eta_2 = \text{ELU}(W_2 a + W_3 c + b_2)
$$

**Variable Selection:**

$$
v_t = \text{Softmax}(\text{GRN}(\Xi_t)) \quad \text{(variable importance weights)}
$$

---

## 💡 Innovation

**What's new:**

Most deep forecasting models at the time (DeepAR, WaveNet, N-BEATS) were either black boxes or didn't handle heterogeneous inputs well. TFT introduced three innovations simultaneously: (1) explicit variable selection that quantifies feature importance, (2) a multi-input architecture that naturally separates static, known-future, and observed-past information, and (3) interpretable attention patterns that show *which historical time steps* influence predictions. This combination of performance and interpretability was unique.

**Compared to prior work:**

| Aspect | DeepAR / N-BEATS | TFT |
|---|---|---|
| Input types | Single input stream | Static, known future, observed past |
| Feature selection | Manual / external | Learned, automatic |
| Interpretability | Black box | Attention + variable importance |
| Output type | Point or parametric | Quantile (probabilistic) |
| Static covariates | Limited support | First-class conditioning |

---

## 🌍 Real-World Applicability

**Use cases:**

TFT is widely used in retail demand forecasting (Walmart, Amazon-style inventory planning), energy load forecasting, financial market prediction, and healthcare patient monitoring. Its interpretability is particularly valuable in regulated industries where stakeholders need to understand *why* a forecast was made. Google AI developed TFT internally and it's available in production forecasting libraries.

**Production considerations:**

| Factor | Assessment |
|---|---|
| **Compute cost** | 🟡 Medium — more expensive than ARIMA, cheaper than ensemble approaches |
| **Data requirements** | Needs sufficient history; handles multiple time series jointly |
| **Latency** | Suitable for batch forecasting; not ideal for sub-second streaming |
| **Scalability** | Handles thousands of parallel time series |

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
| Electricity | P50 QL | 0.055 | 0.059 (DeepAR) |
| Traffic | P50 QL | 0.095 | 0.105 (MQRNN) |
| Retail (Favorita) | P50 QL | 0.245 | 0.259 (DeepAR) |
| Volatility | P50 QL | 0.042 | 0.046 (DeepAR) |

---

## 🤔 Personal Notes

*Add your reflections here after studying the paper.*

---

## 📎 References

1. Salinas et al. "DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks" (2020). [arXiv](https://arxiv.org/abs/1704.04110)
2. Oreshkin et al. "N-BEATS: Neural basis expansion analysis for interpretable time series forecasting" (2020). [arXiv](https://arxiv.org/abs/1905.10437)

---

<div align="center">

[← Back to Time Series](../README.md) · [← Back to Main](../../../README.md)

</div>
