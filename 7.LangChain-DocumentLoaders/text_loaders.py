from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Llama-3.2-1B-Instruct', 
    task = 'text-generation'
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template = 'Write a summary of the following poem in not more than strictly 5 sentences \n {poem}',
    input_variables =['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding = 'utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content[:200])
print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))