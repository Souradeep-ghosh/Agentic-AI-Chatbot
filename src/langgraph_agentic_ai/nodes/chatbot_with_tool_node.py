from langgraph.graph import MessagesState

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
    def __init__(self, model):
        self.llm = model
        
    def create_chatbot(self, tools):
        """
        Binds tools to the LLM and returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state: MessagesState):
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
            
        return chatbot_node