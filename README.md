# Simple PDF Q&A RAG Bot 🤖📄

A beginner-friendly Retrieval-Augmented Generation (RAG) project built with Python and LangChain that allows you to load a PDF document and ask questions about its content using Google Gemini and ChromaDB.

## Tech Stack
* **Framework:** LangChain
* **LLM & Embeddings:** Google Gemini (`ChatGoogleGenerativeAI`, `GoogleGenerativeAIEmbeddings`)
* **Vector Database:** ChromaDB
* **Document Loader:** PyPDFLoader

## Prerequisites & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/simple-pdf-rag-chatbot.git](https://github.com/your-username/simple-pdf-rag-chatbot.git)
   cd simple-pdf-rag-chatbot


1. Install the required dependencies:


pip install langchain langchain-google-genai langchain-chroma langchain-community pypdf python-dotenv

2. Create a .env file in the root directory and add your Google Gemini API Key:

   GOOGLE_API_KEY="your_actual_api_key_here

3. Place your PDF file in the project folder and update the file name in the script if needed, then run:

   python testing.py


   