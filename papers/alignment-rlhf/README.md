# Alignment & RLHF

> Pretraining gives you fluent generation. Alignment is the work of getting from "plausible text" to "the thing the user actually asked for, in a form they can use."

## Why this category exists

This is the part of the stack that most enterprise teams underestimate. Pretraining is mostly outsourced to model vendors now, but everyone needs to align outputs to a real task — and that means owning at least the conceptual chain: a reward model trained from preference data, a policy optimized against it (PPO or its newer cousins), and a process for catching reward hacking before it ships. The papers here are the canonical lineage: PPO is the optimizer, the OpenAI summarization paper showed RLHF works on a measurable task, InstructGPT generalized it to open-ended instruction following, and the more recent personal-alignment work points at where this is going — per-user, not just per-model.

## Papers

| Paper | Year | What it gave us | Folder |
|---|---|---|---|
| Proximal Policy Optimization Algorithms | 2017 | The optimizer that made RLHF tractable. Clipped surrogate objective → stable updates. | [ppo](ppo/) |
| Learning to Summarize from Human Feedback | 2020 | First clean demo: RLHF beats supervised fine-tuning on a task people can actually judge. | [rlhf-summarize](rlhf-summarize/) |
| Training Language Models to Follow Instructions (InstructGPT) | 2022 | Generalized RLHF to open-ended instructions — the direct ancestor of ChatGPT-style alignment. | [instructgpt](instructgpt/) |
| Towards an End-to-End Personal Fine-Tuning Framework for AI Value Alignment | 2025 | Per-user value alignment as a fine-tuning loop. Where alignment is heading. | [personal-value-alignment](personal-value-alignment/) |
| Positive Alignment: AI for Human Flourishing | 2026 | Reframes alignment from "don't be harmful" to "actively support human flourishing." | [positive-alignment](positive-alignment/) |

## Demo notebook

`alignment-rlhf.ipynb` — builds a tiny preference dataset on a toy text task (which of two short generations is "more polite"), trains a reward model on the preferences, then runs a minimal PPO loop against the reward. Final cells visualize reward-hacking when you over-optimize. Everything runs on CPU; the goal is mechanical intuition, not benchmarks.

## My take

Alignment is where the engineering culture matters more than the algorithm. You can implement PPO in 200 lines; the actual work is the preference dataset, the rubric your labelers use, the eval set you trust, and the human-in-the-loop process when the reward model goes sideways. Teams that win at alignment are teams that have a *taste-making function* — someone who can articulate, in writing, what "good" looks like for their domain, and who is empowered to reject outputs the model rates highly but a human wouldn't ship.
