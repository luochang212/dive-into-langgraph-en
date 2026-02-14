# Chart Visualization MCP Server

GitHub: [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart)

Install the package globally:

```bash
npm install -g @antv/mcp-server-chart
```

Start the server:

```bash
# For Streamable transport with custom endpoint
mcp-server-chart --transport streamable --port 1123
```

Configure MCP Server in [app.py](../../app.py):

```
"Chart Visualization": {
    "url": "http://localhost:1123/mcp",
    "transport": "streamable_http",
},
```
