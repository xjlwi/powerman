<div align="center">

# 🧠 ML Research Portfolio — Gen AI / CTO Ontology

**A curated collection of research papers, ebooks, essays and runnable demo notebooks across the modern AI stack.**

Organised the way a Gen-AI engineer / CTO would actually use them: substrate → pretraining → alignment → adaptation → retrieval → agents → applied → engineering → strategy.

[![Categories](https://img.shields.io/badge/Categories-10-blue?style=for-the-badge)](#-categories)
[![Demo Notebooks](https://img.shields.io/badge/Demo_Notebooks-10-green?style=for-the-badge&logo=jupyter)](#-demo-notebooks)
[![Items](https://img.shields.io/badge/Items_Studied-32+-orange?style=for-the-badge)](#)

---

*Each category has a written `README.md` framing the category for a recruiter or founder reader, plus a single runnable `.ipynb` that demonstrates the canonical technique on a small public-data problem.*

</div>

---

## 📋 About This Portfolio
version 0.0, 2026-03-26
version 1.0, last updated 2026-05-25


I'm an applied ML scientist and application backend developer with a deep enthusiasm for generative AI. I build production-grade enterprise systems while staying close to the bigger questions — how AI reshapes engineering leadership, product strategy, and the philosophy of what we're actually building.

This repository is the curated, public-facing version of my reading and implementation work. It's been reorganised (May 2026) around a Gen-AI / CTO-level ontology: instead of grouping by classical academic topic, papers and resources are grouped by *the role they play in shipping an AI system*.

**What you'll find for each category:**

| Section | Description |
|---|---|
| 🧭 **Why this category exists** | The CTO-level framing — what role this slice of the stack plays |
| 📚 **Papers / Resources** | Indexed table with takeaways |
| 🧪 **Demo notebook** | A single runnable `.ipynb` showing the canonical technique on small public data |
| 💭 **My take** | Written opinion — what I'd tell a founder, a hire, or a board about this category |

---

## 🗂️ Categories

| | Category | What it covers |
|---|---|---|
| 🧱 | [Foundations](papers/foundations/README.md) | Attention, ResNet, BatchNorm, ViT, Mamba, SAM2 — the architectures every modern AI system inherits |
| 📚 | [LLM Pretraining](papers/llm-pretraining/README.md) | BERT, GPT-3, in-context learning, long-form speech — the pretrained models that defined the field |
| 🎯 | [Alignment & RLHF](papers/alignment-rlhf/README.md) | PPO, RLHF-Summarize, InstructGPT, Personal Value Alignment, Positive Alignment |
| 🔧 | [Adaptation & Fine-Tuning](papers/adaptation-finetuning/README.md) | TinyLoRA, Text-to-LoRA — parameter-efficient adaptation |
| 🔍 | [Retrieval & RAG](papers/retrieval-rag/README.md) | M3-Embedding, MMR, Medium Daily Digest engineering writeup |
| 🤖 | [Agents, Tools & Memory](papers/agents-tools-memory/README.md) | ToolGen, Agent Memory, Cohere Enterprise Agents, Anthropic Skills |
| 📈 | [Time-Series Forecasting](papers/time-series/README.md) | Temporal Fusion Transformers, Informer |
| 🏭 | [Applied ML, Industrial](papers/applied-ml-industrial/README.md) | XGBoost, ECNN Pump Monitoring — the 80% of enterprise ML that isn't generative |
| ⚙️ | [Gen AI Engineering](papers/gen-ai-engineering/README.md) | Chip Huyen's AI Engineering, AI Magazine, OpenClaw tutorial — the craft of shipping |
| 🧭 | [AI Strategy & Leadership](papers/ai-strategy-leadership/README.md) | a16z, HBR, Harvey AI critiques — the business context |

---

## 🧪 Demo Notebooks

Every category folder contains a single end-to-end notebook designed to run on CPU in under a minute (no API keys, mostly synthetic or public-domain data). They are the place to start if you want a "show me what you'd build" sample.

| Category | Notebook | What it shows |
|---|---|---|
| Foundations | [`foundations.ipynb`](papers/foundations/foundations.ipynb) | Attention from scratch + a residual-connection ablation |
| LLM Pretraining | [`llm-pretraining.ipynb`](papers/llm-pretraining/llm-pretraining.ipynb) | Char-level tiny GPT on synthetic Shakespeare |
| Alignment & RLHF | [`alignment-rlhf.ipynb`](papers/alignment-rlhf/alignment-rlhf.ipynb) | Toy preference dataset → reward model → policy gradient → reward-hacking visible |
| Adaptation | [`adaptation-finetuning.ipynb`](papers/adaptation-finetuning/adaptation-finetuning.ipynb) | LoRA vs full fine-tune on a matrix-factorisation toy + multi-task adapter library |
| Retrieval & RAG | [`retrieval-rag.ipynb`](papers/retrieval-rag/retrieval-rag.ipynb) | FAISS-style retrieval + MMR re-ranking over this portfolio's READMEs |
| Agents | [`agents-tools-memory.ipynb`](papers/agents-tools-memory/agents-tools-memory.ipynb) | Bare-metal agent loop, no frameworks, with a memory ablation benchmark |
| Time-Series | [`time-series.ipynb`](papers/time-series/time-series.ipynb) | Seasonal-naive vs gradient-boosted vs tiny attention model |
| Applied ML | [`applied-ml-industrial.ipynb`](papers/applied-ml-industrial/applied-ml-industrial.ipynb) | XGBoost-class model with calibration, lift, permutation importance, drift sketch |
| Gen AI Engineering | [`gen-ai-engineering.ipynb`](papers/gen-ai-engineering/gen-ai-engineering.ipynb) | LLM service skeleton — router, prompt versioning, eval, structured logs, cost model |
| AI Strategy | [`ai-strategy-leadership.ipynb`](papers/ai-strategy-leadership/ai-strategy-leadership.ipynb) | Unit economics of an AI feature, sensitivity heatmap, Monte Carlo on assumptions |

---

## 🚀 Quick Start

```bash
# Browse the portfolio site
open index.html

# Or open the demo notebooks directly
jupyter notebook papers/<category>/<category>.ipynb
```

Notebooks use only widely-available libraries: `numpy`, `torch`, `scikit-learn`, `pandas`, `matplotlib`. No keys, no downloads, no GPU.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

---

## 📂 Repository Structure

```
.
├── README.md                       ← You are here
├── index.html                      ← Portfolio site (open in browser)
├── papers/
│   ├── foundations/                ← Category folder
│   │   ├── README.md               ← Category framing + my take
│   │   ├── foundations.ipynb       ← Runnable demo notebook
│   │   ├── attention-is-all-you-need/
│   │   ├── resnet/
│   │   ├── batch-normalization/
│   │   ├── vision-transformer/
│   │   ├── mamba/
│   │   └── sam2/
│   ├── llm-pretraining/
│   ├── alignment-rlhf/
│   ├── adaptation-finetuning/
│   ├── retrieval-rag/
│   ├── agents-tools-memory/
│   ├── time-series/
│   ├── applied-ml-industrial/
│   ├── gen-ai-engineering/
│   ├── ai-strategy-leadership/
│   └── _misc/                      ← Non-portfolio personal docs
└── CLAUDE.md
```

The previous topic folders (`deep-learning/`, `nlp-llms/`, `transformers/`, `machine-learning/`) are retained as legacy redirects pointing to their new homes in the ontology above.

---

<div align="center">

*Built with curiosity and rigor. Updated May 2026.*

</div>
