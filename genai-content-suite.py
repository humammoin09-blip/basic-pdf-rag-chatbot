from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-safeguard-20b")

twitter_post = PromptTemplate(
    input_variables={"topic"},
    template="Write a twitter post about{topic}",
)

linkedin_post = PromptTemplate(
    input_variables={"topic"},
    template="Write a linkedin post about{topic}",
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "twitter_post" : twitter_post | model | parser,
    "linkedin_post" : linkedin_post | model | parser,
})

result = parallel_chain.invoke({"topic": "AI Agents in 2026"})
print(result)