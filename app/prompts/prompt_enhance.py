"""
Enhanced system prompt
"""

agent_system_prompt = """
You are an intelligent assistant

Thinking criteria:
1. Adjust thinking depth based on the complexity of user questions
2. Here is the system environment information:
  - Current time: {current_time}
  - Current timezone: {current_timezone}
  - Username: {username}
  - Operating system: {user_os}
""".strip()


def get_system_prompt() -> str:
    """Get system prompt"""
    # Lazy import
    from utils.device_info import get_info

    # Process operating system information
    raw_os = get_info("Operating System (platform)") or "Unknown"
    user_os = "macOS" if raw_os == "Darwin" else raw_os

    return agent_system_prompt.format(
        current_time=get_info("Current Time (now)"),
        current_timezone=get_info("Timezone (timezone)"),
        username=get_info("Username (username)"),
        user_os=user_os,
    )


if __name__ == "__main__":
    import os
    import sys

    # Add project root directory to Python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.dirname(current_dir)
    sys.path.insert(0, app_dir)

    print(get_system_prompt())
