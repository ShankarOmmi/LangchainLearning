from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)    

prompt1 = PromptTemplate(
    template='Generate a simple recipe for {dish} without ingredients list in 5-10 steps.',
    input_variables=['dish']
)   

prompt2 = PromptTemplate(
    template = "Generate a simple list of ingredients required to make {dish} in 5-10 words.",
    input_variables=['dish']        
)

prompt3 = PromptTemplate(
    template = "Merge the following recipe and ingredients list into a single recipe with ingredients and steps. \n Recipe: {recipe} \n Ingredients: {ingredients}",
    input_variables=['recipe', 'ingredients']   
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'recipe': prompt1 | model | parser,
    'ingredients': prompt2 | model | parser         
})


merge_chain = prompt3 | model | parser 


dish = input('Enter the name of a dish: ')


result1 = parallel_chain.invoke({'dish': dish})
print("Recipe:\n", result1['recipe'])
print("Ingredients:\n", result1['ingredients'])

result = merge_chain.invoke(result1)

print("Final Result:\n", result)

parallel_chain.get_graph().print_ascii()