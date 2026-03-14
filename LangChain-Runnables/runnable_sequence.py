from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableSequence

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.2-1B-Instruct",
    task = "text-generation"
)
model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Generate a sarcastic Reddit post about  {topic} in just 3 to 6 sentences',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a summary of the given reddit post in just 1 sentence\n {post}',
    input_variables = ['post']
)

topic = input("Enter the topic : ")
final_chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)


print(final_chain.invoke({'topic': topic}))