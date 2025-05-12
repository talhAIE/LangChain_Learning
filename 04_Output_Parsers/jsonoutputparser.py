from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()

parser=JsonOutputParser()
template=PromptTemplate(
    template="""
give me name , age and city of a fictional person \n {format_instructions}
""",
input_variables=[],
partial_variables={'format_instructions':parser.get_format_instructions() }# partial variable because it filled before runtime Return a JSON object.
)

# # when we use json output parser we need to use the format_instructions (additional information how to parse the output from the model) 
# prompt1=template.format()

# result=model.invoke(prompt1)
# final_result=parser.parse(result.content)

# chain

chain=template | model | parser
result=chain.invoke({})
print(result)

# print(final_result)
# print(type(final_result))
# print(final_result['name'])

# jsonoutputparser problem is we can't use it for schema enforce 
# for schema enforce we have to use structured output parser option of schema enforce


