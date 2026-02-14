"""
Role-play tool
"""

import operator

from typing import Annotated, TypedDict
from pydantic import BaseModel
from langchain.tools import tool, ToolRuntime
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send
from tools.tool_runtime import ToolSchema


# Role-play prompt
role_play_prompt = "Faced with the situation where the goddess {situation}, as a {role}, how should you reply to the goddess in one sentence? Please return in JSON format with a response field"


# Best response prompt
best_response_prompt = """Below are several types of guys and their reactions to the situation where the goddess {situation}.
Which of the following responses do you think can best win back the goddess's heart? Please return the corresponding ID.
Note that the first reaction corresponds to ID 0. Please return in JSON format with an id field.
Below are the guys' reactions:

{responses}"""


# Roles
class Roles(BaseModel):
    roles: list[str]


# Single role
class Role(BaseModel):
    role: str
    situation: str


# Single response
class Response(BaseModel):
    response: str


# Best response ID
class BestResponse(BaseModel):
    id: int


# Global context
class Overall(TypedDict):
    situation: str
    roles: list[str]
    responses: Annotated[list, operator.add]
    best_response: str
    best_role: str


# Define Doge workflow output schema
class DogeOutput(TypedDict):
    roles: list[str]
    responses: list[dict]
    best_response: str
    best_role: str


# Create Doge workflow
def create_doge_graph(llm):

    # [MAP] Use Send function to distribute roles
    def continue_to_responses(state: Overall):
        return [ Send("generate_response", {"role": r, "situation": state["situation"]}) for r in state["roles"] ]

    # [MAP] Role response node: generate response for each role
    def generate_response(state: Role):
        prompt = role_play_prompt.format(role=state["role"], situation=state["situation"])
        response = llm.with_structured_output(Response).invoke(prompt)
        return {"responses": [{"role": state["role"], "content": response.response}]}

    # [REDUCE] Best response node: return the best response
    def best_response(state: Overall):
        responses = "\n\n".join([r["content"] for r in state["responses"]])
        prompt = best_response_prompt.format(responses=responses, situation=state["situation"])
        response = llm.with_structured_output(BestResponse).invoke(prompt)
        best_record = state["responses"][response.id]
        return {"best_response": best_record["content"], "best_role": best_record["role"]}

    doge_builder = StateGraph(Overall, output_schema=DogeOutput)

    # Add nodes
    doge_builder.add_node("generate_response", generate_response)
    doge_builder.add_node("best_response", best_response)

    # Add edges
    doge_builder.add_conditional_edges(START, continue_to_responses, ["generate_response"])
    doge_builder.add_edge("generate_response", "best_response")
    doge_builder.add_edge("best_response", END)

    # Compile graph
    doge_graph = doge_builder.compile(name='best-response')

    return doge_graph


@tool
def role_play(
    runtime: ToolRuntime[ToolSchema],
    situation: str = "tells you she has to work overtime today",
    roles: list[str] = [
        "Male God", "Troll", "Love-struck", "Playboy", "Cute Younger Brother", "Socially Anxious Otaku",
        "Dominant CEO", "Tea-loving Guy", "Artsy Long-haired Guy", "Cute Anime Fan"
    ],
):
    """Simulate a scenario where multiple personas talk to the goddess in a given situation

    For example, you can set the situation to "not replying to my messages" and simulate different roles
    (such as Male God, Love-struck, Playboy, etc.) responding to the goddess.
    Finally, the model will select the response that can best win back the goddess's heart.

    This tool uses the specified LLM model to simulate responses from various personas (such as Male God,
    Love-struck, Playboy, etc.) in specific situations, and the model selects the most appropriate response.
    When the user does not specify a persona, it is recommended to use the default classic roles.

    Args:
        situation: Description of the situation, default is "tells you she has to work overtime today"
        roles: List of personas for role-playing, default is a set of preset classic roles

    Returns:
        str: Formatted text containing all role responses and best response selection results
    """
    base_url = runtime.context.base_url
    api_key = runtime.context.api_key

    # Default to qwen3-max
    model_name = "qwen3-max"
    llm = init_chat_model(
        model=model_name,
        model_provider="openai",
        base_url=base_url,
        api_key=api_key,
    )
    doge_graph = create_doge_graph(llm)
    response = doge_graph.invoke({"roles": roles, "situation": situation})

    return "\n".join(
        [f"Responses from {len(roles)} personas:"]
        + [f"\n【{item['role']}】\n{item['content']}" for item in response["responses"]]
        + [f"\nThe response most favored by {model_name} is from 【{response.get('best_role')}】:\n{response['best_response']}"]
    )
