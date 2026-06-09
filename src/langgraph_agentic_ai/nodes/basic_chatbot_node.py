from src.langgraph_agentic_ai.state.state import State




class BasicChatbotNode:
    """
    This has basic chatbot logic implementation
    
    """
    def __init__(self,model):
        self.llm=model
        
    def process(self, state:State)-> dict:
        """
        It processes the input state and generates a chatbot response
        """
        return {"messages": self.llm.invoke(state['messages'])}
        