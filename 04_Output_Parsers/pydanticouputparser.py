# we will get name age city of the person from the model with data type constraints
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

model=ChatOpenAI()

class Person(BaseModel): # pydantic object
    name: str= Field(description='name of the person')
    age : int= Field(gt=18,description='age of the person')
    city: str=Field(description='Name of the city the person belongs to ')

parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template="""
Give me the name , age and city of a fictional {place} person \n {format_instruction}""",
input_variables=['place'],
partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt=template.invoke({'place':'pakistan'})
print(prompt)
result=model.invoke(prompt)
print(result.content)
# chain=template | model | parser
# result=chain.invoke({'place':'pakistan'})
# print(result)
# print(type(result))