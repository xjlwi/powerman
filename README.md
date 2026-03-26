<div align="center">

# 🧠 ML Research Portfolio

**A curated collection of research papers, implementations, and applied insights across Machine Learning, Deep Learning, and AI.**

[![Papers Studied](https://img.shields.io/badge/Papers_Studied-9-blue?style=for-the-badge&logo=arxiv&logoColor=white)](#)
[![Implementations](https://img.shields.io/badge/Implementations-0-green?style=for-the-badge&logo=python&logoColor=white)](#)
[![Topics](https://img.shields.io/badge/Topics-5-orange?style=for-the-badge&logo=bookstack&logoColor=white)](#-research-topics)

---

*Building intuition from first principles. Each paper is studied for its methodology, innovation, and real-world applicability — not just its results.*

</div>

---

## 📋 About This Portfolio

This repository documents my journey studying foundational and cutting-edge research across ML/AI. Each paper entry includes a structured breakdown covering the core ideas, technical methodology, what makes it novel, and where it applies in production systems. Day 1 of building: 26 March 26.

**What you'll find for each paper:**

| Section | Description |
|---|---|
| 📝 **Summary** | Core contribution in plain language |
| 🏷️ **Tags** | Quick-scan taxonomy (task, architecture, domain) |
| 🔬 **Methodology** | How it works — architectures, losses, training details |
| 💡 **Innovation** | What's genuinely new vs. incremental improvement |
| 🌍 **Real-World Applicability** | Where and how this transfers to production |
| 💻 **Code** | Replications, experiments, and notebooks *(when available)* |

---

## 🗂️ Research Topics

<table>
<tr>
<td align="center" width="20%">
<br>
<a href="papers/deep-learning/README.md">
<img src="https://img.shields.io/badge/-Deep%20Learning-FF6F61?style=for-the-badge&logo=pytorch&logoColor=white" alt="Deep Learning"/>
</a>
<br><br>
<sub>CNNs · Architectures · Optimization · Regularization · Foundation Models</sub>
<br><br>
</td>
<td align="center" width="20%">
<br>
<a href="papers/nlp-llms/README.md">
<img src="https://img.shields.io/badge/-NLP%20%2F%20LLMs-4A90D9?style=for-the-badge&logo=openai&logoColor=white" alt="NLP / LLMs"/>
</a>
<br><br>
<sub>Language Models · RAG · Fine-tuning · Prompting · Alignment</sub>
<br><br>
</td>
<td align="center" width="20%">
<br>
<a href="papers/transformers/README.md">
<img src="https://img.shields.io/badge/-Transformers-9B59B6?style=for-the-badge&logo=huggingface&logoColor=white" alt="Transformers"/>
</a>
<br><br>
<sub>Attention · Efficient Transformers · Vision Transformers · Multimodal</sub>
<br><br>
</td>
<td align="center" width="20%">
<br>
<a href="papers/time-series/README.md">
<img src="https://img.shields.io/badge/-Time%20Series-2ECC71?style=for-the-badge&logo=graphql&logoColor=white" alt="Time Series"/>
</a>
<br><br>
<sub>Forecasting · Anomaly Detection · Temporal Models · Sequence Modeling</sub>
<br><br>
</td>
<td align="center" width="20%">
<br>
<a href="papers/machine-learning/README.md">
<img src="https://img.shields.io/badge/-Machine%20Learning-F39C12?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Machine Learning"/>
</a>
<br><br>
<sub>Classical ML · Ensemble Methods · Feature Engineering · AutoML</sub>
<br><br>
</td>
</tr>
</table>

---

## 🚀 Quick Navigation

> Click a topic above to browse papers, or use the index below to jump to a specific entry.

### Recently Added

| Paper | Topic | Tags | Code |
|---|---|---|---|
| [Deep Residual Learning (ResNet)](papers/deep-learning/resnet/README.md) | Deep Learning | `CNN` `ResNet` `Architecture` | 🔲 |
| [Batch Normalization](papers/deep-learning/batch-normalization/README.md) | Deep Learning | `Optimization` `BatchNorm` `Training` | 🔲 |
| [BERT](papers/nlp-llms/bert/README.md) | NLP / LLMs | `Language Models` `Fine-tuning` `Embeddings` | 🔲 |
| [GPT-3: Few-Shot Learners](papers/nlp-llms/gpt3-few-shot-learners/README.md) | NLP / LLMs | `Language Models` `In-Context Learning` `Prompting` | 🔲 |
| [Attention Is All You Need](papers/transformers/attention-is-all-you-need/README.md) | Transformers | `Self-Attention` `Architecture` `NLP` | 🔲 |
| [Vision Transformer (ViT)](papers/transformers/vision-transformer/README.md) | Transformers | `Vision Transformers` `Multimodal` | 🔲 |
| [Temporal Fusion Transformers](papers/time-series/temporal-fusion-transformers/README.md) | Time Series | `Forecasting` `Temporal Fusion` `Multivariate` | 🔲 |
| [Informer](papers/time-series/informer/README.md) | Time Series | `Forecasting` `Autoregressive` | 🔲 |
| [XGBoost](papers/machine-learning/xgboost/README.md) | Machine Learning | `Ensemble Methods` `Classification` `Regression` | 🔲 |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

---

## 📂 Repository Structure

```
├── README.md                     ← You are here
├── papers/
│   ├── deep-learning/
│   │   ├── README.md             ← Topic overview + paper index
│   │   └── <paper-slug>/
│   │       ├── README.md         ← Paper breakdown
│   │       ├── code/             ← Implementations & notebooks
│   │       └── assets/           ← Figures, diagrams
│   ├── nlp-llms/
│   ├── transformers/
│   ├── time-series/
│   └── machine-learning/
├── assets/
│   └── images/                   ← Shared images & banners
└── CLAUDE.md                     ← Project instructions
```

---

## 📖 How to Use This Repo

1. **Browse by topic** — Click a topic badge above to see all papers in that area
2. **Read a paper breakdown** — Each paper has its own folder with a structured README
3. **Run the code** — Where available, open the notebooks or scripts in `code/`
4. **Add your own** — Use the [paper template](papers/PAPER_TEMPLATE.md) to add new entries

---

<div align="center">

*Built with curiosity and rigor.*

</div>
