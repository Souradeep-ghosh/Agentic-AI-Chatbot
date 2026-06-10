from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

# It will return the tools it has
def get_tools():
    """
    Returns the list of tools to be used in the chatbot
    """
    tools = [TavilySearchResults(max_results=3)]
    return tools
    
def create_tool_node(tools):
    """
    It creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)