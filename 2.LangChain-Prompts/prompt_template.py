from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
)



template = PromptTemplate(
    template = 'Propose your love to {name} in 5 different languages in just 5-10 words in english transcript along with exact english translation. Include the {name} in the message.',
    input_variables = ['name']
)

prompt = template.invoke({'name' : 'Shankar'})

model = ChatHuggingFace(llm=llm)

print(prompt)
result = model.invoke(prompt)
print(result.content)