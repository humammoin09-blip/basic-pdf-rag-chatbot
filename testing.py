from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnablePassthrough, RunnableLambda


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')
loader = PyPDFLoader("100-must-know-psychology-terms-perfected.pdf")
docs = loader.load(
    
)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
)
splitt_docs = text_splitter.split_documents(docs)
print(f"Total chunks created : {len(splitt_docs)}")

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

vector_store = Chroma.from_documents(
    documents=docs, embedding=embeddings, persist_directory="./chroma_db"
)

retriever = vector_store.as_retriever(
    search_type= "similarity", kwargs={"k": 4}
)

def format_docs(retrieved_docs):
  return "\n\n".join(doc.page_content for doc in retrieved_docs)

template = """You are a helpful assistant. Answer the question strictly based only on the provided context.
If you don't know the answer or it's not present in the context, just say "I don't know".

Context:
{context}

Question:
{question}
"""


prompt = PromptTemplate(
    input_variables=["context", "question"], template=template
)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough(),
})

rag_chain = parallel_chain | prompt | model | parser

if __name__ == "__main__":
  user_query = input("Why human behaviour changes: ")
  print("\nSearching and Generating response...\n")
  response = rag_chain.invoke(user_query)
  print("--- Answer ---")
  print(response)