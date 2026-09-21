# GenAI Content Suite

A lightweight GenAI mini-project built using LangChain, LCEL (LangChain Expression Language), and Groq API to generate multi-platform social media content simultaneously.

## Features
- **Prompt Templates:** Uses dynamic prompts for different platforms.
- **Chat Models:** Powered by Groq API (`ChatGroq`).
- **Output Parsers:** Uses `StrOutputParser` for cleaning text outputs.
- **RunnableParallel:** Executes multiple prompt chains in parallel to generate both Twitter and LinkedIn posts at once.

## Tech Stack
- Python
- LangChain
- Groq SDK
- Python-Dotenv

## How to Run
1. Clone the repository.
2. Install dependencies (`pip install langchain langchain-groq python-dotenv`).
3. Create a `.env` file and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here