FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Switch to domestic mirror source and install system dependencies
# If you need to use npx, please install nodejs npm 
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && apt-get install -y \
    curl \
    supervisor \
    procps \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files and install Python dependencies
COPY pyproject.toml .
RUN pip install uv==0.9.24 -i https://mirrors.aliyun.com/pypi/simple/
RUN uv sync -i https://mirrors.aliyun.com/pypi/simple/

# Copy application code
COPY app.py .
COPY config/ ./config/
COPY images/ ./images/
COPY mcp/ ./mcp/
COPY prompts/ ./prompts/
COPY space/ ./space/
COPY tools/ ./tools/
COPY utils/ ./utils/

# Copy supervisor configuration file
COPY docker.conf /etc/supervisor/conf.d/supervisord.conf

# Set entrypoint
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
