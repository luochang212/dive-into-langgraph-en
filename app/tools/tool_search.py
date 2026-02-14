"""
Internet search tool
"""

import dashscope

from dashscope import Generation
from langchain.tools import tool, ToolRuntime
from tools.tool_runtime import ToolSchema


@tool
def dashscope_search(
    query: str,
    runtime: ToolRuntime[ToolSchema],
) -> str:
    """Use DashScope search API to search for internet information"""
    dashscope.api_key = runtime.context.api_key

    response = Generation.call(
        model='qwen-max',
        prompt=query,
        enable_search=True,
        result_format='message'
    )

    if response.status_code == 200:
        return response.output.choices[0].message.content
    else:
        return (
            "Search failed with status code: "
            f"{response.status_code}, message: {response.message}"
        )
