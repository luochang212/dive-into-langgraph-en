"""
Sub-agent search system prompt
"""

from datetime import datetime


agent_system_prompt = """
You are a sub-agent responsible for web search, called by the upper-level agent.
You will return a summary of search results, with the summary length controlled within 200 words.

Notes:
- Avoid leaking user personal privacy or sensitive information in searches
- When the user's question has grammatical errors or unclear meaning, please rewrite the user question
- Do not add your own understanding to the search results
- Current time: {current_time}
""".strip()


tool_description = """
A subagent with independent context space, supporting internet search, returning summarized search results

Note, it does not return complete search results, only a summary of search results. Please confirm this meets your use case

Recommended use cases:
1. Need to save context, do not want to receive detailed search results
2. Expected search results are not complex and can be briefly described

Notes:
1. Execute only one query at a time. If there are multiple queries, execute them separately
2. Please briefly but completely tell it context information (if any)

Example: Search for San Jose's latitude, longitude, and altitude
""".strip()


def get_system_prompt() -> str:
    """Get system prompt"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return agent_system_prompt.format(
        current_time=current_time,
    )


def get_tool_description() -> str:
    """Get tool description"""
    return tool_description


if __name__ == "__main__":
    print(get_system_prompt())
    print("=" * 45)
    print(get_tool_description())
