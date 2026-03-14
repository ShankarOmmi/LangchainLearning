from langchain_community.document_loaders import WebBaseLoader
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
    template = 'Answer just the following question \n {question} from the following text \n {text} in just sentence with sharp answers',
    input_variables =['question', 'text']
)

parser = StrOutputParser()

url = 'https://en.wikipedia.org/wiki/Chennai_Super_Kings'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

question = input("Ask the question: ")
print(chain.invoke({'question': question, 'text': docs[0].page_content}))