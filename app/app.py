"""
An intelligent agent
"""

import os
import uuid
import asyncio
import textwrap
import argparse

from typing import List, Dict, AsyncIterator, Tuple
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents.middleware import SummarizationMiddleware, TodoListMiddleware, dynamic_prompt, ModelRequest
from prompts import middleware_todolist, subagent_search, prompt_enhance
from utils.web_ui import create_ui, theme, custom_css
from utils.tool_view import format_tool_call, format_tool_result
from utils.remove_html import get_cleaned_text
from tools.tool_runtime import ToolSchema
from tools.tool_sci import calculator
from tools.tool_search import dashscope_search
from tools.tool_role import role_play
from config.mcp_config import get_mcp_dict


# Load model configuration
# Note‼️: Please configure DASHSCOPE_API_KEY in .env first
load_dotenv()


# Whether to clean HTML content in chat history
REMOVE_HTML = False


# # Global variables
_agent = None  # Global Agent instance


# Load LLM model
# ==================== Using DashScope ====================
# Aliyun DashScope currently has free quota, supports the following models:
#   kimi-k2-thinking / deepseek-v3.2 / glm-4.7 / qwen3-coder-plus-2025-07-22
# If it feels slow, you can use paid models:
#   qwen3-max / qwen3-max-preview / qwen3-coder-plus
llm = ChatOpenAI(
    model="qwen3-coder-plus",
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    timeout=30,
    extra_body={
        "chat_template_kwargs": {
            "enable_thinking": True,
        }
    }
)
# ==================== Using Ark ====================
# # ByteDance Volcano Ark currently has free quota, supports the following models:
# #   deepseek-v3-2-251201 / kimi-k2-thinking-251104 / doubao-seed-1-8-251228
# llm = ChatOpenAI(
#     model="deepseek-v3-2-251201",
#     base_url=os.getenv("ARK_BASE_URL"),
#     api_key=os.getenv("ARK_API_KEY"),
#     max_retries=1,
#     timeout=30,
# )
# ==================== Using Ollama ====================
# # Before use, you need to:
# # 1. Download qwen3:4b model
# #     ollama pull qwen3:4b
# # 2. Start Ollama service
# #     OLLAMA_HOST=0.0.0.0:11435 ollama serve
# llm = ChatOpenAI(
#     model="qwen3:4b",
#     base_url="http://127.0.0.1:11435/v1",
#     api_key="-",  # non-empty
#     max_retries=1,
#     timeout=30,
#     temperature=0.7,
#     top_p=0.9,
#     extra_body={
#         "chat_template_kwargs": {
#             "enable_thinking": True,
#         }
#     }
# )
# ==================== End ====================


@dynamic_prompt
def dynamic_system_prompt(request: ModelRequest) -> str:
    """Dynamic system prompt for Agent"""
    return prompt_enhance.get_system_prompt()


@dynamic_prompt
def dynamic_system_prompt_subagent_search(request: ModelRequest) -> str:
    """Dynamic system prompt for Search Subagent"""
    return subagent_search.get_system_prompt()


# Create search subagent
search_subagent = create_agent(
    model=llm,
    tools=[dashscope_search],
    middleware=[dynamic_system_prompt_subagent_search],
)


@tool(
    "subagent_search_brief",
    description=subagent_search.get_tool_description(),
)
async def search_brief(
    query: str,
    runtime: ToolRuntime[ToolSchema],
) -> str:
    """Get summary of search results"""
    result = await search_subagent.ainvoke(
        {"messages": [{"role": "user", "content": query}]},
        config={"configurable": {"thread_id": str(uuid.uuid4())}},
        context=runtime.context,
    )
    return result["messages"][-1].content


async def get_agent():
    """Get global Agent instance"""
    global _agent
    if _agent is None:
        client = MultiServerMCPClient(
            {k: v for k, v in get_mcp_dict().items() if k in {
                # Enabled MCP
                "code-execution:stdio",
                # # Disabled MCP
                # "antv-chart:stdio",
                # "filesystem:stdio",
                # "amap-maps:http",
            }}
        )

        # Get MCP tools
        mcp_tools = await client.get_tools()

        # Create agent
        _agent = create_agent(
            model=llm,
            tools=mcp_tools + [calculator, role_play, dashscope_search, search_brief],
            middleware=[
                dynamic_system_prompt,
                SummarizationMiddleware(
                    model=llm,
                    trigger=("tokens", 2000),
                    keep=("messages", 7),
                ),
                TodoListMiddleware(
                    system_prompt=middleware_todolist.get_system_prompt()
                ),
            ],
        )
    return _agent


