import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit_ui.loadui import LoadStreamlitUI

def load_agentic_ai_app():
    """It loads and runs the LangGraph AgenticAI Application Streamlit UI."""
    
    # Loading the Streamlit UI and getting user controls
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_streamlit_ui()

    # Validate user controls
    if not user_controls:
        st.error("Error: Failed to load user input from the UI. Please check your configuration and try again.")
        return

    # Get user message
    user_message = st.chat_input("Enter your message here: ")
    
    if user_message:
        # Process user_message with your agent here
        pass