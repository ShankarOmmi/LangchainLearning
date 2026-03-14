from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Rama is the husband of Sita",
    "Arjuna is the husband of subhadra",
    "Mayabazar is a fictional story in Mahabharata",
]

result = embedding.embed_documents(documents)

print(str(result))