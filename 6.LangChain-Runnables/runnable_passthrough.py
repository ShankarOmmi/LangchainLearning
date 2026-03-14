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
    template = 'Tell me a joke about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain this joke {joke}',
    input_variables = ['joke']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser)
})
topic = input("Enter the topic : ")

final_chain = RunnableSequence( joke_gen_chain, parallel_chain)

final_result = final_chain.invoke({'topic':topic})
print("""The joke is :\n {} \n \n And the explanation is: \n {}""".format(final_result['joke'], final_result['explanation']))