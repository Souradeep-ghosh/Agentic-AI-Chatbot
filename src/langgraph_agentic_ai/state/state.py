from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """State is a TypedDict that defines the structure of the state object used in the agentic AI graph."""
    messages: Annotated[list, add_messages]