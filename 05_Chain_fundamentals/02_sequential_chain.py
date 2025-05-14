from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


'''
topic->LLM->report Generate->LLM->Summary
'''

# Prompt 1 for report generation

prompt_1=PromptTemplate(
    template="""
Generate a detailed report about the topic {topic}
""",
input_variables=['topic']
)

# Prompt 2 for summary generation 

prompt_2=PromptTemplate(
template="""
Generate a 5 pointer summary from the following text \n {text}
""",
input_variables=['text']
)

# Model
model=ChatOpenAI()

# Parser
parser=StrOutputParser()

#Chain
chain= prompt_1 | model | parser | prompt_2 | model | parser

result=chain.invoke(input('Enter a topic:'))
print(result)

# visualize the chain
chain.get_graph().print_ascii()
