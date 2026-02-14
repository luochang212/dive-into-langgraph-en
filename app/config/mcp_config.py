"""
MCP Configuration
"""

import os


def gen_abspath(base_path: str, rel_path: str) -> str:
    abs_dir = os.path.abspath(base_path)
    return os.path.join(abs_dir, rel_path)


def get_mcp_dict(base_path: str = "./") -> dict:
    """Get MCP configuration"""
    return {
        # Services marked with 🌟 below are recommended to enable
        # =============== Code Execution MCP ===============
        # 🌟 stdio
        "code-execution:stdio": {
            "command": "python",
            "args": [gen_abspath(base_path, "mcp/code_execution.py")],
            "transport": "stdio",
        },
        # streamable http
        "code-execution:http": {
            "url": "http://localhost:8001/mcp",
            "transport": "streamable_http",
        },
        # =============== AMap (Gaode Maps) MCP ===============
        # 🌟 streamable http
        # Must apply for AMap API_KEY first, see .env.example for details
        "amap-maps:http": {
            "url": f"https://mcp.amap.com/mcp?key={os.getenv('AMAP_API_KEY')}",
            "transport": "streamable_http",
        },
        # =============== Chart Visualization MCP ===============
        # 🌟 stdio
        "antv-chart:stdio": {
            "command": "npx",
            "args": ["-y", "@antv/mcp-server-chart"],
            "transport": "stdio",
        },
        # streamable http
        # Must start the service first, refer to mcp/mcp-server-chart/README.md
        "antv-chart:http": {
            "url": "http://localhost:1123/mcp",
            "transport": "streamable_http",
        },
        # =============== Filesystem MCP ===============
        # 🌟 stdio
        "filesystem:stdio": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                gen_abspath(base_path, "space"),
            ],
            "transport": "stdio",
        },
    }
