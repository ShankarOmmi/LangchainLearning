from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)


chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful assistant and an expert in {domain}'),
    ('human', 'Explain correctly without any assumptions and only based on the truths about {topic} in just 5-10 sentences.')
])

prompt = chat_template.invoke({'domain' : 'Indian Mythology', 'topic': 'Reason behind the killing of Raavana by Lord Rama'})

print(prompt)

result = model.invoke(prompt)
print(result.content)