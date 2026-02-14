"""
Basic system prompt
"""

agent_system_prompt = "You are a helpful assistant. Be concise and accurate."


def get_system_prompt() -> str:
    """Get system prompt"""
    return agent_system_prompt


if __name__ == "__main__":
    print(get_system_prompt())
