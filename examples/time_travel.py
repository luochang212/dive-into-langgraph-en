import os
import uuid

from dotenv import load_dotenv
from typing_extensions import TypedDict, NotRequired
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver


# Load model configuration
load_dotenv()


# Load model
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen3-coder-plus",
    temperature=0.7,
)


class State(TypedDict):
    topic: NotRequired[str]
    joke: NotRequired[str]


def generate_topic(state: State):
    """Call LLM to generate a joke topic"""
    msg = llm.invoke("请写一个有趣的笑话主题")
    return {"topic": msg.content}


def write_joke(state: State):
    """Based on the joke topic, call LLM to write a short joke"""
    msg = llm.invoke(f"请围绕笑话主题「{state['topic']}」写一个简短的笑话")
    return {"joke": msg.content}


# Build workflow
workflow = StateGraph(State)

# Add nodes
workflow.add_node("generate_topic", generate_topic)
workflow.add_node("write_joke", write_joke)

# Connect node edges
workflow.add_edge(START, "generate_topic")
workflow.add_edge("generate_topic", "write_joke")
workflow.add_edge("write_joke", END)

# Compile
checkpointer = InMemorySaver()
graph = workflow.compile(checkpointer=checkpointer)

# Execute workflow
config = {
    "configurable": {
        "thread_id": uuid.uuid4(),
    }
}
state = graph.invoke({}, config)

print(state["topic"])
print()
print(state["joke"])

# States will be returned in reverse chronological order
states = list(graph.get_state_history(config))

for state in states:
    print(state.next)
    print(state.config["configurable"]["checkpoint_id"])
    print()

# This is the second-to-last state (states are listed in chronological order)
selected_state = states[1]
print(selected_state.next)
print(selected_state.values)

# Create a new checkpoint, which will be associated with the same thread but with a new checkpoint ID
new_config = graph.update_state(selected_state.config, values={"topic": "蘑菇"})
new_config = graph.update_state(new_config, values={"joke": ""})
print(new_config)

# Resume execution from checkpoint
new_state = graph.invoke(None, new_config)

print(new_state["topic"])
print()
print(new_state["joke"])

# recalc = write_joke(new_state)
# print(recalc["joke"])
