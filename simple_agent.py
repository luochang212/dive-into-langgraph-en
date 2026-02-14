import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

# Load model configuration
load_dotenv()

# Configure LLM service
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen3-coder-plus",
)

# Create Agent
agent = create_agent(model=llm)

# langgraph-cli entry function
def get_app():
    return agent
