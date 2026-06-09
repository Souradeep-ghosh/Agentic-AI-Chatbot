from langgraph.graph import StateGraph
from src.langgraph_agentic_ai.state.state import State
from langgraph.graph import START, END
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder: 
    def __init__(self, model):
        self.llm = model
        self.graph_builder= StateGraph(State)
        
        
    def basic_chatbot_build_graph(self):
        """This method builds a basic chatbot graph using the StateGraph class. 
        It defines the structure of the graph and how messages are processed.
        
        Returns:
            StateGraph: An instance of the StateGraph class representing the chatbot graph.
        """
        self.basic_chatbot_node= BasicChatbotNode(self.llm)
        
        self.graph_builder.add_node("Chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "Chatbot")
        self.graph_builder.add_edge("Chatbot", END)
        
        
    def setup_graph(self, usecase: str):
        """
        It sets up the graph for the selected use case. 
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            
        else:
            raise ValueError(f"Unknown usecase: {usecase}")
            
        return self.graph_builder.compile()
        
        