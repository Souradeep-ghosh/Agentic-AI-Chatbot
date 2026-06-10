import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit_ui.loadui import LoadStreamlitUI
from src.langgraph_agentic_ai.LLMs.groqllm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlit_ui.display_result import DisplayResultStreamlit


def load_agentic_ai_app():
    """It loads and runs the LangGraph AgenticAI Application Streamlit UI."""
    
    # Loading the Streamlit UI and getting user controls
    ui_loader = LoadStreamlitUI()
    user_input = ui_loader.load_streamlit_ui()

    # Validate user controls
    if not user_input:
        st.error("Error: Failed to load user input from the UI. Please check your configuration and try again.")
        return

    # Get user message
    user_message = st.chat_input("Enter your message here: ")
    
    # For the front-end
    if user_message:
        # Process user_message with your agent here
        try:
            #Configure the LLMs
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model= obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error : LLM model could not be initialized")
                return
            
            # Initialize and set up the graph based on use cases
            usecase = user_input.get("selected_usecase")
            
            # After getting the usecase, we will trigger the usecase
            if not usecase:
                st.error("Error: No use case selected")
                return
            
            # We will start building the graph
            graph_builder = GraphBuilder(model)
            try:  #Based on a specific usecase, which function should I call here
                graph= graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed. {e}")
                return
                
        except Exception as e :
            st.error(f"Error: LLM initialization failed. {e}")
            return
            
            
            