from typing_extensions import TypedDict, list
from langgraph.graph.message import add_message
from typing import Annotated

class State(TypedDict):
    """State is a TypedDict that defines the structure of the state object used in the agentic AI graph."""
    messages: Annotated[list, add_message]