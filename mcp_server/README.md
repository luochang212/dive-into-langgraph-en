Install the background process management tool `supervisor`:

```bash
pip install supervisor
```

Write configuration and start `supervisord` to maintain background tasks:

```bash
supervisord -c ./mcp_supervisor.conf
```

Check if the ports are providing services normally:

```bash
lsof -i :8000
lsof -i :8001
```

Terminate background tasks:

```bash
pkill -f supervisord
```
