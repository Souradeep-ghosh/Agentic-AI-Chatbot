from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,llm):
        """
        It initializes the AINewsNode with API keys for Tavily and GROQ.
        
        """
        self.tavily = TavilyClient()
        self.llm = llm
        
        # This is used to capture various steps like- fetch_news, news_summary etc. So that, it can be later used for steps shown
        self.state = {}
    
    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the specified frequency.
        
        Args:
            state(dict): The state dictionary containing 'frequency'.
            
        Returns:
            dict: Updated state with 'news_data' key conataining fetched news. 
        """
        
        frequency= state["messages"][0].content.lower()
        self.state["frequency"]= frequency
        time_range_map= {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'yearly' : 'y'}
        days_map= {'daily': 1, 'weekly': 7, 'monthly' : 31, 'yearly' : 366}
        
        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news in India and globally",
            topic= "news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results= 15,
            days=days_map[frequency]
            # include_domains= ["techcrunch.com", "venturebeat.com/ai", ...]
        )
            
        state['news_data']= response.get('results', [])
        self.state['news_data']= state['news_data']
        return state