from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model=ChatOpenAI()

# 1st prompt-> detailed report
template1=PromptTemplate(
    template="""
write a detailed report on {topic}""",
input_variables=['topic']
)

# 2nd prompt-> summary
template2=PromptTemplate(
    template="""
write a 5 line summary on the following text. \n{text}""",
input_variables=['text']
)

# we will use chain concept  here

parser=StrOutputParser() # what it will do : it will parse the output of the model and return it as a string

chain=template1 | model | parser | template2 | model | parser  # this is how chain look this is pipeline 

result =chain.invoke({'topic' : 'black hole'})
print('--'*20)
print(result)

# this is also work with HuggingFacePipeline and local models 
