import streamlit as st
import os

from src.langgraph_agentic_ai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖" + self.config.get_page_title(), layout= "wide")
        st.header("🤖 " + self.config.get_page_title())
        
        with st.sidebar:
            # Getting options from config file
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            # LLM selection box
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)
            
            if self.user_controls['selected_llm'] == "Groq":
                # Model selection box for Groq
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", model_options)
                # API key input for Groq
                self.user_controls['GROQ_API_KEY'] = st.text_input("GROQ API Key", type="password")
                # validating API key for Groq
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning(" 🚧 Please enter your GROQ API Key to proceed. Don't have? refer : https://console.groq.com/keys")
                    
            # Use case selection box
            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", usecase_options)
            
            # Adding Chatbot with tool using Tavily Web search tool
            if self.user_controls["selected_usecase"]== "Chatbot with Web-Search" or if self.user_controls["selected_usecase"] == "AI News" :
                os.environ["TAVILY_API_KEY"]= self.user_controls["TAVILY_API_KEY"]= st.session_state["TAVILY_API_KEY"]= st.text_input("TAVILY_API_KEY", type="password")
                
                # Validating API Key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("🚩Please enter your Tavily API Key to proceed. Don't have? refer: https://app.tavily.com/home")
            
            # For AI News
            if self.user_controls["selected_usecase"] == "AI News" :
                st.subheader(" 📰AI News Explorer")
                
                with st.sidebar: 
                    time_frame = st.selectbox(
                        " 🗓️Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index = 0
                    )
                # For fetching latest AI news, if this button is pressed 
                if st.button(" Fetch Latest AI News", use_container_width = True):
                    st.session_state.timeframe = time_frame
            
        return self.user_controls