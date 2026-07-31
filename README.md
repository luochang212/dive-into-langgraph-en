<div align="center">
  <img src="./img/social-preview.webp" width="100%">
  <h1>Dive into LangGraph</h1>
</div>

<div align="center">
  <img src="https://img.shields.io/github/stars/luochang212/dive-into-langgraph-en?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/luochang212/dive-into-langgraph-en?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-English-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/luochang212/dive-into-langgraph-en/actions/workflows/ci.yml"><img src="https://github.com/luochang212/dive-into-langgraph-en/actions/workflows/ci.yml/badge.svg?branch=main" alt="ci"/></a>
  <a href="https://github.com/luochang212/dive-into-langgraph-en/actions/workflows/deploy-book.yml"><img src="https://github.com/luochang212/dive-into-langgraph-en/actions/workflows/deploy-book.yml/badge.svg?branch=main" alt="deploy-book"/></a>
  <a href="https://zread.ai/luochang212/dive-into-langgraph-en"><img src="https://img.shields.io/badge/%E2%80%8B-zread-00b0aa?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuOTYxNTYgMS42MDAxSDIuMjQxNTZDMS44ODgxIDEuNjAwMSAxLjYwMTU2IDEuODg2NjQgMS42MDE1NiAyLjI0MDFWNC45NjAxQzEuNjAxNTYgNS4zMTM1NiAxLjg4ODEgNS42MDAxIDIuMjQxNTYgNS42MDAxSDQuOTYxNTZDNS4zMTUwMiA1LjYwMDEgNS42MDE1NiA1LjMxMzU2IDUuNjAxNTYgNC45NjAxVjIuMjQwMUM1LjYwMTU2IDEuODg2NjQgNS4zMTUwMiAxLjYwMDEgNC45NjE1NiAxLjYwMDFaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00Ljk2MTU2IDEwLjM5OTlIMi4yNDE1NkMxLjg4ODEgMTAuMzk5OSAxLjYwMTU2IDEwLjY4NjQgMS42MDE1NiAxMS4wMzk5VjEzLjc1OTlDMS42MDE1NiAxNC4xMTM0IDEuODg4MSAxNC4zOTk5IDIuMjQxNTYgMTQuMzk5OUg0Ljk2MTU2QzUuMzE1MDIgMTQuMzk5OSA1LjYwMTU2IDE0LjExMzQgNS42MDE1NiAxMy43NTk5VjExLjAzOTlDNS42MDE1NiAxMC42ODY0IDUuMzE1MDIgMTAuMzk5OSA0Ljk2MTU2IDEwLjM5OTlaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik0xMy43NTg0IDEuNjAwMUgxMS4wMzg0QzEwLjY4NSAxLjYwMDEgMTAuMzk4NCAxLjg4NjY0IDEwLjM5ODQgMi4yNDAxVjQuOTYwMUMxMC4zOTg0IDUuMzEzNTYgMTAuNjg1IDUuNjAwMSAxMS4wMzg0IDUuNjAwMUgxMy43NTg0QzE0LjExMTkgNS42MDAxIDE0LjM5ODQgNS4zMTM1NiAxNC4zOTg0IDQuOTYwMVYyLjI0MDFDMTQuMzk4NCAxLjg4NjY0IDE0LjExMTkgMS42MDAxIDEzLjc1ODQgMS42MDAxWiIgZmlsbD0iI2ZmZiIvPgo8cGF0aCBkPSJNNCAxMkwxMiA0TDQgMTJaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00IDEyTDEyIDQiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K&logoColor=ffffff" alt="zread"/></a>
</div>

<div align="center">

