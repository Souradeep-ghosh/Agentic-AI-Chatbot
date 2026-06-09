from langgraph.graph import StateGaph
from src.langgraph_agentic_ai.state.state import State
from langgraph.graph import START, END

class GraphBuilder: 
    def __init__(self, model):
        self.llm = model
        self.graph_builder= StateGaph(State)
        
        
    def basic_chatbot_build_graph(self):
        """This method builds a basic chatbot graph using the StateGraph class. 
        It defines the structure of the graph and how messages are processed.
        
        Returns:
            StateGaph: An instance of the StateGraph class representing the chatbot graph.
        """
        
        self.graph_builder.add_node("Chatbot", "")
        self.graph_builder.add_edge(START, "Chatbot")
        self.graph_builder.add_edge("Chatbot", END)
        
        