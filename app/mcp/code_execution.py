"""
Code Execution MCP Server
"""

import sys
import subprocess
import tempfile
import textwrap
import os

from fastmcp import FastMCP


# Code execution tool
mcp = FastMCP("code-execution")


@mcp.tool
def execute_python(code: str) -> str:
    """
    Execute Python code and return the result
    Used for mathematical calculations, data analysis, and logical processing

    Args:
        code (str): Python code to execute

    Returns:
        str: Standard output or standard error output of code execution
    """
    # Normalize indentation (LLMs love extra spaces)
    code = textwrap.dedent(code)

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False
    ) as f:
        f.write(code)
        file_path = f.name

    env = {
        "PATH": os.environ.get("PATH", ""),
        "HOME": os.environ.get("HOME", ""),
        "LANG": "C.UTF-8",
    }

    try:
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=20,         # hard stop
            check=False,        # don't raise
            env=env,
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stderr:
            return f"Error:\n{stderr}"

        return stdout if stdout else "Execution finished (no output)"

    except subprocess.TimeoutExpired:
        return "Error: Execution timed out"

    except Exception as e:
        return f"Error: {e}"

    finally:
        os.remove(file_path)


if __name__ == "__main__":
    # # Test
    # print(execute_python("""
    # import math
    # print(sum([i for i in range(10)]))
    # print(math.pi)
    # """))

    # Start MCP Server
    import argparse
    import asyncio

    # Configure network parameters
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 8001))

    parser = argparse.ArgumentParser(description="Start code execution MCP Server")
    parser.add_argument("-t", "--transport", type=str, default="stdio", help="Communication method, optional stdio or http")
    args = parser.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "http":
        asyncio.run(mcp.run(transport="http",
                            host=host,
                            port=port,
                            path="/mcp"))
    else:
        raise ValueError(f"Unknown transport: {args.transport}")
