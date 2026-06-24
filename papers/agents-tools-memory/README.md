# Agents, Tools & Memory

> Agents are the part of the stack where the hype is loudest and the production track record is shortest. Reading the literature carefully is how you separate "what works now" from "what might work later."

## Why this category exists

The 2024–2026 cycle of agent products has been a useful, expensive education. ToolGen reframes tool calling as a generation problem rather than a routing problem; the Agents Memory survey systematizes what "memory" even means in this context (short-term context, long-term episodic, semantic); the Cohere enterprise ebook is the practitioner's view of what actually ships; and the Anthropic / Greyling piece is the contrarian read that says "stop building agents, build skills." All four belong on the desk of anyone making architectural decisions about agentic systems right now.

## Papers

| Paper | Year | What it gave us | Folder |
|---|---|---|---|
| ToolGen: Unified Tool Retrieval and Calling via Generation | 2024 | Treats tool selection as token generation — scales to thousands of tools where retrieval-then-call breaks. | [toolgen](toolgen/) |
| Agents Memory | 2025 | A survey/taxonomy of memory in LLM agents: short-term, long-term, episodic, semantic, procedural. | [agents-memory](agents-memory/) |
| Cohere: Building Enterprise AI Agents (Ebook) | 2025 | Vendor-written but useful: the patterns that show up across real enterprise deployments. | [cohere-enterprise-agents](cohere-enterprise-agents/) |
| Anthropic Says Don't Build Agents, Build Skills Instead | 2026 | The contrarian take: composable, scoped skills beat open-ended agents for reliability. | [anthropic-skills](anthropic-skills/) |

## Demo notebook

`agents-tools-memory.ipynb` — builds a minimal agent loop in pure Python (no LangChain, no frameworks): a planner that proposes a tool call, an executor, and a scratchpad that doubles as short-term memory. Tools include a local file search and a Python REPL. The notebook then layers in two memory modes: (a) raw conversation buffer, (b) a small FAISS-backed semantic memory. Final cell measures task success across the two memory configurations on a tiny benchmark of 10 tasks — the goal is to make the trade-offs tangible.

## My take

I've shipped agents that work. I've also shipped agents that confidently did the wrong thing for two weeks before anyone noticed. The pattern I trust most in 2026:

- **Skills, not agents, when the task is well-scoped.** A skill is a function with a contract. An agent is a process with a goal. Functions are testable; goals are not.
- **Tools should be idempotent and observable.** Every tool call should be safe to retry and emit a structured trace.
- **Memory is a database problem.** Stop pretending it's a prompt engineering problem. If your "memory" is just appending to a string, you don't have memory.

The Anthropic skills framing is closer to where production GenAI engineering actually lives than the agent-as-research-direction framing.