[Chinese](https://github.com/luochang212/dive-into-langgraph) | English

</div>

<div align="center">
  <p><a href="https://www.luochang.ink/dive-into-langgraph-en/">📚 Read Online</a></p>
  <h3>📖 LangGraph 1.0 Guide</h3>
  <p><em>Build powerful Agents from scratch</em></p>
</div>

---

## 📢 News

### ✨ 2026-03-02 Update

This tutorial has been converted into an Agent Skill. You no longer need to study the tutorial manually — just install this Skill for your [Claude Code](https://github.com/anthropics/claude-code) and you can write high-quality LangChain and LangGraph code. See: [SKILL.md](skills/dive-into-langgraph/SKILL.md)

Install this Skill with npx ([dive-into-langgraph](https://skills.sh/luochang212/dive-into-langgraph-en/dive-into-langgraph)):

```bash
npx skills add luochang212/dive-into-langgraph-en
```

## 1. Project Introduction

> In mid-October 2025, LangGraph released version 1.0. The development team promised this is a stable version, and the interfaces are not expected to change significantly in the future. Now is the perfect time to learn it.

This is an open-source e-book project aimed at helping Agent developers quickly master the LangGraph framework. [LangGraph](https://github.com/langchain-ai/langgraph) is an open-source Agent framework developed by the LangChain team. It is powerful and includes everything you need: Memory, MCP, Guardrails, State Management, and Multi-Agent support. LangGraph is typically used together with [LangChain](https://github.com/langchain-ai/langchain): LangChain provides foundational components and tools, while LangGraph handles workflow and state management. Therefore, both libraries need to be learned. To help everyone get started quickly, this tutorial extracts the main features of both libraries and divides them into 14 chapters.

## 2. Installation

```bash
pip install -r requirements.txt
```

<details>
  <summary>Dependency List</summary>

  Below is the list of dependencies in `requirements.txt`:

  ```text
  pydantic
  python-dotenv
  langchain[openai]
  langchain-community
  langchain-mcp-adapters
  langchain-text-splitters
  langgraph
  langgraph-cli[inmem]
  langgraph-supervisor
  langgraph-checkpoint-sqlite
  langgraph-checkpoint-redis
  langmem
  ipynbname
  fastmcp
  bs4
  scikit-learn
  supervisor
  jieba
  dashscope
  tavily-python
  ddgs
  ```
</details>

## 3. Table of Contents

Overview of this tutorial's content:

| No. | Chapter | Main Content |
| -- | -- | -- |
| 1 | [Quickstart](./1.quickstart.ipynb) | Create your first ReAct Agent |
| 2 | [StateGraph](./2.stategraph.ipynb) | Create workflows using StateGraph |
| 3 | [Middleware](./3.middleware.ipynb) | Use custom middleware to implement four features: budget control, message truncation, sensitive word filtering, and PII detection |
| 4 | [Human-in-the-loop](./4.human_in_the_loop.ipynb) | Implement human-in-the-loop using built-in HITL middleware |
| 5 | [Memory](./5.memory.ipynb) | Create short-term and long-term memory |
| 6 | [Context Engineering](./6.context.ipynb) | Manage context using State, Store, and Runtime |
| 7 | [MCP Server](./7.mcp_server.ipynb) | Create MCP Server and integrate with LangGraph |
| 8 | [Supervisor Pattern](./8.supervisor.ipynb) | Two methods to implement Supervisor Pattern: tool-calling and langgraph-supervisor |
| 9 | [Parallelization](./9.parallelization.ipynb) | How to implement concurrency: node parallelism, `@task` decorator, Map-reduce, and Sub-graphs |
| 10 | [RAG](./10.rag.ipynb) | Three ways to implement RAG: vector retrieval, keyword retrieval, and hybrid retrieval |
| 11 | [Web Search](./11.web_search.ipynb) | Implement web search: DashScope, Tavily, and DDGS |
| 12 | [Deep Agents](./12.deep_agents.ipynb) | Brief introduction to Deep Agents |
| 13 | [Gradio APP](./13.gradio_app.ipynb) | Develop a streaming conversational Agent application based on Gradio |
| 14 | [Appendix: Debug Page](./14.langgraph_cli.ipynb) | Introduce the debug page provided by langgraph-cli |

> [!NOTE]
>
> **Promise**: This tutorial is entirely based on LangGraph v1.0, with no legacy code from v0.6.

## 4. Debug Page

`langgraph-cli` provides a debug page that can be launched quickly.

```bash
langgraph dev
```

See details: [Appendix: Debug Page](https://www.luochang.ink/dive-into-langgraph-en/langgraph-cli/)

## 5. Practical Chapter

[Chapter 13](https://www.luochang.ink/dive-into-langgraph-en/gradio-app/) open-sources an Agent application implemented with Gradio + LangChain. The effect is shown below. You can add more features to this application and customize your own Agent.

![gradio_app](./app/images/gradio_app.webp)

See details: [/app](./app/)

## 6. Further Reading

**Official Documentation:**

- [LangChain](https://docs.langchain.com/oss/python/langchain/overview)
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangMem](https://langchain-ai.github.io/langmem/)

**Official Tutorials:**

- [langgraph-101](https://github.com/langchain-ai/langgraph-101)
- [langchain-academy](https://github.com/langchain-ai/langchain-academy)

## 7. How to Contribute

We welcome any form of contribution!

- 🐛 Report Bugs - Submit an Issue if you find any problems
- 💡 Feature Suggestions - Let us know if you have good ideas
- 📝 Content Improvement - Help improve the tutorial content
- 🔧 Code Optimization - Submit Pull Requests

## 8. Star History

[![Star History Chart](https://api.star-history.com/svg?repos=luochang212/dive-into-langgraph-en&type=date&legend=top-left)](https://www.star-history.com/#luochang212/dive-into-langgraph-en&type=date&legend=top-left)

## 9. License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