def get_tools():
    """Get Agent's tool list"""
    agent = asyncio.run(get_agent())
    node = agent.get_graph().nodes["tools"]
    tools = list(node.data.tools_by_name.values())

    # Optimize tool display
    if len(tools) < 13:
        # When there are not many tools, show tool descriptions
        lines = []
        for tool in tools:
            desc = (tool.description or "").split('\n')[0]
            lines.append(f"- `{tool.name}`: {desc}")
        return "\n".join(lines)
    else:
        # When there are too many tools, only show tool names
        tool_names = [tool.name for tool in tools]
        wrapped_text = textwrap.fill(" / ".join(tool_names), width=100)
        return f"\n```text\n{wrapped_text}\n```\n"


def get_greeting():
    """Get Agent's self-introduction"""
    greeting = ""
    try:
        tools_info = get_tools()
        greeting = "\n".join([
            "Hello! I am your intelligent assistant. Available tools include:",
            tools_info,
            "\nWhat can I help you with?",
        ])
    except Exception as e:
        print(f"Error getting tool list: {e}")
        greeting = "Hello! I am your intelligent assistant.\nWhat can I help you with?"
    return greeting


def error_summary(err: Exception, limit: int = 500) -> str:
    """Summarize Agent runtime errors"""
    import traceback

    # Get full error information
    full_trace = "".join(traceback.format_exception(type(err), err, err.__traceback__))
    full_trace = full_trace[-5000:]  # Avoid overly long error messages

    summary = ""
    try:
        # Prioritize outputting log summary
        abstract = llm.invoke("\n".join([
            full_trace,
            "---",
            "Above is the error information from LangChain Agent, please briefly explain the cause:",
        ]))
        summary = f"\n ⚠️ An error occurred, here is the summary:\n{abstract}"
    except Exception:
        # Summary output failed, fallback to outputting raw logs
        summary = f"\n ⚠️ An error occurred, here is the raw log:\n{full_trace[:limit]}"

    return summary


async def _agent_events_optimize(
    agent,
    messages,
    history: List[Dict[str, str]],
) -> AsyncIterator[Tuple[str, List[Dict[str, str]]]]:
    """Optimize display, process messages and values event streams"""
    async for mode, payload in agent.astream(
        {"messages": messages},
        stream_mode=["messages", "values"],
        context=ToolSchema(
            base_url=os.getenv("DASHSCOPE_BASE_URL"),
            api_key=os.getenv("DASHSCOPE_API_KEY")
        ),
    ):
        if mode == "messages":
            token, metadata = payload
            current_node = metadata["langgraph_node"]
            if current_node == "model":
                # Model response
                if token.content:
                    history[-1]["content"] += token.content
                    yield "", history
            elif current_node == "tools":
                # Avoid duplicate output with search subagent
                if token.name in ["subagent:search-brief"]:
                    continue
                # Tool call result
                if token.content:
                    history[-1]["content"] += format_tool_result(token.name, token.content)
                    yield "", history
        elif mode == "values":
            state = payload
            state_messages = state.get("messages") if isinstance(state, dict) else None
            if not state_messages:
                continue
            last_message = state_messages[-1]

            # Tool call parameters
            tool_calls = getattr(last_message, "tool_calls", None)
            if tool_calls:
                history[-1]["content"] += "".join(
                    format_tool_call((tc.get("name") or "unknown"), (tc.get("args") or {}))
                    for tc in tool_calls
                )
                yield "", history


async def generate_response(message: str,
                            history: List[Dict[str, str]]
):
    """Generate Agent response"""
    if not message:
        yield "", history
        return

    # Clean HTML content in the previous AI response to reduce context burden
    # Without tool messages and thinking chain messages, there wouldn't be so many issues (`ヮ´ )
    if REMOVE_HTML and len(history) >= 1 and history[-1]["role"] == "assistant":
        html_content = history[-1]["content"][0]['text']
        history[-1]["content"][0]['text'] = get_cleaned_text(html_content)

    # print("=================================")
    # print(history)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": ""})

    messages = history[:-1]

    agent = await get_agent()

    # Avoid exit caused by MCP call failure
    try:
        # Use optimized display
        async for update in _agent_events_optimize(agent, messages, history):
            yield update
    except Exception as err:
        print(f"An error occurred: {err}")
        history[-1]["content"] += error_summary(err)
        yield "", history

    yield "", history


def main():
    """Main function"""
    # Configure network parameters
    # Docker reserved operation entry, docker host is generally set to 0.0.0.0
    parser = argparse.ArgumentParser(description="Gradio Agent APP")
    parser.add_argument("--host", type=str, default="localhost", help="Host address")
    parser.add_argument("--port", type=int, default=7860, help="Port number")
    args = parser.parse_args()

    app = create_ui(
        llm_func=generate_response,
        tab_name="Gradio APP - WebUI",
        main_title="Gradio Agent APP",
        initial_message=[{"role": "assistant", "content": get_greeting()}]
    )

    app.launch(
        server_name=args.host,
        server_port=args.port,
        share=False,
        theme=theme,
        css=custom_css
    )


if __name__ == "__main__":
    main()
