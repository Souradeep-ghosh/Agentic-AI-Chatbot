import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        
    def display_result_on_ui(self):
        usecase = self.usecase          # ← must be indented with 8 spaces
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                for value in event.values():
                    last_message = value["messages"]
                    
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        if isinstance(last_message, list):
                            st.write(last_message[-1].content)
                        else:
                            st.write(last_message.content)