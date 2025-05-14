"""
Feedback->Model->Sentiment Analaysis->baed on sentiment-> response
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Give me sentiment of the Feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)
# for classification we need to use pydantic output parser to get the output in the form of pydantic object
prompt1=PromptTemplate(
    template="Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}" ,
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2=PromptTemplate(
template="Write an appropriate response for this positive feedback \n {feedback}",
input_variables=['feedback']
)
prompt3=PromptTemplate(
template="Write an appropriate response for this negative feedback \n {feedback}",
input_variables=['feedback']
)
classifier=prompt1 | model | parser2
# This is how branch chain is created
# branch_chain=RunnableBranch(
#     (Condition1,chain1),
#     (Condtition2,chain2),
#     default chain
# )

branch_chain=RunnableBranch(
    (lambda x: x.sentiment=='positive',prompt2 | model | parser),
    (lambda x: x.sentiment=='negative',prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find the Sentiment") # This is not chain it is a function so we need to convert it into runnable after that we can use it as a chain
)

chain=classifier | branch_chain
result=chain.invoke(input('Enter a feedback:'))
print(result)

chain.get_graph().print_ascii()



