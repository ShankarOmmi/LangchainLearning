from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name: str = Field(description='Name of the player')
    age: int = Field(gt=18, description='Age of the player')
    city: str = Field(description='City where the player is from')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a popular player of the {ipl_team} \n {format_instruction}',
    input_variables=['ipl_team'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

ipl_team = input('Enter the name of an IPL team: ')

final_result = chain.invoke({'ipl_team': ipl_team})

print(final_result)