from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Simple Chain

"""
ask user for a topic
and generate a 5 interesting facts about the topic
"""
load_dotenv()

# prompt template
prompt=PromptTemplate(
template="""
Generate a 5 interesting facts about the topic {topic}
""",
input_variables=['topic']
)

# Model
model=ChatOpenAI()

# parser why we need parser? : because we want to get the output in a specific format 

parser=StrOutputParser()

# Chain
chain=prompt | model | parser
result=chain.invoke(input('Enter a topic:'))
print(result)

# # we can visualize the chain using the get_graph method

chain.get_graph().print_ascii()


