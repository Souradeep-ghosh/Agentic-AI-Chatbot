import os
from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraph_agentic_ai/ui/uiconfigfile.ini"):
        # Build absolute path relative to this file's location
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(base_dir, "uiconfigfile.ini")
        
        self.config = ConfigParser()
        self.config.read(config_file)
        
    def get_page_title(self):
        return self.config.get("DEFAULT", "PAGE_TITLE")      
    
    def get_llm_options(self):
        return self.config.get("DEFAULT", "LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config.get("DEFAULT", "USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config.get("DEFAULT", "GROQ_MODEL_OPTIONS").split(", ")
    
    