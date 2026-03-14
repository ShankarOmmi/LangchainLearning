from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Rama is the husband of Sita",
    "Arjuna is the husband of subhadra",
    "Mayabazar is a fictional story in Mahabharata"
]

vector = embedding.embed_documents(documents)

print(str(vector))