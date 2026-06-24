# Gen AI Engineering

> The craft of shipping generative systems — closer to systems engineering than to research. This category collects the practitioner literature.

## Why this category exists

There's a real gap between research papers and production GenAI work. The research literature tells you how a model is trained; the engineering literature (Chip Huyen's book, industry magazines, practitioner blogs) tells you how the system around the model is built — evaluation harnesses, latency budgets, prompt versioning, fallback chains, observability, cost controls. This is the part of the stack a CTO is hiring for, and the part most candidates can't articulate.

## Resources

| Resource | What it covers | Folder |
|---|---|---|
| AI Engineering (Chip Huyen) | The current canonical practitioner's book on shipping LLM systems. | [ai-engineering-book](ai-engineering-book/) |
| AI Magazine, July 2025 issue | Industry trends snapshot — who's deploying what, where the money is going. | [ai-magazine-2025](ai-magazine-2025/) |
| OpenClaw on AWS Free Tier (Jason Yee) | Worked example: deploying a small AI app on free-tier cloud from an iPad. | [openclaw-aws-tutorial](openclaw-aws-tutorial/) |

## Demo notebook

`gen-ai-engineering.ipynb` — builds a small but *complete* LLM service skeleton: a router that picks between a cheap model and an expensive model based on input length, a prompt template versioned in code, an offline eval harness that scores both routes on a fixed eval set, and a structured-log emitter that would feed a real observability pipeline. Final cell prints a cost-per-1000-requests estimate. Designed to look like the inside of a real production codebase, not a research toy.

## My take

The skills gap I see most often in hiring: candidates can prompt a model, but can't tell me *how they would know if it's getting worse over time.* The Chip Huyen book is the book I wish more applied roles had read — it treats LLM systems as systems, with the same rigor we'd apply to any other production service. The other two resources here round it out: one for the industry context, one as a concrete reminder that shipping AI doesn't require a six-figure cloud bill if you know what you're doing.
