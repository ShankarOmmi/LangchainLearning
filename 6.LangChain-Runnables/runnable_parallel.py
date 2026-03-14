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
    template = 'Generate a formal LinkedIn post about {topic} in just 3 to 6 sentences',
    input_variables = ['topic']
)


parallel_chain = RunnableParallel({
    'post1' : RunnableSequence(prompt1, model, parser),
    'post2' : RunnableSequence(prompt2, model, parser)
})
topic = input("Enter the topic : ")


final_result = parallel_chain.invoke({'topic':topic})
print("""Reddit post is :\n {} \n \n And the LinkedIn post is: \n {}""".format(final_result['post1'], final_result['post2']))