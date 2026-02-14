"""
langmem memory example
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.store.memory import InMemoryStore
from langmem import create_manage_memory_tool, create_search_memory_tool
from langchain.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen3-coder-plus",
)

# Create agent with memory capabilities
memory_store = InMemoryStore()

agent = create_agent(
    model=llm,
    tools=[
        # Tool for creating, updating, and deleting memories
        create_manage_memory_tool(store=memory_store, namespace=("memories",)),
        # Tool for searching existing memories
        create_search_memory_tool(store=memory_store, namespace=("memories",)),
    ],
)

# Execute example: simple conversation with agent
response = agent.invoke({"messages": [HumanMessage(content="请记住我喜欢编程。")]})
print("智能体响应:", response["messages"][-1].content)

# Retrieve memories to verify storage
search_result = agent.invoke({"messages": [HumanMessage(content="回忆一下我喜欢什么吗？")]})
print("记忆检索结果:", search_result["messages"][-1].content)
