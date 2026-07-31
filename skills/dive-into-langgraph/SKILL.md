---
name: dive-into-langgraph
description: A comprehensive guide and reference for building agents using LangGraph 1.0, including ReAct agents, state graphs, and tool integrations.
---

# Dive Into LangGraph

LangGraph is an open-source Agent framework developed by the LangChain team. v1.0 is the stable release with fully upgraded framework capabilities, supporting advanced features such as middleware, state graphs, and multi-agent systems. The content of this skill is provided by the "LangGraph 1.0 Complete Guide".

**LangGraph 1.0 Complete Guide**:

- Online documentation: https://luochang212.github.io/dive-into-langgraph-en/
- GitHub: https://github.com/luochang212/dive-into-langgraph-en

## Installing Dependencies

Basic dependencies:

```bash
pip install \
  langgraph \
  "langchain[openai]" \
  langchain-community \
  langchain-mcp-adapters \
  python-dotenv \
  pydantic
```

## Environment Variables

To use LLMs from a model provider, you need to set environment variables. We recommend using Alibaba Cloud Bailian (DashScope) models:

```bash
# Alibaba Cloud Bailian (DashScope)
# Get it at: https://bailian.console.aliyun.com/
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DASHSCOPE_API_KEY=your_api_key_here

# Volcano Ark (ARK)
# Get it at: https://console.volcengine.com/ark/
ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
ARK_API_KEY=your_api_key_here

# Or other model providers...
```

Please add the environment variables to the `.env` file and fill in your API key.

## Chapter Overview

| No. | Chapter | Description | Read Online | Read Offline |
|------|------|----------|----------|----------|
| 1 | **Quickstart** | Create your first ReAct Agent | [Online](https://luochang212.github.io/dive-into-langgraph-en/quickstart/) | [Local](references/1.quickstart.md) |
| 2 | **StateGraph** | Create workflows using StateGraph | [Online](https://luochang212.github.io/dive-into-langgraph-en/stategraph/) | [Local](references/2.stategraph.md) |
| 3 | **Middleware** | Budget control, message truncation, sensitive word filtering, PII detection | [Online](https://luochang212.github.io/dive-into-langgraph-en/middleware/) | [Local](references/3.middleware.md) |
| 4 | **Human-in-the-loop** | Implement human-in-the-loop using HITL middleware | [Online](https://luochang212.github.io/dive-into-langgraph-en/human-in-the-loop/) | [Local](references/4.human_in_the_loop.md) |
| 5 | **Memory** | Short-term and long-term memory | [Online](https://luochang212.github.io/dive-into-langgraph-en/memory/) | [Local](references/5.memory.md) |
| 6 | **Context Engineering** | Manage context using State, Store, Runtime | [Online](https://luochang212.github.io/dive-into-langgraph-en/context/) | [Local](references/6.context.md) |
| 7 | **MCP Server** | Create MCP Server and integrate with LangGraph | [Online](https://luochang212.github.io/dive-into-langgraph-en/mcp-server/) | [Local](references/7.mcp_server.md) |
| 8 | **Supervisor Pattern** | Two methods: tool-calling, langgraph-supervisor | [Online](https://luochang212.github.io/dive-into-langgraph-en/supervisor/) | [Local](references/8.supervisor.md) |
| 9 | **Parallelization** | Node concurrency, `@task` decorator, Map-reduce, Sub-graphs | [Online](https://luochang212.github.io/dive-into-langgraph-en/parallelization/) | [Local](references/9.parallelization.md) |
| 10 | **RAG** | Vector retrieval, keyword retrieval, hybrid retrieval | [Online](https://luochang212.github.io/dive-into-langgraph-en/rag/) | [Local](references/10.rag.md) |
| 11 | **Web Search** | DashScope, Tavily, and DDGS | [Online](https://luochang212.github.io/dive-into-langgraph-en/web-search/) | [Local](references/11.web_search.md) |

## Official Resources

- [LangChain Official Docs](https://docs.langchain.com/oss/python/langchain/overview)
- [LangGraph Official Docs](https://docs.langchain.com/oss/python/langgraph/overview)
- [Deep Agents Official Docs](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangMem Official Docs](https://langchain-ai.github.io/langmem/)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)
- [LangGraph GitHub Repository](https://github.com/langchain-ai/langgraph)
- [langchain-academy GitHub Repository](https://github.com/langchain-ai/langchain-academy)
