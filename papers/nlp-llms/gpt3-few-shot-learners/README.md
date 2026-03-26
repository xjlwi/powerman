<div align="center">

# 📄 Language Models are Few-Shot Learners (GPT-3)

**Authors:** Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, et al.
**Published:** NeurIPS · 2020
**Link:** [arXiv](https://arxiv.org/abs/2005.14165) | [PDF](https://arxiv.org/pdf/2005.14165)

</div>

---

> **One-line takeaway:** *Scaling a language model to 175B parameters enables strong few-shot and zero-shot performance across tasks without any gradient updates, just by conditioning on a few examples in the prompt.*

---

## 🏷️ Tags

![Task](https://img.shields.io/badge/-Language%20Generation-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/-Transformer%20Decoder-purple?style=flat-square)
![Domain](https://img.shields.io/badge/-NLP-green?style=flat-square)
![Method](https://img.shields.io/badge/-Autoregressive-orange?style=flat-square)
![Scale](https://img.shields.io/badge/-175B%20Parameters-red?style=flat-square)

---

## 📝 Summary

GPT-3 showed that sufficiently large language models develop emergent capabilities: they can perform tasks they were never explicitly trained for by simply being shown a few examples in the prompt (few-shot learning) or even from task descriptions alone (zero-shot). At 175 billion parameters, GPT-3 achieved competitive or state-of-the-art results on many NLP benchmarks without any fine-tuning — a radical departure from the BERT-era paradigm of training task-specific models. This paper established scaling laws as a central research direction and demonstrated that in-context learning is a viable alternative to fine-tuning, laying the groundwork for the modern LLM era.

---

## 🔬 Methodology

### Architecture

GPT-3 uses the same autoregressive transformer decoder architecture as GPT-2, scaled up massively. The largest model has 96 layers, 96 attention heads, and a hidden dimension of 12,288. It uses alternating dense and locally banded sparse attention patterns in its layers. The context window is 2048 tokens.

### Training

| Component | Details |
|---|---|
| **Loss function** | Autoregressive language modeling (next-token prediction) |
| **Optimizer** | Adam |
| **Learning rate** | Cosine decay schedule |
| **Batch size** | Gradually increased from 32K to 3.2M tokens |
| **Data** | 300B tokens (filtered Common Crawl, WebText2, Books, Wikipedia) |
| **Hardware** | Thousands of V100 GPUs, estimated $4.6M training cost |

### Key Equations

$$
P(x) = \prod_{i=1}^{n} P(x_i \mid x_1, \dots, x_{i-1})
$$

Standard autoregressive factorization. The novelty is not in the objective but in the emergent capabilities at scale.

---

## 💡 Innovation

**What's new:**

The central finding is that scale alone — with no architectural innovation — produces qualitatively new capabilities. Few-shot learning "in context" means the model adapts to tasks at inference time by pattern-matching from examples in the prompt, with no weight updates. The paper systematically evaluated zero-shot, one-shot, and few-shot settings across dozens of tasks, showing a consistent scaling trend: bigger models are disproportionately better at in-context learning.

**Compared to prior work:**

| Aspect | BERT / Fine-tuning Era | GPT-3 / In-Context Learning |
|---|---|---|
| Task adaptation | Train task-specific head, update all weights | Provide examples in prompt, no training |
| Labeled data needed | Hundreds to thousands of examples | 0–32 examples (in prompt) |
| Model reuse | One model per task | One model, many tasks |
| Scale | 110M–340M parameters | 175B parameters |
| Deployment | Fine-tune and deploy per task | Single API serves all tasks |

---

## 🌍 Real-World Applicability

**Use cases:**

GPT-3 is the direct ancestor of the modern LLM API economy. Its architecture and training approach underpin ChatGPT, Claude, and other commercial systems. In-context learning is now the primary interface for production NLP: code generation, content creation, data extraction, translation, summarization, and agentic workflows all rely on the pattern GPT-3 established.

**Production considerations:**

| Factor | Assessment |
|---|---|
| **Compute cost** | 🔴 High — inference requires multi-GPU setups |
| **Data requirements** | Massive pre-training corpus; zero labeled data at inference |
| **Latency** | 🟡 Medium — autoregressive generation is sequential |
| **Scalability** | API-based serving works well; self-hosting is expensive |

---

## 💻 Code

> **Status:** 🔲 Not started

| File | Description |
|---|---|
| `code/` | *Implementation coming soon* |

---

## 📊 Key Results

| Benchmark | Setting | This Paper | Fine-tuned SOTA |
|---|---|---|---|
| LAMBADA | Zero-shot | 76.2% accuracy | 68.0% |
| TriviaQA | Few-shot | 71.2% accuracy | 68.0% |
| SuperGLUE | Few-shot | 71.8 | 89.3 (fine-tuned) |

---

## 🤔 Personal Notes

*Add your reflections here after studying the paper.*

---

## 📎 References

1. Radford et al. "Language Models are Unsupervised Multitask Learners" (GPT-2, 2019). [Link](https://openai.com/research/better-language-models)
2. Kaplan et al. "Scaling Laws for Neural Language Models" (2020). [arXiv](https://arxiv.org/abs/2001.08361)

---

<div align="center">

[← Back to NLP / LLMs](../README.md) · [← Back to Main](../../../README.md)

</div>
