## Local Deployment of `qwen3:4b` using Ollama

Below is an example using macOS; steps for other desktop systems are similar.

### 1. Install Ollama

- **Visit official website**: `https://ollama.com`
- **Download and install** the package for your system (macOS/Windows/Linux)
- After installation, the `ollama` command is available in the terminal

### 2. Download `qwen3:4b` Model

Execute in terminal:

```bash
ollama pull qwen3:4b
```

Wait for the model download to complete.

### 3. Start Ollama Service

#### 3.1 Local Use Only

```bash
ollama serve
```

By default, the HTTP interface is exposed at `http://127.0.0.1:11434`.

#### 3.2 LAN Access (accessible by other machines / Docker)

```bash
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

Then on other machines, you can access using your machine's IP and port `11435`.

### 4. Simple API Test

```bash
curl http://127.0.0.1:11435/api/generate -d '{
  "model": "qwen3:4b",
  "prompt": "Introduce yourself in one sentence."
}'
```

If you see streaming content returned, it means the local qwen3:4b + Ollama service is working properly.

### 5. Use in LangChain

```python
"""
How to run:
    pip install -U langchain-openai
    OLLAMA_HOST=0.0.0.0:11435 ollama serve
    python ollama.py
"""

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="qwen3:4b",
    base_url="http://127.0.0.1:11435/v1",
    api_key="-",
)

resp = llm.invoke("Introduce yourself in one sentence.")
print(resp.content)

# for chunk in llm.stream("Introduce yourself in one sentence."):
#     print(chunk.content, end="", flush=True)
```
