# 🤖 Agentic AI Chatbot — Powered by LangGraph & Groq

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-1.2.4-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A stateful, multi-agent AI chatbot built with LangGraph's state-driven architecture — featuring web search, AI news summarization, and a modular design ready for RAG and beyond.**

[Features](#-features) • [Architecture](#-architecture) • [Getting Started](#-getting-started) • [Usage](#-usage) • [Project Structure](#-project-structure) • [Roadmap](#-roadmap)

</div>

---

## ✨ Features

| Use Case | Description | Tools Used |
|---|---|---|
| 🗨️ **Basic Chatbot** | Stateful conversational AI with message history | Groq LLM, LangGraph |
| 🌐 **Chatbot with Web Search** | Real-time web-augmented responses | Groq LLM, Tavily Search, LangGraph |
| 📰 **AI News Summarizer** | Fetches and summarizes latest AI news by frequency | Tavily News API, Groq LLM |

---

## 🏗️ Architecture

The project is built around **LangGraph's state-driven architecture**, where each use case is a compiled graph of nodes and edges.

```
User Input (Streamlit UI)
        │
        ▼
   LoadStreamlitUI
        │
        ▼
    GroqLLM Init
        │
        ▼
   GraphBuilder ──────────────────────────────────┐
        │                                          │
        ├── Basic Chatbot Graph                    │
        │     START → ChatbotNode → END            │
        │                                          │
        ├── Web Search Graph                       │
        │     START → ChatbotNode ⇄ ToolNode → END │
        │                                          │
        └── AI News Graph                          │
              START → FetchNews → Summarize        │
                    → SaveResult → END  ───────────┘
        │
        ▼
  DisplayResultStreamlit
        │
        ▼
   Streamlit Chat UI
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [Groq API Key](https://console.groq.com/keys) (free)
- A [Tavily API Key](https://app.tavily.com) (free tier available)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Souradeep-ghosh/Agentic-AI-Chatbot.git
cd Agentic-AI-Chatbot
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv AgentChat
AgentChat\Scripts\activate

# macOS/Linux
python -m venv AgentChat
source AgentChat/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

> 💡 Alternatively, you can enter API keys directly in the Streamlit sidebar at runtime.

**5. Run the application**
```bash
streamlit run app.py
```

---

## 🖥️ Usage

### Basic Chatbot
1. Select **Groq** as the LLM provider
2. Choose a model (e.g. `llama-3.3-70b-versatile`)
3. Enter your Groq API key
4. Select **Basic Chatbot** as the use case
5. Type your message and hit Enter

### Chatbot with Web Search
1. Follow steps 1–3 above
2. Select **Chatbot with Web Search**
3. Enter your Tavily API key
4. Ask any question requiring up-to-date information

### AI News Summarizer
1. Follow steps 1–3 above
2. Select **AI News**
3. Enter your Tavily API key
4. Choose a time frame: Daily / Weekly / Monthly
5. Click **Fetch Latest AI News**

---

## 📁 Project Structure

```
Agentic-AI-Chatbot/
├── app.py                          # Entry point
├── requirements.txt                # Dependencies
├── .gitignore
├── README.md
├── AINews/                         # Auto-generated news summaries (markdown)
└── src/
    └── langgraph_agentic_ai/
        ├── main.py                 # App orchestrator
        ├── LLMs/
        │   └── groqllm.py          # Groq LLM initialization
        ├── graph/
        │   └── graph_builder.py    # LangGraph graph builder
        ├── nodes/
        │   ├── basic_chatbot_node.py       # Basic chatbot node
        │   ├── chatbot_with_tool_node.py   # Tool-augmented chatbot node
        │   └── ai_news_node.py             # AI news fetch + summarize node
        ├── tools/
        │   └── search_tool.py      # Tavily search tool + ToolNode
        ├── state/
        │   └── state.py            # LangGraph MessagesState definition
        └── ui/
            ├── uiconfigfile.py     # Config parser
            ├── uiconfigfile.ini    # UI configuration (titles, models, usecases)
            └── streamlit_ui/
                ├── loadui.py           # Streamlit sidebar + controls
                └── display_result.py  # Chat result renderer
```

---

## 🧠 Supported Groq Models

| Model | Model ID | Best For |
|---|---|---|
| LLaMA 3.3 70B | `llama-3.3-70b-versatile` | Complex reasoning |
| LLaMA 3.1 8B | `llama-3.1-8b-instant` | Fast responses |
| Gemma 2 9B | `gemma2-9b-it` | Instruction following |

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| **LLM Provider** | [Groq](https://groq.com) |
| **Agent Framework** | [LangGraph](https://langchain-ai.github.io/langgraph/) |
| **LLM Abstraction** | [LangChain](https://langchain.com) |
| **Web Search** | [Tavily](https://tavily.com) |
| **Vector Database** | [Pinecone](https://pinecone.io) *(coming soon)* |
| **UI** | [Streamlit](https://streamlit.io) |
| **Language** | Python 3.10+ |

---

## 🗺️ Roadmap

- [x] Basic Chatbot with Groq LLM
- [x] Chatbot with Tavily Web Search
- [x] AI News Summarizer (Daily / Weekly / Monthly)
- [ ] RAG Chatbot with Pinecone vector store
- [ ] Document Q&A (PDF / DOCX upload)
- [ ] Multi-agent collaboration
- [ ] Memory persistence across sessions
- [ ] OpenAI model support
- [ ] Deploy to Streamlit Cloud

---
## 👨‍💻 Author

**Souradeep Ghosh**
- 📧 Connect on [LinkedIn](https://www.linkedin.com/in/souradeep-ghosh-165802150/)
- 🐙 [GitHub](https://github.com/Souradeep-ghosh)
- 🤗 [Hugging Face](https://huggingface.co/Sg31Ghosh)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an [issue](https://github.com/Souradeep-ghosh/Agentic-AI-Chatbot/issues) for bugs or feature requests
- Submit a pull request with improvements

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
Built with ❤️ using LangGraph, Groq & Streamlit
</div>