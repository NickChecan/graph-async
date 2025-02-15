from dotenv import load_dotenv
load_dotenv()

import operator
from typing import Annotated, Any, Sequence

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    aggregate: Annotated[list, operator.add]
    which: str

class ReturnNodeValue:

    def __init__(self, node_secret: str):
        self._value = node_secret

    def __call__(self, state: State) -> Any:
        print(f"Adding {self._value} to {state['aggregate']}")
        return {"aggregate": [self._value]}

builder = StateGraph(State)

# > Example 1
# builder.add_node("a", ReturnNodeValue("I'm A"))
# builder.add_edge(START, "a")
# builder.add_node("b", ReturnNodeValue("I'm B"))
# builder.add_node("b2", ReturnNodeValue("I'm B2"))
# builder.add_node("c", ReturnNodeValue("I'm C"))
# builder.add_node("d", ReturnNodeValue("I'm D"))
#
# # Creates the parallel execution automatically
# builder.add_edge("a", "b")
# builder.add_edge("a", "c")
#
# # Simpler flow
# # builder.add_edge("b", "d")
# # builder.add_edge("c", "d")
# # Advanced Flow
# builder.add_edge("b", "b2")
# builder.add_edge(["b2", "c"], "d")
#
# builder.add_edge("d", END)
# < Example 1

# > Example 2
builder.add_node("a", ReturnNodeValue("I'm A"))
builder.add_edge(START, "a")
builder.add_node("b", ReturnNodeValue("I'm B"))
builder.add_node("c", ReturnNodeValue("I'm C"))
builder.add_node("d", ReturnNodeValue("I'm D"))
builder.add_node("e", ReturnNodeValue("I'm E"))

def route_bc_or_cd(state: State) -> Sequence[str]:
    if state["which"] == "cd":
        return ["c", "d"]
    return ["b", "c"]

intermediates = ["b", "c", "d"]

builder.add_conditional_edges(
    "a",
    route_bc_or_cd,
    intermediates
)

for node in intermediates:
    builder.add_edge(node, "e")

builder.add_edge("e", END)
# > Example 2

graph = builder.compile()

graph.get_graph().draw_mermaid_png(output_file_path="async_graph.png")
print(graph.get_graph().draw_mermaid())

if __name__ == "__main__":
    print("Hello Async Graph")
    # graph.invoke({"aggregate": []}, {"configurable": {"thread_id": "foo"}}) # Example 1

    # > Example 2
    # graph.invoke({"aggregate": [], "which": ""}, {"configurable": {"thread_id": "foo"}}) # Run everything in parallel
    graph.invoke({"aggregate": [], "which": "cd"}, {"configurable": {"thread_id": "foo"}}) # Run C and D
    # < Example 2